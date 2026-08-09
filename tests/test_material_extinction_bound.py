import unittest

from enterprise_math.material_extinction_bound import (
    integer_euclidean_ball_count_from_norm_sq,
    projected_rotation_extinction_upper_bound,
    witness_extinction_within_bound,
)
from enterprise_math.material_oscillator import PythagoreanRotation


class MaterialExtinctionBoundTests(unittest.TestCase):
    def test_small_integer_ball_counts(self):
        self.assertEqual(integer_euclidean_ball_count_from_norm_sq(0), 1)
        self.assertEqual(integer_euclidean_ball_count_from_norm_sq(1), 5)
        self.assertEqual(integer_euclidean_ball_count_from_norm_sq(2), 9)
        self.assertEqual(integer_euclidean_ball_count_from_norm_sq(4), 13)

    def test_zero_state_has_zero_transition_bound(self):
        self.assertEqual(projected_rotation_extinction_upper_bound((0, 0)), 0)
        report = witness_extinction_within_bound(
            (0, 0), PythagoreanRotation(3, 4, 5)
        )
        self.assertEqual(report.witnessed_extinction_time, 0)

    def test_reference_small_states_extinguish_within_exact_ball_count_bound(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for x in range(-8, 9):
            for y in range(-8, 9):
                report = witness_extinction_within_bound((x, y), rotation)
                self.assertIsNotNone(report.witnessed_extinction_time)
                self.assertLessEqual(
                    report.witnessed_extinction_time,
                    report.transition_upper_bound,
                )

    def test_lattice_ball_bound_is_rotation_independent_but_valid_for_multiple_triples(self):
        initial = (20, -17)
        bound = projected_rotation_extinction_upper_bound(initial)
        for rotation in (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(8, 15, 17),
        ):
            report = witness_extinction_within_bound(initial, rotation)
            self.assertEqual(report.transition_upper_bound, bound)
            self.assertLessEqual(report.witnessed_extinction_time, bound)

    def test_reference_399_40_401_extinction_is_far_below_coarse_state_bound(self):
        rotation = PythagoreanRotation(399, 40, 401)
        report = witness_extinction_within_bound((1000, 0), rotation)
        self.assertEqual(report.witnessed_extinction_time, 1570)
        self.assertGreater(report.transition_upper_bound, 1570)

    def test_invalid_norm_is_rejected(self):
        with self.assertRaises(ValueError):
            integer_euclidean_ball_count_from_norm_sq(-1)


if __name__ == "__main__":
    unittest.main()
