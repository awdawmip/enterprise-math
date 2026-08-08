import ast
import inspect
import unittest

import enterprise_math.charged_black_hole as charged
from enterprise_math.black_hole import horizon_observation
from enterprise_math.charged_black_hole import (
    charged_discriminant,
    charged_horizon_observation,
    charged_phase,
    charged_residual,
    discriminant_horizon_cell,
    discriminant_is_square_fixed_point,
    integer_horizon_states,
    positive_horizon_states,
    project_charged_observation,
    rescale_coefficients,
    terminal_zero_precision,
    trapped_interval,
    zero_persistence_limit,
)


class ChargedBlackHoleTests(unittest.TestCase):
    def test_completed_square_identity(self):
        for a in range(0, 30):
            for b in range(0, 100):
                delta = charged_discriminant(a, b)
                for n in range(0, 50):
                    self.assertEqual(
                        4 * charged_residual(n, a, b),
                        (2 * n - a) ** 2 - delta,
                    )

    def test_integer_horizons_iff_discriminant_is_square(self):
        for a in range(0, 50):
            for b in range(0, 300):
                roots = integer_horizon_states(a, b)
                expected = discriminant_is_square_fixed_point(a, b)
                self.assertEqual(bool(roots), expected)
                for root in roots:
                    self.assertEqual(charged_residual(root, a, b), 0)
                self.assertEqual(
                    positive_horizon_states(a, b),
                    tuple(root for root in roots if root > 0),
                )

    def test_discriminant_sign_phase(self):
        for a in range(0, 30):
            for b in range(0, 100):
                delta = charged_discriminant(a, b)
                for n in range(0, 50):
                    difference = (2 * n - a) ** 2 - delta
                    expected = (difference > 0) - (difference < 0)
                    self.assertEqual(charged_phase(n, a, b), expected)

    def test_trapped_interval_is_exact(self):
        for a in range(1, 40):
            for b in range(0, 200):
                interval = trapped_interval(a, b)
                observed = [n for n in range(1, 2 * a + 5) if charged_phase(n, a, b) < 0]
                if interval is None:
                    self.assertEqual(observed, [])
                else:
                    lower, upper = interval
                    self.assertEqual(observed, list(range(lower, upper + 1)))

    def test_nonsquare_discriminant_can_have_trapped_band_without_zero(self):
        a, b = 5, 5
        self.assertEqual(charged_discriminant(a, b), 5)
        self.assertFalse(discriminant_is_square_fixed_point(a, b))
        self.assertEqual(integer_horizon_states(a, b), ())
        self.assertEqual(trapped_interval(a, b), (2, 3))
        self.assertEqual([charged_phase(n, a, b) for n in range(1, 5)], [1, -1, -1, 1])

    def test_parity_constrained_horizon_cell(self):
        for a in range(0, 40):
            for b in range(0, 200):
                delta = charged_discriminant(a, b)
                if delta < 0:
                    continue
                cell = discriminant_horizon_cell(a, b)
                u = cell["u"]
                self.assertEqual(u % 2, a % 2)
                self.assertLessEqual(u * u, delta)
                self.assertGreater((u + 2) * (u + 2), delta)
                self.assertEqual(
                    4 * charged_residual(cell["inner_lower"], a, b),
                    u * u - delta,
                )
                self.assertEqual(
                    4 * charged_residual(cell["inner_upper"], a, b),
                    u * u - delta,
                )
                self.assertEqual(cell["inner_defect"] * 4, delta - u * u)
                self.assertEqual(cell["outer_defect"] * 4, (u + 2) ** 2 - delta)
                self.assertEqual(cell["exact"], u * u == delta)

    def test_divisible_precision_projection(self):
        for a in range(0, 20):
            for b in range(0, 60):
                for n in range(1, 40):
                    for coarse in range(1, 10):
                        for ratio in range(1, 6):
                            fine = coarse * ratio
                            fine_value = charged_horizon_observation(fine, n, a, b)
                            self.assertEqual(
                                project_charged_observation(fine_value, coarse, fine),
                                charged_horizon_observation(coarse, n, a, b),
                            )

    def test_zero_persistence_is_exact(self):
        for a in range(0, 20):
            for b in range(0, 60):
                for n in range(1, 50):
                    limit = zero_persistence_limit(n, a, b)
                    if charged_residual(n, a, b) == 0:
                        self.assertIsNone(limit)
                        for precision in range(1, 50):
                            self.assertEqual(charged_horizon_observation(precision, n, a, b), 0)
                    else:
                        self.assertIsNotNone(limit)
                        for precision in range(1, 50):
                            self.assertEqual(
                                charged_horizon_observation(precision, n, a, b) == 0,
                                precision <= limit,
                            )

    def test_terminal_precision_removes_all_false_zero_states(self):
        for a in range(1, 30):
            precision = terminal_zero_precision(a)
            for b in range(0, 100):
                roots = set(positive_horizon_states(a, b))
                observed_zero = {
                    n
                    for n in range(1, max(100, 4 * a + 10))
                    if charged_horizon_observation(precision, n, a, b) == 0
                }
                self.assertEqual(observed_zero, roots)

    def test_schwarzschild_is_charge_zero_special_case(self):
        for horizon in range(1, 30):
            for precision in range(1, 20):
                for radius in range(1, 80):
                    self.assertEqual(
                        charged_horizon_observation(precision, radius, horizon, 0),
                        horizon_observation(precision, radius, horizon),
                    )

    def test_uniform_integer_scale_preserves_observation_and_horizon_regime(self):
        for a in range(1, 20):
            for b in range(0, 60):
                original_delta = charged_discriminant(a, b)
                original_square = discriminant_is_square_fixed_point(a, b)
                for scale in range(1, 8):
                    scaled_a, scaled_b = rescale_coefficients(scale, a, b)
                    self.assertEqual(
                        charged_discriminant(scaled_a, scaled_b),
                        scale * scale * original_delta,
                    )
                    self.assertEqual(
                        discriminant_is_square_fixed_point(scaled_a, scaled_b),
                        original_square,
                    )
                    for precision in range(1, 8):
                        for radius in range(1, 30):
                            self.assertEqual(
                                charged_horizon_observation(
                                    precision, scale * radius, scaled_a, scaled_b
                                ),
                                charged_horizon_observation(precision, radius, a, b),
                            )

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(charged))
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
