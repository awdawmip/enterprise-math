#!/usr/bin/env python3
"""R762Q exact certificate for temporal marginal observability on 3 signed sources."""
from itertools import product, permutations
import json

N = 3
NLAWS = 1 << (1 << N)

def parity(x):
    return x.bit_count() & 1

def maps(rows, b):
    return [sum((parity(rows[i] & s) ^ ((b >> i) & 1)) << i for i in range(N))
            for s in range(1 << N)]

def image(law, u):
    out = 0
    for s, t in enumerate(u):
        out |= ((law >> s) & 1) << t
    return out

def marginals(law):
    return tuple(((law >> s) & 1) + ((law >> (s | (1 << j))) & 1)
                 for j in range(N) for s in range(1 << N) if not s & (1 << j))

original = [marginals(a) for a in range(NLAWS)]
assert len(set(original)) == 255
by_sig = {}
for a, o in enumerate(original):
    by_sig.setdefault(o, []).append(a)
ambiguous = [v for v in by_sig.values() if len(v) > 1]
even = sum((parity(s) == 0) << s for s in range(1 << N))
odd = even ^ ((1 << (1 << N)) - 1)
assert ambiguous == [[min(even, odd), max(even, odd)]]

invertible = []
for rows in product(range(8), repeat=3):
    u = maps(rows, 0)
    if len(set(u)) == 8:
        invertible.append(rows)
assert len(invertible) == 168

stats = {"preserving": 0, "revealing": 0, "affine_checked": 0,
         "distinct_joint_signature_count": {"255": 0, "256": 0}}
for rows in invertible:
    preserve = all(parity(sum(((r >> j) & 1) << i for i, r in enumerate(rows))) == 1 for j in range(N))
    assert preserve == all(sum((r >> j) & 1 for r in rows) % 2 == 1 for j in range(N))
    for b in range(8):
        u = maps(rows, b)
        signatures = set()
        for a in range(NLAWS):
            signatures.add((original[a], marginals(image(a, u))))
        count = len(signatures)
        assert count == (255 if preserve else 256), (rows, b, count)
        eq = marginals(image(even, u)) == marginals(image(odd, u))
        assert eq == preserve
        stats["preserving" if preserve else "revealing"] += 1
        stats["affine_checked"] += 1
        stats["distinct_joint_signature_count"][str(count)] += 1

assert stats["preserving"] == 192
assert stats["revealing"] == 1152
assert stats["affine_checked"] == 1344

cnot = (0b011, 0b010, 0b100)
u = maps(cnot, 0)
observed_even = marginals(image(even, u))
observed_odd = marginals(image(odd, u))
assert observed_even != observed_odd
assert set(observed_even[4:8]) == {0, 2}
assert all(x == 1 for x in observed_even[:4] + observed_even[8:])
assert all(x + y == 2 for x, y in zip(observed_even, observed_odd))

perm_roots = set()
for perm in permutations(range(3)):
    rows = tuple(1 << k for k in perm)
    for b in range(8):
        perm_roots.add((rows, b))
assert len(perm_roots) == 48
assert all(sum((r >> j) & 1 for r in rows) % 2 == 1 for rows, _ in perm_roots for j in range(3))

result = {
    "schema": "R762Q_TEMPORAL_BRC_OBSERVABILITY_V1",
    "science_scope": "three named sign bits and affine GF(2)^3 candidate updates; no native TRIADIC_CLOSURE_E event is asserted",
    "law_count": NLAWS, "one_time_distinct_signatures": 255,
    "ambiguous_laws": [even, odd],
    "GL3_F2_order": len(invertible),
    "AGL3_F2_order": stats["affine_checked"],
    "affine_parity_preserving": stats["preserving"],
    "affine_parity_revealing": stats["revealing"],
    "signed_permutation_affine_subgroup_order": 48,
    "joint_signature_counts": stats["distinct_joint_signature_count"],
    "explicit_CNOT_rows": list(cnot),
    "explicit_CNOT_after_even_marginals": list(observed_even),
    "explicit_CNOT_after_odd_marginals": list(observed_odd),
    "method": "exhaustive 168 invertible matrices, 8 translations, 256 laws per map; exact integer assertions",
    "outcome": "PASS"
}
print(json.dumps(result, ensure_ascii=False, indent=2))
