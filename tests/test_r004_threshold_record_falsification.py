import json
import pathlib
import unittest
from fractions import Fraction

from enterprise_math.precision_threshold_record import (
    pedalino_representative_region_excluded,
    threshold_record_overlap,
)


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "r004_threshold_record_falsification.json"
SCHEMA_PATH = ROOT / "falsification.schema.json"


class R004ThresholdRecordFalsificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.source_ids = set()
        for path in ROOT.glob("sources*.json"):
            registry = json.loads(path.read_text(encoding="utf-8"))
            cls.source_ids.update(source["id"] for source in registry.get("sources", []))

    def test_model_matches_existing_p016_schema_surface(self):
        self.assertTrue(set(self.schema["required"]).issubset(self.model))
        self.assertEqual(self.model["schema_version"], 1)
        self.assertEqual(self.model["status"], "PHYSICAL-HYPOTHESIS")
        self.assertEqual(self.model["model_id"], "R004-THRESHOLD-RECORD-PREMODEL-V1")

    def test_prediction_is_f3_and_uses_registered_source(self):
        prediction = self.model["predictions"][0]
        self.assertEqual(prediction["kill_test_class"], "F3")
        self.assertTrue(set(prediction["source_ids"]).issubset(self.source_ids))
        self.assertIn("100*delta>91*d", prediction["excluded_parameter_region"])
        self.assertIn("not a confidence-level", prediction["excluded_parameter_region"])

    def test_declared_eta_is_derived_not_a_free_parameter(self):
        names = {parameter["name"] for parameter in self.model["parameters"]}
        self.assertEqual(names, {"d", "delta"})
        self.assertNotIn("eta", names)
        self.assertEqual(threshold_record_overlap(3, 10), Fraction(7, 10))

    def test_integer_exclusion_boundary_matches_documented_region(self):
        self.assertFalse(pedalino_representative_region_excluded(91, 100))
        self.assertTrue(pedalino_representative_region_excluded(92, 100))


if __name__ == "__main__":
    unittest.main()
