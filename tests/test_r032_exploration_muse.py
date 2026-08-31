import json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"experiments"))
import r032_exploration_muse as muse
import r032_error_lesson_compiler as compiler
import r032_productive_failure_backtest as backtest
import r032_shoulder_search as shoulder

class TestR032ExplorationMuse(unittest.TestCase):
    def test_01_startup_tools_are_dormant(self):
        out=muse.startup_payload(); self.assertEqual(out["state"],"TOOLS_DORMANT"); self.assertEqual(out["recommended_tools"],[]); self.assertEqual(out["historical_warnings"],[])
    def test_02_unrequested_muse_is_rejected(self):
        with self.assertRaises(PermissionError): muse.request_muse("AUTOMATIC_CLAIM_CHALLENGE",["future"])
    def test_03_valid_muse_has_four_shelves(self):
        out=muse.request_muse("STUCK",["future","composition"],seed=11); self.assertTrue(out["tool_shelf"] and out["analogy_shelf"] and out["mutation_shelf"] and out["strange_tool"]); self.assertEqual(out["disclaimer"],"ANALOGY_IS_GENERATOR_NOT_EVIDENCE")
    def test_04_muse_tool_selection_is_layer_diverse(self):
        out=muse.request_muse("NEED_NEW_IDEAS",["future","composition","state"],seed=3); self.assertGreaterEqual(len({x["layer"] for x in out["tool_shelf"]}),3)
    def test_05_registry_forbids_nearest_only(self):
        self.assertFalse(muse.load_registry()["selection_policy"]["nearest_neighbor_only"])
    def test_06_lesson_compiler_requires_accepted_failure(self):
        event=dict(json.loads((ROOT/"research_error_lessons.json").read_text())["lessons"][0]); event["researcher_accepted_failure"]=False
        with self.assertRaises(PermissionError): compiler.compile_lesson(event)
    def test_07_lessons_always_have_survivors_and_questions(self):
        out=compiler.validate_frozen_lessons(); self.assertEqual(out["lesson_count"],5); self.assertTrue(out["all_have_survivors"] and out["all_have_new_questions"])
    def test_08_shoulders_forbid_taskbook_or_gold_query_fields(self):
        fs={"failure_class":"FALSE_ROUTE","minimal_witness":["x"],"broken_implication":["a=>b"],"surviving_invariant":["a"],"newly_exposed_object":["c"],"taskbook":"forbidden"}
        with self.assertRaises(ValueError): shoulder.shoulder_search(fs)
    def test_09_shoulders_return_structural_analogs(self):
        fixtures=shoulder.fixture_results(); self.assertEqual(set(fixtures),{"hidden_join_coordinate","phase_after_scaling_failure","scalar_credit_order_failure","generic_novelty_absorbed"}); self.assertTrue(all(x["results"] for x in fixtures.values()))
    def test_10_lessons_are_shoulders_not_fences(self):
        payload=json.loads((ROOT/"research_error_lessons.json").read_text()); self.assertIn("conditional shoulders",payload["anti_fence_rule"]); self.assertNotEqual(payload["anti_fence_rule"],"DO_NOT_TRY_THIS")
    def test_11_four_policy_modes_are_present(self):
        out=backtest.run_backtest(seeds=4,budgets=(14,)); self.assertEqual(set(out["modes"]),set(backtest.MODES))
    def test_12_muse_increases_branch_diversity_in_proxy(self):
        a=backtest.run_backtest(seeds=8,budgets=(18,))["aggregate"]; self.assertGreater(a["MUSE_PLUS_ERROR_INHERITANCE"]["representation_diversity"]["mean"],a["FREE_ONLY"]["representation_diversity"]["mean"]); self.assertGreater(a["MUSE_PLUS_ERROR_INHERITANCE"]["non_registry_concept_yield"]["mean"],a["FREE_ONLY"]["non_registry_concept_yield"]["mean"])
    def test_13_adversary_has_premature_abandonment(self):
        self.assertGreater(backtest.run_backtest(seeds=8,budgets=(18,))["aggregate"]["CLAIM_ADVERSARY"]["premature_abandonment_rate"]["mean"],0)
    def test_14_error_inheritance_saves_reconstruction_cost(self):
        a=backtest.run_backtest(seeds=8,budgets=(18,))["aggregate"]; self.assertGreater(a["MUSE_PLUS_ERROR_INHERITANCE"]["inherited_conceptual_cost_saved"]["mean"],0); self.assertLess(a["MUSE_PLUS_ERROR_INHERITANCE"]["repeated_conceptual_cost"]["mean"],a["FREE_ONLY"]["repeated_conceptual_cost"]["mean"])
    def test_15_scalar_productive_failure_ranking_is_killed(self):
        attack=backtest.productive_failure_scalar_attack(); self.assertTrue(attack["ranking_is_weight_sensitive"]); self.assertEqual(attack["verdict"],"NO_CANONICAL_SCALAR_RANKING"); self.assertGreaterEqual(len(attack["pareto_frontier"]),2)
    def test_16_phase_policies_are_distinct(self):
        p=muse.load_registry()["phase_policy"]; self.assertEqual(p["THEORY_EXPLOSION"]["startup_tools"],"DORMANT"); self.assertNotEqual(p["THEORY_EXPLOSION"]["claim_adversary"],p["CANONICALIZATION"]["claim_adversary"])
    def test_17_backtest_is_deterministic(self):
        self.assertEqual(backtest.run_backtest(seeds=3,budgets=(14,))["aggregate"],backtest.run_backtest(seeds=3,budgets=(14,))["aggregate"])
    def test_18_unproductive_route_can_still_compile_nonfence_lesson(self):
        event={"lesson_id":"SYNTH-UNPRODUCTIVE","source_route":"synthetic/no-signal","failure_class":"UNPRODUCTIVE_ROUTE","researcher_accepted_failure":True,"original_question":"Does this coordinate expose structure?","original_claim_or_model":"A salient pattern may organize the world.","what_failed":["The coordinate did not discriminate tested behavior."],"minimal_witness_or_failure_evidence":["Two distinct behaviors receive the same coordinate."],"what_survived":["Bounded non-discrimination survives."],"unexpected_structure_revealed":["Observable choice is now uncertain."],"new_distinctions":["unproductive vs under-instrumented"],"new_objects_or_coordinates":[],"new_tool_candidate":[],"new_negative_boundary":["salience is not evidence"],"new_questions_generated":["Which observable would discriminate before abandoning the route?"],"analogous_prior_failures":[],"how_prior_failures_helped":[],"what_should_NOT_be_inferred":["Do not infer uselessness under a richer observable."],"novelty_status":"SYNTHETIC","confidence_evidence_grade":"BOUNDED","failure_structure":{"failure_class":"UNPRODUCTIVE_ROUTE","minimal_witness":["non-discriminating coordinate"],"broken_implication":["salience => utility"],"surviving_invariant":["bounded non-discrimination"],"newly_exposed_object":["observable choice"]}}
        out=compiler.compile_lesson(event); self.assertEqual(out["failure_class"],"UNPRODUCTIVE_ROUTE"); self.assertTrue(out["what_survived"] and out["new_questions_generated"])

if __name__=="__main__": unittest.main(verbosity=2)
