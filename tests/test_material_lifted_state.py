import unittest

from enterprise_math.material_lifted_state import (
    advance_lifted_rotation_state,
    axis_lifted_rotation_orbit,
    initial_axis_lifted_rotation_state,
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
    def test_exact_lifted_orbit_preserves_arbitrary_base_norm_per_scale(self):
        rotation = PythagoreanRotation(3, 4, 5)
        initial = (-20, -16)
        base_norm_sq = initial[0] * initial[0] + initial[1] * initial[1]
        states = lifted_rotation_orbit(initial, rotation, 8)
        for index, state in enumerate(states):
            self.assertEqual(state.step, index)
            self.assertEqual(state.scale, rotation.c**index)
            self.assertEqual(state.base_norm_sq, base_norm_sq)
            self.assertEqual(
                state.x * state.x + state.y * state.y,
                base_norm_sq * state.scale * state.scale,
            )

    def test_axis_helper_is_only_a_specialization(self):
        rotation = PythagoreanRotation(3, 4, 5)
        direct = lifted_rotation_orbit((17, 0), rotation, 5)
        axis = axis_lifted_rotation_orbit(17, rotation, 5)
        self.assertEqual(direct, axis)
        self.assertEqual(initial_axis_lifted_rotation_state(17), direct[0])

    def test_one_exact_lift_matches_existing_rotation_lift_state(self):
        rotation = PythagoreanRotation(3, 4, 5)
        state = initial_lifted_rotation_state(10, 0)
        state = advance_lifted_rotation_state(state, rotation)
        self.assertEqual((state.x, state.y, state.scale), (30, 40, 5))
        projection = project_lifted_state_toward_zero(state, 1)
        self.assertEqual(projection.coordinates, (6, 8))
        self.assertEqual(projection.details, (0, 0))

    def test_projecting_exact_lifted_state_once_matches_batched_schedule_for_arbitrary_states(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for x in range(-6, 7):
            for y in range(-6, 7):
                for steps in range(5):
                    orbit_state = lifted_rotation_orbit((x, y), rotation, steps)[-1]
                    projected = project_lifted_state_toward_zero(orbit_state, 1)
                    self.assertEqual(
                        projected.coordinates,
                        batched_rotation_projection((x, y), rotation, steps),
                    )

    def test_sequential_and_batched_projection_are_distinct_schedules_on_arbitrary_state(self):
        rotation = PythagoreanRotation(3, 4, 5)
        initial = (-20, -16)
        exact_two = lifted_rotation_orbit(initial, rotation, 2)[-1]
        batched = project_lifted_state_toward_zero(exact_two, 1).coordinates
        sequential = initial
        for _ in range(2):
            sequential = projected_rotation_step(
                *sequential, rotation, TOWARD_ZERO
            ).after
        self.assertEqual(sequential, (20, -15))
        self.assertEqual(batched, (20, -14))
        self.assertNotEqual(batched, sequential)

    def test_projection_requires_a_divisor_scale(self):
        rotation = PythagoreanRotation(3, 4, 5)
        state = lifted_rotation_orbit((10, 0), rotation, 2)[-1]
        self.assertEqual(state.scale, 25)
        with self.assertRaises(ValueError):
            project_lifted_state_toward_zero(state, 3)


if __name__ == "__main__":
    unittest.main()
