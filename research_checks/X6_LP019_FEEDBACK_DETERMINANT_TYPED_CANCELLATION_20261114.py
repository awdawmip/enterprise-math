#!/usr/bin/env python3
"""Independent exact rational proof-corollary witness for frozen LP019 source typing.

Original frozen sources (not executed or modified by this checker):
 experiments/brc_feedback_mobius_interaction_check.py @ fd2bcff1 blob 7ed252d735e37dd4bca3088f1f2ffa4fac5b446e
 experiments/brc_cycle_interaction_polynomial_check.py @ fd2bcff1 blob 6f37fc8021bf5d9556ed6ff5d5fa34db6b097219
This checks explicit determinant-response identities and the pure 3-cycle Möbius factor;
finite checks are not a proof of general n and do not certify the original executables.
"""
from fractions import Fraction as Q
from itertools import product

VALUES = (Q(0), Q(1,5), Q(1,4), Q(1,3))
EDGES = ((0,0), (0,1), (1,0), (1,1))

def det2(a,b,c,d):
    return (1-a)*(1-d)-b*c

def check_two_state():
    checks=0
    for weights in product(VALUES, repeat=4):
        a,b,c,d=weights
        p=det2(a,b,c,d)
        # Every row sum is <= 2/3, hence spectral radius < 1.
        assert p>0
        inverse=(( (1-d)/p, b/p ), (c/p, (1-a)/p))
        for edge,(u,v) in enumerate(EDGES):
            shifted=list(weights)
            shifted[edge]+=Q(1,7)
            dp=(det2(*shifted)-p)/Q(1,7)  # exact affine-in-one-edge derivative
            q=weights[edge]
            assert dp<=0
            assert -q*dp/p == q*inverse[v][u]
            checks+=1
    assert checks==1024
    return checks

def check_three_cycle():
    checks=0
    for x,y,z in product(VALUES,repeat=3):
        # Pure oriented three-cycle: every non-full principal subset has determinant 1.
        p=1-x*y*z
        j=1/p   # third-order Möbius factor; no signed path count
        assert p>0 and j>=1
        assert (j>1)==(x*y*z>0)
        checks+=1
    assert checks==64
    assert 1/(1-Q(1,2)**3)==Q(8,7)
    return checks

def check_witness():
    a,b,c,d=Q(1,5),Q(1,4),Q(1,3),Q(0)
    p=det2(a,b,c,d)
    assert p==Q(43,60)
    # Three positive labelled directed edges, even though determinant has negative terms.
    responses=(a/p,b*c/p,b*c/p)
    assert responses==(Q(12,43),Q(5,43),Q(5,43))
    return p,responses

if __name__=='__main__':
    n=check_two_state()
    m=check_three_cycle()
    p,r=check_witness()
    print('PASS_X6_LP019_TYPED_FEEDBACK_DETERMINANT_AND_MOBIUS')
    print('exact_2x2_edge_derivative_equalities=',n)
    print('exact_3cycle_mobius_cases=',m)
    print('witness_det=',p,'response=',r,'pure_3cycle_J=',Q(8,7))
    print('original_frozen_executables_replayed=false')
    print('project_result_admitted=false')
