import unittest

from enterprise_math.material_contact_capacity_physical import (
    exact_material_impulse_capacity,
)
from enterprise_math.material_contact_safe_precision import (
    safe_single_contact_precision_report,
)
from enterprise_math.material_physical_projection import ForceImpulseCountScale


def unit_scale():
    return ForceImpulseCountScale(
        force_scale_factor=1,
        time_scale_factor=1,
        momentum_scale_factor=1,
        tick_duration_count=1,
        force_unit="F",
        time_unit="T",
        momentum_unit="P",
    )


def exact_fraction(numerator: int, denominator: int):
    return exact_material_impulse_capacity(
        numerator,
        denominator,
        1,
        unit_scale(),
    )


class MaterialContactSafePrecisionTests(unittest.TestCase):
    def test_underpowered_material_has_no_safe_precision(self):
        report = safe_single_contact_precision_report(
            exact_fraction(1, 4),
            closing_score=1,
            self_coupling=3,
        )
        self.assertFalse(report.physically_strong_enough)
        self.assertLess(report.strength_cross_difference, 0)
        self.assertIsNone(report.safe_plastic_denominator)
        self.assertIsNone(report.safe_impulse_numerator)
        self.assertFalse(report.passive)

    def test_exactly_balanced_material_is_safe_at_plastic_base_denominator(self):
        report = safe_single_contact_precision_report(
            exact_fraction(1, 3),
            closing_score=1,
            self_coupling=3,
        )
        self.assertTrue(report.physically_strong_enough)
        self.assertEqual(report.strength_cross_difference, 0)
        self.assertEqual(report.safe_plastic_denominator, 3)
        self.assertEqual(report.safe_impulse_numerator, 1)
        self.assertEqual(report.represented_material_capacity_numerator, 1)
        self.assertEqual(report.capacity_margin_numerator, 0)
        self.assertTrue(report.exact_zero_score)
        self.assertTrue(report.passive)

    def test_stronger_material_may_be_passive_cheaper_but_plastic_base_is_canonical_safe_choice(self):
        # C=1/2 > R=1/3.  Denominator 2 is already passive/capacity-feasible,
        # but denominator 3 is the first exact zero-score plastic sublattice point.
        report = safe_single_contact_precision_report(
            exact_fraction(1, 2),
            1,
            3,
        )
        self.assertEqual(report.safe_plastic_denominator, 3)
        self.assertEqual(report.safe_impulse_numerator, 1)
        self.assertEqual(report.represented_material_capacity_numerator, 1)
        self.assertTrue(report.passive)
        self.assertTrue(report.exact_zero_score)

    def test_gcd_reduction_sets_exact_plastic_base(self):
        # Demand q/K = 2/6 = 1/3, so denominator 3 rather than 6 is sufficient.
        report = safe_single_contact_precision_report(
            exact_fraction(3, 4),
            2,
            6,
        )
        self.assertEqual(report.safe_plastic_denominator, 3)
        self.assertEqual(report.safe_impulse_numerator, 1)
        self.assertGreaterEqual(report.represented_material_capacity_numerator, 1)

    def test_bounded_strength_comparison_always_succeeds_at_exact_plastic_base_when_not_underpowered(self):
        for capacity_num in range(0, 7):
            for capacity_den in range(1, 8):
                exact = exact_fraction(capacity_num, capacity_den)
                for q in range(1, 8):
                    for coupling in range(1, 9):
                        report = safe_single_contact_precision_report(
                            exact, q, coupling
                        )
                        physically_sufficient = (
                            exact.raw_numerator * coupling
                            >= q * exact.raw_denominator
                        )
                        self.assertEqual(
                            report.physically_strong_enough,
                            physically_sufficient,
                        )
                        if physically_sufficient:
                            self.assertTrue(report.passive)
                            self.assertTrue(report.exact_zero_score)
                            self.assertIsNotNone(report.safe_plastic_denominator)
                            self.assertGreaterEqual(
                                report.represented_material_capacity_numerator,
                                report.safe_impulse_numerator,
                            )
                        else:
                            self.assertIsNone(report.safe_plastic_denominator)

    def test_invalid_contact_parameters_are_rejected(self):
        exact = exact_fraction(1, 2)
        with self.assertRaises(ValueError):
            safe_single_contact_precision_report(exact, 0, 2)
        with self.assertRaises(ValueError):
            safe_single_contact_precision_report(exact, 1, 0)


if __name__ == "__main__":
    unittest.main()
