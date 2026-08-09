import ast
import inspect
import unittest

from enterprise_math import p017_p018_bonferroni_tokens as token_module
from enterprise_math.p017_p018_bonferroni_tokens import (
    defect_token_quotient_descent,
    defect_token_quotient_horizon,
    defect_token_single_use_threshold,
    point_defect_tokens,
    point_full_block_defect_tokens,
    signed_defect_token_profile,
)


class P017P018BonferroniTokenTests(unittest.TestCase):
    def test_order_three_point_defect_has_exact_four_squarefree_tokens(self):
        data = point_defect_tokens((3, 5, 7, 11, 13), 3)
        self.assertEqual(data["defect"], 4)
        self.assertEqual(data["least_support_prime"], 3)
        self.assertEqual(data["tokens"], (1155, 1365, 2145, 3003))

    def test_order_five_six_support_row_has_one_full_product_token(self):
        support = (3, 7, 11, 23, 37, 7283)
        data = point_defect_tokens(support, 5)
        product = 1
        for prime in support:
            product *= prime
        self.assertEqual(data["defect"], 1)
        self.assertEqual(data["tokens"], (product,))

    def test_full_prime_power_block_removal_collapses_actual_six_support_state_to_one(self):
        state = 4_295_098_269  # 3^2*7*11*23*37*7283
        support = (3, 7, 11, 23, 37, 7283)
        data = point_full_block_defect_tokens(65_536, state, support, 5)
        self.assertEqual(data["defect"], 1)
        self.assertEqual(len(data["token_rows"]), 1)
        row = data["token_rows"][0]
        self.assertEqual(row["squarefree_token"], 1_431_699_423)
        self.assertEqual(row["full_block_token"], state)
        self.assertEqual(row["quotient"], 1)
        self.assertEqual(row["omitted_support_primes"], ())
        self.assertTrue(row["single_use_product_regime"])
        self.assertTrue(row["fully_k_smooth"])
        self.assertEqual(row["quotient_support"], ())

    def test_defect_free_rows_have_no_tokens(self):
        for support in ((), (3,), (3, 5, 7), (3, 5, 7, 11, 13)):
            data = point_defect_tokens(support, 5)
            self.assertEqual(data["defect"], 0)
            self.assertEqual(data["tokens"], ())

    def test_whole_profile_token_mass_equals_exact_bonferroni_defect(self):
        for k in (31, 64, 127):
            data = signed_defect_token_profile(k, 3)
            self.assertEqual(data["defect_token_count"], data["high_support_defect"])
            for row in data["defect_rows"]:
                self.assertEqual(len(row["tokens"]), row["defect"])

    def test_order_five_token_single_use_threshold_matches_scale_transition(self):
        for k in (65_536, 131_071, 255_255):
            data = defect_token_single_use_threshold(k, 5)
            expected_primes = (
                (3, 5, 7, 11, 13, 17)
                if k != 255_255
                else (19, 23, 29, 31, 37, 41)
            )
            self.assertEqual(data["minimum_transverse_token_primes"], expected_primes)
            self.assertTrue(data["all_defect_tokens_globally_single_use_by_p017_capacity"])

        data = defect_token_single_use_threshold(524_287, 5)
        self.assertEqual(data["minimum_transverse_token_product"], 255_255)
        self.assertFalse(data["all_defect_tokens_globally_single_use_by_p017_capacity"])

    def test_minimum_token_product_gives_exact_quotient_horizon(self):
        data = defect_token_quotient_horizon(65_536, 5)
        self.assertEqual(data["minimum_transverse_token_product"], 255_255)
        self.assertEqual(data["quotient_ceiling"], 16_826)
        self.assertEqual(data["quotient_root_ceiling"], 129)
        self.assertTrue(data["strict_parent_scale_descent"])

        data = defect_token_quotient_horizon(255_255, 5)
        self.assertEqual(data["minimum_transverse_token_product"], 595_973_171)
        self.assertEqual(data["quotient_ceiling"], 109)
        self.assertEqual(data["quotient_root_ceiling"], 10)
        self.assertTrue(data["strict_parent_scale_descent"])

        data = defect_token_quotient_horizon(524_287, 5)
        self.assertEqual(data["quotient_ceiling"], 1_076_875)
        self.assertFalse(data["strict_parent_scale_descent"])

    def test_actual_large_order_five_squarefree_token_descends_to_small_integer_quotient(self):
        state = 4_295_098_269
        divisor = 1_431_699_423  # 3*7*11*23*37*7283
        data = defect_token_quotient_descent(65_536, state, divisor)
        self.assertEqual(data["quotient"], 3)
        self.assertEqual(data["quotient_root"], 1)
        self.assertTrue(data["strict_parent_scale_descent"])

    def test_invalid_support(self):
        with self.assertRaises(ValueError):
            point_defect_tokens((3, 3, 5), 3)
        with self.assertRaises(ValueError):
            point_defect_tokens((2, 3, 5, 7), 3)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(token_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
