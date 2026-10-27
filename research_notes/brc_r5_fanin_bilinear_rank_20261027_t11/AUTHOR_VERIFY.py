#!/usr/bin/env python3
"""Exact 8-leaf fan-in P/Q observer verifier; all arithmetic Fraction."""
from fractions import Fraction as F
from itertools import product
Z=F(0); ONE=F(1)
q1={"A":F(1,2),"B":F(1,2)}
r1={"A":F(1,2),"B":F(3,2)}
q2={"A":{"U":F(1,3),"V":F(2,3)},"B":{"U":F(1,2),"V":F(1,2)}}
m2={"A":{"U":F(2),"V":F(1,2)},"B":{"U":F(2,3),"V":F(4,3)}}
rr={("A","U"):(F(1,4),F(7,4)),
    ("A","V"):(F(1,2),F(3,2)),
    ("B","U"):(F(1,2),F(3,2)),
    ("B","V"):(F(1,2),F(3,2))}
qleaf,pleaf={},{}
for h in ("A","B"):
    assert sum(q2[h].values(),Z)==ONE
    assert sum(q2[h][k]*m2[h][k] for k in ("U","V"))==ONE
    for k in ("U","V"):
        assert sum(rr[h,k],Z)/2==ONE
        for j in (0,1):
            key=(h,k,j)
            qleaf[key]=q1[h]*q2[h][k]/2
            pleaf[key]=qleaf[key]*r1[h]*m2[h][k]*rr[h,k][j]
            assert qleaf[key]>0 and pleaf[key]>0
assert len(qleaf)==8
assert sum(qleaf.values(),Z)==sum(pleaf.values(),Z)==ONE
assert r1["A"]*m2["A"]["U"]==r1["B"]*m2["B"]["U"]==ONE
assert rr["A","U"]!=rr["B","U"]
def obs(x,ya,yb):
    assert all(Z<=z<=ONE for z in (x,ya,yb))
    ep=eq=tp=tq=Z
    def add(keys,declare_q,time,prob):
        nonlocal ep,eq,tp,tq
        q=sum(qleaf[key] for key in keys)*prob
        p=sum(pleaf[key] for key in keys)*prob
        if declare_q: ep+=p
        else: eq+=q
        tp+=time*p; tq+=time*q
    for h in ("A","B"):
        hkeys=[(h,k,j) for k in ("U","V") for j in (0,1)]
        if h=="A":
            add(hkeys,False,1,ONE-x)
            cont=x
        else: cont=ONE
        add([(h,"V",j) for j in (0,1)],h=="A",2,cont)
        yy=ya if h=="A" else yb
        add([(h,"U",j) for j in (0,1)],False,2,cont*(ONE-yy))
        for j in (0,1):
            add([(h,"U",j)],j==0,3,cont*yy)
    return (ep,eq,tp,tq)
def plus(u,v): return tuple(a+b for a,b in zip(u,v))
def sub(u,v): return tuple(a-b for a,b in zip(u,v))
def mul(c,u): return tuple(c*a for a in u)
def dot(u,v): return sum((a*b for a,b in zip(u,v)),Z)
A=obs(Z,Z,Z)
B=sub(obs(ONE,Z,Z),A)
C=sub(obs(Z,Z,ONE),A)
D=sub(obs(ONE,ONE,Z),plus(A,B))
assert A==(Z,ONE,F(7,4),F(3,2))
assert B==(F(1,12),-F(1,3),F(1,4),F(1,2))
assert C==(F(1,16),-F(1,8),F(1,4),F(1,4))
assert D==(F(1,48),-F(1,12),F(1,6),F(1,6))
def aff(x,y,z): return plus(A,plus(mul(x,B),plus(mul(y,C),mul(z,D))))
samples=(Z,F(1,9),F(1,3),F(2,5),F(7,8),ONE)
for x,ya,yb in product(samples,repeat=3):
    assert obs(x,ya,yb)==aff(x,yb,x*ya)
for x,y in product(samples,repeat=2):
    assert obs(x,y,y)==aff(x,y,x*y)
def det3(t):
    return (t[0][0]*(t[1][1]*t[2][2]-t[1][2]*t[2][1])
           -t[0][1]*(t[1][0]*t[2][2]-t[1][2]*t[2][0])
           +t[0][2]*(t[1][0]*t[2][1]-t[1][1]*t[2][0]))
minor=det3([[B[i],C[i],D[i]] for i in range(3)])
assert minor==F(5,4608)
def xyz(O):
    dp,dq,dt=sub(O,A)[:3]
    return (-F(24,5)*dq-F(12,5)*dt,
            F(32)*dp+F(8)*dq,
            -F(48)*dp-F(24,5)*dq+F(48,5)*dt)
for x,ya,yb in product(samples,repeat=3):
    O=obs(x,ya,yb)
    assert xyz(O)==(x,yb,x*ya)
    dp,dq,dt,dT=sub(O,A)
    assert dT+F(6,5)*dq-F(2,5)*dt==Z
v00,v10,v01,v11=obs(Z,Z,Z),obs(ONE,Z,Z),obs(Z,Z,ONE),obs(ONE,ONE,ONE)
T=mul(F(1,3),plus(v00,plus(v10,v01)))
assert T==(F(7,144),F(61,72),F(23,12),F(7,4))
assert obs(F(1,3),Z,F(1,3))==T
assert xyz(T)==(F(1,3),F(1,3),Z)
assert xyz(T)[2]!=xyz(T)[0]*xyz(T)[1]
lam=(F(-80),F(-8),F(12),Z)
assert (dot(lam,B),dot(lam,C),dot(lam,D))==(-ONE,-ONE,ONE)
assert dot(lam,A)==F(13)
assert dot(lam,obs(ONE,Z,ONE))==F(11)
assert min(dot(lam,v) for v in (v00,v10,v01,v11))==F(12)
print("MODEL: 8 positive leaf pairs; Q total=1 P total=1; AU and BU LR=1")
print("A",A);print("B",B);print("C",C);print("D",D)
print("RANK_MINOR",minor)
print("CORNER_00",v00);print("CORNER_10",v10)
print("CORNER_01",v01);print("CORNER_11",v11)
print("FULL_BARYCENTER",T)
print("INVERSE_XYZ",xyz(T),"LR_PRODUCT_REQUIRED",F(1,9))
print("SLICE_SUPPORT_LAMBDA",lam,"LR_MIN",F(12),"FULL_MIN",F(11),"GAP",ONE)
print("CHECKED 216 full coefficient identities and 36 seedless LR identities over exact rational samples")
print("ALL EXACT CHECKS PASSED")
