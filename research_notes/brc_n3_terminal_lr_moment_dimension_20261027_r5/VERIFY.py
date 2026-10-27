#!/usr/bin/env python3
"""Exact rational finite checks for the terminal LR moment-dimension note."""
from fractions import Fraction as F

def moment(k,y,n):
    return sum((a*b**n for a,b in zip(k,y)),F(0))
def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2
def check(k,y,r):
    assert all(p>0 for p in k)
    assert moment(k,y,0)==1 and moment(k,y,1)==r

y2=(F(1,2),F(3,2))
assert (y2[1]-1)/(y2[1]-y2[0])==F(1,2)
print("TWO_POINT_UNIQUENESS_PASS")

y3=(F(1,2),F(1),F(3,2))
a3=(F(1,4),F(1,2),F(1,4))
b3=(F(1,3),F(1,3),F(1,3))
for k in (a3,b3): check(k,y3,F(1))
v3=[moment(k,y3,2)-1 for k in (a3,b3)]
assert v3==[F(1,8),F(1,6)]
assert tv(a3,b3)==abs(v3[1]-v3[0])/((y3[1]-y3[0])*(y3[2]-y3[1]))==F(1,6)
print("TERNARY_VARIANCE_TV_PASS: variance=1/8,1/6; TV=1/6")

y4=(F(1,2),F(3,4),F(5,4),F(3,2))
ka=(F(3,16),F(6,16),F(2,16),F(5,16))
kb=(F(5,16),F(2,16),F(6,16),F(3,16))
for k in (ka,kb):check(k,y4,F(1))
assert [moment(ka,y4,i)-moment(kb,y4,i) for i in range(4)]==[0,0,0,F(3,128)]
assert moment(ka,y4,2)==moment(kb,y4,2)==F(37,32)
assert moment(ka,y4,3)==F(379,256) and moment(kb,y4,3)==F(373,256)
assert tv(ka,kb)==F(3,8)
print("QUATERNARY_VARIANCE_BLIND_PASS: E[Y^2]=37/32; third-moment gap=3/128; TV=3/8")

root={"a":(F(1,3),F(2,3)),"b":(F(2,3),F(1,3))}
level2={"a":{"x":(F(1,2),F(1,4)),"y":(F(1,2),F(3,4))},
        "b":{"x":(F(2,3),F(1,3)),"y":(F(1,3),F(2,3))}}
third={}
for h,k in (("ax",ka),("by",kb)):
    third[h]=tuple((p,p*y) for p,y in zip(k,y4))
for h in ("ay","bx"):
    third[h]=((F(1,2),F(1,2)),(F(1,2),F(1,2)))
leaves=[]
parents={}
for a,(q1,p1) in root.items():
    for b,(q2,p2) in level2[a].items():
        h=a+b
        parents[h]=(q1*q2,p1*p2)
        assert sum(q for q,p in third[h])==sum(p for q,p in third[h])==1
        for q3,p3 in third[h]:
            leaves.append((h,q1*q2*q3,p1*p2*p3))
assert len(leaves)==12 and all(q>0 and p>0 for h,q,p in leaves)
assert sum(q for h,q,p in leaves)==sum(p for h,q,p in leaves)==1
for h,q,p in leaves:
    assert p/q in (set(y4) if h in ("ax","by") else {parents[h][1]/parents[h][0]})
assert parents["ax"]==(F(1,6),F(1,6)) and parents["by"]==(F(2,9),F(2,9))
minor=parents["ax"][0]*parents["by"][0]*(kb[0]-ka[0])
assert minor==F(1,216)
print("TWELVE_LEAF_STRICTLY_POSITIVE_TREE_PASS")
print("RANK_MINOR_PASS: 1/216")
print("CLAIM_SCOPE: exact finite witness checked, universal claims depend on algebraic proof")
