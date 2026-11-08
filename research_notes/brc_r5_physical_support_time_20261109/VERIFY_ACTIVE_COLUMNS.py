#!/usr/bin/env python3
"""Exact rank and explicit feasibility checks for active-source martingale edge sparsity.

The source columns i=0,6 are forced onto their corresponding diagonal edges.
For each active interior source column, every target row is permitted a priori.
No physical-flow feasibility/admission is asserted by this finite test.
"""
from fractions import Fraction as F
from itertools import combinations

R = [F(v,20) for v in (2,10,15,20,25,30,38)]
N = len(R)

def allowed_edges(active):
    return [(i,j) for j in sorted(active) for i in (range(N) if j not in (0,N-1) else [j])]

def matrix(active):
    active = sorted(active)
    edges = allowed_edges(active)
    A = []
    for i in range(N):
        A.append([F(i==u) for u,v in edges])
    for j in active:
        A.append([F(j==v) for u,v in edges])
    for j in active:
        A.append([R[u] if v==j else F(0) for u,v in edges])
    return A, edges

def rank(a):
    a = [list(row) for row in a]
    if not a:return 0
    n,m = len(a),len(a[0]);h=0
    for k in range(m):
        pivot=next((i for i in range(h,n) if a[i][k]), None)
        if pivot is None:continue
        a[h],a[pivot] = a[pivot],a[h]
        pivot_val=a[h][k]
        a[h]=[v/pivot_val for v in a[h]]
        for i in range(h+1,n):
            if a[i][k]:
                factor=a[i][k]
                a[i]=[u-factor*v for u,v in zip(a[i],a[h])]
        h+=1
        if h==n:break
    return h

def rational_example(active):
    active=set(active)
    E=[[F(0) for _ in range(N)] for _ in range(N)]
    for j in active:
        if j in (0,N-1):continue
        for i in range(N):
            E[i][j]+=F(1,1000) if i==j else F(0)
        for lo in range(j):
            for hi in range(j+1,N):
                scale=F(100) if (lo,hi)==(0,N-1) else F(1,100)
                E[lo][j]+=scale*(R[hi]-R[j])
                E[hi][j]+=scale*(R[j]-R[lo])
    moment = sum((R[j]-1)*sum(E[i][j] for i in range(N)) for j in range(N))
    if (0 not in active) or (N-1 not in active):
        raise ValueError('example requires both extremes')
    E[0][0] += F(1000)+max(F(0),moment)/(1-R[0])
    E[N-1][N-1] += F(1000)+max(F(0),-moment)/(R[N-1]-1)
    total = sum(map(sum,E))
    E=[[v/total for v in row] for row in E]
    mu=[sum(row) for row in E]
    nu=[sum(E[i][j] for i in range(N)) for j in range(N)]
    assert sum(mu)==sum(nu)==1
    assert sum(R[i]*mu[i] for i in range(N))==1
    assert sum(R[j]*nu[j] for j in range(N))==1
    for j in range(N):
        assert sum(R[i]*E[i][j] for i in range(N)) == R[j]*nu[j]
    assert all(mu[j]<nu[j] for j in active if j not in (0,N-1))
    assert all(E[i][j]>0 for i,j in allowed_edges(active))
    assert all(nu[j]==0 for j in set(range(N))-active)
    return len([1 for row in E for x in row if x]),max(nu),min(nu[j]-mu[j] for j in active if j not in (0,N-1))

def main():
    for A in [{0,1,2,3,5,6},{0,1,3,5,6},set(range(7))]:
        arr,edges=matrix(A)
        e=len(A & {0,N-1})
        upper=N+2*len(A)-2-e
        actual=rank(arr)
        print('ACTIVE',','.join(map(str,sorted(A))), 'ALLOWED',len(edges), 'RANK',actual,'UPPER',upper)
        assert actual == upper
        if 0 in A and 6 in A:
            support,maxnu,mindef = rational_example(A)
            print('EXACT_FEASIBLE',support,'MIN_STRICT_DEFICIT_POSITIVE',mindef>0)
    for m in range(1,8):
        for A_tuple in combinations(range(7),m):
            A=set(A_tuple);mat,edges=matrix(A)
            e=len(A&{0,N-1})
            assert rank(mat)<=N+2*m-2-e
    print('PASS_ALL_127_NONEMPTY_ACTIVE_SETS_RANK_BOUND')
    print('PASS_PHYSICAL_G_EQ_B_SOURCE_NODE4_ZERO -> SUPPORT_LE_15_IF_FEASIBLE')
    print('PASS_PHYSICAL_G_EQ_B_EQ_A_SOURCE_NODES2_4_ZERO -> SUPPORT_LE_13_IF_FEASIBLE')

if __name__=='__main__':main()
