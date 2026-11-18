#!/usr/bin/env python3
"""R749SUW: exact finite square-root optimizer for B=t^2+c Q=+1 two-Port observers.
Python stdlib, no floating point. Run: python R749SUW_FIXED_OFFSET_ROOT_CERT.py
"""
import json
from collections import Counter
from math import isqrt


def score(x, y):
    n = x * y
    return (n - 1) * (n - x - 1) * (n - y - 1)


def root_optimized(t, c):
    """All unordered score maximizers; valid for integer t>=3, c>=0.

    Returns (value, winning pairs, root-tests, feasible extra pairs).
    Input is B=t*t+c, and the square (t,t) is always a candidate.
    """
    assert isinstance(t, int) and t >= 3
    assert isinstance(c, int) and c >= 0
    best = score(t, t)
    winners = [(t, t)]
    root_tests = 0
    feasible = 0
    for j in range(1, c + 1):
        n = t * t + j
        for h in range(1, 3 * j):
            root_tests += 1
            s = 2 * t + h
            discr = 4 * t * h + h * h - 4 * j
            if discr < 0:
                continue
            r = isqrt(discr)
            if r * r != discr or (s - r) % 2:
                continue
            x, y = (s - r) // 2, (s + r) // 2
            if x < 2 or x > y or x * y != n or n - s < 1:
                continue
            feasible += 1
            z = score(x, y)
            if z > best:
                best, winners = z, [(x, y)]
            elif z == best:
                winners.append((x, y))
    assert root_tests == (3 * c * c + c) // 2
    return best, sorted(set(winners)), root_tests, feasible


def full_oracle(t, c):
    """Independently enumerate every allowed 2<=x<=y, xy<=t^2+c."""
    B = t*t+c
    best = -1
    winners = []
    for x in range(2, isqrt(B)+1):
        for y in range(x, B//x+1):
            if x*y-x-y < 1:
                continue
            z=score(x,y)
            if z>best:
                best,winners=z,[(x,y)]
            elif z==best:
                winners.append((x,y))
    return best,winners


def endpoint_oracle(t,c):
    """Independently examine all smaller divisors x and its maximal y=floor(B/x)."""
    B=t*t+c
    best=-1
    winners=[]
    for x in range(2,isqrt(B)+1):
        y=B//x
        if x>y or x*y-x-y<1:
            continue
        z=score(x,y)
        if z>best:
            best,winners=z,[(x,y)]
        elif z==best:
            winners.append((x,y))
    return best,winners


def F(n,s):
    return (n-1)*((n-1)**2-(n-1)*s+n)


def witness(t,c):
    v,w,rt,feasible=root_optimized(t,c)
    B=t*t+c
    return {"t":str(t),"c":c,"B":str(B),"score":str(v),
            "root_tests":rt,"feasible_extra":feasible,
            "winners":[{"x":str(x),"y":str(y),"gap":str(B-x*y)} for x,y in w]}


def check():
    # Exact independent complete domain: all factors, no use of the root cutoff.
    count_full=0
    for c in range(0,7):
        for t in range(3,56):
            value,pairs,*_=root_optimized(t,c)
            assert (value,pairs)==full_oracle(t,c),(t,c,"full")
            count_full+=1

    # Endpoint oracle searches all x independently, without the h/j cutoff.
    count_endpoint=0
    for c in range(0,10):
        for t in range(3,1803):
            value,pairs,*_=root_optimized(t,c)
            assert (value,pairs)==endpoint_oracle(t,c),(t,c,"endpoint")
            count_endpoint+=1

    # Extra large continuous fixed-offset slice; this checks all 15 candidate roots.
    c3_counts=Counter()
    c3_ties=0
    for t in range(3,50001):
        value,pairs,root_tests,*_=root_optimized(t,3)
        assert root_tests==15
        for x,y in pairs:
            assert 2<=x<=y and x*y<=t*t+3 and x*y-x-y>=1
            assert score(x,y)==value
            c3_counts[str(t*t+3-x*y)]+=1
        if len(pairs)>1:
            c3_ties+=1

    # Check the exact cutoff polynomial identity; proof is symbolic in the paper.
    cutoff_checks=0
    for t in range(3,503):
        for j in range(1,51):
            p=(4*t**3-2*t*t-4*t+1)+j*(3*t*t+2*t-4)+2*j*j
            assert p>0
            assert F(t*t,2*t)-F(t*t+j,2*t+3*j)==j*p
            cutoff_checks+=1

    # Infinite zero-gap witness family (tested here in a finite independent range).
    family_tests=0
    for c in range(1,16):
        for k in range(1,101):
            t=k*(k+1)+c
            x,y=t-k,t+k+1
            best,winners,*_=root_optimized(t,c)
            assert x*y==t*t+c and (x,y) in winners and winners==[(x,y)]
            assert score(x,y)==best
            family_tests+=1

    large=[witness(t,c) for t,c in [(10**6,3),(10**12,3),(10**24,3),
                                  (10**12,8),(10**12,20),(10**24,25)]]
    return {"result":"PASS","model":"frozen WBRC two-Port auxiliary Q=+1 integer observer",
            "statement":"all integer t>=3, c>=0; all unordered optimizers via <=(3c^2+c)/2 exact root tests",
            "method":"integer discriminant roots, candidate complete cutoff",
            "full_oracle":"t=3..55, c=0..6", "full_domains":count_full,
            "endpoint_oracle":"t=3..1802, c=0..9", "endpoint_domains":count_endpoint,
            "c3_continuous":"t=3..50000", "c3_gap_counts_with_multiplicity":dict(sorted(c3_counts.items())),
            "c3_tie_t_count":c3_ties, "cutoff_polynomial_checks":cutoff_checks,
            "zero_gap_family_checks":family_tests,
            "large_instances":large,"arithmetic":"exact Python integers, decimal strings for large values",
            "evidence_status":"AUTHOR_EXACT_NOT_REVIEWED",
            "frozen_input":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md"}


if __name__=="__main__":
    output=check()
    path="R749SUW_FIXED_OFFSET_ROOT_RESULTS.json"
    with open(path,"w",encoding="utf-8") as f:
        json.dump(output,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write("\n")
    print(output["result"], "full",output["full_domains"], "endpoint",output["endpoint_domains"],
          "cutoff",output["cutoff_polynomial_checks"],
          "c3_gaps",output["c3_gap_counts_with_multiplicity"])
