import unittest
from fractions import Fraction

from enterprise_math.abc_activation_area_action_repair import (
    action_relative_area_repair,
    activation_area_orbit_future_collision,
    orbit_area_future_state,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class ActivationAreaActionRepairTests(unittest.TestCase):
    def setUp(self) -> None:
        thresholds = (Fraction(1, 2), Fraction(1))
        self.flat = dyadic_threshold_staircase(3, 5, 2, 1, thresholds)
        self.jump = dyadic_threshold_staircase(7, 17, 2, 1, thresholds)

    def test_equal_current_area_diverges_under_same_orbit_extension(self) -> None:
        collision = activation_area_orbit_future_collision(self.flat, self.jump)
        self.assertEqual(collision.common_current_area, 2)
        self.assertEqual(collision.left_new_node_rank, 1)
        self.assertEqual(collision.right_new_node_rank, 2)
        self.assertEqual(collision.left_future_area, 3)
        self.assertEqual(collision.right_future_area, 4)
        self.assertFalse(collision.future_area_equal)
        self.assertFalse(collision.area_quotient_future_safe)
        self.assertTrue(collision.collision_verified)

    def test_new_node_rank_repairs_one_step_orbit_future(self) -> None:
        flat = orbit_area_future_state(self.flat)
        jump = orbit_area_future_state(self.jump)
        self.assertEqual(flat.repaired_state, (2, 1))
        self.assertEqual(flat.future_area, 3)
        self.assertTrue(flat.future_reconstructed)
        self.assertEqual(jump.repaired_state, (2, 2))
        self.assertEqual(jump.future_area, 4)
        self.assertTrue(jump.future_reconstructed)

    def test_action_compiler_selects_crossing_for_threshold_action(self) -> None:
        repair = action_relative_area_repair(
            self.jump,
            "threshold",
            Fraction(3, 4),
        )
        self.assertEqual(repair.response_coordinate_name, "crossing_depth")
        self.assertEqual(repair.response_coordinate_value, 1)
        self.assertEqual(repair.directional_area_increment, 1)
        self.assertEqual(repair.future_area, 3)
        self.assertTrue(repair.future_reconstructed)

    def test_action_compiler_selects_rank_for_orbit_action(self) -> None:
        repair = action_relative_area_repair(self.jump, "orbit")
        self.assertEqual(repair.response_coordinate_name, "new_node_rank")
        self.assertEqual(repair.response_coordinate_value, 2)
        self.assertEqual(repair.directional_area_increment, 2)
        self.assertEqual(repair.future_area, 4)
        self.assertTrue(repair.future_reconstructed)

    def test_same_current_area_requires_different_directional_repairs(self) -> None:
        threshold_repair = action_relative_area_repair(
            self.jump,
            "threshold",
            Fraction(3, 4),
        )
        orbit_repair = action_relative_area_repair(self.jump, "orbit")
        self.assertEqual(threshold_repair.current_area, orbit_repair.current_area)
        self.assertNotEqual(
            threshold_repair.response_coordinate_name,
            orbit_repair.response_coordinate_name,
        )

    def test_invalid_action_contracts_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            action_relative_area_repair(self.flat, "threshold")
        with self.assertRaises(ValueError):
            action_relative_area_repair(self.flat, "orbit", Fraction(3, 4))
        with self.assertRaises(ValueError):
            action_relative_area_repair(self.flat, "unknown")


if __name__ == "__main__":
    unittest.main()
