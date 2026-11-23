#!/usr/bin/env python3
"""Exact finite-field witness for frozen R5 primitive order 61.

Characteristic-zero zeros and 122-periodicity are proved in RESEARCH.md.
A finite-field zero is not itself a characteristic-zero zero certificate.
"""
from itertools import permutations
from hashlib import sha256
from math import prod

P, ROOT, D = 367, 47, 61
PERIOD = 2 * D
N = 2 * PERIOD + 1
assert all(P % k for k in range(2, int(P ** .5) + 1))
assert pow(ROOT, D, P) == 1 and ROOT != 1

def q(n):
    return pow(ROOT, n % D, P)

def inv(v):
    return pow(v % P, P - 2, P)

def union_a():
    alpha, beta = q(214), q(215)
    gamma = [q(j) for j in (219, 220, 221)]
    K = prod((1-q(j)) % P for j in range(214, 222)) % P
    acc = [0] * N
    priority = {'a': 0, 'b': 1, 'd': 2}
    for j, z in enumerate(gamma):
        kappa = z*z % P
        for k, other in enumerate(gamma):
            if k != j:
                kappa = kappa * inv(z - other) % P
        v = {'a': alpha, 'b': beta, 'd': z}
        for top, mid, bottom in permutations('abd'):
            e1 = int(priority[top] > priority[mid])
            e2 = int(priority[mid] > priority[bottom])
            u = v[top]*v[mid] % P
            w = u*v[bottom] % P
            scalar = kappa * pow(v[top], e1, P) * pow(u, e2, P) * inv(1-v[top]) % P
            # Series for 1/((1-ut)(1-wt^2)): recurrence of its cubic denominator.
            series = [0] * N
            series[0] = 1
            for k in range(1, N):
                series[k] = (u * series[k-1] + (w * series[k-2] if k >= 2 else 0)
                             - (u * w * series[k-3] if k >= 3 else 0)) % P
            # Exact multiplication by three c-group factors 1/(1-q(price)*t).
            for pp in (216, 217, 218):
                t = q(pp)
                for k in range(1, N):
                    series[k] = (series[k] + t*series[k-1]) % P
            prefix = 0
            for m in range(1+e2, N):
                prefix = (prefix + series[m-1-e2]) % P
                acc[m] = (acc[m] + scalar * prefix) % P
    return [K * x % P for x in acc]

def block_factor(prices):
    return prod((1-q(j)) % P for j in prices) % P

# Pole residue classes: z^r and -z^r as detailed in RESEARCH.md.
c_group = {(-j) % D for j in (216,217,218)}
pairs = {(-(x+y)) % D for x in (214,215) for y in (219,220,221)}
pairs.add((-214-215) % D)
triples = {(-(214+215+j) * pow(2, -1, D)) % D for j in (219,220,221)}
assert (c_group,pairs,triples) == ({26,27,28},{52,53,54,55,59},{11,41,42})
assert len({0} | c_group | pairs | triples) == 12
assert len(triples) == 3 and P % D == 1

A = union_a()
# B_m(z)=C_m(z)=0 since 61|244 (S3), 61|305 (S4); R_m(z)=A_m(z).
assert 244 % D == 0 and 305 % D == 0
assert all(A[i] == A[i+PERIOD] for i in range(N-PERIOD))

# Independent m=1 check by actual three-event inclusion-exclusion.
s0 = list(range(214,219))
s1 = [214] + list(range(216,222))
s2 = [215] + list(range(216,222))
assert A[1] == (block_factor(s0)+block_factor(s1)+block_factor(s2)
                -2*block_factor(range(214,222))) % P
assert [m for m in range(1, PERIOD+1) if A[m] == 0] == list(range(118,123))

csv = 'm,R_mod367\n' + ''.join(f'{m},{A[m]}\n' for m in range(1, PERIOD+1))
print('d=61 p=367 primitive root=47; exact finite-field recurrence PASS')
print('pole residue classes (+):',sorted({0}|c_group|pairs|triples))
print('nonzero residues: 117/117 in m=1..117')
print('zero residues (modular observation):',list(range(118,123)))
print('R1=',A[1],'R53=',A[53],'R61=',A[61],'R117=',A[117],'R123=',A[123])
print('sha256 of 122-row CSV:',sha256(csv.encode()).hexdigest())
print(csv,end='')
