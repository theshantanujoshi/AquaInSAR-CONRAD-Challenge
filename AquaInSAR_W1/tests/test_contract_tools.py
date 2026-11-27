"""Offline, deterministic tests for W1 validation logic.

All CSV fixtures below are SYNTHETIC_TEST software fixtures. They exercise schema
validation only. They are not AquaInSAR observations and no scientific result is
computed from them.
"""

from __future__ import annotations

import copy
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

INSAR_HEADER = [
    "observation_id", "dataset_id", "pixel_id", "longitude", "latitude", "crs",
    "acquisition_date", "platform", "relative_orbit", "pass_direction",
    "measurement_convention", "deformation_value", "deformation_unit",
    "quality_flag", "source_reference", "processing_lineage", "missing_reason",
]

INSAR_ROW = [
    "SYNTHETIC_TEST-INSAR-001", "AQS-INSAR-S1-DISPLACEMENT", "PIXEL-1",
    "79.5", "26.8", "EPSG:4326", "2024-05-01", "SENTINEL-1A", "65",
    "ASCENDING", "LOS", "-3.2", "mm", "VALID", "SYNTHETIC_TEST source",
    "SYNTHETIC_TEST lineage", "",
]

RAIN_HEADER = [
    "observation_id", "dataset_id", "location_id", "observation_date",
    "period_start", "period_end", "longitude", "latitude", "crs",
    "rainfall_value", "rainfall_unit", "accumulation_period",
    "source_spatial_support", "quality_flag", "source_reference",
    "retrieval_date", "processing_lineage",
]

