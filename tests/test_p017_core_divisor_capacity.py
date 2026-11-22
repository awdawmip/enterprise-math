import ast
import inspect
import unittest

from enterprise_math import p017_core_divisor_capacity as capacity_module
from enterprise_math.p017_core_divisor_capacity import (
    raw_signed_divisor_points,
    selected_signed_divisor_incidence_capacity,
    signed_divisor_capacity,
    signed_divisor_residue,
)


class P017CoreDivisorCapacityTests(unittest.TestCase):
    def test_composite_squarefree_divisor_uses_one_mod_2d_class(self):
        data = signed_divisor_residue(31, 15)
        self.assertEqual(data["residue"], 17)
        self.assertEqual(data["modulus"], 30)
        self.assertEqual(raw_signed_divisor_points(31, 15), (-13, 17))

        capacity = signed_divisor_capacity(31, 15)
        self.assertEqual(capacity["raw_signed_points"], (-13, 17))
        self.assertEqual(capacity["anchor_signed_points"], (-13, 17))
        self.assertEqual(capacity["exact_aligned_capacity"], 2)
        self.assertEqual(capacity["exact_anchor_capacity"], 2)
        self.assertEqual(capacity["universal_capacity"], 3)

    def test_alignment_can_strictly_improve_universal_capacity(self):
        data = signed_divisor_capacity(20_000, 17_017)
        self.assertEqual(data["exact_aligned_capacity"], 1)
        self.assertEqual(data["exact_anchor_capacity"], 1)
        self.assertEqual(data["universal_capacity"], 2)
        self.assertEqual(data["anchor_signed_points"], (1_381,))

    def test_anchor_filter_can_strictly_improve_aligned_capacity(self):
        data = signed_divisor_capacity(20_000, 19_019)
        self.assertEqual(data["raw_signed_points"], (-6_627,))
        self.assertEqual(data["exact_aligned_capacity"], 1)
        self.assertEqual(data["exact_anchor_capacity"], 0)
        self.assertEqual(data["universal_capacity"], 2)

    def test_divisor_above_radius_range_is_globally_single_use(self):
        data = signed_divisor_capacity(31, 35)
        self.assertEqual(data["raw_signed_points"], (-23,))
        self.assertEqual(data["anchor_signed_points"], (-23,))
        self.assertEqual(data["universal_capacity"], 1)
        self.assertTrue(data["globally_single_use"])

    def test_prime_power_is_included_as_special_case(self):
        data = signed_divisor_capacity(64, 27)
        self.assertLessEqual(data["exact_anchor_capacity"], data["exact_aligned_capacity"])
        self.assertLessEqual(data["exact_aligned_capacity"], (64 - 1) // 27 + 1)
        self.assertEqual(data["signed_modulus"], 54)

    def test_selected_incidence_family_obeys_exact_anchor_capacity(self):
        data = selected_signed_divisor_incidence_capacity(31, 15, (-13, 17))
        self.assertEqual(data["selected_count"], 2)
        self.assertEqual(data["exact_anchor_capacity"], 2)
        self.assertEqual(data["universal_capacity"], 3)

    def test_anchor_filter_only_removes_raw_points(self):
        for k, divisor in ((31, 15), (64, 27), (631, 35), (631, 49)):
            data = signed_divisor_capacity(k, divisor)
            self.assertLessEqual(data["anchor_count"], data["raw_count"])
            self.assertLessEqual(data["raw_count"], data["universal_capacity"])

    def test_invalid_nontransverse_divisor(self):
        with self.assertRaises(ValueError):
            signed_divisor_capacity(31, 31)
        with self.assertRaises(ValueError):
            signed_divisor_capacity(31, 2)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(capacity_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
