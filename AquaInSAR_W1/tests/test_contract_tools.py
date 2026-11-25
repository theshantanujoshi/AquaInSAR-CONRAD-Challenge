"""Offline, deterministic tests for W1 validation logic.

All CSV fixtures below are SYNTHETIC_TEST software fixtures. They exercise schema
validation only. They are not AquaInSAR observations and no scientific result is
computed from them.
"""

from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT / "src"))

from aquainsar_w1.contract_tools import (  # noqa: E402
    ContractError,
    load_contract,
    validate_contract_structure,
    validate_dataset_csv,
)

CONTRACT_PATH = PACKAGE_ROOT / "contracts" / "AquaInSAR_Data_Contract_v0.9.0.json"
DATASET_ID = "AQS-GW-CGWB-WELL"

HEADER = [
    "observation_id",
    "station_id",
    "observation_date",
    "longitude",
    "latitude",
    "crs",
    "measurement_value",
    "measurement_unit",
    "measurement_type",
    "quality_flag",
    "source_reference",
    "retrieval_date",
    "processing_lineage",
    "dataset_id",
]

VALID_ROW = [
    "SYNTHETIC_TEST-GW-001",
    "SYNTHETIC_TEST-ST-01",
    "2024-05-01",
    "79.5",
    "26.8",
    "EPSG:4326",
    "12.4",
    "m_bgl",
    "WATER_LEVEL_DEPTH_BGL",
    "VALID",
    "SYNTHETIC_TEST source",
    "2026-11-24",
    "SYNTHETIC_TEST lineage",
    "AQS-GW-CGWB-WELL",
]


def make_csv(directory: Path, name: str, rows: list[list[str]], header: list[str] | None = None) -> Path:
    path = directory / name
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header if header is not None else HEADER)
        writer.writerows(rows)
    return path


class ContractStructureTests(unittest.TestCase):
    def test_contract_loads_and_is_structurally_valid(self):
        contract = load_contract(CONTRACT_PATH)
        issues = validate_contract_structure(contract)
        self.assertEqual([], issues, f"unexpected contract issues: {issues}")

    def test_report_is_json_serialisable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "ok.csv", [VALID_ROW])
            report = validate_dataset_csv(path, DATASET_ID, load_contract(CONTRACT_PATH))
            payload = json.loads(json.dumps(report.to_dict()))
            self.assertEqual("PASS", payload["status"])
            self.assertEqual(1, payload["rows_read"])

    def test_unknown_dataset_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "ok.csv", [VALID_ROW])
            with self.assertRaises(ContractError):
                validate_dataset_csv(path, "AQS-NOT-A-DATASET", load_contract(CONTRACT_PATH))


class CsvValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = load_contract(CONTRACT_PATH)

    def rules(self, report) -> list[str]:
        return [issue.rule_id for issue in report.issues]

    def test_valid_row_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "ok.csv", [VALID_ROW])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertEqual("PASS", report.status)
            self.assertEqual(0, report.error_count)

    def test_missing_required_column_is_error(self):
        index = HEADER.index("measurement_unit")
        header = HEADER[:index] + HEADER[index + 1:]
        row = VALID_ROW[:index] + VALID_ROW[index + 1:]
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "missing.csv", [row], header)
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertEqual("FAIL", report.status)
            self.assertIn("VR-001", self.rules(report))

    def test_invalid_date_is_error(self):
        row = list(VALID_ROW)
        row[2] = "01/05/2024"
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "date.csv", [row])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-004", self.rules(report))

    def test_duplicate_primary_key_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "dup.csv", [VALID_ROW, list(VALID_ROW)])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-008", self.rules(report))
            self.assertEqual(2, report.rows_read)

    def test_duplicate_station_date_alternate_key_is_error(self):
        second = list(VALID_ROW)
        second[0] = "SYNTHETIC_TEST-GW-002"
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "dup_alt.csv", [VALID_ROW, second])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-008", self.rules(report))

    def test_out_of_range_coordinate_is_error(self):
        row = list(VALID_ROW)
        row[3] = "200.0"
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "coord.csv", [row])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-005", self.rules(report))

    def test_empty_non_nullable_field_is_error(self):
        row = list(VALID_ROW)
        row[1] = ""
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "empty.csv", [row])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-003", self.rules(report))

    def test_invalid_category_is_error(self):
        row = list(VALID_ROW)
        row[8] = "NOT_A_REAL_TYPE"
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "category.csv", [row])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-006", self.rules(report))

    def test_nonfinite_number_is_error(self):
        row = list(VALID_ROW)
        row[6] = "NaN"
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "nan.csv", [row])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-004", self.rules(report))

    def test_missing_unit_is_error(self):
        row = list(VALID_ROW)
        row[7] = ""
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "nounit.csv", [row])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertIn("VR-009", self.rules(report))

    def test_unexpected_column_is_warning_only(self):
        header = HEADER + ["unexpected_field"]
        row = VALID_ROW + ["extra"]
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "extra.csv", [row], header)
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertEqual("PASS_WITH_WARNINGS", report.status)
            self.assertEqual(0, report.error_count)
            self.assertIn("VR-002", self.rules(report))

    def test_empty_file_is_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "emptyrows.csv", [])
            report = validate_dataset_csv(path, DATASET_ID, self.contract)
            self.assertEqual(0, report.rows_read)
            self.assertIn("VR-002", self.rules(report))
            self.assertNotEqual("FAIL", report.status)


if __name__ == "__main__":
    unittest.main()
