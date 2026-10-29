#!/usr/bin/env python3
"""Author-side exact checker for BRC N4 BU adaptive splice k(a) through b<=37/250.

Checks symbolic polynomial identities and exact rational 16-leaf P/Q observations.
The universal real-domain proof is in PROOF.md and is not established merely
by sampling; the inherited 16-leaf causal reduction and legal TV event bounds
are cited from earlier research and await independent mathematical review.
"""
from fractions import Fraction as F
from collections import defaultdict
import sympy as S

a,b,u,A,B,U,V=S.symbols('a b u A B U V', real=True)
a0=S.Rational(9607,10000); b1=S.Rational(37,250)
k=a/4+S.Rational(11,100)
delta=(1-a)/3
Bs=b-delta
C=(7-a-21*b)/(4*a+12*b+2)
E=S.factor(Bs*C/4)
G=5*a*a+8*a*b-21*b*b-2*b-5
L0=lambda z:(4*a-14*b-3*a*z-(a+3*b)*z*z)/(2*(23-2*z))
L3=lambda z:z*(a-(a+3*b)*z)/(2*(7-2*z))
N0=3750*a**4+22500*a**3*b+51425*a**3+33750*a**2*b**2+190425*a**2*b-262274*a**2+108450*a*b**2-1230594*a*b+354613*a-1061316*b**2+2812989*b-398650
f1=50*a*a+150*a*b+97*a+1116*b-339
f2=75*a*a+225*a*b-317*a-951*b+350
checks=[]
def eq(name,got,want=0):
    diff=S.factor(S.together(got-want))
    assert diff==0,(name,diff)
    checks.append(name)

eq('L0 adaptive gap',L0(k)-E,N0/(1200*(25*a-1139)*(2*a+6*b+1)))
eq('L3 adaptive gap',L3(k)-E,f1*f2/(1200*(25*a-339)*(2*a+6*b+1)))
eq('L3 capacity meeting',L3(C),E)
eq('G capacity slack',E-delta,G/(8*(2*a+6*b+1)))
eq('G at a0 vertex',G.subs({a:a0,b:(4*a0-1)/21}),S.Rational(-310557,700000000))
eq('G on auxiliary lower line',G.subs(a,1-S.Rational(3,5)*b),-24*b*b)
eq('N0_b derivative',S.diff(N0,b),3*(7500*a**3+22500*a*a*b+63475*a*a+72300*a*b-410198*a-707544*b+937663))
eq('N0_a at b1',S.diff(N0,a).subs(b,b1),15000*a**3+164265*a*a-S.Rational(11667592,25)*a+S.Rational(218575721,1250))
eq('N0 corner',N0.subs({a:a0,b:b1}),S.Rational(-9702523137476277,8000000000000))
eq('N0_b certified lower',3*(937663-410198-707544*b1),S.Rational(158530683,125))
eq('N0_a certified upper',15000+164265+S.Rational(218575721,1250)-S.Rational(11667592,25)*a0,S.Rational(-1472447634,15625))
eq('f1 max',f1.subs({a:1,b:b1}),-S.Rational(579,125))
eq('f2 min',f2.subs({a:1,b:b1}),S.Rational(69,125))
eq('C at upper corner',C.subs({a:1,b:b1}),S.Rational(241,648))
eq('C minus k corner',(C-k).subs({a:1,b:b1}),S.Rational(193,16200))
eq('dC/da',S.diff(C,a),-(30-72*b)/(4*a+12*b+2)**2)
eq('dC/db',S.diff(C,b),-(72*a+126)/(4*a+12*b+2)**2)

# Verify achieving policy matches both complete four-atom signed differences.
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*u/4
rQ=a/6-A*u/6-U/3-V/4
rP=a/6-A*u/6-U/12-V/2
DQ=(s,H-s-rQ,rQ,-H)
DP=(t,H-t-rP,rP,-H)
sel={A:S.Integer(1),B:Bs,u:C,U:Bs*(1+C),V:Bs}
for name,obs,want in [('Q',DQ,(delta,E-delta,0,-E)),('P',DP,(0,0,E,-E))]:
    for i,(left,right) in enumerate(zip(obs,want)):
        eq('achieving '+name+' atom '+str(i),left.subs(sel,simultaneous=True),right)

# All sixteen (branch, hidden bit, hidden bit) positive leaves, with exact P/Q masses.
q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaf=[(branch,q2[branch]/4,q2[branch]*rat[branch][j]/4)
      for branch in q2 for j in (0,1) for z in (0,1)]
assert len(leaf)==16 and all(q>0 and p>0 for _,q,p in leaf)
assert sum(q for _,q,_ in leaf)==sum(p for _,_,p in leaf)==F(1)

def observe(law,aa,bb,AA,BB,cc,UU,VV,target):
    obs=defaultdict(F)
    for branch,qmass,pmass in leaf:
        mass=qmass if law=='Q' else pmass
        first=(aa if branch[0]=='A' else bb) if target else (AA if branch[0]=='A' else BB)
        second=(F(1) if branch=='AU' else F(0)) if target else {
            'AU':cc,'BU':cc,'AV':UU/AA,'BV':VV/BB}[branch]
        assert F(0)<=first<=F(1) and F(0)<=second<=F(1)
        obs[(1,'Q',0)]+=mass*(1-first)
        obs[(2,'Q',0)]+=mass*first*(1-second)
        obs[(3,'Q' if (branch=='BU' and not target) else 'P',int(branch=='BU'))]+=mass*first*second
    assert sum(obs.values())==F(1)
    return obs

def tv(P,Q):
    return sum(abs(P.get(key,F(0))-Q.get(key,F(0)))
               for key in P.keys()|Q.keys())/2

params=[(F(481,500),F(37,250)),(F(97,100),F(37,250)),
        (F(99,100),F(37,250)),(F(1),F(37,250)),
        (F(481,500),F(147,1000))]
for aa,bb in params:
    GG=5*aa**2+8*aa*bb-21*bb**2-2*bb-5
    assert GG>=0 and F(0)<bb<=F(37,250) and F(0)<aa<=1
    dd=(1-aa)/3; BC=bb-dd; cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    ee=BC*cc/4; UU=BC*(1+cc)
    assert F(0)<BC<=1 and F(0)<cc<1 and F(0)<=UU<=1 and ee>=dd
    for law in ('P','Q'):
        target=observe(law,aa,bb,F(1),BC,cc,UU,BC,True)
        competitor=observe(law,aa,bb,F(1),BC,cc,UU,BC,False)
        actual=tv(target,competitor)
        assert actual==ee,(law,aa,bb,actual,ee)
    print('EXACT_16_LEAF_WITNESS a=',str(aa),'b=',str(bb),
          'G=',str(GG),'u=',str(cc),'TV_P=TV_Q=',str(ee),sep='')
print('PASS_SYMBOLIC_IDENTITIES',len(checks))
print('PASS_EXACT_PQ_16_LEAF_CASES',len(params))
print('PASS_BRC_N4_BU_ADAPTIVE_SPLICE_TO_37_OVER_250_AUTHOR_ONLY')
