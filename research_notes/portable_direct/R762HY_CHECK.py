"""R762HY: exact-rational six-axis signed Port/BRC second-order return coefficient.

Checks all 15 Ports, all 225 ordered covariance entries, the Johnson scheme
and an independent exact spectral perturbation equation.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import sympy as sp

AXES=tuple(range(6))
PORTS=tuple(combinations(AXES,2))
N=len(PORTS)

def supports(p):
    return [frozenset((*p,c)) for c in AXES if c not in p]

def cross_square(s,t):
    # Sigma^{-1}=10/3 I - 4/9 J and |S|=|T|=3.
    return (F(10,3)*len(s&t)-4)**2

def covariance(p,q):
    return F(1,32)*sum(cross_square(s,t) for s in supports(p) for t in supports(q))

p=PORTS[0]
q1=next(q for q in PORTS if len(set(p)&set(q))==1)
q2=next(q for q in PORTS if len(set(p)&set(q))==0)
c0,c1,c2=covariance(p,p),covariance(p,q1),covariance(p,q2)
assert len({covariance(p,q) for p in PORTS for q in PORTS})==3
assert (c0,c1,c2)==(F(43,6),F(77,24),F(73,36))
k5,k9=c0+2*c1-3*c2,c0-2*c1+c2
mix=(5*F(4,3)*k5+9*F(4,5)*k9)/N
gaussian_b4=F(3*6**2,24)
gaussian_log_square=-F(6*8,8)
correction=mix+gaussian_b4+gaussian_log_square
assert (k5,k9,mix)==(F(15,2),F(25,9),F(14,3))
assert (gaussian_b4,gaussian_log_square,correction)==(F(9,2),F(-6),F(19,6))

# Exact directional perturbation validation, including the nontrivial eigenprojectors.
u=sp.Matrix([1,2,-1,0,3,-2])
v=sp.ones(N,1)/sp.sqrt(N)
A=sp.zeros(N); B2=sp.zeros(N); B4=sp.zeros(N)
for i,pi in enumerate(PORTS):
    for j,pj in enumerate(PORTS):
        if i==j or len(set(pi)&set(pj))!=1: continue
        z=sum(u[a] for a in set(pi)|set(pj))
        A[i,j]=sp.Rational(1,8)
        B2[i,j]=-sp.Rational(1,16)*z*z
        B4[i,j]=sp.Rational(1,192)*z**4
inc=sp.Matrix([[int(a in p) for a in AXES] for p in PORTS])
P1=sp.ones(N)/N
P5=(inc*inc.T-10*P1)/4
P9=sp.eye(N)-P1-P5
assert A*P5==P5/4 and A*P9==-P9/4
R=sp.Rational(4,3)*P5+sp.Rational(4,5)*P9
lam2=(v.T*B2*v)[0]
x2=R*(B2-lam2*sp.eye(N))*v
lam4=(v.T*B4*v)[0]+(v.T*B2*x2)[0]
assert (sp.eye(N)-A)*x2==(B2-lam2*sp.eye(N))*v
assert (v.T*x2)[0]==0
assert lam4==(v.T*(B4*v+B2*x2))[0]
Sigma=sp.Rational(3,10)*sp.eye(6)+sp.Rational(1,5)*sp.ones(6)
assert Sigma.det()==sp.Rational(729,200000)
assert Sigma.inv()==sp.Rational(10,3)*sp.eye(6)-sp.Rational(4,9)*sp.ones(6)
assert lam2==-sp.Rational(1,2)*(u.T*Sigma*u)[0]
assert (lam2,lam4)==(-sp.Rational(15,4),sp.Rational(6009,400))

out={
  "status":"PASS R762HY",
  "frozen_model":"six-axis labeled Port signed composite candidate",
  "c0":str(c0),"c1":str(c1),"c2":str(c2),
  "kappa5":str(k5),"kappa9":str(k9),
  "resolvent_gaussian_expectation":str(mix),
  "quartic_gaussian_expectation":str(gaussian_b4),
  "log_square_gaussian_expectation":str(gaussian_log_square),
  "relative_inverse_m_coefficient":str(correction),
  "exact_direction":[int(x) for x in u],
  "direction_lambda2":str(lam2),"direction_lambda4":str(lam4),
  "sigma_determinant":str(Sigma.det()),
  "coverage":"15 Port states; all 225 covariance entries; exact Johnson projectors; exact rational direction",
  "not_checked":"R762HX continuous torus peak proof and analytic error bound"
}
print(json.dumps(out,indent=2,ensure_ascii=False))
