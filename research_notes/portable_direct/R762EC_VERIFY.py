#!/usr/bin/env python3
"""R762EC complete Q=27 six-branch BRC cyclotomic valuation certificate.
Exact Z[zeta_27] arithmetic in its 18-element integral power basis.
No floating point, numerical roots, or external packages.
"""
from collections import Counter
from itertools import product
from hashlib import sha256
import json

Q=27; PHI=18
BRANCHES=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
# Phi_27(X)=X^18+X^9+1; reduce zeta^e in power basis.
RED=[]
for e in range(Q):
    v=[0]*PHI
    if e<PHI: v[e]=1
    else: v[e-18]=-1;v[e-9]=-1
    RED.append(tuple(v))
# T(X)=(Phi_27(X)-3)/(X-1): (zeta-1)*T(zeta)=-3.
T=(2,)*9+(1,)*9

def repr_sum(exps):
    a=[0]*PHI
    for e in exps:
        for t,v in enumerate(RED[e%Q]): a[t]+=v
    return a

def mul_reduced(a,b):
    out=[0]*PHI
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if not y:continue
            for t,v in enumerate(RED[(i+j)%Q]):out[t]+=x*y*v
    return out

def mul_pi(a):
    out=[0]*PHI
    for i,x in enumerate(a):
        for t,v in enumerate(RED[(i+1)%Q]):out[t]+=x*v
        out[i]-=x
    return out

def divide_pi(a):
    b=mul_reduced(a,T)
    assert all(x%3==0 for x in b)
    q=[-x//3 for x in b]
    assert mul_pi(q)==a,(a,q)
    return q

def valuation(a):
    if not any(a):return 'infinity'
    n=0
    while sum(a)%3==0: # (pi) is kernel of evaluation zeta->1 modulo 3
        a=divide_pi(a)
        n+=1
        assert n<=60
    return n

def main():
    assert mul_pi([1]+[0]*(PHI-1))==[-1,1]+[0]*(PHI-2)
    hist=Counter();witness={};data=bytearray()
    for i,j,k in product(range(Q),repeat=3):
        e=[(u*i+v*j+w*k)%Q for u,v,w in BRANCHES]
        val=valuation(repr_sum(e))
        hist[str(val)]+=1
        witness.setdefault(str(val),[i,j,k]);data.append(255 if val=='infinity' else val)
    expected={'2':13122,'4':3888,'6':1782,'10':432,'12':144,'18':111,'infinity':204}
    assert dict(hist)==expected,(hist,expected)
    assert sum(hist.values())==Q**3
    assert hist['18']+hist['infinity']==315
    proof={
     'record':'R762EC_Q27_COMPLETE_CYCLOTOMIC_SPECTRUM',
     'date':'2026-11-18',
     'task_id':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
     'q':27,
     'model':'six named positive BRC branches P=1+X+Z+XY+YZ+XYZ',
     'integral_basis':'Z[zeta_27], power basis length 18, Phi_27(X)=X^18+X^9+1',
     'exact_division':'(zeta-1)*T(zeta)=-3; T(X)=2(1+...+X^8)+(X^9+...+X^17); divide_pi=-T/3, with integer coefficient and reverse-multiplication assertions',
     'pi_divisible_iff':'sum of power basis coordinates divisible by 3',
     'coverage':'all 27^3=19683 triples; all exact pi-division steps until first nondivisible element, or exactly zero',
     'histogram':expected,
     'witnesses':witness,
     'valuation_bytes_encoding':'i,j,k lexical order; one byte valuation integer; 255 indicates exact zero eigenvalue',
     'valuation_table_sha256':sha256(data).hexdigest(),
     'status':'PASS',
     'scientific_scope':'complete finite Q=27 cyclotomic valuation distribution for candidate positive BRC terminal observer; does not prove all Q or native signed triadic event.'
    }
    print(json.dumps(proof,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
