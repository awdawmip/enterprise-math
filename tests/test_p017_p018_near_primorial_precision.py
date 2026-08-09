import ast
import inspect
import unittest

from enterprise_math import p017_p018_near_primorial_precision as near_module
from enterprise_math.p017_p018_near_primorial_precision import (
    near_primorial_adaptive_order,
    reusable_near_primorial_block_shape,
)


class P017P018NearPrimorialPrecisionTests(unittest.TestCase):
    def test_parity_rule_selects_terminal_residual_order(self):
        expected = {
            8_191: (4, 3, "EVEN", False),
            20_000: (4, 3, "EVEN", False),
            65_536: (5, 5, "ODD", True),
            131_071: (5, 5, "ODD", True),
            255_255: (3, 3, "ODD", True),
            524_287: (6, 5, "EVEN", False),
        }
        for k, (j, order, parity, globally_exact) in expected.items():
            data = near_primorial_adaptive_order(k)
            self.assertEqual(data["transverse_primorial_depth"], j)
            self.assertEqual(data["adaptive_odd_order"], order)
            self.assertEqual(data["J_parity"], parity)
            self.assertEqual(data["globally_exact_product_adaptive_majorant"], globally_exact)
            self.assertTrue(data["residual_ordinary_bonferroni_exact"])

    def test_odd_J_has_no_reusable_product_adaptive_shell(self):
        for k in (65_536, 131_071, 255_255):
            data = near_primorial_adaptive_order(k)
            self.assertEqual(data["remaining_error_shell"], "NONE")
            self.assertGreaterEqual(data["minimum_selected_product"], k)

    def test_even_J_reusable_blocks_have_exactly_J_distinct_primes(self):
        # k=524287 has J=6.  The known reusable block 285285 has
        # radical primes 3,5,7,11,13,19.
        data = reusable_near_primorial_block_shape(524_287, 285_285)
        self.assertEqual(data["transverse_primorial_depth"], 6)
        self.assertEqual(data["adaptive_odd_order"], 5)
        self.assertEqual(data["radical_primes"], (3, 5, 7, 11, 13, 19))
        self.assertEqual(data["radical_prime_count"], 6)
        self.assertTrue(data["terminal_J_prime_shell"])

        # Prime powers are allowed so long as the radical still has J primes.
        data = reusable_near_primorial_block_shape(8_191, 3 * 5 * 7 * 11)
        self.assertEqual(data["radical_prime_count"], 4)

    def test_wrong_radical_depth_is_rejected(self):
        with self.assertRaises(ValueError):
            reusable_near_primorial_block_shape(524_287, 255_255 // 17)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(near_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
