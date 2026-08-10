import unittest
from fractions import Fraction

from enterprise_math.abc_effective_exponent_transfer import (
    oesterle_threshold_from_effective_eta,
    ordinary_sd_implies_effective_sd,
    pasten_eta_threshold_from_oesterle,
)


class AbcEffectiveExponentTransferTests(unittest.TestCase):
    def test_effective_eta_to_oesterle_threshold(self) -> None:
        self.assertEqual(
            oesterle_threshold_from_effective_eta(Fraction(1, 3)),
            Fraction(3, 2),
        )
        self.assertEqual(
            oesterle_threshold_from_effective_eta(Fraction(3, 4)),
            Fraction(4, 1),
        )

    def test_pasten_oesterle_to_eta_threshold(self) -> None:
        self.assertEqual(
            pasten_eta_threshold_from_oesterle(Fraction(3, 2)),
            Fraction(11, 12),
        )
        self.assertEqual(
            pasten_eta_threshold_from_oesterle(Fraction(4, 3)),
            Fraction(7, 8),
        )

    def test_ordinary_small_derivative_pointwise_implies_effective(self) -> None:
        self.assertTrue(ordinary_sd_implies_effective_sd(1, 1, 5, 1, 2))
        self.assertTrue(ordinary_sd_implies_effective_sd(27, 5, 243, 1, 3))


if __name__ == "__main__":
    unittest.main()
