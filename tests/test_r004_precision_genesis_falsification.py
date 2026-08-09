import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "r004_precision_genesis_falsification.json"
SCHEMA_PATH = ROOT / "falsification.schema.json"


class R004PrecisionGenesisFalsificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.source_ids = set()
        for path in ROOT.glob("sources*.json"):
            registry = json.loads(path.read_text(encoding="utf-8"))
            cls.source_ids.update(
                source["id"] for source in registry.get("sources", [])
            )

    def test_top_level_contract_matches_p016_surface(self):
        required = set(self.schema["required"])
        self.assertTrue(required.issubset(self.model))
        self.assertEqual(self.model["schema_version"], 1)
        self.assertIn(
            self.model["status"], self.schema["properties"]["status"]["enum"]
        )
        self.assertEqual(self.model["status"], "PHYSICAL-HYPOTHESIS")

    def test_every_prediction_has_required_fields_and_known_kill_class(self):
        prediction_schema = self.schema["properties"]["predictions"]["items"]
        required = set(prediction_schema["required"])
        allowed_classes = set(
            prediction_schema["properties"]["kill_test_class"]["enum"]
        )
        predictions = self.model["predictions"]
        self.assertGreaterEqual(len(predictions), 1)
        for prediction in predictions:
            self.assertTrue(required.issubset(prediction))
            self.assertIn(prediction["kill_test_class"], allowed_classes)

    def test_every_prediction_source_is_registered(self):
        for prediction in self.model["predictions"]:
            self.assertTrue(prediction["source_ids"])
            self.assertTrue(set(prediction["source_ids"]).issubset(self.source_ids))

    def test_v0_f3_rule_is_predeclared_and_does_not_claim_global_exclusion(self):
        prediction = self.model["predictions"][0]
        self.assertEqual(prediction["kill_test_class"], "F3")
        self.assertIn("V_predicted = eta * V_ordinary", prediction["unavoidable_prediction"])
        self.assertIn("eta = 0", prediction["excluded_parameter_region"])
        self.assertIn(
            "No broader eta interval is claimed excluded",
            prediction["excluded_parameter_region"],
        )


if __name__ == "__main__":
    unittest.main()
