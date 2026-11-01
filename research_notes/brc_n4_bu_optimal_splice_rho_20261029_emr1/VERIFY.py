#!/usr/bin/env python3
"""Author-side exact verification of an optimized L0/L3/K split certificate.
The universal theorem is analytic; the finitely many leaf checks only validate
symbolic identities and concrete rational stochastic strategies.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

z,c,a,b,A,B,U,V=S.symbols('z c a b A B U V', real=True)
D=3*c**2+8*c+14
r=(1-c)*(4+c)/D
h=c*(1-c)/D
f=(a+3*b)*c**2+(3*a+8*b)*c+14*b-4*a
L0=lambda w:(4*a-14*b-3*a*w-(a+3*b)*w*w)/(2*(23-2*w))
L3=lambda w:w*(a-(a+3*b)*w)/(2*(7-2*w))
K=lambda w:b*w/(4+w)
sqrt=S.sqrt
k0=(87-sqrt(5889))/30
c0=(sqrt(5889)-73)/10
rho=(sqrt(5889)-25)/329
kreq=14*(1-c)/(26-c)
checks=[]
def eq(tag,expr,expected=0):
    delta=S.simplify(S.factor(S.together(expr-expected)))
    assert delta==0,(tag,delta)
    checks.append(tag)

eq('f_inversion',f.subs({a:1,b:r}))
eq('r_monotonic_derivative',S.diff(r,c),(c*c-52*c-74)/D**2)
eq('threshold_k',15*k0**2-87*k0+28)
eq('threshold_c',5*c0**2+73*c0-28)
eq('threshold_r',329*rho**2+50*rho-16)
eq('threshold_r_inversion',r.subs(c,c0),rho)
eq('threshold_kreq',kreq.subs(c,c0),k0)
eq('L0_gap',(L0(z).subs({a:1,b:r})-h), (13*c*c*z-72*c*c-c*z*z+20*c*z-28*c+26*z*z+42*z)/(2*(2*z-23)*D))
eq('L3_gap',(L3(z).subs({a:1,b:r})-h),(c-z)*(c*z-14*c-26*z+14)/(2*(2*z-7)*D))
eq('L0_kreq',(L0(kreq).subs({a:1,b:r})-h),(11*c+14)*(5*c*c+73*c-28)/(5*(c+114)*D))
eq('L0_boundary',(L0(k0).subs({a:1,b:r})-h).subs(c,c0))
eq('L3_boundary',(L3(k0).subs({a:1,b:r})-h).subs(c,c0))
eq('L3_equals_K_at_root',L3(c).subs({a:1,b:r})-h)
eq('L3_K_general',L3(c)-K(c),-c*f/(2*(7-2*c)*(4+c)))
assert 0<float(k0)<float(c0)<S.Rational(3,7)<1
assert 0<float(rho)<S.Rational(2,7)
# An exact negative gap outside the split-certificate bound; this is not a minimax counterexample.
cout=F(9,25)
rout=F(1-cout)*(4+cout)/(3*cout*cout+8*cout+14)
hout=F(cout*(1-cout))/(3*cout*cout+8*cout+14)
kout=F(14*(1-cout))/(26-cout)
L0out=(4-14*rout-3*kout-(1+3*rout)*kout*kout)/(2*(23-2*kout))
assert rout>float(rho) and L0out-hout<0

# Direct observable-event certificate verification (symbolic 4-atom representation).
H=B*c/4
ss=(A-a+B-b)/2
st=(A-a+3*(B-b))/4
rq=a/6-A*c/6-U/3-V/4
rp=a/6-A*c/6-U/12-V/2
Q1,Q2,Q3,Q7,P4,P5,P6,Qs=ss,H-ss-rq,H-rq,H,rp,st+rp,H-st,H-ss
m0=((c+4)*Q2+(3-7*c)*Qs+2*(1+4*c-c*c)*P4+2*(c*c-2*c+7)*P5)/(23-2*c)
m3=(c*Q3+7*(1-c)*Q7+2*c*(2-c)*P4+2*c*c*P5)/(7-2*c)
mk=(c*Q1+(4-2*c)*Q7+2*c*P6)/(4+c)
eq('L0_event_mix',L0(c),m0+7*(c+4)*(V-B)/(4*(23-2*c)))
eq('L3_event_mix',L3(c),m3+7*c*(V-B)/(4*(7-2*c)))
eq('K_event_mix',K(c),mk)
# Check coefficient sums and positivity is analytic on their domains.
eq('L0_coeffs_sum',(c+4)+(3-7*c)+2*(1+4*c-c*c)+2*(c*c-2*c+7),23-2*c)
eq('L3_coeffs_sum',c+7*(1-c)+2*c*(2-c)+2*c*c,7-2*c)
eq('K_coeffs_sum',c+(4-2*c)+2*c,4+c)
# Algebraic equality of the constructed causal upper bound for every root f(c)=0.
strategy={A:a+3*K(c), B:4*b/(4+c), U:4*b*(1+c)/(4+c), V:4*b/(4+c)}
DQ=(ss,H-ss-rq,rq,-H)
DP=(st,H-st-rp,rp,-H)
for law,vector,goal in [('Q',DQ,(K(c),0,0,-K(c))),('P',DP,(0,0,K(c),-K(c)))]:
    for i,(actual,desired) in enumerate(zip(vector,goal)):
        expr=S.together((actual-desired).subs(strategy,simultaneous=True)).as_numer_denom()[0]
        eq(f'{law}_strategy_atom_{i}',S.rem(expr,f,c))

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratios={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
        'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(cat,j,m,q2[cat]/4,q2[cat]*ratios[cat][j]/4)
        for cat in q2 for j in (0,1) for m in (0,1)]
assert len(leaves)==16
assert all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(row[3] for row in leaves)==sum(row[4] for row in leaves)==1

def distribution(law,params,target):
    aa,bb,AA,BB,cc,UU,VV=params
    out=defaultdict(F)
    for cat,j,m,q,p in leaves:
        prob=q if law=='Q' else p
        root=cat[0]
        xx=(aa if root=='A' else bb) if target else (AA if root=='A' else BB)
        if target:
            yy=F(1) if cat=='AU' else F(0)
        else:
            yy={'AU':cc,'BU':cc,'AV':UU/AA if AA else F(0), 'BV':VV/BB if BB else F(0)}[cat]
        assert 0<=xx<=1 and 0<=yy<=1
        out[(1,'Q',0)]+=prob*(1-xx)
        out[(2,'Q',0)]+=prob*xx*(1-yy)
        out[(3,'Q' if cat=='BU' and not target else 'P',1 if cat=='BU' else 0)]+=prob*xx*yy
    assert sum(out.values())==1
    return out

def tv(x,y):return sum(abs(x.get(z,0)-y.get(z,0)) for z in x.keys()|y.keys())/2

witnesses=[]
for aa,cc in [(F(1,2),F(3,8)),(F(19,20),F(3,8)),(F(1,2),F(2,5)),
              (F(3,4),F(1,2)),(F(9,10),F(4,5))]:
    rr=(1-cc)*(4+cc)/(3*cc*cc+8*cc+14)
    bb=aa*rr
    hh=bb*cc/(4+cc)
    AA=aa+3*hh;BB=4*bb/(4+cc);UU=BB*(1+cc);VV=BB
    assert 0<rr<=float(rho)
    assert 0<aa<1 and 0<bb<=1 and 0<=AA<=1 and 0<=BB<=1 and 0<=UU<=AA and 0<=VV<=BB
    assert (aa+3*bb)*cc**2+(3*aa+8*bb)*cc+14*bb-4*aa==0
    params=(aa,bb,AA,BB,cc,UU,VV)
    vq=tv(distribution('Q',params,True),distribution('Q',params,False))
    vp=tv(distribution('P',params,True),distribution('P',params,False))
    assert vq==vp==hh,(params,vq,vp,hh)
    witnesses.append((str(aa),str(bb),str(cc),str(hh)))
print('PASS_SYMBOLIC_IDENTITIES',len(checks))
print('OPTIMAL_STITCH',str(k0),str(c0),str(rho))
print('THRESHOLD_DECIMALS',*[str(S.N(v,15)) for v in [k0,c0,rho]])
print('OUTSIDE_CERTIFICATE_SCOPE',str(cout),str(rout),str(kout),'L0_GAP',str(L0out-hout))
print('PASS_16_LEAF_RATIONAL_WITNESSES',witnesses)
print('PASS_BRC_N4_BU_OPTIMAL_L0_L3_K_STITCH_20261029')
