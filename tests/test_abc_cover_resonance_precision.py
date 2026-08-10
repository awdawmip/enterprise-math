import unittest
from fractions import Fraction

from enterprise_math.abc_cover_resonance_precision import (
    cover_resonance_precision_state,
    ratio_resonates_mod_cover_prime,
    resonance_height_incidence_upper_bound,
)


class CoverResonancePrecisionTests(unittest.TestCase):
    def _enumerated_root_count(self, exponent: int, prime: int, mode: str) -> int:
        state = cover_resonance_precision_state(exponent, prime, mode)
        target = 1 if mode == "difference" else prime - 1
        return sum(pow(x, exponent, prime) == target for x in range(1, prime))

    def test_difference_root_count_is_gcd(self) -> None:
        state = cover_resonance_precision_state(6, 13, "difference")
        self.assertEqual(state.exponent_group_gcd, 6)
        self.assertEqual(state.resonance_class_count, 6)
        self.assertEqual(state.unit_ratio_density, Fraction(1, 2))
        self.assertEqual(self._enumerated_root_count(6, 13, "difference"), 6)

    def test_difference_resonance_can_saturate_all_unit_ratios(self) -> None:
        state = cover_resonance_precision_state(4, 5, "difference")
        self.assertEqual(state.resonance_class_count, 4)
        self.assertEqual(state.unit_ratio_density, 1)
        self.assertTrue(state.precision_saturated)
        self.assertEqual(self._enumerated_root_count(4, 5, "difference"), 4)

    def test_sum_resonance_can_be_empty(self) -> None:
        state = cover_resonance_precision_state(4, 5, "sum")
        self.assertFalse(state.solvable)
        self.assertEqual(state.resonance_class_count, 0)
        self.assertEqual(state.unit_ratio_density, 0)
        self.assertEqual(self._enumerated_root_count(4, 5, "sum"), 0)

    def test_sum_resonance_has_g_roots_when_solvable(self) -> None:
        state = cover_resonance_precision_state(2, 5, "sum")
        self.assertTrue(state.solvable)
        self.assertEqual(state.exponent_group_gcd, 2)
        self.assertEqual(state.resonance_class_count, 2)
        self.assertEqual(state.unit_ratio_density, Fraction(1, 2))
        self.assertFalse(state.precision_saturated)
        self.assertEqual(self._enumerated_root_count(2, 5, "sum"), 2)

    def test_stage87_three_to_nine_resonance_is_one_of_two_unit_classes(self) -> None:
        state = cover_resonance_precision_state(3, 3, "sum")
        self.assertEqual(state.resonance_class_count, 1)
        self.assertEqual(state.unit_ratio_density, Fraction(1, 2))
        self.assertTrue(ratio_resonates_mod_cover_prime(13, 11, state))
        self.assertFalse(ratio_resonates_mod_cover_prime(59, 5, state))

    def test_height_incidence_uses_only_resonant_unit_classes(self) -> None:
        # m=3, r=7: gcd(3,6)=3, so half of unit ratio classes resonate.
        state = cover_resonance_precision_state(3, 7, "difference")
        self.assertEqual(state.resonance_class_count, 3)
        bound = resonance_height_incidence_upper_bound(3, 7, "difference", 100)
        self.assertLess(bound, 100**2)
        self.assertEqual(bound, 3 * (100 - 100 // 7) * ((100 + 6) // 7))

    def test_base_equal_to_cover_prime_is_not_a_unit_resonance(self) -> None:
        state = cover_resonance_precision_state(4, 5, "difference")
        self.assertTrue(state.precision_saturated)
        self.assertFalse(ratio_resonates_mod_cover_prime(5, 3, state))


if __name__ == "__main__":
    unittest.main()
