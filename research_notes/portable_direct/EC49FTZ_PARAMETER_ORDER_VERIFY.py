#!/usr/bin/env python3
"""EC49FTZ exact independent price-fiber checks, native BRC author geometry inherited."""
from fractions import Fraction as F
import json
A_LO,A_HI=F(3,4),F(49,64)
B_LO,B_HI=F(7,16),F(57,128)
M2,M3=F(1469,64),F(187,8)
U,C=F(3,4),F(16,945)
E=F(1048576,18958647)
P_MIN=F(17372631,1048576)
P_MAX=F(18958647,1048576)
alpha,beta=F(525,8),F(35,32)

def Mstar(a,b):return alpha*a-F(231,4)*b-F(9,8)
def Zstar(a,b):return beta*a-b/16-F(5,96)
def L(m):return (8*m+173)/480
def x(m):return (740-m)/945
def b(m):return (47-m)/54
def d(m):return A_HI-x(m)
def p_cont(m):return m*(L(m)+U)/2
def p_atom(m):return m*U+(m*beta+U*alpha)*d(m)/2+alpha*beta*d(m)**2/3
def masses(m):
    a0=C*(U-L(m)); bb0=d(m)/54
    return a0,bb0,a0*p_cont(m),bb0*p_atom(m)
def cdf(m,eps,z):
    a0,b0,a1,b1=masses(m)
    denom=a0+b0-eps*(a1+b1)
    if z<=L(m):return F(0)
    if z>=U:return F(1)
    n0=C*(z-L(m));n1=C*m*(z*z-L(m)*L(m))/2
    return (n0-eps*n1)/denom
def top(m,eps):
    a0,b0,a1,b1=masses(m)
    return (b0-eps*b1)/(a0+b0-eps*(a1+b1))

corners=[(a,b) for a in (A_LO,A_HI) for b in (B_LO,B_HI)]
assert all(Mstar(a,b)>0 and Zstar(a,b)>0 for a,b in corners)
assert Mstar(A_LO,B_HI)*Zstar(A_LO,B_HI)==P_MIN
assert Mstar(A_HI,B_LO)*Zstar(A_HI,B_LO)==P_MAX
assert E==1/P_MAX

mvals=[M2+(M3-M2)*F(j,8) for j in range(1,8)]
epsvals=[F(-100),F(-1),F(-1,100),F(0),E/2,E]
checks=0
for m in mvals:
    assert M2<m<M3 and A_LO<x(m)<A_HI and B_LO<b(m)<B_HI
    assert Mstar(x(m),b(m))==m and Zstar(x(m),b(m))==U
    assert p_atom(m)>m*U>p_cont(m)>0
    a0,b0,a1,b1=masses(m)
    assert a1==C*m*(U*U-L(m)*L(m))/2
    assert a0>0 and b0>0 and a1>0 and b1>0
    # Exact antiderivative of p=M_* Z_* on clipped section.
    # M_*(x+r,b)=m+alpha*r, Z_*(x+r,b)=U+beta*r.
    assert b1 == (m*U*d(m)+(m*beta+U*alpha)*d(m)**2/2+alpha*beta*d(m)**3/3)/54
    # Normalized p-tilted law is the mixture limit of uniform-plus-s*p.
    for s in [F(1,10),F(1),F(100)]:
        omega=s*(a1+b1)/(a0+b0+s*(a1+b1))
        for j in range(1,10):
            z=L(m)+(U-L(m))*F(j,10)
            f0=cdf(m,F(0),z)
            f_inf=(C*m*(z*z-L(m)*L(m))/2)/(a1+b1)
            assert cdf(m,-s,z)==(1-omega)*f0+omega*f_inf
            assert F(0)<omega<1
            checks+=1
        assert (a0+b0)/(a0+b0+s*(a1+b1))<=1/(1+s*P_MIN)
    for j in range(1,10):
        z=L(m)+(U-L(m))*F(j,10)
        # m held fixed, increased epsilon shifts Z to the left.
        vals=[cdf(m,ep,z) for ep in epsvals]
        assert all(F(0)<v<F(1) for v in vals)
        assert all(x<y for x,y in zip(vals,vals[1:]))
        checks+=1
    ats=[top(m,ep) for ep in epsvals]
    assert all(x>y for x,y in zip(ats,ats[1:]))
    # derivative d_eps(top) = (b0*a1-b1*a0)/denom^2 < 0.
    assert b0*a1-b1*a0<0
    checks+=1

# Inheritance diagnostic: fixed eps, m-high fiber stochastic order on common thresholds.
for ep in epsvals:
    for z in [F(749,1000),F(3,4)-F(1,1000)]:
        vals=[cdf(m,ep,z) for m in mvals]
        assert all(x>=y for x,y in zip(vals,vals[1:]))
        checks+=1

print(json.dumps({
  'schema':'EC49FTZ_SIGNED_PARAMETER_MONOTONICITY_V1',
  'frozen_native_science':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
  'prior':'h_epsilon=1-epsilon*Mstar*Zstar',
  'epsilon_domain':'(-infinity,1048576/18958647]',
  'm_domain':'(1469/64,187/8)',
  'P_min':str(P_MIN),'P_max':str(P_MAX),
  'new_finding':'for fixed m, epsilon1<epsilon2 implies law(Z|m,epsilon2) <_st law(Z|m,epsilon1)',
  'joint_order':'m1<=m2 and epsilon1>=epsilon2 => law(m1,epsilon1) <=_st law(m2,epsilon2)',
  'limit_epsilon_to_negative_infinity':'normalized p=Mstar*Zstar prior',
  'uniform_TV_bound':'1/(1+s*17372631/1048576), epsilon=-s, s>=0',
  'exact_fraction_assertions':checks,
  'verification':'Fraction exact examples + symbolic proof in accompanying theorem; no all-real inference from grid',
  'native_bellman_rerun':False,
  'independent_review':False,
  'status':'AUTHOR_PROVED_EXACT_FRACTION_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED'
},indent=2))
