#!/usr/bin/env python3
"""PREFIX-757 independent small-layer exact validation and a soft-mask example.
Uses published frozen integer width semantics, only for n=1..25.
The all-orders theorem is analytic; this checker is evidence, not its proof.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb
import json

W = 1 << 18
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k) > W**n

@lru_cache(None)
def wide(n,k):
    if k > n//2: return wide(n,n-k)
    mid = k*W//n
    assert inside(n,k,mid), (n,k,"midpoint-not-inside")
    if k==0: lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(n,k,x): b=x
            else: a=x
        lo,hi=a,b
    a,b=mid,W
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x): a=x
        else: b=x
    if 4*(a-hi)>W: return True
    if 4*(b-lo)<W: return False
    raise ValueError(("undecidable-width",n,k))

mask_rows={n:[k for k in range(n+1) if wide(n,k)] for n in range(1,26)}
assert all(mask_rows[n] == list(range(n+1)) for n in range(1,25))
assert mask_rows[25] == list(range(1,25))
a={0:1}
for n in range(1,26):
    a={k:a.get(k,0)+a.get(k-1,0) for k in mask_rows[n]}
assert all(a[k]==comb(25,k) for k in range(1,25))
def S25(p):
    return sum(Fraction(a.get(k,0))*p**k*(1-p)**(25-k) for k in range(26))
p1,p2=Fraction(0),Fraction(1,4)
delta=S25(p2)-S25(p1)
assert delta==Fraction(4**25-1-3**25,4**25)>0

# Rational soft masks with non-binary retentions; illustrative only.
soft={
    1:[Fraction(1,2),Fraction(1,2)],
    2:[Fraction(1,4),Fraction(3,4),Fraction(1,4)],
    3:[Fraction(0),Fraction(1,2),Fraction(1,2),Fraction(0)],
    4:[Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(2,5),Fraction(1,5)]
}
bprev=[Fraction(1)]
for n,weights in soft.items():
    assert all(weights[k]==weights[n-k] for k in range(n+1))
    assert all(weights[k+1]>=weights[k] for k in range(n//2))
    nxt=[]
    for k in range(n+1):
        x=bprev[k] if k<len(bprev) else Fraction(0)
        y=bprev[k-1] if k>0 else Fraction(0)
        nxt.append(weights[k]*(Fraction(n-k,n)*x+Fraction(k,n)*y))
    assert all(nxt[k]==nxt[n-k] for k in range(n+1))
    assert all(nxt[k+1]>=nxt[k] for k in range(n//2))
    bprev=nxt

out={
    "schema":"PREFIX757_R6_SOFT_MASK_STRICT_ORDER_V1",
    "scientific_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "scope":"n=1..25 exact integer width predicate; n=1..4 example of rational soft masks",
    "arithmetic":"Python arbitrary-precision integers and fractions",
    "mask_memberships_checked":sum(n+1 for n in range(1,26)),
    "rows_1_to_24":"all k accepted",
    "row_25":"k=1..24 accepted; k=0,25 rejected",
    "row_25_survivor_counts":"a[25,k]=binom(25,k) for 1<=k<=24; endpoints zero",
    "S25_formula":"1-p**25-(1-p)**25",
    "sample_p1":"0",
    "sample_p2":"1/4",
    "sample_survival_gap_exact":str(delta),
    "soft_mask_example_rows":len(soft),
    "soft_mask_example_status":"exact rational centrally nondecreasing normalized coefficients",
    "status":"AUTHOR_EXACT_FINITE_CHECK; GENERAL_THEOREM_ANALYTIC_UNREVIEWED",
    "result":"PASS"
}
print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
print("ALL_CHECKS_PASS PREFIX757-R6")
