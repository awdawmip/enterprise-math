import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))

import r021_branching_collapse_oracle as o


class R021OracleTests(unittest.TestCase):
    def test_minimal_naive_composition_counterexample_has_three_states(self):
        c = o.find_min_naive_composition_counterexample(3)
        self.assertIsNotNone(c)
        self.assertEqual(c["n"], 3)
        self.assertNotEqual(c["exact_two_step"], c["naive_two_step"])

    def test_exhaustive_naive_composition_minimality_counts(self):
        x = o.exhaustive_naive_composition_stats(3)
        self.assertEqual(x["minimal_failure_states"], 3)
        self.assertEqual(x["by_n"][0]["composition_failures"], 0)
        self.assertEqual(x["by_n"][1]["composition_failures"], 0)
        self.assertGreater(x["by_n"][2]["composition_failures"], 0)

    def test_successor_partition_is_unique_coarsest_refinement(self):
        s = o.three_state_counterexample_system()
        ck = o.exhaustive_coarsest_refinement(s, lambda x: o.successor_support_signature(s, x, "f"))
        self.assertTrue(ck["verified"])
        # A singleton plus B split into b/c -> 3 blocks.
        self.assertEqual(len(ck["signature_partition"]), 3)

    def test_future_signature_partition_is_unique_coarsest_static_refinement(self):
        s = o.three_state_counterexample_system()
        L = o.words_upto(s.alphabet, 2)
        ck = o.exhaustive_coarsest_refinement(s, lambda x: o.future_signature(s, x, L))
        self.assertTrue(ck["verified"])

    def test_exact_branch_algorithm_preserves_support(self):
        s = o.three_state_counterexample_system()
        start = s.fibre("A")
        word = ("f", "f")
        r = o.branch_on_demand_exact(s, start, word)
        exact = o.execute_fine(s, start, word)
        self.assertEqual(r["final_fine_support"], exact)

    def test_reexpand_mutation_is_detected(self):
        s = o.three_state_counterexample_system()
        start = s.fibre("A")
        word = ("f", "f")
        m = o.naive_reexpand_execution(s, start, word)
        exact = o.observable_support(s, o.execute_fine(s, start, word))
        self.assertNotEqual(m["final_observable_support"], exact)

    def test_merge_inequivalent_mutation_is_detected(self):
        s = o.three_state_counterexample_system()
        m = o.merge_inequivalent_states_mutation(s, "b", "c", o.words_upto(s.alphabet, 2))
        self.assertTrue(m["mutation_detected"])
        self.assertIsNotNone(m["separating_word"])

    def test_forgetful_recoalescence_requires_remaining_signature(self):
        s = o.three_state_counterexample_system()
        exact = frozenset({"b"})
        hull = s.fibre("B")
        self.assertFalse(o.safe_forgetful_merge(s, exact, hull, (("f",),)))
        self.assertTrue(o.safe_forgetful_merge(s, exact, hull, ((),)))

    def test_floor_translation_class_count_formula(self):
        for r in range(2, 10):
            for c in range(1, 12):
                for h in range(0, 12):
                    x = o.floor_translation_signature_classes(r, c, h)
                    self.assertEqual(x["class_count"], x["predicted_count"], (r, c, h, x))

    def test_floor_translation_eventual_full_residue_iff_coprime(self):
        x = o.floor_translation_signature_classes(10, 1, 20)
        self.assertEqual(x["class_count"], 10)
        self.assertTrue(x["full_residue_required_eventually"])
        y = o.floor_translation_signature_classes(12, 8, 20)
        self.assertEqual(y["class_count"], 3)
        self.assertFalse(y["full_residue_required_eventually"])

    def test_floor_fibre_support_stays_at_width_two(self):
        x = o.floor_translation_fibre_support_stats(17, 5, 100)
        self.assertLessEqual(x["max_coarse_branch_width"], 2)

    def test_branch_dictionary_frontier_charges_dictionary(self):
        req = [frozenset({0}), frozenset({1}), frozenset({2}), frozenset({0,1}), frozenset({0,2}), frozenset({1,2})]
        f = o.bounded_branch_dictionary_frontier(3, req)
        pairs = {(x["K"], x["W"]) for x in f}
        self.assertIn((3, 2), pairs)
        self.assertIn((6, 1), pairs)

    def test_powerset_branching_has_exponential_static_state_gap_but_not_live_bits_gap(self):
        x = o.powerset_membership_pareto(8)
        self.assertEqual(x["deterministic_future_states"], 256)
        self.assertEqual(x["branch_atoms"], 8)
        self.assertEqual(x["runtime_branch_config_bits"], x["deterministic_live_label_bits"])
        self.assertGreater(x["branch_work_per_symbol_worst"], x["deterministic_work_per_symbol"])

    def test_middle_incidence_marginal_failure(self):
        x = o.middle_incidence_counterexample()
        self.assertTrue(x["coarse_marginal_predicts_path"])
        self.assertEqual(x["exact_composition"], set())

    def test_pth_power_gap_uses_open_interior(self):
        x = o.pth_cell_translation_stats(2, 2, 1, 2)
        self.assertEqual(x["cell"], (5, 8))
        self.assertEqual(x["cell_size"], 4)
        self.assertLessEqual(x["max_bracket_support_width"], 3)
        self.assertNotEqual(o.pth_bracket(5 + 1, 2), o.pth_bracket(8 + 1, 2))

    def test_witness_cutoff_refines_low_fibre(self):
        x = o.witness_cutoff_groups([6, 10, 14], 2, 7)
        g = next(g for g in x["groups"] if set(g["members"]) == {6,10,14})
        self.assertEqual(g["high_signature_count"], 3)


if __name__ == "__main__":
    unittest.main()
