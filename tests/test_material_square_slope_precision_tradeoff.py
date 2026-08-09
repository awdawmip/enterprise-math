import unittest

from enterprise_math.material_square_slope_precision_tradeoff import (
    minimum_collapse_factor_for_exact_incoming_momentum,
    square_slope_precision_tradeoff,
)


class MaterialSquareSlopePrecisionTradeoffTests(unittest.TestCase):
    def test_loading_root_sets_exact_momentum_lattice_step(self):
        report = square_slope_precision_tradeoff(
            max_depth=10,
            loading_root=3,
            returning_root=2,
        )
        self.assertEqual(report.exact_incoming_momentum_step, 3)
        self.assertEqual(report.exact_outgoing_momentum_step, 2)
        self.assertEqual(report.max_exact_incoming_momentum, 30)
        self.assertEqual(report.exact_incoming_state_count, 10)
        self.assertEqual(report.momentum_span_state_count, 30)
        self.assertEqual(
            (report.exact_momentum_coverage_numerator, report.exact_momentum_coverage_denominator),
            (10, 30),
        )

    def test_exact_supported_momentum_has_depth_plus_one_spatial_requirement(self):
        for root in range(1, 9):
            for depth in range(1, 12):
                momentum = root * depth
                self.assertEqual(
                    minimum_collapse_factor_for_exact_incoming_momentum(momentum, root),
                    depth + 1,
                )
        self.assertIsNone(
            minimum_collapse_factor_for_exact_incoming_momentum(10, 3)
        )

    def test_stiffer_square_slope_reduces_depth_for_shared_supported_momentum(self):
        # p=12 lies on both b=2 and b=4 exact lattices.  The harder b=4 branch
        # turns at depth 3 instead of depth 6, so it needs a thinner spatial layer.
        self.assertEqual(
            minimum_collapse_factor_for_exact_incoming_momentum(12, 2),
            7,
        )
        self.assertEqual(
            minimum_collapse_factor_for_exact_incoming_momentum(12, 4),
            4,
        )

    def test_spatial_saving_trades_against_sparser_momentum_lattice(self):
        depth = 12
        soft = square_slope_precision_tradeoff(depth, 1, 1)
        hard = square_slope_precision_tradeoff(depth, 6, 3)
        self.assertEqual(soft.exact_incoming_state_count, hard.exact_incoming_state_count)
        self.assertEqual(soft.momentum_span_state_count, 12)
        self.assertEqual(hard.momentum_span_state_count, 72)
        self.assertGreater(
            soft.exact_momentum_coverage_numerator * hard.exact_momentum_coverage_denominator,
            hard.exact_momentum_coverage_numerator * soft.exact_momentum_coverage_denominator,
        )

    def test_time_grid_denominators_match_exact_square_slope_clock(self):
        report = square_slope_precision_tradeoff(
            max_depth=12,
            loading_root=5,
            returning_root=3,
        )
        self.assertEqual(report.loading_time_grid_denominator, 5)
        self.assertEqual(report.returning_time_grid_denominator, 3)
        self.assertEqual(report.full_bounce_time_grid_denominator, 15)
        self.assertEqual(
            (report.retention_numerator, report.retention_denominator),
            (3, 5),
        )

    def test_even_loading_root_can_have_coarser_time_denominator_under_unit_mass(self):
        odd = square_slope_precision_tradeoff(8, 5, 1)
        even = square_slope_precision_tradeoff(8, 6, 1)
        self.assertEqual(odd.loading_time_grid_denominator, 5)
        self.assertEqual(even.loading_time_grid_denominator, 3)

    def test_zero_return_root_has_no_outgoing_momentum_lattice_or_return_clock(self):
        report = square_slope_precision_tradeoff(8, 4, 0)
        self.assertIsNone(report.exact_outgoing_momentum_step)
        self.assertIsNone(report.returning_time_grid_denominator)
        self.assertEqual(report.full_bounce_time_grid_denominator, 2)
        self.assertEqual(
            (report.retention_numerator, report.retention_denominator),
            (0, 1),
        )

    def test_mass_can_change_time_denominator_without_changing_space_or_momentum_lattice(self):
        unit = square_slope_precision_tradeoff(10, 5, 3, mass_count=1)
        triple = square_slope_precision_tradeoff(10, 5, 3, mass_count=3)
        self.assertEqual(unit.exact_incoming_momentum_step, triple.exact_incoming_momentum_step)
        self.assertEqual(unit.max_supported_min_collapse_factor, triple.max_supported_min_collapse_factor)
        self.assertEqual(unit.loading_time_grid_denominator, 5)
        self.assertEqual(triple.loading_time_grid_denominator, 5)
        self.assertEqual(unit.returning_time_grid_denominator, 3)
        self.assertEqual(triple.returning_time_grid_denominator, 1)
        self.assertEqual(unit.full_bounce_time_grid_denominator, 15)
        self.assertEqual(triple.full_bounce_time_grid_denominator, 5)

    def test_invalid_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            square_slope_precision_tradeoff(0, 1, 1)
        with self.assertRaises(ValueError):
            square_slope_precision_tradeoff(5, 2, 3)
        with self.assertRaises(ValueError):
            minimum_collapse_factor_for_exact_incoming_momentum(0, 1)
        with self.assertRaises(ValueError):
            minimum_collapse_factor_for_exact_incoming_momentum(1, 0)


if __name__ == "__main__":
    unittest.main()
