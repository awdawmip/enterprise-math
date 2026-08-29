#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from math import gcd, isqrt, prod

TASK_ID = "RS-SEED6-SEED-SPECIFICITY-TRANSFER-TEST"
PUBLICATION_ID = "TP2-45170A2BBF5D87471FCD"

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def factorization(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def omega(n: int) -> int:
    return len(factorization(n))

def Omega(n: int) -> int:
    return sum(factorization(n).values())

def prime_stream():
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2

def fresh_primes(a: int, b: int, count: int = 2) -> list[int]:
    out: list[int] = []
    for p in prime_stream():
        if gcd(p, a * b) == 1:
            out.append(p)
            if len(out) == count:
                return out
    raise AssertionError("unreachable")

def pairing_states(a: int, b: int, p: int, q: int) -> set[tuple[int, int]]:
    return {
        tuple(sorted((a * b, p * q))),
        tuple(sorted((a * p, b * q))),
        tuple(sorted((a * q, b * p))),
    }

def structural_type(a: int, b: int) -> str:
    if a == b:
        return "EQUALITY"
    if gcd(a, b) > 1:
        return "OVERLAP"
    if is_prime(a) and is_prime(b):
        return "C0_PRIME_PAIR"
    if omega(a) == 1 and omega(b) == 1:
        return "C1_COPRIME_ONE_SUPPORT_THICK"
    return "C2_COPRIME_MULTI_SUPPORT"

def coprime_factor_pairs(s: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a in range(2, isqrt(s) + 1):
        if s % a == 0:
            b = s // a
            if gcd(a, b) == 1:
                out.append((a, b))
    return out

def all_factor_pairs(s: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a in range(2, isqrt(s) + 1):
        if s % a == 0:
            out.append((a, s // a))
    return out

def prime_power_snf(alpha: int, beta: int) -> tuple[int, int, int]:
    # Matrix columns are exponent vectors of p^a q^b, p^a r, q^b r:
    # [[alpha, alpha, 0], [beta, 0, beta], [0, 1, 1]].
    g = gcd(alpha, beta)
    return (1, g, 2 * alpha * beta // g)

def record(a: int, b: int) -> dict:
    p, q = fresh_primes(a, b, 2)
    r = p
    d = gcd(a, b)

    t0, t1, t2 = a * b, a * r, b * r
    g01, g02, g12 = gcd(t0, t1), gcd(t0, t2), gcd(t1, t2)
    assert (g01, g02, g12) == (a, b, r * d)

    triangle_product = t0 * t1 * t2
    gcd_product = g01 * g02 * g12
    assert triangle_product == (a * b * r) ** 2
    assert gcd_product * gcd_product == triangle_product * d * d

    l01 = t0 * t1 // g01
    l02 = t0 * t2 // g02
    l12 = t1 * t2 // g12
    assert l01 == a * b * r
    assert l02 == a * b * r
    assert l12 == a * b * r // d

    row_gcds = (gcd(a * p, a * q), gcd(b * p, b * q))
    col_gcds = (gcd(a * p, b * p), gcd(a * q, b * q))
    diag_gcds = (gcd(a * p, b * q), gcd(a * q, b * p))
    assert row_gcds == (a, b)
    assert col_gcds == (p * d, q * d)
    assert diag_gcds == (d, d)
    assert (a * p) * (b * q) == (a * q) * (b * p)

    states = pairing_states(a, b, p, q)
    expected_state_count = 2 if a == b else 3
    assert len(states) == expected_state_count

    gcd_reconstruction = (
        t0 == g01 * g02
        and t1 == g01 * g12
        and t2 == g02 * g12
    )
    assert gcd_reconstruction == (d == 1)

    common_lcm_top = l01 == l02 == l12 == a * b * r
    assert common_lcm_top == (d == 1)

    b3_coatom = is_prime(a) and is_prime(b) and a != b
    parity_oriented = (a % 2) != (b % 2)

    f_a, f_b = factorization(a), factorization(b)
    single_support = len(f_a) == len(f_b) == 1
    pp_snf = None
    if single_support:
        alpha = next(iter(f_a.values()))
        beta = next(iter(f_b.values()))
        pp_snf = list(prime_power_snf(alpha, beta))
        if b3_coatom:
            assert pp_snf == [1, 1, 2]

    return {
        "a": a,
        "b": b,
        "seed": a * b,
        "type": structural_type(a, b),
        "gcd_ab": d,
        "fresh_pq": [p, q],
        "triangle": [t0, t1, t2],
        "triangle_gcds": [g01, g02, g12],
        "triangle_overlap_defect": d * d,
        "common_lcm_top": common_lcm_top,
        "gcd_reconstruction": gcd_reconstruction,
        "boolean_B3_coatom": b3_coatom,
        "pairing_state_count": len(states),
        "rectangle_row_gcds": list(row_gcds),
        "rectangle_col_gcds": list(col_gcds),
        "rectangle_diag_gcds": list(diag_gcds),
        "rank_one_cross_product": True,
        "parity_oriented": parity_oriented,
        "support_profile": sorted([omega(a), omega(b)]),
        "valuation_weight_profile": sorted([Omega(a), Omega(b)]),
        "prime_power_block_snf": pp_snf,
    }

def minimum_pair(predicate, bound: int = 60) -> tuple[int, int, int]:
    candidates = []
    for a in range(2, bound + 1):
        for b in range(a, bound + 1):
            rec = record(a, b)
            if predicate(rec):
                candidates.append((a * b, a, b))
    s, a, b = min(candidates)
    return (a, b, s)

def build_census() -> dict:
    rows = [record(a, b) for a in range(2, 17) for b in range(a, 17)]
    assert len(rows) == 120

    type_counts = Counter(r["type"] for r in rows)
    pairing_counts = Counter(r["pairing_state_count"] for r in rows)

    assert type_counts == Counter({
        "C0_PRIME_PAIR": 15,
        "C1_COPRIME_ONE_SUPPORT_THICK": 23,
        "C2_COPRIME_MULTI_SUPPORT": 26,
        "OVERLAP": 41,
        "EQUALITY": 15,
    })
    assert pairing_counts == Counter({3: 105, 2: 15})
    assert sum(r["boolean_B3_coatom"] for r in rows) == 15
    assert sum(r["gcd_reconstruction"] for r in rows) == 64
    assert sum(r["common_lcm_top"] for r in rows) == 64
    assert sum(r["parity_oriented"] for r in rows) == 56

    # Required controls and two decomposition-sensitive controls.
    control_pairs = [
        (2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (2, 11), (5, 7),
        (3, 4), (2, 6), (2, 9), (3, 6), (4, 9), (2, 15),
    ]
    controls = [record(a, b) for a, b in control_pairs]

    # Seed scalar alone is not a sufficient carrier datum.
    assert all_factor_pairs(12) == [(2, 6), (3, 4)]
    assert coprime_factor_pairs(12) == [(3, 4)]
    assert coprime_factor_pairs(18) == [(2, 9)]
    assert (3, 6) in all_factor_pairs(18)
    assert coprime_factor_pairs(30) == [(2, 15), (3, 10), (5, 6)]

    # For omega(s)>=2, unordered nontrivial coprime factorizations split the
    # distinct prime-power blocks into two nonempty sets.
    for s in range(4, 500):
        k = omega(s)
        observed = len(coprime_factor_pairs(s))
        expected = (2 ** (k - 1) - 1) if k >= 2 else 0
        assert observed == expected, (s, observed, expected)

    minima = {
        "equality_numeric_cell_collapse": [2, 2, 4],
        "distinct_carrier_overlap": list(minimum_pair(
            lambda r: r["a"] != r["b"] and r["gcd_ab"] > 1
        )),
        "coprime_but_not_prime_pair": list(minimum_pair(
            lambda r: r["a"] != r["b"] and r["gcd_ab"] == 1 and not r["boolean_B3_coatom"]
        )),
        "odd_prime_pair_parity_orientation_failure": list(minimum_pair(
            lambda r: r["boolean_B3_coatom"] and not r["parity_oriented"]
        )),
        "coprime_multi_support_carrier": list(minimum_pair(
            lambda r: r["gcd_ab"] == 1 and r["a"] != r["b"] and max(r["support_profile"]) > 1
        )),
        "scalar_multiple_factor_pairs": [2, 6, 12],
        "scalar_multiple_coprime_carrier_pairs": [2, 15, 30],
    }

    transfer_table = [
        {
            "signature": "rooted Boolean B3 coatom / Levi C6 / prime valuation SNF (1,1,2)",
            "classification": "PRIME_PAIR_GENERIC",
            "reason": "Exact whenever a,b,r are three distinct prime atoms; fails first at decorated seed (3,4), s=12.",
        },
        {
            "signature": "gcd-edge reconstruction x_ij = product of incident gcd labels",
            "classification": "COPRIME_PAIR_GENERIC",
            "reason": "For fresh r, gcd labels are a,b,r*gcd(a,b); exact reconstruction iff gcd(a,b)=1.",
        },
        {
            "signature": "triangle product-square checksum",
            "classification": "TAUTOLOGICAL",
            "reason": "(ab)(ar)(br)=(abr)^2 for arbitrary positive a,b,r.",
        },
        {
            "signature": "three unordered perfect-matching states of four named blocks",
            "classification": "ARBITRARY_PAIR_GENERIC",
            "reason": "Three numerical states survive for a!=b and fresh distinct p,q; equality a=b collapses two states.",
        },
        {
            "signature": "S4 action on three perfect matchings with V4 kernel",
            "classification": "TAUTOLOGICAL",
            "reason": "Standard four-label matching combinatorics; independent of the numerical seed.",
        },
        {
            "signature": "bridge rectangle determinant/cross-product zero",
            "classification": "TAUTOLOGICAL",
            "reason": "[[ap,aq],[bp,bq]] is an outer product for all a,b,p,q.",
        },
        {
            "signature": "rectangle diagonal gcds equal 1 and column gcds p,q",
            "classification": "COPRIME_PAIR_GENERIC",
            "reason": "For fresh p,q the exact labels are diagonal d,d and columns pd,qd, d=gcd(a,b).",
        },
        {
            "signature": "pure unlabeled column/pairing incidence under fresh indices",
            "classification": "ARBITRARY_PAIR_GENERIC",
            "reason": "Carrier relabeling gives a canonical combinatorial transfer for distinct decorated carrier blocks.",
        },
        {
            "signature": "intrinsic orientation from parity of the two seed carriers",
            "classification": "FAILS_UNDER_TRANSFER",
            "reason": "Survives on even/odd seeds (6,10,14,22) but fails already at prime-pair seed 15=(3,5); it is a subtype decoration, not Seed-6-specific.",
        },
        {
            "signature": "seed scalar uniquely determines carrier decomposition",
            "classification": "FAILS_UNDER_TRANSFER",
            "reason": "All factor-pair semantics become ambiguous at s=12; even restricting to coprime carrier pairs, ambiguity begins at s=30.",
        },
        {
            "signature": "minimality / the particular adjacent pair 2,3",
            "classification": "SEED6_SPECIFIC",
            "reason": "True only as external arithmetic-order metadata; it does not enter the bridge incidence, gcd, matching, or rank-one laws and is rejected as a core bridge invariant.",
        },
    ]

    return {
        "schema": "SEED6_SEED_SPECIFICITY_TRANSFER_CENSUS_V1",
        "task_id": TASK_ID,
        "publication_id": PUBLICATION_ID,
        "domain": {
            "decorated_seed_pairs": "2 <= a <= b <= 16",
            "count": len(rows),
            "fresh_index_rule": "p,q are the two least primes not dividing ab",
        },
        "summary": {
            "type_counts": dict(sorted(type_counts.items())),
            "pairing_state_counts": {str(k): v for k, v in sorted(pairing_counts.items())},
            "boolean_B3_coatom_count": sum(r["boolean_B3_coatom"] for r in rows),
            "gcd_reconstruction_count": sum(r["gcd_reconstruction"] for r in rows),
            "common_lcm_top_count": sum(r["common_lcm_top"] for r in rows),
            "parity_oriented_count": sum(r["parity_oriented"] for r in rows),
            "all_product_square": True,
            "all_rank_one_cross_product": True,
            "all_triangle_overlap_defect_equals_gcd_ab_squared": True,
        },
        "minimal_counterexamples": minima,
        "selected_controls": controls,
        "scalar_decomposition_examples": {
            "12_all": [list(x) for x in all_factor_pairs(12)],
            "12_coprime": [list(x) for x in coprime_factor_pairs(12)],
            "18_all": [list(x) for x in all_factor_pairs(18)],
            "18_coprime": [list(x) for x in coprime_factor_pairs(18)],
            "30_coprime": [list(x) for x in coprime_factor_pairs(30)],
        },
        "transfer_table": transfer_table,
        "records": rows,
    }

def main() -> None:
    census = build_census()
    print(json.dumps(census, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
