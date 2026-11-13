#!/usr/bin/env python3
"""Exact finite classification of all 16 F7 A6 split permutations; algebraic regression.

Author-side exposed context only: this is not a native Result or Driver review.
"""
from collections import Counter
from itertools import permutations, product
from math import prod

N = 4
ID = tuple(range(N))
D = ((1, 1, 0, 0), (1, -1, 0, 0),
     (0, 0, 1, 1), (0, 0, 1, -1))
E = (1, 0, 0, 0)


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(N))
                       for j in range(N)) for i in range(N))


def mv(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(N)) for i in range(N))


def mpow(a, n):
    out = tuple(tuple(int(i == j) for j in range(N)) for i in range(N))
    for _ in range(n):
        out = mm(out, a)
    return out


def ppow(p, n):
    out = ID
    for _ in range(n):
        out = tuple(p[out[i]] for i in range(N))
    return out


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(N) for j in range(i+1, N))


def det4(a):
    return sum(parity(s)*prod(a[i][s[i]] for i in range(N))
               for s in permutations(range(N)))


def weighted_perm(p, ks):
    return tuple(tuple(ks[j] if p[j] == i else 0 for j in range(N))
                 for i in range(N))


def balance_slots(w):
    u = mv(D, w)
    return tuple(sum(u[j] != 0 for j in range(i, i+2)) for i in (0, 2))


def scalar_twice(w):
    return sum(balance_slots(w))


def main():
    selected = [p for p in permutations(ID) if p[0]//2 != p[1]//2]
    assert len(selected) == 16
    profiles = Counter()
    for p in selected:
        period = next(n for n in range(1, 13) if ppow(p, n) == ID)
        seq = ''.join('B' if ppow(p, n)[0]//2 != ppow(p, n)[1]//2 else 'U'
                      for n in range(period))
        first_loss = next(n for n in range(2, period+1)
                          if ppow(p, n)[0]//2 == ppow(p, n)[1]//2)
        profiles[(period, seq, first_loss)] += 1
    assert profiles == Counter({(2, 'UB', 2): 4,
                                (3, 'UBB', 3): 8,
                                (4, 'UBUB', 2): 4})
    identity = mpow(D, 0)
    checks = 0
    all_k = tuple(product((-2, -1, 1, 2), repeat=4))
    for p in selected:
        for ks in all_k:
            B = weighted_perm(p, ks)
            A = mm(mm(D, B), D)
            assert det4(A) == 16*parity(p)*prod(ks)
            ap = identity
            bp = identity
            for n in range(7):
                lhs = mm(D, ap)
                rhs = mm(bp, D)
                assert all(lhs[i][j] == (2**n)*rhs[i][j]
                           for i in range(N) for j in range(N))
                assert balance_slots(mv(ap, E)) == (
                    (1, 1) if ppow(p, n)[0]//2 != ppow(p, n)[1]//2 else
                    ((2, 0) if ppow(p, n)[0]//2 == 0 else (0, 2)))
                ap = mm(ap, A)
                bp = mm(bp, B)
                checks += 1
    scalar_cases = 0
    for p in selected:
        for ks in ((1, 1, 1, 1), (-1, 2, -2, 3), (2, 3, 5, 7)):
            A = mm(mm(D, weighted_perm(p, ks)), D)
            for n in range(7):
                an = mpow(A, n)
                for z in product((-1, 0, 1), repeat=4):
                    assert scalar_twice(mv(an, z)) == scalar_twice(z)
                    scalar_cases += 1
    result = {
        'splitting_permutations': len(selected),
        'profiles': {f'order_{o}_{s}_first_loss_{f}': c for (o,s,f),c in sorted(profiles.items())},
        'nonzero_k_vectors': len(all_k),
        'matrix_power_identity_checks': checks,
        'scalar_regression_cases': scalar_cases,
        'verdict': 'ALL_PASS',
        'proof_boundary': 'all-permutation classification exhaustive; integer-multiplier universal formula algebraic',
    }
    import json
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
