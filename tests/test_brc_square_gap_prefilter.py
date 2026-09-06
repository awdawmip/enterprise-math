from __future__ import annotations

import hashlib
import unittest
from math import isqrt

from enterprise_math.brc_square_gap_prefilter import (
    DEFAULT_SQUARE_RESIDUE_MODULUS,
    STRONG_SQUARE_RESIDUE_MODULUS,
    ceiling_completion_cost,
    ceiling_completion_square_witness,
    filtered_square_root,
    passes_square_residue_filter,
    square_residue_count,
    square_residue_mask,
    square_residue_payload_bytes,
    square_residue_table,
)
from enterprise_math.brc_square_gap_tables import TABLE_SHA256


class BRCSquareGapPrefilterTests(unittest.TestCase):
    def test_reference_table_sizes(self) -> None:
        self.assertEqual(DEFAULT_SQUARE_RESIDUE_MODULUS, 4032)
        self.assertEqual(STRONG_SQUARE_RESIDUE_MODULUS, 20160)
        self.assertEqual(square_residue_count(4032), 192)
        self.assertEqual(square_residue_count(20160), 576)
        self.assertEqual(square_residue_payload_bytes(4032), 504)
        self.assertEqual(square_residue_payload_bytes(20160), 2520)

    def test_static_tables_match_fresh_generation(self) -> None:
        for modulus in (4032, 20160):
            expected = bytearray((modulus + 7) // 8)
            for value in range(modulus):
                residue = (value * value) % modulus
                expected[residue >> 3] |= 1 << (residue & 7)
            actual = square_residue_table(modulus)
            self.assertEqual(actual, bytes(expected))
            self.assertEqual(
                hashlib.sha256(actual).hexdigest(),
                TABLE_SHA256[modulus],
            )
            self.assertEqual(
                square_residue_mask(modulus),
                int.from_bytes(actual, "little"),
            )

    def test_arbitrary_modulus_fallback(self) -> None:
        modulus = 77
        table = square_residue_table(modulus)
        self.assertEqual(len(table), (modulus + 7) // 8)
        for root in range(200):
            self.assertTrue(passes_square_residue_filter(root * root, modulus))

    def test_no_false_negatives_for_squares(self) -> None:
        for root in range(0, 3000):
            value = root * root
            for modulus in (4032, 20160):
                self.assertTrue(passes_square_residue_filter(value, modulus))
                self.assertEqual(filtered_square_root(value, modulus), root)

    def test_filtered_square_root_matches_exact_test(self) -> None:
        for value in range(0, 20000):
            root = isqrt(value)
            expected = root if root * root == value else None
            self.assertEqual(filtered_square_root(value, 4032), expected)
            self.assertEqual(filtered_square_root(value, 20160), expected)

    def test_ceiling_completion_boundary(self) -> None:
        # Exact square: Fermat completion is zero, unlike BRC next-square cost.
        self.assertEqual(ceiling_completion_cost(9, 1), (3, 0))
        self.assertEqual(ceiling_completion_cost(14, 1), (4, 2))
        self.assertEqual(ceiling_completion_cost(15, 1), (4, 1))

    def test_immediate_difference_of_squares_witness(self) -> None:
        self.assertEqual(ceiling_completion_square_witness(15, 1), (4, 1))
        self.assertIsNone(ceiling_completion_square_witness(14, 1))
        self.assertEqual(
            ceiling_completion_square_witness(
                15, 1, STRONG_SQUARE_RESIDUE_MODULUS
            ),
            (4, 1),
        )


if __name__ == "__main__":
    unittest.main()
