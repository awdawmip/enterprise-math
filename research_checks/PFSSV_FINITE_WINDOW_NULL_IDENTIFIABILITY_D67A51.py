#!/usr/bin/env python3
"""Exact bounded verifier for RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY.

No random sampling. Uses exact integer arithmetic, a finite Eratosthenes sieve,
and rational identities. The geometry is the frozen X=100000, width=1/100
cell from the accepted PFSSV generation-2 result.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction
from math import isqrt

X = 100_000
UPPER = 101_000


def sieve(n: int) -> bytearray:
    prime = bytearray(b"\x01") * (n + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if prime[p]:
            start = p * p
            prime[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return prime


def main() -> int:
    # q <= U/2 because p >= 2.
    prime = sieve(UPPER // 2)
    p_values = [p for p in range(2, isqrt(UPPER) + 1) if prime[p]]
    rows: dict[int, tuple[int, int]] = {}
    q_rows: dict[int, list[int]] = defaultdict(list)
    q_slots: set[int] = set()
    raw_incidence = 0
    diagonal = 0
    overflow = 0
    row_prime_counts: dict[int, int] = {}

    for p in p_values:
        lo = max(p, X // p + 1)
        hi = UPPER // p
        if lo > hi:
            continue
        rows[p] = (lo, hi)
        count = 0
        for q in range(lo, hi + 1):
            q_slots.add(q)
            q_rows[q].append(p)
            if prime[q]:
                count += 1
                raw_incidence += 1
                diagonal += int(q == p)
                overflow += int(p * p > X)
        row_prime_counts[p] = count

    unique_prime_addresses = {q for q in q_slots if prime[q]}
    shared = {q: tuple(ps) for q, ps in q_rows.items() if len(ps) > 1}
    shared_prime = {q: ps for q, ps in shared.items() if prime[q]}

    # Frozen accepted cell-level geometry / count checks.
    assert len(rows) == 66
    assert sum(count == 0 for count in row_prime_counts.values()) == 15
    assert rows[193] == (519, 523)
    assert rows[163] == (614, 619)
    assert rows[239] == (419, 422)
    assert rows[241] == (415, 419)
    assert [q for q in range(519, 524) if prime[q]] == [521, 523]
    assert [q for q in range(614, 620) if prime[q]] == [617, 619]
    assert [q for q in range(519, 524) if prime[q] and q % 30 == 11] == [521]
    assert [q for q in range(614, 620) if q % 30 == 11] == []
    assert [q for q in range(419, 423) if prime[q]] == [419, 421]
    assert [q for q in range(415, 420) if prime[q]] == [419]

    assert len(q_slots) == 2016
    assert len(unique_prime_addresses) == 236
    assert raw_incidence == 237
    assert diagonal == 1
    assert overflow == 1
    assert shared == {
        322: (311, 313),
        356: (281, 283),
        372: (269, 271),
        419: (239, 241),
        441: (227, 229),
    }
    assert shared_prime == {419: (239, 241)}

    slot_by_residue = Counter(q % 30 for q in q_slots)
    prime_by_residue = Counter(q % 30 for q in unique_prime_addresses)
    assert slot_by_residue[29] == 69
    assert prime_by_residue[29] == 29
    assert sum(prime_by_residue.values()) == 236

    # Contract U: uniform over address-level binary configurations preserving
    # the exact unique occupied-address total K_r in every residue class.
    p_uniform = Fraction(prime_by_residue[29], slot_by_residue[29])

    # Contract W: same support and same K_r, but q=419 has weight 2 while every
    # other residue-29 address has weight 1. Other residue fibers remain uniform.
    # P(419 included)=2*C(68,28)/(C(68,29)+2*C(68,28))=29/49.
    p_weighted = Fraction(
        2 * prime_by_residue[29],
        (slot_by_residue[29] - prime_by_residue[29])
        + 2 * prime_by_residue[29],
    )
    assert p_uniform == Fraction(29, 69)
    assert p_weighted == Fraction(29, 49)
    assert p_uniform != p_weighted

    receipt = {
        "schema": "PFSSV_FINITE_WINDOW_IDENTIFIABILITY_CHECK_V1",
        "status": "PASS_EXACT_BOUNDED_NONIDENTIFIABILITY_WITNESS",
        "random_draws": 0,
        "cell": {"X": X, "width": "1/100", "upper": UPPER},
        "frozen_cell_crosscheck": {
            "geometric_rows": len(rows),
            "zero_total_rows": sum(count == 0 for count in row_prime_counts.values()),
            "raw_prime_pair_incidences": raw_incidence,
            "diagonal_incidences": diagonal,
            "overflow_incidences": overflow,
        },
        "address_geometry": {
            "integer_q_slots_union": len(q_slots),
            "unique_actual_prime_q_addresses": len(unique_prime_addresses),
            "shared_integer_addresses": {
                str(q): list(ps) for q, ps in sorted(shared.items())
            },
            "shared_actual_prime_addresses": {
                str(q): list(ps) for q, ps in sorted(shared_prime.items())
            },
        },
        "old_null_capacity_witness": {
            "source_p": 193,
            "source_window": list(rows[193]),
            "source_row_primes": [521, 523],
            "source_residue_11_prime_count": 1,
            "target_p": 163,
            "target_window": list(rows[163]),
            "target_row_primes": [617, 619],
            "target_residue_11_integer_capacity": 0,
        },
        "shared_address_witness": {
            "q": 419,
            "residue_mod_30": 29,
            "rows": [239, 241],
            "p239_window": list(rows[239]),
            "p241_window": list(rows[241]),
            "residue_29_slot_count_in_union": slot_by_residue[29],
            "residue_29_actual_prime_address_count": prime_by_residue[29],
        },
        "two_compatible_laws": {
            "common_conditioning": (
                "exact occupied-address total K_r in every q mod 30 residue "
                "class, with one shared binary variable per integer q address"
            ),
            "uniform_contract_probability_Z419_1": {
                "numerator": p_uniform.numerator,
                "denominator": p_uniform.denominator,
            },
            "weighted_contract_probability_Z419_1": {
                "numerator": p_weighted.numerator,
                "denominator": p_weighted.denominator,
            },
            "weighted_contract": (
                "within residue 29, q=419 has weight 2 and every other address "
                "weight 1; all other residue fibers are uniform"
            ),
            "same_support": True,
            "same_residue_totals": True,
            "different_target_distribution": True,
        },
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
