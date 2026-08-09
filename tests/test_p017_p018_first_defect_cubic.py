import ast
import inspect
import unittest

from enterprise_math import p017_p018_first_defect_cubic as defect_cubic_module
from enterprise_math.p017_p018_first_defect_cubic import (
    first_band_order3_ambiguity_budget,
    first_band_order3_label_cutoff,
    odd_prime_power_base,
    residual_order3_defect_cubic_compression,
    transverse_odd_prime_power_labels,
)


class P017P018FirstDefectCubicTests(unittest.TestCase):
    def test_odd_prime_power_classifier(self):
        expected = {3: 3, 5: 5, 9: 3, 25: 5, 27: 3, 49: 7, 81: 3}
        for value, base in expected.items():
            self.assertEqual(odd_prime_power_base(value), base)
        for value in (1, 2, 12, 15, 21, 45, 75, 105):
            self.assertIsNone(odd_prime_power_base(value))

    def test_exact_label_cutoffs_and_transverse_budgets(self):
        self.assertEqual(
            first_band_order3_label_cutoff(65536),
            {
                "k": 65536,
                "cubic_partner_ambiguity_cutoff": 64,
                "four_prime_product_cutoff": 56,
                "unresolved_prime_power_label_cutoff": 56,
            },
        )
        budget = first_band_order3_ambiguity_budget(65536)
        self.assertEqual(
            budget["candidate_prime_power_labels"],
            (3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43, 47, 49, 53),
        )
        self.assertEqual(budget["candidate_label_count"], 19)

        self.assertEqual(
            transverse_odd_prime_power_labels(20_000, 17),
            (7, 11, 13, 17),
        )

    def test_k65536_r883_is_actual_unresolved_prime_power_defect(self):
        data = residual_order3_defect_cubic_compression(65_536, 883)
        self.assertEqual(data["small_core"], 13)
        self.assertEqual(data["large_core"], 4515)
        self.assertEqual(data["small_core_prime_base"], 13)
        self.assertEqual(data["total_pair_defect"], 1)
        self.assertFalse(data["fully_cubic_resolved"])
        self.assertTrue(data["inside_unresolved_prime_power_budget"])
        self.assertTrue(data["unresolved_prime_power_small_label"])
        self.assertLessEqual(data["small_core"], data["cubic_partner_ambiguity_cutoff"])

    def test_k131071_r17477_is_first_band_defect_but_already_cubic_resolved(self):
        data = residual_order3_defect_cubic_compression(131_071, 17_477)
        self.assertEqual(data["small_core"], 41)
        self.assertEqual(data["large_core"], 1155)
        self.assertEqual(data["small_core_prime_base"], 41)
        self.assertEqual(data["total_pair_defect"], 1)
        self.assertTrue(data["fully_cubic_resolved"])
        self.assertGreater(data["larger_base_root"], data["cubic_horizon"])

    def test_nondefect_residual_radius_is_rejected(self):
        with self.assertRaises(ValueError):
            residual_order3_defect_cubic_compression(20_000, 67)

    def test_band_boundary_is_enforced(self):
        with self.assertRaises(ValueError):
            first_band_order3_label_cutoff(15_015)
        with self.assertRaises(ValueError):
            first_band_order3_label_cutoff(255_256)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(defect_cubic_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
