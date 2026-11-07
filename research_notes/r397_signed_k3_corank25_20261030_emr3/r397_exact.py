#!/usr/bin/env python3
"""Exact finite raw-D Newton observations for corank r=25.
Reimplements original R346 signed twelve K/J branches as printed in immutable
GitHub source R346_verify.py sha 1579ceb717ab1945227eca4f7a1878bf4ffa73e1.
Preserves K3[t²] = -8(1+theta), all other signed branches unchanged.
All arithmetic Python ints/Fraction. No floating sign decisions.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
import json, hashlib, argparse
from pathlib import Path

def C(n,k): return comb(n,k) if 0 <= k <= n else 0

def add(a,b,lim):
    z=[0]*min(lim,max(len(a),len(b)))
    for i,x in enumerate(a[:len(z)]): z[i]+=x
    for i,x in enumerate(b[:len(z)]): z[i]+=x
    return z

def mul(a,b,lim):
    z=[0]*min(lim,len(a)+len(b)-1)
    for i,x in enumerate(a[:len(z)]):
        if x:
            for j,y in enumerate(b[:len(z)-i]):
                if y: z[i+j]+=x*y
    return z

def monomial(n,coef,shift):
    return [0]*shift + [coef*C(n,j) for j in range(n+1)] if n>=0 else [0]

def K(i):
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    z=[0]
    for j,v in enumerate(ds,1):
        if v: z=add(z,monomial(i+1-j,-v,i-1),30)
    return z

def J(s):
    z=[0]
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v: z=add(z,monomial(n,v,s),30)
    return z

def fd(vals):
    a=list(vals); d=[]
    while a:
        d.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return d

def eval_at(theta,r=25):
    theta=F(theta)
    assert theta > -1
    S=5*r+4 # highest D index r+2*(2r+1)+2 = 5r+4
    P=3*r+2 # highest exponent q=r+(2r+1)+1 = 3r+2
    kernels=[None]+[K(i) for i in range(1,13)]
    assert kernels[3][2] == -8
    kernels[3][2] = -8*(1+theta)
    B=[[0]*(P+1) for _ in range(S+1)]
    B[0][0]=B[0][1]=1
    for s in range(1,S+1):
        base=J(s)
        for j,value in enumerate(base[:P+1]): B[s][j]=value
        for i in range(1,min(s,12)+1):
            ker=kernels[i]
            for j,z in enumerate(ker):
                if z:
                    for p in range(j,P+1):
                        B[s][p]+=z*B[s-i][p-j]
    def D(q,k):
        return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))
    M=[]
    for v in range(2*r+1):
        k=v+1; q=r+k
        m=D(q,k)*D(q+1,k+1)-D(q,k+1)*D(q+1,k)
        M.append(m * F(5)**(2*r-1-2*k))
    coeff=fd(M)
    turan=[coeff[j]**2-coeff[j-1]*coeff[j+1] for j in range(1,2*r)]
    top=F(comb(2*r,r),r+1)*(30-16*theta)**(2*r)
    assert coeff[-1]==top
    return dict(r=r,theta=f'{theta.numerator}/{theta.denominator}',coeff=coeff,turan=turan,
        neg_c=[j for j,x in enumerate(coeff) if x<0], neg_t=[j+1 for j,x in enumerate(turan) if x<0],
        zero_c=[j for j,x in enumerate(coeff) if x==0],zero_t=[j+1 for j,x in enumerate(turan) if x==0],
        top=top)

def output(items,path):
    s=[]
    for x in items:
        row={k:([str(y) for y in v] if k in ('coeff','turan') else str(v) if isinstance(v,F) else v) for k,v in x.items()}
        row['pf2']=not(row['neg_c'] or row['neg_t']) and (not any(x['coeff'][j]==0 for j in range(1,len(x['coeff'])-1)))
        s.append(row)
    by=json.dumps({'schema':'EM_R397_CORANK25_FINITE_EXACT_V1','results':s},ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    Path(path).write_text(by)
    print('R397_POINT_CHECK_PASS',[(x['theta'], len(x['neg_c']),len(x['neg_t']),x['neg_c'][:5],x['neg_t'][:5]) for x in s]);print('SHA256',hashlib.sha256(by.encode()).hexdigest())
    return s
if __name__=='__main__':
    import sys
    ap=argparse.ArgumentParser();ap.add_argument('--out',default=str(Path(__file__).with_name('R397_POINTS.json')));ap.add_argument('theta',nargs='*',default=['0','1/2','9/10','901/1000','902/1000','1','15/8'])
    a=ap.parse_args()
    output([eval_at(F(x)) for x in a.theta],a.out)
