#!/usr/bin/env python3
"""R284AZ: exact finite-domain tests for one-read polynomial identity separation.
No third-party dependencies. Exhaustive finite-alphabet tests; they do not prove
that each fresh random draw succeeds or that decoder lookup is polynomial time.
"""
from itertools import permutations, product
from math import comb
import hashlib, json, random, sys


def instrument_bound(n, H):
    N = H ** (n * n)
    return 4 * (n - 1) * comb(N, 2) if N > 1 else 0


def permutation_terms(n):
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        yield p, (-1 if inv % 2 else 1)


def response(flat, n, diagonal, star, terms):
    matrix = [[(diagonal[i] if i == j else 0) - flat[n*i+j]
               - (star[j-1] if i == 0 and j > 0 else 0)
               for j in range(n)] for i in range(n)]
    ans = 0
    for p, sign in terms:
        val = sign
        for i, j in enumerate(p):
            val *= matrix[i][j]
        ans += val
    return ans


def exhaustive_trial(n, H, seed, K=None):
    if K is None:
        K = instrument_bound(n, H)
    rng = random.Random(seed)
    diagonal = [rng.randrange(K + 1) for _ in range(n)]
    star = [rng.randrange(K + 1) for _ in range(n - 1)]
    terms = tuple(permutation_terms(n))
    seen = {}
    max_bits = 0
    collisions = 0
    witness = None
    for flat in product(range(1, H + 1), repeat=n*n):
        y = response(flat, n, diagonal, star, terms)
        max_bits = max(max_bits, abs(y).bit_length())
        if y in seen and seen[y] != flat:
            collisions += 1
            if witness is None:
                witness = {'C1':seen[y], 'C2':flat, 'output':str(y)}
        else:
            seen[y] = flat
    return {
        'n':n, 'H':H, 'seed':seed, 'K':K,
        'candidate_count':H**(n*n),
        'diagonal':diagonal, 'star':star,
        'distinct_outputs':len(seen),
        'collisions':collisions,
        'max_abs_output_bits':max_bits,
        'first_collision':witness,
        'passed':collisions==0
    }


def test_linearity():
    rng = random.Random(2842901)
    checks = 0
    for n in (2,3,4):
        terms = tuple(permutation_terms(n))
        for _ in range(28):
            C = [rng.randint(1,4) for _ in range(n*n)]
            D = [rng.randint(-5,5) for _ in range(n)]
            z = [rng.randint(-4,4) for _ in range(n-1)]
            zero = [0] * (n-1)
            lhs = response(C,n,D,z,terms)
            rhs = response(C,n,D,zero,terms)
            for v in range(n-1):
                basis=[0]*(n-1)
                basis[v]=1
                rhs += z[v]*(response(C,n,D,basis,terms)-response(C,n,D,zero,terms))
            assert lhs==rhs,(n,C,D,z,lhs,rhs)
            checks+=1
    return checks


def main():
    specs=[(2,2,2842902),(3,2,2842903),(3,2,2842904),(3,2,2842905),
           (3,3,2842906),(4,2,2842907)]
    trials=[exhaustive_trial(*spec) for spec in specs]
    checks=test_linearity()
    assert all(t['passed'] for t in trials), [t for t in trials if not t['passed']]
    report={
        'result':'PASS',
        'claim':'Exhaustive finite alphabet examples only; probabilistic bound is symbolic Schwartz-Zippel union bound',
        'model':'exact integer determinant diag(D)-C-sum(z_v E_{0v}), C entries 1..H',
        'instrument_bound':'K=4*(n-1)*binom(H^(n*n),2); P(any collision)<=(n-1)*binom(H^(n*n),2)/(K+1)<1/4',
        'trial_count':len(trials),
        'total_candidates_checked':sum(t['candidate_count'] for t in trials),
        'linearity_comparisons':checks,
        'trials':trials,
        'limitations':['Each random trial succeeds with proven probability, not certainty',
                       'Full alphabet lookup table is exponential in n^2 log H',
                       'Finite test does not independently prove injectivity of polynomial signatures']
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))


if __name__=='__main__':
    main()
