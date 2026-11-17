#!/usr/bin/env python3
"""PREFIX-870: exact certificate for a named-source auxiliary BRC observer."""
import json
from math import gcd, isqrt

def h(g):
    r=1
    for d in range(1,2*g+1):
        r=2*r%g
        if r==1 or r==g-1: return d
    raise AssertionError("odd half-order failed")

def lower(p):
    T=(1<<p)*(p+1)
    B=1
    while ((1<<B)-1)**2<T: B+=1
    assert ((1<<(B-1))-1)**2<T
    return B

def row(p):
    N=1<<p
    g=next(g for g in range(2*p+1,1001,2) if h(g)>=p)
    a=isqrt((N+g-1)//g)
    if a%2==0: a+=1
    while g*a*(a+2)<N: a+=2
    b=a+2
    q1,q2=g*a,g*b
    D=[0]+[s*(1<<i) for i in range(p) for s in (-1,1)]
    assert len(set(d%g for d in D))==2*p+1
    assert gcd(a,b)==1 and gcd(q1,q2)==g and q1%2==q2%2==1
    assert g*a*b>=N and h(g)>=p
    B=max(q1.bit_length(),q2.bit_length()); L=lower(p)
    assert B-L==(0 if p%2 else 1)
    return dict(p=p,L=L,B=B,g=g,h=h(g),a=a,b=b,q1=q1,q2=q2,lcm=g*a*b)

def main():
    rows=[row(p) for p in range(32,56)]
    q1,q2=11,33
    seen=set()
    for u in range(32):
        seen.add((u%q1,u%q2))
        for i in range(5):
            seen.add((u%q1,(u^(1<<i))%q2))
    assert len(seen)==192
    M=(1<<19)-1
    assert M*M==274876858369 and M*M<65*(1<<32)==279172874240
    assert rows[0]["B"]==20
    out=dict(schema="PREFIX870_R6_EXACT_INTEGER_CERTIFICATE_V1",
             frozen_scientific_input="f42f2906d77f24085c123f3ccfe9667d41caa96d",
             model="auxiliary named-binary BRC, fixed two odd modular ports, full ordered transition",
             p_range=[32,55],rows=rows,
             exact_global_p=list(range(33,56,2)),
             gap_at_most_one_p=list(range(32,56,2)),
             p32_class_optimum=20, p32_global_bounds=[19,20],
             p5_sanity_transitions=len(seen),
             validation="ALL_EXACT_ASSERTIONS_PASSED")
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=="__main__":
    main()
