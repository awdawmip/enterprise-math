#!/usr/bin/env python3
"""Exact 2D bridge-corridor verification (author-side; not a universal finite-grid proof)."""
from fractions import Fraction as F
from collections import defaultdict
import sympy as S

a,b,c,A,B,u,U,V=S.symbols('a b c A B u U V',real=True)
d=(1-a)/3
Bstar=b-d
w=(7-a-21*b)/(4*a+12*b+2)
E=S.factor(Bstar*w/4)
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*u/4
rQ=a/6-A*u/6-U/3-V/4
rP=a/6-A*u/6-U/12-V/2
DQ=(s,H-s-rQ,rQ,-H)
DP=(t,H-t-rP,rP,-H)
L0=lambda x:(4*a-14*b-3*a*x-(a+3*b)*x*x)/(2*(23-2*x))
L3=lambda x:x*(a-(a+3*b)*x)/(2*(7-2*x))
checks=[]
def eq(label,expr,expected=0):
    diff=S.factor(S.cancel(expr-expected))
    assert diff==0,(label,diff)
    checks.append(label)
eq('L3(w)=E',L3(w),E)
eq('L0(3/7)-E',L0(S.Rational(3,7))-E,
   (131*a*a+576*a*b-232*a+549*b*b-1746*b+245)/(840*(2*a+6*b+1)))
eq('L3(3/7)-E',L3(S.Rational(3,7))-E,
   (19*a+183*b-43)*(31*a+93*b-49)/(7224*(2*a+6*b+1)))
eq('w>=3/7 condition', w-S.Rational(3,7),
   (43-19*a-183*b)/(7*(4*a+12*b+2)))
eq('t bound', t-(S.Integer(1)-a+3*(B-b))/4,(A-1)/4)
eq('middle two P',DP[1]+DP[2],H-t)
eq('first three P',sum(DP[:3]),H)
sub={A:1,B:Bstar,u:w,U:Bstar*(1+w),V:Bstar}
for law,actual,want in [('Q',DQ,(d,E-d,0,-E)),('P',DP,(0,0,E,-E))]:
    for j in range(4):eq(f'candidate-{law}-{j}',actual[j].subs(sub, simultaneous=True),want[j])
N0=131*a*a+576*a*b-232*a+549*b*b-1746*b+245
eq('N0 min corner',N0.subs({a:S.Rational(99,100),b:S.Rational(13,100)}),S.Rational(89,625))
eq('N0 derivative a',S.diff(N0,a),262*a+576*b-232)
eq('N0 derivative b',S.diff(N0,b),576*a+1098*b-1746)

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
     'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaf=[(k,q2[k]/4,q2[k]*rat[k][j]/4) for k in q2 for j in (0,1) for z in (0,1)]
assert len(leaf)==16 and all(q>0 and p>0 for k,q,p in leaf)
assert sum(q for k,q,p in leaf)==sum(p for k,q,p in leaf)==1

def vec(law,aa,bb,AA,BB,cc,UU,VV,target):
    out=defaultdict(F)
    for k,q,p in leaf:
        mass=q if law=='Q' else p
        one=(aa if k[0]=='A' else bb) if target else (AA if k[0]=='A' else BB)
        two=(F(1) if k=='AU' else F(0)) if target else {'AU':cc,'BU':cc,'AV':UU/AA,'BV':VV/BB}[k]
        assert 0<=one<=1 and 0<=two<=1
        out[(1,'Q',0)]+=mass*(1-one)
        out[(2,'Q',0)]+=mass*one*(1-two)
        out[(3,'Q' if (k=='BU' and not target) else 'P',int(k=='BU'))]+=mass*one*two
    assert sum(out.values())==1
    return out

def tv(x,y):return sum(abs(x.get(k,0)-y.get(k,0)) for k in x.keys()|y.keys())/2

params=[(F(99,100),F(1,10)),(F(99,100),F(13,100)),(F(1),F(1,10)),
        (F(1),F(13,100)),(F(199,200),F(3,25)),(F(999,1000),F(1,8))]
for aa,bb in params:
    dd=(1-aa)/3; BB=bb-dd; cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    AA=F(1);UU=BB*(1+cc);VV=BB;EE=BB*cc/4
    assert 0<BB<1 and F(3,7)<=cc<1 and UU<=AA and VV<=BB and EE>=dd
    for law in 'PQ':
        target=vec(law,aa,bb,AA,BB,cc,UU,VV,True)
        competitor=vec(law,aa,bb,AA,BB,cc,UU,VV,False)
        assert tv(target,competitor)==EE
    print('WITNESS',str(aa),str(bb),'c',str(cc),'TV_P=TV_Q',str(EE))
print('PASS_SYMBOLIC_RELATIONS',len(checks))
print('PASS_16_LEAF_PQ_SIX_RATIONAL_WITNESSES')
print('PASS_BRC_N4_BU_CAPACITY_2D_A099_TO_1_BRIDGE')
