import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_checkpoint_sufficiency_frontier.py"
spec = importlib.util.spec_from_file_location("r022_checkpoint_sufficiency_frontier", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class CheckpointSufficiencyFrontierTests(unittest.TestCase):
    def test_general_side_information_formula_all_partition_pairs(self):
        out = mod.exhaustive_arbitrary_partition_debt()
        self.assertEqual(out["ordered_partition_pairs"], 2704)
        self.assertEqual(out["zero_debt_pairs"], 358)
        self.assertFalse(out["counterexample"])

    def test_latest_information_sufficient_checkpoint(self):
        out = mod.nested_checkpoint_frontier()
        self.assertEqual(out["latest_sufficient_checkpoint_without_extra_metadata"], 1)
        self.assertEqual(out["minimal_rewind_depth_without_extra_metadata"], 2)

    def test_storage_rewind_pareto(self):
        out = mod.nested_checkpoint_frontier()
        pts = [(r["minimum_fixed_side_bits"], r["rewind_depth"]) for r in out["storage_rewind_pareto"]]
        self.assertEqual(pts, [(0, 2), (1, 1), (2, 0)])

    def test_metadata_moves_recovery_point_forward(self):
        out = mod.latest_sufficient_theorem_witness()
        self.assertTrue(out["checkpoint_1_zero_bits_depth_2"])
        self.assertTrue(out["checkpoint_2_one_bit_depth_1"])
        self.assertTrue(out["checkpoint_3_two_bits_depth_0"])


if __name__ == "__main__":
    unittest.main()
