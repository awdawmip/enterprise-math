from __future__ import annotations

import random
import unittest
from math import isqrt

from enterprise_math.brc_multiplier_factor_scan import (
    AdmissibleMultiplierRootState,
    admissible_multipliers,
    heuristic_priority_multipliers,
)
from enterprise_math.brc_multiplier_priority_vertical import (
    first_ascending_vertical_factor_witness,
    first_priority_vertical_factor_witness,
    priority_ordered_multiplier_states,
    remainder_aware_multiplier_jump,
)


class BRCPriorityVerticalTests(unittest.TestCase):
    def _state(self, n: int, multiplier: int) -> AdmissibleMultiplierRootState:
        root = isqrt(n * multiplier)
        return AdmissibleMultiplierRootState(
            n=n,
            multiplier=multiplier,
            root=root,
            remainder=n * multiplier - root * root,
            correction_steps=0,
        )

    def test_priority_state_permutation_preserves_support(self) -> None:
        states = priority_ordered_multiplier_states(14111)
        self.assertEqual(
            tuple(state.multiplier for state in states),
            heuristic_priority_multipliers(),
        )
        self.assertEqual(
            set(state.multiplier for state in states),
            set(admissible_multipliers()),
        )
        for state in states:
            self.assertEqual(
                state.root * state.root + state.remainder,
                state.multiplier * state.n,
            )

    def test_priority_known_first_hit(self) -> None:
        # N=103*137.  At t=0 the ascending admissible order first hits m=35
        # (rank 26), while the current static priority reaches m=48 at rank 4.
        n = 103 * 137
        priority = first_priority_vertical_factor_witness(n, 1)
        ascending = first_ascending_vertical_factor_witness(n, 1)
        self.assertIsNotNone(priority)
        self.assertIsNotNone(ascending)
        assert priority is not None and ascending is not None
        self.assertIn(priority.factor, (103, 137))
        self.assertEqual((priority.multiplier, priority.vertical_offset, priority.priority_rank), (48, 0, 4))
        self.assertEqual((ascending.multiplier, ascending.vertical_offset, ascending.priority_rank), (35, 0, 26))

    def test_remainder_aware_jump_exhaustive_small(self) -> None:
        for n in range(1, 80):
            for source in range(1, 21):
                state = self._state(n, source)
                for target in range(1, 21):
                    cert = remainder_aware_multiplier_jump(state, target)
                    expected = isqrt(n * target)
                    self.assertEqual(cert.target_root, expected)
                    self.assertEqual(cert.target_remainder, n * target - expected * expected)
                    self.assertLessEqual(cert.correction_steps, 1)

    def test_remainder_aware_jump_random_large(self) -> None:
        rng = random.Random(20260906)
        for bits in (128, 512, 1024, 2048, 4096):
            for _ in range(20):
                n = rng.getrandbits(bits - 1) | (1 << (bits - 1)) | 1
                source = rng.randint(1, 100)
                target = rng.randint(1, 100)
                cert = remainder_aware_multiplier_jump(
                    self._state(n, source),
                    target,
                )
                expected = isqrt(n * target)
                self.assertEqual(cert.target_root, expected)
                self.assertEqual(cert.target_remainder, n * target - expected * expected)
                self.assertLessEqual(cert.correction_steps, 1)

    def test_priority_and_ascending_have_same_bounded_existence(self) -> None:
        # Order may change the first witness, never the searched rectangle.
        for p, q in ((103, 137), (109, 181), (127, 251), (149, 331)):
            n = p * q
            for t_limit in (1, 4, 16):
                a = first_ascending_vertical_factor_witness(n, t_limit)
                b = first_priority_vertical_factor_witness(n, t_limit)
                self.assertEqual(a is None, b is None)


if __name__ == "__main__":
    unittest.main()
