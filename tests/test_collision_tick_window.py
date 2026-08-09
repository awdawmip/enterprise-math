import unittest
from itertools import product

from enterprise_math.collision_phase_diagram import interaction_band_states_1d
from enterprise_math.collision_tick_window import (
    ContactTickWindow,
    first_static_contact_tick,
    static_contact_tick_window,
)


def brute_contact(start, step, half_width, tick):
    return all(
        abs(coordinate + tick * velocity) <= half_width
        for coordinate, velocity in zip(start, step, strict=True)
    )


class CollisionTickWindowTests(unittest.TestCase):
    def test_window_membership_matches_direct_integer_sampling_on_small_2d_domain(self):
        starts = list(product(range(-4, 5, 2), repeat=2))
        steps = list(product(range(-2, 3), repeat=2))
        for radius_sum in range(2):
            for factor in range(1, 4):
                half_width = radius_sum + factor - 1
                for start in starts:
                    for step in steps:
                        window = static_contact_tick_window(
                            start, step, radius_sum, factor
                        )
                        for tick in range(11):
                            expected = brute_contact(start, step, half_width, tick)
                            actual = window is not None and window.contains(tick)
                            self.assertEqual(
                                actual,
                                expected,
                                (start, step, radius_sum, factor, tick, window),
                            )

    def test_stationary_inside_band_has_unbounded_contact_window(self):
        window = static_contact_tick_window((1, -1), (0, 0), 0, 2)
        self.assertEqual(window, ContactTickWindow(0, None))
        self.assertTrue(window.contains(10_000))

    def test_stationary_outside_any_coordinate_never_contacts(self):
        self.assertIsNone(static_contact_tick_window((2, 0), (0, 0), 0, 2))

    def test_aligned_diagonal_motion_hits_same_integer_tick(self):
        window = static_contact_tick_window((-2, -2), (2, 2), 0, 2)
        self.assertIsNotNone(window)
        self.assertTrue(window.contains(1))
        self.assertEqual(first_static_contact_tick((-2, -2), (2, 2), 0, 2), 1)

    def test_coordinate_entry_times_can_miss_despite_small_linf_step(self):
        radius_sum = 0
        factor = 2
        start = (-2, 0)
        step = (2, 2)
        self.assertLessEqual(
            max(abs(value) for value in step),
            interaction_band_states_1d(radius_sum, factor),
        )
        self.assertIsNone(static_contact_tick_window(start, step, radius_sum, factor))

    def test_terminal_point_swap_has_no_static_contact_tick(self):
        self.assertIsNone(
            static_contact_tick_window((1, 0), (-2, 0), radius_sum=0, collapse_factor=1)
        )

    def test_coarser_point_swap_is_already_macro_contact_at_tick_zero(self):
        window = static_contact_tick_window(
            (1, 0), (-2, 0), radius_sum=0, collapse_factor=2
        )
        self.assertIsNotNone(window)
        self.assertEqual(window.first_tick, 0)

    def test_one_dimensional_solver_matches_direct_samples(self):
        for factor in range(1, 5):
            half_width = factor - 1
            for start in range(-8, 9):
                for step in range(-3, 4):
                    window = static_contact_tick_window(
                        (start,), (step,), radius_sum=0, collapse_factor=factor
                    )
                    for tick in range(10):
                        expected = abs(start + tick * step) <= half_width
                        actual = window is not None and window.contains(tick)
                        self.assertEqual(actual, expected)

    def test_invalid_shapes_are_rejected(self):
        with self.assertRaises(ValueError):
            static_contact_tick_window((), (), 0, 1)
        with self.assertRaises(ValueError):
            static_contact_tick_window((0,), (0, 1), 0, 1)
        with self.assertRaises(ValueError):
            static_contact_tick_window((0,), (True,), 0, 1)


if __name__ == "__main__":
    unittest.main()
