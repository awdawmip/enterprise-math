#!/usr/bin/env python3
"""Exact finite regression for R284AL: low-rank principal-minor detection.

Uses only SymPy exact Integer/Rational arithmetic; randomness is seeded and
is solely the selection of positive integer diagonal probes.
"""
import json
import random
from itertools import combinations
from sympy import Matrix, symbols

SEED = 284120261119
RNG = random.Random(SEED)


def full_principal_degree(C):
    m = C.rows
    best = 0
    witnesses = []
    for j in range(1, m+1):
        for S in combinations(range(m), j):
            if C.extract(S, S).det() != 0:
                best = j
                witnesses.append(list(S))
    return best, witnesses


def e_coefficients_of_kernel(U, V, d):
    """Return e_0,...,e_r of K=V.T diag(d) U exactly."""
    m,r = U.shape
    assert V.shape == (m,r) and len(d) == m
    K = V.T * Matrix.diag(*d) * U
    t = symbols('z')
    cp = K.charpoly(t).all_coeffs()  # z^r - e1 z^(r-1)+ ...
    return [(-1)**j * cp[j] for j in range(r+1)]


def degree_from_probe(U, V, d):
    e = e_coefficients_of_kernel(U,V,d)
    return max(j for j, x in enumerate(e) if x != 0)


def extract_witness(U,V,d,j):
    """Self-reduce e_j to a single nonzero principal minor."""
    assert j >= 1 and e_coefficients_of_kernel(U,V,d)[j] != 0
    w = list(d)
    attempts = 0
    accepted = 0
    while sum(x != 0 for x in w) > j:
        changed = False
        for i in range(len(w)):
            if w[i] == 0:
                continue
            trial = w[:]
            trial[i] = 0
            attempts += 1
            if e_coefficients_of_kernel(U,V,trial)[j] != 0:
                w = trial
                accepted += 1
                changed = True
                if sum(x != 0 for x in w) == j:
                    break
        assert changed, "Euler identity guarantees one removable coordinate"
    S = [i for i,x in enumerate(w) if x != 0]
    assert len(S) == j
    C = U*V.T
    minor = C.extract(S,S).det()
    assert minor != 0
    exact_ej = e_coefficients_of_kernel(U,V,w)[j]
    assert exact_ej == minor * __import__('math').prod(w[i] for i in S)
    return S, minor, attempts, accepted


def main():
    # Strictly positive nonsymmetric example: rank 2, principal degree 2,
    # yet the unweighted characteristic polynomial misses degree 2.
    U0 = Matrix([[1,1],[1,2],[1,3]])
    V0 = Matrix([[1,1],[1,2],[1,1]])
    C0 = U0*V0.T
    assert C0 == Matrix([[2,3,2],[3,5,3],[4,7,4]])
    assert C0.rank() == 2
    assert degree_from_probe(U0,V0,[1,1,1]) == 1
    assert degree_from_probe(U0,V0,[1,1,2]) == 2
    S0, minor0, _, _ = extract_witness(U0,V0,[1,1,2],2)

    # Synthetic strict-positive factors; m<=6 makes exhaustive truth feasible.
    results = {
        'schema': 'EM_R284AL_EXACT_FINITE_TEST_V1',
        'seed': SEED, 'exact_arithmetic': 'SymPy Integer/Rational',
        'example': {'U': [[int(x) for x in row] for row in U0.tolist()], 'V': [[int(x) for x in row] for row in V0.tolist()], 'C': [[int(x) for x in row] for row in C0.tolist()],
                    'principal_degree': 2, 'uniform_probe_degree': 1,
                    'weighted_probe': [1,1,2], 'weighted_degree': 2,
                    'extracted_witness_0_based': S0,
                    'witness_minor': str(minor0)},
        'families': {}, 'checks': 0, 'witness_checks': 0,
        'probe_exact_hits': 0, 'probe_misses': 0,
        'total_exhaustive_principal_minors': 0,
    }
    for m in range(3,7):
        for r in range(1,min(3,m)+1):
            key = f'm{m}_r{r}'
            counts = {'examples':0,'hits':0,'misses':0,'witnesses':0}
            for instance in range(16):
                while True:
                    U = Matrix([[RNG.randint(1,7) for _ in range(r)] for __ in range(m)])
                    V = Matrix([[RNG.randint(1,7) for _ in range(r)] for __ in range(m)])
                    if U.rank() == r and V.rank() == r:
                        break
                C = U*V.T
                actual,wits = full_principal_degree(C)
                results['total_exhaustive_principal_minors'] += (2**m - 1)
                d = [RNG.randint(1,31) for _ in range(m)]
                observed = degree_from_probe(U,V,d)
                assert 0 <= observed <= actual <= r
                if observed == actual:
                    counts['hits'] += 1
                    results['probe_exact_hits'] += 1
                else:
                    counts['misses'] += 1
                    results['probe_misses'] += 1
                if observed:
                    S,minor,_,_ = extract_witness(U,V,d,observed)
                    assert len(S) == observed
                    assert minor != 0
                    counts['witnesses'] += 1
                    results['witness_checks'] += 1
                counts['examples'] += 1
                results['checks'] += 1
            results['families'][key] = counts
    assert results['checks'] == 192
    assert results['probe_exact_hits'] + results['probe_misses'] == 192
    assert results['witness_checks'] == 192
    # R284AK family: rank k+1 but principal degree exactly 2, with
    # arbitrarily growing gap. Check reduced charpoly and extracted witnesses.
    results['ak_family'] = []
    for k in range(2,6):
        r = k+1
        a = [1]*r
        bs = [a[:j+1]+[2]+a[j+2:] for j in range(k)]
        U = Matrix([a]*k + bs)
        V = Matrix(bs + [a]*k)
        assert U.rank()==r and V.rank()==r
        C = U*V.T
        assert C.rank()==r
        d = [1 + ((i+3*k)*7 % 31) for i in range(2*k)]
        ec = e_coefficients_of_kernel(U,V,d)
        assert ec[2] != 0 and all(v==0 for v in ec[3:])
        S,minor,_,_ = extract_witness(U,V,d,2)
        results['ak_family'].append({'k':k,'m':2*k,'r':r,
                  'probe_degree':2,'exact_witness_0_based':S,
                  'witness_minor':str(minor)})
    results['status'] = 'PASS' 
    print(json.dumps(results,indent=2,ensure_ascii=False,sort_keys=True))


if __name__ == '__main__':
    main()
