#!/usr/bin/env python3
"""R5 six exact rational Blackwell certificates; source-native model, stdlib-only."""
from fractions import Fraction as F
from pathlib import Path
import json
Z,O=F(0),F(1)
r=tuple(map(F,("1/10","1/2","3/4","1","5/4","3/2","19/10")))

def mass(f):
    g,a,b,u,v,w,z=f; d=v-z
    return (F(509,900)*u+F(47,180)*z+F(67,162)*d+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*d,
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*d+F(509,900)*w)

def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def legal(f):
    g,a,b,u,v,w,z=f
    return (Z<=a<=g<=O and Z<=b<=g and
            Z<=u<=F(13,40)*a+b/80 and
            Z<=w<=F(3,40)*a+F(21,80)*b and
            Z<=z<=a/10 and Z<=v-z<=F(9,40)*b)

def source(eta,p,q,theta):
    u=(F(13,40)+eta/80)*p
    w=(F(3,40)+F(21,80)*eta)*q
    z=theta/10
    return (O,O,eta,u,F(9,40)*eta+z,w,z)

def check(x,y,Q):
    assert legal(x) and legal(y)
    assert 9*y[2]*y[6]-4*y[1]*(y[4]-y[6])==0
    assert times(x)==times(y)
    mx,my=mass(x),mass(y)
    assert sum(mx)==sum(my)==O
    assert sum(r[i]*mx[i] for i in range(7))==sum(r[i]*my[i] for i in range(7))==O
    for i in range(7):
        assert all(Q[i][j]>=0 for j in range(7))
        assert sum(Q[i])==my[i]
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j]
        assert sum(r[i]*Q[i][j] for i in range(7))==r[j]*mx[j]
    for d in ((Z,)*7,(O,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),O)):
        dp=tuple(sum(Q[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
        assert all(Z<=t<=O for t in dp)
        assert sum(my[i]*dp[i] for i in range(7))==sum(mx[i]*d[i] for i in range(7))
        assert sum(r[i]*my[i]*dp[i] for i in range(7))==sum(r[i]*mx[i]*d[i] for i in range(7))

n=0
for filename,face in (("THETA_SHARP_CORNERS.json","G"),("F_FACE_Q1_CERTIFICATES.json","F")):
    data=json.loads(Path(__file__).with_name(filename).read_text())
    for label,item in data.items():
        x=tuple(map(F,item["source"]))
        y=tuple(map(F,item["target"]))
        Q=[[Z]*7 for _ in range(7)]
        for i,j,value in item["edges"]:
            assert Q[i][j]==Z
            Q[i][j]=F(value)
        if face=="G":
            assert x==source(F(1,40),F(int(label[0])),F(int(label[1])),F(29,112))
            assert y[2]==Z and y[4]==y[6]
        else:
            eta=Z if label=="eta0" else F(1,40)
            assert x==source(eta,Z,O,Z)
            assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
        check(x,y,Q)
        n+=1
    print("PASS_"+face+"_FACE_NEW_ENDPOINT_CERTIFICATES")
assert n==6
for theta in (Z,F(1,4),F(29,112),F(3,10),O):
    x=source(F(1,40),Z,O,theta)
    tp,tq=times(x)
    assert 14+47*tq-54*tp==(29-112*theta)/160
print("PASS_SHARP_G_FACE_EXACT_DUAL_IDENTITY")
print("PASS_6_NEW_R5_BLACKWELL_RATIONAL_CERTIFICATES")
