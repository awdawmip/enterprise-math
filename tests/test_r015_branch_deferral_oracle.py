import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r015_branch_deferral_oracle.py"
spec = importlib.util.spec_from_file_location("r015_oracle", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
import sys
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class R015OracleTests(unittest.TestCase):
    def test_arbitrary_union_relational_direct_image(self):
        for relation in mod.all_relations(2, 2):
            table = mod.relation_direct_image_table(relation)
            self.assertTrue(mod.preserves_arbitrary_unions(table, 2))
            self.assertTrue(mod.singleton_generated(table, 2))

    def test_composition_orientation_and_boolean_product(self):
        relations = mod.all_relations(2, 2)
        for first in relations:
            for second in relations:
                composed = mod.compose_relations(first, second)
                for support in mod.all_supports(2):
                    self.assertEqual(
                        mod.direct_image(support, composed),
                        mod.direct_image(mod.direct_image(support, first), second),
                    )
                rows = mod.boolean_matrix_product(
                    mod.relation_to_boolean_rows(first), 2, mod.relation_to_boolean_rows(second)
                )
                self.assertEqual(rows, mod.relation_to_boolean_rows(composed))

    def test_three_engines_full_two_state_horizon_four(self):
        summary = mod.exhaustive_two_state_relations(max_horizon=4)
        self.assertEqual(summary["relations"], 16)
        self.assertEqual(summary["initial_supports"], 4)
        self.assertEqual(summary["max_horizon"], 4)
        self.assertEqual(summary["engine_cases"], 279620)
        self.assertEqual(summary["bounded_representations_by_union"], {"0": 1, "1": 2, "2": 2, "3": 22})

    def test_transformer_characterization_x3_y2(self):
        summary = mod.exhaustive_transformer_characterization(max_x=3, max_y=2)
        self.assertEqual(summary["total_transformers"], 66094)
        self.assertEqual(summary["total_union_preserving"], 104)
        self.assertEqual(summary["total_singleton_generated"], 104)
        self.assertEqual(summary["total_binary_union_plus_empty"], 104)
        self.assertEqual(summary["per_size"]["X3_Y2"]["transformers"], 65536)
        self.assertEqual(summary["per_size"]["X3_Y2"]["union_preserving"], 64)

    def test_mutations_detect_divergence(self):
        result = mod.mutation_suite()
        self.assertEqual(result["detected_non_union_preserving"], 3)
        self.assertEqual(result["detected_eager_lazy_divergence"], 3)
        self.assertEqual(result["minimal_distinct_singleton_branch_failure"]["x_size"], 2)

    def test_randomized_larger_systems(self):
        result = mod.randomized_property_suite(seed=15015, trials=200)
        self.assertEqual(result["trials"], 200)
        self.assertGreaterEqual(result["max_states_seen"], 2)
        self.assertGreaterEqual(result["max_horizon_seen"], 1)

    def test_no_float_no_true_division(self):
        result = mod.no_float_or_true_division_audit(MODULE_PATH)
        self.assertEqual(result, {"float_constants": 0, "true_division_nodes": 0})


if __name__ == "__main__":
    unittest.main()
