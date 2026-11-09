#!/usr/bin/env python3
"""Exact 67 distinct historical-short-arc transfer check after S23 n=225."""
from fractions import Fraction as Q
from VERIFY_INTERVAL_COLLAPSE import direct_phase_risk
lo=Q(262204504569236716045286,10**24)
hi=Q(262204504569236716045287,10**24)
for tag,theta in [('lower',lo),('upper',hi)]:
    beta=1-theta
    eta=Q(16,61)-theta
    delta=61*eta
    x=225*eta-Q(1,61)
    assert 0<delta-x<x<delta
    used=set()
    prior=direct_phase_risk(theta,128,225)
    assert prior==-2047+7808*theta
    for j in range(67):
        i=225+j
        rplus=j%61
        a=rplus+(61 if j>=61 else 0)
        b=a+61
        assert b<128 and a not in used
        used.add(a)
        # Each inserted point is x inside the original historical arc a->a+61.
        assert ((i-a)*beta)%1==x
        assert ((b-a)*beta)%1==delta
        now=direct_phase_risk(theta,128,i+1)
        assert now-prior==delta-x,(i,now-prior,delta-x)
        prior=now
    assert len(used)==67
    assert prior==-2047+7808*theta+67*(164*theta-43)
    # First next source index is outside the 67 historical short arcs.
    i=292
    risk293=direct_phase_risk(theta,128,293)
    assert risk293==prior,(tag,prior,risk293)
    print(f'S23_{tag.upper()}_67_TRANSFERS: i=225..291, first_arc_count=61, second_arc_count=6, constant_delta=164*theta-43, risk293_equal_risk292=True')
print('PASS_S23_67_DISJOINT_SHORT_ARC_TRANSFERS')
