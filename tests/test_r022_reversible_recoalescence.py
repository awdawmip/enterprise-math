import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_reversible_recoalescence.py"
spec = importlib.util.spec_from_file_location("r022_reversible_recoalescence", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class ReversibleRecoalescenceTests(unittest.TestCase):
    def test_add_descends_but_delete_does_not(self):
        add_ok, _ = mod.descends_through_support(mod.add_one)
        delete_ok, witness = mod.descends_through_support(mod.delete_one)
        self.assertTrue(add_ok)
        self.assertFalse(delete_ok)
        self.assertEqual(witness[0:2], (1, 2))

    def test_deletion_horizon_token_is_future_equivalence(self):
        for h in range(0, 9):
            ok, classes = mod.verify_deletion_token_coarsest(h)
            self.assertTrue(ok)
            self.assertEqual(classes, h + 2)

    def test_stage_aware_delete_transition(self):
        ok, witness = mod.verify_stage_aware_transition()
        self.assertTrue(ok, witness)

    def test_horizon_extension_only_splits_saturated_class(self):
        out = mod.verify_saturated_class_refinement(2, 5)
        self.assertTrue(out["nonsaturated_classes_unchanged"])
        self.assertTrue(out["matches_expected"])
        self.assertEqual(out["old_saturated_class_refines_to"], (3, 4, 5, 6))

    def test_no_resurrection_on_language_extension(self):
        out = mod.no_resurrection_extension_witness(2, 3)
        self.assertTrue(out["old_token_equal"])
        self.assertFalse(out["new_token_equal"])
        self.assertTrue(out["old_signatures_equal"])
        self.assertFalse(out["new_signatures_equal"])


if __name__ == "__main__":
    unittest.main()
