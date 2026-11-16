#!/usr/bin/env python3
"""R762CJ: exact conditional K4 signed-area orbit and repair verifier."""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial, prod
import json
import sys

VERTICES = tuple(range(4))
HIDDEN = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))

def signed_action(p):
    entries = []
    for a, b in HIDDEN:
        left = tuple(sorted((p[a[0]], p[a[1]])))
        right = tuple(sorted((p[b[0]], p[b[1]])))
        if (left, right) in HIDDEN:
            entries.append((HIDDEN.index((left, right)), 1))
        else:
            entries.append((HIDDEN.index((right, left)), -1))
    return tuple(entries)

ACTIONS = tuple(signed_action(p) for p in permutations(VERTICES))
assert len(ACTIONS) == len(set(ACTIONS)) == 24

def apply(z, matrix, q):
    result = [0, 0, 0]
    for i, (j, sign) in enumerate(matrix):
        result[j] = (sign * z[i]) % q
    return tuple(result)

def self_inverse(a, q):
    return 2 * a % q == 0

def signature(z, q):
    folded = tuple(sorted(min(x, (-x) % q) for x in z))
    if any(self_inverse(a, q) for a in folded):
        return (folded, None)
    negative_parity = sum(x > q // 2 for x in z) % 2
    return (folded, negative_parity)

def multiplicity(folded):
    counts = Counter(folded)
    return factorial(3) // prod(factorial(v) for v in counts.values())

def predicted_size(sig, q):
    folded, parity = sig
    s = sum(self_inverse(a, q) for a in folded)
    return multiplicity(folded) * (2 ** (3 - s) if s else 4)

def weight(z, q):
    return prod(2 if x == 0 else comb(q, x) for x in z)

def verify():
    rows = []
    for q in range(2, 17):
        unseen = set(product(range(q), repeat=3))
        labels = {}
        sizes = Counter()
        mass_total = 0
        masses = []
        while unseen:
            z = min(unseen)
            orbit = {apply(z, a, q) for a in ACTIONS}
            assert orbit <= unseen
            sig = signature(z, q)
            assert sig not in labels
            assert all(signature(x, q) == sig for x in orbit)
            assert len(orbit) == predicted_size(sig, q)
            assert len({weight(x, q) for x in orbit}) == 1
            labels[sig] = len(orbit)
            sizes[len(orbit)] += 1
            one_mass = len(orbit) * weight(z, q)
            mass_total += one_mass
            if q == 3:
                masses.append(one_mass)
            unseen.difference_update(orbit)
        t = q // 2 + 1
        n = (q - 1) // 2
        orbit_formula = comb(t + 2, 3) + comb(n + 2, 3)
        max_formula = 3 if q == 2 else 12 if q <= 4 else 24
        assert len(labels) == orbit_formula
        assert max(sizes) == max_formula
        assert mass_total == 2 ** (3 * q)
        rows.append({
            "q": q,
            "orbit_count": len(labels),
            "max_fiber": max(sizes),
            "repair_bits": (max(sizes) - 1).bit_length(),
            "size_distribution": dict(sorted(sizes.items())),
            "positive_source_mass": str(mass_total),
            "q3_orbit_masses": sorted(masses) if q == 3 else None,
        })
    assert rows[1]["q3_orbit_masses"] == [8, 72, 108, 108, 216]
    return {
        "id": "R762CJ",
        "status": "AUTHOR_CHECKED_NOT_REVIEWED",
        "model": "R762CI conditional K4 opposite-edge signed pair-area residue (D3)",
        "scope": "integer q=2..16, exhaustive all q^3 states and 24 S4 relabelings",
        "general_proof": "separate written combinatorial proof, not inferred from finite runs",
        "number_of_actions": len(ACTIONS),
        "orbit_formula": "C(floor(q/2)+3,3)+C(floor((q-1)/2)+2,3)",
        "max_orbit_formula": "3 if q=2; 12 if q=3 or 4; 24 if q>=5",
        "rows": rows,
    }

if __name__ == "__main__":
    result = json.dumps(verify(), indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if len(sys.argv) == 3 and sys.argv[1] == "--output":
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result, end="")
