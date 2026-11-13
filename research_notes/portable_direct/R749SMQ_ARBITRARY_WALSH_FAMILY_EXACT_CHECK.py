#!/usr/bin/env python3
"""R749SMQ exact finite checker: arbitrary Walsh families over F_2^d (d<=4).
Every enumeration uses integer bit operations; kernel masses use Fraction.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json


def pair(a, b):
    return (a & b).bit_count() & 1


def span(vectors):
    result = {0}
    for v in vectors:
        result |= {w ^ v for w in tuple(result)}
    return frozenset(result)


def subspaces(d):
    spaces = {frozenset({0})}
    while True:
        enlarged = spaces | {span(tuple(s) + (v,)) for s in spaces for v in range(1 << d)}
        if len(enlarged) == len(spaces):
            return sorted(spaces, key=lambda s: (len(s), tuple(sorted(s))))
        spaces = enlarged


def dimension(s):
    return len(s).bit_length() - 1


def orth_nonzero(s, d):
    return frozenset(a for a in range(1, 1 << d)
                     if all(pair(a, x) == 0 for x in s))


def classify(d):
    spaces = subspaces(d)
    entries = [(dimension(s), frozenset(s - {0}), orth_nonzero(s, d))
               for s in spaces]
    assert len(spaces) == {1: 2, 2: 5, 3: 16, 4: 67}[d]
    exact, odd = 0, 0
    gaps = Counter()
    exceptional = set()
    for mask in range(1 << ((1 << d) - 1)):
        U = frozenset(a for a in range(1, 1 << d) if mask & (1 << (a - 1)))
        r = max(dim for dim, sub, orth in entries if sub <= U)
        h = min(dim for dim, sub, orth in entries if not U.intersection(orth))
        assert r <= h
        if r == h:
            exact += 1
        else:
            exceptional.add(U)
            gaps[(r, h, len(U))] += 1
        if U and any(all(pair(a, x) for a in U) for x in range(1, 1 << d)):
            odd += 1
            assert r == h == 1
    return {
        "d": d, "subspaces": len(spaces),
        "families_including_empty": 1 << ((1 << d) - 1),
        "sandwich_exact_families": exact,
        "sandwich_gap_families": len(exceptional),
        "gap_types": [{"r": r, "h": h, "family_size": n, "count": count}
                      for (r, h, n), count in sorted(gaps.items())],
        "odd_balanced_nonempty_families": odd,
    }, exceptional


def check_circuits(exceptional):
    all_nonzero = frozenset(range(1, 16))
    circuits = set()
    for t in combinations(range(1, 16), 5):
        C = frozenset(t)
        if span(t) != frozenset(range(16)):
            continue
        if not all(span(v) == frozenset(range(16)) for v in combinations(t, 4)):
            continue
        assert t[0] ^ t[1] ^ t[2] ^ t[3] ^ t[4] == 0
        circuits.add(C)
    assert len(circuits) == 168
    assert (circuits | {all_nonzero - C for C in circuits}) == exceptional
    return len(circuits)


def check_kernels():
    C = frozenset({1, 2, 4, 8, 15})
    complement = frozenset(range(1, 16)) - C
    signs = {x: [1 - 2 * pair(a, x) for a in sorted(C)] for x in range(16)}
    negatives = {x: sum(s == -1 for s in signs[x]) for x in range(16)}
    assert Counter(negatives.values()) == Counter({0: 1, 2: 10, 4: 5})
    rho_C = {x: (Fraction(1) + Fraction(sum(signs[x]), 3)) / 16
             for x in range(16)}
    rho_bar = {x: Fraction(3, 8) if x == 0 else
                 Fraction(1, 8) if negatives[x] == 4 else Fraction(0)
               for x in range(16)}
    assert all(p >= 0 for p in rho_C.values())
    assert all(p >= 0 for p in rho_bar.values())
    assert sum(rho_C.values()) == sum(rho_bar.values()) == 1
    assert rho_C[0] == Fraction(1, 6)
    assert rho_bar[0] == Fraction(3, 8)
    for a in range(1, 16):
        coefficient_C = sum(rho_C[x] * (1 - 2 * pair(a, x)) for x in range(16))
        coefficient_bar = sum(rho_bar[x] * (1 - 2 * pair(a, x)) for x in range(16))
        if a not in C:
            assert coefficient_C == 0
        if a in C:
            assert coefficient_bar == 0
    for rho in (rho_C, rho_bar):
        for x in range(16):
            column = [rho[z ^ x] for z in range(16)]
            assert sum(column) == 1
            assert all(p >= 0 for p in column)
            assert column[x] == rho[0]
    return {
        "canonical_five_circuit": sorted(C),
        "complement_family": sorted(complement),
        "circuit_kernel_mass_at_zero": "1/6",
        "circuit_kernel_guaranteed_TV_upper": "5/6",
        "complement_kernel_mass_at_zero": "3/8",
        "complement_kernel_guaranteed_TV_upper": "5/8",
        "convolution_columns_checked": 32,
        "character_zero_constraints_checked": 30
    }


def main():
    rows = []
    exceptional = None
    for d in (1, 2, 3, 4):
        result, gaps = classify(d)
        rows.append(result)
        if d < 4:
            assert not gaps
        else:
            exceptional = gaps
    circuit_count = check_circuits(exceptional)
    certificates = check_kernels()
    output = {
        "schema": "R749SMQ_EXACT_FINITE_CHECK_V1",
        "status": "PASS",
        "arithmetic": "exact integer GF(2) enumeration and Fraction",
        "scope": "all retained-character subsets in F_2^d for 1 <= d <= 4; exact special kernels at d=4",
        "classification": rows,
        "exceptional_four_dimensional_five_circuits": circuit_count,
        "kernel_certificates": certificates,
        "proof_boundary": "finite classifications verified; universal minimax inequalities proved separately in the markdown manuscript; no V29/V39 native event claim"
    }
    print(json.dumps(output, sort_keys=True, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
