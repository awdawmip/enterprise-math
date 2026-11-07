#!/usr/bin/env python3
"""EC49L exact positive-leaf model and rational-observer certificate."""
from fractions import Fraction as F
from itertools import product
import sympy as S
import json

W=('U','V','C0','C1')
weights={'P':(F(3,8),F(3,8),F(1,8),F(1,8)),
         'Q':(F(1,8),F(1,8),F(3,8),F(3,8))}
success={'P':(F(1,4),F(3,4),F(1,2),F(1,2)),
         'Q':(F(3,4),F(1,4),F(1,2),F(1,2))}
# U->(A=1 with p0), V->(A=0 with p1); C0,C1 forced A=0,1.
# Second decision remembers A only and purchases Y with q_A.
def value(p0,p1,q0,q1):
    v=[]
    for th in ('P','Q'):
        accept=T=F(0)
        for i,w in enumerate(W):
            a={'U':p0,'V':p1,'C0':1,'C1':1}[w]
            q=q1 if w in ('U','C1') else q0
            accept+=weights[th][i]*a*q*success[th][i]
            T+=weights[th][i]*a*(1+q)
        v.append((accept,T))
    return (v[0][0],v[1][0],v[0][1],v[1][1])

def invert(O):
    alpha,beta,ep,eq=O
    sp=8*(ep-F(1,4));sq=8*(eq-F(3,4))
    X=(3*sp-sq)/8;v=(3*sq-sp)/8
    ap=alpha-v/F(16);bp=beta-3*v/F(16)
    w1=4*(ap-bp);w0=(32*bp-w1)/3
    return X-w0-w1,v,w0,w1

for th in ('P','Q'):
    assert sum(weights[th])==1
    for a,s in zip(weights[th],success[th]):
        assert a*s>0 and a*(1-s)>0
n_det=0
for p in product([F(0),F(1)],repeat=4):
    assert invert(value(*p))==(p[0]+p[1],p[2]+p[3],p[0]*p[3],p[1]*p[2])
    n_det+=1
grid=[F(0),F(1,8),F(1,4),F(1,2),F(3,4),F(1)]
n_grid=0
for p in product(grid,repeat=4):
    assert invert(value(*p))==(p[0]+p[1],p[2]+p[3],p[0]*p[3],p[1]*p[2])
    n_grid+=1
target=tuple(map(F,('7/64','13/64','27/32','41/32')))
assert invert(target)==(F(1),F(1),F(1,8),F(1,8))
x=S.symbols('x');roots=S.solve(S.Eq(x*(1-x),S.Rational(1,8)),x)
assert roots==[S.Rational(1,2)-S.sqrt(2)/4,S.Rational(1,2)+S.sqrt(2)/4]
for x0 in roots:
    p0=x0;p1=1-x0;q1=1-x0;q0=x0
    v=[]
    for th in ('P','Q'):
        acc=t=S.Integer(0)
        for i,w in enumerate(W):
            a={'U':p0,'V':p1,'C0':1,'C1':1}[w]
            q=q1 if w in ('U','C1') else q0
            wt=S.Rational(weights[th][i].numerator,weights[th][i].denominator)
            sy=S.Rational(success[th][i].numerator,success[th][i].denominator)
            acc+=wt*a*q*sy;t+=wt*a*(1+q)
        v.append((S.simplify(acc),S.simplify(t)))
    assert (v[0][0],v[1][0],v[0][1],v[1][1])==tuple(S.Rational(t.numerator,t.denominator) for t in target)
# Rational extra external-bit repair, independently summing branches.
rr=[]
for th in ('P','Q'):
    acc=t=F(0)
    for i,w in enumerate(W):
        a=F(1,2) if w in ('U','V') else F(1)
        q=F(1,4) if w in ('U','V') else F(1,2)
        acc+=weights[th][i]*a*q*success[th][i]
        t+=weights[th][i]*a*(1+q)
    rr.append((acc,t))
assert (rr[0][0],rr[1][0],rr[0][1],rr[1][1])==target
# Rational ex-ante mixing of pure policy tables: differs from fresh behavior.
mixtures=[((0,0,0,0),F(1,8)),((0,1,0,1),F(3,4)),((1,1,1,1),F(1,8))]
assert sum((wt for _,wt in mixtures),F(0))==1
assert tuple(sum((wt*value(*policy)[j] for policy,wt in mixtures),F(0)) for j in range(4))==target
print(json.dumps({'status':'EXACT_PASS','source_latent_atoms_each':8,
 'deterministic_policies':n_det,'rational_grid_policies':n_grid,
 'target':list(map(str,target)),'recovered_features':list(map(str,invert(target))),
 'irrational_roots':[str(r) for r in roots],
 'rational_remembered_external_bit':'PASS',
 'rational_ex_ante_shared_seed':'PASS'},sort_keys=True,indent=2))