RAIN_ROW = [
    "SYNTHETIC_TEST-RAIN-001", "AQS-RAIN-IMD-DISTRICT", "DIST-1",
    "2024-06-01", "2024-06-01", "2024-06-30", "79.5", "26.8", "EPSG:4326",
    "125.4", "mm", "MONTH", "DISTRICT_AGGREGATE", "VALID",
    "SYNTHETIC_TEST source", "2026-11-27", "SYNTHETIC_TEST lineage",
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


class ContractStructureNegativeTests(unittest.TestCase):
    """The contract checker must fail on malformed contracts, not only succeed."""

    def setUp(self):
        self.contract = copy.deepcopy(load_contract(CONTRACT_PATH))

    def test_duplicate_dataset_ids_detected(self):
        self.contract["datasets"].append(copy.deepcopy(self.contract["datasets"][0]))
        issues = validate_contract_structure(self.contract)
        self.assertTrue(
            any(issue.rule_id == "VR-011" and "duplicate" in issue.message for issue in issues)
        )

    def test_invalid_pattern_detected(self):
        self.contract["datasets"][0]["schema"]["fields"][0]["pattern"] = "["
        issues = validate_contract_structure(self.contract)
        self.assertTrue(any(issue.rule_id == "VR-011" for issue in issues))

    def test_missing_description_detected(self):
        del self.contract["datasets"][0]["description"]
        issues = validate_contract_structure(self.contract)
        self.assertTrue(
            any(issue.rule_id == "VR-010" and issue.field == "description" for issue in issues)
        )

    def test_missing_provenance_metadata_detected(self):
        del self.contract["datasets"][0]["source_reference"]
        issues = validate_contract_structure(self.contract)
        self.assertTrue(
            any(issue.rule_id == "VR-010" and issue.field == "source_reference" for issue in issues)
        )

    def test_conditional_flags_outside_allowed_values_detected(self):
        value_field = next(
            definition
            for definition in self.contract["datasets"][0]["schema"]["fields"]
            if definition["name"] == "deformation_value"
        )
        value_field["nullable_when_quality_flags"] = ["NOT_A_REAL_FLAG"]
        issues = validate_contract_structure(self.contract)
        self.assertTrue(any(issue.rule_id == "VR-011" for issue in issues))


class ValueQualityAndProvenanceTests(unittest.TestCase):
    """PR-review fixes: no-value flags, geometry, dataset id, intervals, reason maps."""

    @classmethod
    def setUpClass(cls):
        cls.contract = load_contract(CONTRACT_PATH)

    def report(self, header, row, name="case.csv"):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), name, [row], header)
            return validate_dataset_csv(path, DATASET_ID, self.contract)

    def rules(self, report):
        return [issue.rule_id for issue in report.issues]

    def insar_report(self, rows, header=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "insar.csv", rows, header or INSAR_HEADER)
            return validate_dataset_csv(
                path, "AQS-INSAR-S1-DISPLACEMENT", self.contract
            )

    def rain_report(self, rows, header=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = make_csv(Path(tmp), "rain.csv", rows, header or RAIN_HEADER)
            return validate_dataset_csv(
                path, "AQS-RAIN-IMD-DISTRICT", self.contract
            )

    def test_insar_valid_row_passes(self):
        self.assertEqual("PASS", self.insar_report([INSAR_ROW]).status)

    def test_insar_masked_with_empty_value_and_reason_passes(self):
        row = list(INSAR_ROW)
        row[11] = ""           # deformation_value
        row[13] = "MASKED"     # quality_flag
        row[16] = "MASKED"     # missing_reason
        self.assertEqual("PASS", self.insar_report([row]).status)

    def test_insar_masked_with_value_fails_vr012(self):
        row = list(INSAR_ROW)
        row[13] = "MASKED"
        report = self.insar_report([row])
        self.assertIn("VR-012", self.rules(report))

    def test_gw_not_measured_with_value_fails_vr012(self):
        row = list(VALID_ROW)
        row[9] = "NOT_MEASURED"
        report = self.report(HEADER, row)
        self.assertIn("VR-012", self.rules(report))

    def test_gw_not_measured_empty_value_with_reason_passes(self):
        header = HEADER + ["missing_reason"]
        row = list(VALID_ROW) + ["NOT_MEASURED"]
        row[6] = ""           # measurement_value
        row[9] = "NOT_MEASURED"  # quality_flag
        report = self.report(header, row)
        self.assertEqual("PASS", report.status)

    def test_gw_valid_with_empty_value_fails_vr003(self):
        row = list(VALID_ROW)
        row[6] = ""
        report = self.report(HEADER, row)
        self.assertIn("VR-003", self.rules(report))

    def test_dataset_id_mismatch_fails_vr014(self):
        row = list(VALID_ROW)
        row[13] = "AQS-INSAR-S1-DISPLACEMENT"
        report = self.report(HEADER, row)
        self.assertIn("VR-014", self.rules(report))

    def test_dataset_id_versioned_form_passes(self):
        row = list(VALID_ROW)
        row[13] = "AQS-GW-CGWB-WELL-v1.0.0"
        report = self.report(HEADER, row)
        self.assertEqual("PASS", report.status)

    def test_multiple_empty_optional_fields_require_map(self):
        header = HEADER + ["datum", "screen_depth_m", "aquifer", "missing_reason_map"]
        row = list(VALID_ROW) + ["", "", "", ""]
        report = self.report(header, row)
        self.assertIn("VR-016", self.rules(report))

    def test_multiple_empty_optional_fields_with_map_passes(self):
        header = HEADER + ["datum", "screen_depth_m", "aquifer", "missing_reason_map"]
        reason_map = json.dumps(
            {"datum": "UNAVAILABLE", "screen_depth_m": "NOT_MEASURED", "aquifer": "UNKNOWN"}
        )
        row = list(VALID_ROW) + ["", "", "", reason_map]
        report = self.report(header, row)
        self.assertEqual("PASS", report.status)

    def test_invalid_reason_map_json_fails_vr016(self):
        header = HEADER + ["datum", "missing_reason_map"]
        row = list(VALID_ROW) + ["", "{not json"]
        report = self.report(header, row)
        self.assertIn("VR-016", self.rules(report))

    def test_rainfall_valid_row_passes(self):
        self.assertEqual("PASS", self.rain_report([RAIN_ROW]).status)

    def test_rainfall_end_before_start_fails_vr015(self):
        row = list(RAIN_ROW)
        row[5] = "2024-05-31"  # period_end
        report = self.rain_report([row])
        self.assertIn("VR-015", self.rules(report))

    def test_insar_missing_geometry_column_fails_vr001(self):
        index = INSAR_HEADER.index("relative_orbit")
        header = INSAR_HEADER[:index] + INSAR_HEADER[index + 1:]
        row = INSAR_ROW[:index] + INSAR_ROW[index + 1:]
        report = self.insar_report([row], header)
        self.assertIn("VR-001", self.rules(report))

    def test_insar_different_tracks_same_pixel_date_passes(self):
        second = list(INSAR_ROW)
        second[0] = "SYNTHETIC_TEST-INSAR-002"
        second[8] = "66"  # relative_orbit
        report = self.insar_report([INSAR_ROW, second])
        self.assertNotIn("VR-008", self.rules(report))

    def test_insar_same_track_same_pixel_date_fails_vr008(self):
        second = list(INSAR_ROW)
        second[0] = "SYNTHETIC_TEST-INSAR-002"
        report = self.insar_report([INSAR_ROW, second])
        self.assertIn("VR-008", self.rules(report))


if __name__ == "__main__":
    unittest.main()
