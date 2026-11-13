#!/usr/bin/env python3
"""R749SNI: exact left slab [1/2,3/5] extension of R749SNH.
Depends on adjacent R749SNH_OFFDIAGONAL_HALF_SWEEP_EXACT_CHECK.py.
"""
from fractions import Fraction as Q
from itertools import product
import json
from R749SNH_OFFDIAGONAL_HALF_SWEEP_EXACT_CHECK import AD, SIGNS, vertices, src


def tv(source, s):
    _, h, up, un, wp, wn = source
    tau, sigma, eta = 2 - 2 * s, 2 * s - Q(4,5), Q(1,5)
    acc = Q(0)
    for a,d in AD:
        base = 1 + Q(a,2) + s*d + h*a*d
        dec = 1 + tau*a + sigma*d + eta*a*d
        assert dec >= 0
        for p,q in SIGNS:
            b = base + p*(up if a==1 else un) + q*(wp if d==1 else wn)
            assert b >= 0
            acc += abs(b - dec)/32
    return acc


def verify_lower():
    ea = (0,4,5,8,10)
    eb = (0,1,2,3,12,13,14,15)
    for s in (Q(1,2), Q(11,20), Q(7,12), Q(3,5)):
        alpha=src(Q(1,2),s,s-Q(1,2),2*(1-s),0,1,0)
        beta=src(Q(1,2),s,Q(3,2)-s,0,0,0,0)
        assert min(alpha+beta)>=0 and sum(alpha)==sum(beta)==1
        for tau,sigma,eta in ((Q(1),Q(1,5),Q(1,5)),(Q(4,5),Q(2,5),Q(1,5)),(Q(0),Q(0),Q(0))):
            dec=[(1+tau*a+sigma*d+eta*a*d)/16 for a,d in AD for _ in SIGNS]
            la=sum(alpha[i]-dec[i] for i in ea)
            lb=sum(beta[i]-dec[i] for i in eb)
            assert la == (11-8*s-tau-sigma+3*eta)/16
            assert lb == (3-2*s-2*eta)/4
            assert (4*la+lb)/5 == (13-10*s)/20+(1-tau-sigma+eta)/20


def main():
    lo,hi=Q(1,2),Q(3,5)
    V,info=vertices(lo,hi)
    gap=[tv(v,v[0])-(13-10*v[0])/20 for v in V]
    assert all(x<=0 for x in gap)
    verify_lower()
    data={'name':'R749SNI_LEFT_HALF_SWEEP_EXTENSION','interval':['1/2','3/5'],
        'theorem':'rho(1/2,s)=(13-10s)/20 for every real s in [1/2,3/5]',
        'method':'two signed-source event lower cuts + decoder positivity; joint six-dimensional vertex upper certificate',
        'six_facet_combinations':info['six_facet_combinations'],
        'nonsingular_bases':info['nonsingular_bases'],
        'feasible_bases':info['feasible_bases'],
        'distinct_vertices':len(V),
        'endpoint_counts':info['endpoint_counts'],
        'equality_vertices':sum(x==0 for x in gap),
        'violations':sum(x>0 for x in gap),
        'max_gap':str(max(gap)),
        'status':'PASS'}
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
