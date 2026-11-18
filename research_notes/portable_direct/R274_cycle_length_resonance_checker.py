#!/usr/bin/env python3
"""R274 exact p=13 directed BRC Port cycle certificate; stdlib only."""
from fractions import Fraction as F
import json, hashlib
from pathlib import Path
p=13

def vpint(x):
    assert isinstance(x,int) and x!=0
    k=0
    while x%p==0:
        k+=1;x//=p
    return k

def mul(A,B):
    d=len(A)
    return [[sum(A[i][h]*B[h][j] for h in range(d)) for j in range(d)]
            for i in range(d)]

def ident(d):
    return [[F(int(i==j)) for j in range(d)] for i in range(d)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def cycle(d,w,omitted=None):
    W=[[F(0) for _ in range(d)] for _ in range(d)]
    for i in range(d):
        if i!=omitted:
            W[i][(i+1)%d]=w
    return W

identity_checks=0
for t in (1,2,3):
    w=F(1,1+p**t)
    for d in range(2,7):
        W=cycle(d,w)
        C=ident(d)
        T=ident(d)
        for _ in range(1,d):
            T=mul(T,W)
            C=add(C,T)
        q=w**d
        S=[[x/(1-q) for x in row] for row in C]
        A=[[F(int(i==j))-W[i][j] for j in range(d)] for i in range(d)]
        assert mul(A,S)==ident(d)
        assert all(S[i][i]==1/(1-q) for i in range(d))
        for missing in range(d):
            V=cycle(d,w,omitted=missing)
            T=ident(d)
            acc=ident(d)
            for _ in range(1,d):
                T=mul(T,V)
                acc=add(acc,T)
            assert mul(T,V)==[[F(0) for _ in range(d)] for _ in range(d)]
            assert all(acc[i][i]==1 for i in range(d))
        identity_checks+=1

results=[]
for t in range(1,5):
    P=p**t
    for d in sorted(set(list(range(2,41))+[169,2197])):
        D=(1+P)**d-1
        depth=vpint(D)
        assert depth==t+vpint(d)
        results.append({"t":t,"cycle_length":d,"v13_length":vpint(d),
                        "v13_denominator":depth,"v13_observer_increment":-depth})
assert len(results)==4*41
payload={"schema":"EM_R274_K_CYCLE_PORT_RESONANCE_V1",
         "tested_t_range":[1,4],"cycle_lengths":"2..40, 169, 2197",
         "finite_cases":len(results),
         "matrix_identity_checks":identity_checks,"small_cycle_dim_range":[2,6],
         "prime":13,"arithmetic":"exact integer and Fraction",
         "all_checks":"PASS","results":results}
s=json.dumps(payload,sort_keys=True,indent=2)+"\n"
Path(__file__).with_name("R274_verification.json").write_text(s)
print("PASS",len(results),"matrix",identity_checks,
      "SHA256",hashlib.sha256(s.encode()).hexdigest())
