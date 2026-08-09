import unittest
from math import isqrt

from enterprise_math.label_erasure import (
    full_state_recoverable,
    label_decoder,
    label_recoverable,
    overlap_pairs,
)


class LabelErasureTests(unittest.TestCase):
    def test_label_recoverable_iff_shell_images_are_disjoint(self) -> None:
        shells = {
            "left": range(0, 4),
            "right": range(10, 14),
        }
        self.assertTrue(label_recoverable(shells, lambda x: x))
        self.assertEqual(overlap_pairs(shells, lambda x: x), ())

        self.assertFalse(label_recoverable(shells, lambda x: x % 10))
        collisions = overlap_pairs(shells, lambda x: x % 10)
        self.assertEqual(len(collisions), 1)
        self.assertEqual(collisions[0][2], frozenset({0, 1, 2, 3}))

    def test_decoder_exists_exactly_on_disjoint_images(self) -> None:
        shells = {2: [20, 21], 3: [30, 31]}
        decoder = label_decoder(shells, lambda x: x // 10)
        self.assertEqual(decoder, {2: 2, 3: 3})

        with self.assertRaises(ValueError):
            label_decoder(shells, lambda _x: 0)

    def test_label_recovery_is_weaker_than_full_state_recovery(self) -> None:
        shells = {
            "a": [25, 26, 27],
            "b": [49, 50],
        }
        self.assertTrue(label_recoverable(shells, isqrt))
        self.assertFalse(full_state_recoverable(shells, isqrt))

    def test_full_state_recovery_requires_within_shell_injectivity_too(self) -> None:
        shells = {"a": [1, 2], "b": [3, 4]}
        self.assertTrue(full_state_recoverable(shells, lambda x: x))
        self.assertFalse(full_state_recoverable(shells, lambda x: x // 2))


if __name__ == "__main__":
    unittest.main()
