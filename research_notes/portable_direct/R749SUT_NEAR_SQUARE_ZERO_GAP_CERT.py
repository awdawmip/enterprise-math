#!/usr/bin/env python3
"""R749SUT: exact integer checks for a zero-gap near-square Q=+1 family.

The universal results are proved in the accompanying paper; tests are finite.
Full global nonstandard transfer uses upstream unreviewed R749SUO classification.
"""
from math import isqrt
import json


def tau_xy(x, y):
    n = x*y
    return (n-1)*(n-x-1)*(n-y-1)


def q1_oracle(B):
    best, winners = -1, []
    for x in range(2, isqrt(B)+1):
        y = B//x
        n = x*y
        if n-x-y < 1:
            continue
        score = tau_xy(x,y)
        if score > best:
            best, winners = score, [(x,y)]
        elif score == best:
            winners.append((x,y))
    return best, winners


def fourfold_polynomial(B, s):
    """64*[T(B,s) - (B-1-D)^3] for D=B-(s-1)^2/4."""
    A = B-1
    d4 = 4*B-(s-1)**2
    return 16*A*A*(3*d4-4*s)+4*A*(16*B-3*d4*d4)+d4**3


def certified_near_square(t,h):
    return t >= 11 and h >= 0 and 4*t >= 4*h+3*(h-1)**2+12


def verify():
    tested_near = 0
    minimum_polynomial = None
    for t in range(11,601):
        h=0
        while certified_near_square(t,h):
            B=t*(t+h)
            s=2*t+h
            p=fourfold_polynomial(B,s)
            assert p>0,(t,h,p)
            best,pairs=q1_oracle(B)
            assert best==tau_xy(t,t+h) and pairs==[(t,t+h)],(t,h,best,pairs)
            a,u,v,d=B-t-1,B-1,B-s,B-t-h-1
            assert min(a,u,v,d)>=1 and max(a,u,v,d)<=B-1
            assert a*d-u*v==1 and u+v-a-d==1
            tested_near+=1
            minimum_polynomial=p if minimum_polynomial is None else min(minimum_polynomial,p)
            h+=1
    certified_general=0
    for B in range(6,2001):
        best,winners=q1_oracle(B)
        for x in range(2,isqrt(B)+1):
            if B%x: continue
            y=B//x
            if B-x-y<1: continue
            s=x+y
            if 4*B-(s-1)**2<=0: continue
            if fourfold_polynomial(B,s)>0:
                assert tau_xy(x,y)==best and winners==[(x,y)],(B,x,y,best,winners)
                certified_general+=1
    samples=[]
    for t,h in [(11,0),(11,1),(11,2),(11,3),(25,5),(100,10),(1000,30),(1000000,500)]:
        B=t*(t+h);s=2*t+h
        samples.append(dict(t=t,h=h,M=str(B-1),certified_by_simple_inequality=certified_near_square(t,h),
            factor_pair=[t,t+h],oriented_tuple=[str(B-t-1),str(B-1),str(B-s),str(B-t-h-1)],
            tau=str(tau_xy(t,t+h)),strict_gap_polynomial_positive=fourfold_polynomial(B,s)>0))
    return dict(id="R749SUT_NEAR_SQUARE_ZERO_GAP_V1",status="PASS",
        method="pure exact Python integer arithmetic",
        near_square_oracle=dict(t_min=11,t_max=600,cases=tested_near,
             minimum_fourfold_polynomial=str(minimum_polynomial)),
        generic_gap_oracle=dict(B_min=6,B_max=2000,certified_factor_pairs_checked=certified_general),
        samples=samples,
        proof_status="author proof; upstream universal Q=+1 classification is AUTHOR_EXACT_NOT_REVIEWED",
        scope="Finite checks are not a proof of the infinite family; algebraic proof is in the note.")


if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,sort_keys=True,indent=2))
