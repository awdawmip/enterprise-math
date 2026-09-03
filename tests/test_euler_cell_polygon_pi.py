from __future__ import annotations

import inspect
import unittest
from decimal import Decimal, localcontext

import enterprise_math.euler_cell_polygon_pi as polygon_pi
from enterprise_math.euler_cell_polygon_pi import (
    cell_polygon_levels,
    exact_cell_polygon_certificate,
    physical_cell_area_interval,
    residual_interval_from_three,
    theoretical_width_refinement_factor,
    verify_level,
    verify_polygon_areas,
    width_refinement_factor,
)


class EulerCellPolygonPiTests(unittest.TestCase):
    def test_exact_c6_c12_certificate(self) -> None:
        certificate = exact_cell_polygon_certificate()
        self.assertTrue(certificate.valid)
        self.assertEqual(certificate.c12_lower.rational, 3)
        self.assertEqual(certificate.c12_lower.radial, 0)
        self.assertEqual(certificate.physical_c12_lower.rational, 1)
        self.assertEqual(certificate.physical_c12_lower.radial, 0)

    def test_finite_level_identities(self) -> None:
        levels = cell_polygon_levels(9, precision=120)
        for level in levels:
            self.assertTrue(verify_level(level, tolerance=Decimal("1e-90")))

    def test_nested_area_squeeze(self) -> None:
        levels = cell_polygon_levels(10, precision=120)
        for previous, following in zip(levels, levels[1:]):
            self.assertLess(previous.lower_area, following.lower_area)
            self.assertLess(following.upper_area, previous.upper_area)
            self.assertLess(following.lower_area, following.upper_area)

    def test_c12_baseline_and_physical_unit_area(self) -> None:
        level = cell_polygon_levels(1, precision=120)[1]
        with localcontext() as context:
            context.prec = 100
            self.assertLess(abs(level.lower_area - Decimal(3)), Decimal("1e-95"))
            physical_lower, physical_upper = physical_cell_area_interval(level)
            self.assertLess(abs(physical_lower - Decimal(1)), Decimal("1e-95"))
            self.assertGreater(physical_upper, Decimal(1))

    def test_polygon_shoelace_areas(self) -> None:
        levels = cell_polygon_levels(5, precision=120)
        for level in levels:
            self.assertTrue(
                verify_polygon_areas(level, tolerance=Decimal("1e-80")),
                msg=f"polygon area mismatch at level {level.level}",
            )

    def test_width_refinement_is_strictly_better_than_quarter(self) -> None:
        levels = cell_polygon_levels(10, precision=120)
        quarter = Decimal(1) / Decimal(4)
        for previous, following in zip(levels, levels[1:]):
            observed = width_refinement_factor(previous, following)
            predicted = theoretical_width_refinement_factor(following)
            self.assertLess(abs(observed - predicted), Decimal("1e-90"))
            self.assertGreater(observed, Decimal(0))
            self.assertLess(observed, quarter)

    def test_residual_intervals_from_three_are_nested(self) -> None:
        levels = cell_polygon_levels(8, precision=120)[1:]
        intervals = [residual_interval_from_three(level) for level in levels]
        for (low, high), (next_low, next_high) in zip(intervals, intervals[1:]):
            self.assertLess(low, next_low)
            self.assertLess(next_high, high)
            self.assertLess(next_low, next_high)

    def test_no_target_value_or_trigonometric_constructor(self) -> None:
        source = inspect.getsource(polygon_pi)
        forbidden = (
            "math.pi",
            "cmath.pi",
            "sin(",
            "cos(",
            "tan(",
            "atan(",
            "acos(",
            "asin(",
        )
        for token in forbidden:
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
