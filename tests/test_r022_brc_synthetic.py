import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "r022_brc_synthetic.py"
spec = importlib.util.spec_from_file_location("r022_brc_synthetic", MODULE_PATH)
r022 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(r022)


class R022BRCTests(unittest.TestCase):

    def test_generic_primitive_oracles(self):
        out = r022.generic_primitive_smoke_tests()
        self.assertEqual(out["minimal_coordinate_feature_subsets"], [(1,)])
        self.assertEqual(out["minimum_solver_covers"], [("A", "B")])
        self.assertTrue(out["rcc_positive"])
        self.assertTrue(out["rcc_mutation_rejected"])
        self.assertTrue(out["ncc_positive"])
        self.assertTrue(out["partial_move_positive"])
        self.assertEqual(out["pareto_names"], ["A", "B", "C"])

    def test_md5_router_minimal_raw_coordinate_signature(self):
        out = r022.branch_signature_router_model()
        self.assertEqual(out["minimal_raw_coordinate_subset_size"], 9)
        self.assertEqual(out["compiled_route_labels"], 5)
        self.assertEqual(out["fixed_width_compiled_route_token_bits"], 3)
        self.assertTrue(out["every_raw_bit_has_deletion_witness"])

    def test_router_minimum_need_not_equal_semantic_future_quotient(self):
        out = r022.router_nonunique_minimum_counterexample()
        self.assertEqual(out["minimal_router_blocks"], 2)
        self.assertEqual(out["semantic_future_classes_if_all_outputs_equal"], 1)

    def test_residual_recoalescence_is_exact_but_not_stronger_than_deterministic_quotient(self):
        out = r022.residual_recoalescence_model()
        self.assertTrue(out["safe_recoalescence"])
        self.assertEqual(out["max_full_histories"], 4096)
        self.assertEqual(out["max_live_residual_tokens"], 5)
        self.assertEqual(out["deterministic_future_complete_states"], 5)

    def test_current_output_only_merge_is_unsafe(self):
        out = r022.unsafe_current_output_merge_kill()
        self.assertEqual(out["spurious_results"], ["spurious"])

    def test_endpoint_equality_does_not_preserve_provenance(self):
        out = r022.provenance_endpoint_kill()
        self.assertTrue(out["endpoint_only_safe_for_endpoint_existence"])
        self.assertFalse(out["endpoint_only_safe_for_provenance_exactness"])

    def test_safe_partial_moves_not_closed_under_composition(self):
        out = r022.partial_neutral_move_kill()
        self.assertTrue(out["n_safe_partial"])
        self.assertTrue(out["m_safe_partial"])
        self.assertFalse(out["composition_defined"])

    def test_deeper_causal_rewind_can_be_required(self):
        out = r022.causal_rewind_kill()
        self.assertFalse(out["one_step_recovers"])
        self.assertTrue(out["deeper_rewind_recovers"])
        self.assertEqual(out["causal_refinement_depth"], 2)

    def test_arbitrary_distance_can_move_opposite_future_defect(self):
        out = r022.misleading_potential_kill()
        self.assertLess(out["metric_after"], out["metric_before"])
        self.assertGreater(out["future_defect_after"], out["future_defect_before"])

    def test_nfa_dfa_storage_work_pareto(self):
        out = r022.nfa_dfa_pareto_model()
        self.assertEqual(out["nfa_states"], 7)
        self.assertEqual(out["minimal_dfa_states"], 64)
        self.assertEqual(out["nfa_max_live_branch_width"], 7)

    def test_bidirectional_gain_is_standard_mitm(self):
        out = r022.bidirectional_interface_model()
        self.assertEqual(out["full_end_check_assignments"], 1048576)
        self.assertEqual(out["bidirectional_frontier_total"], 2048)
        self.assertEqual(out["enumeration_work_ratio_full_to_bidirectional"], 512.0)

    def test_branch_budget_balances_dual_frontiers(self):
        out = r022.branch_budget_model()
        self.assertEqual(out["best_balanced_split"]["split"], 10)


if __name__ == "__main__":
    unittest.main()
