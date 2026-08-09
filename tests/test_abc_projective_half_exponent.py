import unittest
from fractions import Fraction

from enterprise_math.abc_projective_half_exponent import (
    HALF,
    direct_global_projective_eta_threshold_from_oesterle,
    masser_abc_can_force_projective_eta,
    pcc_eta_implies_oesterle_below_two,
    pcc_oesterle_threshold,
)


class AbcProjectiveHalfExponentTests(unittest.TestCase):
    def test_direct_threshold_tends_to_half_as_M_tends_to_one(self) -> None:
        self.assertEqual(
            direct_global_projective_eta_threshold_from_oesterle(Fraction(3, 2)),
            Fraction(5, 6),
        )
        close = direct_global_projective_eta_threshold_from_oesterle(Fraction(101, 100))
        self.assertGreater(close, HALF)
        self.assertLess(close, Fraction(52, 100))

    def test_pcc_below_half_implies_an_oesterle_exponent_below_two(self) -> None:
        eta = Fraction(49, 100)
        self.assertTrue(pcc_eta_implies_oesterle_below_two(eta))
        self.assertEqual(pcc_oesterle_threshold(eta), Fraction(100, 51))
        self.assertLess(pcc_oesterle_threshold(eta), 2)

    def test_pcc_at_or_above_half_does_not_cross_below_two_by_this_map(self) -> None:
        self.assertFalse(pcc_eta_implies_oesterle_below_two(Fraction(1, 2)))
        self.assertFalse(pcc_eta_implies_oesterle_below_two(Fraction(3, 5)))

    def test_full_abc_exponent_family_can_force_any_target_above_half(self) -> None:
        for target in (Fraction(51, 100), Fraction(3, 5), Fraction(3, 4)):
            M, threshold = masser_abc_can_force_projective_eta(target)
            self.assertGreater(M, 1)
            self.assertLess(M, 2)
            self.assertLess(threshold, target)


if __name__ == "__main__":
    unittest.main()
