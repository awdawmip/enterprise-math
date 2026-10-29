#!/usr/bin/env python3
"""Exact scoped 16-leaf validation of sub-rho capacity pocket (author-side only).

The continuum theorem is PROOF.md; finite rational tests verify model realizability
and stated algebra, not reviewer independence or a formal EM admission.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

a,b,u,A,B,U,V=S.symbols('a b u A B U V',real=True)
w=(2*a-7*b)/(2*a+4*b)
delta=(1-a)/3
Bstar=b-delta
v=b*w/Bstar
H=b*w/4
L0=lambda x:(4*a-14*b-3*a*x-(a+3*b)*x*x)/(2*(23-2*x))
L3=lambda x:x*(a-(a+3*b)*x)/(2*(7-2*x))
T=a*a+38*a*b-7*a+105*b*b-14*b
G=5*a*a+8*a*b-21*b*b-2*b-5
E=Bstar*(7-a-21*b)/(4*(4*a+12*b+2))
checks=[]
def eq(label,x,y=0):
    z=S.factor(S.cancel(x-y))
    assert z==0,(label,z)
    checks.append(label)
eq('L0(w)=H',L0(w),H)
eq('L3(w)=H',L3(w),H)
eq('v=bw/Bstar',v,3*b*(2*a-7*b)/(2*(a+2*b)*(a+3*b-1)))
eq('L3(v)-H factor',L3(v)-H,-b*(a-1)*(2*a-7*b)*T/(8*(a+2*b)*(a+3*b-1)*(7*a*a+29*a*b-7*a+63*b*b-14*b)))
eq('positive last factor',(a+2*b)*(a+3*b-1)*(7-2*v),7*a*a+29*a*b-7*a+63*b*b-14*b)
eq('E-H exact factor',E-H,(1-a)*T/(24*(a+2*b)*(2*a+6*b+1)))
eq('T-derivative-a',S.diff(T,a),2*a+38*b-7)
eq('T-derivative-b',S.diff(T,b),38*a+210*b-14)
eq('G-derivative-a',S.diff(G,a),10*a+8*b)
eq('G-derivative-b',S.diff(G,b),8*a-42*b-2)
eq('L0-derivative numerator',S.factor(S.diff(L0(u),u)*2*(23-2*u)**2),a*(2*u*u-46*u-61)+b*(6*u*u-138*u-28))
eq('L3-derivative numerator',S.factor(S.diff(L3(u),u)*2*(7-2*u)**2),7*a-14*(a+3*b)*u+2*(a+3*b)*u*u)
loA,hiA=F(49,50),F(1)
loB,hiB=F(151,1000),F(77,500)
frac=lambda expr,aa,bb:F(str(S.factor(expr.subs({a:S.Rational(aa.numerator,aa.denominator),b:S.Rational(bb.numerator,bb.denominator)}))))
assert frac(T,loA,loB)==F(749,200000)>0
assert frac(G,loA,hiB)==F(50831,250000)>0
rmax=hiB/loA
assert rmax==F(11,70) and F(5889)-(F(25)+F(329)*rmax)**2==F(611,100)>0
assert loB/hiA>F(8,61) and loB>F(37,250)
assert 2*hiB<loA and (1-loA)/3 < loB/2

t=(A-a+3*(B-b))/4
s=(A-a+B-b)/2
J=B*u/4
rQ=a/6-A*u/6-U/3-V/4
rP=a/6-A*u/6-U/12-V/2
DQ=(s,J-s-rQ,rQ,-J)
DP=(t,J-t-rP,rP,-J)
pol={A:a,B:b,u:w,U:b*(1+w),V:b}
for label,seq,want in [('Q',DQ,(0,H,0,-H)),('P',DP,(0,0,H,-H))]:
    for j in range(4):eq('candidate-'+label+str(j),seq[j].subs(pol,simultaneous=True),want[j])
eq('P measured first-three event',sum(DP[:3]),J)
eq('P measured middle-two event',DP[1]+DP[2],J-t)
eq('t first-layer capacity',(1-a+3*(B-b))/4-t,(1-A)/4)

# Original declared 16 positive leaves under Q and P, source-labelled BU observation.
q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(k,j,z,q2[k]/4,q2[k]*rat[k][j]/4)
        for k in q2 for j in (0,1) for z in (0,1)]
assert len(leaves)==16 and all(q>0 and p>0 for k,j,z,q,p in leaves)
assert sum(q for _,_,_,q,p in leaves)==sum(p for _,_,_,q,p in leaves)==1

def terminal(law,aa,bb,AA,BB,uu,UU,VV,target):
    distribution=defaultdict(F)
    for k,j,z,q,p in leaves:
        mass=q if law=='Q' else p
        rate=(aa if k[0]=='A' else bb) if target else (AA if k[0]=='A' else BB)
        continuation=(F(1) if k=='AU' else F(0)) if target else {
            'AU':uu,'BU':uu,'AV':UU/AA,'BV':VV/BB}[k]
        assert 0<=rate<=1 and 0<=continuation<=1
        distribution[(1,'Q',0)]+=mass*(1-rate)
        distribution[(2,'Q',0)]+=mass*rate*(1-continuation)
        distribution[(3,'Q' if (k=='BU' and not target) else 'P',int(k=='BU'))]+=mass*rate*continuation
    assert sum(distribution.values())==1
    return distribution

def tv(x,y):
    return sum(abs(x.get(k,0)-y.get(k,0)) for k in x.keys()|y.keys())/2

witnesses=[(loA,loB),(loA,hiB),(hiA,loB),(hiA,hiB),(F(97,100),F(19,125)),
           (F(99,100),F(153,1000))]
for aa,bb in witnesses:
    ww=(2*aa-7*bb)/(2*aa+4*bb)
    BB=bb-(1-aa)/3
    vv=bb*ww/BB
    EE=BB*(7-aa-21*bb)/(4*(4*aa+12*bb+2))
    HH=bb*ww/4
    AA=aa;UU=bb*(1+ww);VV=bb
    assert 0<BB and 0<ww<F(3,7) and ww<=vv<1 and F(0)<UU<AA and VV==bb
    assert frac(T,aa,bb)>0 and frac(G,aa,bb)>0
    for law in ('Q','P'):
        tgt=terminal(law,aa,bb,AA,bb,ww,UU,VV,True)
        cmp=terminal(law,aa,bb,AA,bb,ww,UU,VV,False)
        assert tv(tgt,cmp)==HH,(aa,bb,law,tv(tgt,cmp),HH)
    assert EE>=HH and (EE>HH if aa<1 else EE==HH)
    lv=frac(L3(v),aa,bb)
    assert lv>=HH
    print('WITNESS','a=',aa,'b=',bb,'w=',ww,'v=',vv,'TV_P=TV_Q=',HH,'E-H=',EE-HH,'L3(v)-H=',lv-HH)
print('PASS_SYMBOLIC_IDENTITIES',len(checks))
print('PASS_RATIONAL_CORNER_BOUNDS','Tmin=',frac(T,loA,loB),'Gmin=',frac(G,loA,hiB),
      'rmax=',rmax,'rho_squared_margin=',F(611,100))
print('PASS_16_STRICT_POSITIVE_PQ_LEAVES',len(leaves),'witnesses',len(witnesses))
print('PASS_ALL_REAL_CONTINUATION_ANALYTIC_SPLICE_IN_PROOF')
print('STATUS AUTHOR_SIDE_PORTABLE_UNREVIEWED_NOT_ADMITTED')
