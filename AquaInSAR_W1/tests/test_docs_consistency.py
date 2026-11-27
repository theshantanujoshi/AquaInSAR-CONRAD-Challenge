"""Consistency checks between human-readable and machine-readable W1 deliverables."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT / "src"))

from aquainsar_w1.contract_tools import load_contract  # noqa: E402

CONTRACT_JSON = PACKAGE_ROOT / "contracts" / "AquaInSAR_Data_Contract_v0.9.0.json"
CONTRACT_MD = PACKAGE_ROOT / "contracts" / "AquaInSAR_Data_Contract_v0.9.0.md"
PROTOCOL_MD = PACKAGE_ROOT / "protocols" / "AquaInSAR_Exploratory_Comparison_Protocol_v0.9.0.md"
README = PACKAGE_ROOT / "README.md"


class DocumentationConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(CONTRACT_JSON.read_text(encoding="utf-8"))
        cls.contract_md = CONTRACT_MD.read_text(encoding="utf-8")
        cls.protocol_md = PROTOCOL_MD.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")

    def test_version_and_id_agree(self):
        self.assertIn(self.contract["contract"]["id"], self.contract_md)
        self.assertIn(self.contract["contract"]["version"], self.contract_md)
        self.assertIn(self.contract["contract"]["status"], self.contract_md)

    def test_every_dataset_id_is_in_human_contract(self):
        for dataset in self.contract["datasets"]:
            with self.subTest(dataset=dataset["dataset_id"]):
                self.assertIn(dataset["dataset_id"], self.contract_md)

    def test_every_active_field_name_is_in_human_contract(self):
        for dataset in self.contract["datasets"]:
            schema = dataset.get("schema", {})
            for definition in schema.get("fields", []):
                with self.subTest(dataset=dataset["dataset_id"], field=definition["name"]):
                    self.assertIn(f"`{definition['name']}`", self.contract_md)

    def test_validation_rules_are_documented(self):
        for rule in self.contract["validation_rules"]:
            with self.subTest(rule=rule["id"]):
                self.assertIn(rule["id"], self.contract_md)
                self.assertIn(rule["severity"], self.contract_md)

    def test_contract_and_protocol_cite_each_other(self):
        self.assertIn("AquaInSAR_Data_Contract_v0.9.0.json", self.contract_md)
        self.assertIn("AQS-DC", self.protocol_md)
        self.assertIn("AQS-DC", self.contract_md)

    def test_protocol_has_required_method_sections(self):
        for section in ("4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"):
            with self.subTest(section=section):
                self.assertIn(f"## {section}", self.protocol_md)

    def test_protocol_states_no_results(self):
        self.assertIn("not a results report", self.protocol_md)
        self.assertIn("No AquaInSAR comparison has been", self.protocol_md)
        self.assertIn("computed.", self.protocol_md)

    def test_protocol_is_draft_version_with_assignment_numbering_note(self):
        self.assertIn("`0.9.0`", self.protocol_md)
        self.assertIn("Draft for W1 review", self.protocol_md)
        self.assertIn("retain the numbering used in the W1 assignment", self.protocol_md)

    def test_readme_references_current_protocol_file(self):
        self.assertIn("AquaInSAR_Exploratory_Comparison_Protocol_v0.9.0.md", self.readme)

    def test_readme_explains_package_and_status(self):
        self.assertIn("AquaInSAR_W1", self.readme)
        self.assertIn("v0.9.0", self.readme)
        self.assertIn("not", self.readme.lower())

    def test_machine_contract_loads_without_third_party_packages(self):
        contract = load_contract(CONTRACT_JSON)
        self.assertEqual("AQS-DC", contract["contract"]["id"])
        self.assertEqual(5, len(contract["datasets"]))


if __name__ == "__main__":
    unittest.main()
