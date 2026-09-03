from __future__ import annotations

import unittest
from decimal import Decimal, localcontext
from fractions import Fraction

from enterprise_math.spectral_precision import (
    dyadic_completion_certificate,
    dyadic_smallest_eigenvalue,
    integer_mode_parity_curvature,
    self_check,
    spectral_decimation,
    tau_lt_four_sign_certificate,
    verify_dirichlet_coefficient_identity,
    wallis_partial,
    wallis_upper_step_ratio,
)


class SpectralPrecisionTests(unittest.TestCase):
    def test_small_wallis_values(self) -> None:
        self.assertEqual(wallis_partial(1), Fraction(4, 3))
        self.assertEqual(wallis_partial(2), Fraction(64, 45))

    def test_target_free_wallis_upper_ratio(self) -> None:
        for n in range(1, 21):
            self.assertEqual(
                wallis_upper_step_ratio(n),
                1 - Fraction(1, (2 * n + 1) ** 2 * (4 * n + 5)),
            )

    def test_dirichlet_coefficient_formula(self) -> None:
        for M in range(2, 17):
            self.assertTrue(verify_dirichlet_coefficient_identity(M), M)

    def test_tau_lt_four_rational_sign(self) -> None:
        self.assertEqual(tau_lt_four_sign_certificate(), Fraction(-268, 405))

    def test_integer_mode_curvature_is_wallis(self) -> None:
        for q in range(2, 11):
            self.assertEqual(integer_mode_parity_curvature(q), wallis_partial(q - 1))

    def test_dyadic_inverse_decimation(self) -> None:
        with localcontext() as ctx:
            ctx.prec = 70
            for q in (2, 4, 8, 16, 32, 64):
                a_q = dyadic_smallest_eigenvalue(q, precision=70)
                a_2q = dyadic_smallest_eigenvalue(2 * q, precision=70)
                self.assertLess(abs(spectral_decimation(a_2q) - a_q), Decimal("1e-60"))

    def test_completion_width_is_exact(self) -> None:
        for q in (2, 4, 8, 16, 32, 64):
            cert = dyadic_completion_certificate(q, precision=80)
            self.assertEqual(cert.width_exact, Fraction(2, 15 * q**4))
            self.assertLess(cert.lower, cert.upper)

    def test_corrected_q64_diagnostic_prefix(self) -> None:
        cert = dyadic_completion_certificate(64, precision=90)
        self.assertTrue(str(cert.lower).startswith("3.141592651214810479084013489"))

    def test_self_check(self) -> None:
        self.assertTrue(all(self_check(max_M=20, max_wallis_n=20).values()))

    def test_domain_guards(self) -> None:
        with self.assertRaises(ValueError):
            dyadic_smallest_eigenvalue(1)
        with self.assertRaises(ValueError):
            dyadic_smallest_eigenvalue(6)


if __name__ == "__main__":
    unittest.main()
