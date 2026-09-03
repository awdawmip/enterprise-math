#!/usr/bin/env python3
"""Exact regressions for r005a_p2_gap_shadow_inversion.py."""
from __future__ import annotations

import json
import tempfile
from bisect import bisect_left, bisect_right
from math import isqrt
from pathlib import Path

from r005a_p2_gap_shadow_inversion import (
    GapRow,
    P85,
    build_seam,
    canonical_rows_sha256,
    ceil_sqrt,
    floor_square_preimage,
    floor_width,
    load_catalog,
    scan_gap_shadows,
    validate_catalog_for_seam,
)


def sieve(limit: int) -> list[int]:
    a = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        a[0] = 0
    if limit >= 1:
        a[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if a[p]:
            a[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [i for i, v in enumerate(a) if v]


def prev_next_prime(n: int, primes: list[int]) -> tuple[int, int]:
    i = bisect_right(primes, n) - 1
    return primes[i], primes[i + 1]


def test_floor_square_inverse() -> None:
    for Q in range(1, 80):
        for m in range(0, 300):
            lo, hi = floor_square_preimage(m, Q)
            brute = [k for k in range(0, ceil_sqrt((m + 1) * Q) + 2) if k * k // Q == m]
            if brute:
                assert (lo, hi) == (min(brute), max(brute))
            else:
                assert lo > hi


def test_gap_shadow_equivalence() -> int:
    # Exhaustively test the exact equivalence over many rational square intervals.
    primes = sieve(20_000)
    checks = 0
    for Q in range(2, 80):
        for k in range(2, 800):
            A = k * k
            U = A + 2 * k
            n = A // Q
            if n < 2 or n + 100 >= primes[-1]:
                continue
            D = U // Q - n
            a, b = prev_next_prime(n, primes)
            t = n - a
            g = b - a
            left_index = bisect_left(primes, n + 1)
            right_index = bisect_right(primes, U // Q)
            prime_free = left_index == right_index
            assert prime_free == (g > D + t)
            checks += 1
    return checks


def test_deficit_formula() -> int:
    checks = 0
    for q in (5, 7, 11, 13, 17, 19):
        Q = q * q
        G = 10
        H = G // 2
        for s in range(1, Q):
            k = H * Q - s
            r = (s * s) % Q
            D = floor_width(k, Q)
            d = G - D
            expected_d = -((r - 2 * s) // Q)
            assert d == expected_d
            assert ((d - 1) * Q < 2 * s - r <= d * Q)
            checks += 1
    return checks


def all_gap_rows(primes: list[int], start: int, end: int, min_gap: int) -> list[GapRow]:
    rows: list[GapRow] = []
    for a, b in zip(primes, primes[1:]):
        if start <= a <= end and b - a >= min_gap:
            rows.append(GapRow(a, b - a))
    return rows


def test_synthetic_shadow_scanner() -> tuple[int, int]:
    # Generic small exact analogue of the q^2 seam: compare inversion to k-enumeration.
    Q = 47 * 47
    G = 20
    k_lo = 15_000
    k_hi = 20_000
    n_lo = k_lo * k_lo // Q
    n_hi = k_hi * k_hi // Q
    primes = sieve(n_hi + 200)
    max_gap = max(b - a for a, b in zip(primes, primes[1:]) if n_lo - 10 <= a <= n_hi)
    G = max(G, max_gap)

    # Exact brute failures.
    failures: set[int] = set()
    dmax = 0
    for k in range(k_lo, k_hi + 1):
        A = k * k
        U = A + 2 * k
        n = A // Q
        D = U // Q - n
        dmax = max(dmax, G - D)
        i = bisect_left(primes, n + 1)
        if i == bisect_right(primes, U // Q):
            failures.add(k)

    # Minimal seam-like object, preserving scanner contract.
    from r005a_p2_gap_shadow_inversion import Seam
    threshold = G - dmax + 1
    if threshold > 1 and threshold % 2:
        threshold += 1
    seam = Seam(
        q=47,
        q_square=Q,
        gap_bound=G,
        h=G // 2,
        k_global_fail=k_lo,
        k_q2_width=k_hi + 1,
        k_last=k_hi,
        s_max=0,
        d_max_bound=dmax,
        floor_start=n_lo,
        floor_end=n_hi,
        required_gap_start_min=n_lo - max(0, dmax - 1),
        required_gap_start_max=n_hi,
        required_complete_gap_ge=threshold,
        one_unit_whole_seam=False,
    )
    rows = all_gap_rows(primes, seam.required_gap_start_min, n_hi, threshold)
    inverted = {x["k"] for x in scan_gap_shadows(seam, rows)}
    assert inverted == failures
    return len(failures), len(rows)


def test_q_frontiers() -> dict[str, int | bool]:
    s1 = build_seam(78541)
    s2 = build_seam(78553)
    assert s1.one_unit_whole_seam
    assert s1.d_max_bound == 1
    assert not s2.one_unit_whole_seam
    assert s2.d_max_bound == 2
    assert s2.q_square == 6_170_573_809
    assert s2.k_global_fail == 2_822_453_183_434
    assert s2.k_q2_width == 2_826_122_804_522
    assert s2.s_max == 3_669_621_088
    assert s2.floor_start == 1_291_005_053_866_736
    assert s2.floor_end == 1_294_364_244_470_160
    assert s2.required_gap_start_min == 1_291_005_053_866_735
    assert s2.required_complete_gap_ge == 916
    return {
        "q78541_one_unit": s1.one_unit_whole_seam,
        "q78553_d_max": s2.d_max_bound,
        "q78553_required_start": s2.required_gap_start_min,
        "q78553_required_end": s2.required_gap_start_max,
    }


def test_catalog_fail_closed() -> str:
    seam = build_seam(78553)
    rows: list[GapRow] = []
    data = {
        "schema": "R005A_CONSECUTIVE_PRIME_GAP_CATALOG_V1",
        "source_id": "regression-incomplete",
        "coverage_start": seam.required_gap_start_min,
        "coverage_end": seam.required_gap_start_max,
        "complete_for_gap_ge": 916,
        "max_gap_bound": 916,
        "max_gap_bound_start": seam.required_gap_start_min,
        "max_gap_bound_end": seam.required_gap_start_max,
        "completeness_attestation": False,
        "rows_sha256": canonical_rows_sha256(rows),
        "rows": [],
    }
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "c.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        metadata, loaded = load_catalog(p)
        try:
            validate_catalog_for_seam(metadata, loaded, seam, verify_rows=True)
        except ValueError as exc:
            assert "completeness_attestation" in str(exc)
            return str(exc)
    raise AssertionError("incomplete catalog was not rejected")


def main() -> None:
    test_floor_square_inverse()
    shadow_checks = test_gap_shadow_equivalence()
    deficit_checks = test_deficit_formula()
    synthetic_failures, synthetic_rows = test_synthetic_shadow_scanner()
    frontier = test_q_frontiers()
    fail_closed = test_catalog_fail_closed()
    result = {
        "schema": "R005A_P2_GAP_SHADOW_REGRESSION_RESULT_V1",
        "status": "PASS",
        "floor_square_inverse": "exhaustive Q<=79,m<300",
        "gap_shadow_equivalence_checks": shadow_checks,
        "deficit_formula_checks": deficit_checks,
        "synthetic_scanner_failure_count": synthetic_failures,
        "synthetic_large_gap_rows": synthetic_rows,
        "frontier": frontier,
        "fail_closed_message": fail_closed,
        "p85": P85,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
