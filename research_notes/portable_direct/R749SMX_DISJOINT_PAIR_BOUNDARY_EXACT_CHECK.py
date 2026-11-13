#!/usr/bin/env python3
"""Exact checks for R749SMX: complement-disjoint pair marginal/boundary fibers.

All checks use integers or fractions.Fraction, no floating point.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

C=(1,2,4,8,15)
B=tuple(a for a in range(1,16) if a not in C)
SIGNS=(-1,1)

def chi(a,x):
    return 1 if (a&x).bit_count()%2==0 else -1

def density(t,s,h,u,v,w,z,x):
    A,Bb,P,Q=(chi(i,x) for i in (3,12,1,4))
    return (1+t*A+s*Bb+h*A*Bb+u*P+v*A*P+w*Q+z*Bb*Q)/16

def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2

assert sorted((chi(3,x),chi(12,x),chi(1,x),chi(4,x)) for x in range(16))==sorted(product(SIGNS,repeat=4))
assert B==(3,5,6,7,9,10,11,12,13,14)

# Exact equivalence of all sixteen positivity inequalities to the four grouped inequalities
# on a small but nontrivial seven-dimensional rational grid, not used as the general proof.
grid=(-2,-1,0,1,2)  # half-units
positivity_profiles=0
for t,s,h,u,v,w,z in product(grid,repeat=7):
    group=all(2+t*A+s*Bb+h*A*Bb >=abs(u+v*A)+abs(w+z*Bb)
              for A,Bb in product(SIGNS,repeat=2))
    direct=all(2+t*A+s*Bb+h*A*Bb+u*P+v*A*P+w*Q+z*Bb*Q >=0
               for A,Bb,P,Q in product(SIGNS,repeat=4))
    assert group==direct
    positivity_profiles+=1

boundary_profiles=0
boundary_radii=[]
for eps,s in product(SIGNS,(F(-1),F(-3,4),F(-1,2),F(-1,3),F(0),F(1,3),F(1,2),F(3,4),F(1))):
    r=1-abs(s)
    center=[density(F(eps),s,F(eps)*s,F(0),F(0),F(0),F(0),x) for x in range(16)]
    assert all(a>=0 for a in center) and sum(center)==1
    for zeta in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
        u=r*zeta
        # Here v=eps*u, giving total coefficient 2*u on the A=eps face.
        p=[density(F(eps),s,F(eps)*s,u,F(eps)*u,F(0),F(0),x) for x in range(16)]
        assert all(a>=0 for a in p) and sum(p)==1
        for a in B:
            m=sum(p[x]*chi(a,x) for x in range(16))
            assert m==(F(eps) if a==3 else s if a==12 else 0), (eps,s,u,a,m)
        assert tv(center,p)==abs(u)/2
        boundary_profiles+=1
    plus=[density(F(eps),s,F(eps)*s,r,F(eps)*r,F(0),F(0),x) for x in range(16)]
    minus=[density(F(eps),s,F(eps)*s,-r,-F(eps)*r,F(0),F(0),x) for x in range(16)]
    assert tv(plus,minus)==r
    assert tv(center,plus)==r/2
    assert tv(center,minus)==r/2
    boundary_radii.append({'t':str(eps),'s':str(s),'radius':str(r/2)})

# Future observer identity: for any finite stochastic K, the boundary-fiber image
# is a line and its exact minimax radius is (1-|s|)/2 * sum_y |(K d)(y)|,
# d_x=chi_1(x)/8 when chi_3(x)=eps and 0 otherwise.
observer_profiles=0
for eps,s,lam,eta in product(SIGNS,(F(-1),F(-1,2),F(0),F(1,2),F(1)),
                               (F(-1),F(-1,2),F(0),F(1,2),F(1)),
                               (F(-1),F(0),F(1))):
    r=1-abs(s)
    def k(y,x):
        p=chi(1,x); bb=chi(12,x)
        if y==0: return (1+lam*p)/4
        if y==1: return (1+eta*bb)/4
        return F(1)-(1+lam*p)/4-(1+eta*bb)/4
    assert all(k(y,x)>=0 for x in range(16) for y in range(3))
    assert all(sum(k(y,x) for y in range(3))==1 for x in range(16))
    def law(u):
        src=[density(F(eps),s,F(eps)*s,u,F(eps)*u,F(0),F(0),x) for x in range(16)]
        return [sum(k(y,x)*src[x] for x in range(16)) for y in range(3)]
    d=[sum(k(y,x)*chi(1,x)/8 for x in range(16) if chi(3,x)==eps) for y in range(3)]
    predicted=r*sum(abs(v) for v in d)/2
    assert tv(law(0),law(r))==predicted
    assert tv(law(-r),law(r))/2==predicted
    assert predicted==r*abs(lam)/4
    observer_profiles+=1

result={
  'schema':'R749SMX_DISJOINT_COMPLEMENT_BOUNDARY_EXACT_V1',
  'status':'PASS',
  'domain':'G=F2^4, C=(1,2,4,8,15), B=G*\\C; retained m_3=t,m_12=s, other B moments zero',
  'general_fiber_parameters':['h','u','v','w','z'],
  'general_fiber_positivity':'for all A,B in {+-1}: 1+tA+sB+hAB >= |u+vA|+|w+zB|',
  'boundary_formula':'rho_B(eps,s)=(1-|s|)/2 for eps in {+-1}, s in [-1,1]; symmetric for rho_B(t,eps)',
  'positivity_grid_rational_profiles':positivity_profiles,
  'boundary_probability_and_moment_profiles':boundary_profiles,
  'finite_future_observer_profiles':observer_profiles,
  'future_observer_exact_minimax':'(1-|s|)/2 * sum_y |sum_{x:chi_3(x)=eps} K(y|x)chi_1(x)/8|',
  'boundary_center_radius_examples':boundary_radii,
  'arithmetic':'exact integer and Fraction; analytic proof establishes continuum',
  'scientific_input_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'scope':'Auxiliary signed-source model; native V29/V39 correspondence and independent review pending'
}
out=Path(__file__).with_name('R749SMX_DISJOINT_PAIR_BOUNDARY_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS', 'positivity',positivity_profiles, 'boundary',boundary_profiles, 'future_observers',observer_profiles, 'file',out.name)
