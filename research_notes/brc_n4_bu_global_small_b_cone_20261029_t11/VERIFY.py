#!/usr/bin/env python3
"""Exact author-side verifier for BRC N=4 BU small-b cone (2026-10-29).
Mathematical universal inference relies on analytic proof; finite tests are not a proof.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

a,b,A,B,c,U,V=S.symbols('a b A B c U V', real=True)
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
h=B*c/4
rq=a/6-A*c/6-U/3-V/4
rp=a/6-A*c/6-U/12-V/2
DQ=(s,h-s-rq,rq,-h)
DP=(t,h-t-rp,rp,-h)
L0=(4*a-14*b-3*a*c-(a+3*b)*c**2)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
K=b*c/(4+c)
f=(a+3*b)*c**2+(3*a+8*b)*c+14*b-4*a
H=b*c/(4+c)

checks=0
def eq(x,y):
    global checks
    z=S.factor(S.together(x-y))
    assert z==0, z
    checks+=1

eq(f.subs(c,S.Rational(3,7)),-(124*a-881*b)/49)
eq(f.subs(c,1),25*b)
eq(L0.subs(c,S.Rational(3,7)),(4*a-23*b)/70)
eq(L3.subs(c,S.Rational(3,7)),3*(4*a-9*b)/602)
eq(L0.subs(c,S.Rational(3,7))-b/5,(4*a-37*b)/70)
eq(L3.subs(c,S.Rational(3,7))-b/5,(60*a-737*b)/3010)
eq(L3-K,-c*f/(2*(7-2*c)*(4+c)))
# Independent nonnegative event-mixture certificates. Terms V-B are nonpositive.
Q1,Q2,Q3,Q7,P4,P5,P6,Qs=s,h-s-rq,h-rq,h,rp,t+rp,h-t,h-s
m0=((c+4)*Q2+(3-7*c)*Qs+2*(1+4*c-c*c)*P4+2*(c*c-2*c+7)*P5)/(23-2*c)
m3=(c*Q3+7*(1-c)*Q7+2*c*(2-c)*P4+2*c*c*P5)/(7-2*c)
mk=(c*Q1+(4-2*c)*Q7+2*c*P6)/(4+c)
eq(L0,m0+7*(c+4)*(V-B)/(4*(23-2*c)))
eq(L3,m3+7*c*(V-B)/(4*(7-2*c)))
eq(K,mk)
eq(S.diff(L0,c),(a*(2*c*c-46*c-61)+b*(6*c*c-138*c-28))/(2*(23-2*c)**2))
eq(S.diff(L3,c),(7*a-14*(a+3*b)*c+2*(a+3*b)*c*c)/(2*(7-2*c)**2))
# Candidate strategy produces exact signed deltas modulo f=0.
strategy={A:a+3*H,B:4*b/(4+c),U:4*b*(1+c)/(4+c),V:4*b/(4+c)}
for vec,goal in [(DQ,(H,0,0,-H)),(DP,(0,0,H,-H))]:
    for expr,expected in zip(vec,goal):
        remainder=S.rem(S.together((expr-expected).subs(strategy,simultaneous=True)).as_numer_denom()[0],f,c)
        eq(remainder,0)
# Numerical rational 16-leaf checks (not a universal inference).
q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratios={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
        'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(cat,j,k,q2[cat]/4,q2[cat]/4*ratios[cat][j])
        for cat in q2 for j in (0,1) for k in (0,1)]
assert len(leaves)==16
assert all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(x[3] for x in leaves)==sum(x[4] for x in leaves)==1

def obs(law,par,target):
    aa,bb,AA,BB,cc,UU,VV=par
    out=defaultdict(F)
    for cat,j,k,q,p in leaves:
        mass=q if law=='Q' else p
        root=cat[0]
        x=(aa if root=='A' else bb) if target else (AA if root=='A' else BB)
        if target:
            y=F(1) if cat=='AU' else F(0)
        else:
            y={'AU':cc,'BU':cc,'AV':UU/AA if AA else F(0),
               'BV':VV/BB if BB else F(0)}[cat]
        assert 0<=x<=1 and 0<=y<=1
        out[(1,'Q',0)]+=mass*(1-x)
        out[(2,'Q',0)]+=mass*x*(1-y)
        out[(3,'Q' if cat=='BU' and not target else 'P',1 if cat=='BU' else 0)]+=mass*x*y
    assert sum(out.values())==1
    return out

def tv(x,y): return sum(abs(x.get(k,0)-y.get(k,0)) for k in set(x)|set(y))/2

cases=[]
for aa,cc in [(F(1,10),F(4,5)),(F(1,2),F(4,5)),(F(9,10),F(4,5)),
              (F(3,4),F(9,10)),(F(1,4),F(19,20))]:
    bb=aa*(1-cc)*(4+cc)/(3*cc*cc+8*cc+14)
    HH=bb*cc/(4+cc)
    AA=aa+3*HH;BB=4*bb/(4+cc);UU=BB*(1+cc);VV=BB
    assert F(0)<bb<=F(60,737)*aa and aa+F(3,5)*bb<=1
    assert 0<cc<1 and 0<=AA<=1 and 0<=BB<=1 and 0<=UU<=AA and 0<=VV<=BB
    assert (aa+3*bb)*cc**2+(3*aa+8*bb)*cc+14*bb-4*aa==0
    params=(aa,bb,AA,BB,cc,UU,VV)
    vals=[]
    for law in ('Q','P'):
        target=obs(law,params,True)
        competitor=obs(law,params,False)
        loss=tv(target,competitor)
        assert loss==HH, (law,loss,HH)
        vals.append(loss)
    cases.append({'a':str(aa),'b':str(bb),'c':str(cc),'TV_Q':str(vals[0]),'TV_P':str(vals[1])})
assert cases[1]['TV_Q']=='1/279'
assert cases[2]['TV_Q']=='1/155'
assert S.Rational(60,737)<S.Rational(4,37)
assert S.Rational(60,737)<S.Rational(124,881)
print('EXACT_SYMBOLIC_CHECKS',checks)
print('EXACT_16_LEAF_MASS',len(leaves),'P_Q_TOTALS',1,1)
print('RATIONAL_CASES',cases)
print('PASS_EXACT_BRC_N4_BU_GLOBAL_SMALL_B_CONE_20261029')
