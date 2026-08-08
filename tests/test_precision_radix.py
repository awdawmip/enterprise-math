import unittest

from enterprise_math.precision_radix import (
    additive_diamond_flat,
    braid_left,
    braid_right,
    direct_carry,
    join_detail,
    radix_swap,
    split_detail,
    staged_carry,
)


class PrecisionRadixTests(unittest.TestCase):
    def test_mixed_radix_split_join_are_inverse(self):
        for r in range(1, 8):
            for s in range(1, 8):
                for value in range(r * s):
                    digits = split_detail(value, r, s)
                    self.assertEqual(join_detail(*digits, r, s), value)

    def test_radix_swap_is_involutive_with_swapped_parameters(self):
        for r in range(1, 8):
            for s in range(1, 8):
                for u in range(r):
                    for v in range(s):
                        swapped = radix_swap(u, v, r, s)
                        self.assertEqual(radix_swap(*swapped, s, r), (u, v))

    def test_adjacent_radix_swaps_satisfy_braid_coherence(self):
        for r in range(1, 6):
            for s in range(1, 6):
                for t in range(1, 6):
                    for a in range(r):
                        for b in range(s):
                            for c in range(t):
                                self.assertEqual(
                                    braid_left(r, s, t, a, b, c),
                                    braid_right(r, s, t, a, b, c),
                                )

    def test_staged_carry_equals_direct_product_radix_carry(self):
        for r in range(1, 9):
            for s in range(1, 9):
                total = r * s
                for first in range(total):
                    for second in range(total):
                        direct = direct_carry(total, first, second)
                        self.assertEqual(staged_carry(r, s, first, second), direct)
                        self.assertEqual(staged_carry(s, r, first, second), direct)
                        self.assertTrue(additive_diamond_flat(r, s, first, second))


if __name__ == "__main__":
    unittest.main()
