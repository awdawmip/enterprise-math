import unittest

from enterprise_math.material_integer_linear_oscillator import (
    ELLIPTIC_SHORT_PERIOD,
    HYPERBOLIC,
    PARABOLIC_BOUNDARY,
    integer_linear_material_invariant,
    integer_linear_material_step,
    integer_linear_oscillator_classification,
    iterate_integer_linear_material,
)


class MaterialIntegerLinearOscillatorTests(unittest.TestCase):
    def test_exact_integer_quadratic_invariant_is_preserved(self):
        for a in range(1, 6):
            for b in range(1, 6):
                for x in range(-10, 11):
                    for p in range(-10, 11):
                        before = integer_linear_material_invariant(x, p, a, b)
                        x1, p1 = integer_linear_material_step(x, p, a, b)
                        after = integer_linear_material_invariant(x1, p1, a, b)
                        self.assertEqual(before, after)

    def test_positive_integer_elliptic_cases_have_only_periods_6_4_3(self):
        cases = ((1, 1, 6), (1, 2, 4), (2, 1, 4), (1, 3, 3), (3, 1, 3))
        for a, b, period in cases:
            report = integer_linear_oscillator_classification(a, b)
            self.assertEqual(report.regime, ELLIPTIC_SHORT_PERIOD)
            self.assertEqual(report.exact_matrix_period, period)
            self.assertGreater(report.invariant_discriminant_resource, 0)
            for state in ((1, 0), (0, 1), (2, -3), (-4, 5)):
                self.assertEqual(
                    iterate_integer_linear_material(*state, a, b, period),
                    state,
                )

    def test_matrix_periods_are_exact_not_merely_upper_bounds(self):
        for a, b, period in ((1, 1, 6), (1, 2, 4), (2, 1, 4), (1, 3, 3), (3, 1, 3)):
            basis = ((1, 0), (0, 1))
            for shorter in range(1, period):
                self.assertTrue(
                    any(
                        iterate_integer_linear_material(*state, a, b, shorter) != state
                        for state in basis
                    )
                )

    def test_product_four_is_parabolic_and_has_linear_growth_witness(self):
        for a, b in ((1, 4), (2, 2), (4, 1)):
            report = integer_linear_oscillator_classification(a, b)
            self.assertEqual(report.regime, PARABOLIC_BOUNDARY)
            self.assertEqual(report.invariant_discriminant_resource, 0)
            states = [iterate_integer_linear_material(1, 0, a, b, n) for n in range(8)]
            magnitudes = [max(abs(x), abs(p)) for x, p in states]
            self.assertGreater(magnitudes[-1], magnitudes[1])

    def test_product_above_four_is_hyperbolic_and_indefinite(self):
        for a, b in ((1, 5), (2, 3), (3, 2), (5, 1)):
            report = integer_linear_oscillator_classification(a, b)
            self.assertEqual(report.regime, HYPERBOLIC)
            self.assertLess(report.invariant_discriminant_resource, 0)
            start = max(abs(v) for v in (1, 0))
            end_state = iterate_integer_linear_material(1, 0, a, b, 8)
            self.assertGreater(max(abs(v) for v in end_state), start)

    def test_reference_ab_one_orbit_is_exact_six_phase_hexagonal_cycle(self):
        state = (5, 0)
        orbit = [state]
        for _ in range(6):
            state = integer_linear_material_step(*state, 1, 1)
            orbit.append(state)
        self.assertEqual(
            orbit,
            [(5, 0), (0, -5), (-5, -5), (-5, 0), (0, 5), (5, 5), (5, 0)],
        )
        self.assertTrue(all(integer_linear_material_invariant(x, p, 1, 1) == 25 for x, p in orbit))

    def test_invalid_coefficients_are_rejected(self):
        with self.assertRaises(ValueError):
            integer_linear_oscillator_classification(0, 1)
        with self.assertRaises(ValueError):
            integer_linear_material_step(1, 0, 1, 0)


if __name__ == "__main__":
    unittest.main()
