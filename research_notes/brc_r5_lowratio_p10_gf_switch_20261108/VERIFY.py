#!/usr/bin/env python3
"""Exact rational verifier of the R5 low-ratio p=1,q=0 G/F face-switch lift.
Requires Python >=3.9; standard library only. No floating-point inference."""
import json
from fractions import Fraction as F
from pathlib import Path
C = json.loads((Path(__file__).parent / "CERTIFICATES.json").read_text(encoding="utf-8"))["certificates"]
r = tuple(map(F, ("1/10","1/2","3/4","1","5/4","3/2","19/10")))
E0=(F(0),)*7
E1=(F(1),)+(F(0),)*6
def lin(t,x,y): return tuple((1-t)*a+t*b for a,b in zip(x,y))
def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u,(g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def lawful(x):
    g,a,b,u,v,w,z=x
    return (0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80
        and 0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10
        and 0<=v-z<=F(9,40)*b)
def seedless(x):
    g,a,b,u,v,w,z=x
    return lawful(x) and 9*b*z==4*a*(v-z)
def source(eta,theta):
    u=F(13,40)+eta/80
    z=theta/10
    return (F(1),F(1),eta,u,F(9,40)*eta+z,F(0),z)
def diag(x):
    m=mass(x)
    return tuple(tuple(m[i] if i==j else F(0) for j in range(7)) for i in range(7))
def mixq(t,q0,q1):
    return tuple(tuple((1-t)*q0[i][j]+t*q1[i][j] for j in range(7)) for i in range(7))
def matrix(key):
    q=[[F(0)]*7 for _ in range(7)]
    for i,j,v in C[key]["edges"]:
        assert q[i][j]==0
        q[i][j]=F(v)
    return tuple(tuple(row) for row in q)
def anchor(key):
    return (source(F(1,40),F(C[key]["theta"])),
            tuple(map(F,C[key]["y"])),matrix(key))
def check(x,y,q):
    assert lawful(x) and seedless(y) and times(x)==times(y)
    mx,my=mass(x),mass(y)
    assert sum(mx)==sum(my)==1
    assert all(z>=0 for row in q for z in row)
    for i in range(7): assert sum(q[i])==my[i]
    for j in range(7):
        assert sum(q[i][j] for i in range(7))==mx[j]
        assert sum(r[i]*q[i][j] for i in range(7))==r[j]*mx[j]
    for d in (tuple(F(j,8) for j in range(1,8)),tuple(F(j%2) for j in range(7))):
        mapped=tuple(sum(q[i][j]*d[j] for j in range(7))/my[i] if my[i] else F(0) for i in range(7))
        assert all(0<=v<=1 for v in mapped)
        assert sum(my[i]*mapped[i] for i in range(7))==sum(mx[j]*d[j] for j in range(7))
        assert sum(r[i]*my[i]*mapped[i] for i in range(7))==sum(r[j]*mx[j]*d[j] for j in range(7))
def base(theta):
    assert 0<=theta<=1
    if theta<=F(3,4):
        t=F(4,3)*theta
        _,y0,q0=anchor("G0")
        _,y1,q1=anchor("G34")
        y,q=lin(t,y0,y1),mixq(t,q0,q1)
        assert y[2]==0 and y[4]==y[6]
    else:
        t=3*theta-2
        _,y0,q0=anchor("F23")
        y,q=lin(t,y0,source(F(1,40),F(1))),mixq(t,q0,diag(source(F(1,40),F(1))))
        assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    return source(F(1,40),theta),y,q
def low_eta(eta,theta):
    assert 0<=eta<=F(1,40) and 0<=theta<=F(3,4)
    x1,y1,q1=base(theta)
    x0=source(F(0),theta)
    k=40*eta
    x,y,q=lin(k,x0,x1),lin(k,x0,y1),mixq(k,diag(x0),q1)
    assert x==source(eta,theta) and y[2]==0 and y[4]==y[6]
    return x,y,q
def scaled(g,s,theta,h,eta=None):
    assert 0<=s<=g<=1 and 0<=h<=1
    x,y,q=base(theta) if eta is None else low_eta(eta,theta)
    w=(1-g,g-s,s)
    xx=tuple(sum(w[k]*z[k] for k in range(3)) for z in zip(E0,E1,x))
    yy=tuple(sum(w[k]*z[k] for k in range(3)) for z in zip(E0,E1,y))
    Qs=(diag(E0),diag(E1),q)
    qq=tuple(tuple(sum(w[k]*Qs[k][i][j] for k in range(3)) for j in range(7)) for i in range(7))
    return lin(h,xx,yy),yy,mixq(h,qq,diag(yy))
def main():
    for key in ("G0","G34","F23"):
        check(*anchor(key))
        print("ANCHOR_PASS",key,len(C[key]["edges"]))
    count=0
    for g,s in ((F(0),F(0)),(F(1,2),F(0)),(F(1,2),F(1,4)),(F(1),F(1))):
        for theta in map(F,("0","1/4","1/2","2/3","3/4","7/8","1")):
            for h in map(F,("0","1/3","1")):
                check(*scaled(g,s,theta,h));count+=1
    print("SCALED_FULL_THETA_PASS",count)
    count=0
    for eta in map(F,("0","1/160","1/80","1/40")):
        for g,s in ((F(0),F(0)),(F(3,4),F(1,2)),(F(1),F(1))):
            for theta in map(F,("0","1/4","2/3","3/4")):
                for h in map(F,("0","1/2","1")):
                    check(*scaled(g,s,theta,h,eta));count+=1
    print("LOW_ETA_G_PRISM_PASS",count)
    print("PASS_R5_P10_GF_FACE_SWITCH_ALL_REAL_PROOF_BY_NONNEGATIVE_INTERPOLATION")
if __name__=="__main__": main()
