from __future__ import annotations

from math import isqrt

from enterprise_math.brc_neighbor_square_lift_shortcut import (
    compressed_neighbor_distance_start_level,
    compressed_power2_neighbor_distance_candidates,
    neighbor_distance_square_parameters,
    neighbor_square_parameters,
    power2_neighbor_square_candidates,
    probe_neighbor_distance_square_lift,
    probe_neighbor_square_lift,
    try_compressed_power2_neighbor_distance_shortcuts,
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


def test_general_distance_identity() -> None:
    for epsilon in (1, -1):
        for distance in range(1, 12, 2):
            for a in range(2, 20):
                for t in range(1, 20, 2):
                    n = a * a * t + epsilon * distance
                    if n <= distance or n % 2 == 0:
                        continue
                    m_expected = 2 * a - epsilon * distance
                    if m_expected <= 0:
                        continue
                    tt, m, z = neighbor_distance_square_parameters(
                        n, a, distance, epsilon
                    )
                    assert tt == t
                    assert m == m_expected
                    assert z == m * t + 1
                    assert (
                        m * n
                        == a * a * z - (a - epsilon * distance) ** 2
                    )


def test_non_square_rejection_changes_nothing() -> None:
    probe = probe_neighbor_square_lift(35, 2, -1)
    assert not probe.factor_hit


def test_beyond_horizon_regression_m127() -> None:
    n = 18_677_761  # 383 * 48,767
    probe = probe_neighbor_square_lift(n, 64, 1)
    assert probe.multiplier == 127
    assert probe.square_test_value == 761**2
    assert probe.fixed_gap_root == 63
    assert probe.factor_hit
    assert probe.proper_factor in (383, 48_767)


def test_beyond_horizon_regression_m255() -> None:
    n = 1_523_713  # 389 * 3917
    probe = probe_neighbor_square_lift(n, 128, 1)
    assert probe.multiplier == 255
    assert probe.square_test_value == 154**2
    assert probe.factor_hit
    assert probe.proper_factor in (389, 3917)


def test_beyond_horizon_regression_m511() -> None:
    n = 6_094_849  # 761 * 8009
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


def test_radius64_start_level_is_a32() -> None:
    assert compressed_neighbor_distance_start_level(100, 64) == 5
    # D=8,16,32 move the first possible beyond-100 level to a=64.
    assert compressed_neighbor_distance_start_level(100, 8) == 6
    assert compressed_neighbor_distance_start_level(100, 16) == 6
    assert compressed_neighbor_distance_start_level(100, 32) == 6
    # Not every (H,D) admits one-residue compression of the entire window.
    assert compressed_neighbor_distance_start_level(10, 8) is None


def _brute_power2_distance_candidates(
    n: int, horizon: int, distance_limit: int
) -> tuple[tuple[int, int, int, int], ...]:
    out: list[tuple[int, int, int, int]] = []
    for distance in range(1, distance_limit + 1):
        for epsilon in (1, -1):
            shifted = n - epsilon * distance
            if shifted <= 0:
                continue
            k = 1
            while True:
                a = 1 << k
                square = a * a
                if square > shifted:
                    break
                if shifted % square == 0:
                    multiplier = 2 * a - epsilon * distance
                    if multiplier > horizon:
                        out.append((distance, epsilon, a, multiplier))
                k += 1
    return tuple(sorted(out))


def test_compressed_window_equals_explicit_distance_scan() -> None:
    # Exact finite regression of the no-distance-scan theorem.
    for distance_limit in (8, 16, 32, 64):
        assert compressed_neighbor_distance_start_level(100, distance_limit) is not None
        for n in range(101, 2500, 2):
            expected = _brute_power2_distance_candidates(
                n, 100, distance_limit
            )
            compressed = tuple(sorted(
                compressed_power2_neighbor_distance_candidates(
                    n,
                    ordinary_horizon=100,
                    max_distance=distance_limit,
                    all_levels=True,
                )
            ))
            assert compressed == expected


def test_balanced_radius64_incremental_witness_m171() -> None:
    # 7,245,781 = 1847 * 3923.  N+43 = 64^2 * 1769, and the compressed
    # radius-64 observer finds d=43 without scanning d=1..64.
    n = 7_245_781
    candidates = compressed_power2_neighbor_distance_candidates(
        n,
        ordinary_horizon=100,
        max_distance=64,
        all_levels=True,
    )
    assert (43, -1, 64, 171) in candidates
    probe = probe_neighbor_distance_square_lift(n, 64, 43, -1)
    assert probe.multiplier == 171
    assert probe.square_test_value == 550**2
    assert probe.fixed_gap_root == 107
    assert probe.factor_hit
    assert probe.proper_factor in (1847, 3923)

    probes = try_compressed_power2_neighbor_distance_shortcuts(
        n,
        ordinary_horizon=100,
        max_distance=64,
        all_levels=True,
    )
    assert any(p.multiplier == 171 and p.factor_hit for p in probes)
