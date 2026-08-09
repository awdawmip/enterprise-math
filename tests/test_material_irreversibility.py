import unittest

from enterprise_math.material_irreversibility import projected_rotation_fiber
from enterprise_math.material_oscillator import PythagoreanRotation


class MaterialIrreversibilityTests(unittest.TestCase):
    def test_reference_projected_value_has_three_global_histories_with_different_losses(self):
        rotation = PythagoreanRotation(3, 4, 5)
        fiber = projected_rotation_fiber((0, -25), rotation)
        self.assertEqual(fiber.multiplicity, 3)
        self.assertEqual(
            tuple(history.previous for history in fiber.histories),
            ((-21, -15), (-20, -16), (-20, -15)),
        )
        self.assertEqual(fiber.distinct_loss_values, (0, 31, 41))

    def test_zero_projected_state_has_five_preimages_for_3_4_5_rotation(self):
        rotation = PythagoreanRotation(3, 4, 5)
        fiber = projected_rotation_fiber((0, 0), rotation)
        self.assertEqual(fiber.multiplicity, 5)
        self.assertEqual(fiber.distinct_loss_values, (0, 1))
        self.assertIn((0, 0), [history.previous for history in fiber.histories])

    def test_same_zero_loss_can_land_in_fibers_with_different_multiplicity(self):
        rotation = PythagoreanRotation(3, 4, 5)
        left = projected_rotation_fiber((6, -42), rotation)
        right = projected_rotation_fiber((0, -35), rotation)
        self.assertEqual(left.multiplicity, 2)
        self.assertEqual(right.multiplicity, 3)
        self.assertIn(0, left.distinct_loss_values)
        self.assertIn(0, right.distinct_loss_values)

    def test_every_enumerated_history_is_unique_and_has_bounded_detail(self):
        rotation = PythagoreanRotation(5, 12, 13)
        for qx in range(-4, 5):
            for qy in range(-4, 5):
                fiber = projected_rotation_fiber((qx, qy), rotation)
                self.assertEqual(
                    fiber.multiplicity,
                    len({history.previous for history in fiber.histories}),
                )
                for history in fiber.histories:
                    self.assertLess(abs(history.details[0]), rotation.c)
                    self.assertLess(abs(history.details[1]), rotation.c)

    def test_projected_fiber_is_finite_even_on_infinite_integer_state_space(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for after in ((1000, 1000), (-1000, 0), (0, 1000), (-1000, -1000)):
            fiber = projected_rotation_fiber(after, rotation)
            # Finite detail enumeration gives a finite global fiber without a
            # bounded search box on previous states.
            self.assertLessEqual(fiber.multiplicity, (2 * rotation.c - 1) ** 2)


if __name__ == "__main__":
    unittest.main()
