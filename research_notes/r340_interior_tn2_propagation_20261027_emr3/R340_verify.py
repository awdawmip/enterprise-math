#!/usr/bin/env python3
"""R340 exact full-signed BRC recurrence and interior-minor test; integers only."""
import argparse, hashlib, json
from math import comb
from pathlib import Path

def c(n,k): return comb(n,k) if 0 <= k <= n else 0

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    while len(z)>1 and not z[-1]: z.pop()
    return z

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w: z[i+j]+=v*w
    while len(z)>1 and not z[-1]: z.pop()
    return z

def term(n,v,shift):
    return [0]*shift+[v*c(n,j) for j in range(n+1)] if n>=0 and v else [0]

def kernel(i):
    d=(-c(4,i)+c(2,i-1),c(5,i-1)-c(5,i-2),c(7,i-2),-c(9,i-3))
    out=[0]
    for h,v in enumerate(d,1): out=add(out,term(i+1-h,-v,i-1))
    return out

def forcing(s):
    out=[0]
    for v,n in ((-c(3,s-1),s),(-c(6,s-1),s-1),(c(8,s-2),s-2)):
        out=add(out,term(n,v,s))
    return out

def run(n):
    K=[None]+[kernel(i) for i in range(1,13)]
    J=[None]+[forcing(s) for s in range(1,11)]
    B=[[1,1]]
    for s in range(1,2*n+3):
        row=J[s][:] if s<=10 else [0]
        for i in range(1,min(12,s)+1): row=add(row,mul(K[i],B[s-i]))
        B.append(row)
    D=[]
    for q in range(n+2):
        z=[2**(q-v)*B[q+v][q] for v in range(q+1)]
        d=[]
        while z:
            d.append(z[0]);z=[z[i+1]-z[i] for i in range(len(z)-1)]
        D.append(d)
    assert [D[5][0],D[5][1],D[6][0],D[6][1]]==[7008,43600,80512,414400]
    interior_hash=hashlib.sha256();edge_hash=hashlib.sha256()
    interior=0;positive=0;negative=[]
    for q in range(1,n+1):
        a,h=B[q][q],B[q+1][q]
        a1,h1=B[q+1][q+1],B[q+2][q+1]
        assert D[q][0]==2**q*a and D[q][1]==2**(q-1)*(h-2*a)
        for k in range(q):
            m=D[q][k]*D[q+1][k+1]-D[q][k+1]*D[q+1][k]
            assert m!=0
            if m>0: positive+=1
            else: negative.append((q,k))
            if k==0:
                assert m==4**q*(a*h1-a1*h)
                edge_hash.update(f'{q}:{m}\n'.encode())
            else:
                assert m>0
                interior+=1;interior_hash.update(f'{q},{k}:{m}\n'.encode())
    assert negative==[(q,0) for q in range(5,n+1)]
    assert interior==n*(n-1)//2
    assert all(D[q][k]>0 for q in range(n+2) for k in range(q+1))
    assert all(D[q][q]==5**q for q in range(n+2))
    triangle=sum(B[s][q]>0 for s in range(len(B)) for q in range(s+1))
    assert triangle==len(B)*(len(B)+1)//2
    exterior=sum(v<0 for s,row in enumerate(B) for v in row[s+1:])
    assert exterior>0
    result=dict(schema='EM_R340_EXACT_V1',status='PASS',q_max=n,
        minors_total=n*(n+1)//2,minors_positive=positive,
        minors_negative=len(negative),negative_positions='(q,0) for q=5..q_max',
        interior_positive=interior,interior_sha256=interior_hash.hexdigest(),
        edge_sha256=edge_hash.hexdigest(),signed_B_rows=len(B),
        D_positive=(n+2)*(n+3)//2,D_diagonal_5_pow_q=n+2,
        triangle_positive=triangle,exterior_negative_retained=exterior,
        scope='finite exhaustive check only; no infinite conjecture proved',
        arithmetic='Python arbitrary precision integers, no floating point')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--q-max',type=int,default=320)
    p.add_argument('--output',default='R340_COMPACT_EVIDENCE.json')
    a=p.parse_args();assert 5<=a.q_max<=640
    result=run(a.q_max)
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('R340 PASS',result['minors_total'],result['interior_positive'])
