import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "r022_structured_certificate_fastpaths.py"
spec = importlib.util.spec_from_file_location("r022_structured_certificate_fastpaths", MODULE_PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class StructuredCertificateFastPathTests(unittest.TestCase):
    def test_exhaustive_laminar_basis_theorem(self):
        r = m.exhaustive_laminar_theorem()
        self.assertEqual(r["laminar_families_tested"], 831)
        self.assertTrue(r["theorem_holds_in_exhaustive_model"])
        self.assertEqual(r["failures"], [])

    def test_laminar_examples(self):
        r = m.laminar_examples()
        self.assertEqual(r["chain_basis"], ["large"])
        self.assertEqual(r["chain_width"], 1)
        self.assertEqual(r["forest_basis"], ["a", "b"])
        self.assertEqual(r["forest_width"], 2)

    def test_prefix_certificate_reuse_depth(self):
        r = m.prefix_certificate_cache_model()
        self.assertEqual(r["certificate_reuse_depth"], 3)
        self.assertEqual(r["certificate_validity"], {"1": True, "3": True, "4": False, "5": False})

    def test_noncumulative_footprint_kills_refinement_tree(self):
        r = m.noncumulative_footprint_kill()
        self.assertFalse(r["depth2_refines_depth1"])


if __name__ == "__main__":
    unittest.main()
