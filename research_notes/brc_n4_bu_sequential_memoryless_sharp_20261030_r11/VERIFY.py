#!/usr/bin/env python3
"""Exact check of persistent-vs-memoryless readout of BU stage-four leaf bit.
Author-only portable BRC exercise. No native physics or reviewer acceptance.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from sympy import sqrt, simplify, Rational, solveset, S, diff, symbols

q_src={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r_j={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves={}
for s,j,k in product(q_src,range(2),range(2)):
    q=q_src[s]/4
    leaves[s,j,k]=(q*r_j[s][j],q)
assert len(leaves)==16
assert all(p>0 and q>0 for p,q in leaves.values())
assert [sum(x[i] for x in leaves.values()) for i in (0,1)]==[F(1),F(1)]

# Old observable G0 only; terminal sensors are hypothetical typed extensions.
def coarse(s): return {'AU':'T3_P_AU','AV':'T2_Q','BU':'T3_Q_BU','BV':'T2_Q'}[s]
def dist(law, decoder, theta=((F(1,2),F(1,2)),(F(1,2),F(1,2)))):
    """decoder='physical', 'persistent', or 'memoryless' (two independent fresh draws)."""
    out=defaultdict(F)
    for (s,j,k),pq in leaves.items():
        mass=pq[law]
        if s!='BU':
            out[(coarse(s),None,0,0)]+=mass
        elif decoder in ('physical','persistent'):
            # Persistent simulator averages over its ONE fair private draw
            # conditional on BU,j rather than physical k; both conditional laws fair.
            if decoder=='physical':
                out[(coarse(s),j,k,k)]+=mass
            else:
                for bit in (0,1):
                    out[(coarse(s),j,bit,bit)]+=mass*F(1,2)
        else:
            t1,t2=theta[j]
            for y1,y2 in product((0,1),repeat=2):
                out[(coarse(s),j,y1,y2)]+=mass*(t1 if y1 else 1-t1)*(t2 if y2 else 1-t2)
    return dict(out)

def tv(a,b):
    return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in set(a)|set(b)),F(0))/2

bu_p=[sum(v[0] for (s,jj,k),v in leaves.items() if s=='BU' and jj==j) for j in (0,1)]
bu_q=[sum(v[1] for (s,jj,k),v in leaves.items() if s=='BU' and jj==j) for j in (0,1)]
assert bu_p==[F(1,40),F(9,40)] and bu_q==[F(1,8),F(1,8)]
for law in (0,1):
    true=dist(law,'physical')
    persist=dist(law,'persistent')
    assert true==persist
    assert tv(true,dist(law,'memoryless'))==F(1,8)
    for t in (F(0), F(1,4), F(1,3), F(1,2), F(3,4), F(1)):
        f=(abs(F(1,2)-(1-t)**2)+2*t*(1-t)+abs(F(1,2)-t*t))/2
        assert tv(true,dist(law,'memoryless',theta=((t,t),(t,t))))==F(1,4)*f
        # all variable-pair outcomes reproduce the weighted per-fiber identity
        tp,tq=F(1,4),F(2,3)
        fp=(abs(F(1,2)-(1-tp)**2)+2*tp*(1-tp)+abs(F(1,2)-tp*tp))/2
        fq=(abs(F(1,2)-(1-tq)**2)+2*tq*(1-tq)+abs(F(1,2)-tq*tq))/2
        weights=bu_p if law==0 else bu_q
        assert tv(true,dist(law,'memoryless',theta=((tp,tp),(tq,tq))))==weights[0]*fp+weights[1]*fq

x=symbols('x',real=True)
alpha=1-1/sqrt(2)
beta=1/sqrt(2)
# f piecewise on [0,alpha], [alpha,beta], [beta,1]
f_left=Rational(1,2)-x*x
f_mid=2*x*(1-x)
f_right=Rational(1,2)-(1-x)**2
v=sqrt(2)-1
assert simplify(f_left.subs(x,alpha)-v)==0
assert simplify(f_mid.subs(x,alpha)-v)==0
assert simplify(f_mid.subs(x,beta)-v)==0
assert simplify(f_right.subs(x,beta)-v)==0
assert diff(f_left,x)==-2*x # decreasing on [0,alpha]
assert diff(f_right,x)==2*(1-x) # increasing on [beta,1]
assert diff(f_mid,x,2)==-4 # concave => min endpoints
assert simplify(2*alpha*(1-alpha)-v)==0
assert simplify(v/F(4)-(sqrt(2)-1)/4)==0
assert simplify(F(1,4)*Rational(1,2)-Rational(1,8))==0

# More general time-inhomogeneous product decoder: per BU,j, first and second
# readout may have distinct Bernoulli parameters p,q.  Its TV with the repeated
# fair same-bit target is 1-min(A,1/2)-min(B,1/2), A=(1-p)(1-q), B=pq.
# Cauchy-Schwarz: sqrt(A)+sqrt(B)<=1. Over this region the maximal overlap
# min(A,1/2)+min(B,1/2) is 2-sqrt(2), attained at p=q=1-1/sqrt(2)
# (or p=q=1/sqrt(2)). This analytical proof, not a finite test, establishes
# the sharp global lower bound for ALL independent two-step emissions.
for p1,p2 in product([F(0),F(1,8),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(7,8),F(1)],repeat=2):
    A=(1-p1)*(1-p2); B=p1*p2
    f=1-min(A,F(1,2))-min(B,F(1,2))
    assert f>=F(2,5) # finite grid sanity check only, not sharpness proof
    for law in (0,1):
        actual=dist(law,'physical')
        simulated=dist(law,'memoryless',theta=((p1,p2),(p1,p2)))
        assert tv(actual,simulated)==F(1,4)*f
# Exact simultaneous P,Q minimax follows pointwise f(p,q)>=v, plus both BU masses=1/4.
# Repeated identical readout of a shared k: fresh per-call fair resampling incurs 1/8;
# persistent one-bit Bernoulli(k) sample reproduces BOTH laws for every transcript length.
print('PASS_BRC16_PQ_POSITIVE_NORMALIZED_AND_BU_J_MASSES')
print('BU P_j=',bu_p,' Q_j=',bu_q)
print('PASS_BOTH_LAWS_PERSISTENT_COUPLING_EXACT')
print('fresh fair per-call two-query TV P=Q=',tv(dist(0,'physical'),dist(0,'memoryless')))
print('sharp per-fiber independent-time product TV = sqrt(2)-1 =',v)
print('sharp global memoryless two-law radius = (sqrt(2)-1)/4 =',v/4)
print('sharp calibrated fair-one-query memoryless radius = 1/8')
print('PASS_BRC_N4_BU_SEQUENTIAL_SIMULATOR_MEMORYLESS_SHARP_BOUND_20261030')
