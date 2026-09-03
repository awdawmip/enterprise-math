from __future__ import annotations

import inspect
import unittest
from decimal import Decimal
from fractions import Fraction

import enterprise_math.euler_character_completion as completion
from enterprise_math.euler_character_completion import (
    cayley_mesh_bound,
    cell_mean_tower,
    cell_viete_partial_product,
    character_mul,
    character_norm_square,
    chord_mesh,
    completion_report,
    phase_fraction,
    solve_normalized_quarter_turn_form,
    verify_cell_viete_telescope,
    verify_mesh_bound,
    verify_norm_multiplicativity,
    verify_phase_refinement,
    verify_uniform_residual_bound,
)
from enterprise_math.euler_cell_polygon_pi import cell_polygon_levels


class EulerCharacterCompletionTests(unittest.TestCase):
    def test_unique_normalized_quadratic_form(self) -> None:
        certificate = solve_normalized_quarter_turn_form()
        self.assertTrue(certificate.normalized_identity)
        self.assertTrue(certificate.is_unique_normalized_solution)
        samples = [
            (Fraction(-5, 7), Fraction(11, 13)),
            (Fraction(0), Fraction(1)),
            (Fraction(3, 2), Fraction(-4, 9)),
        ]
        self.assertTrue(certificate.invariant_on(samples))

    def test_character_norm_is_multiplicative(self) -> None:
        samples = [
            ((Fraction(3, 5), Fraction(4, 5)), (Fraction(5, 13), Fraction(12, 13))),
            ((Fraction(-7, 25), Fraction(24, 25)), (Fraction(1), Fraction(0))),
            ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(1))),
        ]
        for left, right in samples:
            self.assertTrue(verify_norm_multiplicativity(left, right))
            product = character_mul(left, right)
            self.assertEqual(
                character_norm_square(*product),
                character_norm_square(*left) * character_norm_square(*right),
            )

    def test_mean_renormalization_matches_polygon_tower(self) -> None:
        tolerance = Decimal("1e-90")
        for step in cell_mean_tower(10, precision=120):
            self.assertLess(abs(step.geometric_residual), tolerance)
            self.assertLess(abs(step.harmonic_residual), tolerance)
            self.assertLess(step.lower, step.next_lower)
            self.assertLess(step.next_lower, step.next_upper)
            self.assertLess(step.next_upper, step.upper)

    def test_cell_viete_telescope(self) -> None:
        for level in range(1, 11):
            self.assertTrue(verify_cell_viete_telescope(level, precision=120))
        self.assertEqual(cell_viete_partial_product(1, precision=120), Decimal(1))

    def test_first_cell_factor_is_sqrt_two_plus_sqrt_three_over_two(self) -> None:
        levels = cell_polygon_levels(2, precision=120)
        expected = ((Decimal(2) + Decimal(3).sqrt()).sqrt()) / Decimal(2)
        self.assertLess(abs(levels[2].scalar - expected), Decimal("1e-110"))

    def test_uniform_residual_width_bound(self) -> None:
        self.assertTrue(verify_uniform_residual_bound(12, precision=120))

    def test_chord_mesh_has_explicit_dyadic_bound(self) -> None:
        self.assertTrue(verify_mesh_bound(12, precision=120))
        for level in range(13):
            self.assertLess(
                chord_mesh(level, precision=120),
                cayley_mesh_bound(level, precision=120),
            )

    def test_phase_fraction_is_refinement_invariant(self) -> None:
        for level in range(9):
            sides = 6 * (2**level)
            for index in range(-2 * sides, 2 * sides + 1):
                self.assertTrue(verify_phase_refinement(level, index))
                self.assertEqual(
                    phase_fraction(level, index),
                    phase_fraction(level + 1, 2 * index),
                )

    def test_completion_report_is_finite_and_target_free(self) -> None:
        report = completion_report(8, precision=100)
        self.assertTrue(report["quadratic_form"]["normalized_unique"])
        self.assertTrue(report["mean_steps_valid"])

        source = inspect.getsource(completion)
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
