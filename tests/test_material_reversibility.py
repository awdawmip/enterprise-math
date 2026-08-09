import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_reversibility import (
    ExtendedProjectedRotationState,
    after_only_collision,
    extended_projected_rotation_state,
    reconstruct_previous_rotation_state,
)


class MaterialReversibilityTests(unittest.TestCase):
    def test_retained_details_reconstruct_every_small_previous_state(self):
        rotation = PythagoreanRotation(3, 4, 5)
        seen = set()
        for x in range(-20, 21):
            for y in range(-20, 21):
                previous = (x, y)
                extended = extended_projected_rotation_state(previous, rotation)
                self.assertEqual(
                    reconstruct_previous_rotation_state(extended, rotation),
                    previous,
                )
                self.assertNotIn(extended, seen)
                seen.add(extended)

    def test_value_only_projection_has_explicit_history_merge(self):
        rotation = PythagoreanRotation(3, 4, 5)
        left = (-20, -16)
        right = (-20, -15)
        left_extended = extended_projected_rotation_state(left, rotation)
        right_extended = extended_projected_rotation_state(right, rotation)
        self.assertEqual(left_extended.after, (0, -25))
        self.assertEqual(right_extended.after, (0, -25))
        self.assertEqual(left_extended.details, (4, -3))
        self.assertEqual(right_extended.details, (0, 0))
        self.assertTrue(after_only_collision(left, right, rotation))
        self.assertNotEqual(left_extended, right_extended)

    def test_invalid_detail_state_outside_rotation_image_is_rejected(self):
        rotation = PythagoreanRotation(3, 4, 5)
        invalid = ExtendedProjectedRotationState(
            after=(0, 0),
            details=(1, 0),
        )
        with self.assertRaises(ValueError):
            reconstruct_previous_rotation_state(invalid, rotation)

    def test_detail_bound_is_enforced(self):
        rotation = PythagoreanRotation(3, 4, 5)
        invalid = ExtendedProjectedRotationState(
            after=(0, 0),
            details=(5, 0),
        )
        with self.assertRaises(ValueError):
            reconstruct_previous_rotation_state(invalid, rotation)

    def test_same_previous_state_is_not_called_history_collision(self):
        rotation = PythagoreanRotation(3, 4, 5)
        state = (7, -9)
        self.assertFalse(after_only_collision(state, state, rotation))


if __name__ == "__main__":
    unittest.main()
