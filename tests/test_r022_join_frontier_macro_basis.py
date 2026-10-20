import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_join_frontier_macro_basis.py"
spec = importlib.util.spec_from_file_location("r022_join_frontier_macro_basis", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class JoinFrontierMacroBasisTests(unittest.TestCase):
    def test_distributive_frontier_cover_exhaustive(self):
        out = mod.exhaustive_distributive_model()
        self.assertEqual(out["natural_order_posets"], 40)
        self.assertEqual(out["target_ideals_checked"], 317)
        self.assertFalse(out["counterexample"])

    def test_boolean_macro_width_is_representation_relative(self):
        out = mod.boolean_macro_cover_model()
        self.assertEqual(out["canonical_join_frontier_width"], 6)
        self.assertEqual(out["existing_dictionary_optimum_width"], 2)
        self.assertEqual(out["free_target_macro_width_if_admissible"], 1)

    def test_nondistributive_frontier_cover_kill(self):
        out = mod.m3_nondistributive_kill()
        self.assertTrue(out["join_is_target_top"])
        self.assertFalse(out["canonical_frontier_fully_covered"])
        self.assertTrue(out["kill"])

    def test_proof_carrying_verifier_accepts_exact_suboptimal(self):
        out = mod.proof_carrying_model()
        self.assertTrue(out["suboptimal_candidate_verified"])
        self.assertTrue(out["optimal_candidate_verified"])

    def test_proof_carrying_verifier_rejects_unsafe_cap(self):
        self.assertTrue(mod.proof_carrying_model()["unsafe_truncation_rejected"])


if __name__ == "__main__":
    unittest.main()
