from __future__ import annotations

import random
import unittest
from math import isqrt

from enterprise_math.brc_multiplier_priority_jump import (
    admissible_same_parity_factor_pair_count,
    direct_multiplier_jump_from_one,
    odd_n_multiplier_is_difference_square_feasible,
    prioritized_odd_multiplier_order,
)


class BRCMultiplierPriorityJumpTests(unittest.TestCase):
    def test_mod4_skip_rule(self) -> None:
        for m in range(1, 101):
            self.assertEqual(
                odd_n_multiplier_is_difference_square_feasible(m),
                m % 4 != 2,
            )
        self.assertEqual(
            sum(1 for m in range(1, 101) if not odd_n_multiplier_is_difference_square_feasible(m)),
            25,
        )

    def test_admissible_pair_count_examples(self) -> None:
        self.assertEqual(admissible_same_parity_factor_pair_count(1), 1)
        self.assertEqual(admissible_same_parity_factor_pair_count(45), 3)
        self.assertEqual(admissible_same_parity_factor_pair_count(96), 4)
        self.assertEqual(admissible_same_parity_factor_pair_count(6), 0)

    def test_priority_order_is_exact_feasible_set(self) -> None:
        order = prioritized_odd_multiplier_order(100)
        self.assertEqual(order[0], 1)
        self.assertEqual(len(order), 75)
        self.assertEqual(set(order), {m for m in range(1, 101) if m % 4 != 2})
        scores = [admissible_same_parity_factor_pair_count(m) for m in order[1:]]
        self.assertTrue(all(a >= b for a, b in zip(scores, scores[1:])))

    def test_exhaustive_small_direct_jump(self) -> None:
        for n in range(1, 500, 2):
            for m in range(1, 101):
                state = direct_multiplier_jump_from_one(n, m)
                root = isqrt(m * n)
                self.assertEqual(state.root, root)
                self.assertEqual(state.remainder, m * n - root * root)
                self.assertLessEqual(state.correction_steps, 11)

    def test_random_large_direct_jump(self) -> None:
        rng = random.Random(20260906)
        for bits in (128, 256, 512, 1024, 2048, 4096, 8192):
            for _ in range(12):
                n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                for m in (3, 5, 9, 15, 45, 64, 96, 99, 100):
                    state = direct_multiplier_jump_from_one(n, m)
                    root = isqrt(m * n)
                    self.assertEqual((state.root, state.remainder), (root, m * n - root * root))
                    self.assertLessEqual(state.correction_steps, 11)


if __name__ == "__main__":
    unittest.main()
