#!/usr/bin/env python3
"""PREFIX458: exact rational rank for septic moment evaluations on W6.
Integer certificate combines modular lower rank with exact integer kernel.
P000 native X6; D={+e1, +/-e2,...,+/-e6}; unmodified BRC path semantics.
"""
import math, time, hashlib
import numpy as np
from numba import njit

DEGREE=7; M=DEGREE-1; PRIMES=(32003,32009)

def support(m):
    steps = [(1,0,0,0,0,0)]
    for i in range(1,6):
        for s in (-1,1):
            e=[0]*6; e[i]=s; steps.append(tuple(e))
    pts={(0,)*6}
    for _ in range(m):
        pts={tuple(a+b for a,b in zip(p,e)) for p in pts for e in steps}
    return sorted(pts)

def exponents(d):
    def comp(n,k):
        if k==1:
            yield (n,);return
        for a in range(n+1):
            for b in comp(n-a,k-1):yield (a,)+b
    return [e for t in range(d+1) for e in comp(t,6)]

def matrix(pts,exps,d):
    X=np.asarray(pts,dtype=np.int64)
    pows=np.stack([X**k for k in range(d+1)])
    A=np.ones((len(pts),len(exps)),dtype=np.int64)
    for i,e in enumerate(exps):
        for j,z in enumerate(e):
            if z: A[:,i]*=pows[z,:,j]
    return A

@njit(cache=True)
def powmod(a, n, p):
    v=1
    while n:
        if n & 1: v=v*a%p
        a=a*a%p
        n//=2
    return v

@njit(cache=True)
def fast_elim(A, p):
    R,C=A.shape
    B=(A%p).astype(np.int64)
    pivots=np.empty(min(R,C),dtype=np.int64)
    r=0
    for c in range(C):
        select=-1
        for rr in range(r,R):
            if B[rr,c]!=0:
                select=rr;break
        if select<0:continue
        if select!=r:
            for cc in range(c,C):
                B[r,cc],B[select,cc]=B[select,cc],B[r,cc]
        inv=powmod(B[r,c],p-2,p)
        for rr in range(r+1,R):
            if B[rr,c]!=0:
                mul=B[rr,c]*inv%p
                for cc in range(c+1,C):
                    B[rr,cc]=(B[rr,cc]-mul*B[r,cc])%p
                B[rr,c]=0
        pivots[r]=c; r+=1
        if r==R:break
    return r,pivots[:r],B

def modular_null(A,p):
    rank,piv,B=fast_elim(A,p)
    pivot_set=set(map(int,piv)); free=[i for i in range(A.shape[1]) if i not in pivot_set]
    K=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    K[free,np.arange(len(free))]=1
    for i in range(rank-1,-1,-1):
        col=int(piv[i]); inv=pow(int(B[i,col]),-1,p)
        K[col]=(-(B[i,col+1:] @ K[col+1:])*inv)%p
    assert not np.any((A%p) @ K %p)
    return rank,list(map(int,piv)),free,K

def rational_reconstruct(res,mod):
    b=math.isqrt(mod//2)
    r0,r1=mod,int(res)%mod
    t0,t1=0,1
    while abs(r1)>b:
        q=r0//r1; r0,r1=r1,r0-q*r1; t0,t1=t1,t0-q*t1
    if not t1 or abs(t1)>b:raise ValueError('reconstruct bounds')
    if t1<0:r1,t1=-r1,-t1
    if math.gcd(r1,t1)!=1 or (int(res)*t1-r1)%mod: raise ValueError('reconstruct congruence')
    return r1,t1

def run():
    start=time.monotonic()
    S=support(M); E=exponents(DEGREE); A=matrix(S,E,DEGREE)
    print('W6_points',len(S),'degree7_monomials',len(E),'max_abs_A',int(np.abs(A).max()),flush=True)
    ranks=[]; pivots=[]; frees=[]; kernels=[]
    for prime in PRIMES:
        st=time.monotonic()
        r,p,f,K=modular_null(A,prime)
        print('prime',prime,'rank',r,'nullity',len(f),'elapsed',round(time.monotonic()-st,2),flush=True)
        ranks.append(r);pivots.append(p);frees.append(f);kernels.append(K)
    assert pivots[0]==pivots[1] and frees[0]==frees[1]
    p0,p1=PRIMES; mod=p0*p1
    mul=pow(p0,-1,p1)
    residues=kernels[0]+p0*((kernels[1]-kernels[0])*mul%p1)
    K=np.zeros_like(residues)
    largest_den=0
    for j in range(K.shape[1]):
        ratios=[rational_reconstruct(x,mod) for x in residues[:,j]]
        denominator=math.lcm(*(x[1] for x in ratios));largest_den=max(largest_den,denominator)
        K[:,j]=[a*(denominator//b) for a,b in ratios]
    print('kernel',K.shape,'maxcoef',np.max(np.abs(K)),'largest_denominator',largest_den,flush=True)
    # Safe int64 if every row's conservative absolute matmul bound fits.
    bound=int(np.abs(A).max())*int(np.abs(K).max())*A.shape[1]
    assert bound<2**63, bound
    exact=A@K
    assert not np.any(exact)
    for j,col in enumerate(frees[0]):
        assert K[col,j]>0
        assert sum(K[col,k]!=0 for k in range(K.shape[1]))==1
    assert ranks[0]==ranks[1]
    print('EXACT PASS rank',ranks[0], 'deficiency',len(E)-ranks[0], 'nonzero_K',int(np.count_nonzero(K)),'bound',bound, 'seconds',round(time.monotonic()-start,2))
    np.savez_compressed('/mnt/data/prefix458_work/PREFIX458_INTEGER_KERNEL.npz',K=K,pivots=np.asarray(pivots[0]),free=np.asarray(frees[0]),exps=np.asarray(E),support=np.asarray(S))

if __name__=='__main__':run()
