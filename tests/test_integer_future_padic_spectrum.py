import unittest

from enterprise_math.integer_future_padic_spectrum import (
    complete_padic_smith_spectrum,
    free_vs_deep_torsion_indistinguishable_through,
    padic_kernel_spectrum_from_matrix,
    padic_spectrum_from_kernel_exponents,
)


class IntegerFuturePadicSpectrumTests(unittest.TestCase):
    def test_complete_kernel_curve_recovers_free_rank_and_positive_valuation_multiplicities(self):
        # Smith factors are 1,2,4,8 with one additional free hidden coordinate.
        matrix = (
            (1, 0, 0, 0, 0),
            (0, 2, 0, 0, 0),
            (0, 0, 4, 0, 0),
            (0, 0, 0, 8, 0),
        )
        report = complete_padic_smith_spectrum(matrix, 2)
        self.assertEqual(report.hidden_free_rank, 1)
        self.assertEqual(
            report.positive_valuation_multiplicities,
            ((1, 1), (2, 1), (3, 1)),
        )
        self.assertEqual(report.sufficient_precision_exponent, 4)
        self.assertEqual(
            report.finite_reconstruction.kernel_exponents,
            (4, 7, 9, 10),
        )
        self.assertEqual(
            report.finite_reconstruction.slopes,
            (4, 3, 2, 1),
        )
        self.assertEqual(report.finite_reconstruction.unresolved_tail_slope, 1)

    def test_discrete_slope_drops_recover_exact_valuation_counts_below_observed_tail(self):
        # kappa slopes 5,4,4,2 imply one valuation at depth1 and two at depth3;
        # the final slope 2 remains an unresolved mixture of free rank and any
        # torsion deeper than the observed exponent.
        spectrum = padic_spectrum_from_kernel_exponents(
            2,
            (5, 9, 13, 15),
        )
        self.assertEqual(spectrum.slopes, (5, 4, 4, 2))
        self.assertEqual(
            spectrum.recovered_exact_valuation_multiplicities,
            ((1, 1), (3, 2)),
        )
        self.assertEqual(spectrum.unresolved_tail_slope, 2)
        self.assertTrue(spectrum.slopes_nonincreasing)

    def test_free_direction_and_deep_finite_torsion_are_identical_until_precision_crosses_depth(self):
        for prime in (2, 3, 5):
            for depth in range(1, 6):
                for observed in range(1, depth + 1):
                    self.assertTrue(
                        free_vs_deep_torsion_indistinguishable_through(
                            prime,
                            depth,
                            observed,
                        )
                    )
                self.assertFalse(
                    free_vs_deep_torsion_indistinguishable_through(
                        prime,
                        depth,
                        depth + 1,
                    )
                )

    def test_sharp_free_vs_torsion_curves_split_exactly_one_level_after_depth(self):
        prime = 2
        depth = 4
        free = padic_kernel_spectrum_from_matrix(
            ((1, 0),),
            prime,
            depth + 2,
        )
        torsion = padic_kernel_spectrum_from_matrix(
            ((1, 0), (0, prime ** depth)),
            prime,
            depth + 2,
        )
        self.assertEqual(
            free.kernel_exponents[:depth],
            torsion.kernel_exponents[:depth],
        )
        self.assertEqual(free.kernel_exponents[depth], depth + 1)
        self.assertEqual(torsion.kernel_exponents[depth], depth)

    def test_no_torsion_case_needs_only_first_prime_power_level_to_recover_free_rank(self):
        report = complete_padic_smith_spectrum(
            ((1, 0, 0),),
            3,
        )
        self.assertEqual(report.hidden_free_rank, 2)
        self.assertEqual(report.positive_valuation_multiplicities, ())
        self.assertEqual(report.sufficient_precision_exponent, 1)
        self.assertEqual(report.finite_reconstruction.slopes, (2,))

    def test_other_prime_ignores_unrelated_torsion(self):
        matrix = (
            (2, 0),
            (0, 8),
        )
        report = complete_padic_smith_spectrum(matrix, 3)
        self.assertEqual(report.hidden_free_rank, 0)
        self.assertEqual(report.positive_valuation_multiplicities, ())
        self.assertEqual(report.sufficient_precision_exponent, 1)
        self.assertEqual(report.finite_reconstruction.kernel_exponents, (0,))

    def test_validation(self):
        with self.assertRaises(ValueError):
            padic_spectrum_from_kernel_exponents(2, ())
        with self.assertRaises(ValueError):
            padic_spectrum_from_kernel_exponents(2, (1, 3))
        with self.assertRaises(ValueError):
            padic_spectrum_from_kernel_exponents(4, (1,))
        with self.assertRaises(ValueError):
            free_vs_deep_torsion_indistinguishable_through(2, 0, 1)
        with self.assertRaises(TypeError):
            free_vs_deep_torsion_indistinguishable_through(2, 1, False)


if __name__ == "__main__":
    unittest.main()
