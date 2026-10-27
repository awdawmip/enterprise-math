#!/usr/bin/env python3
"""GH-11/GH-12 original-S reflection certificate (author checks only).

Only standard-library modular integer arithmetic and exact rational arithmetic.
No claim of native Enterprise Math execution or independent review is made.
"""
from fractions import Fraction
from math import factorial, isqrt, comb


def prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n) + 1))


def legendre_neg3(p):
    result = pow(-3 % p, (p - 1) // 2, p)
    assert result in (1, p - 1)
    return 1 if result == 1 else -1


def core(p):
    assert prime(p) and p > 3 and p % 4 == 1
    d, modulus = (p - 1) // 4, p * p
    C = [1]
    for r in range(d):
        a = 9 * (4 * r + 1) ** 3
        b = (4 * r + 2) * (4 * r + 3) * (4 * r + 4)
        assert b % p
        C.append(C[-1] * a * pow(b, -1, modulus) % modulus)
    T = sum((8 * r + 1) * c for r, c in enumerate(C)) % modulus
    assert C[d] % p != 0
    assert T % p == 0
    return d, modulus, C, T


def original_s_evidence(p, d, modulus):
    # Independent factorial-source calculation, including the genuine tail.
    h = []
    f4r, invfac, invpower9 = 1, 1, 1
    inv2304 = pow(2304, -1, modulus)
    for r in range(p):
        if r:
            for j in range(4 * r - 3, 4 * r + 1):
                f4r = f4r * j % modulus
            invfac = invfac * pow(r, -1, modulus) % modulus
            invpower9 = invpower9 * inv2304 % modulus
        h.append(f4r * pow(invfac, 4, modulus) * invpower9 % modulus)
    full = sum((8 * r + 1) * h[r] for r in range(p)) % modulus
    short = sum((8 * r + 1) * h[r] for r in range(d + 1)) % modulus
    tail = (full - short) % modulus
    chi = legendre_neg3(p)
    assert full == p * chi % modulus  # only the p^2 consequence of GZ
    assert short % p == 0 and tail % p == 0
    assert all(h[r] % p == 0 for r in range(d + 1, p))
    return h, full, short, tail, chi


def lambda_plus(p, r):
    x = 0
    for i in range(1, r + 1):
        x += sum(pow(4 * i - j, -1, p) for j in (1, 2, 3))
        x -= 3 * pow(4 * i, -1, p)
    return x % p


def full_certificate(p):
    d, modulus, C, T = core(p)
    h, full, short, tail, chi = original_s_evidence(p, d, modulus)
    H = sum(h[:d + 1]) % p
    Lambda = [0]
    for r in range(1, d + 1):
        increment = sum(pow(4 * r - j, -1, p) for j in (1, 2, 3)) - 3 * pow(4 * r, -1, p)
        Lambda.append((Lambda[-1] + increment) % p)
    K = sum((8 * r + 1) * h[r] * Lambda[r] for r in range(d + 1)) % p
    for r in range(d + 1):
        ratio = C[d - r] * pow(C[d], -1, modulus) % modulus
        expected = h[r] * (1 - p * Lambda[r]) % modulus
        assert ratio == expected, (p, r, ratio, expected)
    normalized = T * pow(C[d], -1, modulus) % modulus
    rhs = (-short + p * (2 * H + K)) % modulus
    assert normalized == rhs
    assert normalized % p == 0
    second = normalized // p
    tail_div_p = tail // p
    rhs_second = (-chi + tail_div_p + 2 * H + K) % p
    assert second == rhs_second
    return (p, d, T // p, C[d] % p, chi, second, tail_div_p % p, H, K)


def check_exact_rationals(p):
    d = (p - 1) // 4
    C = [Fraction(1)]
    for r in range(d):
        C.append(C[-1] * Fraction(9 * (4 * r + 1) ** 3,
                                     (4 * r + 2) * (4 * r + 3) * (4 * r + 4)))
    for r in range(d + 1):
        inverse_product = Fraction(1)
        for i in range(1, r + 1):
            inverse_product *= Fraction((p + 1 - 4 * i) * (p + 2 - 4 * i) * (p + 3 - 4 * i),
                                        9 * (p - 4 * i) ** 3)
        assert C[d - r] / C[d] == inverse_product
    return p, d



def check_gh13(p):
    """GH13: 3-mod-4 original-S defect equality, one exact finite case."""
    assert prime(p) and p > 3 and p % 4 == 3
    d = (p - 3) // 4
    c, h, b = 1, 1, 1
    C, H, B = [1], [1], [1]
    for r in range(d):
        c = c * 9 * (4*r+1)**3 * pow((4*r+2)*(4*r+3)*(4*r+4), -1, p) % p
        h = h * (4*r+1)*(4*r+2)*(4*r+3) * pow(576*(r+1)**3, -1, p) % p
        b = b * (4*r+3)*(4*r+4)*(4*r+5) * pow(9*(4*r+6)**3, -1, p) % p
        C.append(c); H.append(h); B.append(b)
    U = []
    for r in range(d+1):
        u = (4*r+1)*pow(2*r+1, -3, p)*pow(comb(2*r,r),-4,p)*pow(4,4*r,p)%p
        U.append(u)
        assert B[r] == H[r]*u % p
    original_short = sum((8*r+1)*H[r] for r in range(d+1))%p
    residual = sum(H[r]*((8*r+5)*U[r]-(8*r+1)) for r in range(d+1))%p
    T = sum((8*r+1)*C[r] for r in range(d+1))%p
    assert original_short == 0  # finite independent check of the GZ implication
    assert T*pow(C[d],-1,p)%p == -residual%p
    # This last zero is finite empirical checking, NOT a proof for all p.
    assert residual == 0 and T == 0
    return p, d, residual, T

def main():
    checked = 0
    # Both p^1 theorem and stronger (unproved) second-digit conjecture checked
    # on the entire stated finite range. A test is not a universal proof.
    for p in range(5, 10000):
        if not prime(p) or p % 4 != 1:
            continue
        d, modulus, C, T = core(p)
        chi = legendre_neg3(p)
        second = (T * pow(C[d], -1, modulus) % modulus) // p
        assert second == chi % p, (p, second, chi)
        checked += 1
    print('GH11 modulo-p + experimental GH12-strengthened chi:',
          checked, 'primes p<10000 congruent 1 mod 4, PASS')
    exact = [check_exact_rationals(p) for p in (5, 13, 17, 29, 37, 41)]
    print('Exact rational reflected identity:', exact, 'PASS')
    fully_checked = [p for p in range(5, 2000) if prime(p) and p % 4 == 1]
    witnesses = [full_certificate(p) for p in fully_checked]
    print('GH12 independent factorial-tail/moments modulo p^2:',
          len(witnesses), 'primes p<2000 congruent 1 mod 4, PASS')
    gh13 = [check_gh13(p) for p in range(7, 2000) if prime(p) and p%4 == 3]
    print('GH13 S-defect exact relation and finite zero observation:', len(gh13), "primes p<2000 congruent 3 mod 4, PASS")
    print('Witnesses (p,d,T/p mod p,C_d mod p,chi,T/(pC_d),E/p,H,K):')
    for v in witnesses:
        if v[0] in (5, 13, 17, 29, 181, 373):
            print(v)


if __name__ == '__main__':
    main()
