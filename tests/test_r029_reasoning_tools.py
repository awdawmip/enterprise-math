import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments"
sys.path.insert(0, str(EXP))

from r029_reasoning_tool_registry import (
    load_registry, validate_registry, tool_index, can_contribute_theorem_evidence,
    rank_tools, resolve_alias,
)
from r029_reasoning_tool_oracle import (
    load_json, validate_composition_matrix, validate_kill_fixtures,
    trigger_mutation_results, COMPOSITION, KILLS,
)

class R029ReasoningToolsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = load_registry()
        cls.idx = tool_index(cls.reg)

    def test_registry_schema(self):
        self.assertEqual(validate_registry(self.reg), [])

    def test_trust_classes_present(self):
        got = {t["trust_class"] for t in self.reg["tools"]}
        self.assertEqual(got, {
            "PROOF_PRESERVING","EXACT_SEMANTIC_TRANSFORMATION",
            "ADVERSARIAL_DIAGNOSTIC","INTERPRETIVE_LENS"
        })

    def test_philosophy_lens_never_theorem_evidence(self):
        t = self.idx["ONTOLOGICAL_COMMITMENT_LENS"]
        self.assertFalse(can_contribute_theorem_evidence(t, certificate_present=True))

    def test_diagnostic_never_theorem_evidence(self):
        t = self.idx["ONE_STEP_EXACT_NOT_COMPOSITION_SAFE"]
        self.assertFalse(can_contribute_theorem_evidence(t, certificate_present=True))

    def test_exact_transform_requires_certificate(self):
        t = self.idx["FACTOR_THROUGH_COMPLETE_ENCODING"]
        self.assertFalse(can_contribute_theorem_evidence(t, certificate_present=False))
        self.assertTrue(can_contribute_theorem_evidence(t, certificate_present=True))

    def test_seed_alias_resolution(self):
        self.assertEqual(resolve_alias(self.reg,"SUPPORT_COUNT_PROVENANCE_SPLIT"),
                         "BOOLEAN_COUNT_PROVENANCE_CARRIER_SPLIT")
        self.assertEqual(resolve_alias(self.reg,"CAUSAL_PREDICTIVE_RETROSPECTIVE_SPLIT"),
                         "CAUSAL_PREDICTIVE_RETROSPECTIVE_RELEVANCE_SPLIT")

    def test_composition_matrix(self):
        matrix = load_json(COMPOSITION)
        self.assertEqual(validate_composition_matrix(matrix,self.reg), [])
        classes = {r["class"] for r in matrix["rules"]}
        self.assertEqual(classes, {"ALWAYS_SAFE","SAFE_WITH_PRECONDITIONS","DIAGNOSTIC_ONLY","KNOWN_INVALID"})

    def test_universal_claim_kill_fixtures(self):
        kills = load_json(KILLS)
        self.assertEqual(validate_kill_fixtures(kills,self.reg), [])
        self.assertEqual(len(kills["claims"]),10)

    def test_trigger_mutations(self):
        results = trigger_mutation_results(self.reg)
        self.assertTrue(all(results.values()), results)

    def test_keyword_all_tests_does_not_trigger_quantifier_scope(self):
        ranked = rank_tools(self.reg,{"claim_text":"all tests passed","task_tags":["validation"]},max_advisory=20)
        ids={r["id"] for r in ranked["all_positive_candidates"]}
        self.assertNotIn("QUANTIFIER_SCOPE_CHECK",ids)

    def test_semantic_continuation_without_future_keyword(self):
        ranked=rank_tools(self.reg,{
            "claim_text":"the quotient must be closed under arbitrary continuations",
            "task_tags":["precision"]
        },max_advisory=20)
        ids={r["id"] for r in ranked["all_positive_candidates"]}
        self.assertIn("FUTURE_LANGUAGE_RELATIVITY",ids)

    def test_sparse_advisory_selection(self):
        ranked=rank_tools(self.reg,{
            "claim_text":"one-step exact quotient will be composed repeatedly",
            "task_tags":["quotient","composition"]
        },max_advisory=4)
        self.assertLessEqual(len(ranked["advisory_diagnostic_or_generator"]),4)
        self.assertLess(len(ranked["advisory_diagnostic_or_generator"]),len(self.reg["tools"]))

    def test_root_coverage_history_fixture_triggers(self):
        ranked=rank_tools(self.reg,{
            "claim_text":"build pass is offered as Lean checked evidence; verify root import compiled target",
            "task_tags":["Lean","validation"]
        },max_advisory=12)
        ids={r["id"] for r in ranked["all_positive_candidates"]}
        self.assertIn("ROOT_COVERAGE_EVIDENCE_CHECK",ids)

    def test_realized_path_credit_does_not_type_as_exact_factorization(self):
        t=self.idx["REALIZED_PATH_VS_DECLARED_LANGUAGE_CREDIT"]
        self.assertEqual(t["trust_class"],"ADVERSARIAL_DIAGNOSTIC")
        self.assertIn("declared-language", " ".join(t["may_destroy_or_not_preserve"]).lower())

    def test_every_tool_has_counterexample_and_prior_art_root(self):
        for t in self.reg["tools"]:
            self.assertTrue(t["anti_examples"],t["id"])
            self.assertTrue(t["prior_art_root"]["references"],t["id"])
            self.assertTrue(t["project_specific_residue"],t["id"])

if __name__ == "__main__":
    unittest.main()
