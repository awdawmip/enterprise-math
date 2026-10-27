#!/usr/bin/env python3
"""Exact author-side check of the D25 Cauchy tail-reflection identity.

This is not a native H0/B0 divided-power experiment or a Source Result.
"""

from math import comb, isqrt


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def terms(p, exponent=2):
    modulus = p ** exponent
    t, b = [1], [1]
    for k in range(1, p):
        t.append(t[-1] * (2*k-1) * (3*k-2) * (3*k-1)
                 * pow(36 * k**3, -1, modulus) % modulus)
        b.append(b[-1] * (2*k-1) * pow(4*k, -1, modulus) % modulus)
    return t, b


def direct_terms(p, modulus):
    """Independent integer-binomial construction at the same original cutoff."""
    t = [comb(2*k, k)**2 * comb(3*k, k)
         * pow(216, -k, modulus) % modulus for k in range(p)]
    b = [comb(2*j, j) * pow(8, -j, modulus) % modulus
         for j in range(p)]
    return t, b


def observers(p, t, b, modulus):
    N = p - 1
    B, prefix = [], 0
    for item in b:
        prefix = (prefix + item) % modulus
        B.append(prefix)
    half = pow(2, -1, modulus)
    W = sum((6*k+1) * t[k] for k in range(p)) % modulus
    H = (half * sum((6*k+1) * t[k] * B[N-k]
                    for k in range(p))) % modulus
    K = (3*half * sum((2*(N-k)+1) * t[k] * b[N-k]
                      for k in range(p))) % modulus
    return B[-1], W, H, K, (H-K) % modulus


def reflected_tail(p, t_reduced):
    """T_p=sum_{k<=2m} (6k+1)t_k sum_{s<k}8^s/((2s+1)C(2s,s))."""
    m = (p - 1) // 6
    total, tail, u = 0, 0, 1
    for k in range(2*m+1):
        total = (total + (6*k+1) * t_reduced[k] * tail) % p
        if k < 2*m:
            tail = (tail + u) % p
            # u_(k+1)/u_k=4(k+1)/(2k+3), denominator a p-unit.
            u = (u * 4*(k+1) * pow(2*k+3, -1, p)) % p
    return total


def check_prime(p):
    assert is_prime(p) and p % 6 == 1
    mod = p*p
    t, b = terms(p)
    B, W, H, K, S = observers(p, t, b, mod)
    T = reflected_tail(p, [x % p for x in t])
    chi = 1 if pow(2, (p-1)//2, p) == 1 else -1

    # Proved all-prime identities, checked as exact implementation regressions.
    assert B % p == chi % p, (p, 'quadratic character', B)
    assert H == ((B*W + p*T) * pow(2, -1, mod)) % mod, (p, 'tail reflection')
    assert K == (3*p*pow(2, -1, mod)) % mod, (p, 'previous boundary theorem')

    # Finite observations only. These are NOT universal proofs.
    assert T == 3*(1-chi), (p, 'conjectural T pattern', T, chi)
    assert W == p, (p, 'original W p2 observation', W)
    assert S == (-chi*p) % mod, (p, 'Le Lan p2 conjecture', S)

    # Validate the signed p-adic reflection directly against the original b_j.
    if p <= 73 or p == 373:
        m = (p - 1) // 6
        u = 1
        for s in range(2*m):
            j = p-1-s
            assert b[j] % p == 0
            assert (-(b[j]//p)) % p == u, (p, s, 'reflection sign')
            u = u * 4*(s+1) * pow(2*s+3, -1, p) % p

    # Independent original integer binomials rather than the term recurrences.
    if p <= 73 or p == 373:
        t0, b0 = direct_terms(p, mod)
        assert (t, b) == (t0, b0), (p, 'binomial witness mismatch')
        assert observers(p, t0, b0, mod) == (B, W, H, K, S)
    return chi, B, W, H, K, S, T


if __name__ == '__main__':
    primes = [p for p in range(7, 10000) if is_prime(p) and p % 6 == 1]
    for p in primes:
        check_prime(p)
    print('primes_p_lt_10000_p_1mod6:', len(primes))
    for p in (7, 13, 19, 373):
        print('certificate:', p, check_prime(p))
    print('PASS_AUTHOR_SIDE_TAIL_REFLECTION_P2_AND_FINITE_CONJECTURE_CHECKS')
