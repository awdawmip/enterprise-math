#!/usr/bin/env python3
"""Stand-alone full 384x384 Gamma old-witness scan from frozen 189-layer counts.
Independent of PREFIX751/752 import graphs. Python >=3.10 + numpy.
Run companion PREFIX754_R6_GAMMA_FLOAT_ERROR_BOUND.py for exact error envelope.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from collections import defaultdict
from functools import lru_cache
from math import comb, ldexp
import numpy as np

N=189; W=1<<18; DEN=768
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*W//n
    assert inside(n,k,mid)
    if k==0:lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(n,k,x):b=x
            else:a=x
        lo,hi=a,b
    a,b=mid,W
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x):a=x
        else:b=x
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ValueError(('width-undecidable',n,k))

rows=[{0:1}]
for n in range(1,N+1):
    d=defaultdict(int)
    for k,v in rows[-1].items():d[k]+=v;d[k+1]+=v
    rows.append({k:v for k,v in d.items() if wide(n,k)})
assert not rows[N]
assert sum(len(r) for r in rows[:N])==9529

def tail(a,d):
    b=d-a;pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    den=1;vals=[]
    for n,row in enumerate(rows[:N]):
        if n:den*=d
        num=sum(v*pa[k]*pb[n-k] for k,v in row.items())
        f=num/den
        p,q=float(f).as_integer_ratio()
        assert abs(num*q-p*den)*(1<<53)<=den*q,('tail-rounding',a,d,n)
        vals.append(f)
    return np.array(vals,dtype=np.float64)

T=np.stack([tail(k,DEN) for k in range(385)])
star=tail(3,20)
C=np.empty((N,N));D=np.empty((N,N))
for n in range(N):
    for m in range(N):
        c=comb(n+m,n);den=1<<(n+m+1)
        C[n,m]=ldexp(float(c),-(n+m+1))
        D[n,m]=(n+m+1)*C[n,m]
        p,q=float(C[n,m]).as_integer_ratio()
        assert abs(c*q-p*den)*(1<<53)<=c*q
A=T.sum(axis=1)
B=T@np.arange(1,N+1,dtype=np.float64)
MU=A[:,None]+A[None,:]-T@C@T.T
M2=2*(B[:,None]+B[None,:])-T@D@T.T
one=np.arange(1,N+1,dtype=np.float64)
mu=T[0].sum()+star.sum()-T[0]@C@star
m2=2*(T[0]@one+star@one)-T[0]@D@star
G=(m2-mu*mu)-M2[1:,1:]+MU[:-1,:-1]**2-np.maximum(0,(mu-MU[:-1,:-1])/2)
assert G.shape==(384,384) and np.all(np.isfinite(G))
I,J=np.indices(G.shape)
offset=np.abs(I-J)
inner=offset<=51;outer=offset>=171
assert int(np.sum(G>0))==137168
assert int(inner.sum())==36900 and int(outer.sum())==45582
x_inner=float(np.min(G[inner]));x_outer=float(np.min(G[outer]))
assert abs(x_inner-0.7664868306305976)<1e-8
assert abs(x_outer-2.990905434524393)<1e-8
assert float(np.min(np.abs(G)))>0.0185
assert x_inner-1/100000>383/500
assert x_outer-1/100000>299/100
print('ALL_CHECKS_PASS PREFIX754 INDEPENDENT_FULL_GRID')
print('survivor_entries 9529, positive_cells',int((G>0).sum()))
print('near_band_min',format(x_inner,'.17g'))
print('far_band_min',format(x_outer,'.17g'))
print('global_min_abs',format(float(np.min(np.abs(G))),'.17g'))
