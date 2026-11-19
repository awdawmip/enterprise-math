#!/usr/bin/env python3
"""Exact rational experiment for spanning-tree directed Port reconstruction."""
from fractions import Fraction as Q
from itertools import permutations
from random import Random
import json

rng=Random(28420261119)

def det(A):
    n=len(A)
    ans=Q(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=Q(-1 if inv%2 else 1)
        for i in range(n): term*=A[i][p[i]]
        ans+=term
    return ans

def coef_F(C, S):
    R=[i for i in range(len(C)) if i not in S]
    return det([[-C[i][j] for j in R] for i in R])

def coef_HminusF_over_z(C,S,u,v):
    R=[i for i in range(len(C)) if i not in S]
    if u not in R or v not in R:return Q(0)
    M=[[-C[i][j] for j in R] for i in R]
    old=det(M)
    M[R.index(u)][R.index(v)]-=Q(1)
    return det(M)-old

def direct_poly_value(C,d,probe=None,z=Q(0)):
    n=len(C)
    M=[[(-C[i][j]+(d[i] if i==j else 0)) for j in range(n)] for i in range(n)]
    if probe is not None:
        u,v=probe;M[u][v]-=z
    return det(M)

def reconstruct(C,edges):
    n=len(C);I=list(range(n))
    alpha=[-coef_F(C,tuple(j for j in I if j!=i)) for i in I]
    p={}
    for i in I:
        for j in range(i+1,n):
            p[(i,j)]=alpha[i]*alpha[j]-coef_F(C,tuple(k for k in I if k not in (i,j)))
    getp=lambda i,j:p[tuple(sorted((i,j)))]
    known=[[None]*n for _ in I]
    for i in I:known[i][i]=alpha[i]
    q={}
    for u,v in edges:
        S=tuple(k for k in I if k not in (u,v))
        c_vu=-coef_HminusF_over_z(C,S,u,v)
        assert c_vu>0
        known[v][u]=c_vu
        known[u][v]=getp(u,v)/c_vu
        for w in I:
            if w in (u,v):continue
            T=tuple(k for k in I if k not in (u,v,w))
            zc=coef_HminusF_over_z(C,T,u,v)
            q[(u,v,w)]=c_vu*alpha[w]-zc
    passes=0
    while True:
        changed=0
        for u,v in edges:
            for w in I:
                if w in (u,v):continue
                target=q[(u,v,w)]
                if known[w][u] is not None and known[v][w] is None:
                    value=target/known[w][u]
                    known[v][w]=value;known[w][v]=getp(v,w)/value
                    changed+=1
                elif known[v][w] is not None and known[w][u] is None:
                    value=target/known[v][w]
                    known[w][u]=value;known[u][w]=getp(w,u)/value
                    changed+=1
        passes+=1
        if changed==0:break
        assert passes<=n*n
    assert all(x is not None for row in known for x in row)
    return tuple(tuple(row) for row in known),passes

def main():
    count=0;coefficient_checks=0;full_det_checks=0;maxpasses=0
    by_n={}
    for n in range(2,7):
        trials={2:55,3:55,4:55,5:40,6:20}[n]
        by_n[str(n)]=0
        for t in range(trials):
            A=tuple(tuple(Q(rng.randint(1,9),rng.randint(1,8)) for _ in range(n)) for _ in range(n))
            edges=[]
            for v in range(1,n):
                u=rng.randrange(v)
                edges.append((u,v) if rng.randrange(2) else (v,u))
            got,passes=reconstruct(A,edges)
            assert got==A,(n,edges)
            maxpasses=max(maxpasses,passes)
            by_n[str(n)]+=1;count+=1
            for u,v in edges:
                c=-coef_HminusF_over_z(A,tuple(k for k in range(n) if k not in (u,v)),u,v)
                assert c==A[v][u]
                coefficient_checks+=1
                for w in range(n):
                    if w in (u,v):continue
                    h=coef_HminusF_over_z(A,tuple(k for k in range(n) if k not in (u,v,w)),u,v)
                    assert h==A[v][u]*A[w][w]-A[v][w]*A[w][u]
                    coefficient_checks+=1
            if n<=5 and t<3:
                d=tuple(Q(rng.randint(1,6)) for _ in range(n))
                for probe in (None,edges[0]):
                    z=Q(1,7) if probe else Q(0)
                    val=direct_poly_value(A,d,probe,z)
                    poly=Q(0)
                    for mask in range(1<<n):
                        S=tuple(i for i in range(n) if mask&(1<<i))
                        monom=Q(1)
                        for i in S:monom*=d[i]
                        poly+=monom*(coef_F(A,S)+(z*coef_HminusF_over_z(A,S,*probe) if probe else 0))
                    assert val==poly
                    full_det_checks+=1
    # Actual nonidentifiable disconnected-probe case, including full polynomial coefficient equality.
    n=4;eps=Q(1,100)
    A=tuple(tuple(eps*(1+(i+2*j)%4) for j in range(n)) for i in range(n))
    edges=((0,1),(2,3))
    scal=(Q(1),Q(1),Q(2),Q(2))
    B=tuple(tuple(scal[i]*A[i][j]/scal[j] for j in range(n)) for i in range(n))
    assert B!=A
    assert max(sum(row) for row in A)<1 and max(sum(row) for row in B)<1
    disconnected_coefficients=0
    for mask in range(1<<n):
        S=tuple(i for i in range(n) if mask&(1<<i))
        assert coef_F(A,S)==coef_F(B,S);disconnected_coefficients+=1
        for u,v in edges:
            assert coef_HminusF_over_z(A,S,u,v)==coef_HminusF_over_z(B,S,u,v)
            disconnected_coefficients+=1
    print(json.dumps({
        'schema':'R284AT_EXACT_VERIFICATION_V1',
        'status':'PASS',
        'method':'Standard-library Fraction, Leibniz determinants and full multiaffine coefficient equality',
        'spanning_tree_reconstruction_cases':count,
        'cases_by_n':by_n,
        'pair_and_triple_probe_coefficient_checks':coefficient_checks,
        'full_det_polynomial_reconstruction_checks':full_det_checks,
        'max_closure_passes':maxpasses,
        'disconnected_positive_stable_counterexample':{'n':4,'probes':['E_01','E_23'],'gauge':['1','1','2','2'],'checked_F_and_H_coefficients':disconnected_coefficients},
        'limitations':'Mathematical proof covers all n>=2 and strict positivity; finite experiments n=2..6; no native X6 dynamical claim or independent review.'
    },indent=2,sort_keys=True))

if __name__=='__main__':main()
