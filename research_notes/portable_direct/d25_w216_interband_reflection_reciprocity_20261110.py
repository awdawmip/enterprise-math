#!/usr/bin/env python3
"""Exact author-side original W216 grade-1/2 reflection certificate; no external libraries."""
from math import comb

def primes(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for n in range(2, int(limit**0.5) + 1):
        if sieve[n]:
            sieve[n*n:limit+1:n] = b"\x00" * ((limit - n*n)//n + 1)
    return (p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1)

def verify(p, independent=False):
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 6
    modulus = p**3
    A = [1]
    for k in range(p - 1):
        A.append(A[-1] * (2*k + 1) * (3*k + 1) * (3*k + 2)
                 * pow(36 * (k + 1)**3, -1, modulus) % modulus)
    u0 = A[2*m + 1] // p % p
    assert u0 != 0
    paired_grade_two = 0
    original_grade_two = 0
    g = 1
    dual_sum = 0
    for j in range(m):
        k = 2*m + 1 + j
        h = p - k
        assert 3*m + 1 <= h <= 4*m
        assert A[k] % p == 0 and A[h] % (p*p) == 0
        L = A[k] // p % p
        H = A[h] // (p*p) % p
        assert L != 0 and H != 0
        assert 36 * pow(k, 3, p) * L * H % p == 1
        assert L == u0 * g % p
        paired_grade_two = (paired_grade_two + (1 - 6*k) *
                            pow(36 * k**3 * L, -1, p)) % p
        original_grade_two = (original_grade_two + (6*h + 1) * H) % p
        dual_sum = (dual_sum + (2*j + 1) *
                    pow((3*j + 2)**3 * g, -1, p)) % p
        if independent:
            for index in (k, h):
                raw = comb(2*index, index)**2 * comb(3*index, index)
                raw = raw * pow(216, -index, modulus) % modulus
                assert raw == A[index]
        if j + 1 < m:
            ratio = (3*(6*j + 7)*(j + 1)*(3*j + 4) *
                     pow(4*(3*j + 5)**3, -1, p)) % p
            g = g * ratio % p
    assert paired_grade_two == original_grade_two
    assert -9 * pow(4*u0, -1, p) * dual_sum % p == original_grade_two
    return (m, u0, original_grade_two)

def main():
    ps = list(primes(2000))
    total_pairs = 0
    for p in ps:
        m, u0, w2 = verify(p, independent=p in (7, 13, 19, 373))
        total_pairs += m
        if p in (7, 13, 19, 373, 997, 1999):
            print("p=%d m=%d u0=%d W2_over_p2_modp=%d" % (p, m, u0, w2))
    print("PASS primes=%d pairs=%d independent_original_checks=%d" %
          (len(ps), total_pairs, 2*sum((p-1)//6 for p in (7,13,19,373))))
    assert len(ps) == 148 and total_pairs == 22952

if __name__ == "__main__":
    main()
