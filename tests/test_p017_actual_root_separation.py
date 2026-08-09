import unittest

from enterprise_math.p017_actual_root_separation import (
    actual_lower_band_overlaps,
    actual_lower_band_root_images,
    actual_lower_band_root_images_disjoint,
)


class ActualRootSeparationTests(unittest.TestCase):
    def test_sharp_k8_actual_root_collision(self) -> None:
        overlaps = actual_lower_band_overlaps(8)
        self.assertEqual(overlaps, ((2, 3, frozenset({5})),))

    def test_k9_starts_uniform_actual_root_separation(self) -> None:
        self.assertTrue(actual_lower_band_root_images_disjoint(9))
        images = actual_lower_band_root_images(9)
        self.assertEqual(images[2], frozenset({6, 7}))
        self.assertEqual(images[3], frozenset({5}))

    def test_actual_root_images_disjoint_through_large_finite_probe(self) -> None:
        for k in range(9, 2000):
            self.assertTrue(
                actual_lower_band_root_images_disjoint(k),
                (k, actual_lower_band_overlaps(k)),
            )

    def test_only_small_actual_collisions_before_stable_threshold(self) -> None:
        events = {
            k: actual_lower_band_overlaps(k)
            for k in range(2, 9)
            if actual_lower_band_overlaps(k)
        }
        self.assertEqual(
            events,
            {
                5: ((2, 3, frozenset({3})),),
                6: ((2, 3, frozenset({4})),),
                8: ((2, 3, frozenset({5})),),
            },
        )


if __name__ == "__main__":
    unittest.main()
