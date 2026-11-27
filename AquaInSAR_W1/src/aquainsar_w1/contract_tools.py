"""Contract-consistency and CSV validation tools for AquaInSAR W1.

Design constraints (from AQS-DC v0.9.0 and ADR-0001):

* Standard library only. No third-party runtime dependency.
* Validation is read-only: inputs are never modified, filtered, imputed or repaired.
* Every problem is returned as a structured Issue with rule id, severity, row and field.
* This module does not perform scientific analysis. Passing validation is not evidence
  that a dataset is scientifically valid, comparable to another dataset, or suitable for
  validation or prediction.

Command line::

    python -m aquainsar_w1.contract_tools check-contract --contract PATH
    python -m aquainsar_w1.contract_tools validate-csv --contract PATH \
        --dataset AQS-GW-CGWB-WELL --csv PATH
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Iterable

__all__ = [
    "ContractError",
    "Issue",
    "ValidationReport",
    "load_contract",
    "validate_contract_structure",
    "validate_dataset_csv",
]


class ContractError(ValueError):
    """Raised when the contract itself cannot be used for validation."""


@dataclass(frozen=True)
class Issue:
    severity: str
    rule_id: str
    dataset_id: str
    row: int | None
    field: str | None
    message: str


@dataclass
class ValidationReport:
    dataset_id: str
    csv_path: str
    contract_id: str
    contract_version: str
    rows_read: int
    issues: list[Issue] = field(default_factory=list)
    status: str = "PASS"

    @property
    def error_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity == "ERROR")

    @property
    def warning_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity == "WARNING")

    @property
    def issue_count(self) -> int:
        return len(self.issues)

    def finalise(self) -> "ValidationReport":
        if self.error_count:
            self.status = "FAIL"
        elif self.warning_count:
            self.status = "PASS_WITH_WARNINGS"
        else:
            self.status = "PASS"
        return self

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["issues"] = [asdict(issue) for issue in self.issues]
        data["error_count"] = self.error_count
        data["warning_count"] = self.warning_count
        data["issue_count"] = self.issue_count
        return data


def _parse_typed_value(raw: str, value_type: str) -> None:
    """Raise ValueError when *raw* does not parse as the declared type."""
    if value_type == "string":
        return
    if value_type == "date":
        date.fromisoformat(raw)
        return
    if value_type == "datetime":
        normalised = raw[:-1] + "+00:00" if raw.endswith("Z") else raw
        datetime.fromisoformat(normalised)
        return
    if value_type in {"decimal", "integer"}:
        try:
            number = Decimal(raw)
        except InvalidOperation as exc:  # pragma: no cover - defensive
            raise ValueError("not a decimal number") from exc
        if not number.is_finite():
            raise ValueError("non-finite numbers are not measurements")
        if value_type == "integer" and number != number.to_integral_value():
            raise ValueError("not an integer")
        return
    raise ValueError(f"unsupported field type: {value_type}")


_SUPPORTED_TYPES = {"string", "date", "datetime", "decimal", "integer"}


def load_contract(path: str | Path) -> dict[str, Any]:
    """Load and minimally check the JSON contract."""
    contract_path = Path(path)
    try:
        with contract_path.open("r", encoding="utf-8") as handle:
            contract = json.load(handle)
    except FileNotFoundError as exc:
        raise ContractError(f"contract not found: {contract_path}") from exc
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON in {contract_path}: {exc}") from exc
    if not isinstance(contract, dict):
        raise ContractError("contract root must be a JSON object")
    for key in ("contract", "conventions", "validation_rules", "datasets"):
        if key not in contract:
            raise ContractError(f"contract missing required section: {key}")
    return contract


def _metadata_issues(contract: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    required = contract["conventions"].get("provenance", {}).get(
        "required_metadata_fields", []
    )
    for dataset in contract["datasets"]:
        dataset_id = dataset.get("dataset_id", "<missing>")
        for key in required:
            value = dataset.get(key)
            if value is None or value == "" or value == []:
                issues.append(
                    Issue(
                        "ERROR",
                        "VR-010",
                        dataset_id,
                        None,
                        key,
                        f"required dataset metadata '{key}' is missing or empty",
                    )
                )
    record_fields = contract["conventions"].get("provenance", {}).get(
        "required_record_fields", []
    )
    for dataset in contract["datasets"]:
        schema = dataset.get("schema")
        if not schema:
            continue
        names = {f.get("name") for f in schema.get("fields", [])}
        for key in record_fields:
            if key not in names:
                issues.append(
                    Issue(
                        "ERROR",
                        "VR-010",
                        dataset.get("dataset_id", "<missing>"),
                        None,
                        key,
                        f"required record provenance field '{key}' is absent from schema",
                    )
                )
    return issues


def validate_contract_structure(contract: dict[str, Any]) -> list[Issue]:
    """Check internal consistency of the contract (VR-011, VR-010)."""
    issues: list[Issue] = []
    seen_datasets: set[str] = set()
    seen_rules: set[str] = set()

    for rule in contract["validation_rules"]:
        rule_id = rule.get("id")
        if not rule_id or rule_id in seen_rules:
            issues.append(
                Issue("ERROR", "VR-011", "<contract>", None, None,
                      f"duplicate or missing validation rule id: {rule_id}")
            )
        else:
            seen_rules.add(rule_id)
        if rule.get("severity") not in {"ERROR", "WARNING"}:
            issues.append(
                Issue("ERROR", "VR-011", "<contract>", None, None,
                      f"rule {rule_id} has invalid severity")
            )

    for dataset in contract["datasets"]:
        dataset_id = dataset.get("dataset_id")
        if not dataset_id or dataset_id in seen_datasets:
            issues.append(
                Issue("ERROR", "VR-011", dataset_id or "<missing>", None, None,
                      "duplicate or missing dataset_id")
            )
        else:
            seen_datasets.add(dataset_id)

        schema = dataset.get("schema")
        if not schema:
            continue
        fields = schema.get("fields", [])
        if not fields:
            issues.append(
                Issue("ERROR", "VR-011", dataset_id, None, None,
                      "active schema has no fields")
            )
            continue
        names: set[str] = set()
        quality_definition = next(
            (definition for definition in fields if definition.get("name") == "quality_flag"),
            None,
        )
        quality_allowed = set(quality_definition.get("allowed_values", [])) if quality_definition else set()
        for definition in fields:
            name = definition.get("name")
            if not name or name in names:
                issues.append(
                    Issue("ERROR", "VR-011", dataset_id, None, name,
                          "duplicate or missing field name")
                )
                continue
            names.add(name)
            value_type = definition.get("type")
            if value_type not in _SUPPORTED_TYPES:
                issues.append(
                    Issue("ERROR", "VR-011", dataset_id, None, name,
                          f"unsupported type '{value_type}'")
                )
            if not isinstance(definition.get("required"), bool) or not isinstance(
                definition.get("nullable"), bool
            ):
                issues.append(
                    Issue("ERROR", "VR-011", dataset_id, None, name,
                          "required and nullable must be booleans")
                )
            if "allowed_values" in definition:
                allowed = definition["allowed_values"]
                if not isinstance(allowed, list) or not allowed:
                    issues.append(
                        Issue("ERROR", "VR-011", dataset_id, None, name,
                              "allowed_values must be a non-empty list")
                    )
            if "pattern" in definition:
                try:
                    re.compile(definition["pattern"])
                except re.error as exc:
                    issues.append(
                        Issue("ERROR", "VR-011", dataset_id, None, name,
                              f"invalid regex pattern: {exc}")
                    )
            minimum = definition.get("minimum")
            maximum = definition.get("maximum")
            if minimum is not None and maximum is not None and minimum > maximum:
                issues.append(
                    Issue("ERROR", "VR-011", dataset_id, None, name,
                          "minimum is greater than maximum")
                )
            if "nullable_when_quality_flags" in definition:
                conditional_flags = definition["nullable_when_quality_flags"]
                if not isinstance(conditional_flags, list) or not all(
                    isinstance(flag, str) for flag in conditional_flags
                ):
                    issues.append(
                        Issue("ERROR", "VR-011", dataset_id, None, name,
                              "nullable_when_quality_flags must be a list of strings")
                    )
                elif quality_allowed and not set(conditional_flags).issubset(quality_allowed):
                    issues.append(
                        Issue("ERROR", "VR-011", dataset_id, None, name,
                              "nullable_when_quality_flags contains flags not allowed for this dataset")
                    )

        has_start = "period_start" in names
        has_end = "period_end" in names
        if has_start != has_end:
            issues.append(
                Issue("ERROR", "VR-011", dataset_id, None, None,
                      "period_start and period_end must both be declared")
            )

        for constraint in schema.get("unique_constraints", []):
            if not constraint or not set(constraint).issubset(names):
                issues.append(
                    Issue("ERROR", "VR-011", dataset_id, None, None,
                          f"unique constraint references unknown field(s): {constraint}")
                )
        for pair in schema.get("unit_pairs", []):
            if len(pair) != 2 or not set(pair).issubset(names):
                issues.append(
                    Issue("ERROR", "VR-011", dataset_id, None, None,
                          f"unit pair references unknown field(s): {pair}")
                )

    issues.extend(_metadata_issues(contract))
    return issues


def _find_dataset(contract: dict[str, Any], dataset_id: str) -> dict[str, Any]:
    for dataset in contract["datasets"]:
        if dataset.get("dataset_id") == dataset_id:
            return dataset
    raise ContractError(f"unknown dataset_id: {dataset_id}")


def validate_dataset_csv(
    csv_path: str | Path, dataset_id: str, contract: dict[str, Any]
) -> ValidationReport:
    """Validate one CSV against its contract schema. Never modifies the input."""
    path = Path(csv_path)
    dataset = _find_dataset(contract, dataset_id)
    schema = dataset.get("schema")
    if not schema or not schema.get("fields"):
        raise ContractError(f"dataset {dataset_id} has no active CSV schema")

    header_contract = contract["contract"]
    report = ValidationReport(
        dataset_id=dataset_id,
        csv_path=str(path),
        contract_id=header_contract.get("id", "UNKNOWN"),
        contract_version=header_contract.get("version", "UNKNOWN"),
        rows_read=0,
    )

    try:
        handle = path.open("r", encoding="utf-8-sig", newline="")
    except FileNotFoundError as exc:
        report.issues.append(
            Issue("ERROR", "VR-001", dataset_id, None, None,
                  f"CSV file not found: {path}")
        )
        return report.finalise()

    with handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        field_defs = schema["fields"]
        fields_by_name = {definition["name"]: definition for definition in field_defs}

        for definition in field_defs:
            if definition["required"] and definition["name"] not in header:
                report.issues.append(
                    Issue("ERROR", "VR-001", dataset_id, None, definition["name"],
                          "required column is missing from CSV header")
                )
        extra = sorted(set(header) - set(fields_by_name))
        if extra:
            report.issues.append(
                Issue("WARNING", "VR-002", dataset_id, None, None,
                      f"undefined column(s) in CSV header: {', '.join(extra)}")
            )
        if len(header) != len(set(header)):
            report.issues.append(
                Issue("WARNING", "VR-002", dataset_id, None, None,
                      "CSV header contains duplicate column names")
            )

        conventions = contract["conventions"]
        coord_ranges = {
            "longitude": conventions.get("coordinates", {}).get("longitude_range"),
            "latitude": conventions.get("coordinates", {}).get("latitude_range"),
        }
        quality_conventions = conventions.get("quality", {})
        no_value_flags = set(quality_conventions.get("no_value_flags", []))
        value_required_flags = set(quality_conventions.get("value_required_flags", []))
        reason_codes = set(
            conventions.get("missing_values", {}).get("reason_codes", [])
        )

        seen_keys: dict[tuple[str, ...], tuple[int, str]] = {}
        for row_number, row in enumerate(reader, start=1):
            report.rows_read += 1
            present: dict[str, str] = {}
            raw_quality = row.get("quality_flag")
            quality_value = raw_quality.strip() if isinstance(raw_quality, str) else ""
            for definition in field_defs:
                name = definition["name"]
                raw = row.get(name)
                value = raw.strip() if isinstance(raw, str) else ""
                present[name] = value
                conditional_flags = set(definition.get("nullable_when_quality_flags", []))
                conditionally_nullable = bool(conditional_flags) and quality_value in conditional_flags
                if not value:
                    if definition["required"] and not definition["nullable"] and not conditionally_nullable:
                        report.issues.append(
                            Issue("ERROR", "VR-003", dataset_id, row_number, name,
                                  "empty value in non-nullable field")
                        )
                    continue

                value_type = definition["type"]
                try:
                    _parse_typed_value(value, value_type)
                except (ValueError, TypeError) as exc:
                    report.issues.append(
                        Issue("ERROR", "VR-004", dataset_id, row_number, name,
                              f"value {value!r} does not parse as {value_type}: {exc}")
                    )
                    continue

                if value_type in {"decimal", "integer"}:
                    number = Decimal(value)
                    minimum = definition.get("minimum")
                    maximum = definition.get("maximum")
                    if minimum is not None and number < Decimal(str(minimum)):
                        report.issues.append(
                            Issue("ERROR", "VR-004", dataset_id, row_number, name,
                                  f"value {value} is below minimum {minimum}")
                        )
                    if maximum is not None and number > Decimal(str(maximum)):
                        report.issues.append(
                            Issue("ERROR", "VR-004", dataset_id, row_number, name,
                                  f"value {value} is above maximum {maximum}")
                        )

                allowed = definition.get("allowed_values")
                if allowed is not None and value not in allowed:
                    report.issues.append(
                        Issue("ERROR", "VR-006", dataset_id, row_number, name,
                              f"value {value!r} is not in allowed_values {allowed}")
                    )
                pattern = definition.get("pattern")
                if pattern is not None and re.fullmatch(pattern, value) is None:
                    report.issues.append(
                        Issue("ERROR", "VR-007", dataset_id, row_number, name,
                              f"value {value!r} does not match pattern {pattern}")
                    )
                if name in coord_ranges:
                    bounds = coord_ranges[name]
                    if bounds:
                        coordinate_value = Decimal(value)
                        if not (Decimal(str(bounds[0])) <= coordinate_value <= Decimal(str(bounds[1]))):
                            report.issues.append(
                                Issue("ERROR", "VR-005", dataset_id, row_number, name,
                                      f"coordinate {value} outside global range {bounds}")
                            )

            for value_field, unit_field in schema.get("unit_pairs", []):
                if present.get(value_field) and not present.get(unit_field):
                    report.issues.append(
                        Issue("ERROR", "VR-009", dataset_id, row_number, unit_field,
                              f"unit missing while {value_field} is present")
                    )

            # VR-012/VR-013: a value is present only for value-required quality flags;
            # no-value flags require an explicit reason for the empty measurement.
            for definition in field_defs:
                conditional_flags = definition.get("nullable_when_quality_flags")
                if not conditional_flags:
                    continue
                value_field = definition["name"]
                if quality_value in conditional_flags and present.get(value_field):
                    report.issues.append(
                        Issue("ERROR", "VR-012", dataset_id, row_number, value_field,
                              f"value present while quality_flag={quality_value} means no reliable value")
                    )
                if quality_value not in no_value_flags or present.get(value_field):
                    continue
                reason_present = bool(present.get("missing_reason"))
                if not reason_present and present.get("missing_reason_map"):
                    try:
                        parsed_reason_map = json.loads(present["missing_reason_map"])
                        if (
                            isinstance(parsed_reason_map, dict)
                            and parsed_reason_map.get(value_field) in reason_codes
                        ):
                            reason_present = True
                    except (ValueError, TypeError):
                        pass
                if not reason_present:
                    report.issues.append(
                        Issue("ERROR", "VR-013", dataset_id, row_number, value_field,
                              f"no-value quality_flag={quality_value} requires a reason for empty {value_field}")
                    )

            expected_id = dataset["dataset_id"]
            actual_id = present.get("dataset_id", "")
            if actual_id and actual_id != expected_id and not actual_id.startswith(expected_id + "-v"):
                report.issues.append(
                    Issue("ERROR", "VR-014", dataset_id, row_number, "dataset_id",
                          f"row dataset_id {actual_id!r} does not match selected dataset {expected_id!r}")
                )

            period_start = present.get("period_start", "")
            period_end = present.get("period_end", "")
            if period_start and period_end:
                try:
                    if date.fromisoformat(period_end) < date.fromisoformat(period_start):
                        report.issues.append(
                            Issue("ERROR", "VR-015", dataset_id, row_number, "period_end",
                                  "period_end precedes period_start")
                        )
                except ValueError:
                    pass  # parse failures are already reported as VR-004

            reason_map_raw = present.get("missing_reason_map", "")
            reason_map: dict[str, str] = {}
            if reason_map_raw:
                try:
                    parsed_map = json.loads(reason_map_raw)
                    if not isinstance(parsed_map, dict):
                        raise ValueError("not a JSON object")
                    for key, value in parsed_map.items():
                        if key not in fields_by_name or value not in reason_codes:
                            raise ValueError("unknown field or invalid reason code")
                    reason_map = parsed_map
                except (ValueError, TypeError) as exc:
                    report.issues.append(
                        Issue("ERROR", "VR-016", dataset_id, row_number, "missing_reason_map",
                              f"invalid missing_reason_map: {exc}")
                    )
            empty_optional = [
                definition["name"]
                for definition in field_defs
                if definition["name"] in header
                and not definition["required"]
                and definition["name"] not in {"missing_reason", "missing_reason_map"}
                and not present.get(definition["name"])
            ]
            if len(empty_optional) > 1 and not reason_map:
                report.issues.append(
                    Issue("ERROR", "VR-016", dataset_id, row_number, "missing_reason_map",
                          "multiple empty optional fields require per-field missing_reason_map: "
                          + ", ".join(empty_optional))
                )

            for constraint in schema.get("unique_constraints", []):
                key = tuple(present.get(name, "") for name in constraint)
                if key in seen_keys:
                    first_row = seen_keys[key][0]
                    report.issues.append(
                        Issue("ERROR", "VR-008", dataset_id, row_number,
                              ", ".join(constraint),
                              f"duplicate of unique constraint {list(constraint)} "
                              f"first seen at data row {first_row}")
                    )
                else:
                    seen_keys[key] = (row_number, ",".join(constraint))

        if report.rows_read == 0:
            report.issues.append(
                Issue("WARNING", "VR-002", dataset_id, None, None,
                      "CSV contains no data rows")
            )

    return report.finalise()


def _print_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aquainsar_w1.contract_tools",
        description="AquaInSAR W1 contract and CSV validation (no scientific analysis).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check-contract", help="check contract internal consistency")
    check.add_argument("--contract", required=True)

    validate = subparsers.add_parser("validate-csv", help="validate a CSV against a dataset schema")
    validate.add_argument("--contract", required=True)
    validate.add_argument("--dataset", required=True)
    validate.add_argument("--csv", required=True)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        contract = load_contract(args.contract)
    except ContractError as exc:
        print(f"CONTRACT ERROR: {exc}", file=sys.stderr)
        return 2

    if args.command == "check-contract":
        issues = validate_contract_structure(contract)
        payload = {
            "contract_id": contract["contract"].get("id"),
            "contract_version": contract["contract"].get("version"),
            "status": "FAIL" if any(i.severity == "ERROR" for i in issues) else "PASS",
            "issues": [asdict(issue) for issue in issues],
        }
        _print_json(payload)
        return 1 if payload["status"] == "FAIL" else 0

    try:
        report = validate_dataset_csv(args.csv, args.dataset, contract)
    except ContractError as exc:
        print(f"CONTRACT ERROR: {exc}", file=sys.stderr)
        return 2
    _print_json(report.to_dict())
    return 1 if report.status == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
