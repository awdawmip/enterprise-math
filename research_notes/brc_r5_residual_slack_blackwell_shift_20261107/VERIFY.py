#!/usr/bin/env python3
"""Exact finite checks for the all-real R5 residual-neutralizing spread lemma.
The accompanying proof uses affine identities, so samples are regressions, not universal certification.
"""
from fractions import Fraction as F
from itertools import product
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
Z=F(0); ONE=F(1)
def masses(x):
    g,a,b,u,v,w,z=x
    c0=F(13,40)*a+b/80
    c1=a/10+F(9,40)*b
    c2=F(3,40)*a+F(21,80)*b
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            c0-u,(g-a)/2,
            1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,c2-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def legal(x):
    g,a,b,u,v,w,z=x
    return (0<=a<=g<=1 and 0<=b<=g and
            0<=u<=F(13,40)*a+b/80 and
            0<=w<=F(3,40)*a+F(21,80)*b and
            0<=z<=a/10 and 0<=v-z<=F(9,40)*b)
def residual(x):
    _,a,b,_,v,_,z=x
    return 9*b*z-4*a*(v-z)
def seedless(x):return residual(x)==0

def shift(x):
    g,a,b,u,v,w,z=x
    assert legal(x) and b>0 and residual(x)<=0
    d=-residual(x)/(9*b)
    assert g-d>=max(a,b)
    assert z+d<=a/10
    y=(g-d,a,b,u,v+d,w,z+d)
    assert legal(y) and seedless(y)
    return y,d

def Q_matrix(x,y,d):
    mx=masses(x);my=masses(y)
    Q=[[Z for _ in range(7)] for _ in range(7)]
    for i in range(7):Q[i][i]=my[i] if i in (2,4) else mx[i]
    Q[0][2]=d/5;Q[0][4]=F(11,180)*d
    Q[3][2]=F(43,180)*d;Q[3][4]=F(43,180)*d
    Q[6][2]=F(11,180)*d;Q[6][4]=d/5
    return Q

def check(x,y,d,Q):
    mx,my=masses(x),masses(y)
    assert legal(x) and legal(y) and seedless(y)
    assert times(x)==times(y)
    assert sum(mx)==sum(my)==1
    assert sum(R[i]*mx[i] for i in range(7))==1
    assert sum(R[i]*my[i] for i in range(7))==1
    assert tuple(my[i]-mx[i] for i in range(7))==(F(47,180)*d,Z,-d/2,F(43,90)*d,-d/2,Z,F(47,180)*d)
    assert all(v>=0 for row in Q for v in row)
    for i in range(7):assert sum(Q[i])==my[i]
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j]
        assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j]
    for dvec in ((Z,)*7,(ONE,)*7,(F(1,7),F(2,7),F(3,7),F(4,7),F(5,7),F(6,7),ONE)):
        mapped=[sum(Q[i][j]*dvec[j] for j in range(7))/my[i] if my[i]>0 else Z for i in range(7)]
        assert all(Z<=di<=ONE for di in mapped)
        assert sum(my[i]*mapped[i] for i in range(7))==sum(mx[j]*dvec[j] for j in range(7))
        assert sum(R[i]*my[i]*mapped[i] for i in range(7))==sum(R[j]*mx[j]*dvec[j] for j in range(7))

assert F(1,5)+F(11,180)==F(47,180)
assert 2*F(43,180)==F(43,90)
assert F(1,10)*F(1,5)+F(43,180)+F(19,10)*F(11,180)==F(3,4)/2
assert F(1,10)*F(11,180)+F(43,180)+F(19,10)*F(1,5)==F(5,4)/2
print('PASS_SYMBOLIC_DELTA_M_AND_SIX_EDGE_MARTINGALE_COEFFICIENTS')

a,b=F(3,4),F(1,2)
ucap=F(13,40)*a+b/80;wcap=F(3,40)*a+F(21,80)*b
for p,q in product((Z,ONE),repeat=2):
    x=(ONE,a,b,p*ucap,F(9,40)*b,q*wcap,Z)
    y,d=shift(x);check(x,y,d,Q_matrix(x,y,d))
    assert d==F(3,40) and y[0]==F(37,40)
    print('SATURATED_CORNER',str(p),str(q),'TP_TQ',*(str(v) for v in times(x)),'PASS')

count=0
for g,a,b in ((F(1),F(1,2),F(1,3)),(ONE,F(3,4),F(1,2)),(F(4,5),F(2,5),F(3,5)),(ONE,F(1,3),F(2,3)),(ONE,F(4,5),F(1,4))):
    for t,zeta,pu,pw in product((Z,F(1,3),F(2,3),ONE),(Z,F(1,2),ONE),(Z,F(1,2),ONE),(Z,F(1,2),ONE)):
        z=zeta*a*t/10
        gap=F(9,40)*b*t
        x=(g,a,b,pu*(F(13,40)*a+b/80),z+gap,pw*(F(3,40)*a+F(21,80)*b),z)
        if not legal(x):continue
        d=(a*t/10)-z
        if g-d<max(a,b):continue
        y,d1=shift(x)
        assert d1==d
        check(x,y,d1,Q_matrix(x,y,d1))
        count+=1
print('PASS_GENERAL_NEGATIVE_RESIDUAL_RATIONAL_CASES',count)

x=(ONE,F(3,4),F(1,2),F(1,4),F(9,80),F(3,16),Z)
y,d=shift(x);check(x,y,d,Q_matrix(x,y,d))
print('STRICT_NEW_SOURCE',','.join(map(str,x)))
print('SEEDLESS_TARGET',','.join(map(str,y)))
print('MATCHED_TIMES',','.join(map(str,times(x))))
print('RESIDUAL',str(residual(x)),'SHIFT',str(d))
print('PASS_R5_ALL_REAL_NEGATIVE_RESIDUAL_SLACK_BLACKWELL_LIFT')
