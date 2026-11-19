#!/usr/bin/env python3
"""Exact Fraction certificate for the EC49FUJ n=15 count-two minimax phase.

Pure standard library.  The count law is the clipped-price observer inherited
from frozen BRC16943; this program verifies algebraic/finite certificates,
not independent Bellman optimality or native X6 physical dynamics.
"""
from fractions import Fraction as Q
from math import comb

BETA = Q(3, 637)
ETA = Q(141024, 1653649)
U_I = Q(21829245984, 45529434409)
U_E = Q(4822040484, 8132285009)
L = Q(61, 4000)
X_B_LO, X_B_HI = Q(2956, 10**7), Q(2957, 10**7)
X_2_LO, X_2_HI = Q(15172, 10**6), Q(15174, 10**6)


def T_E(x):
    return (1-x)*(1+ETA*x)


def T_I(x):
    return (1-x)*(1-BETA*x)


def p_minus_r_u_to_power(x, exponent):
    """Sign-changing endpoint likelihood comparison for K=1."""
    t = T_E(x)
    return (1-t) - (1-U_E*t)*U_E**exponent


def count_two_sign(x):
    """Sign of L_E(K=2)-1, via r^2 u^13 - p^2."""
    t = T_E(x)
    return (1-U_E*t)**2*U_E**13-(1-t)**2


def mul(a, b):
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i+j] += v*w
    return out


def poly_pow(p, exponent):
    out = [Q(1)]
    for _ in range(exponent):
        out = mul(out, p)
    return out


def count_two_gap_coefficients(u, polynomial_T):
    """D2(T,u)=15(1-u^14)T^14 - 14(1-u^15)T^15."""
    p14 = poly_pow(polynomial_T, 14)
    p15 = mul(p14, polynomial_T)
    return [15*(1-u**14)*(p14[i] if i < len(p14) else 0)
            - 14*(1-u**15)*p15[i] for i in range(len(p15))]


def endpoint_gap_coefficients():
    ti = [Q(1), -(1+BETA), BETA]
    te = [Q(1), ETA-1, -ETA]
    ci = count_two_gap_coefficients(U_I, ti)
    ce = count_two_gap_coefficients(U_E, te)
    return [v-w for v, w in zip(ci, ce)]


def evaluate(coefs, x):
    z = Q(0)
    for value in reversed(coefs):
        z = z*x+value
    return z


def bernstein_on_zero_L(coefs, L):
    """Power-to-degree-n Bernstein coefficients on x in [0,L]."""
    n = len(coefs)-1
    a = [v*L**i for i, v in enumerate(coefs)]
    return [sum((a[i]*Q(comb(k,i), comb(n,i)) for i in range(k+1)), Q(0))
            for k in range(n+1)]


def D2(T,u):
    return 15*T**14*(1-u**14)-14*T**15*(1-u**15)


def main():
    assert Q(0) < X_B_LO < X_B_HI < X_2_LO < X_2_HI < L < Q(1,20)
    assert Q(2,5) < U_I < U_E < Q(3,5)
    assert T_I(L) > Q(13,14)  # T(theta,x) >= T_I(x) for all theta
    assert T_E(L) < 1
    # x_B root: p - r*u^14 switches negative to positive.
    assert p_minus_r_u_to_power(X_B_LO,14) < 0
    assert p_minus_r_u_to_power(X_B_HI,14) > 0
    # x_2 root: r^2*u^13 - p^2 switches positive to negative.
    assert count_two_sign(X_2_LO) > 0
    assert count_two_sign(X_2_HI) < 0

    coefficients = endpoint_gap_coefficients()
    bernstein = bernstein_on_zero_L(coefficients,L)
    assert len(coefficients) == len(bernstein) == 31
    assert all(v > Q(1,20000) for v in bernstein)
    assert bernstein[0] == evaluate(coefficients,Q(0))
    assert bernstein[-1] == evaluate(coefficients,L)
    # A rational interior point, which lies in the phase, and a direct identity.
    x=Q(1,1000)
    gap=D2(T_I(x),U_I)-D2(T_E(x),U_E)
    assert evaluate(coefficients,x)==gap
    assert gap > Q(1,20000)
    risk=(1-D2(T_E(x),U_E))/2
    assert Q(0) < risk < Q(1,2)
    print('PASS; power degree=30; positive Bernstein coefficients=31/31')
    print('uniform endpoint gap J(x) > 1/20000 on [0,61/4000]')
    print('first-count bracket=',X_B_LO,X_B_HI)
    print('second-count bracket=',X_2_LO,X_2_HI)
    print('min Bernstein coefficient (decimal)=',format(float(min(bernstein)),'.15g'))
    print('example x=1/1000: minimax risk=',format(float(risk),'.15g'))
    print('example x=1/1000: D2(infinity)-D2(E)=',format(float(gap),'.15g'))
    print('scope: author exact algebra+certificate, model-parent dependent; NOT_REVIEWED')

if __name__=='__main__':
    main()
