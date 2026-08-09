import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_recurrence_plateau import (
    min_quadratic_fixed_plateau_radius,
    min_quadratic_fixed_point_theorem,
    min_quadratic_fixed_points,
    min_quadratic_plateau,
)


class MaterialRecurrencePlateauTests(unittest.TestCase):
    def test_3_4_5_has_only_zero_and_unit_diagonal_plateaus(self):
        rotation = PythagoreanRotation(3, 4, 5)
        self.assertEqual(min_quadratic_fixed_plateau_radius(rotation), 1)
        self.assertEqual(
            min_quadratic_fixed_points(rotation),
            ((-1, -1), (0, 0), (1, 1)),
        )
        plateau = min_quadratic_plateau(rotation)
        self.assertEqual(plateau.fixed_point_count, 3)

    def test_399_40_401_has_100_positive_and_negative_plateaus(self):
        rotation = PythagoreanRotation(399, 40, 401)
        self.assertEqual(min_quadratic_fixed_plateau_radius(rotation), 100)
        plateau = min_quadratic_plateau(rotation)
        self.assertEqual(plateau.fixed_point_count, 201)
        self.assertEqual(plateau.fixed_points[0], (-100, -100))
        self.assertEqual(plateau.fixed_points[-1], (100, 100))

    def test_closed_form_matches_implemented_policy_on_selected_triples_and_box(self):
        rotations = (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(8, 15, 17),
            PythagoreanRotation(7, 24, 25),
            PythagoreanRotation(20, 21, 29),
            PythagoreanRotation(399, 40, 401),
        )
        for rotation in rotations:
            radius = min_quadratic_fixed_plateau_radius(rotation)
            bound = radius + 4
            for u in range(-bound, bound + 1):
                for v in range(-bound, bound + 1):
                    min_quadratic_fixed_point_theorem(u, v, rotation)

    def test_off_diagonal_states_are_never_fixed(self):
        rotation = PythagoreanRotation(399, 40, 401)
        for k in range(-20, 21):
            self.assertFalse(
                min_quadratic_fixed_point_theorem(k, k + 1, rotation)
            )

    def test_first_state_outside_plateau_is_not_fixed(self):
        rotation = PythagoreanRotation(399, 40, 401)
        radius = min_quadratic_fixed_plateau_radius(rotation)
        self.assertFalse(
            min_quadratic_fixed_point_theorem(
                radius + 1,
                radius + 1,
                rotation,
            )
        )
        self.assertFalse(
            min_quadratic_fixed_point_theorem(
                -(radius + 1),
                -(radius + 1),
                rotation,
            )
        )


if __name__ == "__main__":
    unittest.main()
