#!/usr/bin/env python3
"""Exact witness for the S23 AV n=3 three-class observer minimax.

Source scientific pin: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Only Python stdlib Fraction arithmetic is used for all assertions.
"""
from fractions import Fraction as Q
from math import comb

D = Q(5211, 21952)
T = (Q(0), Q(0), Q(1381, 1764), Q(919, 37044))

def q(z):
    return sum(Q(comb(3,k))*z**(3-k)*(1-z)**k*T[k] for k in range(4))

def low(z):
    amax = min(Q(7,8), 1-Q(8,7)*z)
    return 1-(amax+z)**3

def high(z):
    amin = max(Q(1,2),1-2*z)
    return 1-(amin+z)**3

def residual_formula(index,z):
    # The following are 5211/21952 - (high-q) or - (q-low).
    if index == 0: return (4*z-1)*(196160*z*z-191428*z-155401)/592704
    if index == 1: return (4*z-1)*(492512*z*z-339604*z+363215)/592704
    if index == 2: return (-15760384*z**3+9473088*z*z-21674424*z+2573053)/4741632
    if index == 3: return -(4*z-1)**2*(85976*z-125993)/592704
    raise ValueError(index)

intervals = ((Q(1,16),Q(1,4)),(Q(1,4),Q(7,16)),
             (Q(1,16),Q(7,64)),(Q(7,64),Q(7,16)))

def verify():
    assert all(0 <= t <= 1 for t in T)
    C=(Q(1),Q(0),Q(0),Q(0))
    assert all(0 <= T[k]+C[k] <= 1 for k in range(4))
    for ztest in (Q(1,16),Q(1,4),Q(7,16)):
        qc=sum(Q(comb(3,k))*ztest**(3-k)*(1-ztest)**k*C[k] for k in range(4))
        assert qc==ztest**3
    assert sum(Q(comb(3,k))*Q(1,4)**(3-k)*Q(3,4)**k*T[k]
               for k in range(4)) == Q(935,2744)
    assert q(Q(1,4)) == Q(935,2744)
    assert high(Q(1,4)) == Q(37,64)
    assert low(Q(1,4)) == Q(2269,21952)
    assert high(Q(1,4))-q(Q(1,4)) == D
    assert q(Q(1,4))-low(Q(1,4)) == D
    for j,(left,right) in enumerate(intervals):
        # 4 samples prove cubic polynomial identity exactly.
        for k in range(4):
            z=left+(right-left)*Q(k,3)
            target = (D-high(z)+q(z)) if j<2 else (D-q(z)+low(z))
            assert residual_formula(j,z) == target, (j,z)
    # Global non-negativity via rational interval signs; no discretization.
    assert 196160*Q(1,4)**2-155401 < 0  # upper-left Q1 <= this
    assert 363215-339604*Q(7,16) > 0      # upper-right Q2 >= this
    assert 125993-85976*Q(7,16) > 0       # lower-right factor
    assert (2573053-21674424*Q(7,64)
            -15760384*Q(7,64)**3) > 0     # lower-left positive lower bound
    print('PASS_S23_N3_THREE_CLASS_COARSE_MINIMAX_EXACT_20261107')
    print('source_pin', '43ec6098b1330ae86d0a7863be336c5d97f6ef34')
    print('domain','a,c in [1/2,7/8], z=(1-a)c in [1/16,7/16]')
    print('A_decoder_coefficients',*[str(x) for x in T])
    print('C_decoder_coefficients','1','0','0','0')
    print('q_at_1_4',q(Q(1,4)))
    print('exact_minimax',D)
    print('piecewise_interval_count',len(intervals))
    print('proof_mode','exact rational polynomial identities + interval sign checks')

if __name__=='__main__': verify()
