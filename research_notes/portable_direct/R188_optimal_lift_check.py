#!/usr/bin/env python3
"""R188: exact finite check of optimal-tree lifting's adjacency lemma."""
from itertools import permutations
import json, math

def states(k):
    return (p for r in range(k+1) for p in permutations(range(k),r))

def oracle(s,a,b=None):
    U={a} if b is None else {a,b}
    return next((x for x in reversed(s) if x in U),None)

def recover(s,k):
    raw={};calls=0
    def less(x,y):
        nonlocal calls
        z=oracle(s,x,y)
        raw[frozenset((x,y))]=z
        calls+=1
        return x<y if z is None else z==y
    def sort(xs):
        if len(xs)<2:return xs
        m=len(xs)//2;u=sort(xs[:m]);v=sort(xs[m:])
        out=[];i=j=0
        while i<len(u) and j<len(v):
            if less(u[i],v[j]):
                out.append(u[i]);i+=1
            else:
                out.append(v[j]);j+=1
        return out+u[i:]+v[j:]
    a=sort(list(range(k)))
    assert all(frozenset((x,y)) in raw for x,y in zip(a,a[1:]))
    if oracle(s,a[0]) is not None:
        absent=0
    else:
        absent=1
        while absent<k and raw[frozenset((a[absent-1],a[absent]))] is None:
            absent+=1
    return tuple(a[absent:]),calls

def verify():
    rows=[]
    for k in range(1,8):
        count=0;maximum=0
        for state in states(k):
            got,n=recover(state,k)
            assert got==state,(k,state,got)
            count+=1;maximum=max(maximum,n)
        depth=math.ceil(math.log2(k)) if k>1 else 0
        mergesort_bound=k*depth-2**depth+1
        assert maximum<=mergesort_bound
        rows.append({"k":k,"states":count,"maximum_sort_pair_calls":maximum,
                     "mergesort_bound":mergesort_bound,"singleton_calls":1,
                     "extra_pair_calls_after_sort":0,"adjacent_witnesses":"ALL"})
    print(json.dumps({"schema":"EM_R188_CHECK_V1","cases":rows,
        "total_states":sum(x["states"] for x in rows),"result":"PASS"},
        indent=2))

if __name__=="__main__":verify()
