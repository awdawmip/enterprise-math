#!/usr/bin/env python3
"""Exact Q-rank proof for PREFIX-455. Python stdlib, no floating point."""
from itertools import product
from math import comb, gcd, prod, factorial

def walks(m):
    s={(0,)*6}
    for _ in range(m):
        nxt=set()
        for x in s:
            for i in range(6):
                for v in ((1,) if i==0 else (-1,1)):
                    y=list(x); y[i]+=v; nxt.add(tuple(y))
        s=nxt
    return sorted(s)

def support(q,d):
    m=d-1
    return sorted({(x[0]-j*q,)+x[1:]
                   for j in range(m//q+1) for x in walks(m-j*q)})

def powers(d):
    return [a for k in range(d+1)
            for a in product(range(k+1),repeat=6) if sum(a)==k]

def exact_rank(rows):
    piv={}; chosen=[]
    for k,values in enumerate(rows):
        row={i:int(v) for i,v in enumerate(values) if v}
        while row:
            j=min(row)
            if j not in piv:
                g=0
                for v in row.values():g=gcd(g,abs(v))
                sign=1 if row[j]>0 else -1
                piv[j]={i:sign*v//g for i,v in row.items()}
                chosen.append(k)
                break
            p=piv[j];a=row[j];b=p[j]
            row={i:b*row.get(i,0)-a*p.get(i,0) for i in row.keys()|p.keys()}
            row={i:v for i,v in row.items() if v}
            if row:
                g=0
                for v in row.values():g=gcd(g,abs(v))
                row={i:v//g for i,v in row.items()}
    return len(piv),chosen

def rank_certificate(q,d,expected_size,expected_rank,lower):
    s=support(q,d); ex=powers(d)
    assert len(s)==expected_size
    mat=[[prod(xi**a for xi,a in zip(x,e)) for e in ex] for x in s]
    r,_=exact_rank(mat)
    r2,basis=exact_rank([[row[i] for row in mat] for i in range(len(ex))])
    assert r==r2==expected_rank
    assert sum(sum(ex[i])<d for i in basis)==lower
    print('RANK',q,d,'N',q+d-2,'support',len(s),'rank',r,'defect',len(ex)-r,
          'top_degree_basis',r-lower)

def witness(q,d):
    x=[2*j-d for j in range(d+1)]
    w=[(-1)**(d-j)*comb(d,j) for j in range(d+1)]
    assert sum(w)==0
    for k in range(d):assert sum(v*t**k for v,t in zip(w,x))==0
    assert sum(v*t**d for v,t in zip(w,x))==2**d*factorial(d)
    # All other X6 coordinates are fixed: x1=q-2, x3=...=x6=0.
    print('WITNESS',q,d,'mass_each',2**(d-1),'degree_d_delta',2**d*factorial(d))

for args in [(2,4,253,169,84),(3,4,243,163,84),(4,4,242,162,84),
             (5,5,743,398,210)]:rank_certificate(*args)
for q,d in [(2,4),(3,4),(11,4),(2,5),(5,5),(7,6)]:witness(q,d)
print('PREFIX455 EXACT INTEGER CERTIFICATE PASS')
