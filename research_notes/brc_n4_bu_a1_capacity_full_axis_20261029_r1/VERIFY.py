#!/usr/bin/env python3
"""Exact verification of BRC N4 BU a=1 capacity-axis theorem (author-side).

Checks symbolic identities supporting the analytic proof, and reconstructs
both P/Q laws from 16 strictly positive leaves at rational test parameters.
Finite tests audit algebra and realizability; continuum optimality is PROOF.md.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

b,c = S.symbols('b c', real=True)
a,A,B,u,U,V = S.symbols('a A B u U V', real=True)
s = (A-a+B-b)/2
t = (A-a+3*(B-b))/4
H = B*u/4
rQ = a/6-A*u/6-U/3-V/4
rP = a/6-A*u/6-U/12-V/2
DQ = (s,H-s-rQ,rQ,-H)
DP = (t,H-t-rP,rP,-H)
w = (2-7*b)/(2+4*b)
E = S.factor(b*w/4)
L0 = lambda x: (4-14*b-3*x-(1+3*b)*x*x)/(2*(23-2*x))
L3 = lambda x: x*(1-(1+3*b)*x)/(2*(7-2*x))
checks=[]
def eq(label,x,y=0):
    z=S.factor(S.cancel(x-y))
    assert z==0, (label,z)
    checks.append(label)

# Exact lower-certificate anchors and case splits.
eq('L0-w-anchor',L0(w),E)
eq('L3-w-anchor',L3(w),E)
eq('L0-3/7-gap',L0(S.Rational(3,7))-E,(b-2)*(61*b-8)/(280*(2*b+1)))
eq('L3-3/7-gap',L3(S.Rational(3,7))-E,(31*b-6)*(61*b-8)/(2408*(2*b+1)))
eq('w-3/7-threshold',w-S.Rational(3,7),(8-61*b)/(7*(2+4*b)))
# Universal event-capacity bound is established by the two cases B>=b, B<b.
# Check observed-event identities directly.
eq('P-event-H-t',DP[1]+DP[2],H-t)
eq('P-event-H',DP[0]+DP[1]+DP[2],H)
eq('Q-event-H',DQ[0]+DQ[1]+DQ[2],H)
eq('capacity-t',t.subs(a,1), (A-1+3*(B-b))/4)
# Derivative sign polynomials (each denominator strictly positive on domain).
num0=S.factor(S.diff(L0(c),c)* 2*(23-2*c)**2)
eq('L0-derivative',num0,2*c*c-46*c-61+b*(6*c*c-138*c-28))
num3=S.factor(S.diff(L3(c),c)* 2*(7-2*c)**2)
eq('L3-derivative',num3,7-14*(1+3*b)*c+2*(1+3*b)*c*c)
# The law-correct feasible root-upper strategy and zero strategy.
policy={a:S.Integer(1),A:S.Integer(1),B:b,u:w,U:b*(1+w),V:b}
for law, delta, want in [('Q',DQ,(0,E,0,-E)),('P',DP,(0,0,E,-E))]:
    for i,(actual,target) in enumerate(zip(delta,want)):
        eq('policy-'+law+str(i),actual.subs(policy,simultaneous=True),target)
zero={a:S.Integer(1),A:S.Integer(1),B:b,u:S.Integer(0),U:S.Rational(2,7),V:S.Rational(2,7)}
for law,delta in [('Q',DQ),('P',DP)]:
    for i,actual in enumerate(delta):eq('zero-'+law+str(i),actual.subs(zero,simultaneous=True))
# Exact capacity-collision curve parameterization.
C=S.symbols('C',real=True)
D=3*C*C+8*C+14
r=(1-C)*(4+C)/D
q=S.factor(r*C/(4+C))
a_cap=D/(11*C+14)
eq('root-homogeneity',q,C*(1-C)/D)
eq('root-capacity-alpha',a_cap*(1+3*q),1)
eq('root-capacity-b',a_cap*r,(1-C)*(4+C)/(11*C+14))
eq('C=half-r',r.subs(C,S.Rational(1,2)),S.Rational(3,25))
eq('C=half-alpha',a_cap.subs(C,S.Rational(1,2)),S.Rational(25,26))

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(k,q2[k]/4,q2[k]*rat[k][j]/4) for k in q2 for j in (0,1) for _ in (0,1)]
assert len(leaves)==16 and all(p>0 and q>0 for k,q,p in leaves)
assert sum(q for k,q,p in leaves)==F(1) and sum(p for k,q,p in leaves)==F(1)

def lawvec(law,aa,bb,AA,BB,cc,UU,VV,target):
    dist=defaultdict(F)
    for k,q,p in leaves:
        mass=q if law=='Q' else p
        rate=(aa if k[0]=='A' else bb) if target else (AA if k[0]=='A' else BB)
        if target:
            continue2=F(1) if k=='AU' else F(0)
        else:
            continue2={'AU':cc,'BU':cc,'AV':UU/AA if AA else F(0),
                       'BV':VV/BB if BB else F(0)}[k]
        assert 0<=rate<=1 and 0<=continue2<=1
        dist[(1,'Q',0)]+=mass*(1-rate)
        dist[(2,'Q',0)]+=mass*rate*(1-continue2)
        dist[(3,'Q' if (k=='BU' and not target) else 'P',int(k=='BU'))]+=mass*rate*continue2
    assert sum(dist.values())==F(1)
    return dist

def tv(d1,d2):return sum(abs(d1.get(k,F(0))-d2.get(k,F(0))) for k in d1.keys()|d2.keys())/2

witnesses=[]
for bb in (F(1,1000),F(1,25),F(3,25),F(8,61),F(1,7),F(1,4),F(2,7),F(1,2),F(1)):
    aa=F(1)
    if bb<=F(2,7):
        cc=(2-7*bb)/(2+4*bb)
        AA=aa; BB=bb;UU=bb*(1+cc);VV=bb
        expected=bb*cc/4
    else:
        cc=F(0);AA=aa;BB=bb;UU=F(2,7);VV=F(2,7)
        expected=F(0)
    for law in ('P','Q'):
        target=lawvec(law,aa,bb,AA,BB,cc,UU,VV,True)
        comp=lawvec(law,aa,bb,AA,BB,cc,UU,VV,False)
        assert tv(target,comp)==expected, (bb,law,tv(target,comp),expected)
    witnesses.append(f'b={bb}: TV_P=TV_Q={expected}, c={cc}, U={UU}')

# Rational counterexample to extending the old root value into the infeasible face.
bb=F(3,25); root=F(1,2); h=bb*root/(4+root); gap=F(87,6200)-h
assert h==F(1,75) and gap==F(13,18600)>0
assert 1+3*h==F(26,25)>1
print('PASS_SYMBOLIC_IDENTITIES',len(checks))
print('PASS_16_LEAF_LAWS',len(leaves),'strictly_positive_per_law',len(witnesses),'rational_witnesses')
for line in witnesses:print(line)
print('CAPACITY_OBSTRUCTION_C_HALF',f'r={F(3,25)}',f'a_cap={F(25,26)}',f'root_h={h}',f'actual={F(87,6200)}',f'gap={gap}')
print('PASS_BRC_N4_BU_A1_FULL_AXIS_20261029_AUTHOR')
