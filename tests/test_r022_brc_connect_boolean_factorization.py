import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_brc_connect_boolean_factorization.py"
spec = importlib.util.spec_from_file_location("r022_brc_connect_boolean_factorization", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class BRCConnectBooleanFactorizationTests(unittest.TestCase):
    def test_subset_intersection_factorization(self):
        out = mod.subset_intersection_model(5)
        self.assertEqual(out["distinct_left_compatibility_rows"], 32)
        self.assertEqual(out["boolean_rank_exact"], 5)
        self.assertTrue(out["factorization_exact"])

    def test_atom_drop_is_detected(self):
        out = mod.omitted_atom_kill(5)
        self.assertFalse(out["exact_after_drop"])
        self.assertTrue(out["missing_singleton_pair_should_connect"])
        self.assertFalse(out["factor_after_drop_connects"])

    def test_relation_table_storage_scaling(self):
        rows = {row["k"]: row for row in mod.scaling_rows()}
        self.assertEqual(rows[5]["relation_to_factor_membership_ratio"], 3.2)
        self.assertEqual(rows[10]["relation_to_factor_membership_ratio"], 51.2)

    def test_proof_carrying_factor_verifier(self):
        out = mod.proof_carrying_factor_verifier()
        self.assertTrue(out["exact_factor_accepted"])
        self.assertTrue(out["truncated_factor_rejected"])


if __name__ == "__main__":
    unittest.main()
