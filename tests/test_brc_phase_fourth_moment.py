from __future__ import annotations

from math import isqrt
import random
from unittest.mock import patch

from enterprise_math.brc_linear_deep_tail import (
    common_mod8_linear_tail_threshold,
    odd_n_multiplier_is_representative,
)
from enterprise_math.brc_phase_fourth_moment import (
    FOURTH_PHASE_TAIL_FACTOR,
    PHASE_FOURTH_DIFFERENCE_MAX,
    PHASE_FOURTH_DIFFERENCE_MIN,
    PHASE_SEED_TRANSITIONS,
    FourthPhaseMomentTracker,
    aligned_fourth_phase_tail_threshold,
    fourth_phase_tail_sufficient,
    fourth_phase_tail_threshold,
    odd_n_fourth_phase_tail_states,
    phase_fourth_candidate_gap,
    phase_fourth_difference_bounds,
    reused_reciprocal_table_bytes,
)
from enterprise_math.brc_phase_quotient_remainder import RECIPROCAL_RAW_BYTES


def _direct_state(n: int, multiplier: int) -> tuple[int, int]:
    root = isqrt(n * multiplier)
    return root, n * multiplier - root * root


def test_seventh_root_threshold_is_minimal() -> None:
    for n in list(range(1, 1000, 2)) + [(1 << bits) + 3 for bits in (64, 256, 1024)]:
        threshold = fourth_phase_tail_threshold(n)
        assert threshold**7 >= FOURTH_PHASE_TAIL_FACTOR * n
        if threshold > 1:
            assert (threshold - 1) ** 7 < FOURTH_PHASE_TAIL_FACTOR * n
        aligned = aligned_fourth_phase_tail_threshold(n)
        assert odd_n_multiplier_is_representative(aligned)
        assert fourth_phase_tail_sufficient(n, aligned)


def test_candidate_gap_identity_and_bound_exhaustive() -> None:
    for n in range(1, 600, 2):
        start = aligned_fourth_phase_tail_threshold(n)
        for offset in range(8):
            m0 = start + offset
            if not odd_n_multiplier_is_representative(m0):
                continue
            states = [_direct_state(n, m0 + 8 * i) for i in range(5)]
            candidate, gap = phase_fourth_candidate_gap(
                states[0][0],
                states[0][1],
                states[1][0],
                states[1][1],
                states[2][0],
                states[2][1],
                states[3][0],
                states[3][1],
            )
            assert gap == (m0 + 32) * n - candidate * candidate
            correction = states[4][0] - candidate
            assert PHASE_FOURTH_DIFFERENCE_MIN <= correction <= PHASE_FOURTH_DIFFERENCE_MAX


def test_small_streams_match_direct_roots() -> None:
    for n in range(1, 800, 2):
        states = odd_n_fourth_phase_tail_states(n, None, 140)
        for state in states:
            assert (state.root, state.remainder) == _direct_state(n, state.multiplier)


def test_random_large_streams_match_direct_roots() -> None:
    for bits in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
        rng = random.Random(2026090715 + bits)
        for _ in range(4):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            tracker = FourthPhaseMomentTracker(n)
            for _ in range(320):
                state = tracker.advance()
                assert (state.root, state.remainder) == _direct_state(
                    n,
                    state.multiplier,
                )
                if state.mode == "FOURTH_PHASE_RECURRENCE":
                    assert (
                        PHASE_FOURTH_DIFFERENCE_MIN
                        <= state.phase_correction
                        <= PHASE_FOURTH_DIFFERENCE_MAX
                    )


def test_exactly_nineteen_seed_roots_then_recurrence_only() -> None:
    n = (1 << 2047) + 0x123456789ABCDEF
    tracker = FourthPhaseMomentTracker(n)
    modes = [tracker.advance().mode for _ in range(300)]
    assert tracker.seed_root_calls == PHASE_SEED_TRANSITIONS == 19
    assert modes.count("SEED_DIRECT_ROOT") == 19
    assert tracker.recurrent_transitions == 300 - 19
    assert all(mode == "FOURTH_PHASE_RECURRENCE" for mode in modes[19:])


def test_only_twenty_total_target_roots_are_materialized() -> None:
    n = (1 << 4095) + 0xF00DCAFE12345
    calls = 0

    def counted_isqrt(value: int) -> int:
        nonlocal calls
        calls += 1
        return isqrt(value)

    with patch(
        "enterprise_math.brc_phase_fourth_moment.isqrt",
        side_effect=counted_isqrt,
    ):
        tracker = FourthPhaseMomentTracker(n)
        for _ in range(500):
            tracker.advance()
    assert calls == 1 + PHASE_SEED_TRANSITIONS == 20


def test_fourth_order_tail_begins_before_order_one_tail_for_large_n() -> None:
    for bits in (512, 1024, 2048, 4096):
        n = (1 << (bits - 1)) + 1
        fourth = aligned_fourth_phase_tail_threshold(n)
        linear = common_mod8_linear_tail_threshold(n)
        assert fourth < linear


def test_reuses_existing_reciprocal_table_without_new_payload() -> None:
    assert reused_reciprocal_table_bytes() == RECIPROCAL_RAW_BYTES == 1024


def test_unbounded_stream_passes_multiplier_10000() -> None:
    n = 1_000_003 * 1_000_033
    tracker = FourthPhaseMomentTracker(n)
    while tracker.multiplier <= 10_000:
        tracker.advance_pair()
    assert (tracker.root, tracker.remainder) == _direct_state(n, tracker.multiplier)


def test_declared_bounds_are_stable() -> None:
    assert phase_fourth_difference_bounds() == (-347, 7)
