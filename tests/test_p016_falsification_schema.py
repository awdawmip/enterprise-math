import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "falsification.schema.json"


class TestP016FalsificationSchema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    def test_contract_requires_model_structure_and_predictions(self):
        required = set(self.schema["required"])
        self.assertTrue(
            {
                "schema_version",
                "model_id",
                "status",
                "state_space",
                "transition_law",
                "observation_map",
                "parameters",
                "symmetries",
                "conserved_quantities",
                "predictions",
            }.issubset(required)
        )

    def test_every_model_must_expose_at_least_one_kill_test_prediction(self):
        predictions = self.schema["properties"]["predictions"]
        self.assertEqual(predictions["minItems"], 1)
        item = predictions["items"]
        required = set(item["required"])
        self.assertTrue(
            {
                "id",
                "kill_test_class",
                "observable",
                "unavoidable_prediction",
                "current_constraint",
                "falsified_if",
                "source_ids",
            }.issubset(required)
        )

    def test_kill_test_classes_are_exactly_f1_through_f9(self):
        classes = self.schema["properties"]["predictions"]["items"]["properties"]["kill_test_class"]["enum"]
        self.assertEqual(classes, [f"F{i}" for i in range(1, 10)])

    def test_source_ids_must_use_registry_prefix(self):
        source_ids = self.schema["properties"]["predictions"]["items"]["properties"]["source_ids"]
        self.assertEqual(source_ids["items"]["pattern"], "^SRC-")

    def test_status_keeps_hypothesis_and_falsification_distinct(self):
        statuses = self.schema["properties"]["status"]["enum"]
        self.assertIn("PHYSICAL-HYPOTHESIS", statuses)
        self.assertIn("FALSIFIED", statuses)
        self.assertNotEqual(statuses.index("PHYSICAL-HYPOTHESIS"), statuses.index("FALSIFIED"))


if __name__ == "__main__":
    unittest.main()
