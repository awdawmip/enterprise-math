#!/usr/bin/env python3
"""R284AU: exact one-scale scalar Port reconstruction for bounded rational matrices.
Python stdlib only; no numerical approximation. Input A has positive integer entries.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import permutations
from random import Random
from collections import deque
import json


def det_bareiss(mat):
    m=[list(map(int,r)) for r in mat]
    n=len(m)
    if not n:return 1
    sign=1;prev=1
    for k in range(n-1):
        if m[k][k]==0:
            pivot=next((i for i in range(k+1,n) if m[i][k]),None)
            if pivot is None:return 0
            m[k],m[pivot]=m[pivot],m[k];sign=-sign
        piv=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=m[i][j]*piv-m[i][k]*m[k][j]
                assert numerator%prev==0,('bareiss_nondivisible',numerator,prev)
                m[i][j]=numerator//prev
        for i in range(k+1,n):m[i][k]=0
        prev=piv
    return sign*m[-1][-1]


def round_nearest_fraction(a,b):
    assert b>0
    return (2*a+b)//(2*b)


def leading_minor_oracle(A,T,edge=None,scale=None):
    n=len(A); M=max(map(max,A))
    B=factorial(n)*(M+1)**n
    L=2*B+2 if scale is None else scale
    complement=set(range(n))-set(T)
    mat=[[(L if i==j and i in complement else 0)-A[i][j]-(1 if edge==(i,j) else 0)
          for j in range(n)] for i in range(n)]
    value=det_bareiss(mat)
    leading=round_nearest_fraction(value,L**len(complement))
    return leading,value,L


def reconstruction(A,tree_edges):
    n=len(A);M=max(map(max,A));L=2*factorial(n)*(M+1)**n+2
    calls=0
    cache={}
    def query(T,edge=None):
        nonlocal calls
        key=(tuple(sorted(T)),edge)
        if key not in cache:
            coeff,_,_=leading_minor_oracle(A,T,edge,L)
            cache[key]=coeff
            calls+=1
        return cache[key]
    alpha=[-query([i]) for i in range(n)]
    p={}
    for i in range(n):
        for j in range(i+1,n):p[i,j]=alpha[i]*alpha[j]-query([i,j])
    getp=lambda i,j:p[tuple(sorted((i,j)))]
    known=[[None for _ in range(n)]for _ in range(n)]
    for i in range(n):known[i][i]=alpha[i]
    q={}
    for u,v in tree_edges:
        a_vu=query([u,v])-query([u,v],(u,v))
        assert a_vu>0
        known[v][u]=a_vu
        known[u][v]=getp(u,v)//a_vu
        assert known[u][v]*a_vu==getp(u,v)
        for w in range(n):
            if w in (u,v):continue
            delta=query([u,v,w],(u,v))-query([u,v,w])
            q[(u,v,w)]=a_vu*alpha[w]-delta
    adj=[[] for _ in range(n)]
    orientation={frozenset((u,v)):(u,v) for u,v in tree_edges}
    for u,v in tree_edges:adj[u].append(v);adj[v].append(u)
    for x in range(n):
        visited={x}; queue=deque([x])
        while queue:
            a=queue.popleft()
            for b in adj[a]:
                if b in visited:continue
                visited.add(b);queue.append(b)
                if a==x:continue
                u,v=orientation[frozenset((a,b))]
                val=q[(u,v,x)]
                if (u,v)==(a,b):
                    assert val%known[x][a]==0
                    known[b][x]=val//known[x][a]
                    assert getp(x,b)%known[b][x]==0
                    known[x][b]=getp(x,b)//known[b][x]
                else:
                    assert (u,v)==(b,a)
                    assert val%known[a][x]==0
                    known[x][b]=val//known[a][x]
                    assert getp(x,b)%known[x][b]==0
                    known[b][x]=getp(x,b)//known[x][b]
    assert known==A, ('not_reconstructed',known,A)
    naive_query_bound=n+comb(n,2)+(n-1)+2*(n-1)*(n-2)
    assert calls<=naive_query_bound
    return {"n":n,"M":M,"L_bit_length":L.bit_length(),"calls":calls,
            "naive_query_bound":naive_query_bound,
            "max_det_bit_length_bound":(factorial(n)*(L+M+1)**n).bit_length(),
            "witness":{"a_01":A[0][1],"a_10":A[1][0],"recovered_entries":n*n}}


def det_fraction_by_permutations(matrix):
    n=len(matrix);total=Fraction(0)
    for p in permutations(range(n)):
        negative=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2
        term=Fraction(-1 if negative else 1)
        for i in range(n):term*=matrix[i][p[i]]
        total+=term
    return total


def rational_oracle_bridge_check():
    A=[[1,3,2],[4,2,1],[2,1,5]]
    n=len(A);M=5;b=37
    L=2*factorial(n)*(M+1)**n+2
    trials=0
    for T in ([0],[1,2],[0,1,2]):
        for edge in (None,(0,1)):
            S=set(range(n))-set(T)
            d=[Fraction(L,b) if i in S else Fraction(0) for i in range(n)]
            z=Fraction(0) if edge is None else Fraction(1,b)
            mat=[[(d[i] if i==j else 0)-Fraction(A[i][j],b)-(z if edge==(i,j) else 0)
                  for j in range(n)] for i in range(n)]
            rational=det_fraction_by_permutations(mat)
            M_integer=[[(L if i==j and i in S else 0)-A[i][j]-(1 if edge==(i,j) else 0)
                  for j in range(n)] for i in range(n)]
            assert rational*b**n==det_bareiss(M_integer)
            trials+=1
    return {"rational_denominator":b,"oracle_scaling_cases":trials}


def zero_support_counterexample():
    values=[]
    for beta in (1,2):
        C=[[1,beta],[0,1]]
        for D in [(0,0),(2,5),(9,10)]:
            for z in (0,1,4):
                M=[[(D[i] if i==j else 0)-C[i][j]-(z if (i,j)==(0,1) else 0)
                    for j in range(2)]for i in range(2)]
                values.append((beta,D,z,det_bareiss(M)))
    for v in values[:9]:
        same=next(x for x in values[9:] if x[1]==v[1] and x[2]==v[2])
        assert v[3]==same[3]
    assert det_bareiss([[1,-1],[-1,1]])!=det_bareiss([[1,-2],[-1,1]])
    return {"class":"2x2 upper-triangular with C21=0",
            "pair":[[[1,1],[0,1]],[[1,2],[0,1]]],
            "E12_response":"identical for all diagonal variables and edit z",
            "reverse_E21":"distinguishes beta"}


def run(seed=28420261119):
    rng=Random(seed)
    runs=[]; tree_edges_checked=0; scalar_queries=0
    per_n={2:40,3:45,4:45,5:40,6:24,7:14}
    for n,count in per_n.items():
        for k in range(count):
            A=[[rng.randrange(1,6) for _ in range(n)] for __ in range(n)]
            edges=[]
            for j in range(1,n):
                parent=rng.randrange(j)
                edges.append((j,parent) if rng.randrange(2) else (parent,j))
            data=reconstruction(A,edges)
            scalar_queries+=data['calls'];tree_edges_checked+=len(edges)
            runs.append(data)
    boundary=[]
    for A,tree in [([[1,2],[3,4]],[(1,0)]),
                   ([[1]*6 for _ in range(6)],[(i,i+1) for i in range(5)]),
                   ([[1,2,1],[1,1,2]],[(0,1),(2,1)])]:
        data=reconstruction(A,tree)
        boundary.append(data)
    return {"theorem_id":"R284AU","status":"PASS",
            "arithmetic":"exact integer Bareiss + exact balanced integer extraction",
            "seed":seed,"random_cases":len(runs),"boundary_cases":len(boundary),
            "dimension_counts":{str(n):count for n,count in per_n.items()},
            "tree_edges_checked":tree_edges_checked+sum(r['n']-1 for r in boundary),
            "scalar_oracle_queries":scalar_queries+sum(r['calls'] for r in boundary),
            "max_query_count":max(r['calls'] for r in runs),
            "max_L_bit_length":max(r['L_bit_length'] for r in runs),
            "max_integer_det_bound_bits":max(r['max_det_bit_length_bound'] for r in runs),
            "boundary_results":boundary,
            "rational_bridge":rational_oracle_bridge_check(),
            "sparse_boundary":zero_support_counterexample(),
            "verification_scope":"208 pseudorandom strictly-positive integer cores of n=2..7 plus 3 exact boundary cores; scale is computed solely from n and known M; result checks A entries exactly",
            "general_theorem_status":"AUTHOR_PROVED_NOT_INDEPENDENTLY_REVIEWED"}


if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2,ensure_ascii=False))
