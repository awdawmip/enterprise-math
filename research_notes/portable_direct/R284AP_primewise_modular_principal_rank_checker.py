#!/usr/bin/env python3
"""R284AP: exact primewise exterior-span principal-rank verifier (stdlib only)."""
import json
import math
import random
from itertools import combinations, permutations


def det(a):
    n = len(a)
    if n == 0:
        return 1
    return sum((-1) ** sum(t[i] > t[j] for i in range(n) for j in range(i+1, n))
               * math.prod(a[i][t[i]] for i in range(n)) for t in permutations(range(n)))


def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % d for d in range(3, math.isqrt(n) + 1, 2))


def prime_coverage(k, M):
    # Explicit bound for every nonzero principal minor of XY^T, at any grade.
    B = max([1] + [math.comb(k, j) * math.factorial(j)**2 * M**(2*j)
                    for j in range(1, k+1)])
    primes, Q, n = [], 1, 2
    while Q <= B:
        if isprime(n):
            primes.append(n)
            Q *= n
        n += 1
    return B, primes, Q


def state(X, Y, S, k):
    j = len(S)
    a = []
    b = []
    for J in combinations(range(k), j):
        a.append(det([[X[i][h] for h in J] for i in S]))
        b.append(det([[Y[i][h] for h in J] for i in S]))
    return tuple(x*y for x in a for y in b), sum(a[i]*b[i] for i in range(len(a)))


def mod_span_run(X, Y, p):
    m, k = len(X), len(X[0])
    basis = [[((), (1,))]] + [[] for _ in range(k)]
    pivots = [dict() for _ in range(k+1)]
    pivots[0][0] = (1,)
    seen = 0
    for i in range(m):
        for j in range(min(k, i+1), 0, -1):
            prior = list(basis[j-1])
            for S, _ in prior:
                T = S + (i,)
                raw, _ = state(X, Y, T, k)
                v = [q % p for q in raw]
                for pivot, row in sorted(pivots[j].items()):
                    scalar = v[pivot]
                    if scalar:
                        v = [(v[h] - scalar * row[h]) % p for h in range(len(v))]
                seen += 1
                leading = next((h for h, z in enumerate(v) if z), None)
                if leading is not None:
                    inv = pow(v[leading], -1, p)
                    pivots[j][leading] = tuple((x*inv) % p for x in v)
                    basis[j].append((T, raw))
    witness = None
    for j in range(k, 0, -1):
        for S, _ in basis[j]:
            _, trace = state(X, Y, S, k)
            if trace % p:
                witness = S
                break
        if witness is not None:
            return j, witness, seen, [len(b) for b in basis], [[S for S, _ in bj] for bj in basis]
    return 0, None, seen, [len(b) for b in basis], [[S for S, _ in bj] for bj in basis]


