#!/usr/bin/env python3
"""R104 exact finite-domain checker (not a proof of the unbounded theorem)."""
import json
from itertools import product
from math import lcm

WEIGHTS = [
    (1, 1, 1, 1), (1, 1, 5, 23), (1, 1, 11, 11),
    (11, 11, 11, 11), (12, 1, 1, 1), (39, 1, 1, 1),
    (2, 4, 7, 3), (4, 2, 7, 1), (6, 1, 2, 11),
    (3, 8, 5, 2), (1, 9, 12, 3), (8, 3, 1, 7),
    (9, 1, 59, 41)
]
PORTS = (11, 17, 27, 28, 39, 40)


def q(a):
    return max(sum(max(t, 0) for t in a), sum(max(-t, 0) for t in a))


def canon(a):
    return a if next(t for t in a if t) > 0 else tuple(-t for t in a)


def moments(a):
    x, y, z = a
    return (x + 3*y + 6*z, 3*x + 12*y + 30*z, 7*x + 39*y + 126*z)


def score_numerator(a, ws, L):
    A,B,C,D=ws
    u,v,h = moments(a)
    return max(abs(t) * (L // den) for t,den in zip(
        (u,v,h,v-u,h-u,h-v),
        (A+B,A+C,A+D,B+C,B+D,C+D)
    ))


def bounding_box(ws):
    A,B,C,D=ws
    # E_s=max(1/(A+B),1/(A+D),1/(B+C),1/(C+D)) exactly.
    from fractions import Fraction
    E=max(Fraction(1,t) for t in (A+B,A+D,B+C,C+D))
    U=int(E*(A+B)); V=int(E*(A+C)); H=int(E*(A+D))
    return U,V,H


def finite_box(ws):
    U,V,H=bounding_box(ws)
    result=set()
    for u in range(-U,U+1):
        for v in range(-V,V+1):
            if v % 3: continue
            for h in range(-H,H+1):
                if (h-u)%6 or (h-u-6*v)%12: continue
                x2=h+19*u-8*v
                y3=-h-14*u+7*v
                z12=h+11*u-6*v
                if x2%2 or y3%3 or z12%12: continue
                a=(x2//2,y3//3,z12//12)
                if a!=(0,0,0): result.add(canon(a))
    return result


def brute_directions(maxp):
    result=[]
    for x in range(-maxp,maxp+1):
        for y in range(-maxp,maxp+1):
            for z in range(-maxp,maxp+1):
                if x>0 or (x==0 and y>0) or (x==0 and y==0 and z>0):
                    a=(x,y,z)
                    if q(a)<=maxp: result.append((a,q(a)))
    return result


def main():
    source=brute_directions(max(PORTS))
    assert len(source)==110740
    summary=[]
    for w in WEIGHTS:
        A,B,C,D=w
        L=lcm(A+B,A+C,A+D,B+C,B+D,C+D)
        box=finite_box(w)
        box_scores={a:score_numerator(a,w,L) for a in box}
        for p in PORTS:
            b={a:v for a,v in box_scores.items() if q(a)<=p}
            assert b
            val=min(b.values())
            minimizers={a for a,v in b.items() if v==val}
            brute_min=min(score_numerator(a,w,L) for a,qa in source if qa<=p)
            brute_set={a for a,qa in source if qa<=p and score_numerator(a,w,L)==brute_min}
            assert val==brute_min and minimizers==brute_set, (w,p)
            # Third-residue separation: every vector with F<3*eta/2
            near={a for a,qa in source if qa<=p and 2*score_numerator(a,w,L)<3*val}
            classes={tuple(t%3 for t in a) for a in near}
            pairs={min(res,tuple((-t)%3 for t in res)) for res in classes}
            assert len(near)==len(pairs)<=13,(w,p,len(near))
            if w==(9,1,59,41) and p==40:
                assert val*10==L and len(near)==12 and len(minimizers)==3
            summary.append({"weights":w,"p":p,"minimum_numerator":val,
                            "common_denominator":L,"minimizers":len(minimizers),
                            "sub_1_5_minimum_directions":len(near),
                            "box_candidates":len(box)})
    witness=next(a for a,qa in source if a==(10,-5,1))
    assert q(witness)==11
    print(json.dumps({"schema":"X6_R104_AUTHOR_EXACT_CHECK_V1",
                      "mode":"integer_exact", "port_limit":40,
                      "unoriented_vectors":len(source),
                      "weight_samples":len(WEIGHTS),"budgets_per_weight":len(PORTS),
                      "cases":len(summary),"maximum_minimizer_count":max(x["minimizers"] for x in summary),
                      "maximum_sub_1_5_count":max(x["sub_1_5_minimum_directions"] for x in summary),
                      "all_assertions":"PASS","detail":summary},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
