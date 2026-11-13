#!/usr/bin/env python3
"""R754 exact finite S6-C3 framed triadic BRC observer checker; stdlib only."""
from itertools import combinations, permutations, product
from collections import Counter
import json

N = 6
AX = tuple(range(N))
SIGNS = (-1, 1)

def rotations(x):
    return [x[k:] + x[:k] for k in range(3)]

def canon(x):
    return min(rotations(tuple(x)))

def states():
    ans = set()
    for axes in combinations(AX, 3):
        for signs in product(SIGNS, repeat=3):
            t = tuple(zip(axes, signs))
            ans.add(canon(t))
            ans.add(canon((t[0], t[2], t[1])))
    return sorted(ans)

def apply(x, g):
    return tuple((g[axis], sign) for axis, sign in x)

def compose(h, g):
    return tuple(h[g[i]] for i in AX)

def edges(x):
    return frozenset((x[i], x[(i+1)%3]) for i in range(3))

def minority_root(x):
    counts = Counter(sign for _, sign in x)
    if len(counts) != 2:
        return None
    unique_sign = next(s for s, n in counts.items() if n == 1)
    k = next(k for k, p in enumerate(x) if p[1] == unique_sign)
    return rotations(x)[k]

def main():
    X = states()
    ix = {x:i for i,x in enumerate(X)}
    G = list(permutations(AX))
    ig = {g:i for i,g in enumerate(G)}
    assert len(X) == 320 and len(G) == 720
    root_count = sum(len(rotations(x)) for x in X)
    assert root_count == 960
    rows = []
    phases = []
    for g in G:
        newids = []
        ks = []
        for x in X:
            moved = apply(x,g)
            j = ix[canon(moved)]
            k = rotations(X[j]).index(moved)
            newids.append(j)
            ks.append(k)
            assert edges(moved) == frozenset((apply((a,),g)[0], apply((b,),g)[0]) for a,b in edges(x))
        rows.append(newids)
        phases.append(ks)
    generators = []
    for i in range(N-1):
        h = list(AX)
        h[i],h[i+1] = h[i+1],h[i]
        generators.append(ig[tuple(h)])
    comparisons = 0
    for gi,g in enumerate(G):
        for hi in generators:
            h = G[hi]
            hgi = ig[compose(h,g)]
            for xi in range(len(X)):
                gx = rows[gi][xi]
                assert rows[hgi][xi] == rows[hi][gx]
                assert phases[hgi][xi] == (phases[gi][xi] + phases[hi][gx])%3
                comparisons += 1
    assert comparisons == 1152000
    hom = [i for i,x in enumerate(X) if len(set(s for _,s in x)) == 1]
    mix = [i for i in range(len(X)) if i not in set(hom)]
    assert len(hom) == 80 and len(mix) == 240
    assert all(minority_root(X[i]) is None for i in hom)
    assert all(minority_root(X[i]) in rotations(X[i]) for i in mix)
    for g in G:
        for i in mix:
            x = X[i]
            assert minority_root(apply(x,g)) == apply(minority_root(x),g)
    hist_all = Counter()
    hist_hom = Counter()
    hist_mix = Counter()
    for gi in range(len(G)):
        for xi in range(len(X)):
            if rows[gi][xi] == xi:
                k = phases[gi][xi]
                hist_all[k] += 1
                (hist_hom if xi in hom else hist_mix)[k] += 1
    assert hist_hom == Counter({0:480, 1:480, 2:480})
    assert hist_mix == Counter({0:1440})
    assert hist_all == Counter({0:1920, 1:480, 2:480})
    x = canon(((0,1),(1,1),(2,1)))
    gi = ig[(1,2,0,3,4,5)]
    xi = ix[x]
    assert rows[gi][xi] == xi and phases[gi][xi] == 1
    out = {
      "checker": "R754_X6_CYCLIC_FRAME_COCYCLE_EXACT_PASS",
      "domain": "unmarked oriented signed triads on six axes with S6 relabeling",
      "state_count": len(X),
      "marked_root_count": root_count,
      "axis_permutations": len(G),
      "all_action_and_phase_checks": len(G)*len(X),
      "cocycle_generator_comparisons": comparisons,
      "homogeneous_sign_states": len(hom),
      "mixed_sign_states": len(mix),
      "homogeneous_stabilizer_phase_histogram": dict(sorted(hist_hom.items())),
      "mixed_stabilizer_phase_histogram": dict(sorted(hist_mix.items())),
      "total_stabilizer_phase_histogram": dict(sorted(hist_all.items())),
      "witness": {
        "x": [list(y) for y in x], "g": [1,2,0,3,4,5],
        "g_x_equals_x": True, "root_shift_mod3": 1
      },
      "scope_note": "S6 action-groupoid root cocycle, not native V39 physical based-loop h"
    }
    print(out["checker"])
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
    return out

if __name__ == "__main__":
    main()
