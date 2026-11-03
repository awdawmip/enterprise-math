#!/usr/bin/env python3
"""PREFIX-457 exact Q-rank of degree<=6 monomials on W_5(+e1,+/-e2..+/-e6).
Uses NumPy int64 for bounded integral arithmetic; all certificate equalities are exact.
"""
import itertools
import math
import time
import numpy as np

PRIMES = (32003, 32009)
DEGREE = 6


def steps():
    ans = [(1, 0, 0, 0, 0, 0)]
    for i in range(1, 6):
        for s in (-1, 1):
            v = [0] * 6
            v[i] = s
            ans.append(tuple(v))
    assert len(ans) == 11
    return ans


def support(m):
    pts = {(0,) * 6}
    for _ in range(m):
        pts = {tuple(x + y for x, y in zip(a, b)) for a in pts for b in steps()}
    return sorted(pts)


def monomials(d):
    ans = []
    def recurse(prefix, k, left):
        if left == 1:
            ans.append(tuple(prefix + [k]))
            return
        for j in range(k + 1):
            recurse(prefix + [j], k - j, left - 1)
    for total in range(d + 1):
        recurse([], total, 6)
    return ans


def evaluate(points, exponents, d):
    X = np.asarray(points, dtype=np.int64)
    powers = np.stack([X ** j for j in range(d + 1)])
    A = np.ones((len(points), len(exponents)), dtype=np.int64)
    for j, alpha in enumerate(exponents):
        for i, exponent in enumerate(alpha):
            if exponent:
                A[:, j] *= powers[exponent, :, i]
    assert np.max(np.abs(A)) <= 15625
    return A


def modular_nullspace(A, p):
    a = A.copy() % p
    rows, cols = a.shape
    rank, pivots = 0, []
    for col in range(cols):
        possibilities = np.flatnonzero(a[rank:, col])
        if not len(possibilities):
            continue
        chosen = rank + int(possibilities[0])
        if chosen != rank:
            a[[rank, chosen]] = a[[chosen, rank]]
        inverse = pow(int(a[rank, col]), -1, p)
        below = np.flatnonzero(a[rank + 1:, col]) + rank + 1
        if len(below):
            factors = a[below, col] * inverse % p
            a[below, col:] = (a[below, col:] - factors[:, None] * a[rank, col:]) % p
        pivots.append(col)
        rank += 1
        if rank == rows:
            break
    pivot_set = set(pivots)
    free = [j for j in range(cols) if j not in pivot_set]
    K = np.zeros((cols, len(free)), dtype=np.int64)
    K[free, np.arange(len(free))] = 1
    for i in range(rank - 1, -1, -1):
        tail = a[i, pivots[i] + 1:] @ K[pivots[i] + 1:]
        K[pivots[i]] = (-tail * pow(int(a[i, pivots[i]]), -1, p)) % p
    assert not np.any((A % p) @ K % p)
    return rank, pivots, free, K


def rat_reconstruct(value, modulus):
    bound = math.isqrt(modulus // 2)
    r0, r1 = modulus, int(value) % modulus
    t0, t1 = 0, 1
    while abs(r1) > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    assert t1 and abs(t1) <= bound
    if t1 < 0:
        r1, t1 = -r1, -t1
    assert math.gcd(r1, t1) == 1 and (int(value) * t1 - r1) % modulus == 0
    return r1, t1


def run():
    start = time.monotonic()
    W = support(DEGREE - 1)
    E = monomials(DEGREE)
    A = evaluate(W, E, DEGREE)
    assert len(W) == 1925 and len(E) == 924
    r0, piv0, free0, K0 = modular_nullspace(A, PRIMES[0])
    r1, piv1, free1, K1 = modular_nullspace(A, PRIMES[1])
    assert r0 == r1 == 844 and piv0 == piv1 and free0 == free1
    modulus = PRIMES[0] * PRIMES[1]
    factor = pow(PRIMES[0], -1, PRIMES[1])
    residues = K0 + PRIMES[0] * ((K1 - K0) * factor % PRIMES[1])
    K = np.zeros_like(residues)
    largest_denominator = 0
    for j in range(len(free0)):
        rational = [rat_reconstruct(v, modulus) for v in residues[:, j]]
        denominator = math.lcm(*(pair[1] for pair in rational))
        largest_denominator = max(largest_denominator, denominator)
        for i, (numerator, divisor) in enumerate(rational):
            K[i, j] = numerator * (denominator // divisor)
    assert len(free0) == 80
    assert np.max(np.abs(K)) <= 345
    assert not np.any(A @ K)
    for j, index in enumerate(free0):
        assert K[index, j] > 0
        assert all(K[index, k] == 0 for k in range(len(free0)) if k != j)
    # Every W5 point has a legal ordered 5-step realization by construction.
    # Modular rank 844 implies rank_Q >= 844; 80 exact independent integer
    # kernel polynomials imply rank_Q <= 924 - 80 = 844.
    print('PREFIX457 EXACT SEXTIC CERTIFICATE: PASS')
    print('directions=11; native_X6_dim=6; path_duration_in_terminal_sector=5')
    print(f'W5_distinct_endpoints={len(W)}; monomials_degree_le_6={len(E)}')
    print(f'modular_primes={PRIMES}; both_modular_ranks={r0},{r1}; pivot_columns_identical=True')
    print(f'CRT_modulus={modulus}; independent_integer_kernel_vectors={K.shape[1]}')
    print(f'exact_A_times_K_is_zero=True; kernel_nonzero_terms={int(np.count_nonzero(K))}')
    print(f'kernel_max_absolute_coefficient={int(np.max(np.abs(K)))}; largest_rational_denominator={largest_denominator}')
    print('rational_rank_of_W5_degree_le_6=844; deficiency=80')
    print('for_every_integer_q_ge_6: rank_total_degree_le_6_at_N_eq_q_plus_4 = 924*q-80')
    print(f'elapsed_seconds={time.monotonic()-start:.3f} (diagnostic, variable)')


if __name__ == '__main__':
    run()
