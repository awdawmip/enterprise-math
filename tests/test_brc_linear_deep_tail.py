from __future__ import annotations

from math import isqrt
import random

from enterprise_math.brc_linear_deep_tail import (
    common_mod8_linear_tail_sufficient,
    common_mod8_linear_tail_threshold,
    linear_tail_sufficient,
    linear_tail_threshold,
    next_odd_n_representative_multiplier,
    odd_n_linear_deep_tail_states,
    odd_n_multiplier_is_representative,
    order1_pell_pair,
    order1_two_correction_certificate,
    transport_order1_linear_tail,
)


def _align_representative(multiplier: int) -> int:
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def test_order1_pell_identity_grid() -> None:
    for m in range(1, 200):
        for h in (1, 2):
            a, b = order1_pell_pair(m, h)
            assert a - b == 2 * h
            assert (m + h) * b * b - m * a * a == h**3
            assert a > b > 0


def test_thresholds_are_minimal_for_declared_sufficient_bounds() -> None:
    values = (1, 3, 17, 10**12 + 39, (1 << 511) + 12345)
    for n in values:
        common = common_mod8_linear_tail_threshold(n)
        assert common_mod8_linear_tail_sufficient(n, common)
        if common > 1:
            assert not common_mod8_linear_tail_sufficient(n, common - 1)

        for h in (1, 2):
            threshold = linear_tail_threshold(n, h)
            assert linear_tail_sufficient(n, threshold, h)
            if threshold > 1:
                assert not linear_tail_sufficient(n, threshold - 1, h)


def test_h1_tail_starts_no_later_than_common_h2_tail() -> None:
    for bits in (64, 128, 256, 512, 1024):
        n = (1 << (bits - 1)) + 12345
        assert linear_tail_threshold(n, 1) <= common_mod8_linear_tail_threshold(n)
        assert linear_tail_threshold(n, 2) == common_mod8_linear_tail_threshold(n)


def test_exhaustive_small_odd_tail_matches_direct_roots() -> None:
    for n in range(1, 300, 2):
        start = _align_representative(common_mod8_linear_tail_threshold(n))
        states = odd_n_linear_deep_tail_states(n, start, 40)
        for state in states:
            root = isqrt(state.multiplier * n)
            assert state.root == root
            assert state.remainder == state.multiplier * n - root * root
            assert 0 <= state.correction_steps <= 2


def test_random_large_tail_matches_direct_roots() -> None:
    rng = random.Random(20260907)
    for bits in (128, 256, 512, 1024, 2048, 4096, 8192):
        for _ in range(8):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            start = _align_representative(common_mod8_linear_tail_threshold(n))
            states = odd_n_linear_deep_tail_states(n, start, 80)
            for state in states:
                root = isqrt(state.multiplier * n)
                assert (state.root, state.remainder) == (
                    root,
                    state.multiplier * n - root * root,
                )
                assert state.correction_steps <= 2


def test_general_exact_certificate_entrypoint() -> None:
    n = (1 << 521) + 987654321
    m = linear_tail_threshold(n, 1)
    target = m * n
    root = isqrt(target)

    class Source:
        pass

    source = Source()
    source.n = n
    source.multiplier = m
    source.root = root
    source.remainder = target - root * root

    assert order1_two_correction_certificate(root, m, 1)
    state = transport_order1_linear_tail(source, m + 1)
    direct = isqrt((m + 1) * n)
    assert state.root == direct
    assert state.remainder == (m + 1) * n - direct * direct
    assert state.correction_steps <= 2


def test_stream_is_not_bounded_by_old_multiplier_100_surface() -> None:
    n = (1 << 1023) + 42424243
    start = _align_representative(max(10_001, common_mod8_linear_tail_threshold(n)))
    states = odd_n_linear_deep_tail_states(n, start, 200)
    assert states[0].multiplier >= 10_001
    assert states[-1].multiplier > states[0].multiplier
    assert all(odd_n_multiplier_is_representative(s.multiplier) for s in states)


def test_representative_gaps_are_only_one_or_two() -> None:
    m = 1
    for _ in range(500):
        nxt = next_odd_n_representative_multiplier(m)
        assert nxt - m in (1, 2)
        assert odd_n_multiplier_is_representative(nxt)
        m = nxt
