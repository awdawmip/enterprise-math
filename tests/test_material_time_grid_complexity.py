import unittest
from math import gcd

from enterprise_math.material_time_grid_complexity import (
    material_time_grid_complexity,
    square_slope_time_grid_denominator,
)


class MaterialTimeGridComplexityTests(unittest.TestCase):
    def test_hooke_targets_have_one_depth_independent_duration(self):
        targets = tuple(range(0, 11))
        report = material_time_grid_complexity(targets)
        self.assertEqual(report.minimal_time_grid_denominator, 1)
        self.assertEqual(
            {(d.numerator, d.denominator) for d in report.distinct_exact_durations},
            {(2, 1)},
        )
        self.assertEqual(report.no_finite_duration_depths, ())

    def test_square_slope_branch_has_one_constant_rational_duration(self):
        for root in range(1, 12):
            targets = tuple(root * k for k in range(0, 9))
            report = material_time_grid_complexity(targets)
            expected_den = root // gcd(2, root)
            self.assertEqual(report.minimal_time_grid_denominator, expected_den)
            self.assertEqual(square_slope_time_grid_denominator(root), expected_den)
            self.assertEqual(len(report.distinct_exact_durations), 1)
            duration = report.distinct_exact_durations[0]
            common = gcd(2, root)
            self.assertEqual(
                (duration.numerator, duration.denominator),
                (2 // common, root // common),
            )

    def test_nonlinear_targets_can_require_multiple_time_denominators_and_lcm_budget(self):
        targets = (0, 2, 3, 7, 8)
        report = material_time_grid_complexity(targets)
        durations = {
            (item.depth, item.exact_duration.numerator, item.exact_duration.denominator)
            for item in report.requirements
            if item.exact_duration is not None
        }
        self.assertEqual(
            durations,
            {
                (1, 1, 1),
                (2, 4, 3),
                (3, 6, 7),
                (4, 1, 1),
            },
        )
        self.assertEqual(report.minimal_time_grid_denominator, 21)

    def test_irregular_deformation_grid_changes_time_complexity(self):
        targets = (0, 2, 4, 6)
        unit = material_time_grid_complexity(targets)
        irregular = material_time_grid_complexity(
            targets,
            deformation_counts=(0, 1, 3, 8),
        )
        self.assertEqual(unit.minimal_time_grid_denominator, 1)
        self.assertEqual(irregular.minimal_time_grid_denominator, 6)
        self.assertEqual(
            {(d.numerator, d.denominator) for d in irregular.distinct_exact_durations},
            {(1, 1), (3, 2), (8, 3)},
        )
        self.assertNotEqual(unit.distinct_exact_durations, irregular.distinct_exact_durations)

    def test_positive_depth_with_zero_momentum_target_is_explicitly_not_a_finite_rest_endpoint(self):
        report = material_time_grid_complexity((0, 0, 2, 3))
        self.assertEqual(report.no_finite_duration_depths, (1,))
        self.assertFalse(report.requirements[0].finite_dynamic_endpoint)
        self.assertIsNone(report.requirements[0].exact_duration)

    def test_mass_rescales_denominators_by_exact_reduction(self):
        targets = tuple(5 * k for k in range(0, 5))
        unit = material_time_grid_complexity(targets, mass_count=1)
        double = material_time_grid_complexity(targets, mass_count=2)
        self.assertEqual(unit.minimal_time_grid_denominator, 5)
        self.assertEqual(double.minimal_time_grid_denominator, 5)
        # tau changes 2/5 -> 4/5, but denominator resource is unchanged.
        self.assertEqual(
            {(d.numerator, d.denominator) for d in unit.distinct_exact_durations},
            {(2, 5)},
        )
        self.assertEqual(
            {(d.numerator, d.denominator) for d in double.distinct_exact_durations},
            {(4, 5)},
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            material_time_grid_complexity((1, 2, 3))
        with self.assertRaises(ValueError):
            material_time_grid_complexity((0, 1, 2), deformation_counts=(0, 2, 1))
        with self.assertRaises(ValueError):
            square_slope_time_grid_denominator(0)


if __name__ == "__main__":
    unittest.main()
