#!/usr/bin/env python3
"""Independent finite-field witness for the frozen R5 41st-root threshold sequence.

All operations are exact in F_p. The all-m periodicity and characteristic-zero
vanishing are proved separately in RESEARCH.md; modular zero never proves
characteristic-zero zero. The code verifies nonzero for all other 77 residues.
"""
from itertools import permutations
from hashlib import sha256
from math import prod

P, ROOT = 821, 28
PERIOD = 82
N = 2 * PERIOD + 1
assert all(P % d for d in range(2, int(P ** .5) + 1))
assert pow(ROOT, 41, P) == 1 and ROOT != 1


def inv(x):
    return pow(x % P, P - 2, P)


def q(n):
    return pow(ROOT, n % 41, P)


def mul(a, b):
    out = [0] * N
    for i, x in enumerate(a):
        if x:
            for j in range(N - i):
                out[i + j] = (out[i + j] + x * b[j]) % P
    return out


def geom(x):
    ans = [1] * N
    for j in range(1, N):
        ans[j] = ans[j - 1] * x % P
    return ans


def group_series(prices):
    h = [1] + [0] * (N - 1)
    for price in prices:
        h = mul(h, geom(q(price)))
    return h


def first_three_union():
    alpha, beta = q(214), q(215)
    gamma = [q(x) for x in (219, 220, 221)]
    h = group_series(range(216, 219))
    D = prod(1 - q(x) for x in range(214, 222)) % P
    ans = [0] * N
    priority = {'a': 0, 'b': 1, 'd': 2}
    for j, z in enumerate(gamma):
        kappa = z*z % P
        for k, other in enumerate(gamma):
            if k != j:
                kappa = kappa * inv(z - other) % P
        v = {'a': alpha, 'b': beta, 'd': z}
        for top, middle, bottom in permutations(('a','b','d')):
            delta1 = int(priority[top] > priority[middle])
            delta2 = int(priority[middle] > priority[bottom])
            u = v[top] * v[middle] % P
            w = u * v[bottom] % P
            scalar = (kappa * pow(v[top],delta1,P)
                      * pow(u,delta2,P) * inv(1-v[top])) % P
            series = [0] * N
            for k in range(N):
                for ell in range(k//2+1):
                    series[k] = (series[k] + pow(u,k-2*ell,P)
                                 * pow(w,ell,P)) % P
            hs = mul(h,series)
            prefix = 0
            for m in range(1+delta2,N):
                prefix = (prefix + hs[m-1-delta2]) % P
                ans[m] = (ans[m] + scalar * prefix) % P
    return [x*D % P for x in ans]


def last_group():
    h = group_series(range(296,313))
    D = prod(1-q(x) for x in range(296,313)) % P
    ans = [0]*N
    s = 0
    for m in range(1,N):
        s = (s+h[m-1])%P
        ans[m] = s*D%P
    return ans


A = first_three_union()
C = last_group()
R = [(a+c-a*c)%P for a,c in zip(A,C)]
assert all(A[i] == A[i+82] for i in range(83))
assert all(C[i] == C[i+41] for i in range(N-41))
assert all(R[i] == R[i+82] for i in range(83))
zero = [m for m in range(1,83) if R[m] == 0]
assert zero == [78,79,80,81,82], zero
assert R[9] == 66 and R[50] == 130
assert R[83] == R[1] and R[119] == R[37]
csv = 'm,R_mod821\n' + ''.join(f'{m},{R[m]}\n' for m in range(1,83))
print('p=821, primitive41 root=28; A, C, R exact modular recurrence PASS')
print('R zero residues in [1,82]:',zero)
print('nonzero residues:', 82-len(zero))
print('R9=',R[9],'R50=',R[50], 'R83=',R[83], 'R119=', R[119])
print('sha256 of R residue CSV:', sha256(csv.encode()).hexdigest())
print(csv, end='')
