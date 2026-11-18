#!/usr/bin/env python3
"""Exact sparse Z/9 calculation for finite BRC null quotients, q=3,9,27."""
from collections import defaultdict
from itertools import product
import json


def four_generators(q):
    for family in 'ABCD':
        f=defaultdict(int)
        for r in range(q):
            for s in range(q):
                if family=='A': g=(0,r+s,-s)
                elif family=='B': g=(r+s,0,s)
                elif family=='C': g=(r+s,-s,0)
                else: g=(r+2*s,r+s,-s)
                f[tuple(a%q for a in g)]+=2 if r%3==0 else -1
        yield f


def translated_columns(q):
    G=list(product(range(q),repeat=3))
    index={g:i for i,g in enumerate(G)}
    uv=[((0,1,0),(0,1,-1)),((1,0,0),(1,0,1)),
        ((1,0,0),(1,-1,0)),((1,1,0),(2,1,-1))]
    for f,(u,v) in zip(four_generators(q),uv):
        H={tuple((3*r*u[i]+s*v[i])%q for i in range(3))
           for r in range(q//3) for s in range(q)}
        assert len(H)==q*q//3
        seen=set()
        count=0
        for g in G:
            if g in seen: continue
            count+=1
            for h in H:
                seen.add(tuple((g[i]+h[i])%q for i in range(3)))
            col={}
            for x,c in f.items():
                k=index[tuple((x[i]+g[i])%q for i in range(3))]
                col[k]=c%9
            yield col
        assert count==3*q


def image_mod9(q):
    unit={}; unit_order=[]; three_columns=[]
    inv9={1:1,2:5,4:7,5:2,7:4,8:8}
    count=0
    for col in translated_columns(q):
        count+=1
        w={k:v for k,v in col.items() if v}
        for k in unit_order:
            factor=w.get(k,0)
            if not factor: continue
            for j,c in unit[k].items():
                v=(w.get(j,0)-factor*c)%9
                if v: w[j]=v
                else: w.pop(j,None)
        pivot=next((k for k,v in w.items() if v%3),None)
        if pivot is None:
            three_columns.append(w)
        else:
            fac=inv9[w[pivot]]
            unit[pivot]={k:(fac*v)%9 for k,v in w.items()}
            unit_order.append(pivot)
    assert count==12*q
    # Divide residuals by 3 after eliminating all invertible Z/9 pivots.
    mod3={}
    for w in three_columns:
        w=dict(w)
        for pivot in unit_order:
            factor=w.get(pivot,0)
            if factor:
                for k,c in unit[pivot].items():
                    v=(w.get(k,0)-factor*c)%9
                    if v:w[k]=v
                    else:w.pop(k,None)
        assert all(c%3==0 for c in w.values())
        x={k:c//3 for k,c in w.items()}
        while x:
            pivot=min(x)
            if pivot not in mod3:
                fac=x[pivot] # inverse of 1 and 2 in F3
                mod3[pivot]={k:(fac*v)%3 for k,v in x.items()}
                break
            fac=x[pivot]
            for k,c in mod3[pivot].items():
                v=(x.get(k,0)-fac*c)%3
                if v:x[k]=v
                else:x.pop(k,None)
    return dict(Q=q,columns=count,unit_factors=len(unit),
                exactly_three_factors=len(mod3),
                rational_kernel_rank=8*q-12,
                quotient_3_rank=4*q-8)


def main():
    results=[]
    for q in (3,9,27):
        r=image_mod9(q)
        assert r['unit_factors']==4*q-4
        assert r['exactly_three_factors']==4*q-8
        assert r['unit_factors']+r['exactly_three_factors']==r['rational_kernel_rank']
        results.append(r)
    print(json.dumps({'schema':'R762EH_MOD9_NULL_QUOTIENT_CERT_V1',
         'status':'PASS',
         'method':'exhaustive exact Z/9 sparse pivots plus residual F3 rank',
         'scope':'finite q=3,9,27 conditional on R762ED rational kernel rank',
         'results':results},sort_keys=True,indent=2))


if __name__=='__main__':
    main()
