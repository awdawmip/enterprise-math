import ast
import inspect
import itertools
import unittest

import enterprise_math.black_hole as black_hole
from enterprise_math.black_hole import (
    clock_shell_interval,
    clock_state,
    horizon_boundary_state_count,
    horizon_is_singleton,
    horizon_observation,
    horizon_zero_collision_count,
    horizon_zero_interval,
    horizon_zero_width,
    l1_ball_count,
    l1_shell_count,
    outgoing_primitive_step,
    outgoing_shell_expansion,
    project_horizon_observation,
)
from enterprise_math.precision_system import refinement_projection


class DiscreteBlackHoleTests(unittest.TestCase):
    def test_divisible_precision_projection(self):
        for horizon in range(1, 40):
            for coarse in range(1, 15):
                for ratio in range(1, 8):
                    fine = coarse * ratio
                    for radius in range(1, 120):
                        fine_value = horizon_observation(fine, radius, horizon)
                        self.assertEqual(
                            project_horizon_observation(fine_value, coarse, fine),
                            horizon_observation(coarse, radius, horizon),
                        )

    def test_nondivisible_numeric_increase_need_not_refine(self):
        horizon = 1
        states = [3, 4]
        coarse = lambda radius: horizon_observation(4, radius, horizon)
        fine = lambda radius: horizon_observation(9, radius, horizon)
        self.assertEqual([coarse(radius) for radius in states], [2, 3])
        self.assertEqual([fine(radius) for radius in states], [6, 6])
        with self.assertRaises(ValueError):
            refinement_projection(states, coarse, fine)

    def test_zero_interval_and_width_are_exact(self):
        for precision in range(2, 30):
            for horizon in range(1, 100):
                lower, upper = horizon_zero_interval(precision, horizon)
                expected = list(range(lower, upper + 1))
                observed = [
                    radius
                    for radius in range(1, upper + 10)
                    if horizon_observation(precision, radius, horizon) == 0
                ]
                self.assertEqual(observed, expected)
                self.assertEqual(horizon_zero_width(precision, horizon), len(expected))

    def test_zero_basin_is_nested_under_larger_precision(self):
        for horizon in range(1, 60):
            for coarse in range(2, 12):
                coarse_lower, coarse_upper = horizon_zero_interval(coarse, horizon)
                coarse_zero = set(range(coarse_lower, coarse_upper + 1))
                for fine in range(coarse, 18):
                    fine_lower, fine_upper = horizon_zero_interval(fine, horizon)
                    fine_zero = set(range(fine_lower, fine_upper + 1))
                    self.assertTrue(fine_zero.issubset(coarse_zero))

    def test_singleton_resolution_threshold_is_exact(self):
        for precision in range(2, 40):
            for horizon in range(1, 100):
                lower, upper = horizon_zero_interval(precision, horizon)
                singleton = (lower, upper) == (horizon, horizon)
                self.assertEqual(singleton, precision >= horizon + 1)
                self.assertEqual(horizon_is_singleton(precision, horizon), singleton)

    def test_clock_shell_characterization_including_skipped_levels(self):
        for sigma in range(2, 9):
            for horizon in range(1, 25):
                for clock in range(sigma):
                    interval = clock_shell_interval(sigma, horizon, clock)
                    observed = [
                        radius
                        for radius in range(horizon, 3000)
                        if clock_state(sigma, radius, horizon) == clock
                    ]
                    if interval is None:
                        self.assertEqual(observed, [])
                        continue
                    lower, upper = interval
                    if upper is None:
                        self.assertEqual(observed, list(range(lower, 3000)))
                    else:
                        self.assertEqual(observed, list(range(lower, upper + 1)))

        self.assertIsNone(clock_shell_interval(3, 1, 1))
        self.assertEqual(clock_state(3, 1, 1), 0)
        self.assertEqual(clock_state(3, 2, 1), 2)

    def test_external_finite_radius_clock_never_reaches_sigma(self):
        for sigma in range(2, 12):
            for horizon in range(1, 20):
                for radius in range(horizon, 1000):
                    self.assertLess(clock_state(sigma, radius, horizon), sigma)

    def test_resolved_horizon_has_outside_fixed_inside_causal_phases(self):
        for horizon in range(1, 50):
            precision = horizon + 1
            self.assertEqual(outgoing_primitive_step(precision, horizon, horizon), 0)
            for radius in range(1, horizon):
                self.assertEqual(outgoing_primitive_step(precision, radius, horizon), -1)
            for radius in range(horizon + 1, horizon + 40):
                self.assertEqual(outgoing_primitive_step(precision, radius, horizon), 1)
            self.assertEqual(outgoing_primitive_step(precision, 0, horizon), 0)

    def test_general_l1_shell_formula_matches_bruteforce(self):
        for dimension in range(1, 5):
            for radius in range(0, 6):
                brute_force = sum(
                    1
                    for point in itertools.product(
                        range(-radius, radius + 1), repeat=dimension
                    )
                    if sum(abs(coordinate) for coordinate in point) == radius
                )
                self.assertEqual(l1_shell_count(dimension, radius), brute_force)

    def test_three_dimensional_shell_and_ball_closed_forms(self):
        for radius in range(1, 100):
            self.assertEqual(l1_shell_count(3, radius), 4 * radius * radius + 2)
            self.assertEqual(
                l1_ball_count(3, radius),
                (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3,
            )

    def test_resolved_three_dimensional_shell_expansion_sign(self):
        for horizon in range(2, 50):
            precision = horizon + 1
            self.assertEqual(outgoing_shell_expansion(precision, horizon, horizon, 3), 0)
            for radius in range(1, horizon):
                self.assertLess(outgoing_shell_expansion(precision, radius, horizon, 3), 0)
            for radius in range(horizon + 1, horizon + 30):
                self.assertGreater(outgoing_shell_expansion(precision, radius, horizon, 3), 0)

    def test_boundary_count_collapses_to_one_shell_at_terminal_resolution(self):
        for horizon in range(1, 60):
            precision = horizon + 1
            self.assertEqual(
                horizon_boundary_state_count(precision, horizon, 3),
                l1_shell_count(3, horizon),
            )

    def test_zero_fiber_collision_contribution(self):
        for precision in range(2, 20):
            for horizon in range(1, 50):
                width = horizon_zero_width(precision, horizon)
                self.assertEqual(horizon_zero_collision_count(precision, horizon, 0), 1)
                self.assertEqual(horizon_zero_collision_count(precision, horizon, 1), width)
                if width >= 2:
                    self.assertEqual(
                        horizon_zero_collision_count(precision, horizon, 2),
                        width * (width - 1) // 2,
                    )

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(black_hole))
        float_constants = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        true_divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(float_constants, [])
        self.assertEqual(true_divisions, [])


if __name__ == "__main__":
    unittest.main()
