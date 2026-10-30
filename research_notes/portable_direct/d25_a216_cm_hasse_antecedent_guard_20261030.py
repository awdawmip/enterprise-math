#!/usr/bin/env python3
"""Independent exact finite-field regression for D25 CM/Hasse antecedent.

This verifies polynomial identities at all p = 1 (mod 6) below the bound,
plus supersingular CM-specialization zero at p = 13,19 (mod 24).
Finite computations do not replace the uniform Deuring theorem.
Only Python standard library is used; all arithmetic is exact.
"""
from fractions import Fraction
from math import comb


def primes_below(n):
    isprime = bytearray(b'\x01') * n
    isprime[:2] = b'\x00\x00'
    for x in range(2, int(n ** .5) + 1):
        if isprime[x]:
            isprime[x*x:n:x] = b'\x00' * len(isprime[x*x:n:x])
    return [p for p in range(n) if isprime[p]]


def mul2(x, y, p):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % p,
            (x[0]*y[1] + x[1]*y[0]) % p)


def eval2(coefficients, t, p):
    acc = (0, 0)
    for c in reversed(coefficients):
        acc = mul2(acc, t, p)
        acc = ((acc[0] + c) % p, acc[1])
    return acc


def br(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mulr(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def powr(x, n):
    out = (Fraction(1), Fraction(0))
    for _ in range(n):
        out = mulr(out, x)
    return out


def inverse_r(x):
    norm = x[0]*x[0] - 2*x[1]*x[1]
    assert norm != 0
    return (x[0]/norm, -x[1]/norm)


def cm_j_discriminant_check():
    t = (Fraction(1, 2), Fraction(-1, 4))
    one = (Fraction(1), Fraction(0))
    omt = br(one, (-t[0], -t[1]))
    invariant = mulr(t, omt)
    assert invariant == (Fraction(1,8), Fraction(0))
    c = br(one, (8*t[0], 8*t[1]))
    j = mulr((Fraction(27), Fraction(0)),
             mulr(powr(c, 3), inverse_r(mulr(t, powr(omt, 3)))))
    assert j == (Fraction(2417472), Fraction(-1707264)), j
    j2 = powr(j, 2)
    h = br(j2, br((-4834944*j[0], -4834944*j[1]),
                     (Fraction(14670139392), Fraction(0))))
    assert h == (0, 0), h
    return j


def check_prime(p):
    assert p >= 7 and p % 6 == 1
    m = (p - 1)//6
    inv4 = pow(4, -1, p)
    inv2 = pow(2, -1, p)
    # Finite Gauss polynomial P_m(z)=sum C(m,k)C(2m,k) z^k.
    P = [comb(m,k)*comb(2*m,k) % p for k in range(m+1)]
    # Exact quadratic transform P_m(4u(1-u)), computed as a polynomial.
    P_quad = [0]*(2*m+1)
    for k, a in enumerate(P):
        scalar = a*pow(4,k,p) % p
        for j in range(k+1):
            n = k+j
            P_quad[n] = (P_quad[n] + scalar*comb(k,j)*(-1)**j) % p
    # R_m(u) from _2F1(-2m,-4m;1-p/2;u) reduced mod p.
    R = [comb(2*m,k)*comb(4*m,k) % p for k in range(2*m+1)]
    # Here coefficients are positive (negative integer parameters yield +).
    assert P_quad == R, (p,'quadratic',next((k for k in range(len(R)) if P_quad[k]!=R[k]),None))
    # H_p(t) from [x^(p-1)] (4x^3+(x+a3)^2)^((p-1)/2).
    # H = sum_{k=0}^{2m} C(3m,k) C(6m-2k,k) (4/27)^k (1-t)^k.
    # Build H coefficient polynomial in u=(1-t).
    H_u = [comb(3*m,k)*comb(6*m-2*k,k) *pow(4*pow(27,-1,p),k,p)%p
           for k in range(2*m+1)]
    assert H_u == R, (p,'hasse', next((k for k in range(len(R)) if H_u[k]!=R[k]),None))
    # R_m(1-t)==R_m(t) due to Legendre polynomial evenness.
    # Check the reflected coefficient polynomial mod p, independently.
    reflect = [0]*(2*m+1)
    for k, c in enumerate(R):
        for j in range(k+1):
            reflect[j] = (reflect[j]+c*comb(k,j)*(-1)**j) % p
    assert reflect == R, (p,'legendre_reflection')
    P_half = sum(c*pow(inv2,k,p) for k,c in enumerate(P)) % p
    if p % 24 in (13,19):
        assert pow(2, (p-1)//2, p) == p-1, (p,'sqrt2_should_be_nonsquare')
        assert pow(p-6, (p-1)//2, p) == p-1, (p,'CM_should_be_inert')
        t = (2*inv4%p, -inv4%p)
        P_at_t = eval2(R,t,p)
        H_at_t = eval2(H_u,(1-t[0],-t[1]),p)
        assert P_at_t == H_at_t == (0,0), (p,'Hasse_CM', P_at_t,H_at_t)
        assert P_half == 0, (p,'target_CM_zero',P_half)
    return P_half, sum(P[k]*k*pow(inv2,k-1,p) for k in range(1,m+1))%p


def main():
    j = cm_j_discriminant_check()
    print('CM_J_PAIR', j)
    allprimes = [p for p in primes_below(1500) if p%6==1]
    frozen = []
    for p in allprimes:
        val, derivative = check_prime(p)
        if p % 24 in (13,19):
            assert derivative != 0, (p, 'root_multiplicity')
            frozen.append(p)
            if p in (13,19,373):
                print('FIXED_WITNESS',p,'m',(p-1)//6,'P_half',val,'P_prime',derivative)
    assert len(allprimes)==115 and len(frozen)==60
    print('ALL_P_EQ_1_MOD6_CHECKED',len(allprimes))
    print('FROZEN_CLASSES_CHECKED',len(frozen))
    print('PASS_CM_J_HILBERT_MINUS24_QUADRATIC_HASSE_AND_FINITE_POLYNOMIAL_IDENTITIES')

if __name__ == '__main__': main()
