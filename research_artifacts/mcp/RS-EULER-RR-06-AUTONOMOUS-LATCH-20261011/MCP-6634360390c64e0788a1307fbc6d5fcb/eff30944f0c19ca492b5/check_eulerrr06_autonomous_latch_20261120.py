#!/usr/bin/env python3
"""Exact finite-state checks for declared Euler RR-06 controller extension."""
from itertools import product
Z3 = range(3)
for j,a in product(Z3, repeat=2):
    outputs=[]
    for r,b in product(Z3,range(2)):
        outputs.append(((r+j-a)%3,1) if b==0 else (r,1))
    assert len(outputs)==6 and len(set(outputs))==3
checks=0
for m in range(2,10):
    def F(s):
        j,a,r,c=s
        return (j,a,(r+j-a)%3 if c==0 else r,(c+1)%m)
    def inv(s):
        j,a,r,cp=s
        c=(cp-1)%m
        return (j,a,(r-j+a)%3 if c==0 else r,c)
    S=list(product(Z3,Z3,Z3,range(m)))
    assert len({F(s) for s in S})==len(S)
    for s in S:
        assert inv(F(s))==s
        x=s
        for _ in range(3*m):
            x=F(x)
        assert x==s
        checks+=2
    for j,a in product(Z3,repeat=2):
        s=F((j,a,a,0))
        assert s[2]==j and s[3]==1
        for _ in range(m-1):
            prev=s[2]
            s=F(s)
            assert s[2]==prev
        assert s[3]==0
        checks+=m
print({"tested_m":list(range(2,10)), "assertion_groups":checks, "status":"PASS"})
