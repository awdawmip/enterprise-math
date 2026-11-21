#!/usr/bin/env python3
"""R74: exact rational finite crosscheck; the all-p theorem is proved in the paper."""
from fractions import Fraction as Q
import json

WITNESSES = ((15, -6, 1), (10, -5, 1), (24, -14, 3))
SAMPLES = (Q(1, 100), Q(1, 11), Q(1, 10), Q(1, 2), Q(1), Q(3), Q(11), Q(12), Q(100))

def demand(a):
    return max(sum(max(x, 0) for x in a), sum(max(-x, 0) for x in a))

def gaps(a):
    x, y, z = a
    m2 = 2*x + 6*y + 12*z
    m3 = 6*x + 24*y + 60*z
    m4 = 14*x + 78*y + 252*z
    return abs(m4), abs(m3-m2), max(abs(m2), abs(m3), abs(m4-m2), abs(m4-m3))

def radius(g, t):
    b, c, u = g
    return max(Q(b, 4), Q(c, 4)/t, Q(u, 2)/(1+t))

def theorem(t):
    if t <= Q(1,11):
        return Q(6)/(1+t)
    if t <= 1:
        return Q(1,2)/t
    if t <= 11:
        return Q(1,2)
    return Q(6)/(1+t)

def main():
    n = 30
    shells = [[] for _ in range(n+1)]
    for a2 in range(-n,n+1):
        for a3 in range(-n,n+1):
            for a4 in range(-n,n+1):
                a=(a2,a3,a4)
                if not any(a):
                    continue
                if next(v for v in a if v) < 0:  # quotient by overall sign
                    continue
                q=demand(a)
                if q <= n:
                    shells[q].append((a,gaps(a)))
    assert sum(map(len,shells)) == 47305
    assert [demand(a) for a in WITNESSES] == [16,11,27]
    assert [gaps(a) for a in WITNESSES] == [(6,0,12),(2,2,2),(0,12,12)]
    observations=[]
    for t in SAMPLES:
        best = None
        for p in range(1,n+1):
            for a,g in shells[p]:
                val=radius(g,t)
                if best is None or val < best[0]:
                    best=(val,a,p)
            if p in (26,27,30):
                if p >= 27:
                    assert best[0] == theorem(t), (t,p,best,theorem(t))
                observations.append({"t":str(t),"p":p,"min_radius":str(best[0]),"witness":list(best[1]),"witness_demand":best[2]})
        if t > 11:
            r26=next(x for x in observations if x['t']==str(t) and x['p']==26)
            assert Q(r26['min_radius']) > theorem(t)
    report={"schema":"X6_R74_TWO_NOISY_CHANNEL_CERTIFICATE_V1",
            "scope":"exhaustive unoriented q<=30; symbolic paper covers all p>=27 and all positive real t",
            "unoriented_tested":sum(map(len,shells)),
            "sample_weights":[str(t) for t in SAMPLES],
            "witnesses":[{"a":list(a),"q":demand(a),"gaps_B_T_U":list(gaps(a))} for a in WITNESSES],
            "observations": observations, "assertions":"PASS"}
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
