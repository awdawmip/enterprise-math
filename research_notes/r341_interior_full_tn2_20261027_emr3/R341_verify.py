#!/usr/bin/env python3
"""R341 exact finite BRC check and generic TN2 telescoping certificate.
Not a reproduction of the cited R340 q<=320 certificate.
"""
import json
from fractions import Fraction
from math import comb

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def add(a,b):
    result=[0]*max(len(a),len(b))
    for i,x in enumerate(a): result[i]+=x
    for i,x in enumerate(b): result[i]+=x
    while len(result)>1 and result[-1]==0: result.pop()
    return result

def mul(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: result[i+j]+=x*y
    while len(result)>1 and result[-1]==0: result.pop()
    return result

def term(n,value,shift):
    return [0]*shift + [value*choose(n,i) for i in range(n+1)] if n>=0 and value else [0]

def kernel(i):
    coeff=(-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3))
    result=[0]
    for h,x in enumerate(coeff,1): result=add(result,term(i+1-h,-x,i-1))
    return result

def forcing(s):
    result=[0]
    for value,degree in ((-choose(3,s-1),s),(-choose(6,s-1),s-1),(choose(8,s-2),s-2)):
        result=add(result,term(degree,value,s))
    return result

def brc(n):
    K=[None]+[kernel(i) for i in range(1,13)]
    J=[None]+[forcing(s) for s in range(1,11)]
    B=[[1,1]]
    for s in range(1,2*n+3):
        row=J[s][:] if s<=10 else [0]
        for i in range(1,min(12,s)+1): row=add(row,mul(K[i],B[s-i]))
        B.append(row)
    D=[]
    for q in range(n+2):
        seq=[2**(q-v)*B[q+v][q] for v in range(q+1)]
        row=[]
        while seq:
            row.append(seq[0]);seq=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
        D.append(row)
    return B,D

def adjacent(D,r,j):
    return D[r][j]*D[r+1][j+1]-D[r][j+1]*D[r+1][j]

def expanded(D,q,p,k,l):
    def v(r,j): return Fraction(D[r][j+1],D[r][j])
    s=Fraction(0)
    for j in range(k,l):
        prefix=Fraction(1)
        for h in range(k,j): prefix*=v(q,h)
        suffix=Fraction(1)
        for h in range(j+1,l): suffix*=v(p,h)
        diff=sum((Fraction(adjacent(D,r,j),D[r][j]*D[r+1][j]) for r in range(q,p)), Fraction(0))
        s+=prefix*suffix*diff
    return D[q][k]*D[p][k]*s

def run(n=12):
    assert n>=3
    B,D=brc(n)
    assert [D[5][0],D[5][1],D[6][0],D[6][1]]==[7008,43600,80512,414400]
    checked=0
    local_count=0
    minimum_local=None
    for q in range(1,n):
        for j in range(1,q):
            m=adjacent(D,q,j)
            assert m>0,(q,j,m)
            local_count+=1
            minimum_local=m if minimum_local is None else min(minimum_local,m)
    for q in range(2,n):
        for p in range(q+1,n+1):
            for k in range(1,q):
                for l in range(k+1,q+1):
                    a=D[q][k]*D[p][l]-D[q][l]*D[p][k]
                    assert a>0,(q,p,k,l,a)
                    b=expanded(D,q,p,k,l)
                    assert b==a,(q,p,k,l,b,a)
                    checked+=1
    assert checked==comb(n+1,4)
    assert local_count==(n-1)*(n-2)//2
    assert comb(322,4)==439633040
    return dict(schema='R341_LOCAL_TO_GLOBAL_TN2_V1',status='PASS',n=n,
                generic_formula='verified by exact fractions on all BRC interior rectangles to n',
                local_minors_checked=local_count,full_minors_checked=checked,
                min_local_minor=str(minimum_local),
                R340_cited_max_q=320,R340_cited_local_interior_positive=51040,
                R340_deduced_all_interior_2x2_positive=comb(322,4),
                arithmetic='exact Python integers and fractions',
                source_scope='R340 remote proof and code as previously published; n<=12 independently rerun here',
                result_scope='mathematical lifting theorem general; finite R340 corollary q,p<=321')

if __name__=='__main__':
    from pathlib import Path
    result=run(12)
    path=Path(__file__).with_name('R341_EVIDENCE.json')
    path.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
