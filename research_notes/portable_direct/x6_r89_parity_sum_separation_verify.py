#!/usr/bin/env python3
"""Exact integer-domain checks for X6 R89 conditional BRC observer.
The unbounded-domain result is proved in the companion R89 paper; this tests q<=30.
"""
from fractions import Fraction
import json
from itertools import product

P = 30
WEIGHTS = [
    (1, 1, 1, 1), (1000, 1, 1000, 1), (1, 1000, 1, 1000),
    (8, 3, 8, 3), (50, 1, 51, 2), (1, 5, 1, 30),
    (1, 1, 11, 11), (1, 1, 12, 12), (7, 1, 1, 15),
    (13, 1, 1, 1), (20, 20, 1, 1), (1, 100, 100, 1),
]
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
S = (10, -5, 1)

def q(a):
    return max(sum(max(v, 0) for v in a), sum(max(-v, 0) for v in a))

def gaps(a):
    x, y, z = a
    u = x + 3*y + 6*z
    v = 3*x + 12*y + 30*z
    h = 7*x + 39*y + 126*z
    return (abs(u), abs(v), abs(h), abs(v-u), abs(h-u), abs(h-v))

def objective(g, w):
    return max(Fraction(gj, w[i]+w[j]) for gj,(i,j) in zip(g,PAIRS))

def main():
    diffs = [((x,y,z),q((x,y,z)),gaps((x,y,z)))
             for x,y,z in product(range(-P,P+1),repeat=3)
             if (x,y,z)>(0,0,0) and 0<q((x,y,z))<=P]
    assert len(diffs)==47305, len(diffs)
    assert gaps(S)==(1,0,1,1,0,1)
    rows=[]
    for w in WEIGHTS:
        d=min(w[0],w[2])+min(w[1],w[3])
        K=max(w[0]+w[2],w[1]+w[3])
        L=Fraction(6*d,K)
        fs=Fraction(1,d)
        minima={11:None,21:None,22:None,30:None}
        minimizers={p:[] for p in minima}
        for a,p,g in diffs:
            f=objective(g,w)
            if a==S:
                assert f==fs
                continue
            ratio=f/fs
            assert ratio >= (L if p<=21 else min(Fraction(2),L)),(w,a,p,ratio,L)
            for budget in minima:
                if p<=budget:
                    if minima[budget] is None or ratio<minima[budget]:
                        minima[budget]=ratio
                        minimizers[budget]=[a]
                    elif ratio==minima[budget]:
                        minimizers[budget].append(a)
        if K<6*d:
            assert minima[30]>1,(w,minima[30])
        if w[0]==w[2] and w[1]==w[3]:
            assert minima[22]==minima[30]==2
            assert minimizers[22]==minimizers[30]==[(20,-10,2)]
        rows.append({"weights":list(w),"kappa":str(Fraction(max(w),min(w))),
                     "d":d,"K":K,"lower_bound_nonmultiple":str(L),
                     "criterion_K_lt_6d":K<6*d,
                     "min_competitor_ratio_by_port":{str(k):str(v) for k,v in minima.items()},
                     "min_competitor_directions_at_30":[list(a) for a in minimizers[30]]})
    print(json.dumps({"schema":"X6_R89_EXACT_AUTHOR_CHECK_V1",
        "checked_unoriented_nonzero_directions_q_le_30":len(diffs),
        "weight_tuples_checked":len(WEIGHTS),
        "total_direction_weight_pairs":len(diffs)*len(WEIGHTS),
        "arithmetic":"Python fractions.Fraction exact",
        "assertions":"PASS",
        "universal_claim_basis":"symbolic divisibility proof",
        "results":rows},indent=2,ensure_ascii=False))

if __name__=="__main__":main()
