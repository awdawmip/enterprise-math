#!/usr/bin/env python3
"""Exact independent finite-check for signed twelve-branch BRC K3 deformation.
Rebuilds raw K/J -> B -> D -> H/Q; no native X6 claim, no float sign tests.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
def choose(n,k): return comb(n,k) if 0<=k<=n else 0

def branch_K(i):
    ds=(-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),
        choose(7,i-2),-choose(9,i-3))
    out={}
    for j,v in enumerate(ds,1):
        if v:
            for m in range(i+2-j):
                p=i-1+m
                out[p]=out.get(p,0)-v*choose(i+1-j,m)
    return out

def source_J(s):
    out={}
    for v,n in ((-choose(3,s-1),s),(-choose(6,s-1),s-1),(choose(8,s-2),s-2)):
        if v and n>=0:
            for m in range(n+1):
                p=s+m
                out[p]=out.get(p,0)+v*choose(n,m)
    return out

def difference(xs):
    a=list(xs);out=[]
    while a:
        out.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return out

def build(theta,R=16):
    theta=Fraction(theta);pmax=3*R+2;smax=5*R+4
    kernels=[None]+[branch_K(i) for i in range(1,13)]
    assert kernels[3][2]==-8
    kernels[3][2]=-8*(1+theta)
    B=[[Fraction(0) for _ in range(pmax+1)] for _ in range(smax+1)]
    B[0][0]=B[0][1]=Fraction(1)
    for s in range(1,smax+1):
        for j,v in source_J(s).items():
            if j<=pmax:B[s][j]=v
        for i in range(1,min(12,s)+1):
            for shift,k in kernels[i].items():
                if not k:continue
                row=B[s-i];dest=B[s]
                for t in range(pmax-shift+1):
                    if row[t]:dest[t+shift]+=k*row[t]
    def D(q,k):
        return sum(((-1)**(k-w))*choose(k,w)*Fraction(2)**(q-w)*B[q+w][q]
                   for w in range(k+1))
    def H(r,u):return D(r+u,u)/Fraction(5)**u
    def Q(r):
        out=[]
        for v in range(2*r+1):
            k=v+1;q=r+k
            m=D(q,k)*D(q+1,k+1)-D(q,k+1)*D(q+1,k)
            out.append(m*Fraction(5)**(2*r-1-2*k))
        return out
    return H,Q

def run():
    points=['-1/2','0','1/2','901/1000','902/1000','1','15/8','2']
    coranks=[1,2,3,4,5,6,8,12,15,16]
    result=[]
    for p in points:
        theta=Fraction(p);H,Q=build(theta)
        row={'theta':p,'coranks':[]}
        for r in coranks:
            dh=difference([H(r,u) for u in range(r+1)])
            c=difference(Q(r))
            a=30-16*theta
            assert dh[-1]==(a/Fraction(5))**r,(p,r,'H')
            assert c[-1]==Fraction(choose(2*r,r),r+1)*a**(2*r),(p,r,'Q')
            rec={'r':r,'top_H':str(dh[-1]),'top_Q':str(c[-1]),
                'degree_H':max((i for i,x in enumerate(dh) if x),default=-1),
                'degree_Q':max((i for i,x in enumerate(c) if x),default=-1),
                'negative_C':[i for i,x in enumerate(c) if x<0],
                'negative_T':[i for i in range(1,2*r)
                    if c[i]*c[i]-c[i-1]*c[i+1]<0]}
            row['coranks'].append(rec)
        result.append(row)
    ks={i:branch_K(i) for i in range(1,13)}
    for degree,expected in [(0,{1:2}),(1,{1:3,2:-1}),(2,{2:4,3:-8})]:
        assert {i:k.get(degree,0) for i,k in ks.items() if k.get(degree,0)}==expected
    deg16=result[points.index('15/8')]['coranks'][-1]
    assert deg16['degree_H']==8 and deg16['degree_Q']==16
    assert deg16['negative_T']==[14,15] and deg16['top_Q']=='0'
    content=json.dumps({'schema':'R384_SIGNED_K3_TOP_DIRECT_EXACT_V1',
        'arithmetic':'exact integer/Fraction','observations':result},ensure_ascii=False,indent=2)+'\n'
    (HERE/'R384_EVIDENCE.json').write_text(content)
    summary={'schema':'R384_SIGNED_K3_TOP_SUMMARY_V1',
      'exact_checks':len(points)*len(coranks)*2,
      'parameters':points,'coranks':coranks,
      'theta15over8_r16':deg16,
      'evidence_sha256':hashlib.sha256(content.encode()).hexdigest()}
    (HERE/'R384_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('R384_EXACT_PASS',json.dumps(summary))
if __name__=='__main__':run()
