#!/usr/bin/env python3
"""Independent exact integer enumeration of the R5 six-cone t-pole envelope.
Scope: frozen 214..314, three joint U events, primitive d in ORDERS.
No root-of-unity numerical approximation; uses congruences modulo 2d.
"""
from itertools import permutations
from collections import Counter

ORDERS = (7,9,11,13,16,17,19,23,25,27,31,37)
EXPECTED = (3,3,3,3,2,2,2,1,2,3,3,2)

def compute(d):
    maximum = 0
    witnesses = []
    profile = Counter()
    for r in (219,220,221):
        for a,b,c in permutations((214,215,r)):
            for j in range(2*d):
                lin = tuple(n for n in (0,216,217,218,a+b)
                            if (j+2*n) % (2*d) == 0)
                quad = (j+214+215+r) % d == 0
                mult = len(lin) + int(quad)
                profile[mult] += 1
                if mult > maximum:
                    maximum = mult
                    witnesses = [(r,a,b,c,j,lin,quad)]
                elif mult == maximum:
                    witnesses.append((r,a,b,c,j,lin,quad))
    return maximum,witnesses,profile

if __name__ == "__main__":
    print("R5 six-cone upper pole envelope at primitive roots")
    for d,expected in zip(ORDERS,EXPECTED):
        maximum,witnesses,profile = compute(d)
        assert maximum == expected,(d,maximum,expected)
        r,a,b,c,j,lin,quad = witnesses[0]
        print(f"d={d:>2} mu={maximum} terms={sum(profile.values())} "
              f"maximizers={len(witnesses)} witness=(r={r},perm={a},{b},{c},"
              f"j={j},linear={lin},quadratic={int(quad)})")
    for d in ORDERS:
        if d in (7,27,31):
            common = 217 if d in (7,31) else 216
            assert common % d == 0
            assert all(p % d != 0 for p in (214,215,219,220,221))
    print("PASS 12/12 pole envelopes and three common-factor jet reductions")
