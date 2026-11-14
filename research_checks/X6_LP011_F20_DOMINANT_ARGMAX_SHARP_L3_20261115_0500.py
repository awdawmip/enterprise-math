#!/usr/bin/env python3
"""Exact signed-X6 LP011 dominant-axis observer certificate (stdlib only).

Frozen science: P000 V5 @59538f585d037d09ef687b28715c4bc1a3f9fe03.
All-twenty-triple F is a derived observer, not native Cell identity.
"""
from itertools import combinations, product
from math import factorial

AXES = range(6)
TRIPLES = tuple(combinations(AXES, 3))

def shell_mass(n, k=6):
    if k == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for tail in shell_mass(n - a, k - 1):
                yield (a,) + tail

def shell(n):
    for counts in shell_mass(n):
        active = tuple(i for i, v in enumerate(counts) if v)
        for signs in product((-1, 1), repeat=len(active)):
            v = list(counts)
            for i, sign in zip(active, signs):
                v[i] *= sign
            yield tuple(v)

def F(z):
    return tuple(
        tuple(z[i] - min(z[j] for j in t) for i in t)
        for t in TRIPLES
    )

def L(z):
    return sum(abs(x) for x in z)

def G(z):
    return sum(x * x for x in z)

def B(z):
    return factorial(L(z)) // __import__("math").prod(factorial(abs(x)) for x in z)

def D(z):
    m = max(abs(x) for x in z)
    return tuple(i for i, x in enumerate(z) if abs(x) == m)

def predicted_D(z):
    h = min(z)
    a = tuple(x - h for x in z)
    M = max(a)
    if M == 0:
        return tuple(AXES)
    if 2 * h + M > 0:
        return tuple(i for i, x in enumerate(a) if x == M)
    if 2 * h + M < 0:
        return tuple(i for i, x in enumerate(a) if x == 0)
    return tuple(i for i, x in enumerate(a) if x == 0 or x == M)

def main():
    counts = []
    collision_fibres = []
    for n in range(4):
        groups = {}
        endpoints = tuple(shell(n))
        for z in endpoints:
            assert L(z) == n
            assert predicted_D(z) == D(z)
            groups.setdefault((F(z), L(z), G(z)), []).append(z)
        ambiguous = [g for g in groups.values() if len({D(z) for z in g}) > 1]
        if n < 3:
            assert len(ambiguous) == 0
            assert all(len(g) == 1 for g in groups.values())
        else:
            assert len(ambiguous) == 20
            assert len(groups) == 272
            for g in ambiguous:
                assert len(g) == 2
                z, w = g
                assert G(z) == G(w) == 3
                assert B(z) == B(w) == 6
                assert set(D(z)).isdisjoint(set(D(w)))
                assert set(D(z)) | set(D(w)) == set(AXES)
                assert sorted(x-y for x,y in zip(z,w)) in [[-1]*6,[1]*6]
            collision_fibres = ambiguous
        counts.append((n, len(endpoints), len(groups), len(ambiguous)))
    for t in range(1, 13):
        z = (0,t,t,t,0,0)
        w = (-t,0,0,0,-t,-t)
        assert F(z) == F(w)
        assert L(z) == L(w) == 3*t
        assert G(z) == G(w) == 3*t*t
        assert B(z) == B(w) == factorial(3*t)//factorial(t)**3
        assert D(z) == (1,2,3)
        assert D(w) == (0,4,5)
    print("PASS_X6_LP011_F20_DOMINANT_ARGMAX_SHARP_L3")
    print("n, endpoint_count, F_L_G_fibre_count, ambiguous_argmax_fibres =", counts)
    print("integer scaling family tested t=1..12; certified 20 sharp length-3 fibres")

if __name__ == "__main__":
    main()
