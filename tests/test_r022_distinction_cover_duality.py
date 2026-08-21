import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_distinction_cover_duality.py"
spec = importlib.util.spec_from_file_location("r022_distinction_cover_duality", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class DistinctionCoverDualityTests(unittest.TestCase):
    def test_all_four_pair_set_families(self):
        out = mod.exhaustive_pairblock_reduction()
        self.assertEqual(out["nonempty_set_families"], 32767)
        self.assertEqual(out["coverable_families"], 32297)
        self.assertEqual(out["mismatches"], 0)

    def test_information_debt_can_be_smaller_than_extractor_complexity(self):
        out = mod.information_vs_extraction_witness()
        self.assertEqual(out["abstract_side_bits"], 1)
        self.assertEqual(out["minimum_future_probe_basis"], 4)
        self.assertEqual(out["minimum_raw_feature_basis"], 4)

    def test_md5_router_representation_classes_are_distinct(self):
        out = mod.md5_router_shape_note()
        self.assertEqual(out["source_shaped_raw_features"], 9)
        self.assertEqual(out["compiled_fixed_width_bits"], 3)

    def test_proof_carrying_basis_verification(self):
        out = mod.proof_carrying_basis_witness()
        self.assertTrue(out["suboptimal_basis_exact"])
        self.assertFalse(out["unsafe_truncation_exact"])


if __name__ == "__main__":
    unittest.main()
