#!/usr/bin/env python3
"""Exact F_3 and integer verification for R762EJ, numpy >= 1.24.
Finite checks are not a universal proof; all-q proof uses R762EI.
"""
import json
import numpy as np

G_RELATIONS = [
    ("100","001","002","011"),
    ("010","001","002","020"),
    ("001","001","002","002"),
    ("000","102","000","021"),
    ("000","012","000","012"),
    ("000","000","102","021"),
    ("000","000","012","012"),
    ("000","000","000","111")
]
F_WITNESSES = [
    ("200","020","020","100"),
    ("011","010","210","100"),
    ("011","210","010","100"),
    ("002","000","220","100"),
    ("211","000","200","200"),
    ("010","110","000","200"),
    ("122","100","000","100"),
    ("222","210","210","000")
]
OMIT=((0,0),(0,1),(0,2),(1,0),(1,1),(2,0),(2,1),(3,0))
P_SHIFTS=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def rank_mod3(mat):
    a=mat.copy().astype(np.uint8,copy=False)
    nr,nc=a.shape
    row=0
    for col in range(nc):
        if row==nr: break
        candidates=np.flatnonzero(a[row:,col])
        if not len(candidates): continue
        pivot=row+int(candidates[0])
        if pivot!=row: a[[pivot,row]]=a[[row,pivot]]
        if a[row,col]==2: a[row]=(2*a[row])%3
        below=np.flatnonzero(a[row+1:,col])+row+1
        for begin in range(0,len(below),2048):
            rows=below[begin:begin+2048]
            factor=a[rows,col].copy()
            a[rows]=(a[rows]+(3-factor[:,None])*a[row])%3
        row+=1
    return row

def verify(q):
    x,y,z=np.indices((q,q,q),dtype=np.int32)
    ell=(x,y,z,(x-y+z)%q)
    m=((y+z)%3,(x-z)%3,(x+y)%3,(y+z)%3)
    L=np.zeros((q**3,4*q),dtype=np.uint8)
    B=np.zeros((q**3,4*q),dtype=np.uint8)
    rows=np.arange(q**3)
    for j in range(4):
        col=j*q+ell[j].reshape(-1)
        L[rows,col]=1
        B[rows,col]=(1+m[j].reshape(-1))%3
        for t in range(q):
            vec=np.where((ell[j]==t)&(m[j]==0),1,
                np.where((ell[j]==t)&(m[j]==1),-1,0)).astype(np.int16)
            pvec=sum(np.roll(vec,shift,axis=(0,1,2)) for shift in P_SHIFTS)
            assert np.count_nonzero(pvec)==0,(q,j,t)
    omit={j*q+t for j,t in OMIT}
    keep=[col for col in range(4*q) if col not in omit]
    assert len(keep)==4*q-8
    lr=rank_mod3(L)
    br=rank_mod3(np.concatenate((L,B[:,keep]),axis=1))
    ar=rank_mod3(np.concatenate((L,B),axis=1))
    assert (lr,br,ar)==(4*q-4,8*q-12,8*q-12)
    for gs,fs in zip(G_RELATIONS,F_WITNESSES):
        expr=np.zeros((q,q,q),dtype=np.int16)
        for j in range(4):
            g=np.array(list(map(int,gs[j])),dtype=np.int16)
            f=np.array(list(map(int,fs[j])),dtype=np.int16)
            expr+=f[ell[j]%3]+g[ell[j]%3]*m[j]
        assert np.count_nonzero(expr%3)==0
    rel=np.zeros((8,4*q),dtype=np.uint8)
    for row,gs in enumerate(G_RELATIONS):
        for j in range(4):
            for t in range(q):
                rel[row,j*q+t]=int(gs[j][t%3])
    assert rank_mod3(rel)==8
    assert rank_mod3(rel[:,sorted(omit)])==8
    return dict(q=q,points=q**3,stripe_generators=4*q,
        independent_generators=len(keep),omitted_generators=[f"{j}:{t}" for j,t in OMIT],
        rank_mod3_L=lr,rank_mod3_L_plus_minimal_B=br,
        rank_mod3_L_plus_all_B=ar,relations_verified=8,
        exact_integer_annihilations_verified=4*q,basis_and_relations="PASS")

if __name__=="__main__":
    results=[verify(q) for q in (3,9,27)]
    print(json.dumps({"schema":"R762EJ_EXACT_EVIDENCE_V1",
        "method":"complete_integer_annihilation_and_finite_field_rank",
        "q_values":[3,9,27],"results":results,"all_pass":True,
        "note":"Finite checks; all-q claim proved in paper conditional on R762EI."},
        indent=2,ensure_ascii=False))
