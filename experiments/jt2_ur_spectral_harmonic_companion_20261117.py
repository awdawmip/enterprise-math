#!/usr/bin/env python3
"""Independent exact rational checks for the JT2 spectral-harmonic companion.
Finite checks are examples; the general coefficient lemma has a symbolic proof.
"""
from fractions import Fraction as F
from math import comb


def q_coeffs(m):
    c0 = F((-1)**m * comb(2*m, m), 4**m)
    c = [c0]
    for j in range(m):
        c.append(c[-1] * F((j-m)*(2*j+2*m+1), (j+1)*(2*j+1)))
    return c


def z_derivative_coeffs(m):
    # Independently differentiate the spectral coefficient recurrence.
    C = m*(2*m+1)
    a, aprime = F(1), F(0)
    c0 = F((-1)**m * comb(2*m, m), 4**m)
    result = []
    for j in range(m+1):
        result.append(c0*aprime)
        if j < m:
            d = (j+1)*(2*j+1)
            a, aprime = a*F(j*(2*j+1)-C, d), (aprime*(j*(2*j+1)-C)-a)/d
    return result


def weights(m):
    t = F(0)
    out = [t]
    for i in range(m):
        t += F(1, (m-i)*(2*m+2*i+1))
        out.append(t)
    return out


def val_at_half(c):
    return sum((v*F(1, 2**j) for j, v in enumerate(c)), F(0))


def modq(q, p):
    if q.denominator % p == 0:
        raise ValueError("non-unit denominator")
    return q.numerator * pow(q.denominator, -1, p) % p


def direct_J(c):
    m = len(c)-1
    return sum((c[j]*c[k]*F(1, (2*(j+k)+1)*2**(j+k))
                for j in range(m+1) for k in range(m+1)), F(0))


def weighted_S(c):
    m = len(c)-1
    return sum((c[j]*F(1, (2*m+2*j+1)*2**(m+j))
                for j in range(m+1)), F(0))


def check_symbolic():
    for m in range(1, 9):
        c = q_coeffs(m)
        zs = z_derivative_coeffs(m)
        ts = weights(m)
        assert zs == [c[j]*ts[j] for j in range(m+1)], m
    return 8


def check_modular():
    data = []
    for p in (13, 19, 37, 43, 61, 67, 109):
        m = (p-1)//6
        c = q_coeffs(m)
        H = [F(0)]
        for i in range(1, 2*m+1):
            H.append(H[-1]+F(1, i))
        harm = [3*(H[m]-H[m-j]-H[2*m]+H[2*m-j])
                for j in range(m+1)]
        t = weights(m)
        assert all(modq(t[j], p) == modq(harm[j], p)
                   for j in range(m+1))
        val = val_at_half(c)
        assert modq(val, p) == 0, "CM0 premise failed"
        u = modq(val, p*p)//p
        d = modq(val_at_half([j*c[j] for j in range(1, m+1)]), p)
        z = modq(val_at_half([c[j]*harm[j]
                              for j in range(m+1)]), p)
        J = modq(direct_J(c), p)
        s = modq(weighted_S(c), p)
        cm = modq(c[m], p)
        assert (2*J-d*z-2*cm*s) % p == 0, p
        eps = (18*u*d-2*J-3) % p
        data.append((p, m, eps))
        assert eps == 0, p
    return data


if __name__ == "__main__":
    print("exact spectral derivative coefficients m=1..", check_symbolic())
    print("modular checks (p,m,epsilon):", check_modular())
