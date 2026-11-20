#!/usr/bin/env python3
"""PREFIX-954 independent full two-core named-XOR moment validation."""
import json
from PREFIX954_R6_TOP_BIT_SWEEP import floor_sum, lower_top, top_top

def lower_lower(p,k,l):
    H=1<<(p-1); N=H//2
    total=N*(p-2)*(p-3)//4
    for j in range(1,p-1):
        mod=1<<(j+1)
        q=(l*pow(k,-1,mod))%mod
        h=1<<(j-1)
        C=h-floor_sum(h,1<<j,2*q,q)+2*floor_sum(h,mod,2*q,q)
        total+=(N//(1<<j))*C
    return total

def exact_full(p,k,l):
    H=1<<(p-1); M=2*H; a0=H+1
    total=(lower_lower(p,k,l)+lower_top(p,k,l)
           +lower_top(p,l,k)+top_top(p,k,l))
    z_k=p-(k*a0%M).bit_count()
    z_l=p-(l*a0%M).bit_count()
    total+=(2*z_l if k>=3 else 0)+(2*z_k if l>=3 else 0)
    total+=4 if k>=3 and l>=3 else 0
    return total

def raw_witness_count(p,k,a):
    """Count solutions of (ka XOR 2^j)-2^i=t*a for t>=1 without classifying them."""
    count=0
    v=k*a
    for j in range(p):
        flipped=v^(1<<j)
        for i in range(p):
            d=flipped-(1<<i)
            if d>0 and d%a==0:
                count+=1
    return count

def direct_all(p,k,l):
    H=1<<(p-1); total=0
    for a in range(H+1,2*H,2):
        total+=raw_witness_count(p,k,a)*raw_witness_count(p,l,a)
    return total

def verify():
    checks=0
    for p in range(4,9):
        H=1<<(p-1)
        for k in range(1,H,2):
            for l in range(1,H,2):
                formula=exact_full(p,k,l)
                brute=direct_all(p,k,l)
                assert formula==brute,(p,k,l,formula,brute)
                assert formula==exact_full(p,l,k),(p,k,l)
                checks+=1
    assert checks==5456
    assert lower_lower(19,21,23)==9448558
    answer=exact_full(19,21,23)
    assert answer==10541801
    assert answer==exact_full(19,23,21)
    return {
        "scope":"auxiliary named XOR observer",
        "frozen_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "p4_to_p8_all_ordered_pairs":checks,
        "method":"direct original i,j,t enumeration versus compressed integer-only formula",
        "p19_21_23_lower_lower":9448558,
        "p19_21_23_full_named_moment":answer,
        "status":"PASS"
    }

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
