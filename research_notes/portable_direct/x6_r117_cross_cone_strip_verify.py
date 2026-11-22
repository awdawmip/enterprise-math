#!/usr/bin/env python3
"""Exact six-pair finite replay of the R117 conditional BRC strip theorem.
The analytic proof, not this finite Port replay, covers all integer p >= 10.
"""
from fractions import Fraction as Q
from math import lcm
import json

Q0, Q1, D = Q(3, 5), Q(7, 10), Q(1, 4)
PORTS = (10, 11, 15, 16, 17, 21, 28)
BASE = ((0, 1, -1), (0, 1, 1), (1, 0, 0), (1, -1, -1),
        (1, -1, 1), (1, 1, -1), (1, 1, 1))
NEW = (1, 2, 0)

def inverse(t, m, n):
    assert (m - n) % 2 == 0
    return (10*t - 12*m + 3*n, -5*t + 7*m - 2*n,
            t + (n - 3*m)//2)

def canonical(a):
    b = tuple(-v for v in a)
    return min(a, b)

def port(a):
    return max(sum(max(x, 0) for x in a), sum(max(-x, 0) for x in a))

def gaps(a):
    x, y, z = a
    h = (0, x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)
    return tuple(abs(h[i] - h[j]) for i in range(4) for j in range(i+1, 4))

VECTORS = []
for x in range(-28, 29):
    for y in range(-28, 29):
        for z in range(-28, 29):
            a = (x, y, z)
            if a != (0,0,0) and a == canonical(a) and port(a) <= 28:
                VECTORS.append((port(a), a, gaps(a)))
assert len(VECTORS) == 38598

def verify(q, d):
    assert Q0 <= q <= Q1 and -D <= d <= D
    w = (1+10*q, 11-10*q, 35+36*q, 143-72*q+d)
    den = lcm(*(v.denominator for v in w))
    W = [int(v*den) for v in w]
    sums = [W[i]+W[j] for i in range(4) for j in range(i+1,4)]
    Y = W[1]+W[3]
    near = set()
    less_than_eta = 0
    for p,a,gg in VECTORS:
        if all(g*Y < 6*s for g,s in zip(gg,sums)):
            less_than_eta += 1
        if all(g*Y < 9*s for g,s in zip(gg,sums)):
            near.add(a)
    assert less_than_eta == 0
    predicted = {canonical(inverse(*r)) for r in BASE}
    enters = 151*q > 100+d
    if enters:
        predicted.add(canonical(inverse(*NEW)))
    assert near == predicted, (q,d,near ^ predicted)
    ports = {}
    for p in PORTS:
        got = {a for a in near if port(a) <= p}
        expected = {a for a in predicted if port(a) <= p}
        assert got == expected
        # (0,1,1) realizes the exact optimum from Port 10 onward.
        witness = canonical(inverse(0,1,1))
        assert port(witness) == 10
        gw = gaps(witness)
        assert all(g*Y <= 6*s for g,s in zip(gw,sums))
        assert any(g*Y == 6*s for g,s in zip(gw,sums))
        ports[str(p)] = len(got)
    return {"q":str(q),"delta":str(d),"entry":enters,
            "weights":[str(v) for v in w],"eta":str(Q(6,1)/(w[1]+w[3])),
            "candidate_vectors_checked":len(VECTORS),
            "near_count_at_p28":len(near),"ports":ports}

def main():
    samples = [(Q0,-D), (Q0,D), (Q1,-D), (Q1,D)]
    for d in (-D, Q(0), D):
        q_star = (100+d)/151
        samples.extend([(q_star-Q(1,1000),d), (q_star,d),
                        (q_star+Q(1,1000),d)])
    result = {"schema":"X6_R117_TWO_PARAMETER_STRIP_EXACT_REPLAY_V1",
              "domain":{"q":[str(Q0),str(Q1)],
                        "delta":[str(-D),str(D)],
                        "port":"all >=10 by proof, exact replay <=28"},
              "case_count":len(samples),
              "total_nonzero_unoriented_checked":len(VECTORS)*len(samples),
              "results":[verify(q,d) for q,d in samples],
              "author_review":"NOT_INDEPENDENTLY_REVIEWED"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__ == "__main__":
    main()
