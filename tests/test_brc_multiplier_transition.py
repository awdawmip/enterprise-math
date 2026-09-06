from __future__ import annotations

import hashlib
import random
import unittest

from enterprise_math.brc_multiplier_transition import (
    initial_multiplier_root_state,
    multiplier_root_state_sequence,
    next_multiplier_root_state,
    static_transition_payload_bytes,
    transition_table_mode,
)
from enterprise_math.brc_multiplier_transition_table import (
    MAX_STATIC_FRACTION_BITS,
    MAX_STATIC_N_BITS,
    RAW_PAYLOAD_BYTES,
    TABLE_SHA256,
    fraction_bits_for_n_bits,
    high_precision_constants,
    regenerate_high_precision_constants,
    regenerated_payload,
    transition_constants_for_n_bits,
)
from enterprise_math.core import integer_nth_root


class BRCMultiplierTransitionTests(unittest.TestCase):
    def test_static_table_regenerates_exactly(self) -> None:
        self.assertEqual(
            high_precision_constants(), regenerate_high_precision_constants()
        )
        payload = regenerated_payload()
        self.assertEqual(len(payload), RAW_PAYLOAD_BYTES)
        self.assertEqual(hashlib.sha256(payload).hexdigest(), TABLE_SHA256)
        self.assertEqual(static_transition_payload_bytes(), RAW_PAYLOAD_BYTES)

    def test_dyadic_truncation_is_exact(self) -> None:
        high = high_precision_constants()
        for n_bits in (128, 512, 1024, 2048, 4096):
            B, low, mode = transition_constants_for_n_bits(n_bits)
            self.assertEqual(mode, "STATIC")
            shift = MAX_STATIC_FRACTION_BITS - B
            self.assertEqual(low, tuple(value >> shift for value in high))
            self.assertEqual(B, fraction_bits_for_n_bits(n_bits))

    def test_dynamic_fallback_above_static_cap(self) -> None:
        bits = MAX_STATIC_N_BITS + 1
        _, values, mode = transition_constants_for_n_bits(bits)
        self.assertEqual(mode, "DYNAMIC_CACHED")
        self.assertEqual(len(values), 99)

    def test_exhaustive_small_equivalence_and_two_correction_bound(self) -> None:
        for n in range(1, 500):
            states = multiplier_root_state_sequence(n, 100)
            for m, state in enumerate(states, 1):
                root = integer_nth_root(m * n, 2)
                self.assertEqual(state.root, root)
                self.assertEqual(state.remainder, m * n - root * root)
                self.assertLessEqual(state.correction_steps, 2)

    def test_random_big_equivalence(self) -> None:
        rng = random.Random(20260906)
        for bits in (128, 256, 512, 1024, 2048, 4096, 8192):
            for _ in range(2):
                n = rng.getrandbits(bits - 1) | (1 << (bits - 1)) | 1
                states = multiplier_root_state_sequence(n, 100)
                for m, state in enumerate(states, 1):
                    root = integer_nth_root(m * n, 2)
                    self.assertEqual(
                        (state.root, state.remainder),
                        (root, m * n - root * root),
                    )
                    self.assertLessEqual(state.correction_steps, 2)

    def test_single_step_matches_sequence(self) -> None:
        n = (1 << 1023) + 987654321
        state = initial_multiplier_root_state(n)
        states = [state]
        for _ in range(99):
            state = next_multiplier_root_state(state)
            states.append(state)
        self.assertEqual(tuple(states), multiplier_root_state_sequence(n, 100))

    def test_ceiling_gap_is_exact(self) -> None:
        n = 10007 * 10009
        for state in multiplier_root_state_sequence(n, 100):
            x = state.root if state.remainder == 0 else state.root + 1
            self.assertEqual(
                state.ceiling_completion_gap,
                x * x - state.multiplier * n,
            )

    def test_mode_boundary(self) -> None:
        self.assertEqual(transition_table_mode(1 << 2047), "STATIC")
        self.assertEqual(transition_table_mode(1 << 4095), "STATIC")
        self.assertEqual(transition_table_mode(1 << 4096), "DYNAMIC_CACHED")


if __name__ == "__main__":
    unittest.main()
