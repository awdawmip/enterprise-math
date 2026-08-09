import unittest

from enterprise_math.material_square_slope_family import (
    square_slope_depth_report,
    square_slope_material_family,
)


class MaterialSquareSlopeFamilyTests(unittest.TestCase):
    def test_elastic_hooke_family_has_square_work_and_exact_integer_momentum(self):
        family = square_slope_material_family(20, 1, 1)
        for depth in range(0, 21):
            report = square_slope_depth_report(family, depth)
            self.assertEqual(report.loading_work_numerator2, depth * depth)
            self.assertEqual(report.returning_work_numerator2, depth * depth)
            self.assertEqual(report.dissipated_work_numerator2, 0)
            self.assertEqual(report.incoming_whole_momentum, depth)
            self.assertEqual(report.outgoing_whole_momentum, depth)
            self.assertTrue(report.exact_work_energy_turn)
            self.assertTrue(report.exact_rational_momentum_closure)

    def test_rational_retention_is_derived_from_square_branch_slopes(self):
        family = square_slope_material_family(12, 5, 3)
        self.assertEqual((family.retention_numerator, family.retention_denominator), (3, 5))
        for depth in range(1, 13):
            report = square_slope_depth_report(family, depth)
            self.assertEqual(report.incoming_whole_momentum, 5 * depth)
            self.assertEqual(report.outgoing_whole_momentum, 3 * depth)
            self.assertEqual(report.loading_work_numerator2, 25 * depth * depth)
            self.assertEqual(report.returning_work_numerator2, 9 * depth * depth)
            self.assertEqual(report.dissipated_work_numerator2, 16 * depth * depth)

    def test_zero_return_root_is_no_return_work_family(self):
        family = square_slope_material_family(8, 4, 0)
        self.assertEqual((family.retention_numerator, family.retention_denominator), (0, 1))
        for depth in range(0, 9):
            report = square_slope_depth_report(family, depth)
            self.assertEqual(report.outgoing_whole_momentum, 0)
            self.assertEqual(report.returning_work_numerator2, 0)
            self.assertEqual(report.dissipated_work_numerator2, report.loading_work_numerator2)

    def test_any_reduced_rational_retention_can_be_realized_exactly(self):
        for denominator in range(1, 9):
            for numerator in range(0, denominator + 1):
                family = square_slope_material_family(5, denominator, numerator)
                from math import gcd
                common = gcd(numerator, denominator)
                expected = (numerator // common, denominator // common)
                self.assertEqual(
                    (family.retention_numerator, family.retention_denominator),
                    expected,
                )
                report = square_slope_depth_report(family, 5)
                self.assertEqual(
                    report.outgoing_whole_momentum * denominator,
                    report.incoming_whole_momentum * numerator,
                )

    def test_force_samples_are_monotone_and_returning_never_exceeds_loading(self):
        family = square_slope_material_family(10, 7, 4)
        loading = family.law.profile.loading
        returning = family.law.profile.returning
        self.assertEqual(loading, tuple(49 * k for k in range(11)))
        self.assertEqual(returning, tuple(16 * k for k in range(11)))
        self.assertTrue(all(a <= b for a, b in zip(loading, loading[1:])))
        self.assertTrue(all(a <= b for a, b in zip(returning, returning[1:])))
        self.assertTrue(all(r <= l for l, r in zip(loading, returning)))

    def test_invalid_roots_are_rejected(self):
        with self.assertRaises(ValueError):
            square_slope_material_family(5, 0, 0)
        with self.assertRaises(ValueError):
            square_slope_material_family(5, 2, 3)
        with self.assertRaises(ValueError):
            square_slope_material_family(0, 1, 1)


if __name__ == "__main__":
    unittest.main()
