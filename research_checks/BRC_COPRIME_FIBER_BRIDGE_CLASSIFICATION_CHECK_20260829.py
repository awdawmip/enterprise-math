#!/usr/bin/env python3
"""
Exact finite regression checker for:
RS-BRC-COPRIME-FIBER-BRIDGE-CLASSIFICATION

This checker does not prove the arbitrary-integer F3R2 theorem. It verifies
the bridge/CRT translation and counterexamples on an exact bounded domain.

Verifier may know p,q. The factor-blind observables under test use only
N and the public integer matrix A.
"""
from math import gcd
from itertools import product

BOUND = 16
PRIMES = (3, 5, 7, 11)


def det(A):
    a, b, c, d = A
    return a * d - b * c


def gh(A):
    a, b, c, d = A
    return gcd(abs(a), abs(d)), gcd(abs(b), abs(c))


def survivor(A):
    g, h = gh(A)
    return det(A) in (1, -1) and g > 1 and h > 1


def proper_divisor(x, N):
    return 1 < x < N and N % x == 0


def factor_blind_alignment(A, N):
    g, h = gh(A)
    u = gcd(N, g)
    v = gcd(N, h)
    split = proper_divisor(u, N) and proper_divisor(v, N)
    endpoint = proper_divisor(u, N) or proper_divisor(v, N)
    return u, v, split, endpoint


def crt_zero_status(x, p, q):
    return (x % p == 0, x % q == 0)


def diagonal_monomial_mod(A, r):
    a, b, c, d = (x % r for x in A)
    return b == 0 and c == 0 and a != 0 and d != 0


def antidiagonal_monomial_mod(A, r):
    a, b, c, d = (x % r for x in A)
    return a == 0 and d == 0 and b != 0 and c != 0


def classify(A, p, q):
    N = p * q
    g, h = gh(A)
    u, v, split, endpoint = factor_blind_alignment(A, N)
    if not survivor(A):
        return "NONSURVIVOR"
    if split:
        return "HIDDEN_SPLIT_DIRECT_ENDPOINTS"
    if u == N or v == N:
        return "SURVIVOR_BOTH_HIDDEN_FACTORS_SAME_ORIENTATION"
    if endpoint:
        return "SURVIVOR_ONE_HIDDEN_FACTOR_DIRECT_GCD_ONLY"
    return "SURVIVOR_UNALIGNED"


def check_explicit_examples():
    examples = [
        ((-4, -3, -3, -2), 5, 7, "SURVIVOR_UNALIGNED"),
        ((-35, -68, -18, -35), 5, 7, "SURVIVOR_BOTH_HIDDEN_FACTORS_SAME_ORIENTATION"),
        ((-5, -6, -4, -5), 5, 7, "SURVIVOR_ONE_HIDDEN_FACTOR_DIRECT_GCD_ONLY"),
        ((-10, -7, -7, -5), 5, 7, "HIDDEN_SPLIT_DIRECT_ENDPOINTS"),
    ]
    for A, p, q, want in examples:
        assert det(A) in (1, -1), (A, det(A))
        got = classify(A, p, q)
        assert got == want, (A, got, want, gh(A))
    return examples


def exhaustive():
    mats = 0
    survivors = 0
    pairs = 0
    split_cases = 0
    endpoint_cases = 0
    same_side_cases = 0
    unaligned_cases = 0

    for A in product(range(-BOUND, BOUND + 1), repeat=4):
        if det(A) not in (1, -1):
            continue
        mats += 1
        g, h = gh(A)
        assert gcd(g, h) == 1, (A, g, h)
        if survivor(A):
            survivors += 1

        for p_i, p in enumerate(PRIMES):
            for q in PRIMES[p_i + 1 :]:
                N = p * q
                pairs += 1
                u, v, split, endpoint = factor_blind_alignment(A, N)

                # A is unimodular, hence invertible in every CRT channel.
                assert gcd(abs(det(A)), N) == 1
                # F3R2's two cross-gcd supports cannot share a prime.
                assert gcd(u, v) == 1

                if split:
                    split_cases += 1
                    assert survivor(A)
                    assert u * v == N
                    assert {u, v} == {p, q}
                    # u comes from g=(a,d): anti-diagonal orientation mod u.
                    assert antidiagonal_monomial_mod(A, u)
                    # v comes from h=(b,c): diagonal orientation mod v.
                    assert diagonal_monomial_mod(A, v)
                    # The "observable" already is direct gcd endpoint recovery.
                    assert gcd(N, g) == u
                    assert gcd(N, h) == v

                if endpoint:
                    endpoint_cases += 1

                if u == N or v == N:
                    same_side_cases += 1
                    if u == N:
                        assert antidiagonal_monomial_mod(A, p)
                        assert antidiagonal_monomial_mod(A, q)
                    if v == N:
                        assert diagonal_monomial_mod(A, p)
                        assert diagonal_monomial_mod(A, q)

                if survivor(A) and u == 1 and v == 1:
                    unaligned_cases += 1

                # Candidate residues g mod N and h mod N are one-sided-zero
                # exactly when their direct Euclidean gcd is a proper factor.
                zg = crt_zero_status(g, p, q)
                zh = crt_zero_status(h, p, q)
                assert (zg[0] != zg[1]) == proper_divisor(gcd(N, g), N)
                assert (zh[0] != zh[1]) == proper_divisor(gcd(N, h), N)

    return {
        "bounded_unimodular_matrices": mats,
        "bounded_survivors": survivors,
        "matrix_semiprime_pairs": pairs,
        "hidden_split_cases": split_cases,
        "direct_endpoint_cases": endpoint_cases,
        "same_orientation_both_factor_cases": same_side_cases,
        "survivor_unaligned_cases": unaligned_cases,
    }


def main():
    examples = check_explicit_examples()
    counts = exhaustive()
    print("PASS")
    print("explicit_examples=", len(examples))
    for k, v in counts.items():
        print(f"{k}={v}")


if __name__ == "__main__":
    main()
