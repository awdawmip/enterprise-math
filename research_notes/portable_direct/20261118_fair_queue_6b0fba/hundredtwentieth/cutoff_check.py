"""Verify the prime cutoff variance and exact signed decomposition on the original carries."""
import argparse
from fractions import Fraction
from itertools import combinations
import json
from math import fsum, gcd, isqrt, log, prod
from pathlib import Path


def primes_to(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = bytes((limit - p*p)//p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def carry(n, modulus):
    return (2*n)//modulus - 2*(n//modulus)


def exact_decomposition():
    checks = 0
    primes = primes_to(150)
    for n in range(8, 151):
        alpha = Fraction(sum(carry(n, m) for m in range(1, n + 1)), n)
        for k in (4, 5, 8):
            for y in {2, isqrt(n), n//2}:
                for p in primes:
                    if p > n:
                        break
                    powers = []
                    v = p
                    while v <= n:
                        powers.append(v)
                        v *= p
                    count = len(powers)
                    a = Fraction(p//2, p)
                    lower = powers[1:k-1]
                    # Each coefficient has a rational part and a coefficient of gamma.
                    source_rational = sum(carry(n, m) - alpha for m in powers)
                    removed_prime = carry(n, p) if p > y else a
                    removed = removed_prime - count*alpha + sum(carry(n, m) for m in lower)
                    removed_gamma = -1 + count - len(lower)
                    target = (carry(n, p) - a if p <= y else 0) + sum(carry(n, m) for m in powers[k-1:])
                    assert source_rational - removed == target
                    assert -removed_gamma == -len(powers[k-1:])
                    checks += 1
    return checks


def exact_period():
    ps = (2, 3, 5, 7)
    period = prod(ps)
    rows = [[Fraction(carry(n, p)) - Fraction(p//2, p) for n in range(period)] for p in ps]
    variances = []
    for p, row in zip(ps, rows):
        a = Fraction(p//2, p)
        assert sum(row) == 0
        variance = sum(x*x for x in row)/period
        assert variance == a*(1-a)
        variances.append(str(variance))
    for left, right in combinations(rows, 2):
        assert sum(x*y for x, y in zip(left, right)) == 0
    return {'period': period, 'primes': ps, 'variance_diagonal': variances, 'mixed_terms_zero': 6}


def sample_block(n0, y):
    ps = primes_to(y)
    n1 = 2*n0
    delta = [0.0] * (n0 + 1)
    logweights = [log(p) for p in ps]
    bias = fsum((p//2)/p * w for p, w in zip(ps, logweights))
    variance = fsum(w*w*((p//2)/p)*(1-(p//2)/p) for p, w in zip(ps, logweights))
    for p, w in zip(ps, logweights):
        # On each p-cycle the gate is one on the final floor(p/2) residues.
        for b in range((n0//p)*p, n1, p):
            lo, hi = max(n0, b + (p+1)//2), min(n1, b+p)
            if lo < hi:
                delta[lo-n0] += w
                delta[hi-n0] -= w
    values = []
    total = 0.0
    max_error = 0.0
    for i in range(n0):
        total += delta[i]
        v = total - bias
        original = fsum(w*(carry(n0+i, p) - (p//2)/p) for p, w in zip(ps, logweights))
        max_error = max(max_error, abs(v-original))
        values.append(original)
    assert max_error < 1e-7
    full = fsum(v*v for v in values)
    half = fsum(v*v for v in values[:n0//2])
    assert abs(full-n0*variance) <= 3*y*y*variance
    assert abs(half-(n0//2)*variance) <= 3*y*y*variance
    weighted = n0*fsum(v*v/(n0+i)**2 for i, v in enumerate(values))
    return {'N': n0, 'y': y, 'prime_count': len(ps), 'periodic_variance': round(variance, 10),
            'full_mean_square_over_variance': round(full/(n0*variance), 10),
            'weighted_square_over_variance': round(weighted/variance, 10),
            'two_source_evaluations_agree': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    data = {'exact_prime_coefficient_comparisons': exact_decomposition(),
            'complete_small_period': exact_period(),
            'actual_integer_blocks': [sample_block(n, y) for n, y in
                [(4096, 13), (16384, 23), (65536, 43), (131072, 61)]]}
    text = json.dumps(data, indent=2) + '\n'
    if args.out:
        args.out.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
