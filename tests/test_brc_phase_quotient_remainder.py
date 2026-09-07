import math
import random
import unittest

from enterprise_math.brc_linear_deep_tail import (
    common_mod8_linear_tail_threshold,
    next_odd_n_representative_multiplier,
    odd_n_multiplier_is_representative,
)
from enterprise_math.brc_phase_quotient_remainder import (
    PHASE_SECOND_DIFFERENCE_MAX,
    PHASE_SECOND_DIFFERENCE_MIN,
    RECIPROCAL_RAW_BYTES,
    RECIPROCAL_TABLE_ENTRIES,
    PhaseQuotientRemainderTracker,
    phase_second_difference_bounds,
    reciprocal_seed_table,
)


def align_representative(multiplier: int) -> int:
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


class PhaseQuotientRemainderTests(unittest.TestCase):
    def test_reciprocal_table_shape(self) -> None:
        table = reciprocal_seed_table()
        self.assertEqual(len(table), RECIPROCAL_TABLE_ENTRIES)
        self.assertEqual(RECIPROCAL_RAW_BYTES, 1024)
        self.assertTrue(all(0 <= value < 2**16 for value in table))

    def test_declared_second_difference_bounds(self) -> None:
        self.assertEqual(phase_second_difference_bounds(1), (-3, 51))
        self.assertEqual(phase_second_difference_bounds(2), (-3, 99))
        self.assertEqual(PHASE_SECOND_DIFFERENCE_MIN, -3)
        self.assertEqual(PHASE_SECOND_DIFFERENCE_MAX, 99)

    def test_exhaustive_small_tail_second_differences(self) -> None:
        residues = (0, 1, 3, 5, 7)
        for n in range(5, 600, 2):
            start = common_mod8_linear_tail_threshold(n)
            for residue in residues:
                m = start + ((residue - start) % 8)
                h = next_odd_n_representative_multiplier(m) - m
                values = []
                for offset in (0, 8, 16):
                    mm = m + offset
                    root = math.isqrt(mm * n)
                    values.append((2 * h * root) // (4 * mm + h))
                second = values[2] - 2 * values[1] + values[0]
                lower, upper = phase_second_difference_bounds(h)
                self.assertGreaterEqual(second, lower)
                self.assertLessEqual(second, upper)

    def test_tracker_matches_direct_divmod(self) -> None:
        for bits in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
            rng = random.Random(20260907 + bits)
            for _ in range(3):
                n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                m = align_representative(common_mod8_linear_tail_threshold(n))
                tracker = PhaseQuotientRemainderTracker(n)
                for _ in range(400):
                    h = next_odd_n_representative_multiplier(m) - m
                    root = math.isqrt(m * n)
                    result = tracker.divide(root, m, h)
                    expected = divmod(2 * h * root, 4 * m + h)
                    self.assertEqual((result.quotient, result.remainder), expected)
                    m += h

    def test_only_ten_seed_divmods_in_long_stream(self) -> None:
        n = (1 << 1023) + 643
        m = align_representative(common_mod8_linear_tail_threshold(n))
        tracker = PhaseQuotientRemainderTracker(n)
        seed_count = 0
        recurrence_count = 0
        for _ in range(500):
            h = next_odd_n_representative_multiplier(m) - m
            root = math.isqrt(m * n)
            result = tracker.divide(root, m, h)
            if result.mode == "SEED_DIVMOD":
                seed_count += 1
            else:
                recurrence_count += 1
            m += h
        self.assertEqual(seed_count, 10)
        self.assertEqual(recurrence_count, 490)
        self.assertGreater(m, 100)


if __name__ == "__main__":
    unittest.main()
