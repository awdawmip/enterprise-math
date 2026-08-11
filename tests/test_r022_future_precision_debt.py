import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_future_precision_debt.py"
spec = importlib.util.spec_from_file_location("r022_future_precision_debt", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class FuturePrecisionDebtTests(unittest.TestCase):
    def test_all_five_state_refinement_pairs(self):
        out = mod.exhaustive_refinement_debt()
        self.assertEqual(out["partitions"], 52)
        self.assertEqual(out["refinement_pairs"], 358)
        self.assertFalse(out["counterexample"])

    def test_debt_composes_along_refinement_chains(self):
        out = mod.exhaustive_debt_composition()
        self.assertEqual(out["refinement_triples"], 1304)
        self.assertTrue(out["split_count_composition_exact"])
        self.assertTrue(out["alphabet_size_submultiplicative"])
        self.assertTrue(out["fixed_width_bits_subadditive"])

    def test_bounded_deletion_debt(self):
        out = mod.bounded_deletion_debt(2, 5)
        self.assertEqual(out["new_subclasses_inside_old_saturated_class"], 4)
        self.assertEqual(out["minimum_fixed_width_side_bits"], 2)

    def test_zero_metadata_iff_no_split(self):
        out = mod.no_metadata_no_split_law()
        self.assertTrue(out["zero_bit_same_partition"])
        self.assertFalse(out["zero_bit_refined_partition"])
        self.assertEqual(out["refined_debt_bits"], 1)


if __name__ == "__main__":
    unittest.main()
