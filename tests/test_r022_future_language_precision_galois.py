import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_future_language_precision_galois.py"
spec = importlib.util.spec_from_file_location("r022_future_language_precision_galois", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class FutureLanguagePrecisionGaloisTests(unittest.TestCase):
    def test_galois_and_closure_laws_exhaustive(self):
        out = mod.galois_exhaustive_model()
        self.assertEqual(out["galois_pairs_checked"], 960)
        self.assertEqual(out["language_union_pairs_checked"], 4096)
        self.assertEqual(out["single_operation_extensions_checked"], 384)
        self.assertFalse(out["counterexample"])

    def test_descent_operations_form_monoid(self):
        out = mod.descent_monoid_model()
        self.assertTrue(out["monoid"])
        self.assertEqual(out["composition_pairs_checked"], 248832)

    def test_observation_safe_operations_need_not_form_monoid(self):
        out = mod.observation_safe_nonmonoid_kill()
        self.assertTrue(out["no_counterexample_states_2"])
        self.assertEqual(out["minimal_counterexample_states"], 3)
        self.assertTrue(out["f_safe"])
        self.assertTrue(out["g_safe"])
        self.assertFalse(out["composition_safe"])

    def test_language_extension_is_local_kernel_split(self):
        out = mod.incremental_refinement_witness()
        self.assertTrue(out["local_split_law_holds"])
        self.assertNotEqual(out["old_kernel"], out["new_kernel"])


if __name__ == "__main__":
    unittest.main()
