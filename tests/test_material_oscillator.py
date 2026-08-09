import unittest

from enterprise_math.material_oscillator import (
    FLOOR,
    TOWARD_ZERO,
    PythagoreanRotation,
    digital_circle_quarter,
    digital_circle_radial_defect,
    integer_rotation_lift,
    projected_rotation_first_repeat,
    projected_rotation_orbit,
    projected_rotation_step,
    recurrence_first_repeat,
    recurrence_sine_samples,
    signed_divmod_toward_zero,
    signed_project,
)


class MaterialOscillatorTests(unittest.TestCase):
    def test_pythagorean_lift_has_exact_scaled_norm(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for x in range(-8, 9):
            for y in range(-8, 9):
                raw_x, raw_y = integer_rotation_lift(x, y, rotation)
                self.assertEqual(
                    raw_x * raw_x + raw_y * raw_y,
                    25 * (x * x + y * y),
                )

    def test_toward_zero_divmod_reconstructs_signed_state(self):
        for divisor in range(1, 9):
            for value in range(-40, 41):
                quotient, detail = signed_divmod_toward_zero(value, divisor)
                self.assertEqual(value, divisor * quotient + detail)
                self.assertLess(abs(detail), divisor)
                if detail:
                    self.assertEqual(detail > 0, value > 0)
                self.assertEqual(quotient, signed_project(value, divisor, TOWARD_ZERO))

    def test_toward_zero_projected_rotation_never_increases_squared_radius(self):
        rotation = PythagoreanRotation(3, 4, 5)
        saw_loss = False
        for x in range(-12, 13):
            for y in range(-12, 13):
                report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
                self.assertLessEqual(report.norm_sq_after, report.norm_sq_before)
                self.assertEqual(
                    report.norm_sq_loss,
                    report.norm_sq_before - report.norm_sq_after,
                )
                saw_loss |= report.norm_sq_loss > 0
        self.assertTrue(saw_loss)

    def test_floor_projection_can_increase_squared_radius_on_negative_states(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = projected_rotation_step(-20, -19, rotation, FLOOR)
        self.assertEqual(report.after, (3, -28))
        self.assertEqual(report.norm_sq_before, 761)
        self.assertEqual(report.norm_sq_after, 793)
        self.assertLess(report.norm_sq_loss, 0)

    def test_high_resolution_rotation_has_expected_quarter_wave_prefix(self):
        rotation = PythagoreanRotation(399, 40, 401)
        orbit = projected_rotation_orbit(1000, rotation, 16, TOWARD_ZERO)
        self.assertEqual(
            tuple(y for _x, y in orbit),
            (0, 99, 197, 293, 386, 475, 560, 639, 712, 777, 835, 884, 924, 955, 977, 989, 991),
        )
        norms = [x * x + y * y for x, y in orbit]
        self.assertEqual(norms, sorted(norms, reverse=True))

    def test_toward_zero_rotation_eventually_reaches_zero_in_reference_probe(self):
        rotation = PythagoreanRotation(399, 40, 401)
        repeat = projected_rotation_first_repeat(1000, rotation, 2000, TOWARD_ZERO)
        self.assertIsNotNone(repeat)
        first_index, repeat_index, states = repeat
        self.assertEqual(first_index, repeat_index - 1)
        self.assertEqual(states[-1], (0, 0))

    def test_recurrence_is_distinct_from_two_coordinate_rotation_and_can_cycle(self):
        rotation = PythagoreanRotation(399, 40, 401)
        recurrence = recurrence_sine_samples(1000, rotation, 17, TOWARD_ZERO)
        orbit = projected_rotation_orbit(1000, rotation, 16, TOWARD_ZERO)
        rotation_y = tuple(y for _x, y in orbit)
        self.assertEqual(recurrence[:6], rotation_y[:6])
        self.assertNotEqual(recurrence, rotation_y)
        cycle = recurrence_first_repeat(1000, rotation, 2000, TOWARD_ZERO)
        self.assertIsNotNone(cycle)
        first, repeated = cycle
        self.assertLess(first, repeated)
        self.assertGreater(first, 0)

    def test_digital_circle_is_monotone_and_has_exact_root_basin_defect_bound(self):
        amplitude = 40
        points = digital_circle_quarter(amplitude)
        self.assertEqual(points[0], (amplitude, 0))
        self.assertEqual(points[-1], (0, amplitude))
        xs = [x for x, _y in points]
        ys = [y for _x, y in points]
        self.assertEqual(xs, sorted(xs, reverse=True))
        self.assertEqual(ys, sorted(ys))
        for point in points:
            _x, y = point
            defect = digital_circle_radial_defect(amplitude, point)
            self.assertGreaterEqual(defect, 0)
            self.assertLess(defect, 2 * y + 1)

    def test_invalid_rotation_and_projection_modes_are_rejected(self):
        with self.assertRaises(ValueError):
            PythagoreanRotation(3, 4, 6)
        with self.assertRaises(ValueError):
            signed_project(1, 2, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
