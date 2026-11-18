#!/usr/bin/env python3
"""R749SUR: exact candidate-root filter for the two-Port closest-divisor maximum.
Integer arithmetic only. Uses the R749SUO Q=+1 and R749SUP near-product facts.
"""
import json
from math import isqrt


def near_product(m):
    t = isqrt(m + 1)
    k = m + 1 - t*t
    j = 1 if k <= t else 2
    z = 0
    while z*(z+j) < j*t-k:
        z += 1
    x, y = t-z, t+z+j
    assert x >= 2 and x*y <= m+1
    return x, y, t, z


def value(x, y):
    n = x*y
    return (n-1)*(n-x-1)*(n-y-1)


def filtered_optimizer(m):
    assert m >= 9999
    b = m+1
    x0,y0,t,z = near_product(m)
    witness = value(x0,y0)
    k = m*(m*m+b)-witness
    def excess(x):
        return m*m*(x*x+b)-k*x
    assert excess(x0) <= 0
    lo,hi = 2,x0
    while lo < hi:
        mid = (lo+hi)//2
        if excess(mid) <= 0:
            hi=mid
        else:
            lo=mid+1
    xmin=lo
    assert excess(xmin) <= 0 and (xmin==2 or excess(xmin-1)>0)
    best=-1
    opt=[]
    for x in range(xmin,t+1):
        y=b//x
        if y < x or x*y-x-y < 1:
            continue
        score=value(x,y)
        if score>best:
            best=score
            opt=[(x,y)]
        elif score==best:
            opt.append((x,y))
    assert best >= witness
    labels=sum(2 if x==y else 4 for x,y in opt)
    return best,labels,opt,dict(candidate_x_count=t-xmin+1,x_min=xmin,t=t,
        witness_x=x0,witness_y=y0,witness_n=x0*y0,near_z=z)


def independent_full_x(m):
    """Independent exact enumeration of every possible smaller Q=1 factor."""
    b=m+1
    top=isqrt(b)
    best=-1
    opt=[]
    for x in range(2,top+1):
        y=b//x
        if x*y-x-y<1:
            continue
        score=value(x,y)
        if score>best:
            best=score
            opt=[(x,y)]
        elif score==best:
            opt.append((x,y))
    return best,sum(2 if x==y else 4 for x,y in opt),opt


def verify():
    tested=0
    max_w=0
    for m in range(9999,25001):
        fast=filtered_optimizer(m)
        slow=independent_full_x(m)
        assert fast[:3]==slow,(m,fast[:3],slow)
        max_w=max(max_w,fast[3]["candidate_x_count"])
        tested+=1
    cases={}
    samples=[9999,10000,25000,100000,1000000,100000000,10**12]
    expected={9999:979804019799,25000:15420641299674,
              100000:993550256897434,1000000:997998004001997999,
              100000000:999799980004000199979999}
    for m in samples:
        fast=filtered_optimizer(m)
        slow=independent_full_x(m)
        assert fast[:3]==slow,(m,fast[:3],slow)
        if m in expected: assert fast[0]==expected[m]
        cases[str(m)]={"score":str(fast[0]),"named_optima":fast[1],
            "factor_pairs":[list(v) for v in fast[2]],**fast[3]}
    return {"status":"PASS","id":"R749SUR_V1","model":"pinned WBRC-T30-T32 auxiliary named 2-Port feedback",
         "all_m_crosscheck":{"from":9999,"through":25000,"count":tested,
           "max_filtered_candidate_count":max_w},
         "extra_independent_full_x_cases":len(samples),"examples":cases,
         "verification":"independent complete x scan; exact integer polynomial cutoff; no floating point",
         "limits":"conditional on the cited prior R749SUO Q=1 theorem; finite checks are not proof of its global assertion"}


if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,sort_keys=True,indent=2))
