#!/usr/bin/env python3
"""R762CW: exact standard-library checks of equivariant K3 flag lifts and path tapes."""
import itertools
import json
from collections import Counter
from math import factorial

AXES = tuple(range(1, 7))
SUPPORTS = tuple(itertools.combinations(AXES, 3))
FLAGS = tuple((s, k, a, b) for s in SUPPORTS for k in (1, 2)
              for a in s for b in s if b != a)
FLAG_SET = set(FLAGS)
PERMS = tuple(itertools.permutations(AXES))
MODES = ("ba", "bc", "ca", "cb")
assert len(SUPPORTS) == 20 and len(FLAGS) == 240 and len(PERMS) == 720

def third(s, a, b):
    return next(x for x in s if x not in (a, b))

def transform(flag, mode):
    s, k, a, b = flag
    c = third(s, a, b)
    aa, bb = {"ba": (b, a), "bc": (b, c),
              "ca": (c, a), "cb": (c, b)}[mode]
    return (s, k, aa, bb)

def permute(flag, perm):
    s, k, a, b = flag
    lookup = dict(zip(AXES, perm))
    return (tuple(sorted(lookup[x] for x in s)), k, lookup[a], lookup[b])

def signflip(flag):
    s, k, a, b = flag
    return (s, 3 - k, a, b)

cycle_distribution = {}
equivariance_assertions = 0
signflip_assertions = 0
for mode in MODES:
    mapping = {f: transform(f, mode) for f in FLAGS}
    assert set(mapping.values()) == FLAG_SET
    assert all(transform(signflip(f), mode) == signflip(mapping[f]) for f in FLAGS)
    signflip_assertions += len(FLAGS)
    periods = Counter()
    for f in FLAGS:
        x = f
        p = 0
        while True:
            x = mapping[x]
            p += 1
            if x == f:
                break
            assert p < 7
        periods[p] += 1
    cycle_distribution[mode] = dict(sorted(periods.items()))
    for perm in PERMS:
        for f in FLAGS:
            assert transform(permute(f, perm), mode) == permute(mapping[f], perm)
            equivariance_assertions += 1
    for s in SUPPORTS:
        for k in (1, 2):
            for a in s:
                images = {mapping[(s, k, a, b)][2] for b in s if b != a}
                assert images == set(s) - {a}

def target_counts(h):
    counts = [1, 0, 0]
    for _ in range(h):
        counts = [sum(counts[j] for j in range(3) if j != i) for i in range(3)]
    return counts

horizon_results = []
walk_assertions = 0
for h in range(13):
    total = 1 << h
    eps = -1 if h % 2 else 1
    assert (total + 2 * eps) % 3 == 0
    assert (total - eps) % 3 == 0
    diag = (total + 2 * eps) // 3
    off = (total - eps) // 3
    expected = [diag, off, off]
    assert target_counts(h) == expected
    assert diag + 2 * off == total
    if h:
        assert off % 2 == 1
    counts = Counter()
    def visit(v, depth):
        if depth == h:
            counts[v] += 1
            return
        for w in range(3):
            if w != v:
                visit(w, depth + 1)
    visit(0, 0)
    for j in range(3):
        assert counts[j] == expected[j]
        walk_assertions += 1
    horizon_results.append({"h": h, "total": total,
                            "diag": diag, "offdiag_each": off})

assert cycle_distribution == {"ba": {2: 240}, "bc": {3: 240},
                              "ca": {3: 240}, "cb": {2: 240}}
print(json.dumps({
    "schema": "EM_R762CW_EXACT_CHECK_V1",
    "base_mixed_triads": 120,
    "marked_flags": len(FLAGS),
    "supports": len(SUPPORTS),
    "group_order": factorial(6),
    "signflip_assertions": signflip_assertions,
    "equivariance_assertions": equivariance_assertions,
    "path_word_endpoint_assertions": walk_assertions,
    "flag_map_cycle_period_counts": cycle_distribution,
    "horizons": horizon_results,
    "independent_review": "NOT_REVIEWED",
    "candidate_not_native_license": True
}, ensure_ascii=False, sort_keys=True, indent=2))
