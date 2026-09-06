from __future__ import annotations

import hashlib
import random
import unittest
from math import isqrt

from enterprise_math.brc_multiplier_factor_scan import (
    STRONG_CASCADE_UNIFORM_PASS_FRACTION,
    admissible_multipliers,
    admissible_root_state_sequence,
    first_immediate_factor_witness,
    heuristic_priority_multipliers,
    odd_multiplier_admissible,
    strong_cascade_passes_squarehood,
)
from enterprise_math.brc_multiplier_transition_jump2_table import (
    RAW_PAYLOAD_BYTES,
    TABLE_SHA256,
    regenerated_payload,
)
from enterprise_math.brc_square_gap_table_46189 import (
    QUADRATIC_RESIDUE_CLASSES,
    RAW_PAYLOAD_BYTES as RESIDUE_PAYLOAD_BYTES,
    SQUARE_RESIDUE_TABLE,
    TABLE_SHA256 as RESIDUE_SHA256,
)


class BRCAdmissibleCascadeTests(unittest.TestCase):
    def test_static_payload_integrity(self) -> None:
        payload = regenerated_payload()
        self.assertEqual(len(payload), RAW_PAYLOAD_BYTES)
        self.assertEqual(hashlib.sha256(payload).hexdigest(), TABLE_SHA256)
        self.assertEqual(len(SQUARE_RESIDUE_TABLE), RESIDUE_PAYLOAD_BYTES)
        self.assertEqual(sum(byte.bit_count() for byte in SQUARE_RESIDUE_TABLE), 3780)
        self.assertEqual(QUADRATIC_RESIDUE_CLASSES, 3780)
        self.assertEqual(hashlib.sha256(SQUARE_RESIDUE_TABLE).hexdigest(), RESIDUE_SHA256)

    def test_strong_cascade_has_no_square_false_negatives(self) -> None:
        for root in range(5000):
            self.assertTrue(strong_cascade_passes_squarehood(root * root))
        self.assertEqual(
            (STRONG_CASCADE_UNIFORM_PASS_FRACTION.numerator,
             STRONG_CASCADE_UNIFORM_PASS_FRACTION.denominator),
            (108, 46189),
        )

    def test_mod4_admissible_multiplier_set(self) -> None:
        path = admissible_multipliers(100)
        self.assertEqual(len(path), 75)
        self.assertEqual(path[0], 1)
        self.assertEqual(path[-1], 100)
        self.assertTrue(all(m % 4 != 2 for m in path))
        self.assertEqual(sum(not odd_multiplier_admissible(m) for m in range(1, 101)), 25)

    def test_excluded_multiplier_cannot_hit_difference_of_squares(self) -> None:
        for n in range(3, 300, 2):
            for m in range(2, 101, 4):
                target = m * n
                lower = isqrt(target)
                x = lower if lower * lower == target else lower + 1
                gap = x * x - target
                b = isqrt(gap)
                self.assertNotEqual(b * b, gap)

    def test_admissible_transport_matches_direct_roots_exhaustively(self) -> None:
        for n in range(1, 500, 2):
            states = admissible_root_state_sequence(n)
            self.assertEqual(len(states), 75)
            for state in states:
                direct = isqrt(state.multiplier * n)
                self.assertEqual(state.root, direct)
                self.assertEqual(state.remainder, state.multiplier * n - direct * direct)
                self.assertLessEqual(state.correction_steps, 3)

    def test_admissible_transport_matches_big_integer_roots(self) -> None:
        rng = random.Random(20260906)
        for bits in (128, 256, 512, 1024, 2048, 4096):
            for _ in range(8):
                n = rng.getrandbits(bits - 1) | (1 << (bits - 1)) | 1
                for state in admissible_root_state_sequence(n):
                    direct = isqrt(state.multiplier * n)
                    self.assertEqual(
                        (state.root, state.remainder),
                        (direct, state.multiplier * n - direct * direct),
                    )

    def test_factor_witness_and_priority_order(self) -> None:
        self.assertEqual(first_immediate_factor_witness(15), (3, 1))
        order = heuristic_priority_multipliers()
        self.assertEqual(order[:10], (1, 96, 45, 48, 63, 72, 75, 15, 80, 99))
        self.assertEqual(set(order), set(admissible_multipliers()))
        self.assertEqual(len(order), len(set(order)))


if __name__ == "__main__":
    unittest.main()
