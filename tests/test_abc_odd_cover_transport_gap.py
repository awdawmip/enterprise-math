import unittest
from fractions import Fraction

from enterprise_math.abc_odd_cover_transport_gap import odd_cover_transport_gap_state


class OddCoverTransportGapTests(unittest.TestCase):
    def test_nonresonant_squarefree_is_forced_attenuation(self) -> None:
        state = odd_cover_transport_gap_state(5, 59, 3, 3, "sum")
        self.assertEqual(state.two_bit_classifier, (False, True))
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, Fraction(1, 3))
        self.assertEqual(state.transport_class, "attenuated")

    def test_resonant_squarefree_is_forced_resonance(self) -> None:
        state = odd_cover_transport_gap_state(11, 13, 3, 3, "sum")
        self.assertEqual(state.two_bit_classifier, (True, True))
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, 1)
        self.assertEqual(state.transport_class, "resonant")

    def test_resonant_repeated_is_forced_amplification(self) -> None:
        state = odd_cover_transport_gap_state(7, 29, 3, 3, "sum")
        self.assertEqual(state.two_bit_classifier, (True, False))
        self.assertEqual(state.quotient_residual, 19)
        self.assertEqual(state.repeated_support_floor, 7)
        self.assertTrue(all(prime % 6 == 1 for prime in state.repeated_quotient_primes))
        self.assertEqual(state.inheritance_multiplier, 19)
        self.assertEqual(state.transport_class, "amplified")

    def test_nonresonant_repeated_is_forced_strong_amplification(self) -> None:
        state = odd_cover_transport_gap_state(3, 13, 3, 3, "difference")
        self.assertEqual(state.two_bit_classifier, (False, False))
        self.assertEqual(state.quotient_residual, 19)
        self.assertEqual(state.inheritance_multiplier, Fraction(19, 3))
        self.assertGreater(state.inheritance_multiplier, 2)
        self.assertEqual(state.transport_class, "amplified")

    def test_fifth_cover_repeated_support_is_one_mod_ten(self) -> None:
        resonant = odd_cover_transport_gap_state(19, 29, 2, 5, "difference")
        self.assertTrue(resonant.support_resonance)
        self.assertFalse(resonant.quotient_squarefree)
        self.assertEqual(resonant.quotient_residual, 121)
        self.assertIn(11, resonant.repeated_quotient_primes)
        self.assertEqual(resonant.inheritance_multiplier, 121)

        nonresonant = odd_cover_transport_gap_state(7, 47, 2, 5, "sum")
        self.assertFalse(nonresonant.support_resonance)
        self.assertFalse(nonresonant.quotient_squarefree)
        self.assertEqual(nonresonant.quotient_residual, 41)
        self.assertIn(41, nonresonant.repeated_quotient_primes)
        self.assertEqual(41 % 10, 1)
        self.assertEqual(nonresonant.inheritance_multiplier, Fraction(41, 5))
        self.assertGreater(nonresonant.inheritance_multiplier, 2)

    def test_no_weak_amplification_branch_survives(self) -> None:
        fixtures = [
            (7, 29, 3, 3, "sum"),
            (3, 13, 3, 3, "difference"),
            (19, 29, 2, 5, "difference"),
            (7, 47, 2, 5, "sum"),
        ]
        for fixture in fixtures:
            state = odd_cover_transport_gap_state(*fixture)
            if state.transport_class == "amplified" and not state.support_resonance:
                self.assertGreater(state.inheritance_multiplier, 2)


if __name__ == "__main__":
    unittest.main()
