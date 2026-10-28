#!/usr/bin/env python3
"""Exact author checks: C_T de Rham / Gauss-Manin / Hasse-Legendre.

No external math-Source operations, no native experiment; independent portable check.
Requires Python 3 and SymPy for the rational-identity portion.
"""
import sympy as sp

T, x = sp.symbols('T x')
b = (1 + T) / 8
f = x**3 + x**2 + b*x
D = x**2 + x + b

# The basic exact-differential equality d(y/x) = (x - b/x) omega.
assert sp.factor((x*sp.diff(f,x)-2*f)/x**2 - (x-b/x)) == 0

# Exact-differential cohomological reduction.  The coefficients of
# [omega], [x omega] in the rational one-forms X=omega/D, Y=x omega/D.
X0 = 2 / (4*b-1)
X1 = 1 / (b*(4*b-1))
Y0 = -1 / (4*b-1)
Y1 = -2 / (4*b-1)
assert sp.factor(Y0 + 2*b*X0 - 1) == 0
assert sp.factor(Y1 + 2*b*X1) == 0
assert sp.factor((1-2*b)*Y0+b*X0-1) == 0
assert sp.factor((1-2*b)*Y1+b*X1-1) == 0

# Connection rows: nabla_T [omega,eta]^t = A(T) [omega,eta]^t.
A = sp.Matrix([[-1/(4*(T-1)), -1/(T*T-1)],
               [1/(8*(T-1)),  1/(4*(T-1))]])
M = sp.Matrix([[1, 0],[-sp.Rational(1,2), -1]])
assert (M*M-sp.eye(2)) == sp.zeros(2)
assert (M*A+A.subs(T,-T)*M).applyfunc(sp.factor) == sp.zeros(2)
assert sp.factor(A.trace()) == 0
assert sp.factor(A.det()+1/(16*(T*T-1))) == 0

# Picard-Fuchs elimination: y'' - (c'/c)y' - Q y = 0,
# where c=A[0,1] and Q=a'+a^2+cb-(c'/c)a.
a, c = A[0,0], A[0,1]
B = A[1,0]
Q = sp.factor(sp.diff(a,T)+a*a+c*B-sp.diff(c,T)*a/c)
assert sp.factor(Q + 3/(16*(T*T-1))) == 0
assert sp.factor(-sp.diff(c,T)/c - 2*T/(T*T-1)) == 0
print('PASS_EXACT_Q_DE_RHAM_KAPPA_MATRIX_GM_COVARIANCE_PICARD_FUCHS')

# Hasse-Cartier of C_T: [x^{p-1}](x^3+x^2+bx)^((p-1)/2).
# Its coefficient in (1+T)^j is binom(N,2j)binom(2j,j)/8^j.
# P_n(-T) = sum_j (-n)_j(n+1)_j (1+T)^j/[j!^2 2^j].
# Compare these coefficients exactly in each finite field.
def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2,int(n**.5)+1):
        if sieve[q]: sieve[q*q:n+1:q] = b'\x00' * ((n-q*q)//q+1)
    return [q for q in range(11,n+1) if sieve[q] and q%8==3]

count, compared = 0, 0
for p in primes_upto(10000):
    m = (p-3)//8
    n, N = 2*m, (p-1)//2
    assert N == 4*m+1
    lhs, rhs = 1, 1
    # j=0: both coefficients are 1. Recurrences avoid huge binomials.
    inv8, inv2 = pow(8,-1,p), pow(2,-1,p)
    for j in range(n+1):
        assert lhs == rhs, (p,j,lhs,rhs)
        compared += 1
        if j<n:
            inv_denom = pow((j+1)**2,-1,p)
            lhs = (lhs*(N-2*j)*(N-2*j-1)*inv_denom*inv8)%p
            rhs = (rhs*((-n+j)%p)*((n+1+j)%p)*inv_denom*inv2)%p
    count += 1
print(f'PASS_HASSE_LEGENDRE_COEFFICIENTS {count} primes p<10000, {compared} exact coefficients')

# Explicit generic-parameter warning: the target Euler derivative does not
# vanish identically just from the isogeny family.
p=11
p2_t0_sq = 8*pow(9,-1,p)%p
# P_2=(3T^2-1)/2, T P_2'-P_2=(3T^2+1)/2
assert ((3*p2_t0_sq+1)*pow(2,-1,p))%p == 0
assert pow(2,-1,p) != 0  # At T=0 the same Euler expression is 1/2.
print('PASS_DISTINGUISH_FAMILY_COVARIANCE_FROM_CM_SPECIAL_VALUE p=11')
