#!/usr/bin/env python3
"""Executed release audit for the sharp BRC N4 BU global rho theorem.
Exact symbolic relations plus a strict 16-leaf rational competitor witness.
Continuum optimality is analytic (PROOF.md), not a finite-check inference.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

a,b,A,B,u,U,V,c=S.symbols('a b A B u U V c', real=True)
r=S.symbols('r',positive=True)
ss=(A-a+B-b)/2
st=(A-a+3*(B-b))/4
H=B*u/4
rq=a/6-A*u/6-U/3-V/4
rp=a/6-A*u/6-U/12-V/2
DQ=[ss,H-ss-rq,rq,-H]
DP=[st,H-st-rp,rp,-H]
w=(2-7*r)/(2+4*r)
e0=b*w/4
L0=lambda x:(4*a-14*b-3*a*x-(a+3*b)*x*x)/(2*(23-2*x))
L3=lambda x:x*(a-(a+3*b)*x)/(2*(7-2*x))
K=lambda x:b*x/(4+x)
checks=[]
def exact(label,got,want=0):
    assert S.factor(S.together(got-want))==0,label
    checks.append(label)
exact('L0_w',L0(w).subs(b,a*r),a*r*w/4)
exact('L3_w',L3(w).subs(b,a*r),a*r*w/4)
rc=(1-c)*(4+c)/(3*c*c+8*c+14)
wc=S.factor(w.subs(r,rc))
exact('c_minus_w',c-wc,c*(1-c)*(7-2*c)/(2*(c*c+2*c+22)))
exact('root_L3_K',L3(c)-K(c),-c*((a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a)/(2*(7-2*c)*(4+c)))
exact('sharp_factor',c*(1-c)/(3*c*c+8*c+14)-rc*wc/4,
      c*(c-1)*(5*c*c+73*c-28)/(8*(c*c+2*c+22)*(3*c*c+8*c+14)))
rho=(S.sqrt(5889)-25)/329
crit=(S.sqrt(5889)-73)/10
exact('rho_critical',rc.subs(c,crit),rho)
policy={A:a,B:b,u:w,U:b*(1+w),V:b}
for law,delta,goal in [('Q',DQ,[0,e0,0,-e0]),('P',DP,[0,0,e0,-e0])]:
    for i in range(4):
        exact(law+str(i),delta[i].subs(policy,simultaneous=True).subs(r,b/a),S.sympify(goal[i]).subs(r,b/a))
zero={A:a,B:b,u:0,U:2*a/7,V:2*a/7}
for law,delta in [('Q',DQ),('P',DP)]:
    for i in range(4): exact(law+'zero'+str(i),delta[i].subs(zero,simultaneous=True))

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
rat={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(k,q2[k]/4,q2[k]*rat[k][j]/4) for k in q2 for j in (0,1) for _ in (0,1)]
assert len(leaves)==16 and all(q>0 and p>0 for _,q,p in leaves)
assert sum(x[1] for x in leaves)==sum(x[2] for x in leaves)==1

def lawvec(law,aa,bb,AA,BB,cc,UU,VV,target):
    dist=defaultdict(F)
    for k,q,p in leaves:
        weight=q if law=='Q' else p
        v=(aa if k[0]=='A' else bb) if target else (AA if k[0]=='A' else BB)
        t=(F(1) if k=='AU' else F(0)) if target else {'AU':cc,'BU':cc,'AV':UU/AA,'BV':VV/BB}[k]
        assert 0<=v<=1 and 0<=t<=1
        dist[(1,'Q',0)]+=weight*(1-v)
        dist[(2,'Q',0)]+=weight*v*(1-t)
        dist[(3,'Q' if (k=='BU' and not target) else 'P',int(k=='BU'))]+=weight*v*t
    assert sum(dist.values())==1
    return dist

def tv(q,p):return sum(abs(q.get(k,0)-p.get(k,0)) for k in q.keys()|p.keys())/2

aa=F(1,2);bb=F(872,10793);cc=F(9,25)
rr=bb/aa
assert rr==F(1-cc)*(4+cc)/(3*cc*cc+8*cc+14)
ww=(2*aa-7*bb)/(2*aa+4*bb)
h=bb*cc/(4+cc);e=bb*ww/4
assert ww==F(4689,14281) and e==F(1022202,154134833)
assert h==F(72,10793) and h-e==F(6030,154134833)>0
for law in ['P','Q']:
    best=tv(lawvec(law,aa,bb,aa,bb,ww,bb*(1+ww),bb,True),
            lawvec(law,aa,bb,aa,bb,ww,bb*(1+ww),bb,False))
    root=tv(lawvec(law,aa,bb,aa+3*h,4*bb/(4+cc),cc,4*bb*(1+cc)/(4+cc),4*bb/(4+cc),True),
            lawvec(law,aa,bb,aa+3*h,4*bb/(4+cc),cc,4*bb*(1+cc)/(4+cc),4*bb/(4+cc),False))
    assert best==e and root==h
print('PASS_SYMBOLIC_IDENTITIES',len(checks))
print('PASS_EXACT_16_LEAF_STRICT_COUNTEREXAMPLE',str(h),str(e),str(h-e))
print('PASS_RELEASE_BRC_N4_BU_SHARP_RHO_GLOBAL_20261029')
