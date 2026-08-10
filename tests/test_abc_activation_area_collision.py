import unittest
from fractions import Fraction

from enterprise_math.abc_activation_area_collision import activation_area_collision
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class ActivationAreaCollisionTests(unittest.TestCase):
    def test_exact_same_grid_same_area_different_boundary_collision(self) -> None:
        thresholds = (Fraction(1, 2), Fraction(1))
        flat = dyadic_threshold_staircase(3, 5, 2, 1, thresholds)
        jump = dyadic_threshold_staircase(7, 17, 2, 1, thresholds)

        self.assertEqual(flat.pressures, (Fraction(1, 2), Fraction(1, 2)))
        self.assertEqual(jump.pressures, (Fraction(1, 6), Fraction(13, 6)))

        collision = activation_area_collision(flat, jump)
        self.assertTrue(collision.area_equal)
        self.assertEqual(collision.common_area, 2)
        self.assertFalse(collision.activation_matrix_equal)
        self.assertFalse(collision.crossing_depths_equal)
        self.assertFalse(collision.node_ranks_equal)
        self.assertFalse(collision.boundary_word_equal)
        self.assertTrue(collision.collision_verified)

        self.assertEqual(flat.crossing_depths, (0, None))
        self.assertEqual(jump.crossing_depths, (1, 1))
        self.assertEqual(
            flat.activation_matrix,
            ((True, True), (False, False)),
        )
        self.assertEqual(
            jump.activation_matrix,
            ((False, True), (False, True)),
        )

    def test_collision_distinguishes_a_declared_future_cell(self) -> None:
        thresholds = (Fraction(1, 2), Fraction(1))
        flat = dyadic_threshold_staircase(3, 5, 2, 1, thresholds)
        jump = dyadic_threshold_staircase(7, 17, 2, 1, thresholds)
        collision = activation_area_collision(flat, jump)
        self.assertEqual(collision.first_distinguishing_cell, (0, 0))
        self.assertTrue(collision.left_cell_value)
        self.assertFalse(collision.right_cell_value)

    def test_area_is_safe_only_for_the_aggregate_area_query(self) -> None:
        thresholds = (Fraction(1, 2), Fraction(1))
        flat = dyadic_threshold_staircase(3, 5, 2, 1, thresholds)
        jump = dyadic_threshold_staircase(7, 17, 2, 1, thresholds)
        collision = activation_area_collision(flat, jump)
        # The area future cannot distinguish the pair by definition.
        self.assertEqual(collision.common_area, 2)
        # Any future retaining this threshold/node cell can distinguish it.
        self.assertNotEqual(flat.activation_matrix[0][0], jump.activation_matrix[0][0])

    def test_rejects_different_threshold_grids(self) -> None:
        left = dyadic_threshold_staircase(
            3, 5, 2, 1, (Fraction(1, 2), Fraction(1))
        )
        right = dyadic_threshold_staircase(
            7, 17, 2, 1, (Fraction(1, 3), Fraction(1))
        )
        with self.assertRaises(ValueError):
            activation_area_collision(left, right)


if __name__ == "__main__":
    unittest.main()
