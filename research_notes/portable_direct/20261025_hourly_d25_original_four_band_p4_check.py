#!/usr/bin/env python3
"""Independent exact integer certificates for the original signed W_p four bands.

Author-side finite computations. No native CM/Frobenius experiment is run.
"""
from math import isqrt


def primes_below(bound):
    for n in range(7, bound):
        if n % 6 != 1:
            continue
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def four_band_and_direct(p):
    assert p >= 7 and p % 6 == 1
    m, mod = (p - 1) // 6, p ** 4
    roots = ((2 * m, pow(3, -1, mod)),
             (3 * m, pow(2, -1, mod)),
             (4 * m, 2 * pow(3, -1, mod) % mod))
    half, sixth = pow(2, -1, mod), pow(6, -1, mod)
    b = 1  # d_n/(6n+1), no illegal inverse when 6n+1=p
    ell = sigma = tau = 0
    direct_base = 1  # direct original Pochhammer quotient without 6n+1
    signed_w = 0
    band = [0, 0, 0, 0]
    last_d = None
    for n in range(p):
        d = (6 * n + 1) * b % mod
        grade = (n > 2 * m) + (n > 3 * m) + (n > 4 * m)
        if grade == 0:
            jet = (1 + p * ell
                   + p ** 2 * (ell ** 2 - sigma) * half
                   + p ** 3 * (ell ** 3 - 3 * ell * sigma + 2 * tau) * sixth)
        elif grade == 1:
            jet = 1 + p * ell + p ** 2 * (ell ** 2 - sigma) * half
        elif grade == 2:
            jet = 1 + p * ell
        else:
            jet = 1
        band[grade] = (band[grade] + p ** grade * d * jet) % mod
        signed_w = (signed_w + (6 * n + 1) * direct_base) % mod
        if n == p - 1:
            last_d = d % p
        if n == p - 1:
            continue
        j = n
        increment = 1
        for s, alpha in roots:
            if j == s:
                increment = increment * alpha % mod
            else:
                t = (j - s) % mod
                inverse = pow(t, -1, mod)  # 0 < |j-s| < p
                increment = increment * t % mod
                ell = (ell + alpha * inverse) % mod
                sigma = (sigma + alpha * alpha * inverse * inverse) % mod
                tau = (tau + alpha ** 3 * inverse ** 3) % mod
        b = b * increment * pow(2 * (n + 1) ** 3, -1, mod) % mod
        direct_base = (direct_base * (2 * n + 1) * (3 * n + 1) *
                       (3 * n + 2) * pow(36 * (n + 1) ** 3, -1, mod)) % mod
    assert signed_w == sum(band) % mod
    assert last_d == 5  # universal source-tail endpoint theorem
    return tuple(band), signed_w


def reverse_tail_kernel(p):
    """Independent mod-p branch computation, no full p^4 jets or n! modulo p^4."""
    m = (p - 1) // 6
    term = 5
    total = 0
    distinct_nonzero = True
    for k in range(2 * m):
        total = (total + term) % p
        distinct_nonzero &= (term != 0)
        if k == 2 * m - 1:
            break
        # d_{p-2-k}/d_{p-1-k}, exact finite-field reverse transfer
        j = k + 1
        numerator = 2 * j ** 3 * (6 * j + 5)
        denominator = (6 * j - 1) * (j * 3 + 2) * (2 * j + 1) * (3 * j + 1)
        # divide by (j+2/3)(j+1/2)(j+1/3): multiply numerator by 18
        term = term * numerator * 18 * pow(denominator, -1, p) % p
    assert distinct_nonzero
    return total


def main():
    cases = sorted(set(primes_below(600)) | {1327, 19963})
    for p in cases:
        b, w = four_band_and_direct(p)
        tail = reverse_tail_kernel(p)
        assert b[3] == (p ** 3) * tail
        assert w % p ** 3 == p
        if p in {7, 13, 19, 211, 1327, 19963}:
            print(f"p={p} m={(p-1)//6} B={b} W_mod_p4={w} "
                  f"B3_div_p3={tail} last_d=5 W_minus_p_div_p3={(w-p)//p**3%p}")
    print(f"PASS: {len(cases)} primes, original recurrence vs four-band; "
          "independent reverse-tail kernel; exact p^4; universal last coefficient")


if __name__ == "__main__":
    main()
