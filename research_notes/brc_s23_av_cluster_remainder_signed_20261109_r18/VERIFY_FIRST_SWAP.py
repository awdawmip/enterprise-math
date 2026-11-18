#!/usr/bin/env python3
"""Exact certificate for one-boundary first-swap risk update at S23 n=226."""
from fractions import Fraction as F
from VERIFY_CLUSTER_MIXED import direct_risk

lo=F(262204504569236716045286,10**24)
hi=F(262204504569236716045287,10**24)
for theta in [lo,hi]:
    eta=F(16,61)-theta
    delta=61*eta
    gaps=[]
    for r in range(61):
        last=r+61*((226-1-r)//61)
        rp=(r+19)%61
        gaps.append((F(1,61)+(rp-last)*eta,r))
    assert [r for G,r in gaps if G<=0]==[42]
    x=225*eta-F(1,61)
    assert x==-dict((r,G) for G,r in gaps)[42]
    assert 0<delta-x<x<delta
    assert direct_risk(theta,128,225)==-2047+7808*theta
    assert direct_risk(theta,128,226)==-2090+7972*theta
    assert direct_risk(theta,128,226)-direct_risk(theta,128,225)==delta-x
print('PASS_S23_FIRST_CROSSING_226_EXACT')
print('crossing_cluster_r=42 next_r=0','new_cut_i=225','historical_arc=[t0,t61]')
print('x=225*eta-1/61=59-225*theta')
print('delta=61*eta=16-61*theta')
print('new_risk_increment=delta-x=164*theta-43')
print('exact_theta_interval_endpoints_checked=2')
