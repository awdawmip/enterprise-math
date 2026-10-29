#!/usr/bin/env python3
"""Exact symbolic Farkas proof and full-16-leaf rational checks (author-side)."""
from fractions import Fraction as F
from collections import defaultdict
import sympy as s
u,A,B,U,V=s.symbols("u A B U V",real=True)
a,b=s.Rational(961,1000),s.Rational(151,1000)
P1=(a-A+3*(b-B))/4
Q1=(a-A+b-B)/2
P3=(A*u-a)/6+U/12+V/2
Q3=(A*u-a)/6+U/3+V/4
D4=B*u/4
DP=(P1,-P1-P3-D4,P3,D4)
DQ=(Q1,-Q1-Q3-D4,Q3,D4)
def event(law,mask):
    atoms=DP if law=="P" else DQ
    return s.expand(sum(atoms[i] for i in range(4) if mask>>i&1))
def cert(name,events,weights,mu,target):
    assert s.factor(sum(weights)-1)==0
    lhs=sum(w*event(l,m) for (l,m),w in zip(events,weights))-mu*(B-V)
    assert s.factor(lhs-target)==0
    print("PASS_SYMBOLIC",name,str(s.factor(target)))
J=(1730-2883*u-1414*u*u)/(2000*(23-2*u))
h=u*(961-1414*u)/(2000*(7-2*u))
K=151*u/(1000*(4+u))
cert("EARLY",[("P",10),("P",11),("Q",9),("Q",13)],
 [2*(u*u-2*u+7)/(23-2*u),2*(1+4*u-u*u)/(23-2*u),
 (3-7*u)/(23-2*u),(u+4)/(23-2*u)],7*(u+4)/(4*(23-2*u)),J)
cert("MIDDLE",[("P",8),("P",10),("P",11),("Q",12)],
 [7*(1-u)/(7-2*u),2*u*u/(7-2*u),2*u*(2-u)/(7-2*u),u/(7-2*u)],
 7*u/(4*(7-2*u)),h)
cert("LATE",[("P",8),("P",9),("Q",14)],
 [2*(2-u)/(u+4),2*u/(u+4),u/(u+4)],0,K)
u0=s.Rational(171,500)
p=1414*u*u+4091*u-1730
r=(s.sqrt(26521161)-4091)/2828
estar=s.sqrt(26521161)/15000-s.Rational(413,1250)
t=s.Rational(517,40000)
assert s.simplify(p.subs(u,r))==0
assert p.subs(u,u0)<0<p.subs(u,s.Rational(239,638))
assert s.factor(s.diff(J,u))==(2828*u*u-65044*u-62849)/(2000*(2*u-23)**2)
assert s.factor(s.diff(h,u,2))==6979/(125*(2*u-7)**3)
assert s.factor(s.diff(K,u))==604/(1000*(u+4)**2)
assert J.subs(u,u0)>t and h.subs(u,u0)>t
assert 26521161<s.Rational(5149875,1000)**2
assert s.simplify(h.subs(u,r)-estar)==0
assert s.simplify(K.subs(u,r)-estar)==0
As=(1414*u+1033)/(250*(7-2*u))
Bs=(961-1414*u)/(500*(7-2*u))
Us=(1+u)*Bs
sub={A:As,B:Bs,U:Us,V:Bs}
assert s.factor(P1.subs(sub))==0
assert s.factor(DP[1].subs(sub))==0
assert s.factor((P3+u*Bs/4).subs(sub))==0
assert s.factor(Q3.subs(sub))==0
assert s.factor((Q1+u*Bs/4).subs(sub))==s.factor(p/(2000*(2*u-7)))
assert s.factor(DQ[1].subs(sub))==s.factor(-p/(2000*(2*u-7)))
assert s.simplify((u*Bs/4).subs(u,r)-estar)==0
print("PASS_UNIVERSAL_MINIMAX_CERTIFICATE",str(estar))
q={"AU":F(1,6),"AV":F(1,3),"BU":F(1,4),"BV":F(1,4)}
lik={"AU":(F(9,10),F(11,10)),"AV":(F(1,4),F(1,4)),
     "BU":(F(1,5),F(9,5)),"BV":(F(2),F(2))}
leaves=[(c,j,k,q[c]/4,q[c]*lik[c][j]/4)
        for c in ("AU","AV","BU","BV") for j in range(2) for k in range(2)]
assert len(leaves)==16
assert all(x[3]>0 and x[4]>0 for x in leaves)
assert sum(x[3] for x in leaves)==sum(x[4] for x in leaves)==1
atoms=((1,"Q",0),(2,"Q",0),(3,"P",0),(3,"Q",1))
def obs(law,first,second):
    d=defaultdict(F)
    for c,j,k,Q,P in leaves:
        mass=P if law=="P" else Q
        x,y=first[c[0]],second[c]
        z=int(c=="BU")
        d[atoms[0]]+=mass*(1-x)
        d[atoms[1]]+=mass*x*(1-y)
        d[(3,"Q" if z else "P",z)]+=mass*x*y
    arr=tuple(d[v] for v in atoms)
    assert sum(arr)==1
    return arr
def tv(x,y):return sum(abs(v-w) for v,w in zip(x,y))/2
for name,v in (("NEAR_ROOT",F(18721181,50000000)),("STRICT",F(234,625))):
    aa=(1414*v+1033)/(250*(7-2*v))
    bb=(961-1414*v)/(500*(7-2*v))
    uu=(1+v)*bb
    assert 0<=v<=1 and 0<bb<=1 and 0<=uu<=aa<=1
    first={"A":aa,"B":bb}
    second={"AU":v,"AV":uu/aa,"BU":v,"BV":F(1)}
    target1={"A":F(961,1000),"B":F(151,1000)}
    target2={"AU":F(1),"AV":F(0),"BU":F(0),"BV":F(0)}
    for law in ("P","Q"):
        val=tv(obs(law,first,second),obs(law,target1,target2))
        assert val==v*bb/4
        if name=="NEAR_ROOT": assert val==F(201985162574423973,15627881900000000000)
        else: assert val==F(31560633,2441875000)
        print("PASS_FULL16",name,law,str(val))
print("PASS_BRC_N4_BU_COMMON_U_GLOBAL_MINIMAX_20261030")
