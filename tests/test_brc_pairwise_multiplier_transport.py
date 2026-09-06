from __future__ import annotations

import random
import unittest
from math import isqrt
from types import SimpleNamespace
from unittest.mock import patch

from enterprise_math.brc_multiplier_priority_jump import prioritized_odd_multiplier_order
from enterprise_math.brc_multiplier_transition import initial_multiplier_root_state
from enterprise_math.brc_pairwise_multiplier_transport import (
    pairwise_correction_bound,
    pairwise_multiplier_order_states,
    pairwise_prioritized_odd_multiplier_states,
    transport_multiplier_root_state,
)


class BRCPairwiseMultiplierTransportTests(unittest.TestCase):
    def test_bound_examples(self) -> None:
        self.assertEqual(pairwise_correction_bound(7, 7), 0)
        self.assertLessEqual(pairwise_correction_bound(96, 45), 2)
        self.assertEqual(pairwise_correction_bound(1, 100), 11)

    def test_exhaustive_small_all_pairs(self) -> None:
        order = prioritized_odd_multiplier_order(100)
        for n in range(1, 160, 2):
            for source_m in order:
                source_root = isqrt(source_m * n)
                source = SimpleNamespace(
                    n=n,
                    multiplier=source_m,
                    root=source_root,
                    remainder=source_m * n - source_root * source_root,
                )
                for target_m in order:
                    state = transport_multiplier_root_state(source, target_m)
                    root = isqrt(target_m * n)
                    self.assertEqual(
                        (state.root, state.remainder),
                        (root, target_m * n - root * root),
                    )
                    self.assertLessEqual(
                        state.correction_steps,
                        pairwise_correction_bound(source_m, target_m),
                    )
                    if target_m < source_m:
                        self.assertLessEqual(state.correction_steps, 2)

    def test_random_large_bidirectional_pairs(self) -> None:
        rng = random.Random(20260907)
        order = prioritized_odd_multiplier_order(100)
        for bits in (128, 256, 512, 1024, 2048, 4096, 8192):
            for _ in range(10):
                n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                source_m = rng.choice(order)
                target_m = rng.choice(order)
                source_root = isqrt(source_m * n)
                source = SimpleNamespace(
                    n=n,
                    multiplier=source_m,
                    root=source_root,
                    remainder=source_m * n - source_root * source_root,
                )
                state = transport_multiplier_root_state(source, target_m)
                target_root = isqrt(target_m * n)
                self.assertEqual(
                    (state.root, state.remainder),
                    (target_root, target_m * n - target_root * target_root),
                )

    def test_priority_sequence_exact(self) -> None:
        for n in (15, 527, 6437, 39973, 123456789123456789):
            order = prioritized_odd_multiplier_order(100)
            states = pairwise_prioritized_odd_multiplier_states(n)
            self.assertEqual(tuple(state.multiplier for state in states), order)
            for state in states:
                root = isqrt(state.multiplier * n)
                self.assertEqual(
                    (state.root, state.remainder),
                    (root, state.multiplier * n - root * root),
                )

    def test_initial_root_materialized_once(self) -> None:
        # Production invariant: one N-dependent root for a complete priority stream.
        from enterprise_math import brc_pairwise_multiplier_transport as module

        original = initial_multiplier_root_state
        calls = 0

        def counted(n: int):
            nonlocal calls
            calls += 1
            return original(n)

        with patch.object(module, "initial_multiplier_root_state", counted):
            states = pairwise_multiplier_order_states(
                1009 * 1013,
                prioritized_odd_multiplier_order(100),
            )
        self.assertEqual(len(states), 62)
        self.assertEqual(calls, 1)


if __name__ == "__main__":
    unittest.main()
