#!/usr/bin/env python3
"""PREFIX-867 independent p=19 lower-bound audit and all eight CRT upper witnesses.
Exact integers only. This implementation does not import or invoke the C++ checker.
"""
import json
from math import gcd

WITNESSES = (
    (19, 47, 105, 107, 13),
    (20, 47, 149, 151, 13),
    (21, 47, 211, 213, 14),
    (22, 47, 297, 301, 14),
    (23, 47, 421, 425, 15),
    (24, 53, 561, 565, 15),
    (25, 53, 795, 797, 16),
    (26, 53, 1125, 1127, 16),
)

def h(q):
    z = 2 % q
    for d in range(1, q+1):
        if z in (1, q-1):
            return d
        z = (z * 2) % q
    raise ValueError(q)

def check_upper():
    rows = []
    for p,g,a,b,width in WITNESSES:
        assert gcd(a,b)==1 and a%2==b%2==g%2==1
        q1,q2=g*a,g*b
        assert h(g)>=p and g*a*b>=1<<p
        assert max(q1.bit_length(),q2.bit_length())==width
        rows.append((p,q1,q2,h(g),g*a*b))
    return rows

def check_p19():
    p,b=19,12
    N,M,T=1<<p,(1<<b)-1,(1<<p)*(p+1)
    safe=[q for q in range(3,M+1,2) if h(q)>=p]
    first_count=pair_count=survivors=0
    for q1 in safe:
        old=list(range(0,N,q1))
        size=len(old)*(p+1)
        if q1*M<T or size>M:
            continue
        valid=[q2 for q2 in safe if
               q1*q2>=T and q1*q2//gcd(q1,q2)>=N and q2>=size]
        if not valid:
            continue
        first_count+=1
        pair_count+=len(valid)
        vals=[v for u in old for v in
              (u,) + tuple(u^(1<<i) for i in range(p))]
        for q2 in valid:
            seen=set()
            for v in vals:
                z=v%q2
                if z in seen:
                    break
                seen.add(z)
            else:
                survivors+=1
    assert (len(safe),first_count,pair_count,survivors)==(1957,755,322946,0)
    return {"safe_moduli":len(safe),
            "eligible_first_moduli":first_count,
            "eligible_pairs":pair_count,
            "survivors":survivors}

if __name__=="__main__":
    result={"schema":"PREFIX867_INDEPENDENT_PYTHON_V1",
            "p19":check_p19(),
            "crt_witnesses":check_upper(),
            "status":"ALL_EXACT_ASSERTIONS_PASSED"}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
