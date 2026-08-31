import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_brc_compiler_core.py"
spec = importlib.util.spec_from_file_location("r022_brc_compiler_core", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class BRCCompilerCoreTests(unittest.TestCase):
    def test_end_to_end_semantic_plan(self):
        out = mod.synthetic_end_to_end()
        self.assertEqual(out["target_partition"], ((0,), (1,), (2,), (3,), (4,), (5,)))
        self.assertEqual(out["required_pair_count"], 6)
        self.assertEqual(out["side_bits"], 2)

    def test_future_and_feature_mutations_are_rejected(self):
        out = mod.synthetic_end_to_end()
        self.assertTrue(out["dropped_future_rejected"])
        self.assertTrue(out["dropped_feature_rejected"])

    def test_rjc_mutation_is_rejected(self):
        out = mod.synthetic_end_to_end()
        self.assertTrue(out["support_rewrite_exact"])
        self.assertTrue(out["unsafe_support_rewrite_rejected"])

    def test_interface_factor_mutation_is_rejected(self):
        out = mod.synthetic_end_to_end()
        self.assertTrue(out["interface_factor_exact"])
        self.assertTrue(out["truncated_interface_factor_rejected"])

    def test_mutation_suite(self):
        out = mod.mutation_suite()
        self.assertEqual(out["passed"], 5)
        self.assertEqual(out["total"], 5)


if __name__ == "__main__":
    unittest.main()
