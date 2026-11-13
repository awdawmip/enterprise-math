#!/usr/bin/env python3
"""R708 exact source-counting BRC checker; six-axis Cell-local candidate triads."""
import json
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import factorial
from pathlib import Path

AXES = 6
TRIPLES = tuple(combinations(range(AXES), 3))

@lru_cache(None)
def partition_count(n):
    """Count labeled-token partitions by singling out the first remaining token."""
    if not any(n):
        return 1
    if sum(n) % 3:
        return 0
    m = sum(n) // 3
    if max(n) > m:
        return 0
    i = next(i for i, v in enumerate(n) if v)
    out = 0
    for j in range(i + 1, AXES):
        if not n[j]:
            continue
        for k in range(j + 1, AXES):
            if not n[k]:
                continue
            r = list(n)
            for axis in (i, j, k):
                r[axis] -= 1
            out += n[j] * n[k] * partition_count(tuple(r))
    return out

def greedy_certificate(n):
    """Exhibit m disjoint axis triples and certify remaining max<=m-1."""
    r = list(n)
    triples = []
    while any(r):
        m = sum(r) // 3
        ix = sorted(range(AXES), key=lambda i: (-r[i], i))[:3]
        assert m > 0 and r[ix[-1]] > 0
        for i in ix:
            r[i] -= 1
        assert max(r) <= m - 1 and sum(r) == 3 * (m - 1)
        triples.append(tuple(sorted(ix)))
    return triples

def coefficient_powers(max_m):
    """Independent integer coefficient recurrence for H(x)^m."""
    poly = {(0,) * AXES: 1}
    yield 0, poly
    for m in range(1, max_m + 1):
        nxt = defaultdict(int)
        for n, coeff in poly.items():
            for triple in TRIPLES:
                r = list(n)
                for i in triple:
                    r[i] += 1
                nxt[tuple(r)] += coeff
        poly = dict(nxt)
        yield m, poly

def hidden_axis_counts(n, i, j):
    """Exact C_k=n_k*D(n-e_i-e_j-e_k) with named visible tokens."""
    if i == j or not n[i] or not n[j]:
        return {}
    out = {}
    for k in range(AXES):
        if k in (i, j) or not n[k]:
            continue
        r = list(n)
        for a in (i, j, k):
            r[a] -= 1
        out[k] = n[k] * partition_count(tuple(r))
    return out

def run():
    totals = {}
    for m, poly in coefficient_powers(5):
        profiles = (n for n in product(range(m + 1), repeat=AXES)
                    if sum(n) == 3 * m)
        checked = 0
        for n in profiles:
            coefficient = poly.get(n, 0)
            labeled = coefficient
            for v in n:
                labeled *= factorial(v)
            labeled //= factorial(m)
            assert partition_count(n) == labeled, (m, n)
            assert (partition_count(n) > 0) == (max(n) <= m)
            greedy = greedy_certificate(n)
            assert len(greedy) == m
            assert tuple(sum(i in t for t in greedy) for i in range(AXES)) == n
            checked += 1
        totals[str(m)] = {"feasible_profiles": checked, "poly_support": len(poly)}
    assert [totals[str(i)]["feasible_profiles"] for i in range(6)] == [
        1, 20, 141, 580, 1751, 4332]
    family_cases = 0
    for m in range(1, 8):
        for a in range(m + 1):
            n = (m, m, a, m - a, 0, 0)
            D = partition_count(n)
            hidden = hidden_axis_counts(n, 0, 1)
            assert D == factorial(m) ** 2
            assert hidden.get(2, 0) == a * factorial(m - 1) ** 2
            assert hidden.get(3, 0) == (m - a) * factorial(m - 1) ** 2
            assert sum(hidden.values()) == factorial(m) * factorial(m - 1)
            family_cases += 1
    n = (3, 3, 2, 1, 0, 0)
    assert partition_count(n) == 36
    assert hidden_axis_counts(n, 0, 1) == {2: 8, 3: 4}
    assert family_cases == 35
    evidence = {
        "marker": "R708_TRIAD_FEASIBILITY_SOURCE_KERNEL_EXACT_PASS",
        "source_type": "Cell-local labeled equal-quantum three-distinct-axis candidate",
        "finite_profiles": totals,
        "total_profiles_checked": sum(x["feasible_profiles"] for x in totals.values()),
        "family_cases_checked": family_cases,
        "independent_methods": [
            "H^m coefficient recurrence", "first-labeled-token source recurrence",
            "constructive greedy certificate"],
        "infinite_family": {
            "D": "(m!)^2", "hidden_k": "a*((m-1)!)^2",
            "hidden_l": "(m-a)*((m-1)!)^2"},
        "witness": {
            "n": list(n), "D": 36, "visible_named_pair_cotriad_count": 12,
            "hidden_integer_sources": {"2": 8, "3": 4},
            "conditional_probabilities": {"2": "2/3", "3": "1/3"}},
        "scope": "Exact integer positive BRC source-counts only, no native physical update"}
    print(evidence["marker"], totals, evidence["witness"])
    return evidence

if __name__ == "__main__":
    output = run()
    Path(__file__).with_name(
        "R708_TRIAD_FEASIBILITY_BRC_EVIDENCE_20261111.json"
    ).write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                 encoding="utf-8")
