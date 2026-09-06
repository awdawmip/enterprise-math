from __future__ import annotations

import unittest
from math import isqrt

from enterprise_math.brc_square_gap_prefilter import (
    DEFAULT_SQUARE_RESIDUE_MODULUS,
    ceiling_completion_cost,
    ceiling_completion_square_witness,
    filtered_square_root,
    passes_square_residue_filter,
    square_residue_count,
)


class BRCSquareGapPrefilterTests(unittest.TestCase):
    def test_reference_table_sizes(self) -> None:
        self.assertEqual(DEFAULT_SQUARE_RESIDUE_MODULUS, 4032)
        self.assertEqual(square_residue_count(4032), 192)
        self.assertEqual(square_residue_count(20160), 576)

    def test_no_false_negatives_for_squares(self) -> None:
        for root in range(0, 1000):
            value = root * root
            self.assertTrue(passes_square_residue_filter(value, 4032))
            self.assertEqual(filtered_square_root(value, 4032), root)

    def test_filtered_square_root_matches_exact_test(self) -> None:
        for value in range(0, 20000):
            root = isqrt(value)
            expected = root if root * root == value else None
            self.assertEqual(filtered_square_root(value, 4032), expected)

    def test_ceiling_completion_boundary(self) -> None:
        # Exact square: Fermat completion is zero, unlike BRC next-square cost.
        self.assertEqual(ceiling_completion_cost(9, 1), (3, 0))
        self.assertEqual(ceiling_completion_cost(14, 1), (4, 2))
        self.assertEqual(ceiling_completion_cost(15, 1), (4, 1))

    def test_immediate_difference_of_squares_witness(self) -> None:
        self.assertEqual(ceiling_completion_square_witness(15, 1), (4, 1))
        self.assertIsNone(ceiling_completion_square_witness(14, 1))


if __name__ == "__main__":
    unittest.main()
