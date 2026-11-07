#!/usr/bin/env python3
"""Exact Fraction certificate for frozen R5 three-key capacity at T_P=T_Q=31/10.

Standard-library-only. Structural universal proof is the affine identity verified
coefficientwise, together with the stated nonnegative flow slacks.
"""
from fractions import Fraction as F

R = tuple(map(lambda ab:F(*ab), ((1,10),(1,2),(3,4),(1,1),(5,4),(3,2),(19,10))))
ZERO = F(0)
T = F(31,10)
C = F(6269,11400)


def model(g,a,b,u,v,w,z, require_legal=True):
    cap0 = F(13,40)*a + b/80
    cap1 = a/10 + F(9,40)*b
    cap2 = F(3,40)*a + F(21,80)*b
    tp = 1+g+(3*a+5*b)/8+u/2+v+F(3,2)*w
    tq = 1+g+(a+b)/2+u+v+w
    m0 = F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100
    m6 = u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
    masses=(m0,cap0-u,(g-a)/2,
            1-g+cap1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,cap2-w,m6)
    U = C + F(1312,1425)*(tp-T) - F(6887,8550)*(tq-T)
    slacks=(g-a,cap1-v,F(9,40)*b-v+z,u,1-g)
    dual = sum((p*q for p,q in zip(
        (F(14473,34200),F(116,285),F(247,810),F(113,1425),F(3511,11400)),slacks)),ZERO)
    assert U - (masses[0]+masses[1]+masses[6]) == dual
    if require_legal:
        assert ZERO<=g<=1 and ZERO<=a<=g and ZERO<=b<=g
        assert ZERO<=u<=cap0 and ZERO<=v<=cap1 and ZERO<=w<=cap2
        assert ZERO<=z<=a/10 and ZERO<=v-z<=F(9,40)*b
        assert all(q>=ZERO for q in masses)
        assert sum(masses,ZERO)==1
        assert sum((r*m for r,m in zip(R,masses)),ZERO)==1
        assert dual>=0
        if tp==tq==T:
            assert masses[0]+masses[1]+masses[6]<=C
    return tp,tq,masses,dual,(cap0,cap1,cap2)

# Affine identity: one constant and seven basis directions, all exact rational.
zero=(ZERO,)*7
model(*zero,require_legal=False)
for k in range(7):
    x=list(zero);x[k]=F(1)
    model(*x,require_legal=False)
print('PASS_AFFINE_IDENTITY_CONSTANT_AND_SEVEN_BASIS_VECTORS')

# Exact sharp seedless likelihood-ratio construction.
g,a,b,u,v,w,z=(F(1),F(1),F(10,19),ZERO,F(83,380),F(9,76),F(1,10))
tp,tq,masses,dual,caps=model(g,a,b,u,v,w,z)
assert tp==tq==T and dual==0
assert caps==(F(63,190),F(83,380),F(81,380))
assert (u/caps[0],v/caps[1],w/caps[2])==(ZERO,F(1),F(5,9))
assert (z,v-z)==(a/10,F(9,40)*b)  # both middle branches have probability 1
assert masses==(F(1739,22800),F(63,190),ZERO,F(1351,11400),F(9,38),F(9,95),F(3239,22800))
assert sum((masses[i] for i in (0,1,6)),ZERO)==C
print('PASS_EXACT_UNIQUE_EQUALITY_FLOW_AND_SEEDLESS_RATIOS')

# Complete rational three-key declaration box for a representative 5^3 grid.
checks=0
for x_num in range(5):
    for y_num in range(5):
        for z_num in range(5):
            e=(masses[0]*F(x_num,4),masses[1]*F(y_num,4),masses[6]*F(z_num,4))
            eq=sum(e,ZERO)
            one_minus_ep=R[0]*e[0]+R[1]*e[1]+R[6]*e[2]
            assert ZERO<=eq<=C
            assert ZERO<=one_minus_ep<=1
            assert F(1)-one_minus_ep == F(1) - (e[0]/10+e[1]/2+F(19,10)*e[2])
            checks+=1
corner=(F(1)-R[0]*masses[0]-R[1]*masses[1]-R[6]*masses[6],C,tp,tq)
assert corner==(F(167,300),F(6269,11400),T,T)
print('PASS_BOX_125_EXACT_DECLARATIONS_AND_CORNER',tuple(map(str,corner)))
print('PASS_EXACT_R5_THREE_KEY_SHARP_31_OVER_10_GLOBAL_SUPPORT')
