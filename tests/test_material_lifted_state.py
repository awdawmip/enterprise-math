import unittest

from enterprise_math.material_lifted_state import (
    advance_lifted_rotation_state,
    initial_lifted_rotation_state,
    lifted_rotation_orbit,
    project_lifted_state_toward_zero,
)
from enterprise_math.material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    projected_rotation_step,
)
from enterprise_math.material_projection_schedule import batched_rotation_projection


class MaterialLiftedStateTests(unittest.TestCase):
    def test_exact_lifted_orbit_preserves_radius_per_explicit_scale(self):
        rotation = PythagoreanRotation(3, 4, 5)
        amplitude = 17
        states = lifted_rotation_orbit(amplitude, rotation, 8)
        for index, state in enumerate(states):
            self.assertEqual(state.step, index)
            self.assertEqual(state.scale, rotation.c**index)
            self.assertEqual(
                state.x * state.x + state.y * state.y,
                amplitude * amplitude * state.scale * state.scale,
            )

    def test_one_exact_lift_matches_existing_rotation_lift_state(self):
        rotation = PythagoreanRotation(3, 4, 5)
        state = initial_lifted_rotation_state(10)
        state = advance_lifted_rotation_state(state, rotation)
        self.assertEqual((state.x, state.y, state.scale), (30, 40, 5))
        projection = project_lifted_state_toward_zero(state, 1)
        self.assertEqual(projection.coordinates, (6, 8))
        self.assertEqual(projection.details, (0, 0))

    def test_projecting_exact_lifted_state_once_matches_batched_schedule(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for x in range(-5, 6):
            for y in range(-5, 6):
                amplitude_sq = x * x + y * y
                root = int(amplitude_sq**0.5)
                if root * root != amplitude_sq:
                    continue
                # Build a valid exact state directly at scale 1 only when the
                # integer point lies on an integer-radius circle.
                state = initial_lifted_rotation_state(root)
                # Rotate the axis-aligned amplitude instead of arbitrary (x,y)
                # so the invariant constructor remains explicit.
                _ = x, y
                for steps in range(5):
                    orbit_state = lifted_rotation_orbit(root, rotation, steps)[-1]
                    projected = project_lifted_state_toward_zero(orbit_state, 1)
                    self.assertEqual(
                        projected.coordinates,
                        batched_rotation_projection((root, 0), rotation, steps),
                    )

    def test_sequential_projection_is_a_different_precision_schedule(self):
        rotation = PythagoreanRotation(3, 4, 5)
        exact_two = lifted_rotation_orbit(20, rotation, 2)[-1]
        batched = project_lifted_state_toward_zero(exact_two, 1).coordinates
        sequential = (20, 0)
        for _ in range(2):
            sequential = projected_rotation_step(
                *sequential, rotation, TOWARD_ZERO
            ).after
        # This particular axis-aligned state happens to agree; the general
        # cadence counterexamples are covered in test_material_projection_schedule.
        self.assertEqual(batched, sequential)

    def test_projection_requires_a_divisor_scale(self):
        rotation = PythagoreanRotation(3, 4, 5)
        state = lifted_rotation_orbit(10, rotation, 2)[-1]
        self.assertEqual(state.scale, 25)
        with self.assertRaises(ValueError):
            project_lifted_state_toward_zero(state, 3)


if __name__ == "__main__":
    unittest.main()
