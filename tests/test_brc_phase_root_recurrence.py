from __future__ import annotations

from math import isqrt
import random
from unittest.mock import patch

from enterprise_math.brc_linear_deep_tail import (
    common_mod8_linear_tail_threshold,
    odd_n_multiplier_is_representative,
)
from enterprise_math.brc_phase_quotient_remainder import RECIPROCAL_RAW_BYTES
from enterprise_math.brc_phase_root_recurrence import (
    PHASE_SEED_TRANSITIONS,
    PHASE_THIRD_DIFFERENCE_MAX,
    PHASE_THIRD_DIFFERENCE_MIN,
    PhaseRootRemainderTracker,
    odd_n_phase_root_tail_states,
    phase_root_candidate_gap,
    phase_root_third_difference_bounds,
    reused_reciprocal_table_bytes,
)


def _align_representative(multiplier: int) -> int:
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def _start(n: int) -> int:
    return _align_representative(common_mod8_linear_tail_threshold(n))


def _direct_state(n: int, multiplier: int) -> tuple[int, int]:
    root = isqrt(n * multiplier)
    return root, n * multiplier - root * root


def test_phase_candidate_gap_identity_exhaustive() -> None:
    for n in range(1, 500, 2):
        start = _start(n)
        for residue_offset in range(8):
            m0 = start + residue_offset
            if not odd_n_multiplier_is_representative(m0):
                continue
            states = [_direct_state(n, m0 + 8 * i) for i in range(4)]
            candidate, gap = phase_root_candidate_gap(
                states[0][0],
                states[0][1],
                states[1][0],
                states[1][1],
                states[2][0],
                states[2][1],
            )
            assert gap == (m0 + 24) * n - candidate * candidate
            correction = states[3][0] - candidate
            assert PHASE_THIRD_DIFFERENCE_MIN <= correction <= PHASE_THIRD_DIFFERENCE_MAX


def test_small_tail_streams_match_direct_roots() -> None:
    for n in range(1, 700, 2):
        states = odd_n_phase_root_tail_states(n, _start(n), 120)
        for state in states:
            root, remainder = _direct_state(n, state.multiplier)
            assert (state.root, state.remainder) == (root, remainder)


def test_random_large_tail_streams_match_direct_roots() -> None:
    for bits in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
        rng = random.Random(20260907 + bits)
        for _ in range(4):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            tracker = PhaseRootRemainderTracker(n, _start(n))
            for _ in range(260):
                state = tracker.advance()
                root, remainder = _direct_state(n, state.multiplier)
                assert (state.root, state.remainder) == (root, remainder)
                if state.mode == "PHASE_RECURRENCE":
                    assert (
                        PHASE_THIRD_DIFFERENCE_MIN
                        <= state.phase_correction
                        <= PHASE_THIRD_DIFFERENCE_MAX
                    )


def test_exactly_fourteen_seed_divisions_then_phase_only() -> None:
    n = (1 << 1023) + 0x123456789ABCDEF
    tracker = PhaseRootRemainderTracker(n, _start(n))
    modes = []
    for _ in range(200):
        modes.append(tracker.advance().mode)
    assert tracker.seed_divisions == PHASE_SEED_TRANSITIONS == 14
    assert modes.count("SEED_ORDER1") == 14
    assert tracker.recurrent_transitions == 200 - 14
    assert all(mode == "PHASE_RECURRENCE" for mode in modes[14:])


def test_only_initial_target_root_is_materialized() -> None:
    n = (1 << 2047) + 0xF00DCAFE12345
    start = _start(n)
    calls = 0

    def counted_isqrt(value: int) -> int:
        nonlocal calls
        calls += 1
        return isqrt(value)

    with patch(
        "enterprise_math.brc_phase_root_recurrence.isqrt",
        side_effect=counted_isqrt,
    ):
        tracker = PhaseRootRemainderTracker(n, start)
        for _ in range(300):
            tracker.advance()
    assert calls == 1


def test_reuses_existing_one_kibibyte_reciprocal_table() -> None:
    assert reused_reciprocal_table_bytes() == RECIPROCAL_RAW_BYTES == 1024


def test_stream_is_unbounded_beyond_old_multiplier_horizon() -> None:
    n = 1_000_003 * 1_000_033
    tracker = PhaseRootRemainderTracker(n, _start(n))
    while tracker.multiplier <= 10_000:
        tracker.advance()
    root, remainder = _direct_state(n, tracker.multiplier)
    assert (tracker.root, tracker.remainder) == (root, remainder)


def test_declared_bounds_are_stable() -> None:
    assert phase_root_third_difference_bounds() == (-3, 387)
