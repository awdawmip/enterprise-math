import ast
import inspect
import unittest

from enterprise_math import p017_high_product_square_decoder as decoder_module
from enterprise_math.p017_high_product_square_decoder import (
    selected_residual_divisor_square_decoder,
)


class P017HighProductSquareDecoderTests(unittest.TestCase):
    def test_even_multiple_ambiguity_is_removed_by_odd_partner_parity(self):
        # The raw decoder interval contains 33*46 and 33*47, but only the odd
        # partner quotient 47 is admissible.
        data = selected_residual_divisor_square_decoder(49, 41, 33, 47)
        self.assertEqual(data["square_root"], 62)
        self.assertEqual(data["candidate_multiples_of_A"], (1518, 1551))
        self.assertEqual(data["candidate_odd_partner_products"], (1551,))
        self.assertEqual(data["decoded_partner_factor"], 47)
        self.assertEqual(data["remaining_repair_bits"], 0)

    def test_j4_collision_boundary_still_decodes_zero_repair(self):
        # At k=1951 the raw A-multiple window again has two consecutive
        # quotient values, 1668 and 1669.  Odd parity selects the true factor.
        data = selected_residual_divisor_square_decoder(1_951, -1_363, 1_365, 1_669)
        self.assertEqual(data["candidate_multiples_of_A"], (2_276_820, 2_278_185))
        self.assertEqual(data["candidate_odd_partner_products"], (2_278_185,))
        self.assertEqual(data["decoded_product"], 2_278_185)

    def test_large_product_with_wide_raw_integer_window_is_selected_by_A(self):
        data = selected_residual_divisor_square_decoder(8_191, -6_193, 7_035, 3_719)
        self.assertEqual(data["combined_product"], 26_163_165)
        self.assertEqual(data["square_root"], 13_118)
        self.assertTrue(data["decoder_width_less_than_2A"])
        self.assertEqual(data["candidate_odd_partner_products"], (26_163_165,))

    def test_known_same_product_duplicate_splits_decode_same_S_from_different_A(self):
        left = selected_residual_divisor_square_decoder(9_070, 233, 6_279, 11)
        right = selected_residual_divisor_square_decoder(9_070, 779, 3_003, 23)
        self.assertEqual(left["combined_product"], 69_069)
        self.assertEqual(right["combined_product"], 69_069)
        self.assertEqual(left["square_root"], right["square_root"])
        self.assertEqual(left["remaining_repair_bits"], 0)
        self.assertEqual(right["remaining_repair_bits"], 0)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(decoder_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
