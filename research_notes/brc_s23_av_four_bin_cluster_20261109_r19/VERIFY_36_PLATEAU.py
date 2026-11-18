#!/usr/bin/env python3
"""S23 first 36-step risk plateau n293..328 and first restored increment n329."""
from fractions import Fraction as Q
from VERIFY_INTERVAL_COLLAPSE import direct_phase_risk

def historical_maxima(beta,m,n):
    cuts=sorted(((i*beta)%1,i) for i in range(n))
    owner=next(i for _,i in reversed(cuts) if i<m)
    ret={i:Q(0) for i in range(m)}
    for j,(point,i) in enumerate(cuts):
        if i<m:owner=i
        nxt=cuts[(j+1)%n][0]+(j==n-1)
        gap=nxt-point
        if gap>ret[owner]:ret[owner]=gap
    return ret

lo=Q(262204504569236716045286,10**24)
hi=Q(262204504569236716045287,10**24)
for tag,theta in [('lower',lo),('upper',hi)]:
    beta=1-theta
    eta=Q(16,61)-theta;delta=61*eta;x=225*eta-Q(1,61)
    assert 0<delta-x<x<delta
    oldrisk=direct_phase_risk(theta,128,292)
    assert oldrisk==-4928+18796*theta
    for h in range(6,42):
        i=286+h
        assert 292<=i<=327
        # Event targets the historical boundary arc that starts at h+61.
        a=h+61
        assert ((i-a)*beta)%1==x
        old=historical_maxima(beta,128,i)
        new=historical_maxima(beta,128,i+1)
        assert old[a]==delta and new[a]==delta,(h,old[a],new[a])
        assert sum(old.values())==sum(new.values())
        assert direct_phase_risk(theta,128,i+1)==oldrisk
    a=42+61;i=328
    old=historical_maxima(beta,128,i)
    new=historical_maxima(beta,128,i+1)
    assert ((i-a)*beta)%1==x
    assert old[a]==delta and new[a]==x
    assert sum(old.values())-sum(new.values())==delta-x
    newrisk=direct_phase_risk(theta,128,329)
    assert newrisk-oldrisk==delta-x
    assert newrisk==-4971+18960*theta
    print(f'S23_{tag.upper()}_PLATEAU: n=293..328, 36 distinct long historical arcs, each preserves a second delta gap, next_growth_n=329, increment=164*theta-43')
print('PASS_S23_36_ZERO_PLATEAU_AND_FIRST_RESTART')
