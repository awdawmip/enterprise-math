#!/usr/bin/env python3
"""Exact audit for the R005-A p=2 repair-gap multiplicity checkpoint.

Reuses the independent 49-basin / 50-residual certificate family from
r005a_p2_exact_residual_family.py. This is a finite regression only; the
companion note contains the symbolic proofs.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json

import r005a_p2_exact_residual_family as base


def prev_prime_le(n: int) -> int:
    m = n
    if m >= 3 and m % 2 == 0:
        m -= 1
    while m >= 2:
        if base.is_prime(m):
            return m
        m -= 2 if m > 3 else 1
    raise ValueError("no previous prime")


def next_prime_gt(n: int) -> int:
    m = n + 1
    if m <= 2:
        return 2
    if m % 2 == 0:
        m += 1
    while not base.is_prime(m):
        m += 2
    return m


def small_nonforced_coordinates(k: int) -> tuple[int, int, tuple[int, ...]]:
    """NF_k intersect (floor(U^(1/4)), floor(A^(1/3))]."""
    A = k * k
    U = A + 2 * k
    c4 = base.integer_root(U, 4)
    c3a = base.integer_root(A, 3)
    out: list[int] = []
    for q in base.BASE_PRIMES:
        if q <= c4:
            continue
        if q > c3a:
            break
        assert q**3 <= A
        if not base.witness_forced(k, q):
            out.append(q)
    return c4, c3a, tuple(out)


def cofactor_gap(k: int, q: int) -> tuple[int, int, int]:
    A = k * k
    x_floor = A // q
    alpha = prev_prime_le(x_floor)
    beta = next_prime_gt(x_floor)
    return alpha, beta, beta - alpha


def residual_blocks_by_k() -> dict[int, list[tuple[int, ...]]]:
    blocks: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for k, _, factors in base.CERTIFICATES:
        blocks[k].append(tuple(sorted(p for p, _ in factors)))
    return dict(blocks)


def transversal_number(blocks: list[tuple[int, ...]]) -> int:
    vertices = sorted(set().union(*(set(block) for block in blocks)))
    for r in range(len(vertices) + 1):
        for choice in combinations(vertices, r):
            chosen = set(choice)
            if all(chosen.intersection(block) for block in blocks):
                return r
    raise AssertionError("finite hypergraph has no transversal")


def main() -> None:
    blocks_by_k = residual_blocks_by_k()
    assert len(blocks_by_k) == 49

    small_count_hist = Counter()
    two_small_basins: list[int] = []
    total_small = 0
    shared_gap_groups = 0
    min_ratio = None
    min_ratio_row = None

    for k, blocks in sorted(blocks_by_k.items()):
        A = k * k
        U = A + 2 * k
        _, _, small_nf = small_nonforced_coordinates(k)
        assert small_nf

        # P2-GM1: the small-NF set is a transversal.
        assert all(set(block).intersection(small_nf) for block in blocks)
        tau = transversal_number(blocks)
        assert tau <= len(small_nf)

        small_count_hist[len(small_nf)] += 1
        total_small += len(small_nf)
        if len(small_nf) == 2:
            two_small_basins.append(k)

        gap_groups: dict[tuple[int, int], list[int]] = defaultdict(list)
        for q in small_nf:
            alpha, beta, g = cofactor_gap(k, q)

            # q is non-forced, so the eligible cofactor interval is prime-free.
            assert alpha * q <= A
            assert beta * q > U

            # P2-GM2, exact form of g > 2*(A/q)^(1/4).
            assert q * (g**4) > 16 * A

            ratio = g / ((A / q) ** 0.25)
            if min_ratio is None or ratio < min_ratio:
                min_ratio = ratio
                min_ratio_row = {
                    "k": k,
                    "q": q,
                    "alpha": alpha,
                    "beta": beta,
                    "gap": g,
                    "ratio_g_over_x_quarter": ratio,
                }
            gap_groups[(alpha, beta)].append(q)

        # P2-GM3: repeated occupancy of one cofactor gap is amplified.
        for (alpha, beta), qs in gap_groups.items():
            if len(qs) < 2:
                continue
            shared_gap_groups += 1
            qs = sorted(qs)
            m = len(qs)
            g = beta - alpha
            q_lo, q_hi = qs[0], qs[-1]
            assert g * q_lo * q_hi > A * (q_hi - q_lo)
            assert g**3 > 8 * ((m - 1) ** 3) * A

    result = {
        "status": "R005-A P2 REPAIR-GAP MULTIPLICITY EXACT AUDIT / NOT EXHAUSTIVE IN k",
        "verified_basins": len(blocks_by_k),
        "verified_residuals": len(base.CERTIFICATES),
        "small_nf_total": total_small,
        "small_nf_count_histogram": dict(sorted(small_count_hist.items())),
        "two_small_nf_basins": two_small_basins,
        "all_certificate_basins_tau_le_small_nf_count": True,
        "all_small_nf_coordinates_satisfy_exact_quarter_power_gap": True,
        "shared_cofactor_gap_groups_in_current_family": shared_gap_groups,
        "shared_gap_amplification_checked": True,
        "minimum_observed_gap_ratio": min_ratio_row,
        "interpretation": (
            "A repair number >= t requires at least t small non-forced coordinates. "
            "Each such coordinate forces a cofactor prime gap g>2*x^(1/4). "
            "If m of them occupy one cofactor gap, that gap is forced above "
            "2*(m-1)*k^(2/3)."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
