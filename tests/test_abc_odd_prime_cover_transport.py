import unittest
from fractions import Fraction

from enterprise_math.abc_odd_prime_cover_transport import (
    cover_resonance_congruence_holds,
    odd_prime_cover_transport_state,
)


class OddPrimeCoverTransportTests(unittest.TestCase):
    def test_nonresonant_squarefree_quotient_attenuates_by_one_over_r(self) -> None:
        state = odd_prime_cover_transport_state(5, 59, 3, 3, "sum")
        self.assertFalse(state.resonance_support)
        self.assertEqual(state.ancestor_quotient_gcd, 1)
        self.assertEqual(state.overlap_factor, 1)
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, Fraction(1, 3))
        self.assertEqual(state.transport_class, "attenuated")
        self.assertEqual(state.quotient_cover_prime_valuation, 0)
        self.assertTrue(cover_resonance_congruence_holds(state))

    def test_resonant_squarefree_quotient_is_exactly_preserved(self) -> None:
        state = odd_prime_cover_transport_state(11, 13, 3, 3, "sum")
        self.assertTrue(state.resonance_support)
        self.assertEqual(state.ancestor_quotient_gcd, 3)
        self.assertEqual(state.overlap_factor, 3)
        self.assertEqual(state.quotient_cover_prime_valuation, 1)
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, 1)
        self.assertEqual(state.transport_class, "resonant")
        self.assertTrue(state.normalization_cancelled)
        self.assertTrue(cover_resonance_congruence_holds(state))

    def test_resonant_repeated_quotient_amplifies_by_its_residual(self) -> None:
        state = odd_prime_cover_transport_state(7, 29, 3, 3, "sum")
        self.assertTrue(state.resonance_support)
        self.assertEqual(state.overlap_factor, 3)
        self.assertEqual(state.quotient_residual, 19)
        self.assertEqual(state.inheritance_multiplier, 19)
        self.assertEqual(state.transport_class, "amplified")
        self.assertTrue(cover_resonance_congruence_holds(state))

    def test_nonresonant_repeated_quotient_can_still_amplify(self) -> None:
        state = odd_prime_cover_transport_state(3, 13, 3, 3, "difference")
        self.assertFalse(state.resonance_support)
        self.assertEqual(state.overlap_factor, 1)
        self.assertEqual(state.quotient_residual, 19)
        self.assertEqual(state.inheritance_multiplier, Fraction(19, 3))
        self.assertEqual(state.transport_class, "amplified")
        self.assertTrue(cover_resonance_congruence_holds(state))

    def test_odd_cover_resonance_is_conditional_not_universal(self) -> None:
        resonant = odd_prime_cover_transport_state(11, 13, 3, 3, "sum")
        nonresonant = odd_prime_cover_transport_state(5, 59, 3, 3, "sum")
        self.assertTrue(resonant.resonance_support)
        self.assertFalse(nonresonant.resonance_support)

    def test_even_cover_is_outside_this_module(self) -> None:
        with self.assertRaises(ValueError):
            odd_prime_cover_transport_state(3, 5, 2, 2, "difference")


if __name__ == "__main__":
    unittest.main()
