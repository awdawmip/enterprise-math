#!/usr/bin/env python3
"""Exact sharp F-face p threshold, frozen seven-node R5 law; no LP dependency."""
from fractions import Fraction as F
import VERIFY as base
P0=F(2741,3900)
T=F(1,13)
def src(p):
    return base.source(T,p,F(1),F(0),F(0))
def target0():
    g=F(1199,1300)
    return (g,F(0),g,F(0),F(9,40)*g,F(21,80)*g,F(0))
# The p=1 witness is the earlier full-axis high-p slab certificate.
def target1():
    return base.Y[0,1,1,0,0]
def residual_identity(p,y):
    g,a,b,u,v,w,z=y
    A=a
    B=g-b
    C=u
    D=F(3,40)*a+F(21,80)*b-w
    EP=base.tp(y)-base.tp(src(p))
    EQ=base.tq(y)-base.tq(src(p))
    EF1=z-a/10
    EF2=v-z-F(9,40)*b
    rhs=F(37,5)*A+F(82,15)*B+F(80,3)*C+F(236,15)*D+F(212,5)*EP-F(718,15)*EQ+F(82,15)*EF1+F(82,15)*EF2
    return p-P0-rhs

def main():
    # Both sides are affine in (p,g,a,b,u,v,w,z). These 9 basis evaluations
    # exhaustively verify the coefficient identity over the rational field.
    zero=(F(0),)*7
    assert residual_identity(F(0),zero)==0
    for j in range(7):
        basis=list(zero);basis[j]=F(1)
        assert residual_identity(F(0),basis)==0
    assert residual_identity(F(1),zero)==0
    print('PASS_EXACT_AFFINE_DUAL_IDENTITY_BASIS 9')
    y0=target0();y1=target1()
    base.verify(src(P0),y0)
    base.verify(src(F(1)),y1)
    print('PASS_EXACT_ENDPOINT_BLACKWELL_WITNESSES 2')
    print('PSTAR',P0,'TARGET',','.join(map(str,y0)))
    print('PSTAR_HINGE_SLACKS',','.join(str(base.hinge(y0,k)-base.hinge(src(P0),k)) for k in base.R[1:-1]))
    for j in range(201):
        s=F(j,200)
        p=(1-s)*P0+s
        y=tuple((1-s)*u+s*v for u,v in zip(y0,y1))
        base.verify(src(p),y)
    print('PASS_201_EXACT_INTERVAL_REGRESSIONS')
    print('THEOREM_SHARP_F_FACE_P_IF_AND_ONLY_IF_2741_OVER_3900_LE_P_LE_1')
if __name__=='__main__': main()
