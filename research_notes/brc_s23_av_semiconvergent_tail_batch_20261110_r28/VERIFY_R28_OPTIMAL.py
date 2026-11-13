#!/usr/bin/env python3
"""Exact endpoint certificate for minimal terminal H and maximal bracket K."""
from fractions import Fraction
from bisect import bisect_right
from collections import Counter
Q,A,J,C,M=14298,3749,25339,6644,128
bound=(Fraction(262204504569236716045286,10**24),
       Fraction(262204504569236716045287,10**24))
for i,theta in enumerate(bound):
    cuts=sorted(((t*theta)%1,t) for t in range(M))
    positions=[p for p,_ in cuts]
    ids=[t for _,t in cuts]
    def owner(t):
        p=(t*theta)%1
        z=bisect_right(positions,p)-1
        assert z>=0
        return z
    def occupancy(h):
        return Counter(owner(t) for t in range(J-h,J))
    freq163=occupancy(163)
    freq164=occupancy(164)
    missing163=set(range(M))-set(freq163)
    assert len(freq163)==M-1 and missing163=={127} and ids[127]==61
    assert set(freq164)==set(range(M))
    assert freq164[127]==1 and owner(J-164)==127
    assert Counter(freq164.values())=={1:92,2:36}
    u=Q*theta-A
    v=C-J*theta
    assert u>0 and v>0 and v-9*u>0 and v-10*u<0
    slacks=[]
    for t in range(J-164,J):
        p=(t*theta)%1
        arc=owner(t)
        right=positions[(arc+1)%M]+(1 if arc==M-1 else 0)
        slacks.append(right-p-9*u)
    assert min(slacks)>0
    print('endpoint',i,'H_min',164,'missing_H163_phase_rank',127,
          'missing_H163_source_cut',61,'multiplicity_H164_1',92,
          'multiplicity_H164_2',36,'K_max',9,'v_minus_9u',v-9*u,
          'v_minus_10u',v-10*u,
          'min_forward_slack_for_9u',min(slacks))
print('PASS_R28_OPTIMAL_H164_AND_MAXIMAL_K9')
