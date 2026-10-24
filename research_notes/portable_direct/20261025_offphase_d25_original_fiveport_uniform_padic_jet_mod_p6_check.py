#!/usr/bin/env python3
"""Author-side exact checks for a uniform source-labeled WZ p-adic jet generator.
Only Python's standard library is used. It is not a native CM/DP experiment.
"""
from fractions import Fraction as F
from math import factorial, isqrt

E = [2, 2, 2, 1, 1]
C = [-1, 2, 5, 8, 11]
A4 = F(240151883718153049, 11643159880396800000)


def primes_below(limit):
    return [p for p in range(13, limit) if p % 6 == 1
            and all(p % d for d in range(2, isqrt(p) + 1))]


def H(n, s):
    return sum((F(1, j ** s) for j in range(1, n + 1)), F(0))


def q(p, b):
    return (b ** (p - 1) - 1) // p


def alpha_beta(p, order):
    m = (p - 1) // 6
    n = 2 * m
    assert p == 6 * m + 1 and p >= 13 and order <= p - 2
    a, b, t = q(p, 2), q(p, 3), q(p, 108)
    alpha, beta = {}, {}
    for s in range(1, order + 1):
        alpha[s] = (F((-1) ** s * t ** s, s)
                    - F(2, s) * (H(n, s) - 1)
                    + F((-1) ** (s + 1), s) * (2 * H(p - 2, s) - H(n - 1, s)))
        bracket = (-sum((F(e, c ** s) for e, c in zip(E, C)), F(0))
                   - 2 * a ** s - 3 * b ** s
                   + 2 * (-1) ** s * H(n - 1, s) + 2 * H(p - 1, s)
                   + H(5, s) + 2 ** s * H(4, s) + 2 ** s
                   - 2 * H(2, s) - H(n + 4, s))
        beta[s] = F((-1) ** (s + 1), s) * bracket
    return alpha, beta


def exp_jet(log_coeffs, order):
    """e_0=1, j*e_j=sum_{s<=j} s*ell_s*e_{j-s}; exact rational."""
    e = [F(1)]
    for j in range(1, order + 1):
        e.append(sum((s * log_coeffs[s] * e[j - s]
                      for s in range(1, j + 1)), F(0)) / j)
    return e


def mod_q(x, p, digits):
    modulus = p ** digits
    assert x.denominator % p, ("non-unit denominator", p, x.denominator)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def C_edge(p):
    return F((p + 1) * (2 * p - 1) ** 2 * (30 * p ** 2 + 77 * p + 40),
             2 * (p + 2) * (2 * p + 1) * (4 * p - 1) * (4 * p + 5))


def ratio(k, p):
    return F((2 * p + 2 * k + 3) * (2 * p + 3 * k - 1) * (2 * p + 3 * k),
             4 * (2 * p + 3 * k + 1) * (p + k + 2) * (4 * p + 3 * k + 11))


def B_ports(p):
    total, product = F(0), F(1)
    for j in range(1, 5):
        total += (6 * p + 6 * j + 7) * product
        if j < 4:
            product *= ratio(j, p)
    return total


def uniform_jet(p, N=5):
    m = (p - 1) // 6
    alpha, beta = alpha_beta(p, N)
    u = 2 * m * sum((v * p ** j for j, v in enumerate(exp_jet(alpha, N))), F(0))
    sigma = F(3, 220) * sum((v * p ** j for j, v in enumerate(exp_jet(beta, N-1))), F(0))
    return u * C_edge(p) + p * sigma * B_ports(p), u, sigma


def source_U(p):
    n = (p - 1) // 3
    value = F(p - 1, 3 * 108 ** (p - 1))
    for k in range(2, n + 1):
        value *= (1 - F(p, k)) ** 2
    for j in range(1, p - 1):
        value *= (1 + F(p, j)) ** 2
    for j in range(1, n):
        value /= (1 + F(p, j))
    return value


def V(r, t):
    return F(factorial(6 * r) * factorial(4 * r + 2 * t) * factorial(3 * t),
             3 ** (6 * r) * 216 ** t * factorial(2 * r) * factorial(t) ** 2
             * factorial(2 * r + t) ** 2 * factorial(4 * r + t))


def source_W(r, t):
    return (6 * t + 12 * r + 1) * V(r, t)


def original_quotient(p):
    m = (p - 1) // 6
    a = sum((source_W(m + 1, t) for t in range(4 * m + 5)), F(0))
    b = sum((source_W(m, t) for t in range(4 * m + 1)), F(0))
    return (a - b) / p


def check():
    selected = primes_below(1000)
    assert len(selected) == 79
    a0 = F(250809, 17920)
    a1 = F(466056841, 63974400)
    a2 = F(22193173931, 114194304000)
    a3 = F(-98135062039471, 1630694661120000)
    for p in selected:
        m = (p - 1) // 6
        total, u, sigma = uniform_jet(p)
        assert mod_q(u - source_U(p), p, 6) == 0, (p, "old edge")
        assert mod_q(sigma - V(m + 1, 4 * m + 1) / p ** 2, p, 5) == 0, (p, "tail")
        b4 = a0 + a1 * p + a2 * p ** 2 + a3 * p ** 3 + A4 * p ** 4
        assert mod_q(B_ports(p) - b4, p, 5) == 0, (p, "transfer A4")
        direct_5_port = (source_U(p) * C_edge(p)
                         + sum((source_W(m + 1, 4 * m + j) / p
                                for j in range(1, 5)), F(0)))
        assert mod_q(total - direct_5_port, p, 6) == 0, (p, "source ports")
    print("PASS: 79/79 p<1000 target primes: U mod p^6, sigma mod p^5, B mod p^5, five labeled source ports mod p^6")
    independent = [13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109, 127, 211]
    for p in independent:
        got, _, _ = uniform_jet(p)
        assert mod_q(original_quotient(p) - got, p, 6) == 0, (p, "raw S difference")
    print("PASS: 14/14 independent raw factorial S_{m+1}-S_m reconstructions mod p^6")
    print("p=13 witness (S_{m+1}-S_m)/p mod 13^6:", mod_q(original_quotient(13), 13, 6))


if __name__ == "__main__":
    check()
