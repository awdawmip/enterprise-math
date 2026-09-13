from __future__ import annotations

import unittest
from fractions import Fraction

from enterprise_math.brc_count_centered_carry import (
    GammaAffine,
    direct_gamma_centered_prime_error_form,
    mobius_divisor_deconvolution_form,
    valuation_product,
)
from enterprise_math.brc_mobius_log_gauge import (
    mobius_log_gauge_transfer,
    rational_log_valuations,
)


class BRCMobiusLogGaugeTests(unittest.TestCase):
    def test_rational_log_valuation_roundtrip(self) -> None:
        for numerator in range(1, 65):
            for denominator in range(1, 65):
                self.assertEqual(
                    valuation_product(rational_log_valuations(numerator, denominator)),
                    Fraction(numerator, denominator),
                )

    def test_integer_endpoint_gauge_transfer(self) -> None:
        for n in range(1, 81):
            state = mobius_log_gauge_transfer(n)
            self.assertEqual(state.inversion_sum, GammaAffine(0, -1))
            self.assertTrue(state.verify())
            self.assertTrue(
                state.as_form().equivalent(mobius_divisor_deconvolution_form(n))
            )
            self.assertTrue(
                state.as_form().equivalent(direct_gamma_centered_prime_error_form(n))
            )


if __name__ == "__main__":
    unittest.main()
