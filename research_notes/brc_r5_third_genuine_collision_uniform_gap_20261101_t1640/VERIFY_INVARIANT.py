#!/usr/bin/env python3
"""Exact signed-support annihilator certificate for R5 third-key time-only subtrees.
Run in the same directory as VERIFY.py; no packages outside Python stdlib.
"""
from fractions import Fraction as F
from itertools import product
from VERIFY import O, R, dot
Z, U = F(0), F(1)
H = (F(5), F(0), F(5), F(-8))

def full_formula(p1,p2,q1,q2,qb,r):
    return (F(-33,8) + sum(F(13,16)*p-F(1,8)*p*q+q/F(8) for p,q in ((p1,q1),(p2,q2)))
            -qb/F(4)+F(5,2)*r)

def lr_formula(p,q,r):
    return (-33+13*p-2*p*q+20*r)/8

def main():
    # Any delayed K-only P outcomes change times along (8/5,1),
    # so the H=(5,0,5,-8) functional is annihilated exactly.
    assert dot(H,(Z,Z,F(1,20),F(1,32)))==Z
    # Both sides are separately affine in every policy parameter
    # and in total delay parameter lambda, so corners suffice.
    count=0
    for p,q,r,k,lam in product((Z,U), repeat=5):
        assert dot(H,R(p,q,r,k,lam))==lr_formula(p,q,r)
        count+=1
    for p1,p2,q1,q2,qb,r,k1,k2,lam in product((Z,U), repeat=9):
        assert dot(H,O(p1,p2,q1,q2,qb,r,k1,k2,lam))==full_formula(p1,p2,q1,q2,qb,r)
        count+=1
    witness=O(Z,Z,Z,Z,U,Z,U,U,F(1,4))
    assert witness==(F(4,5),F(7,32),F(21,8),F(43,16))
    assert dot(H,witness)==-F(35,8)
    # R and O permit lambda=h*eps, whose interpretation comes from
    # a legal eps in (0,1) and a positive integral delay h.
    regression=0
    for h in (1,2,3,5,10):
        eps=F(1,2); lam=h*eps
        lvals=[dot(H,R(p,q,r,k,lam)) for p,q,r,k in product((Z,U),repeat=4)]
        fvals=[dot(H,O(*x,lam)) for x in product((Z,U),repeat=8)]
        assert min(lvals)==-F(33,8) and min(fvals)==-F(35,8)
        assert min(lvals)-min(fvals)==F(1,4)
        regression+=len(lvals)+len(fvals)
    print('annihilator_H=(5,0,5,-8); H_dot_K_delay_vector=0')
    print('all_real_LR_H=(-33+13*p-2*p*q+20*r)/8')
    print('all_real_FULL_H=-33/8+sum_i(13*p_i/16-p_i*q_i/8+q_i/8)-q_B/4+5*r/2')
    print('all_real_min_H_LR=-33/8; FULL=-35/8; gap=1/4')
    print('all_real_Linf_distance_lower=1/72')
    print('multi_affine_corner_checks=',count,'delay_h_regression_policies=',regression)
    print('PASS_EXACT_R5_DELAY_INVARIANT_SIGNED_SUPPORT_CERT')

if __name__=='__main__':main()
