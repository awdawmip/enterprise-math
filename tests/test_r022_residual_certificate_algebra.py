import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "r022_residual_certificate_algebra.py"
spec = importlib.util.spec_from_file_location("r022_residual_certificate_algebra", MODULE_PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ResidualCertificateAlgebraTests(unittest.TestCase):
    def test_rcc_ncc_are_join_rewrites(self):
        r = m.rjc_special_cases()
        self.assertTrue(r["rcc_as_idempotence"])
        self.assertTrue(r["ncc_as_bottom_elimination"])
        self.assertTrue(r["wrong_nonempty_prune_rejected"])

    def test_rjc_congruence_under_union(self):
        self.assertTrue(m.rjc_special_cases()["congruence_under_configuration_union"])

    def test_collective_dominance_beats_pairwise(self):
        r = m.collective_dominance_counterexample()
        self.assertFalse(any(r["pairwise_dominated"].values()))
        self.assertTrue(all(r["collectively_removable"].values()))
        self.assertTrue(all(len(b) == 2 for b in r["minimum_bases"]))

    def test_local_irredundance_is_not_global_minimum(self):
        r = m.antichain_greedy_trap()
        self.assertTrue(r["pairwise_incomparable"])
        self.assertEqual(r["irredundant_basis_sizes"], [3, 4])

    def test_language_extension_invalidates_certificate(self):
        r = m.language_extension_kill()
        self.assertTrue(r["exact_on_short_language"])
        self.assertFalse(r["exact_after_language_extension"])

    def test_support_idempotence_does_not_preserve_multiplicity(self):
        r = m.multiplicity_kill()
        self.assertTrue(r["support_merge_exact"])
        self.assertFalse(r["multiplicity_preserved"])

    def test_free_union_token_trivializes_width(self):
        r = m.free_union_token_width_kill()
        self.assertEqual(r["existing_token_min_width"], 2)
        self.assertEqual(r["free_synthesized_union_token_width"], 1)

    def test_set_cover_reduction_witness(self):
        r = m.set_cover_reduction_witness()
        self.assertEqual(r["minimum_cover_size"], 2)
        self.assertEqual(r["minimum_exact_branch_bases"], [["S0", "S3"]])


if __name__ == "__main__":
    unittest.main()
