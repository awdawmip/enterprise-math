from __future__ import annotations

import unittest
from math import isqrt

from enterprise_math.brc_multiplier_factor_scan import (
    admissible_root_state_sequence,
)
from enterprise_math.brc_multiplier_vertical_wheel import (
    ADAPTIVE_WHEEL_THRESHOLD,
    LONG_WHEEL_MODULUS,
    SHORT_WHEEL_MODULUS,
    adaptive_first_wheel_modulus,
    first_vertical_factor_witness,
    vertical_gap_at,
    vertical_next_gap,
    vertical_residue_wheel,
    vertical_square_candidates,
    vertical_state_from_multiplier_state,
)
from enterprise_math.brc_square_gap_prefilter import square_residue_table
from enterprise_math.brc_square_gap_table_46189 import (
    MODULUS as SECOND_MODULUS,
    SQUARE_RESIDUE_TABLE as SECOND_TABLE,
)


def _contains(table: bytes, modulus: int, value: int) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


class BRCMultiplierVerticalWheelTests(unittest.TestCase):
    def test_vertical_formula_and_recurrence(self) -> None:
        for n in range(3, 150, 2):
            for horizontal in admissible_root_state_sequence(n, 20):
                state = vertical_state_from_multiplier_state(horizontal)
                x = state.base_x
                gap = state.base_gap
                for t in range(50):
                    self.assertEqual(vertical_gap_at(state, t), gap)
                    self.assertEqual(gap, x * x - horizontal.multiplier * n)
                    x, gap = vertical_next_gap(x, gap)

    def test_wheel_periodicity_and_exact_first_stage(self) -> None:
        for n in range(3, 80, 2):
            horizontal = admissible_root_state_sequence(n, 15)[-1]
            state = vertical_state_from_multiplier_state(horizontal)
            for modulus in (1008, 20160):
                wheel = vertical_residue_wheel(state, modulus)
                table = square_residue_table(modulus)
                support = set(wheel.offsets)
                for t in range(min(2 * modulus, 5000)):
                    expected = _contains(table, modulus, vertical_gap_at(state, t))
                    self.assertEqual((t % modulus) in support, expected)

    def test_two_stage_candidate_set_matches_direct_filters(self) -> None:
        first_modulus = 1008
        first_table = square_residue_table(first_modulus)
        for n in range(3, 100, 2):
            for horizontal in admissible_root_state_sequence(n, 15)[::4]:
                state = vertical_state_from_multiplier_state(horizontal)
                actual = {
                    candidate.t
                    for candidate in vertical_square_candidates(
                        state, 1000, first_modulus=first_modulus
                    )
                }
                expected = set()
                for t in range(1000):
                    gap = vertical_gap_at(state, t)
                    if _contains(first_table, first_modulus, gap) and _contains(
                        SECOND_TABLE, SECOND_MODULUS, gap
                    ):
                        expected.add(t)
                self.assertEqual(actual, expected)

    def test_no_false_negative_for_actual_square_gaps(self) -> None:
        for n in range(3, 120, 2):
            horizontal = admissible_root_state_sequence(n, 20)[-1]
            state = vertical_state_from_multiplier_state(horizontal)
            candidates = {
                candidate.t
                for candidate in vertical_square_candidates(
                    state, 1200, first_modulus=1008
                )
            }
            for t in range(1200):
                gap = vertical_gap_at(state, t)
                root = isqrt(gap)
                if root * root == gap:
                    self.assertIn(t, candidates)

    def test_known_vertical_factor_hit(self) -> None:
        # 5959=59*101. Fermat center x=80; ceil(sqrt(N))=78, so t=2.
        horizontal = admissible_root_state_sequence(5959, 1)[0]
        state = vertical_state_from_multiplier_state(horizontal)
        factor, t = first_vertical_factor_witness(
            state, 20, first_modulus=1008
        )
        self.assertEqual(t, 2)
        self.assertIn(factor, (59, 101))

    def test_adaptive_wheel_policy_boundary(self) -> None:
        self.assertEqual(adaptive_first_wheel_modulus(10_000), SHORT_WHEEL_MODULUS)
        self.assertEqual(
            adaptive_first_wheel_modulus(ADAPTIVE_WHEEL_THRESHOLD - 1),
            SHORT_WHEEL_MODULUS,
        )
        self.assertEqual(
            adaptive_first_wheel_modulus(ADAPTIVE_WHEEL_THRESHOLD),
            LONG_WHEEL_MODULUS,
        )
        self.assertEqual(adaptive_first_wheel_modulus(1_000_000), LONG_WHEEL_MODULUS)


if __name__ == "__main__":
    unittest.main()
