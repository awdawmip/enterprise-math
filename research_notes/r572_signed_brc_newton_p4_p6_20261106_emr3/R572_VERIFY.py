#!/usr/bin/env python3
"""R572 exact Newton p4/p6 proof certificate for frozen R462 signed BRC auxiliary scalar.
Uses SymPy rational polynomial identities and Python integer arithmetic; no floating-point roots.
"""
from math import comb
from fractions import Fraction
import sympy as s

k,t=s.symbols('k t',integer=True)

def cat(n):
    return comb(2*n,n)//(n+1)

def H(n,j):
    r=2*n+1
    if j<2 or j>r: return 0
    return comb(r+j,2*j)*sum(comb(j-1,2*q)*4**q*cat(n-q)
                             for q in range(min(n,(j-1)//2)+1))

# Closed forms A_j = H_k(j+2)/H_k(2) for j=1..6.
A={
 1:(k+2)*(4*k+1)/s.Integer(15),
 2:(k-1)*(k+2)*(2*k+5)*(8*k+5)/s.Integer(420),
 3:(k-1)*(k+2)*(k+3)*(2*k+5)*(32*k**2-16*k-33)/s.Integer(18900),
 4:(k-2)*(k-1)*(k+2)*(k+3)*(2*k+5)*(2*k+7)*(64*k**2-8*k-57)/s.Integer(1247400),
 5:(k-2)*(k-1)*(k+2)*(k+3)*(k+4)*(2*k+5)*(2*k+7)*(4*k-3)*(64*k**2-96*k-145)/s.Integer(113513400),
 6:(k-3)*(k-2)*(k-1)*(k+2)*(k+3)*(k+4)*(2*k+5)*(2*k+7)*(2*k+9)*(512*k**3-960*k**2-752*k+615)/s.Integer(13621608000),
}
# Newton for Q(y)=y^d+sum_j (-1)^j A_j y^(d-j).
p={}
for m in range(1,7):
    p[m]=s.factor(-sum((-1)**j*A[j]*p[m-j] for j in range(1,m))
                   -m*(-1)**m*A[m])

P4=(18688*k**7+108736*k**6+252932*k**5-1127884*k**4
    -7829539*k**3-19596652*k**2-29110835*k-15480446)
P6=(7491584*k**11+41017856*k**10-53092960*k**9
    -1053547600*k**8-2415621820*k**7+12839628644*k**6
    +102755266351*k**5+342909684895*k**4+688977135565*k**3
    +875097279805*k**2+701292907192*k+259328600488)
assert s.cancel(p[4]+(k+2)*P4/s.Integer(218295000))==0
assert s.cancel(p[6]-(k+2)*P6/s.Integer(8939180250000))==0

# Exact coefficientwise positivity on shifted half-lines.
c4=list(reversed([int(c) for c in s.Poly(s.expand(P4.subs(k,t+5)),t).all_coeffs()]))
c6=list(reversed([int(c) for c in s.Poly(s.expand(P6.subs(k,t+2)),t).all_coeffs()]))
assert len(c4)==8 and len(c6)==12 and min(c4)>0 and min(c6)>0

# Independent direct Catalan/Hesssenberg coefficient crosscheck, complete finite k=2..1000.
for n in range(2,1001):
    den=H(n,2)
    for j in range(1,7):
        assert Fraction(H(n,j+2),den)==Fraction(A[j].subs(k,n))
    aa=[Fraction(H(n,j+2),den) for j in range(1,7)]
    pp={}
    for m in range(1,7):
        pp[m]=-sum((-1)**j*aa[j-1]*pp[m-j] for j in range(1,m)) -m*(-1)**m*aa[m-1]
        assert pp[m]==Fraction(p[m].subs(k,n))
    assert pp[4]<0 if n>=5 else pp[4]>0
    assert pp[6]>0

for n in (5,9,29,30,100,1000):
    v4=Fraction(p[4].subs(k,n)); v6=Fraction(p[6].subs(k,n))
    print(f'K={n} P4={v4} P6={v6} RHO4_POWER4={abs(v4)/Fraction(2*n-1)} RHO6_POWER6={v6/Fraction(2*n-1)}')
print('P4_SHIFT_K5_ASC',c4)
print('P6_SHIFT_K2_ASC',c6)
print('R572_NEWTON_P4_P6_EXACT_PASS k=2..1000 n=999')
