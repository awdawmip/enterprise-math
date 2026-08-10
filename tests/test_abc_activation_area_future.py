import unittest
from fractions import Fraction

from enterprise_math.abc_activation_area_future import (
    activation_area_future_collision,
    threshold_area_future_state,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class ActivationAreaFutureTests(unittest.TestCase):
    def setUp(self) -> None:
        thresholds = (Fraction(1, 2), Fraction(1))
        self.flat = dyadic_threshold_staircase(3, 5, 2, 1, thresholds)
        self.jump = dyadic_threshold_staircase(7, 17, 2, 1, thresholds)

    def test_equal_current_area_diverges_under_same_threshold_extension(self) -> None:
        collision = activation_area_future_collision(
            self.flat,
            self.jump,
            Fraction(3, 4),
        )
        self.assertEqual(collision.common_current_area, 2)
        self.assertIsNone(collision.left_crossing_depth)
        self.assertEqual(collision.right_crossing_depth, 1)
        self.assertEqual(collision.left_future_area, 2)
        self.assertEqual(collision.right_future_area, 3)
        self.assertFalse(collision.future_area_equal)
        self.assertFalse(collision.area_quotient_future_safe)
        self.assertTrue(collision.collision_verified)

    def test_crossing_depth_repairs_one_step_future_area(self) -> None:
        flat = threshold_area_future_state(self.flat, Fraction(3, 4))
        jump = threshold_area_future_state(self.jump, Fraction(3, 4))
        self.assertEqual(flat.repaired_state, (2, None))
        self.assertEqual(flat.active_span, 0)
        self.assertEqual(flat.future_area, 2)
        self.assertTrue(flat.future_reconstructed)

        self.assertEqual(jump.repaired_state, (2, 1))
        self.assertEqual(jump.active_span, 1)
        self.assertEqual(jump.future_area, 3)
        self.assertTrue(jump.future_reconstructed)

    def test_current_area_plus_delta_is_equivalent_one_step_repair(self) -> None:
        state = threshold_area_future_state(self.jump, Fraction(3, 4))
        self.assertEqual(state.future_area, state.current_area + state.active_span)
        # At fixed h=1, crossing depth 1 and active span 1 determine each other.
        self.assertEqual(state.crossing_depth, 1)
        self.assertEqual(state.active_span, 1)

    def test_a_threshold_already_in_grid_is_not_a_valid_extension(self) -> None:
        with self.assertRaises(ValueError):
            threshold_area_future_state(self.flat, Fraction(1, 2))


if __name__ == "__main__":
    unittest.main()
