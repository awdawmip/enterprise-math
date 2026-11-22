import ast
import inspect
import unittest

from enterprise_math import p017_p018_product_adaptive_bonferroni as adaptive_module
from enterprise_math.p017_p018_product_adaptive_bonferroni import (
    product_adaptive_point_majorant,
    product_adaptive_signed_profile,
    product_adaptive_uniform_exactness,
)


class P017P018ProductAdaptiveBonferroniTests(unittest.TestCase):
    def test_uniform_high_product_threshold_can_make_order_one_exact(self):
        # k=18 has first two transverse odd primes 5,7, product 35>17.
        # State 325=5^2*13 has ordinary order-one defect one, so this is
        # non-vacuous: the high-product correction removes a real defect token.
        uniform = product_adaptive_uniform_exactness(18, 1)
        self.assertEqual(uniform["minimum_transverse_token_primes"], (5, 7))
        self.assertEqual(uniform["minimum_transverse_token_product"], 35)
        self.assertTrue(uniform["product_adaptive_majorant_uniformly_exact"])

        row = product_adaptive_point_majorant(18, 325, (5, 13), 1)
        self.assertEqual(row["ordinary_bonferroni_value"], 2)
        self.assertEqual(row["ordinary_defect"], 1)
        self.assertEqual(row["high_product_token_count"], 1)
        self.assertEqual(row["reusable_token_count"], 0)
        self.assertEqual(row["product_adaptive_value"], 1)
        self.assertTrue(row["pointwise_exact"])

        profile = product_adaptive_signed_profile(18, 1)
        self.assertGreater(profile["ordinary_bonferroni_sum"], profile["exact_nonempty_union"])
        self.assertEqual(profile["product_adaptive_sum"], profile["exact_nonempty_union"])
        self.assertEqual(profile["reusable_token_excess"], 0)
        self.assertTrue(profile["pointwise_exact_on_all_rows"])

    def test_mixed_high_and_reusable_tokens_leave_exact_reusable_excess(self):
        # k=22, n=525=3*5^2*7.  Order one fixes least prime 3 and gives
        # tokens {3,5} and {3,7}.  Full blocks are 75 (>21) and 21 (=21).
        # So one token is removed and exactly one reusable unit remains.
        row = product_adaptive_point_majorant(22, 525, (3, 5, 7), 1)
        self.assertEqual(row["ordinary_bonferroni_value"], 3)
        self.assertEqual(row["ordinary_defect"], 2)
        self.assertEqual(row["high_product_token_count"], 1)
        self.assertEqual(row["reusable_token_count"], 1)
        self.assertEqual(row["product_adaptive_value"], 2)
        self.assertEqual(row["product_adaptive_excess"], 1)
        self.assertFalse(row["pointwise_exact"])
        self.assertEqual(row["high_product_tokens"][0]["full_block_token"], 75)
        self.assertEqual(row["reusable_tokens"][0]["full_block_token"], 21)

    def test_prime_row_remains_zero(self):
        row = product_adaptive_point_majorant(22, 503, (), 3)
        self.assertEqual(row["nonempty_indicator"], 0)
        self.assertEqual(row["product_adaptive_value"], 0)
        self.assertTrue(row["pointwise_exact"])

    def test_adjusted_majorant_never_drops_below_exact_union_bounded(self):
        for k in range(4, 28):
            for order in (1, 3):
                profile = product_adaptive_signed_profile(k, order)
                self.assertGreaterEqual(
                    profile["product_adaptive_sum"],
                    profile["exact_nonempty_union"],
                )
                self.assertEqual(
                    profile["product_adaptive_sum"] - profile["exact_nonempty_union"],
                    profile["reusable_token_excess"],
                )

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(adaptive_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
