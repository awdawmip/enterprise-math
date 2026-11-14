"""R149: exact complement duality and conditional CRT autocorrelation checks.

Scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
All arithmetic is Python arbitrary-precision integer/Fraction.
"""
from fractions import Fraction as F
from math import gcd

def slope_support(w):
    m = len(w)
    s = [0]
    for ch in w:
        s.append(s[-1] + int(ch))
    lo, hi = F(0), F(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            lo = max(lo, F(s[j] - s[i] - 1, j - i))
            hi = min(hi, F(s[j] - s[i] + 1, j - i))
    if lo >= hi:
        return None
    a, b, c, d = lo.numerator, lo.denominator, hi.numerator, hi.denominator
    U = min(b * (s[j] + 1) - j * a for j in range(m + 1))
    V = max(d * s[j] - j * c for j in range(m + 1))
    return a, b, c, d, U, V

def count(p, K):
    a, b, c, d, U, V = p
    L = K - 1
    lo, hi = F(L * a - U, b), F(L * c - V, d)
    ceil_hi = -((-hi).numerator // (-hi).denominator)
    floor_lo = lo.numerator // lo.denominator
    return ceil_hi - floor_lo - 1

def covariance(p):
    a, b, c, d, U, V = p
    g = gcd(b, d)
    mid = F(g - 1, 2)
    return sum(((F((a * t - U) % g) - mid) *
                (F((V - c * t) % g) - mid) for t in range(g)), F(0)) / (g * b * d)

def autocorrelation(p):
    a, b, c, d, U, V = p
    g = gcd(b, d)
    assert (a + c) % g == 0
    lam = (U + V) % g
    return F(g * g - 1 - 6 * lam * (g - lam), 12 * b * d)

def main():
    nwords = ncomp = nauto = nrev = ncong = 0
    npositive = 0
    for m in range(1, 16):
        for i in range(1 << m):
            w = format(i, f"0{m}b")
            p = slope_support(w)
            if p is None:
                continue
            nwords += 1
            wb = ''.join('1' if v == '0' else '0' for v in w)
            pb = slope_support(wb)
            a, b, c, d, U, V = p
            assert pb == (d - c, d, b - a, b, d - V, b - U)
            for K in (2, 3, 4, 7, 15, 31):
                assert count(p, K) == count(pb, K)
                ncomp += 1
            g = gcd(b, d)
            if g > 1:
                ncong += 1
                assert (a + c) % g == 0  # finite observation, not an assumed theorem
            if (a + c) % g == 0:
                assert covariance(p) == autocorrelation(p)
                assert covariance(p) == covariance(slope_support(w[::-1]))
                nauto += 1
                nrev += 1
            npositive += covariance(p) > 0
    assert (nwords, ncomp, nauto, nrev, ncong, npositive) == (
        1906, 11436, 1906, 1906, 298, 6)
    print('R149_COMPLEMENT_AUTOCORRELATION_PASS')
    print(dict(words=nwords, complement_checks=ncomp,
               conditional_autocorrelation_checks=nauto,
               reversal_covariance_checks=nrev,
               noncoprime_congruence_observations=ncong,
               positive_covariance_words=npositive))

if __name__ == '__main__':
    main()
