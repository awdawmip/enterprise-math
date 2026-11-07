"""R588: exact finite coefficient-change verification and numerical root sanity.
The theorem k^5 V_k -> +infinity is analytic, not inferred from this finite test.
Only the auxiliary scalar polynomial is evaluated; no native BRC dynamics.
"""
from fractions import Fraction as F
from math import comb


def catalan(n):
    return comb(2*n, n)//(n+1)


def H(k, s):
    return comb(2*k+1+s, 2*s)*sum(
        comb(s-1, 2*q)*4**q*catalan(k-q)
        for q in range(min(k, (s-1)//2)+1)
    )


def coeffs(k):
    d = 2*k-1
    A = [F(1)] + [F(H(k,j+2), H(k,2)) for j in range(1,d+1)]
    Q_ascending = [(-1)**(d-i)*A[d-i] for i in range(d+1)]
    F_ascending_direct = [(-1)**j*A[j]/k**(2*j) for j in range(d+1)]
    F_ascending_from_reciprocal = [Q_ascending[d-j]/k**(2*j) for j in range(d+1)]
    assert F_ascending_direct == F_ascending_from_reciprocal
    assert F_ascending_direct[0] == 1
    assert Q_ascending[0] != 0
    return A,Q_ascending,F_ascending_direct

check_count=0
for k in range(2,49):
    a,q,f=coeffs(k)
    check_count += len(f)
print('R588_EXACT_RECIPROCAL_COEFFICIENTS_PASS',check_count,'coefficients','k=2..48')

# Additional independently evaluated polynomial test at rational nonzero arguments.
for k in range(2,25):
    d=2*k-1
    _,q,f=coeffs(k)
    for z in [F(-3,7),F(2,3),F(7,5)]:
        lhs=sum(f[j]*z**j for j in range(d+1))
        lam=F(k*k,1)/z
        rhs=(z/F(k*k,1))**d * sum(q[j]*lam**j for j in range(d+1))
        assert lhs == rhs
print('R588_EXACT_RECIPROCAL_EVALUATIONS_PASS',23*3,'rational evaluations')

# Optional approximate diagnostic of auxiliary roots; never a proof of divergence.
import sympy as sp
x=sp.symbols('x')
for k in range(2,8):
    d=2*k-1
    a,q,f=coeffs(k)
    poly=sp.Poly(sum(sp.Rational(q[j].numerator,q[j].denominator)*x**j for j in range(d+1)),x)
    roots=poly.nroots(n=24,maxsteps=500)
    mus=[complex(1/r) for r in roots]
    zs=[complex(k*k/r) for r in roots]
    V=sum((z.imag)**2 for z in mus)/d
    scaled_a=k**5*V
    scaled_b=k/d*sum(z.imag**2 for z in zs)
    assert abs(scaled_a-scaled_b)<1e-8*max(1,abs(scaled_a))
    print('R588_AUX_NUMERIC_SANITY',k,'V',format(V,'.12g'),'k5V',format(scaled_a,'.12g'))
print('R588_SPECTRAL_LEAKAGE_FINITE_CROSSCHECK_PASS')
