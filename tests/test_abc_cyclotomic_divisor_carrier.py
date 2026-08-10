import unittest
from fractions import Fraction

from enterprise_math.abc_cyclotomic_divisor_carrier import (
    cyclotomic_divisor_carrier_state,
    cyclotomic_index_set,
    top_cyclotomic_carrier,
)


class CyclotomicDivisorCarrierTests(unittest.TestCase):
    def test_sign_specific_index_sets(self) -> None:
        self.assertEqual(cyclotomic_index_set(3, "difference"), (1, 3))
        self.assertEqual(cyclotomic_index_set(3, "sum"), (2, 6))
        self.assertEqual(cyclotomic_index_set(4, "difference"), (1, 2, 4))
        self.assertEqual(cyclotomic_index_set(4, "sum"), (8,))
        self.assertEqual(cyclotomic_index_set(9, "difference"), (1, 3, 9))
        self.assertEqual(cyclotomic_index_set(9, "sum"), (2, 6, 18))

    def test_prime_exponent_cube_sum_top_layer_is_forced(self) -> None:
        state = cyclotomic_divisor_carrier_state(11, 13, 3, "sum")
        self.assertEqual(state.index_set, (2, 6))
        self.assertEqual(state.overlap_factor, 3)
        self.assertEqual(state.projective_ratio, Fraction(7, 6))
        top = top_cyclotomic_carrier(state)
        self.assertEqual(top.selected_indices, (6,))
        self.assertEqual(top.outside_carrier, 12)
        self.assertLess(top.outside_carrier, state.projective_denominator)
        self.assertTrue(top.selected_repetition_forced_by_margin)
        self.assertTrue(top.selected_actually_repeated)

    def test_prime_exponent_fifth_difference_top_layer_is_forced(self) -> None:
        state = cyclotomic_divisor_carrier_state(19, 29, 5, "difference")
        self.assertEqual(state.index_set, (1, 5))
        self.assertEqual(state.overlap_factor, 5)
        self.assertEqual(state.projective_ratio, Fraction(121, 48))
        top = top_cyclotomic_carrier(state)
        self.assertTrue(top.selected_repetition_forced_by_margin)
        self.assertGreater(top.selected_residual_product, 1)

    def test_fourth_power_difference_top_forcing_fails_exactly(self) -> None:
        state = cyclotomic_divisor_carrier_state(23, 41, 4, "difference")
        self.assertEqual(state.index_set, (1, 2, 4))
        self.assertEqual(state.overlap_factor, 4)
        self.assertEqual(state.projective_ratio, Fraction(3, 2))
        top = top_cyclotomic_carrier(state)
        self.assertEqual(top.selected_indices, (4,))
        self.assertEqual(top.selected_residual_product, 1)
        self.assertEqual(top.outside_carrier, state.active_residual)
        self.assertGreaterEqual(top.outside_carrier, state.projective_denominator)
        self.assertFalse(top.selected_repetition_forced_by_margin)
        self.assertFalse(top.selected_actually_repeated)

    def test_fourth_power_sum_single_layer_forces_top(self) -> None:
        state = cyclotomic_divisor_carrier_state(839, 1277, 4, "sum")
        self.assertEqual(state.index_set, (8,))
        self.assertEqual(state.overlap_factor, 1)
        top = top_cyclotomic_carrier(state)
        self.assertEqual(top.outside_carrier, 1)
        self.assertTrue(top.selected_repetition_forced_by_margin)
        self.assertTrue(top.selected_actually_repeated)

    def test_ninth_power_difference_inherits_lower_cube_pressure(self) -> None:
        state = cyclotomic_divisor_carrier_state(23, 71, 9, "difference")
        self.assertEqual(state.index_set, (1, 3, 9))
        self.assertEqual(state.overlap_factor, 3**2)
        self.assertEqual(state.projective_ratio, Fraction(1372, 47))
        layer = {item.index: item for item in state.layers}
        self.assertTrue(layer[9].squarefree)
        self.assertEqual(layer[9].residual, 1)
        self.assertEqual(layer[9].value, 3 * 811 * 54501859)
        top = top_cyclotomic_carrier(state)
        self.assertFalse(top.selected_repetition_forced_by_margin)
        self.assertFalse(top.selected_actually_repeated)
        self.assertEqual(top.outside_carrier, state.active_residual)

    def test_ninth_power_sum_inherits_lower_cube_pressure(self) -> None:
        state = cyclotomic_divisor_carrier_state(11, 13, 9, "sum")
        self.assertEqual(state.index_set, (2, 6, 18))
        self.assertEqual(state.overlap_factor, 3**2)
        self.assertEqual(state.projective_ratio, Fraction(7, 6))
        layer = {item.index: item for item in state.layers}
        self.assertTrue(layer[18].squarefree)
        self.assertEqual(layer[18].residual, 1)
        self.assertEqual(layer[18].value, 3 * 19 * 73 * 883)
        top = top_cyclotomic_carrier(state)
        self.assertFalse(top.selected_repetition_forced_by_margin)
        self.assertFalse(top.selected_actually_repeated)


if __name__ == "__main__":
    unittest.main()
