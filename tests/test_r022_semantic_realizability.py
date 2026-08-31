import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_semantic_realizability.py"
spec = importlib.util.spec_from_file_location("r022_semantic_realizability", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class SemanticRealizabilityTests(unittest.TestCase):
    def test_proof_carrying_proposer_can_be_suboptimal_but_exact(self):
        out = mod.proof_carrying_greedy_witness()
        self.assertEqual(out["greedy_width"], 3)
        self.assertEqual(out["optimum_width"], 2)
        self.assertTrue(out["greedy_exact"])
        self.assertFalse(out["unsafe_cap_exact"])

    def test_representation_relative_width(self):
        out = mod.representation_relative_width_witness()
        self.assertEqual(out["free_synthetic_width"], 1)
        self.assertEqual(out["existing_dictionary_width"], 2)
        self.assertEqual(out["semantic_singleton_width"], 3)
        self.assertTrue(out["all_exact"])

    def test_weighted_laminar_exhaustive(self):
        out = mod.verify_weighted_laminar_exhaustive()
        self.assertEqual(out["families"], 63)
        self.assertEqual(out["cost_trials"], 2559)
        self.assertFalse(out["counterexample"])

    def test_interval_fast_path_strictly_extends_laminar(self):
        crossing = [(0, 1), (1, 2)]
        self.assertFalse(mod.is_laminar(mod.interval_set(iv) for iv in crossing))
        self.assertEqual(len(mod.interval_greedy_basis(crossing)), 2)
        out = mod.verify_interval_greedy_exhaustive()
        self.assertEqual(out["families"], 32767)
        self.assertFalse(out["counterexample"])

    def test_overlap_component_factorization_exhaustive(self):
        out = mod.verify_overlap_component_factorization_exhaustive()
        self.assertEqual(out["families"], 32767)
        self.assertFalse(out["counterexample"])


if __name__ == "__main__":
    unittest.main()
