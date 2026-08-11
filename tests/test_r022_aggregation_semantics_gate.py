import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_aggregation_semantics_gate.py"
spec = importlib.util.spec_from_file_location("r022_aggregation_semantics_gate", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class AggregationSemanticsGateTests(unittest.TestCase):
    def test_duplicate_forgetting_depends_on_idempotence(self):
        out = mod.duplicate_forgetting_examples()
        self.assertTrue(out["boolean_support_duplicate_forget_exact"])
        self.assertFalse(out["natural_multiplicity_duplicate_forget_exact"])
        self.assertTrue(out["min_score_duplicate_forget_exact"])

    def test_coefficients_repair_multiplicity_merge(self):
        out = mod.coefficient_preserving_merge()
        self.assertTrue(out["exact"])
        self.assertEqual(out["coefficient"], 4)

    def test_identity_pruning_is_generic(self):
        out = mod.zero_prune_examples()
        self.assertTrue(out["natural_zero_prune_exact"])
        self.assertTrue(out["boolean_bottom_prune_exact"])
        self.assertTrue(out["min_infinity_prune_exact"])

    def test_provenance_strengthening_kills_support_only_forgetting(self):
        out = mod.provenance_strengthening_kill()
        self.assertTrue(out["support_merge_exact"])
        self.assertFalse(out["provenance_forget_exact"])
        self.assertTrue(out["provenance_union_token_exact"])


if __name__ == "__main__":
    unittest.main()
