#!/usr/bin/env python3
"""Exact checker for the longitudinal/transverse readout conic."""

from __future__ import annotations

from fractions import Fraction


def check_rational(s: int, a: int) -> None:
    assert s % 2 == 1 and s > 0 and a != 0
    A=Fraction(a,1)
    S=Fraction(s,1)
    b=-Fraction(1,s*a)
    J=S*(b-2*A)/2
    P=-S*(b-A)**2/8

    lhs=(
        16*J**4
        +160*S*J**2*P
        +8*S*J**2
        +256*S**2*P**2
        -32*S**2*P
        +S**2
    )
    assert lhs==0,(s,a,lhs)

    X=4*J**2/S
    Y=16*P
    assert (2*X+Y-4)*(X+2*Y+4)==-18

    f1=8*J**2+16*S*P-4*S
    f2=4*J**2+32*S*P+4*S
    assert f1==6*S**2*A**2
    assert f2==-3/A**2
    assert f1*f2==-18*S**2


def main() -> None:
    for s in range(1,50,2):
        for a in list(range(-20,0))+list(range(1,21)):
            check_rational(s,a)

    print("PARAMETER_ELIMINATION_IDENTITY=PASS")
    print("UNIVERSAL_NORMALIZED_SPLIT_CONIC=PASS")
    print("RECIPROCAL_SQUARE_FACTOR_RECOVERY=PASS")
    print("POISSON_18_CAUSAL_LINK_NOT_ASSUMED")


if __name__ == "__main__":
    main()
