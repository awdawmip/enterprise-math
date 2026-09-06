from __future__ import annotations

import unittest
from math import isqrt

from enterprise_math.brc_multiplier_strip_reduction import (
    multiplier_strip_class,
    reduce_square_hit_to_parent,
    strip_reduced_multipliers,
    two_adic_strip_counts,
)


class BRCMultiplierStripReductionTests(unittest.TestCase):
    def test_complete_2adic_classification_through_100(self) -> None:
        counts = two_adic_strip_counts(100)
        self.assertEqual(counts, {
            "IMPOSSIBLE": 25,
            "REDUNDANT_BY_4": 13,
            "PRIMITIVE_2ADIC": 62,
        })
        reduced = strip_reduced_multipliers(100)
        self.assertEqual(len(reduced), 62)
        self.assertTrue(all(m % 4 != 2 and m % 8 != 4 for m in reduced))

    def test_impossible_class_has_no_square_gap_hit(self) -> None:
        for n in range(3, 250, 2):
            for m in range(2, 101, 4):
                base = isqrt(m * n)
                if base * base != m * n:
                    base += 1
                for t in range(30):
                    gap = (base + t) * (base + t) - m * n
                    root = isqrt(gap)
                    self.assertNotEqual(root * root, gap)

    def test_redundant_hit_maps_to_parent_with_half_offset(self) -> None:
        mapped = 0
        for n in range(3, 180, 2):
            for m in range(4, 101, 8):
                base = isqrt(m * n)
                if base * base != m * n:
                    base += 1
                for t in range(60):
                    gap = (base + t) * (base + t) - m * n
                    root = isqrt(gap)
                    if root * root != gap:
                        continue
                    witness = reduce_square_hit_to_parent(n, m, t)
                    self.assertIsNotNone(witness)
                    assert witness is not None
                    self.assertEqual(witness.parent_multiplier, m // 4)
                    self.assertEqual(witness.parent_t, t // 2)
                    self.assertEqual(witness.parent_x * 2, witness.x)
                    self.assertEqual(witness.parent_y * 2, witness.y)
                    mapped += 1
        self.assertGreater(mapped, 100)

    def test_nonsquare_gap_returns_none(self) -> None:
        # N=15, m=4 has base ceil(sqrt(60))=8; t=0 gives gap 4 (hit), t=1 gives 21.
        self.assertIsNone(reduce_square_hit_to_parent(15, 4, 1))
        witness = reduce_square_hit_to_parent(15, 4, 0)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual((witness.parent_multiplier, witness.parent_t), (1, 0))

    def test_class_boundary_examples(self) -> None:
        self.assertEqual(multiplier_strip_class(6), "IMPOSSIBLE")
        self.assertEqual(multiplier_strip_class(12), "REDUNDANT_BY_4")
        self.assertEqual(multiplier_strip_class(5), "PRIMITIVE_2ADIC")
        self.assertEqual(multiplier_strip_class(8), "PRIMITIVE_2ADIC")


if __name__ == "__main__":
    unittest.main()
