#!/usr/bin/env python3
"""R5 positive-residual Blackwell repair: exact Fraction regression checks.
The all-real argument is in RESEARCH.md; this checker verifies the identities
and a rational test family, not a numerical extrapolation.
"""
from fractions import Fraction as F
from itertools import product
r=(F(1,10), F(1,2), F(3,4), F(1), F(5,4), F(3,2), F(19,10))
Z=F(0); O=F(1); k=F(247,1620)

def masses(x):
    g,a,b,u,v,w,z=x
    c0=F(13,40)*a+b/80; c1=a/10+F(9,40)*b; c2=F(3,40)*a+F(21,80)*b
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        c0-u,(g-a)/2,
        1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,c2-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def legal(x):
    g,a,b,u,v,w,z=x
    return 0<=a<=g<=1 and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and \
        0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10 and 0<=v-z<=F(9,40)*b

def residual(x):
    _,a,b,_,v,_,z=x
    return 9*b*z-4*a*(v-z)

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
        1+g+(a+b)/2+u+v+w)

def seedless_target(x):
    g,a,b,u,v,w,z=x
    assert legal(x) and a>0 and b>0
    zs=4*a*v/(4*a+9*b)
    return (g,a,b,u,v,w,zs)

def transport(x):
    assert legal(x) and residual(x)>=0
    if residual(x)==0: return x,[[masses(x)[i] if i==j else Z for j in range(7)] for i in range(7)]
    y=seedless_target(x)
    h=k*(x[6]-y[6])
    assert h>0
    mx=masses(x); my=masses(y)
    Q=[[Z]*7 for _ in range(7)]
    for i in range(7): Q[i][i]=mx[i] if i in (0,6) else my[i]
    Q[0][3]=h;Q[6][3]=h
    return y,Q

def check(x):
    assert legal(x) and residual(x)>=0
    y,Q=transport(x); mx=masses(x);my=masses(y)
    assert legal(y) and residual(y)==0 and times(y)==times(x)
    assert sum(mx)==sum(my)==1
    assert sum(r[i]*mx[i] for i in range(7))==sum(r[i]*my[i] for i in range(7))==1
    assert all(q>=0 for row in Q for q in row)
    for i in range(7): assert sum(Q[i])==my[i]
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j]
        assert sum(r[i]*Q[i][j] for i in range(7))==r[j]*mx[j]
    for d in ((Z,)*7,(O,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),O)):
        mapped=tuple(sum(Q[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
        assert all(Z<=di<=O for di in mapped)
        assert sum(my[i]*mapped[i] for i in range(7))==sum(mx[j]*d[j] for j in range(7))
        assert sum(r[i]*my[i]*mapped[i] for i in range(7))==sum(r[j]*mx[j]*d[j] for j in range(7))
    return y

assert F(67,162)-F(47,180)==k
assert (F(43,90)-F(14,81))==2*k
assert r[0]+r[6]==2*r[3]
print('PASS_EXACT_AFFINE_MASS_AND_MARTINGALE_COEFFICIENTS')
count=0
for g,a,b in ((O,O,O),(O,F(3,4),F(1,2)),(O,F(4,5),F(1,4)),(F(4,5),F(2,5),F(3,5)),(O,F(1,3),F(2,3))):
    uc=F(13,40)*a+b/80; wc=F(3,40)*a+F(21,80)*b
    for zn,qn,p,wq in product((Z,F(1,4),F(1,2),O),repeat=4):
        z=zn*a/10; v=z+qn*F(9,40)*b
        x=(g,a,b,p*uc,v,wq*wc,z)
        if residual(x)>=0:
            check(x);count+=1
print('PASS_EXACT_POSITIVE_RATIONAL_CASES',count)
source=(O,F(3,4),F(1,2),F(1,4),F(3,40),F(3,16),F(3,40))
target=check(source)
assert residual(source)==F(27,80)
assert target==(O,F(3,4),F(1,2),F(1,4),F(3,40),F(3,16),F(3,100))
assert times(source)==(F(123,40),F(251,80))
assert k*(source[6]-target[6])==F(247,36000)
print('POSITIVE_WITNESS_SOURCE',','.join(map(str,source)))
print('POSITIVE_WITNESS_TARGET',','.join(map(str,target)))
print('TIMES',','.join(map(str,times(source))))
print('TRANSPORT_OFFDIAGONAL',F(247,36000))
# Exact limitation of the fixed-six-coordinate repair when residual < 0.
neg=(O,F(3,4),F(1,2),Z,F(9,80),Z,Z)
yn=seedless_target(neg)
assert residual(neg)<0 and legal(yn) and masses(yn)[0]<masses(neg)[0]
print('NEGATIVE_FIXED_SLICE_HINGE_OBSTRUCTION',masses(neg)[0]-masses(yn)[0])
print('PASS_R5_ALL_REAL_POSITIVE_RESIDUAL_TWO_EDGE_BLACKWELL_LIFT')
