#!/usr/bin/env python3
"""Exact checker for odd-sector extremal Joukowski saturation uniqueness."""

from __future__ import annotations

from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n)+1):
        if n%d==0:
            return False
    return True


def lane_set(s: int, q: int) -> set[int]:
    h=(s-1)//2
    return {j%q for j in range(-h,h+1)}


def lambda_image(s: int, q: int) -> set[int]:
    inv2=pow(2,-1,q)
    return {(-s*a - inv2*pow(a,-1,q))%q for a in range(1,q)}


def sumsq_lane(s: int) -> int:
    h=(s-1)//2
    return 2*sum(j*j for j in range(1,h+1))


def main() -> None:
    # Verify formulas and uniqueness over a broad exact grid.
    hits_minus=[]
    hits_plus=[]
    for s in range(3,1000,2):
        qm=2*s-1
        if is_prime(qm):
            sat=lambda_image(s,qm)==lane_set(s,qm)
            if sat:
                hits_minus.append((s,qm))
                assert qm==5 and s==3
            # moment identity if saturation
            if sat:
                lhs=sumsq_lane(s)%qm
                rhs=((s+1)*pow(2,-1,qm))%qm
                assert lhs==rhs
                assert 75%qm==0

        qp=2*s+1
        if is_prime(qp):
            sat=lambda_image(s,qp)==lane_set(s,qp)
            if sat:
                hits_plus.append((s,qp))
                assert qp==7 and s==3
            if sat:
                lhs=sumsq_lane(s)%qp
                rhs=(-s*pow(2,-1,qp))%qp
                assert lhs==rhs
                assert 21%qp==0

    assert hits_minus==[(3,5)]
    assert hits_plus==[(3,7)]

    # Native fiber profiles at the two extremal characteristics.
    for q,expected in ((5,{-1:1,0:2,1:1}),(7,{-1:2,0:2,1:2})):
        counts={-1:0,0:0,1:0}
        for a in range(1,q):
            lam=(-3*a - pow(2,-1,q)*pow(a,-1,q))%q
            signed=lam if lam<=q//2 else lam-q
            assert signed in counts
            counts[signed]+=1
        assert counts==expected,(q,counts)

    print("LOWER_EXTREMAL_UNIQUENESS_S3_Q5=PASS")
    print("UPPER_EXTREMAL_UNIQUENESS_S3_Q7=PASS")
    print("SECOND_MOMENT_OBSTRUCTIONS_75_AND_21=PASS")
    print("NATIVE_Q5_PROFILE_121=PASS")
    print("NATIVE_Q7_PROFILE_222=PASS")


if __name__ == "__main__":
    main()
