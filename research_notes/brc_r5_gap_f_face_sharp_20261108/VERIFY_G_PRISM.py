#!/usr/bin/env python3
"""Explicit positive-residual-capable G-face five-parameter R5 prism; Fraction.
Reuses the exact frozen seven-node calibration from sibling VERIFY.py.
"""
from fractions import Fraction as F
from itertools import product
import VERIFY as base
T0,T1=F(3,20),F(7,39)
P1=F(303,2450)
Q0=F(3,20)
K1=F(7,20)

def explicit_target(t,p,q,theta,kappa):
    x=base.source(t,p,q,theta,kappa)
    U=F(1,80)
    return (F(1),F(0),F(1),U,
            F(3,4)*t+2*x[3]+x[4]-2*U,
            U+x[5]-x[3]-t/4,F(0))

def check(t,p,q,theta,kappa):
    x=base.source(t,p,q,theta,kappa)
    y=explicit_target(t,p,q,theta,kappa)
    base.lawful(x);base.lawful(y)
    assert y[1]==y[6]==0
    assert base.tp(x)==base.tp(y) and base.tq(x)==base.tq(y)
    margins=[base.hinge(y,r)-base.hinge(x,r) for r in base.R[1:-1]]
    assert all(z>=0 for z in margins)
    return margins

def main():
    minima=[None]*5
    for t,p,q,theta,kappa in product((T0,T1),(F(0),P1),(Q0,F(1)),(F(0),F(1)),(F(0),K1)):
        margins=check(t,p,q,theta,kappa)
        minima=[z if old is None or z<old else old for old,z in zip(minima,margins)]
    assert all(z>=0 for z in minima)
    print('PASS_EXACT_G_32_CORNERS',32)
    print('MIN_HINGE_GAP_FIVE',','.join(map(str,minima)))
    for j in range(251):
        t=T0+(T1-T0)*F((31*j+7)%251,251)
        p=P1*F((19*j+5)%251,251)
        q=Q0+(F(1)-Q0)*F((23*j+13)%251,251)
        theta=F((29*j+17)%251,251)
        kappa=K1*F((37*j+11)%251,251)
        check(t,p,q,theta,kappa)
    print('PASS_EXACT_G_251_INTERIOR_REGRESSIONS')
    print('THEOREM_ALL_REAL_G_FACE_T_3_20_TO_7_39_P_0_TO_303_2450_Q_3_20_TO_1_KAPPA_0_TO_7_20')
if __name__=='__main__': main()
