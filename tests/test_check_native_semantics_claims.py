import importlib.util
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("checker", ROOT / "tools" / "check_native_semantics_claims.py")
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
assert SPEC.loader is not None
SPEC.loader.exec_module(checker)


class NativeSemanticsCheckerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture_doc = json.loads((ROOT / "research" / "r044_generated" / "R044_ADVERSARIAL_FIXTURES.json").read_text())

    def test_all_frozen_adversarial_fixtures(self):
        for fixture in self.fixture_doc["fixtures"]:
            with self.subTest(fixture=fixture["fixture_id"]):
                got = checker.check_claim(fixture["claim"])["verdict"]
                self.assertEqual(got, fixture["expected_verdict"])

    def test_explicit_metric_base_is_not_blanket_forbidden(self):
        fx = next(x for x in self.fixture_doc["fixtures"] if x["fixture_id"] == "F10_METRIC_EXPLICITLY_BASE")
        result = checker.check_claim(fx["claim"])
        self.assertEqual(result["verdict"], "NATIVE_ADMISSIBLE")
        self.assertEqual(set(result["effective_strata"]), {"N0"})

    def test_explicit_continuum_base_is_not_blanket_forbidden(self):
        fx = next(x for x in self.fixture_doc["fixtures"] if x["fixture_id"] == "F11_CONTINUUM_EXPLICITLY_BASE")
        self.assertEqual(checker.check_claim(fx["claim"])["verdict"], "NATIVE_ADMISSIBLE")

    def test_missing_theorem_critical_dependency_fails_closed(self):
        fx = next(x for x in self.fixture_doc["fixtures"] if x["fixture_id"] == "F14_OMITTED_DEPENDENCY_FAILS_CLOSED")
        result = checker.check_claim(fx["claim"])
        self.assertEqual(result["verdict"], "UNRESOLVED")
        self.assertTrue(any(f["code"] == "NSA-DEPENDENCY-OMITTED" for f in result["findings"]))

    def test_n2_mislabeled_n0_is_detected_from_typed_kind(self):
        fx = next(x for x in self.fixture_doc["fixtures"] if x["fixture_id"] == "F15_N2_FALSELY_REPORTED_N0")
        result = checker.check_claim(fx["claim"])
        self.assertEqual(result["verdict"], "SEMANTIC_MISMATCH")
        self.assertTrue(any(f["code"] == "NSA-UNDERSTATED-STRATUM" for f in result["findings"]))

    def test_scalar_certificate_cannot_promote_full_object(self):
        fx = next(x for x in self.fixture_doc["fixtures"] if x["fixture_id"] == "F04_SCALAR_INVARIANCE_STRONG_PROMOTION")
        result = checker.check_claim(fx["claim"])
        self.assertEqual(result["verdict"], "SEMANTIC_MISMATCH")
        self.assertTrue(any(f["code"] == "NSA-CERT-STRENGTH" for f in result["findings"]))

    def test_text_trigger_does_not_decide_verdict(self):
        fx = next(x for x in self.fixture_doc["fixtures"] if x["fixture_id"] == "F10_METRIC_EXPLICITLY_BASE")
        result = checker.check_claim(fx["claim"])
        self.assertEqual(result["verdict"], "NATIVE_ADMISSIBLE")

    def test_dangling_dependency_is_unresolved(self):
        claim = {
            "claim_id": "dangling",
            "claim_text": "conditional propagation",
            "declared_n0_primitives": ["E"],
            "critical_symbols": ["E", "kernel"],
            "dependencies": [{"id": "kernel", "kind": "operation", "claimed_stratum": "N1", "depends_on": ["missing"]}],
            "promotion_target_strength": "OBJECT",
            "proposed_claim_class": "CONDITIONAL",
        }
        result = checker.check_claim(claim)
        self.assertEqual(result["verdict"], "UNRESOLVED")
        self.assertTrue(any(f["code"] == "NSA-LEDGER-DANGLING" for f in result["findings"]))


if __name__ == "__main__":
    unittest.main()
