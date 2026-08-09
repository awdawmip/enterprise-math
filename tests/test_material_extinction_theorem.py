import unittest

from enterprise_math.material_extinction_theorem import (
    certify_no_nonzero_periodic_orbit,
    finite_order_obstruction,
    reduced_rotation_trace,
    zero_loss_step_is_exact,
)
from enterprise_math.material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    projected_rotation_step,
)


class MaterialExtinctionTheoremTests(unittest.TestCase):
    def test_known_rotations_have_nonintegral_reduced_trace(self):
        cases = (
            (PythagoreanRotation(3, 4, 5), (6, 5)),
            (PythagoreanRotation(5, 12, 13), (10, 13)),
            (PythagoreanRotation(8, 15, 17), (16, 17)),
            (PythagoreanRotation(399, 40, 401), (798, 401)),
        )
        for rotation, expected in cases:
            self.assertEqual(reduced_rotation_trace(rotation), expected)
            obstruction = finite_order_obstruction(rotation)
            self.assertGreater(obstruction.reduced_trace_denominator, 1)
            self.assertTrue(obstruction.trace_is_noninteger)
            self.assertTrue(obstruction.rational_root_theorem_requires_integer_trace)

    def test_zero_radius_loss_is_exactly_zero_projection_detail(self):
        rotations = (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(8, 15, 17),
        )
        saw_exact_nonzero = False
        saw_lossy = False
        for rotation in rotations:
            for x in range(-12, 13):
                for y in range(-12, 13):
                    step = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
                    exact = zero_loss_step_is_exact(step)
                    self.assertEqual(exact, step.details == (0, 0))
                    self.assertEqual(exact, step.norm_sq_loss == 0)
                    saw_exact_nonzero |= exact and (x, y) != (0, 0)
                    saw_lossy |= not exact
        self.assertTrue(saw_exact_nonzero)
        self.assertTrue(saw_lossy)

    def test_no_nonzero_cycle_certificate_exists_for_valid_rotations(self):
        for rotation in (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(8, 15, 17),
            PythagoreanRotation(399, 40, 401),
        ):
            certificate = certify_no_nonzero_periodic_orbit(rotation)
            self.assertTrue(certificate.no_nonzero_periodic_orbit)
            self.assertGreater(
                certificate.finite_order_obstruction.reduced_trace_denominator,
                1,
            )

    def test_bounded_orbits_find_zero_before_any_nonzero_repeat(self):
        rotations = (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
        )
        for rotation in rotations:
            for x0 in range(-5, 6):
                for y0 in range(-5, 6):
                    state = (x0, y0)
                    seen = set()
                    for _ in range(500):
                        if state == (0, 0):
                            break
                        self.assertNotIn(state, seen)
                        seen.add(state)
                        state = projected_rotation_step(
                            *state, rotation, TOWARD_ZERO
                        ).after
                    self.assertEqual(state, (0, 0))


if __name__ == "__main__":
    unittest.main()
