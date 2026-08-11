import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve()
MOD_PATH = HERE.parents[1] / "experiments" / "r021_branching_collapse_oracle.py"
spec = importlib.util.spec_from_file_location("r021", MOD_PATH)
r021 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
import sys
sys.modules[spec.name] = r021
spec.loader.exec_module(r021)


class R021BranchingCollapseTests(unittest.TestCase):
    def test_future_partition_unique_coarsest(self):
        s = r021.sample_partition_system()
        out = r021.verify_unique_coarsest_partitions(
            s, [(), ("a",), ("b",), ("a", "b"), ("b", "a")], "a"
        )
        self.assertTrue(out["future_unique_coarsest"])
        self.assertTrue(out["one_step_unique_coarsest"])

    def test_min_composition_counterexample_is_two_states(self):
        out = r021.exhaustive_min_composition_counterexample(2)
        self.assertEqual(out["minimal_n"], 2)
        self.assertEqual(out["witness"]["exact"], [])
        self.assertEqual(out["witness"]["naive"], [0])

    def test_floor_translation_class_formula(self):
        for r, c in [(8, 1), (12, 8), (12, 6), (10, 20), (15, 6)]:
            out = r021.floor_translation_theory(r, c, 12)
            phase = r // __import__("math").gcd(r, c)
            for row in out["rows"]:
                h = row["horizon"]
                expected = 1 if c % r == 0 else min(h + 1, phase)
                self.assertEqual(row["classes"], expected)

    def test_floor_coprime_eventually_reconstructs_residue(self):
        out = r021.floor_translation_theory(11, 4, 12)
        self.assertTrue(out["long_horizon_reconstructs_all_residues"])
        self.assertEqual(out["rows"][9]["classes"], 11)

    def test_square_bracket_plus_one_refines_one_threshold_per_step(self):
        out = r021.bracket_gap_translation(2, 2, 1, 4)
        self.assertEqual(out["fibre_size"], 4)
        self.assertEqual([r["classes"] for r in out["rows"]], [2, 3, 4, 4])

    def test_witness_cutoff_requires_distinction(self):
        out = r021.witness_cutoff_example()
        self.assertFalse(out["storage_advantage"])
        self.assertNotEqual(out["higher_witness_sets"][6], out["higher_witness_sets"][10])

    def test_middle_incidence_reexpansion_is_spurious(self):
        out = r021.middle_incidence_example()
        self.assertEqual(out["fine_two_step_support"], [])
        self.assertEqual(out["naive_coarse_two_step_support"], [0])
        self.assertTrue(out["repair_token_is_exact_fine_identity_here"])

    def test_nfa_pareto_witness_charges_metadata(self):
        out = r021.nfa_pareto_witness()
        self.assertEqual(out["minimal_branch_atoms"], 2)
        self.assertLess(
            out["branching"]["total_incidences_plus_labels"],
            out["deterministic_total_incidences_plus_labels"],
        )
        self.assertEqual(out["branching"]["encoder_incidences"], 4)

    def test_two_atom_nfa_exhaustive_reaches_four_dfa_states(self):
        out = r021.exhaustive_two_atom_nfa_search()
        self.assertTrue(out["pass"])
        self.assertEqual(out["maximum_minimal_DFA_states"], 4)

    def test_recoalescence_current_coarse_only_is_unsafe(self):
        out = r021.mutation_suite()
        self.assertTrue(out["merge_by_current_coarse_only_detected_unsafe"])
        self.assertTrue(out["remaining_signature_criterion_rejects_merge"])

    def test_full_oracle(self):
        self.assertTrue(r021.run_all()["pass"])


if __name__ == "__main__":
    unittest.main()
