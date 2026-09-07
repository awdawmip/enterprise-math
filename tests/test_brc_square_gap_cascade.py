from fractions import Fraction
from math import isqrt
import unittest

from enterprise_math.brc_square_gap_cascade import (
    cascade_profile_stats,
    cascade_raw_table_bytes,
    cascade_survival_density,
    cascade_table,
    filtered_square_root_cascade,
    passes_square_residue_cascade,
    square_residue_count_for_stage,
)


class BRCSquareGapCascadeTests(unittest.TestCase):
    def test_stage_sizes_and_counts(self):
        self.assertEqual(len(cascade_table(4032)), 504)
        self.assertEqual(len(cascade_table(12155)), 1520)
        self.assertEqual(len(cascade_table(12673)), 1585)
        self.assertEqual(square_residue_count_for_stage(4032), 192)
        self.assertEqual(square_residue_count_for_stage(12155), 1134)
        self.assertEqual(square_residue_count_for_stage(12673), 1800)

    def test_exact_profile_storage(self):
        self.assertEqual(cascade_raw_table_bytes("BASE"), 504)
        self.assertEqual(cascade_raw_table_bytes("COMPACT"), 2024)
        self.assertEqual(cascade_raw_table_bytes("BALANCED"), 3609)

    def test_exact_crt_densities(self):
        self.assertEqual(cascade_survival_density("BASE"), Fraction(1, 21))
        self.assertEqual(cascade_survival_density("COMPACT"), Fraction(54, 12155))
        self.assertEqual(
            cascade_survival_density("BALANCED"), Fraction(19440, 30808063)
        )

    def test_no_false_negative_for_squares(self):
        for root in range(20000):
            square = root * root
            self.assertTrue(passes_square_residue_cascade(square, "BASE"))
            self.assertTrue(passes_square_residue_cascade(square, "COMPACT"))
            self.assertTrue(passes_square_residue_cascade(square, "BALANCED"))

    def test_filtered_square_root_is_exact(self):
        for value in range(10000):
            root = isqrt(value)
            expected = root if root * root == value else None
            self.assertEqual(filtered_square_root_cascade(value), expected)

    def test_profile_stats(self):
        stats = cascade_profile_stats("balanced")
        self.assertEqual(stats.profile, "BALANCED")
        self.assertEqual(stats.moduli, (4032, 12155, 12673))
        self.assertEqual(stats.raw_table_bytes, 3609)
        self.assertEqual(stats.survival_density, Fraction(19440, 30808063))
        self.assertEqual(stats.rejection_density, 1 - stats.survival_density)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            passes_square_residue_cascade(-1)
        with self.assertRaises(ValueError):
            passes_square_residue_cascade(4, "missing")
        with self.assertRaises(ValueError):
            cascade_table(17)


if __name__ == "__main__":
    unittest.main()
