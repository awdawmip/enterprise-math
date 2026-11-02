from collections import Counter
from math import comb, factorial
from fractions import Fraction
from pathlib import Path
from hashlib import sha1
from experiments.x6_signed_native_spatial_v16_20260905 import signed_brc as B
p=Path(B.__file__).read_bytes()
assert sha1(b'blob '+str(len(p)).encode()+b'\0'+p).hexdigest()=='300a96e3dc24bf6fff73743037a0347a8bc83176'
def moments(c,n,q,d):
    return tuple(sum(v*(n-2*k)**j for k,v in c.items() if k%q==r)
                 for r in range(q) for j in range(d+1))
def rk(A):
    A=[list(map(Fraction,row)) for row in A]; m=len(A); n=len(A[0]); rank=0
    for j in range(n):
        if rank==m: break
        p=next((i for i in range(rank,m) if A[i][j]),None)
        if p is None: continue
        A[rank],A[p]=A[p],A[rank]
        v=A[rank][j]; A[rank]=[u/v for u in A[rank]]
        for i in range(rank+1,m):
            v=A[i][j]
            A[i]=[a-v*b for a,b in zip(A[i],A[rank])]
        rank+=1
    return rank
for n in range(15):
    for q in range(1,6):
        for d in range(4):
            A=[[int(k%q==r)*(n-2*k)**j for k in range(n+1)]
               for r in range(q) for j in range(d+1)]
            assert rk(A)==min(n+1,q*(d+1))
for q in range(1,5):
    for d in range(4):
        m=d+1
        for n in (q*m,q*m+1):
            E=Counter({q*t:comb(m,t) for t in range(m+1) if t%2==0})
            O=Counter({q*t:comb(m,t) for t in range(m+1) if t%2})
            assert moments(E,n,q,d)==moments(O,n,q,d)
            gap=sum(v*(n-2*k)**m for k,v in E.items())-sum(v*(n-2*k)**m for k,v in O.items())
            assert gap==factorial(m)*(2*q)**m
            for c in (E,O):
                for k,v in c.items():
                    assert v<=comb(n,k)<=B.endpoint_multiplicity(n,(n-2*k,0,0,0,0,0))
A=Counter({0:1,3:2}); C=Counter({1:2,4:1})
assert moments(A,4,1,2)==moments(C,4,1,2)
assert moments(A,4,2,2)[1]-moments(C,4,2,2)[1]==8
print('PASS native signed BRC pinned blob; 300 exact ranks; 32 positive-word fibers; n=4 mixed observer gap=8')
