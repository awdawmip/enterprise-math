import unittest

from enterprise_math.p017_actual_root_separation import (
    actual_lower_band_overlaps,
    actual_lower_band_root_images,
    actual_lower_band_root_images_disjoint,
    exact_window_lower_band_overlaps,
    exact_window_lower_band_root_images,
    exact_window_lower_band_root_images_disjoint,
)


class ActualRootSeparationTests(unittest.TestCase):
    def test_sharp_k8_actual_shell_root_collision(self) -> None:
        overlaps = actual_lower_band_overlaps(8)
        self.assertEqual(overlaps, ((2, 3, frozenset({5})),))

    def test_k6_collision_is_window_only_not_realized_shell(self) -> None:
        self.assertEqual(
            exact_window_lower_band_overlaps(6),
            ((2, 3, frozenset({4})),),
        )
        self.assertEqual(actual_lower_band_overlaps(6), ())

    def test_k9_starts_uniform_exact_window_and_actual_shell_separation(self) -> None:
        self.assertTrue(exact_window_lower_band_root_images_disjoint(9))
        self.assertTrue(actual_lower_band_root_images_disjoint(9))

        window_images = exact_window_lower_band_root_images(9)
        self.assertEqual(window_images[2], frozenset({6, 7}))
        self.assertEqual(window_images[3], frozenset({5}))

        actual_images = actual_lower_band_root_images(9)
        self.assertTrue(actual_images[2] <= window_images[2])
        self.assertTrue(actual_images[3] <= window_images[3])

    def test_exact_window_root_images_disjoint_through_large_finite_probe(self) -> None:
        for k in range(9, 2000):
            self.assertTrue(
                exact_window_lower_band_root_images_disjoint(k),
                (k, exact_window_lower_band_overlaps(k)),
            )

    def test_actual_shell_root_images_disjoint_through_large_finite_probe(self) -> None:
        for k in range(9, 1000):
            self.assertTrue(
                actual_lower_band_root_images_disjoint(k),
                (k, actual_lower_band_overlaps(k)),
            )

    def test_small_window_and_actual_collision_profiles_are_distinct(self) -> None:
        window_events = {
            k: exact_window_lower_band_overlaps(k)
            for k in range(2, 9)
            if exact_window_lower_band_overlaps(k)
        }
        self.assertEqual(
            window_events,
            {
                5: ((2, 3, frozenset({3})),),
                6: ((2, 3, frozenset({4})),),
                8: ((2, 3, frozenset({5})),),
            },
        )

        actual_events = {
            k: actual_lower_band_overlaps(k)
            for k in range(2, 9)
            if actual_lower_band_overlaps(k)
        }
        self.assertEqual(
            actual_events,
            {
                5: ((2, 3, frozenset({3})),),
                8: ((2, 3, frozenset({5})),),
            },
        )


if __name__ == "__main__":
    unittest.main()
