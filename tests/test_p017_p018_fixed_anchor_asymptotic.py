import ast
import inspect
import unittest

from enterprise_math import p017_p018_fixed_anchor_asymptotic as asymptotic_module
from enterprise_math.p017_p018_fixed_anchor_asymptotic import (
    fixed_anchor_log2_coefficient,
    leading_prime_power_value,
    split_correction_prime_power_value,
)


class P017P018FixedAnchorAsymptoticTests(unittest.TestCase):
    def test_allowed_prime_values_match_r2_and_r1_layers(self):
        self.assertEqual(leading_prime_power_value(3), (4, 1))
        self.assertEqual(leading_prime_power_value(5), (8, 3))
        self.assertEqual(split_correction_prime_power_value(3), (2, 1))
        self.assertEqual(split_correction_prime_power_value(5), (4, 3))

    def test_fixed_anchor_coefficient_is_delta_squared_over_eight(self):
        empty = fixed_anchor_log2_coefficient(())
        self.assertEqual(empty["log2_leading_coefficient"], (1, 8))
        self.assertEqual(empty["analytic_scope"], "FIXED_M")
        self.assertFalse(empty["moving_M_uniformity"])

        data = fixed_anchor_log2_coefficient((3, 5, 7))
        self.assertEqual(data["odd_anchor_density"], (16, 35))
        self.assertEqual(data["log2_leading_coefficient"], (32, 1225))

    def test_invalid_prime_is_rejected(self):
        with self.assertRaises(ValueError):
            leading_prime_power_value(9)
        with self.assertRaises(ValueError):
            split_correction_prime_power_value(2)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(asymptotic_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
