#!/usr/bin/env python3
"""R749SPV: exact source-multiset codec for the frozen R749SPR Walsh center polytope.
Standard library, integer arithmetic; finite exhaustive checks of levels 2..5.
This is an author check, not independent review or native X6 validation.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
from math import comb
import json

FACETS = (
    ((-1, -1, -1), -2), ((-1, -1, 1), -2),
    ((-1, 1, -1), -2), ((-1, 1, 1), -2),
    ((1, -1, -1), -2), ((1, -1, 1), -4),
    ((1, 1, -1), -4), ((1, 1, 1), -2),
)
ANCHORS = ((-2, -1, 1), (-2, 0, 0), (-1, -2, 1), (-1, -1, 1))

def within(x, n=1):
    return all(sum(m[i]*x[i] for i in range(3)) >= n*c for m, c in FACETS)

def points(n=1):
    return {x for x in product(range(-2*n, 2*n + 1), repeat=3) if within(x, n)}

def plus(a, b):
    return tuple(a[i]+b[i] for i in range(3))

def target_sum(ids, alphabet):
    return tuple(sum(alphabet[i][j] for i in ids) for j in range(3))

def recover(n, x, residual, alphabet, anchor_ids):
    """Reconstruct all 26 nonnegative counts or reject an invalid 22-count residual.

    Residual entries are the nonanchor multiplicities in fixed sorted alphabet order.
    Derivation: remaining (N,H,U,V) is represented using four unimodular anchors.
    """
    assert len(residual) == 22 and len(alphabet) == 26
    nonanchors = tuple(i for i in range(26) if i not in anchor_ids)
    N = n - sum(residual)
    H, U, V = (x[j]-sum(residual[k]*alphabet[i][j]
                   for k, i in enumerate(nonanchors)) for j in range(3))
    ac = (-H + V - 2*N, N-V, -U-V, 2*N + H + U + V)
    counts = [0]*26
    for i, c in zip(nonanchors, residual):
        counts[i] = c
    for i, c in zip(anchor_ids, ac):
        counts[i] = c
    if min(counts) < 0 or sum(counts) != n:
        return None
    if tuple(sum(counts[i]*alphabet[i][j] for i in range(26)) for j in range(3)) != x:
        return None
    return tuple(counts)

p = tuple(sorted(points()))
assert len(p) == 33
f2 = defaultdict(list)
for i, j in combinations_with_replacement(range(33), 2):
    f2[plus(p[i], p[j])].append((p[i], p[j]))
forced = frozenset(a for pairs in f2.values() if len(pairs)==1 for pair in pairs for a in pair)
assert len(forced)==25 and len(f2)==179
assert all(b in forced for b in ANCHORS)

results = []
for extra in ((0,0,0), (-1,0,0)):
    alphabet = tuple(sorted(forced | {extra}))
    assert len(alphabet)==26
    anchor_ids = tuple(alphabet.index(a) for a in ANCHORS)
    nonanchors = tuple(i for i in range(26) if i not in anchor_ids)
    observations = []
    for n in range(2,6):
        fibers = Counter()
        tested = 0
        for ids in combinations_with_replacement(range(26), n):
            counts = [0]*26
            for i in ids:
                counts[i] += 1
            x = target_sum(ids, alphabet)
            encoded = tuple(counts[i] for i in nonanchors)
            decoded = recover(n, x, encoded, alphabet, anchor_ids)
            assert decoded == tuple(counts), (n, ids, x)
            fibers[x] += 1
            tested += 1
        expected = (46*n**3 + 33*n**2 + 17*n + 3)//3
        assert tested == comb(n+25,25) and len(fibers)==expected
        observations.append({
            'n': n,
            'source_multisets': tested,
            'distinct_readouts': len(fibers),
            'max_fiber': max(fibers.values()),
            'unique_readouts': sum(v==1 for v in fibers.values()),
        })
    results.append({'extra_letter':extra, 'anchors':ANCHORS,
                    'anchor_indices':anchor_ids, 'nonanchor_indices':nonanchors,
                    'levels':observations})

print(json.dumps({'status':'PASS', 'unit':'R749SPV',
    'claim':'Each 26-letter minimum universal alphabet has a determinant -1 common four-anchor block; 22 nonanchor counts and (n,H,U,V) give a lossless exact integer provenance codec.',
    'four_anchor_matrix_det': -1,
    'scale_coordinate_convention':'n,H,U,V are integer total count and summed scaled H,U,V',
    'inverse_anchor_counts': {
        'c0':'-H+V-2*N', 'c1':'N-V',
        'c2':'-U-V','c3':'2*N+H+U+V',
        'N':'n-sum(nonanchor_counts)',
        '(H,U,V)':'X-sum(nonanchor_count * source_vector)'},
    'tested_levels':'2..5 exhaustive source-multiset enumeration for each alphabet',
    'numeric_mode':'exact Python integers', 'alphabets':results,
    'review':'AUTHOR_EXACT_NOT_REVIEWED',
    'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'dependencies':['R749SPR complete K','R749SPU minimal alphabets and Theta(n^22) bound']
}, sort_keys=True, indent=2, ensure_ascii=False))
