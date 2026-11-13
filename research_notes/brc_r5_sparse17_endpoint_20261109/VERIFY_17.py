#!/usr/bin/env python3
"""Fraction-only seven-node martingale support reduction: 37 -> 17."""
from fractions import Fraction as Q
r=tuple(map(Q,['1/10','1/2','3/4','1','5/4','3/2','19/10']))
n=len(r)

def rows(edges):
    return ([[Q(i==k) for i,j in edges] for k in range(n)]+
            [[Q(j==k) for i,j in edges] for k in range(n)]+
            [[r[i] if j==k else Q(0) for i,j in edges] for k in range(n)])

def reduce_matrix(M):
    A=[v[:] for v in M]; piv=[]
    for col in range(len(A[0])):
        k=next((i for i in range(len(piv),len(A)) if A[i][col]),None)
        if k is None: continue
        t=len(piv);A[t],A[k]=A[k],A[t]
        c=A[t][col];A[t]=[x/c for x in A[t]]
        for i in range(len(A)):
            if i!=t and A[i][col]:
                c=A[i][col];A[i]=[x-c*y for x,y in zip(A[i],A[t])]
        piv.append(col)
    return A,piv

def constraints(E):
    return (tuple(sum(E[i*n+j] for j in range(n)) for i in range(n)),
            tuple(sum(E[i*n+j] for i in range(n)) for j in range(n)),
            tuple(sum(r[i]*E[i*n+j] for i in range(n)) for j in range(n)))

def sparsify(E):
    M=list(E);rounds=0
    while sum(x>0 for x in M)>3*n-4:
        assert all(M[i*n]==0 for i in range(1,n))
        assert all(M[i*n+n-1]==0 for i in range(n-1))
        ix=[v for v,w in enumerate(M) if w>0][:3*n-3]
        A,piv=reduce_matrix(rows([(v//n,v%n) for v in ix]))
        free=next(j for j in range(len(ix)) if j not in piv)
        d=[Q(0)]*len(ix);d[free]=1
        for row,col in enumerate(piv):d[col]=-A[row][free]
        assert min(d)<0<max(d)
        step=min(M[ix[j]]/-x for j,x in enumerate(d) if x<0)
        for j,x in enumerate(d):M[ix[j]]+=step*x
        assert min(M)>=0
        rounds+=1
    return M,rounds

def dense():
    E=[Q(0)]*(n*n)
    for j in range(n):
        if j==0 or j==n-1: E[j*n+j]=Q(1,n);continue
        E[j*n+j]=Q(1,2*n)
        pairs=[(lo,hi) for lo in range(j) for hi in range(j+1,n)]
        for lo,hi in pairs:
            z=Q(1,2*n*len(pairs))
            E[lo*n+j]+=z*(r[hi]-r[j])/(r[hi]-r[lo])
            E[hi*n+j]+=z*(r[j]-r[lo])/(r[hi]-r[lo])
    return E

allowed=[(i,j) for j in range(n) for i in range(n)
         if j not in (0,n-1) or i==j]
assert len(allowed)==37 and len(reduce_matrix(rows(allowed))[1])==17
E=dense(); assert sum(x>0 for x in E)==37
before=constraints(E)
S,rounds=sparsify(E)
assert constraints(S)==before and sum(x>0 for x in S)==17
assert rounds==20
print('EXACT_ALLOWED_COLUMN_RANK',17)
print('EXACT_MARTINGALE_SPARSE_SUPPORT',37,'TO',17,'IN',rounds,'ROUNDS')
print('ALL_21_MASS_AND_MOMENT_CONSTRAINTS_PRESERVED')