def rank_mod(vectors, p):
    """Verifier's independent full-field Gaussian elimination."""
    if not vectors:
        return 0
    a = [[x % p for x in v] for v in vectors]
    nr, nc, row = len(a), len(a[0]), 0
    for col in range(nc):
        pivot = next((i for i in range(row,nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        iv = pow(a[row][col], -1, p)
        a[row] = [(x * iv) % p for x in a[row]]
        for i in range(row+1,nr):
            mul = a[i][col]
            if mul:
                a[i] = [(a[i][h] - mul*a[row][h]) % p for h in range(nc)]
        row += 1
        if row == nr:
            break
    return row


def verify_final_basis(X, Y, p, labels):
    """Independent non-prefix certificate: true basis + all E_i closures."""
    m, k = len(X), len(X[0])
    assert labels[0] == [()] and len(labels) == k+1
    total_closure = 0
    grade_vecs = []
    for j in range(k+1):
        assert len(set(labels[j])) == len(labels[j])
        assert all(len(S) == j and list(S) == sorted(S) and all(0 <= i < m for i in S) for S in labels[j])
        vv = [state(X,Y,S,k)[0] for S in labels[j]]
        assert rank_mod(vv,p) == len(vv)
        grade_vecs.append(vv)
    for j in range(1,k+1):
        for S in labels[j-1]:
            for i in range(m):
                if i in S:
                    continue
                T = tuple(sorted(S+(i,)))
                v = state(X,Y,T,k)[0]
                assert rank_mod(grade_vecs[j]+[v],p) == len(grade_vecs[j])
                total_closure += 1
    d = max([0]+[j for j in range(1,k+1)
                 if any(state(X,Y,S,k)[1] % p for S in labels[j])])
    return d, total_closure


def oracle(X, Y):
    m, k = len(X), len(X[0])
    C = [[sum(X[i][a]*Y[j][a] for a in range(k)) for j in range(m)] for i in range(m)]
    for j in range(min(k,m), 0, -1):
        for S in combinations(range(m), j):
            if det([[C[i][h] for h in S] for i in S]):
                return j, S
    return 0, None


def assess(X, Y):
    m, k = len(X), len(X[0])
    assert len(Y) == m and all(len(a) == k for a in X + Y)
    M = max([1] + [abs(a) for row in X + Y for a in row])
    B, primes, Q = prime_coverage(k, M)
    runs = [(p, *mod_span_run(X, Y, p)) for p in primes]
    d = max(t[1] for t in runs)
    witness = next((t[2] for t in runs if t[1] == d and t[2] is not None), None)
    if witness is not None:
        C = [[sum(X[i][a]*Y[j][a] for a in range(k)) for j in range(m)] for i in range(m)]
        assert det([[C[i][h] for h in witness] for i in witness]) != 0
    return d, witness, B, primes, Q, sum(t[3] for t in runs), runs


def run():
    rng = random.Random(284016)
    tests = []
    tests.append(([[2]], [[1]], 'two-prime-needed'))
    tests.append(([[1,0],[0,0]], [[0,1],[0,0]], 'nilpotent-no-principal'))
    tests.append(([[1,0],[0,1]], [[1,0],[0,1]], 'symmetric-positive'))
    for case in range(84):
        m = rng.randint(2, 6)
        k = rng.randint(1, min(3,m))
        X = [[rng.randint(-3,3) for _ in range(k)] for _ in range(m)]
        Y = [[rng.randint(-3,3) for _ in range(k)] for _ in range(m)]
        tests.append((X,Y,f'random-{case:02d}'))
    total_candidates, max_p, max_B_bits, max_Q_bits, divergence, total_closures = 0, 0, 0, 0, 0, 0
    sample = []
    for X,Y,name in tests:
        got = assess(X,Y)
        expected, _ = oracle(X,Y)
        assert got[0] == expected, (name,got,expected)
        total_candidates += got[5]
        for p, d_p, _, _, _, labels in got[6]:
            checked_d, closure_count = verify_final_basis(X,Y,p,labels)
            assert checked_d == d_p
            total_closures += closure_count
        max_p = max(max_p, len(got[3]))
        max_B_bits = max(max_B_bits,got[2].bit_length())
        max_Q_bits = max(max_Q_bits,got[4].bit_length())
        divergence += int(len({t[1] for t in got[6]}) > 1)
        if len(sample) < 3:
            sample.append({'case':name, 'd':got[0], 'witness':got[1], 'primes':got[3],
                           'per_prime_d':[t[1] for t in got[6]], 'minor_bound':got[2]})
    return {'schema':'R284AP_EXACT_VERIFICATION_V1','seed':284016,'method':'primewise exterior DP; integer independent Leibniz oracle',
            'tested_instances':len(tests),'exact_oracle_agreement':len(tests),
            'total_modular_candidates':total_candidates,'independent_final_basis_closure_checks':total_closures, 'max_prime_count':max_p,
            'max_minor_bound_bits':max_B_bits,'max_prime_product_bits':max_Q_bits,
            'instances_with_modular_degree_divergence':divergence,
            'examples':sample,'general_theorem_status':'AUTHOR_PROVED_NOT_INDEPENDENTLY_REVIEWED','status':'PASS'}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
