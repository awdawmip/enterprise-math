#!/usr/bin/env python3
"""Author-side exact-integer verification of A216 all-digit p^3 block lift.

Independent left side: original integer binomial formula, not the block formula.
No native H0/B0 experiment, Source CLAIM, or mathematical admission is implied.
"""
from math import comb


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


def a216(n, modulus):
    return (comb(2*n, n)**2 * comb(3*n, n) * pow(216, -n, modulus)) % modulus


def lift(p, u, r):
    assert p >= 7 and p % 6 == 1 and is_prime(p)
    assert u >= 0 and 0 <= r < p
    modulus = p**3
    inv2 = pow(2, -1, modulus)
    q = (pow(216, p - 1, modulus) - 1) // p
    d1 = d2 = 0
    hit = 1
    hits = 0
    for j in range(r):
        for numerator, scale, hit_factor in (
            (2*j + 1, 2, 2*u + 1),
            (3*j + 1, 3, 3*u + 1),
            (3*j + 2, 3, (3*u + 2)*inv2),
        ):
            if numerator % p == 0:
                hit = hit * hit_factor % modulus
                hits += 1
            else:
                reciprocal = scale * pow(numerator, -1, modulus) % modulus
                d1 += reciprocal
                d2 += reciprocal * reciprocal
        inverse = pow(j + 1, -1, modulus)
        d1 -= 3 * inverse
        d2 -= 3 * inverse * inverse
    d1 %= modulus
    d2 %= modulus
    z = (d1 - q) % modulus
    jet = (1 + p*u*z + p*p*inv2*(u*u*(z*z - d2) + u*q*q)) % modulus
    source = (a216(u, modulus)*a216(r, modulus)*hit) % modulus
    a_prediction = source * jet % modulus
    weight = 6*r + 1
    w_jet = (weight + p*u*(6 + weight*z)
             + p*p*(weight*inv2*(u*u*(z*z-d2)+u*q*q)+6*u*u*z)) % modulus
    w_prediction = source * w_jet % modulus
    return a_prediction, w_prediction, hits


def validate():
    count = 0
    tier_counts = [0, 0, 0, 0]
    primes = [p for p in range(7, 180) if p % 6 == 1 and is_prime(p)]
    for p in primes:
        modulus = p**3
        for u in range(4):
            for r in range(p):
                expected_a, expected_w, hits = lift(p,u,r)
                actual_a = a216(p*u+r, modulus)
                actual_w = ((6*(p*u+r)+1)*actual_a) % modulus
                assert (expected_a,expected_w)==(actual_a,actual_w), (p,u,r,hits,expected_a,actual_a,expected_w,actual_w)
                tier_counts[hits] += 1
                count += 1
    selected = [0, 1, 62, 124, 125, 186, 187, 248, 249, 300, 372]
    p = 373
    witnesses = []
    for u in [1, 2]:
        for r in selected:
            expected_a, expected_w, hits = lift(p,u,r)
            actual_a = a216(p*u+r, p**3)
            assert expected_a == actual_a
            assert expected_w == (6*(p*u+r)+1)*actual_a % p**3
            witnesses.append((u,r,hits,expected_a,expected_w))
    assert all(tier_counts), tier_counts
    print('PASS_D25_A216_FULL_DIGIT_P3_A_AND_SIGNED_W',count,'cases',len(primes),'primes p<180',tuple(tier_counts))
    print('PASS_P373_CROSS_TIER_INDEPENDENT_BINOMIAL',len(witnesses),'cases')
    print('P373_WITNESSES',witnesses)


if __name__ == '__main__':
    validate()
