"""Regression tests for the scope and evidence requirements of residual claims."""

import json
from pathlib import Path
import unittest


CONSTRAINTS = Path(__file__).resolve().parents[1] / "research_constraints"


class ResidualPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((CONSTRAINTS / "residual_first.json").read_text(encoding="utf-8"))
        cls.rules = cls.policy["rules"]
        cls.heartbeat = json.loads((CONSTRAINTS / "heartbeat_brc_only.json").read_text(encoding="utf-8"))

    def test_unclassified_nonzero_residual(self):
        for conclusion in (
            "nonzero_residual_alone_rejects_object",
            "unknown_residual_is_automatically_noise",
            "unknown_residual_is_automatically_physics",
        ):
            with self.subTest(conclusion=conclusion):
                self.assertIs(self.rules[conclusion], False)
        self.assertIn("provenance_kind_or_unknown", self.policy["evidence_by_claim"]["conclusion_depends_on_residual"])

    def test_closed_counterexample_needs_a_witness_and_no_repair_trial(self):
        self.assertIs(self.rules["verified_counterexample_to_exact_claim_refutes_that_claim"], True)
        self.assertEqual(
            set(self.policy["evidence_by_claim"]["verified_counterexample"]),
            {"claim_and_satisfied_hypotheses", "witness", "scope_of_refutation"},
        )
        self.assertFalse(self.rules["repair_attempt_required_to_close_refuted_claim"])
        self.assertFalse(self.rules["followup_required_after_objective_complete"])
        self.assertEqual(self.rules["minimum_number_of_methods_to_try"], 0)
        self.assertEqual(self.policy["required_record"], [])

    def test_lossy_compression_retains_its_own_evidence_obligation(self):
        requirements = self.policy["evidence_by_claim"]["lossy_compression"]
        self.assertIn("declared_observer_and_future_operations", requirements)
        self.assertIn("preservation_proof_or_explicit_error_bound", requirements)
        self.assertIs(self.rules["exact_claim_obligations_remain"], True)
        self.assertIs(self.rules["goal_used_as_proof_premise"], False)

    def test_external_comparison_authorization_only_covers_the_comparison(self):
        self.assertEqual(
            set(self.heartbeat["scope"]),
            {"enterprise-math/heartbeat", "enterprise-math/BRC-Shor", "native-residual-attribution"},
        )
        self.assertEqual(self.heartbeat["classical_comparison_execution"], "NO_NEW_RUN_WITHOUT_EXPLICIT_LATER_USER_AUTHORIZATION")
        comparison = self.heartbeat["authorized_external_comparison"]
        self.assertTrue(comparison["separate_external_model_inputs_and_comparison_claim"])
        self.assertFalse(comparison["substitutes_for_native_BRC_computation_or_residual_attribution"])
        self.assertEqual(self.heartbeat["scientific_arithmetic_route"], "ACTUAL_TYPED_BRC_ONLY")


if __name__ == "__main__":
    unittest.main()
