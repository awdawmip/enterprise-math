#!/usr/bin/env python3
"""Exact author-side BRC N4 BU curved-capacity certificate checker.
Scope: symbolic event inequalities, algebraic boundary, six 16-leaf P/Q witnesses.
It does NOT prove the 16-leaf-to-four-atom reduction anew or grant formal review.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

a,b,u,A,B,U,V = S.symbols('a b u A B U V',real=True)
d=(1-a)/3
G=5*a*a+8*a*b-21*b*b-2*b-5
P=131*a*a+576*a*b-232*a+549*b*b-1746*b+245
q=24045*b*b-26924*b+3040
alpha=(-4*b+S.sqrt(121*b*b+10*b+25))/5
bs=(S.Integer(13462)-82*S.sqrt(16081))/24045
C=(7-a-21*b)/(4*a+12*b+2)
Bs=b-d
E=S.factor(Bs*C/4)
L0=lambda x:(4*a-14*b-3*a*x-(a+3*b)*x*x)/(2*(23-2*x))
L3=lambda x:x*(a-(a+3*b)*x)/(2*(7-2*x))
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*u/4
rQ=a/6-A*u/6-U/3-V/4
rP=a/6-A*u/6-U/12-V/2
DQ=(s,H-s-rQ,rQ,-H)
DP=(t,H-t-rP,rP,-H)
checks=[]
def eq(label,x,y=0):
    z=S.factor(S.cancel(x-y))
    assert z==0,(label,z)
    checks.append(label)

eq('quadratic-root',G.subs(a,alpha))
eq('L3(C)=E',L3(C),E)
eq('E-d',E-d,G/(8*(2*a+6*b+1)))
eq('C-3/7',C-S.Rational(3,7),(43-19*a-183*b)/(7*(4*a+12*b+2)))
eq('1-C',1-C,(5*a+33*b-5)/(2*(2*a+6*b+1)))
eq('L0(3/7)-E',L0(S.Rational(3,7))-E,P/(840*(2*a+6*b+1)))
eq('L3(3/7)-E',L3(S.Rational(3,7))-E,(19*a+183*b-43)*(31*a+93*b-49)/(7224*(2*a+6*b+1)))
eq('resultant',S.resultant(G,P,a),-144*(12*b-5)*q)
eq('root-q',q.subs(b,bs))
eq('q(127/1000)',q.subs(b,S.Rational(127,1000)),S.Rational(1694761,200000))
eq('q(128/1000)',q.subs(b,S.Rational(16,125)),S.Rational(-38496,3125))
eq('G(1-3b/5)',G.subs(a,1-S.Rational(3,5)*b),-24*b*b)
eq('G(24/25,13/100)',G.subs({a:S.Rational(24,25),b:S.Rational(13,100)}),S.Rational(-17,2000))
eq('G(961/1000,13/100)',G.subs({a:S.Rational(961,1000),b:S.Rational(13,100)}),S.Rational(429,200000))
eq('P(961/1000,13/100)',P.subs({a:S.Rational(961,1000),b:S.Rational(13,100)}),S.Rational(-2712969,1000000))
eq('P(1,0)',P.subs({a:1,b:0}),144)
eq('P derivative a',S.diff(P,a),262*a+576*b-232)
eq('G derivative a',S.diff(G,a),10*a+8*b)
R=-(1374*b*b-2117*b+470)/(2*(229*b-145))
eq('P remainder mod G',S.rem(P,G,a),4*(458*a*b-290*a+1374*b*b-2117*b+470)/5)
eq('P remainder vanishes at R',S.rem(P,G,a).subs(a,R))
eq('G(R) factor',G.subs(a,R),-45*(12*b-5)*q/(4*(229*b-145)**2))
eq('G(R(bs))',G.subs(a,R).subs(b,bs))
eq('middle two P-event',DP[1]+DP[2],H-t)
eq('first three P-event',sum(DP[:3]),H)
eq('t capacity upper',t-(1-a+3*(B-b))/4,(A-1)/4)
sel={A:1,B:Bs,u:C,U:Bs*(1+C),V:Bs}
for law,vec,want in [('Q',DQ,(d,E-d,0,-E)),('P',DP,(0,0,E,-E))]:
    for i in range(4):eq('candidate-'+law+'-'+str(i),vec[i].subs(sel,simultaneous=True),want[i])

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaf=[(k,q2[k]/4,q2[k]*rat[k][j]/4) for k in q2 for j in (0,1) for z in (0,1)]
assert len(leaf)==16 and all(qmass>0 and pmass>0 for _,qmass,pmass in leaf)
assert sum(qmass for _,qmass,_ in leaf)==sum(pmass for _,_,pmass in leaf)==1

def observe(law,aa,bb,AA,BB,cc,UU,VV,target):
    out=defaultdict(F)
    for k,qmass,pmass in leaf:
        mass=qmass if law=='Q' else pmass
        one=(aa if k[0]=='A' else bb) if target else (AA if k[0]=='A' else BB)
        two=(F(1) if k=='AU' else F(0)) if target else {'AU':cc,'BU':cc,'AV':UU/AA,'BV':VV/BB}[k]
        assert F(0)<=one<=F(1) and F(0)<=two<=F(1)
        out[(1,'Q',0)]+=mass*(1-one)
        out[(2,'Q',0)]+=mass*one*(1-two)
        out[(3,'Q' if (k=='BU' and not target) else 'P',int(k=='BU'))]+=mass*one*two
    assert sum(out.values())==1
    return out

def tv(x,y):return sum(abs(x.get(k,F(0))-y.get(k,F(0))) for k in x.keys()|y.keys())/2

params=[(F(999,1000),F(1,100)),(F(99,100),F(1,20)),(F(193,200),F(9,100)),
        (F(481,500),F(3,25)),(F(961,1000),F(1,8)),(F(1),F(127,1000))]
for aa,bb in params:
    assert F(0)<bb<F(128,1000)
    gg=5*aa**2+8*aa*bb-21*bb**2-2*bb-5
    assert gg>=0
    dd=(1-aa)/3
    BC=bb-dd
    cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    ee=BC*cc/4
    uu=BC*(1+cc)
    assert 0<BC<1 and F(3,7)<=cc<1 and 0<=uu<=1 and ee>=dd
    for law in 'PQ':
        target=observe(law,aa,bb,F(1),BC,cc,uu,BC,True)
        comp=observe(law,aa,bb,F(1),BC,cc,uu,BC,False)
        assert tv(target,comp)==ee,(aa,bb,law,tv(target,comp),ee)
    print('WITNESS',str(aa),str(bb),'C',str(cc),'P_TV=Q_TV',str(ee))
print('PASS_EXACT_SYMBOLIC',len(checks))
print('PASS_SIX_16LEAF_PQ_RATIONAL_WITNESSES')
print('PASS_BRC_N4_BU_CURVED_CAPACITY_SHARP_STITCH_BOUND_20261029')
