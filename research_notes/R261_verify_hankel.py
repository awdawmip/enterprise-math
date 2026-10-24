#!/usr/bin/env python3
"""R262 exact certificate: 7-state Hankel rank for coarse q/00 query.
No third-party packages. All arithmetic is exact integer arithmetic.
This is a formal BRC quotient checker, NOT a native Source module execution.
"""
import json
from itertools import product

S = [(0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)]
EDGES = {0:((2,-1,-1),(2,1,-1)), 1:((0,-1,-1),(0,1,-1)), 2:((1,1,1),(2,1,-1))}
DELTA = ((1,0),(2,0),(2,2))
OUT = tuple((q,g) for q in range(3) for g in (0,1))

def step(q,r,eps,k,a):
    t,eta,b=EDGES[q][a]
    return t,DELTA[r][a],eta*eps,eta*k+b

def det_bareiss(matrix):
    a=[row[:] for row in matrix]; n=len(a); den=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            idx=next((i for i in range(k+1,n) if a[i][k]),None)
            if idx is None: return 0
            a[k],a[idx]=a[idx],a[k]; sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*p-a[i][k]*a[k][j]
                assert num%den==0
                a[i][j]=num//den
            a[i][k]=0
        den=p
    return sign*a[-1][-1]

def direct_outputs(m):
    v=[0]*6
    for word in product((0,1),repeat=m):
        q=r=k=0; eps=1
        for a in word: q,r,eps,k=step(q,r,eps,k,a)
        v[OUT.index((q,int(r==2)))]+=1
    return v

def main():
    assert len(S)==7
    ix={s:i for i,s in enumerate(S)}
    T=[[0]*7 for _ in S]
    for i,(q,r) in enumerate(S):
        for a in (0,1):
            t,rr,_,_=step(q,r,1,0,a)
            assert (t,rr) in ix
            T[i][ix[t,rr]]+=1
    row=[1,0,0,0,0,0,0]
    f=[]
    for m in range(8):
        v=[0]*6
        for i,(q,r) in enumerate(S): v[OUT.index((q,int(r==2)))]+=row[i]
        assert sum(v)==1<<m
        assert v==direct_outputs(m), (m,v,direct_outputs(m))
        f.append(v)
        nxt=[0]*7
        for i in range(7):
            for j in range(7): nxt[j]+=row[i]*T[i][j]
        row=nxt
    H=[f[i]+[f[i+1][2]] for i in range(7)]
    assert det_bareiss(H)==-880
    hist={(0,0,1,0):1}
    for m in range(21):
        coarse=[0]*6
        for (q,r,eps,k),c in hist.items():
            coarse[OUT.index((q,int(r==2)))]+=c
        assert sum(coarse)==1<<m
        if m<=7: assert coarse==f[m]
        out={}
        for (q,r,eps,k),c in hist.items():
            for a in (0,1):
                key=step(q,r,eps,k,a)
                out[key]=out.get(key,0)+c
        hist=out
    report={'schema':'EM_R262_AUTHOR_HANKEL_CERTIFICATE_V1',
            'claim':'time-homogeneous finite-dimensional linear realization of effect-marginalized terminal (q, contains_00) exact counts has minimal dimension 7',
            'determinant':-880,'minor_rows':'prefix depths 0..6',
            'minor_columns':['future=0 q0 false','future=0 q0 true','future=0 q1 false','future=0 q1 true','future=0 q2 false','future=0 q2 true','future=1 q1 false'],
            'depth_counts_0_to_7':f,'H':H,'adjacency_T':T,
            'verification':{'direct_word_enumeration_depths':'0..7','affine_positive_histogram_depths':'0..20','arithmetic':'exact integers','status':'PASS'},
            'not_verified':['native Enterprise Math Python modules','R193 actual observer/time-port','native P000 heartbeat physical realization','formal independent review']}
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
