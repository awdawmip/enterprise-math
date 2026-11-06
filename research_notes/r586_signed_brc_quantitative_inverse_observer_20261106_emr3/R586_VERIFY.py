"""R586 independent finite checks; exact claims use Fraction and integers.
The numerical V(k) table is exploratory, not a root-isolation proof.
"""
from fractions import Fraction as F
from math import comb, sqrt

def C(n):
    return comb(2*n, n)//(n+1)

def H(k, s):
    return comb(2*k+1+s, 2*s)*sum(
        comb(s-1, 2*q)*4**q*C(k-q)
        for q in range(min(k, (s-1)//2)+1)
    )

def spectral_coefficients(k):
    d=2*k-1
    base=H(k,2)
    return [F(H(k,j+2),base) for j in range(d+1)]

def t2_newton(k):
    d=2*k-1
    c=spectral_coefficients(k)
    # Q=x^d-A1*x^(d-1)+A2*x^(d-2) - ..., and inverse roots
    # elementary inverse symmetrics come from the reversed coefficients.
    en=F(c[-2],c[-1]); e2=F(c[-3],c[-1]);
    return en*en-2*e2

def lower_V_from_T2(k):
    d=2*k-1
    return max(F(0), 1-t2_newton(k)/d)

for k in range(2,41):
    d=2*k-1
    t=t2_newton(k)
    expected=F(12*k*k-20*k+1,4*k+1)
    assert t==expected,(k,t,expected)
    lb=lower_V_from_T2(k)
    assert lb==max(F(0),F(-4*k*k+18*k-2,(4*k+1)*(2*k-1)))

# k=2, Q2 has one real root by exact cubic discriminant -567.
assert spectral_coefficients(2)==[F(1),F(12,5),F(9,5),F(3,5)]
a,b,c,d=5,-12,9,-3
disc=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
assert disc==-567
f=lambda x:5*x**3-12*x*x+9*x-3
left,right=F(14387,10000),F(14388,10000)
assert f(left)<0<f(right)
# u=1/lambda_real, and T1(2)=3,T2(2)=1.
# V2=(2/3)+(u-1)^2/2, strictly decreasing for 0<u<1.
u_lo,u_hi=1/right,1/left
v=lambda u:F(2,3)+(u-1)**2/2
v_lo,v_hi=v(u_hi),v(u_lo)
assert F(71315,100000)<v_lo<v_hi<F(71318,100000)
assert lower_V_from_T2(2)==F(2,3)
print('R586_EXACT_39_T2_IDENTITIES_PASS')
print('Q2_DISCRIMINANT',disc,'REAL_ROOT_BRACKET',left,right)
print('V2_STRICT_RATIONAL_BRACKET',v_lo,v_hi)
print('V2_DECIMAL_BRACKET',float(v_lo),float(v_hi))
print('EXACT_FINITE_LOWER_BOUNDS',[(k,str(lower_V_from_T2(k))) for k in range(2,6)])

try:
    import sympy as sp
    z=sp.Symbol('z')
    for k in (2,4,8,12,16,20,24):
        d=2*k-1
        c=spectral_coefficients(k)
        poly=sp.Poly(sum((-1)**j*sp.Rational(a.numerator,a.denominator)*z**(d-j) for j,a in enumerate(c)),z)
        roots=poly.nroots(n=36,maxsteps=150)
        inv=[1/complex(x) for x in roots]
        V=sum(x.imag*x.imag for x in inv)/d
        print('NUMERICAL_ONLY',k,'V=',f'{V:.10f}','sqrt(k)*V=',f'{sqrt(k)*V:.10f}')
except ImportError:
    print('NUMERICAL_ONLY SymPy not installed; exact checks still pass')
print('R586_QUANTITATIVE_OBSERVER_FINITE_CHECK_PASS')
