import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_adaptive_signature_acquisition.py"
spec = importlib.util.spec_from_file_location("r022_adaptive_signature_acquisition", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class AdaptiveSignatureAcquisitionTests(unittest.TestCase):
    def test_md5_source_shaped_adaptive_costs(self):
        out = mod.md5_adaptive_model()
        self.assertEqual(out["static_raw_signature_bits"], 9)
        self.assertEqual(out["source_short_circuit_average_cached_raw_reads"], 3.015625)
        self.assertEqual(out["optimal_adaptive_expected_raw_reads_uniform"], 2.140625)
        self.assertEqual(out["optimal_adaptive_worst_raw_reads"], 9)

    def test_expected_optimal_depth_distribution(self):
        out = mod.md5_adaptive_model()
        self.assertEqual(out["optimal_adaptive_depth_distribution"], {1: 256, 2: 128, 3: 64, 5: 32, 6: 16, 8: 8, 9: 8})

    def test_source_short_circuit_is_exact_but_not_expected_optimal(self):
        out = mod.md5_adaptive_model()
        self.assertGreater(out["source_short_circuit_average_cached_raw_reads"], out["optimal_adaptive_expected_raw_reads_uniform"])

    def test_leaf_purity_verifier(self):
        out = mod.purity_verifier()
        self.assertTrue(out["all_leaves_route_pure"])
        self.assertEqual(out["covered_assignments"], 512)


if __name__ == "__main__":
    unittest.main()
