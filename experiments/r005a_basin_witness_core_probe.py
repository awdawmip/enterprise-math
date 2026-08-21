#!/usr/bin/env python3
"""R005-A/R005-B exact cross-route probe: forced screening core + residual hypergraph.

Domain:
    k^p < n < (k+1)^p

R005-B universal screening horizon:
    F_p(k) = isqrt((k+1)^p - 1)

Witness language:
    candidate prime q <= F_p(k) rejects n iff q | n.

For each basin:
- rejection edge E(n) = candidate prime divisors of composite n;
- forced core = witnesses that are the sole rejector of at least one composite;
- residual composite = E(n) is disjoint from forced core.

By the generic R005-A forced-basis theorem:
- every safe family contains the forced core;
- remaining choices form a hitting-set problem on residual edges;
- a least safe family under inclusion exists iff there are no residual edges.

The scan is exact inside the explicit integer bound.  No conclusion is made
outside that bound.
"""

from __future__ import annotations

from array import array
from collections import Counter
from itertools import combinations
from math import isqrt
import json

MAX_U = 4_004_000
MAX_POWER = 8


def spf_table(limit: int) -> array:
    spf = array("I", [0]) * (limit + 1)
    if limit >= 1:
        spf[1] = 1
    for p in range(2, limit + 1):
        if spf[p] != 0:
            continue
        spf[p] = p
        if p * p <= limit:
            for m in range(p * p, limit + 1, p):
                if spf[m] == 0:
                    spf[m] = p
    return spf


SPF = spf_table(MAX_U)


def is_prime(n: int) -> bool:
    return n >= 2 and SPF[n] == n


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    out = []
    while n > 1:
        q = SPF[n]
        exponent = 0
        while n % q == 0:
            n //= q
            exponent += 1
        out.append((q, exponent))
    return tuple(out)


def distinct_prime_factors(n: int) -> tuple[int, ...]:
    return tuple(q for q, _ in factorization(n))


def primes_up_to(limit: int) -> tuple[int, ...]:
    return tuple(n for n in range(2, limit + 1) if is_prime(n))


def basin_record(power: int, k: int) -> dict:
    lower = k ** power
    upper = (k + 1) ** power - 1
    if upper > MAX_U:
        raise ValueError("basin exceeds exact SPF bound")

    horizon = isqrt(upper)
    witnesses = primes_up_to(horizon)

    edges: dict[int, tuple[int, ...]] = {}
    for n in range(lower + 1, upper + 1):
        if is_prime(n):
            continue
        edge = tuple(q for q in distinct_prime_factors(n) if q <= horizon)
        if not edge:
            raise AssertionError(("missing screening witness", power, k, n, horizon))
        edges[n] = edge

    forced = {edge[0] for edge in edges.values() if len(edge) == 1}
    residual = {
        n: edge
        for n, edge in edges.items()
        if not any(q in forced for q in edge)
    }

    return {
        "power": power,
        "k": k,
        "lower_open": lower,
        "upper_open": (k + 1) ** power,
        "horizon": horizon,
        "witnesses": witnesses,
        "composite_count": len(edges),
        "forced_core": tuple(sorted(forced)),
        "residual_edges": residual,
        "least_exists": not residual,
    }


def residual_minimal_transversals(record: dict) -> list[tuple[int, ...]]:
    edges = list(record["residual_edges"].values())
    if not edges:
        return [()]
    candidates = tuple(sorted(set().union(*map(set, edges))))
    minimal = []
    for r in range(len(candidates) + 1):
        for subset in combinations(candidates, r):
            S = set(subset)
            if not all(S.intersection(edge) for edge in edges):
                continue
            if any(
                all((S - {w}).intersection(edge) for edge in edges)
                for w in S
            ):
                continue
            minimal.append(subset)
    return minimal


def full_minimal_safe_bases(record: dict) -> list[tuple[int, ...]]:
    core = set(record["forced_core"])
    return [
        tuple(sorted(core | set(extra)))
        for extra in residual_minimal_transversals(record)
    ]


