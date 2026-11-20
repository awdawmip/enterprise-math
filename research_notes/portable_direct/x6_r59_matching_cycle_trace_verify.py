#!/usr/bin/env python3
"""X6 R59 exact positive-BRC branch-chain verification, no external dependencies.
Observer: k independent reset AB trials; each pair is a successful branch;
cross-trial cyclic equalities B(t).port = A(t+1).port.
The 0/1 arrays count paths; no physical or signed-amplitude propagation.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations

def multiply(a, b):
    n = len(a)
    return [[sum(a[i][t]*b[t][j] for t in range(n))
             for j in range(n)] for i in range(n)]

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def trace(a):
    return sum(a[i][i] for i in range(len(a)))

def cycles(perm):
    visited = set()
    out = Counter()
    for start in range(len(perm)):
        if start in visited:
            continue
        node = start
        length = 0
        while node not in visited:
            visited.add(node)
            node = perm[node]
            length += 1
        out[length] += 1
    return dict(out)

counts = {}
for p in range(1, 8):
    cnt = 0
    for perm in permutations(range(p)):
        # Each S[i][j] is one explicit positive BRC branch when permitted.
        success = [[int(j != perm[i]) for j in range(p)] for i in range(p)]
        matching = [[int(j == perm[i]) for j in range(p)] for i in range(p)]
        sc = identity(p)
        mc = identity(p)
        f = [0] * (p + 1)
        u, v = Fraction(2), Fraction(3)
        U, V = p*u, p*v
        T = p*(p-1)*u*v
        assert Fraction(U*V, U*V-T) == p
        assert Fraction(U*V, p*p) == u*v
        for k in range(1, p+1):
            # Independently accumulate named closed positive paths.
            sc = multiply(sc, success)
            mc = multiply(mc, matching)
            Lk = trace(sc)
            fk_direct = trace(mc)
            fk_recovered = 1 + (-1)**k*(Lk-(p-1)**k)
            assert fk_direct == fk_recovered
            f[k] = fk_recovered
        reconstructed = {}
        for n in range(1, p+1):
            value = f[n]-sum(d*reconstructed[d] for d in range(1, n) if n%d == 0)
            assert value%n == 0
            reconstructed[n] = value//n
        assert {n: c for n, c in reconstructed.items() if c} == cycles(perm)
        cnt += 1
    counts[p] = cnt

def l2(perm):
    p = len(perm)
    s = [[int(j != perm[i]) for j in range(p)] for i in range(p)]
    return trace(multiply(s, s))

assert l2((1, 2, 3, 0)) == 8
assert l2((1, 0, 3, 2)) == 12
assert sum(counts.values()) == 5913
print({"status": "PASS", "permutation_matchings_by_p": counts,
       "total": sum(counts.values()),
       "p4_l2_4cycle": 8, "p4_l2_two_2cycles": 12})
