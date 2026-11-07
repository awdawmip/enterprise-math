#!/usr/bin/env python3
"""Exact finite checks for S23 n=3 fixed-fiber full-output minimax theorem.
Frozen input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Universal theorem: see analytic proof in PROOF.md; no sampling-based inference.
"""
from fractions import Fraction as Q
from itertools import product

Z0,Z1,Z2,Z3=Q(1,16),Q(7,64),Q(1,4),Q(7,16)
D=Q(5211,21952)

def a_bounds(z):
    return max(Q(1,2),1-2*z),min(Q(7,8),1-Q(8,7)*z)
def b_bounds(z):
    amin,amax=a_bounds(z)
    return 1-z-amax,1-z-amin
def law(z,b):
    a=1-z-b
    assert Q(1,2)<=a<=Q(7,8) and 0<b<=Q(1,4)
    return {w:a**w.count(0)*z**w.count(1)*b**w.count(2)
            for w in product(range(3),repeat=3)}
def four(z,b):
    return (3*b*(1-b)**2,3*b*b-2*b**3,(1-b)**3-z**3,z**3)
def tv(p,q):
    return sum((abs(p[k]-q[k]) for k in p),Q(0))/2
def diameter(z):
    lo,hi=b_bounds(z)
    return (1-lo)**3-(1-hi)**3
def diameter_piece(z):
    if z<=Z1: return (Q(7,8)+z)**3-(1-z)**3
    if z<=Z2: return (1-z/7)**3-(1-z)**3
    return (1-z/7)**3-(Q(1,2)+z)**3
def check(z):
    lo,hi=b_bounds(z)
    assert 0<lo<=hi<=Q(1,4)
    L,H=law(z,lo),law(z,hi)
    for b in (lo,lo+(hi-lo)/4,(lo+hi)/2,lo+3*(hi-lo)/4,hi):
        P=law(z,b)
        assert sum(P.values(),Q(0))==1
        v=four(z,b)
        assert sum(v,Q(0))==1
        assert sum((P[w] for w in P if 2 in w),Q(0))==v[0]+v[1]
        assert sum((P[w] for w in P if 2 not in w and 0 in w),Q(0))==v[2]
        assert P[(1,1,1)]==v[3]
    for w in L:
        assert (H[w]>=L[w]) if (2 in w) else (H[w]<=L[w])
    assert tv(L,H)==diameter(z)==diameter_piece(z)
    assert tv(dict(enumerate(four(z,lo))),dict(enumerate(four(z,hi))))==diameter(z)
    M={w:(L[w]+H[w])/2 for w in L}
    assert tv(L,M)==tv(H,M)==diameter(z)/2
    for b in (lo,lo+(hi-lo)/4,(lo+hi)/2,lo+3*(hi-lo)/4,hi):
        assert tv(law(z,b),M)<=diameter(z)/2
    assert diameter(z)<=2*D
def main():
    assert a_bounds(Z0)==(Q(7,8),Q(7,8))
    assert a_bounds(Z3)==(Q(1,2),Q(1,2))
    assert b_bounds(Z2)==(Q(1,28),Q(1,4))
    assert diameter(Z0)==diameter(Z3)==0
    assert diameter(Z2)==Q(5211,10976)
    assert diameter(Z2)/2==D
    pts=(Z0,Z1,Z2,Z3,Q(1,10),Q(1,8),Q(3,16),Q(5,16),Q(3,8))
    for z in pts: check(z)
    assert Q(9,16)-Q(1,7)>0
    assert Q(1,2)**2*(Q(1,2)-3*Q(1,4))==-Q(1,16)
    print("PASS_S23_N3_FULL_27_FIBER_RADIUS_EXACT_20261107")
    print("frozen_pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34")
    print("z_domain 1/16 7/16")
    print("max_fiber_diameter",diameter(Z2))
    print("max_fiber_radius",D)
    print("max_at_z",Z2)
    print("full_ordered_output_count",3**3)
    print("fourclass_low",*[str(x) for x in four(Z2,Q(1,28))])
    print("fourclass_high",*[str(x) for x in four(Z2,Q(1,4))])
    print("rational_sample_fibers_checked",len(pts))
    print("all_real_proof analytic derivative and exact three-piece diameter")
    print("n4_word_0002_derivative_counterexample",-Q(1,16))
if __name__=="__main__": main()
