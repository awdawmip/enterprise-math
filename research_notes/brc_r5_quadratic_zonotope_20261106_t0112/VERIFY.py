#!/usr/bin/env python3
"""R5 delta=1/4 six-variable quadratic, seven-ratio zonotope exact checker."""
from fractions import Fraction as F
from itertools import product
from random import Random

R2 = (F(3,4), F(5,4))
Q2 = (F(1,2), F(1,2))
R3 = (F(1,2), F(1), F(3,2))
Q3 = ((F(13,20), F(1,5), F(3,20)), (F(1,40), F(9,20), F(21,40)))
R4 = (F(1,10), F(1), F(19,10))
Q4 = {}
for i in range(2):
    for j in range(3):
        Q4[i,j] = ((F(509,900),F(382,900),F(9,900)) if j == 0 else
                   (F(9,900),F(382,900),F(509,900)) if j == 2 else
                   (F(47,180),F(43,90),F(47,180)) if i == 0 else
                   (F(67,162),F(14,81),F(67,162)))
R = tuple(sorted(set((F(1),)+R2+R3+R4)))
assert len(R) == 7
for i in range(2):
    assert sum(Q3[i]) == 1 and sum(Q3[i][j]*R3[j] for j in range(3)) == R2[i]
    for j in range(3):
        assert min(Q4[i,j]) > 0 and sum(Q4[i,j]) == 1
        assert sum(Q4[i,j][k]*R4[k] for k in range(3)) == R3[j]

KEYS = tuple([(1,F(1))]+[(2,r) for r in R2]+[(3,r) for r in R3]+[(4,r) for r in R4])
assert len(KEYS) == 9

def formulas(g,u,z):
    assert F(0) <= u[0] <= g <= 1 and F(0) <= u[1] <= g
    assert all(F(0) <= t <= 1 for t in z)
    stop = {(1,F(1)):1-g}
    for i in range(2):
        stop[2,R2[i]] = Q2[i]*(g-u[i])
    V = [sum(Q2[i]*Q3[i][j]*u[i] for i in range(2)) for j in range(3)]
    for j in range(3):
        stop[3,R3[j]] = V[j]*(1-z[j])
    for k in range(3):
        stop[4,R4[k]] = sum(Q2[i]*Q3[i][j]*u[i]*z[j]*Q4[i,j][k]
                              for i in range(2) for j in range(3))
    T = {r:sum(stop[key] for key in KEYS if key[1] == r) for r in R}
    EQ = 1 + g + sum(Q2[i]*u[i] for i in range(2)) + sum(V[j]*z[j] for j in range(3))
    EP = 1 + g + sum(Q2[i]*R2[i]*u[i] for i in range(2)) + sum(
        R3[j]*V[j]*z[j] for j in range(3))
    assert all(v>=0 for v in stop.values())
    assert sum(T.values()) == sum(r*T[r] for r in R) == 1
    assert EP == sum(stop[key]*key[0]*key[1] for key in KEYS)
    assert EQ == sum(stop[key]*key[0] for key in KEYS)
    return EP,EQ,stop,T

def halfspaces(T,err):
    p,q = err
    for rho in R:
        v = p + rho*q
        lo = 1+sum((rho-r)*T[r] for r in R if r > rho)
        hi = 1+sum((rho-r)*T[r] for r in R if r < rho)
        if not lo <= v <= hi:return False
    return True

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def polygon(T):
    pts = sorted(set((1-sum(r*T[r]*b for r,b in zip(R,bits)),
                       sum(T[r]*b for r,b in zip(R,bits)))
                      for bits in product((0,1), repeat=len(R))))
    if len(pts) <= 2:return pts
    lo=[]; hi=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def inside(poly,p):
    if len(poly)==1:return p==poly[0]
    if len(poly)==2:
        a,b=poly
        return cross(a,b,p)==0 and all(min(a[k],b[k])<=p[k]<=max(a[k],b[k]) for k in (0,1))
    return all(cross(poly[k],poly[(k+1)%len(poly)],p)>=0 for k in range(len(poly)))

rnd = Random(51106)
checked=0
for case in range(180):
    if case==0:g=F(0)
    elif case==1:g=F(1)
    else:g=F(rnd.randrange(0,11),10)
    u=[g*F(rnd.randrange(0,11),10) for _ in range(2)]
    z=[F(rnd.randrange(0,11),10) for _ in range(3)]
    EP,EQ,stop,T=formulas(g,u,z)
    x={key:F(rnd.randrange(0,11),10) for key in KEYS}
    err=(sum(stop[key]*key[1]*(1-x[key]) for key in KEYS),
         sum(stop[key]*x[key] for key in KEYS))
    assert halfspaces(T,err)
    poly=polygon(T)
    assert inside(poly,err)
    for t in range(6):
        test=(F(rnd.randrange(-3,14),10),F(rnd.randrange(-3,14),10))
        assert inside(poly,test)==halfspaces(T,test), (case,test,poly)
        checked+=1
print('PASS_EXACT_R5_QUADRATIC_ZONOTOPE_MEMBERSHIP')
print('model=delta=1/4 ratio_count=7 continuation_variables=6 time_equalities=2 error_inequalities=14 degree_max=2')
print('tested_continuation_and_policy_cases=180 polygon_membership_equivalences=',checked)
print('boundary_cases=g=0,g=1 included; exact Fraction arithmetic; theorem proved analytically')
