from __future__ import annotations

import random
import unittest
from math import isqrt

from enterprise_math.brc_mod8_sparse_transition import (
    compile_two_step_gamma_constants,
    odd_n_sparse_multiplier_root_sequence,
)
from enterprise_math.brc_multiplier_priority_jump import (
    odd_n_multiplier_is_scan_irredundant,
)
from enterprise_math.brc_multiplier_transition_table import (
    transition_constants_for_n_bits,
)


class BRCMod8SparseTransitionTests(unittest.TestCase):
    def test_two_step_compiler_is_lower_bound(self) -> None:
        # The compiled product must never exceed the direct B-bit lower dyadic
        # constant for sqrt((m+2)/m)-1.
        for n_bits in (16, 64, 256, 1024, 4096):
            B, one, _ = transition_constants_for_n_bits(n_bits)
            two = compile_two_step_gamma_constants(B, one)
            scale = 1 << B
            for m, compiled in enumerate(two, start=1):
                direct = isqrt(((m + 2) << (2 * B)) // m) - scale
                self.assertLessEqual(compiled, direct)

    def test_candidate_set_and_steps(self) -> None:
        states = odd_n_sparse_multiplier_root_sequence(101, 100)
        expected = [m for m in range(1, 101) if odd_n_multiplier_is_scan_irredundant(m)]
        self.assertEqual([state.multiplier for state in states], expected)
        self.assertEqual(len(states), 62)
        self.assertTrue(all(state.step_from_previous in (1, 2) for state in states[1:]))

    def test_exhaustive_small_exactness(self) -> None:
        for n in range(1, 500, 2):
            states = odd_n_sparse_multiplier_root_sequence(n, 100)
            for state in states:
                root = isqrt(state.multiplier * n)
                self.assertEqual(state.root, root)
                self.assertEqual(state.remainder, state.multiplier * n - root * root)
                self.assertLessEqual(state.correction_steps, 4)
                if state.step_from_previous == 1:
                    self.assertLessEqual(state.correction_steps, 2)

    def test_random_large_exactness(self) -> None:
        rng = random.Random(20260906)
        for bits in (128, 256, 512, 1024, 2048, 4096, 8192):
            for _ in range(12):
                n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                states = odd_n_sparse_multiplier_root_sequence(n, 100)
                for state in states:
                    root = isqrt(state.multiplier * n)
                    self.assertEqual(
                        (state.root, state.remainder),
                        (root, state.multiplier * n - root * root),
                    )
                    self.assertLessEqual(state.correction_steps, 4)

    def test_two_step_paths_do_not_materialize_removed_middle_state(self) -> None:
        states = odd_n_sparse_multiplier_root_sequence(527, 100)
        by_m = {state.multiplier: state for state in states}
        # 1->3 is a direct two-step transition; m=2 is absent.
        self.assertIn(1, by_m)
        self.assertIn(3, by_m)
        self.assertNotIn(2, by_m)
        self.assertEqual(by_m[3].step_from_previous, 2)
        # 3->5 and 5->7 similarly skip 4 and 6; 7->8 is one step.
        self.assertEqual(by_m[5].step_from_previous, 2)
        self.assertEqual(by_m[7].step_from_previous, 2)
        self.assertEqual(by_m[8].step_from_previous, 1)

    def test_even_n_rejected(self) -> None:
        with self.assertRaises(ValueError):
            odd_n_sparse_multiplier_root_sequence(100, 100)


if __name__ == "__main__":
    unittest.main()
