#!/usr/bin/env python3
"""Exact verification of author-side b <= 3/20 adaptive splice theorem.

Model and observation mapping are inherited from the cited 16-leaf BRC N=4
BU finite model; this checks algebraic identities and finitely many rational
witnesses, not all-real universal quantification or independent admission.
"""
from fractions import Fraction as F
from collections import defaultdict
import sympy as S

a,b,u,A,B,U,V=S.symbols('a b u A B U V',real=True)
a0=S.Rational(9607,10000)
b1=S.Rational(3,20)
k=S.Rational(3,5)*a-S.Rational(59,250)
delta=(1-a)/3
Bs=b-delta
C=(7-a-21*b)/(4*a+12*b+2)
E=S.factor(Bs*C/4)
G=5*a*a+8*a*b-21*b*b-2*b-5
L0=lambda z:(4*a-14*b-3*a*z-(a+3*b)*z*z)/(2*(23-2*z))
L3=lambda z:z*(a-(a+3*b)*z)/(2*(7-2*z))
N=45000*a**4+270000*a**3*b+218350*a**3+405000*a*a*b*b+680100*a*a*b-658988*a*a+75150*a*b*b-3223328*a*b+730981*a-2389092*b*b+6019943*b-855750
f1=300*a*a+900*a*b+157*a+2271*b-934
f2=450*a*a+1350*a*b-1052*a-3156*b+875
checks=[]
def eq(name,got,want=0):
    diff=S.factor(S.together(got-want))
    assert diff==0,(name,diff)
    checks.append(name)

eq('L0 gap expansion',L0(k)-E,N/(6000*(25*a-489)*(2*a+6*b+1)))
eq('L3 gap expansion',L3(k)-E,f1*f2/(6000*(75*a-467)*(2*a+6*b+1)))
eq('L3 and capacity meeting',L3(C),E)
eq('capacity slack from G',E-delta,G/(8*(2*a+6*b+1)))
eq('G at a0 parabola vertex',G.subs({a:a0,b:(4*a0-1)/21}),S.Rational(-310557,700000000))
eq('G lower comparison',G.subs(a,1-S.Rational(3,5)*b),-24*b*b)
eq('G at a=1',G.subs(a,1),3*b*(2-7*b))
eq('dC/da',S.diff(C,a),-(30-72*b)/(4*a+12*b+2)**2)
eq('dC/db',S.diff(C,b),-(72*a+126)/(4*a+12*b+2)**2)
eq('k max',k.subs(a,1),S.Rational(91,250))
eq('k min',k.subs(a,a0),S.Rational(17021,50000))
eq('C corner',C.subs({a:1,b:b1}),S.Rational(19,52))
eq('C-k corner',(C-k).subs({a:1,b:b1}),S.Rational(9,6500))
eq('N_b exact',S.diff(N,b),270000*a**3+810000*a*a*b+680100*a*a+150300*a*b-3223328*a-4778184*b+6019943)
N_b_lower=6019943-3223328-4778184*b1
eq('N_b certified lower',N_b_lower,S.Rational(10399437,5))
eq('N_a at b1',S.diff(N,a).subs(b,b1),(7200000*a**3+31062000*a*a-43828840*a+9966907)/40)
N_a_lower=(7200000*a0**3+31062000*a0**2-43828840+9966907)/40
eq('N_a certified lower',N_a_lower,S.Rational(744132939681,25000000))
eq('N max corner',N.subs({a:1,b:b1}),-S.Rational(270189,200))
eq('f1 max corner',f1.subs({a:1,b:b1}),-S.Rational(27,20))
eq('f2 min corner',f2.subs({a:a0,b:b1}),S.Rational(1620741,2000000))
eq('f2 derivative a at corner',(S.diff(f2,a)).subs({a:a0,b:b1}),S.Rational(1513,100))
eq('f2 derivative b',S.diff(f2,b),1350*a-3156)

# Achieving legal policy, checked in the full four observable atoms.
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
        eq('attaining '+name+' signed atom '+str(i),left.subs(sel,simultaneous=True),right)

# 16 strictly positive labelled leaves; preserve BU source marker.
q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaf=[(branch,q2[branch]/4,q2[branch]*rat[branch][j]/4)
      for branch in q2 for j in (0,1) for hidden in (0,1)]
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
    return sum(abs(P.get(key,F(0))-Q.get(key,F(0))) for key in P.keys()|Q.keys())/2

params=[(F(481,500),F(3,20)),(F(97,100),F(3,20)),(F(99,100),F(3,20)),
        (F(1),F(3,20)),(F(481,500),F(149,1000)),
        (F(1),F(37,250)),(F(1),F(1,100))]
for aa,bb in params:
    GG=5*aa**2+8*aa*bb-21*bb**2-2*bb-5
    assert GG>=0 and F(0)<bb<=F(3,20) and F(0)<aa<=1
    dd=(1-aa)/3; BC=bb-dd; cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    ee=BC*cc/4; UU=BC*(1+cc)
    assert F(0)<BC<=1 and F(0)<cc<1 and F(0)<=UU<=1 and ee>=dd
    for law in ('P','Q'):
        target=observe(law,aa,bb,F(1),BC,cc,UU,BC,True)
        competitor=observe(law,aa,bb,F(1),BC,cc,UU,BC,False)
        actual=tv(target,competitor)
        assert actual==ee,(law,aa,bb,actual,ee)
    print('EXACT_16_LEAF_WITNESS a=',str(aa),' b=',str(bb),
          ' G=',str(GG),' u=',str(cc),' TV_P=TV_Q=',str(ee),sep='')
# Exact obstruction to this one-splice certificate at b=19/125 (> 3/20).
# q=17/50 simultaneously makes both dual gaps strictly negative.
aa,bb,qq=S.Rational(481,500),S.Rational(19,125),S.Rational(17,50)
eq('obstruction G',G.subs({a:aa,b:bb}),S.Rational(1957,250000))
eq('obstruction C',C.subs({a:aa,b:bb}),S.Rational(1423,3836))
eq('obstruction L0(q)-E',(L0(qq)-E).subs({a:aa,b:bb}),-S.Rational(1201,26971875))
eq('obstruction L3(q)-E',(L3(qq)-E).subs({a:aa,b:bb}),-S.Rational(38597,2841037500))
# dL3/du has denominator 2(2u-7)^2, and the numerator
#   a*(2u^2-14u+7)+b*(6u^2-42u)
# strictly decreases for 0<=u<=q and is still positive at q.
d3_num=a*(2*u*u-14*u+7)+b*(6*u*u-42*u)
eq('obstruction derivative numerator',d3_num.subs({a:aa,b:bb,u:qq}),S.Rational(195101,625000))
assert S.Rational(3,20)<bb and qq < C.subs({a:aa,b:bb})
print('EXACT_SINGLE_SPLICE_OBSTRUCTION a=481/500 b=19/125 q=17/50')
print('PASS_SYMBOLIC_IDENTITIES',len(checks))
print('PASS_EXACT_PQ_16_LEAF_CASES',len(params))
print('PASS_BRC_N4_BU_LINEAR_K_TO_B_THREE_TWENTIETHS_AUTHOR_ONLY')