def scan() -> dict:
    power_scan = {}
    bad_records = {}

    for power in range(2, MAX_POWER + 1):
        k = 2
        failures = []
        count = 0
        while (k + 1) ** power - 1 <= MAX_U:
            record = basin_record(power, k)
            count += 1
            if not record["least_exists"]:
                failures.append(k)
                if power == 2:
                    bad_records[k] = record
            k += 1
        power_scan[str(power)] = {
            "scanned_basin_count": count,
            "no_least_count": len(failures),
            "no_least_k": failures,
        }

    expected_square_bad = [
        25, 47, 62, 123, 130, 151, 157, 162, 196, 217, 308, 364, 365,
        479, 556, 888, 924, 935, 1008, 1056, 1078, 1162, 1290, 1345,
        1454, 1511, 1541, 1577, 1612, 1627, 1679, 1781, 1790, 1865, 1897
    ]
    assert power_scan["2"]["no_least_k"] == expected_square_bad
    assert all(power_scan[str(p)]["no_least_count"] == 0 for p in range(3, 9))

    k25 = bad_records[25]
    assert k25["forced_core"] == (2, 3, 5, 11, 17, 23)
    assert k25["residual_edges"] == {637: (7, 13)}
    assert full_minimal_safe_bases(k25) == [
        (2, 3, 5, 7, 11, 17, 23),
        (2, 3, 5, 11, 13, 17, 23),
    ]

    k888 = bad_records[888]
    assert k888["residual_edges"] == {790079: (73, 79, 137)}
    assert factorization(790079) == ((73, 1), (79, 1), (137, 1))

    k1781 = bad_records[1781]
    assert k1781["residual_edges"] == {
        3172511: (101, 311),
        3175339: (101, 149, 211),
    }
    residual_transversals_1781 = residual_minimal_transversals(k1781)
    assert residual_transversals_1781 == [
        (101,),
        (149, 311),
        (211, 311),
    ]
    min_card = min(map(len, residual_transversals_1781))
    min_card_choices = [t for t in residual_transversals_1781 if len(t) == min_card]
    assert min_card_choices == [(101,)]
    assert not all(set((101,)).issubset(t) for t in residual_transversals_1781)

    exponent_patterns = Counter()
    residual_total = 0
    max_residual_per_basin = 0
    square_details = []
    for k in expected_square_bad:
        r = bad_records[k]
        residual_total += len(r["residual_edges"])
        max_residual_per_basin = max(max_residual_per_basin, len(r["residual_edges"]))
        residual_rows = {}
        for n, edge in r["residual_edges"].items():
            fac = factorization(n)
            exponent_patterns[tuple(sorted((e for _, e in fac), reverse=True))] += 1
            residual_rows[str(n)] = {
                "edge": edge,
                "factorization": fac,
            }
        square_details.append({
            "k": k,
            "interval": [k * k + 1, (k + 1) * (k + 1) - 1],
            "forced_core_size": len(r["forced_core"]),
            "residual": residual_rows,
        })

    return {
        "status": "EXACT_BOUNDED_CROSS_ROUTE_PROBE / NOT_THEOREM_BEYOND_BOUND",
        "max_upper_endpoint": MAX_U,
        "power_scan": power_scan,
        "square_summary": {
            "no_least_basin_count": len(expected_square_bad),
            "residual_composite_total": residual_total,
            "max_residual_composites_in_one_basin": max_residual_per_basin,
            "residual_factor_exponent_patterns": {
                str(pattern): count
                for pattern, count in sorted(exponent_patterns.items())
            },
        },
        "earliest_square_no_least": {
            "k": 25,
            "open_basin": "625 < n < 676",
            "horizon": k25["horizon"],
            "candidate_witnesses": k25["witnesses"],
            "forced_core": k25["forced_core"],
            "residual_edges": k25["residual_edges"],
            "inclusion_minimal_safe_bases": full_minimal_safe_bases(k25),
        },
        "first_three_prime_residual": {
            "k": 888,
            "n": 790079,
            "factorization": factorization(790079),
            "edge": k888["residual_edges"][790079],
        },
        "first_two_residual_edge_basin": {
            "k": 1781,
            "residual_edges": k1781["residual_edges"],
            "residual_inclusion_minimal_transversals": residual_transversals_1781,
            "unique_minimum_cardinality_transversal": (101,),
            "least_transversal_exists": False,
        },
        "square_no_least_records": square_details,
    }


if __name__ == "__main__":
    print(json.dumps(scan(), ensure_ascii=False, indent=2))
