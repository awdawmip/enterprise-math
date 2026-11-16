#!/usr/bin/env python3
"""Exact seven-key Blackwell lifts on the symmetric high-v slab; real theorem from affine proof."""
from fractions import Fraction as F
from itertools import product
Z=F(0); O=F(1)
R=(F(1,10),F(1,2),F(3,4),O,F(5,4),F(3,2),F(19,10))
k=F(247,1620)
def diag(m):return [[m[i] if i==j else Z for j in range(7)] for i in range(7)]
def matadd(A,B):return [[A[i][j]+B[i][j] for j in range(7)] for i in range(7)]
def matscale(k,A):return [[k*A[i][j] for j in range(7)] for i in range(7)]
def masses(x):
    g,a,b,u,v,w,z=x
    c0=F(13,40)*a+b/80
    c1=a/10+F(9,40)*b
    c2=F(3,40)*a+F(21,80)*b
    return (
        F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        c0-u,(g-a)/2,
        1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,c2-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def residual(x):
    g,a,b,u,v,w,z=x
    return 9*b*z-4*a*(v-z)
def legal(x):
    g,a,b,u,v,w,z=x
    return (0<=a<=g<=1 and 0<=b<=g<=1 and
            0<=u<=F(13,40)*a+b/80 and
            0<=w<=F(3,40)*a+F(21,80)*b and
            0<=z<=a/10 and 0<=v-z<=F(9,40)*b)
def xflow(g,s,z):return (g,s,s,Z,F(9,40)*s,Z,z)
def midflow(g,s):return (g,s,s,Z,F(9,40)*s,Z,F(9,130)*s)
def lowseed(g,s):return (g,F(19,20)*s,F(19,20)*s,Z,F(11,40)*s,Z,F(11,130)*s)
def observe(x,d):
    m=masses(x)
    return (1-sum(R[i]*m[i]*d[i] for i in range(7)),
            sum(m[i]*d[i] for i in range(7)),*times(x))
X1=xflow(O,O,Z);Y1=lowseed(O,O)
MX,MY=masses(X1),masses(Y1)
K1=[[Z]*7 for _ in range(7)]
K1[0][0]=F(335,363);K1[0][1]=F(405,6292);K1[0][3]=F(241,18876)
K1[1][1]=O;K1[2][1]=F(27,65);K1[2][3]=F(38,65)
K1[3][3]=O;K1[4][3]=F(38,65);K1[4][5]=F(27,65)
K1[5][5]=O;K1[6][3]=F(241,18876);K1[6][5]=F(405,6292);K1[6][6]=F(335,363)
Q1=[[MY[i]*K1[i][j] for j in range(7)] for i in range(7)]
E0=masses(xflow(Z,Z,Z))
E1=masses(xflow(O,Z,Z))
assert E0==(Z,Z,Z,O,Z,Z,Z)
assert E1==(Z,Z,F(1,2),Z,F(1,2),Z,Z)
assert MX==(F(67,720),F(27,80),Z,F(5,36),Z,F(27,80),F(67,720))
assert MY==(F(121,1200),F(513,1600),F(1,40),F(257,2400),F(1,40),F(513,1600),F(121,1200))
def check_transport(x,y,Q):
    assert legal(x) and legal(y) and residual(y)==0
    assert times(x)==times(y)
    mx,my=masses(x),masses(y)
    assert all(v>=0 for row in Q for v in row)
    assert sum(mx)==sum(my)==O
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==O
    for i in range(7):assert sum(Q[i])==my[i],('row',i)
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j],('Q col',j)
        assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j],('P col',j)
    K=[[Q[i][j]/my[i] if my[i] else (O if i==j else Z) for j in range(7)] for i in range(7)]
    assert all(sum(row)==O and all(Z<=q<=O for q in row) for row in K)
    return K
check_transport(X1,Y1,Q1)
print('CORNERS_EXACT_SEVEN_KEY_CERTIFICATE PASS')
def negative_lift(g,s,z):
    t=Z if s==0 else F(130,9)*z/s
    assert 0<=t<=1 and 0<=s<=g<=1
    x=xflow(g,s,z)
    y0=lowseed(g,s);ym=midflow(g,s)
    y=(g,s*(19+t)/20,s*(19+t)/20,Z,s*(11-2*t)/40,Z,s*(11-2*t)/130)
    assert y==tuple((1-t)*y0[i]+t*ym[i] for i in range(7))
    Qlow=matadd(matadd(matscale(1-g,diag(E0)),matscale(g-s,diag(E1))),matscale(s,Q1))
    Q=matadd(matscale(1-t,Qlow),matscale(t,diag(masses(ym))))
    return x,y,Q,t
def positive_lift(g,s,z):
    assert 0<=s<=g<=1 and F(9,130)*s<=z<=s/10
    x=xflow(g,s,z);y=midflow(g,s)
    my=masses(y)
    delta=k*(z-F(9,130)*s)
    Q=diag(my)
    for i in (0,6):
        Q[i][i]-=delta
        Q[i][3]+=delta
    return x,y,Q,delta
for g in (Z,F(1,3),F(4,5),O):
    for frac in (Z,F(1,2),O):
        s=g*frac
        for t in (Z,F(1,3),F(2,3),O):
            x,y,Q,_=negative_lift(g,s,F(9,130)*s*t)
            check_transport(x,y,Q)
        for t in (Z,F(1,3),F(2,3),O):
            z=F(9,130)*s+(s/10-F(9,130)*s)*t
            x,y,Q,_=positive_lift(g,s,z)
            check_transport(x,y,Q)
print('EXACT_PARAMETRIC_96_CASES PASS')
g,s,t=F(4,5),F(1,2),F(1,3)
x,y,Q,_=negative_lift(g,s,F(9,130)*s*t)
K=check_transport(x,y,Q)
assert residual(x)==-F(3,20)
assert times(x)==(F(193,80),F(193,80))
assert y==(F(4,5),F(29,60),F(29,60),Z,F(31,240),Z,F(31,780))
for ds in product((Z,O),repeat=7):
    nd=tuple(sum(K[i][j]*ds[j] for j in range(7)) for i in range(7))
    assert all(Z<=q<=O for q in nd)
    assert observe(x,ds)==observe(y,nd)
print('INTERIOR_R',residual(x),'TIMES',times(x),'SEEDLESS',y)
print('EXACT_128_DECLARATIONS PASS')
x,y,Q,delta=positive_lift(F(4,5),F(1,2),F(1,20))
check_transport(x,y,Q)
assert residual(x)==F(1,10) and delta==F(19,8100)
print('POSITIVE_R',residual(x),'DELTA',delta)
print('PASS_R5_SYMMETRIC_HIGH_V_ALL_Z_SEVEN_KEY_BLACKWELL_SLAB')
