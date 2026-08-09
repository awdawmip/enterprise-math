import itertools
import unittest

from enterprise_math.material_measurement_area_refinement import (
    trace_measurement_refinement,
    trapezoid_refinement_shell,
)
from enterprise_math.material_measurement_refinement_variation import (
    SHELL_NEGATIVE,
    SHELL_POSITIVE,
    SHELL_ZERO,
    compare_refinement_order_variation,
    refinement_shell_range_bound,
    refinement_shell_sign,
    refinement_witness_variation,
    refinement_witness_variation_from_shells,
    secant_slope_change_numerator,
)


class MaterialMeasurementRefinementVariationTests(unittest.TestCase):
    def test_shell_is_exact_secant_slope_change_numerator(self):
        for e0 in range(-2, 3):
            for e2 in range(e0 + 2, e0 + 7):
                for e1 in range(e0 + 1, e2):
                    for s0 in range(-3, 4):
                        for s1 in range(-3, 4):
                            for s2 in range(-3, 4):
                                points = ((e0, s0), (e1, s1), (e2, s2))
                                self.assertEqual(
                                    secant_slope_change_numerator(*points),
                                    trapezoid_refinement_shell(*points),
                                )

    def test_shell_sign_reports_only_oriented_integer_change(self):
        self.assertEqual(refinement_shell_sign((0, 0), (1, 0), (2, 2)), SHELL_NEGATIVE)
        self.assertEqual(refinement_shell_sign((0, 0), (1, 1), (2, 2)), SHELL_ZERO)
        self.assertEqual(refinement_shell_sign((0, 0), (1, 2), (2, 2)), SHELL_POSITIVE)

    def test_response_range_bound_is_sharp_and_matches_exhaustive_small_domain(self):
        lower = -2
        upper = 3
        width = upper - lower
        for e0 in range(-1, 2):
            for e2 in range(e0 + 2, e0 + 6):
                span = e2 - e0
                for e1 in range(e0 + 1, e2):
                    maximum = 0
                    for s0, s1, s2 in itertools.product(range(lower, upper + 1), repeat=3):
                        report = refinement_shell_range_bound(
                            (e0, s0),
                            (e1, s1),
                            (e2, s2),
                            lower,
                            upper,
                        )
                        maximum = max(maximum, report.absolute_shell)
                        self.assertLessEqual(report.absolute_shell, span * width)
                    self.assertEqual(maximum, span * width)

        positive_extremum = refinement_shell_range_bound(
            (0, lower), (2, upper), (5, lower), lower, upper
        )
        negative_extremum = refinement_shell_range_bound(
            (0, upper), (2, lower), (5, upper), lower, upper
        )
        self.assertTrue(positive_extremum.attains_bound)
        self.assertTrue(negative_extremum.attains_bound)
        self.assertEqual(positive_extremum.shell, 25)
        self.assertEqual(negative_extremum.shell, -25)

    def test_variation_exactly_separates_positive_negative_and_cancelled_shell_mass(self):
        report = refinement_witness_variation_from_shells((-15, -3, 3))
        self.assertEqual(report.total_shell, -15)
        self.assertEqual(report.positive_shell_mass, 3)
        self.assertEqual(report.negative_shell_mass, 18)
        self.assertEqual(report.witness_activity, 21)
        self.assertEqual(report.cancelled_shell_mass, 3)
        self.assertEqual(
            report.witness_activity - abs(report.total_shell),
            2 * report.cancelled_shell_mass,
        )

    def test_same_final_measurements_can_have_same_total_but_different_witness_activity(self):
        initial = ((0, 0), (5, 0))
        inserted = ((1, -3), (2, -3), (3, -1))
        comparison = compare_refinement_order_variation(
            initial,
            inserted,
            ((3, -1), (1, -3), (2, -3)),
        )
        self.assertTrue(comparison.same_final_polyline)
        self.assertTrue(comparison.same_total_shell)
        self.assertFalse(comparison.same_witness_activity)
        self.assertFalse(comparison.same_cancelled_shell_mass)
        self.assertEqual(comparison.first_variation.total_shell, -15)
        self.assertEqual(comparison.second_variation.total_shell, -15)
        self.assertEqual(comparison.first_variation.witness_activity, 21)
        self.assertEqual(comparison.second_variation.witness_activity, 15)
        self.assertEqual(comparison.first_variation.cancelled_shell_mass, 3)
        self.assertEqual(comparison.second_variation.cancelled_shell_mass, 0)

    def test_all_orders_preserve_endpoint_total_but_can_realize_multiple_variations(self):
        initial = ((0, 0), (5, 0))
        inserted = ((1, -3), (2, -3), (3, -1))
        totals = set()
        activities = set()
        cancellations = set()
        for order in itertools.permutations(inserted):
            trace = trace_measurement_refinement(initial, order)
            variation = refinement_witness_variation(trace)
            totals.add(variation.total_shell)
            activities.add(variation.witness_activity)
            cancellations.add(variation.cancelled_shell_mass)
        self.assertEqual(totals, {-15})
        self.assertEqual(activities, {15, 19, 21})
        self.assertEqual(cancellations, {0, 2, 3})

    def test_zero_total_can_hide_nonzero_witness_activity(self):
        trace = trace_measurement_refinement(
            ((0, 0), (3, 0)),
            ((1, 1), (2, -1)),
        )
        variation = refinement_witness_variation(trace)
        self.assertEqual(variation.local_shells, (3, -3))
        self.assertEqual(variation.total_shell, 0)
        self.assertEqual(variation.witness_activity, 6)
        self.assertEqual(variation.cancelled_shell_mass, 3)

    def test_invalid_response_range_and_shell_types_are_rejected(self):
        with self.assertRaises(ValueError):
            refinement_shell_range_bound((0, 0), (1, 1), (2, 0), 2, 1)
        with self.assertRaises(ValueError):
            refinement_shell_range_bound((0, 0), (1, 5), (2, 0), 0, 4)
        with self.assertRaises(ValueError):
            refinement_witness_variation_from_shells((1, True))


if __name__ == "__main__":
    unittest.main()
