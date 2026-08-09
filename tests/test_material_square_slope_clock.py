import unittest

from enterprise_math.material_square_slope_clock import compile_square_slope_clock


class MaterialSquareSlopeClockTests(unittest.TestCase):
    def test_half_retention_family_compiles_to_one_load_and_two_return_ticks(self):
        report = compile_square_slope_clock(20, 2, 1)
        self.assertEqual(report.minimal_time_grid_denominator, 1)
        self.assertEqual(report.loading_tick_count, 1)
        self.assertEqual(report.returning_tick_count, 2)
        self.assertEqual(report.total_bounce_tick_count, 3)
        self.assertEqual(
            (report.material.retention_numerator, report.material.retention_denominator),
            (1, 2),
        )

    def test_three_fifths_retention_uses_minimal_common_denominator_fifteen(self):
        report = compile_square_slope_clock(12, 5, 3)
        self.assertEqual(
            (report.loading_duration.numerator, report.loading_duration.denominator),
            (2, 5),
        )
        self.assertEqual(
            (report.returning_duration.numerator, report.returning_duration.denominator),
            (2, 3),
        )
        self.assertEqual(report.minimal_time_grid_denominator, 15)
        self.assertEqual(report.loading_tick_count, 6)
        self.assertEqual(report.returning_tick_count, 10)
        self.assertEqual(report.total_bounce_tick_count, 16)

    def test_elastic_family_has_same_loading_and_return_clock(self):
        for root in range(1, 10):
            report = compile_square_slope_clock(8, root, root)
            self.assertEqual(report.loading_duration, report.returning_duration)
            self.assertEqual(report.loading_tick_count, report.returning_tick_count)
            self.assertEqual(
                (report.material.retention_numerator, report.material.retention_denominator),
                (1, 1),
            )

    def test_zero_return_work_has_no_return_clock(self):
        report = compile_square_slope_clock(8, 4, 0)
        self.assertIsNone(report.returning_duration)
        self.assertIsNone(report.returning_tick_count)
        self.assertIsNone(report.total_bounce_tick_count)
        self.assertEqual(
            (report.material.retention_numerator, report.material.retention_denominator),
            (0, 1),
        )

    def test_mass_changes_reduced_duration_and_clock_cost_exactly(self):
        unit = compile_square_slope_clock(6, 5, 3, mass_count=1)
        triple = compile_square_slope_clock(6, 5, 3, mass_count=3)
        self.assertEqual(unit.minimal_time_grid_denominator, 15)
        self.assertEqual(triple.minimal_time_grid_denominator, 5)
        self.assertEqual(
            (triple.loading_duration.numerator, triple.loading_duration.denominator),
            (6, 5),
        )
        self.assertEqual(
            (triple.returning_duration.numerator, triple.returning_duration.denominator),
            (2, 1),
        )

    def test_clock_cost_is_depth_independent(self):
        shallow = compile_square_slope_clock(2, 7, 4)
        deep = compile_square_slope_clock(50, 7, 4)
        self.assertEqual(shallow.loading_duration, deep.loading_duration)
        self.assertEqual(shallow.returning_duration, deep.returning_duration)
        self.assertEqual(
            shallow.minimal_time_grid_denominator,
            deep.minimal_time_grid_denominator,
        )
        self.assertEqual(shallow.total_bounce_tick_count, deep.total_bounce_tick_count)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            compile_square_slope_clock(0, 1, 1)
        with self.assertRaises(ValueError):
            compile_square_slope_clock(5, 2, 3)
        with self.assertRaises(ValueError):
            compile_square_slope_clock(5, 2, 1, mass_count=0)


if __name__ == "__main__":
    unittest.main()
