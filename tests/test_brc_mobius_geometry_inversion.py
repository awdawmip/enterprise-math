from __future__ import annotations

import unittest

from enterprise_math.brc_count_centered_carry import GammaAffine
from enterprise_math.brc_mobius_geometry_inversion import (
    mobius_inverted_geometry_ratio,
    root_centered_carry_ratio,
)


class BRCMobiusGeometryInversionTests(unittest.TestCase):
    def test_rational_scale_root_recovery(self) -> None:
        for denominator in range(1, 17):
            for numerator in range(denominator, 8 * denominator + 1):
                self.assertEqual(
                    mobius_inverted_geometry_ratio(numerator, denominator),
                    root_centered_carry_ratio(numerator, denominator),
                )

    def test_integer_scale_is_minus_gamma(self) -> None:
        for n in range(1, 129):
            self.assertEqual(mobius_inverted_geometry_ratio(n), GammaAffine(0, -1))


if __name__ == "__main__":
    unittest.main()
