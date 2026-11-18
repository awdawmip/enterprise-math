#!/usr/bin/env python3
"""Exact residue counts for the Hart window laws. Prints a JSON certificate."""
import json
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt


def qr_counts(modulus, residue):
    squares = {x * x % modulus for x in range(modulus)}
    counts = [sum((x*x - 4*residue*r) % modulus in squares for x in range(modulus))
              for r in range(modulus)]
    return squares, counts


def joint(counts, lag):
    m = len(counts)
    return Fraction(sum(a * counts[(r + lag) % m] for r, a in enumerate(counts)), m**3)


def check_primes():
    checked = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        squares = {x * x % p for x in range(p)}

        def chi(t):
            t %= p
            return 0 if t == 0 else 1 if t in squares else -1

        for n in range(1, p):
            _, counts = qr_counts(p, n)
            for r in range(p):
                assert 2 * counts[r] == p + p * (r == 0) + chi(n*r)
            mu = Fraction(p+1, 2*p)
            for h in range(1, p+1):
                numerator = p*p-1 if h == p else p * (chi(n*h) + chi(-n*h)-1) - 1
                assert joint(counts, h) - mu**2 == Fraction(numerator, 4*p**3)
                checked += 1
    return checked


def check_wheels():
    checked = 0
    for modulus, factors in [(15, (3, 5)), (21, (3, 7)), (35, (5, 7))]:
        for n in range(1, modulus):
            if gcd(modulus, n) != 1:
                continue
            squares, counts = qr_counts(modulus, n)
            assert sum(counts) == modulus * len(squares)
            factors_counts = [qr_counts(p, n)[1] for p in factors]
            for h in range(1, modulus+1):
                assert joint(counts, h) == joint(factors_counts[0], h)*joint(factors_counts[1], h)
                checked += 1
    return checked


def check_block():
    # Exhaust the finite two-phase residue law for every pair, independently of A(r).
    p, n, block = 5, 2, 10
    squares, counts = qr_counts(p, n)
    conditional_count = Fraction(sum(a*(p-a) for a in counts), p**3)
    mu = Fraction(sum(counts), p**2)
    second = block*mu
    for h in range(1, block):
        favourable = sum((a*a-4*n*r) % p in squares and (b*b-4*n*(r+h)) % p in squares
                         for r in range(p) for a in range(p) for b in range(p))
        second += 2*(block-h)*Fraction(favourable, p**3)
    variance = second-(block*mu)**2
    assert variance == block*conditional_count
    return str(variance)


def sample(k0):
    # Synthetic cubes give exact endpoints. Every displayed count uses integer arithmetic.
    modulus = 15
    n = k0**3
    alpha = Fraction(1, 4)
    squares = {x*x % modulus for x in range(modulus)}
    passed, selected = [], []
    residues = Counter()
    for k in range(k0, 2*k0+1):
        x = 1 + isqrt(4*n*k-1)
        e = x*x-4*n*k
        assert 0 <= e < 2*x-1
        residues[e % modulus] += 1
        passed.append(e % modulus in squares)
        selected.append(passed[-1] and e*alpha.denominator <= (2*x-1)*alpha.numerator)
    _, counts = qr_counts(modulus, n)
    return {'N': n, 'K': k0, 'positions': len(passed), 'M': modulus, 'score_cutoff': str(alpha),
            'residue_histogram': [residues[i] for i in range(modulus)],
            'wheel_pass': sum(passed), 'wheel_and_score_pass': sum(selected),
            'wheel_and_score_limit_rate': str(alpha*Fraction(len(squares),modulus)),
            'adjacent_wheel_pair': sum(a and b for a, b in zip(passed, passed[1:])),
            'adjacent_wheel_pair_limit_rate': str(joint(counts, 1))}


if __name__ == '__main__':
    evidence = {'prime_covariance_cases': check_primes(), 'crt_lag_cases': check_wheels(),
                'p5_N2_ten_window_variance': check_block(),
                'synthetic_cube_shells': [sample(k) for k in [4096, 65536, 262144]]}
    print(json.dumps(evidence, indent=2, sort_keys=True))
