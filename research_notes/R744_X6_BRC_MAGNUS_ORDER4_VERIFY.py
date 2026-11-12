#!/usr/bin/env python3
"""R744 exact integral BRC path-branch observer; no native force dynamics."""
from itertools import permutations
from collections import defaultdict
from json import dumps

D = 4

def mul(A, B):
    C = defaultdict(int)
    for a, av in A.items():
        for b, bv in B.items():
            if len(a) + len(b) <= D:
                C[a+b] += av*bv
    return {a: v for a, v in C.items() if v}

def gen(i, sign):
    if sign == 1:
        return {(): 1, (i,): 1}
    return {tuple([i]*k): (-1)**k for k in range(D+1)}

def signature(path):
    value = {(): 1}
    for i, sign in path:
        value = mul(value, gen(i, sign))
    return value

def branch(p):
    c = [(i, 1) for i in p]
    L = [(4,1), (5,1), (4,-1), (5,-1)]
    return c + L + [(i, -1) for i in reversed(p)]

def current(path):
    cell = [0]*6
    edges = defaultdict(int)
    for axis, sign in path:
        if sign == 1:
            edges[(tuple(cell), axis)] += 1
            cell[axis] += 1
        else:
            cell[axis] -= 1
            edges[(tuple(cell), axis)] -= 1
    assert cell == [0]*6
    return tuple(sorted((k,v) for k,v in edges.items() if v))

def test():
    report = {}
    for r in range(1,5):
        pset = list(permutations(range(r)))
        signatures = [signature(branch(p)) for p in pset]
        low = [tuple(sorted((w,c) for w,c in s.items() if len(w) <= 3))
               for s in signatures]
        exact = [tuple(sorted(s.items())) for s in signatures]
        assert len(set(low)) == 1
        assert len(set(exact)) == len(pset)
        assert len({current(branch(p)) for p in pset}) == 1
        for p, s in zip(pset, signatures):
            for i in range(r):
                for j in range(r):
                    if i != j:
                        assert s.get((i,j,4,5),0) == int(p.index(i) < p.index(j))
        report[r] = {
            "branches": len(pset),
            "low_order_classes": len(set(low)),
            "degree4_classes": len(set(exact)),
            "current_classes": 1,
            "ordered_pair_coefficient_checks": len(pset)*r*(r-1)
        }
    base = {p: signature(branch(p)) for p in permutations(range(4))}
    for k in range(5):
        f = {i: i for i in range(6)}
        f[k], f[k+1] = f[k+1], f[k]
        for p,s in base.items():
            moved_path = [(f[i], sign) for i, sign in branch(p)]
            moved_signature = {tuple(f[i] for i in word): v
                               for word,v in s.items()}
            assert signature(moved_path) == moved_signature
    return {
        "verification": "R744_X6_BRC_MAGNUS_ORDER4_EXACT_PASS",
        "arithmetic": "integer free-associative ring, words degree <=4",
        "r_cases": report,
        "S6_adjacent_generator_relabel_tests": 120,
        "model": "one positively counted BRC label per branch; signed algebraic observer",
        "native_physical_update": "NOT_EXECUTED"
    }

if __name__ == "__main__":
    print(dumps(test(), ensure_ascii=False, indent=2))
