#!/usr/bin/env python3
"""D25 exact original W216 three-band p^3 certificate (author-side).
For p=6m+1, certify the zero/first grade jets and the entire
valuation partition against the independent original integer binomial sum.
No native H0/B0 computation, mathematical admission or floating-point steps.
"""
from math import comb, factorial

PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 109, 157, 181, 373)


def inv(a, modulus):
    return pow(a % modulus, -1, modulus)


def harmonics(n, modulus, power=1):
    result = [0]
    for j in range(1, n + 1):
        result.append((result[-1] + inv(j ** power, modulus)) % modulus)
    return result


def original_weighted(k, modulus):
    return ((6 * k + 1) * comb(2 * k, k) ** 2 *
            comb(3 * k, k) * inv(216, modulus) ** k) % modulus


def band_certificate(p):
    assert p > 3 and p % 6 == 1
    modulus = p ** 3
    m = (p - 1) // 6
    a, b, c = 2 * m, 3 * m, 4 * m
    h1, h2 = harmonics(c, modulus), harmonics(c, modulus, 2)
    fac = [factorial(j) for j in range(p)]

    def fraction(numerator, denominator):
        return (numerator % modulus) * inv(denominator, modulus) % modulus

    def hdelta(n, k, h):
        return (h[n] - h[n - k]) % modulus

    sums = [0, 0, 0, 0]
    for k in range(p):
        if k <= a:
            zero = ((-1 if k & 1 else 1) * comb(a, k) *
                    comb(b, k) * comb(c, k))
            zero = fraction(zero, 2 ** k)
            alpha = (fraction(hdelta(a, k, h1), 3) +
                     fraction(hdelta(b, k, h1), 2) +
                     fraction(2 * hdelta(c, k, h1), 3)) % modulus
            beta = (fraction(hdelta(a, k, h2), 9) +
                    fraction(hdelta(b, k, h2), 4) +
                    fraction(4 * hdelta(c, k, h2), 9)) % modulus
            jet = (1 - p * alpha +
                   p * p * inv(2, modulus) * (alpha * alpha - beta)) % modulus
            coeff, grade = zero * jet % modulus, 0
        elif k <= b:
            numerator = fac[a] * fac[k - a - 1] * fac[b] * fac[c]
            denominator = fac[b - k] * fac[c - k] * fac[k] ** 3 * 2 ** k
            unit = fraction(numerator, denominator)
            gamma = (fraction(h1[k - a - 1] - h1[a], 3) -
                     fraction(h1[b] - h1[b - k], 2) -
                     fraction(2 * (h1[c] - h1[c - k]), 3)) % modulus
            coeff, grade = p * fraction(unit, 3) * (1 + p * gamma) % modulus, 1
        elif k <= c:
            numerator = (fac[a] * fac[k - a - 1] * fac[b] *
                         fac[k - b - 1] * fac[c])
            denominator = fac[c - k] * fac[k] ** 3 * 2 ** k
            sign = -1 if (b + k) & 1 else 1
            coeff, grade = p * p * fraction(sign * numerator, 6 * denominator) % modulus, 2
        else:
            coeff, grade = 0, 3

        certificate = (6 * k + 1) * coeff % modulus
        direct = original_weighted(k, modulus)
        assert certificate == direct, (p, k, grade, certificate, direct)
        sums[grade] = (sums[grade] + certificate) % modulus

    total = sum(sums) % modulus
    assert total == sum(original_weighted(k, modulus) for k in range(p)) % modulus
    lower = sum(sums[:2]) % modulus
    assert lower % (p*p) == p  # here: tested p, not used to prove universality
    assert total == p
    return {
        'p': p, 'm': m, 'counts': [a+1, b-a, c-b, p-1-c],
        'grade_sums_mod_p3': sums,
        'lower_mod_p3': lower,
        'lower_residue_mod_p': ((lower-p)//(p*p)) % p,
        'grade2_residue_mod_p': (sums[2]//(p*p)) % p,
        'original_W_mod_p3': total
    }


def main():
    for p in PRIMES:
        print(band_certificate(p))
    print('PASS: 13 primes; all k; integer modular reconstruction vs original binomials')


if __name__ == '__main__':
    main()
