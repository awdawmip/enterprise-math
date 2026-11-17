#!/usr/bin/env python3
"""R762DO exact named-branch BRC diagonal observer verifier.

Scope: six named nonnegative integer branches, C_Q endpoint, no native event admission.
"""
import json
from math import gcd
from functools import reduce

BRANCHES = [(0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1)]

def conv(a, shifts, Q):
    b = [0]*Q
    for u, weight in enumerate(a):
        if weight:
            for offset, multiplicity in shifts:
                b[(u+offset)%Q] += multiplicity*weight
    return b

def v3(n):
    if n == 0: return None
    ans=0
    while n % 3 == 0:
        ans+=1
        n//=3
    return ans

def prediction(Q,n):
    d=Q//3
    if n == 0: return 0
    if d == 1: return n-1
    m,r = divmod(n,d)
    if m == 0: return 0
    return m-1+int(2*r >= d)

def run():
    results=[]
    total=0
    for a,end in [(1,36),(2,100),(3,130),(4,165),(5,180)]:
        Q=3**a
        d=Q//3
        gamma=[0]*Q; gamma[0]=1
        f=[0]*Q; f[0]=1
        diag={}
        for triple in BRANCHES:
            residue=sum(triple)%Q
            diag[residue]=diag.get(residue,0)+1
        shifts=sorted(diag.items())
        # Independently check the named-branch diagonal multiplicities.
        expected={}
        for k,mul in [(0,1),(1,2),(2,2),(3,1)]:
            expected[k%Q]=expected.get(k%Q,0)+mul
        assert diag == expected
        samples=[]
        for n in range(1,end+1):
            gamma=conv(gamma,[(0,1),(1,1),(2,1)],Q)
            f=conv(f,shifts,Q)
            g=reduce(gcd,gamma)
            gf=reduce(gcd,f)
            target=prediction(Q,n)
            assert v3(g)==target,(Q,n,g,target)
            assert v3(gf)==target,(Q,n,gf,target)
            if n <= 12:
                two=[0]*Q; two[0]=1
                for _ in range(n):
                    two=conv(two,[(0,1),(1,1)],Q)
                reconstructed=[0]*Q
                for i,weight in enumerate(gamma):
                    if weight:
                        for j,w in enumerate(two):
                            if w:
                                reconstructed[(i+j)%Q]+=weight*w
                assert reconstructed==f,(Q,n,"factorization")
            if n in (1,2,d,d+(d-1)//2,d+(d+1)//2,2*d,3*d,4*d,5*d,end):
                samples.append({"n":n,"valuation":v3(gf),"content":str(gf) if n<=30 else None})
            total+=1
        if a>=2: assert gf%2==1
        results.append({"Q":Q,"range":[1,end],"selected":samples,"last_valuation":v3(gf)})
    return {"schema":"R762DO_BRC_DIAGONAL_VERIFY_V1",
            "date":"2026-11-18","task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
            "carrier":"six named positive integer BRC branches",
            "observer":"diagonal additive endpoint in C_Q",
            "independent_review":"NOT_REVIEWED",
            "configurations":total,"results":results,"status":"PASS"}

if __name__ == "__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
