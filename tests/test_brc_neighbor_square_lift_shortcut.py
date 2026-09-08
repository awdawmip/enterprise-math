from __future__ import annotations

from math import isqrt

from enterprise_math.brc_neighbor_square_lift_shortcut import (
    neighbor_square_parameters,
    power2_neighbor_square_candidates,
    probe_neighbor_square_lift,
    try_power2_neighbor_square_shortcuts,
    valuation_two,
)


def test_valuation_two() -> None:
    assert valuation_two(1) == (0, 1)
    assert valuation_two(96) == (5, 3)
    assert valuation_two(1523712) == (14, 93)


def test_exact_identity_both_signs() -> None:
    for epsilon in (1, -1):
        for a in range(2, 20):
            for t in range(1, 30, 2):
                n = a * a * t + epsilon
                if n <= 1 or n % 2 == 0:
                    continue
                tt, m, z = neighbor_square_parameters(n, a, epsilon)
                assert tt == t
                assert m == 2 * a - epsilon
                assert z == m * t + 1
                assert m * n == a * a * z - (a - epsilon) ** 2


def test_non_square_rejection_changes_nothing() -> None:
    # 33-1=4*8, a=2 gives m=3 and z=25 (a hit), while a different
    # semiprime provides a clean miss.
    probe = probe_neighbor_square_lift(35, 2, -1)
    assert not probe.factor_hit


def test_beyond_horizon_regression_m127() -> None:
    # 18,677,761 = 383 * 48,767 and N-1 = 64^2 * 4560.
    n = 18_677_761
    probe = probe_neighbor_square_lift(n, 64, 1)
    assert probe.multiplier == 127
    assert probe.square_test_value == 761**2
    assert probe.fixed_gap_root == 63
    assert probe.factor_hit
    assert probe.proper_factor in (383, 48_767)


def test_beyond_horizon_regression_m255() -> None:
    # 1,523,713 = 389 * 3917 and N-1 = 128^2 * 93.
    n = 1_523_713
    probe = probe_neighbor_square_lift(n, 128, 1)
    assert probe.multiplier == 255
    assert probe.square_test_value == 154**2
    assert probe.factor_hit
    assert probe.proper_factor in (389, 3917)


def test_beyond_horizon_regression_m511() -> None:
    # 6,094,849 = 761 * 8009 and N-1 = 256^2 * 93.
    n = 6_094_849
    probe = probe_neighbor_square_lift(n, 256, 1)
    assert probe.multiplier == 511
    assert probe.square_test_value == 218**2
    assert probe.factor_hit
    assert probe.proper_factor in (761, 8009)


def test_power2_candidate_trigger_is_beyond_declared_horizon() -> None:
    n = 1_523_713
    candidates = power2_neighbor_square_candidates(
        n, min_multiplier=101, all_levels=False
    )
    assert (1, 128, 255) in candidates
    assert all(m > 100 for _, _, m in candidates)


def test_try_shortcuts_finds_high_v2_witness() -> None:
    probes = try_power2_neighbor_square_shortcuts(
        1_523_713,
        ordinary_horizon=100,
    )
    assert any(p.multiplier == 255 and p.factor_hit for p in probes)


def test_square_hit_reconstructs_exact_difference() -> None:
    n = 18_677_761
    p = probe_neighbor_square_lift(n, 64, 1)
    assert p.square_root is not None
    center = 64 * p.square_root
    gap = p.fixed_gap_root
    assert center * center - gap * gap == p.multiplier * n
    assert isqrt(p.square_test_value) == p.square_root
