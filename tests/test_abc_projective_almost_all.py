import unittest
from fractions import Fraction

from enterprise_math.abc_projective_almost_all import (
    almost_all_oesterle_exponent,
    near_optimal_pcc_eta,
    pcc_eta_margin_for_oesterle,
)


class AbcProjectiveAlmostAllTests(unittest.TestCase):
    def test_positive_margin_exactly_means_pcc_power_beats_target_oesterle(self) -> None:
        M = Fraction(3, 2)
        eta = Fraction(1, 4)
        self.assertEqual(pcc_eta_margin_for_oesterle(M, eta), Fraction(1, 12))

    def test_near_optimal_exponent_formula(self) -> None:
        M = Fraction(3, 2)
        delta = Fraction(1, 100)
        eta = near_optimal_pcc_eta(M, delta)
        self.assertEqual(eta, Fraction(47, 150))
        exponent = almost_all_oesterle_exponent(M, delta)
        self.assertEqual(exponent, Fraction(553, 300))
        self.assertEqual(Fraction(2, 1) - eta / 2, exponent)

    def test_M_near_one_gives_small_but_positive_power_saving(self) -> None:
        M = Fraction(101, 100)
        delta = Fraction(1, 1000)
        eta = near_optimal_pcc_eta(M, delta)
        self.assertGreater(eta, 0)
        exponent = almost_all_oesterle_exponent(M, delta)
        self.assertLess(exponent, 2)

    def test_too_large_delta_rejected_for_near_optimal_parameterization(self) -> None:
        with self.assertRaises(ValueError):
            almost_all_oesterle_exponent(Fraction(3, 2), Fraction(1, 5))


if __name__ == "__main__":
    unittest.main()
