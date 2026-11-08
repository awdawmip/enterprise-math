#!/usr/bin/env python3
"""Incremental upper-bound certificate N(H)<=N0, given prior H-1 coverage.
Checks only new boundary thresholds and their exact immediate neighbors,
plus exterior cells. Uses certified rank/select and prefix occupancy oracles.
"""
from time import perf_counter
import VERIFY_ORACLE as m
from VERIFY_OCCUPANCY import count_prefix_in_gap, N

def verify_increment(H):
    assert 7001<=H<=380294
    assert m.certify_h(H)
    new_points=H+1
    M=(H+1)*(H+2)//2
    checked=set()
    occupied=0; minoccupancy=10**100
    for v in range(H+1):
        j=H-v
        r=m.rank(H,v,j)
        for ix in (r-1,r):
            if not 0<=ix<M-1 or ix in checked:continue
            # left and right are exactly adjacent in T_H by rank/select.
            left=m.select(H,ix)
            right=m.select(H,ix+1)
            assert left==(v,j) or right==(v,j)
            nseen=count_prefix_in_gap(H,N,left,right)
            assert nseen>0,('NEW_GAP_EMPTY',H,left,right,ix)
            minoccupancy=min(minoccupancy,nseen)
            checked.add(ix)
            occupied+=1
    # At least one prefix point in each exterior interval of new T_H.
    # t_min=-H; t_max=r*H. E(0,l)=-r*l, E(k,0)=k.
    l=H*m.D//m.P+1
    k=H*m.P//m.D+1
    assert l<=N and k<=N
    assert m.P*l>m.D*H and m.D*k>m.P*H
    return {'H':H,'frontier':new_points,'changed_intervals':occupied,'min_count':minoccupancy,'left_outer_l':l,'right_outer_k':k}

if __name__=='__main__':
    start=perf_counter()
    assert m.prove_r_enclosure()
    for H in range(7001,7002):
        result=verify_increment(H)
        print('PASS_INCREMENT',result,flush=True)
    print('PASS_S23_AV_ONE_STEP_PLATEAU_EXTENSION',round(perf_counter()-start,3),flush=True)
