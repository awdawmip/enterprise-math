# PREFIX-459 native X6 exact modulo-prime rank certificate.
# Scientific source pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
from functools import lru_cache
from math import comb, isqrt
import numpy as np

PRIMES = (32003, 32009)

@lru_cache(None)
def vectors(n, dim):
    if not dim:
        return ((),)
    return tuple((k,)+v for k in range(n+1)
                 for v in vectors(n-k, dim-1))

def rows(m, t):
    return [(s,a) for s in range(m+1) for a in vectors(m-s,5)
            if (m-s-sum(a))%2==0 and all(a[i]>0 for i in range(t))]

def cols(m, t):
    return [(b,c) for b in range(m+2-t)
            for c in vectors((m+1-t-b)//2,5)
            if b+2*sum(c)+t<=m+1]

def rank_mod(m,t,p):
    R,C=rows(m,t),cols(m,t)
    A=np.empty((len(R),len(C)),dtype=np.int64)
    for i,(s,a) in enumerate(R):
        for j,(b,c) in enumerate(C):
            v=pow(s,b,p)
            for ai,ci in zip(a,c):
                v=v*pow(ai,2*ci,p)%p
            A[i,j]=v
    r=0
    for j in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,j]);
        if len(nz)==0: continue
        i=r+int(nz[0]);A[[r,i]]=A[[i,r]]
        A[r,j:]=A[r,j:]*pow(int(A[r,j]),-1,p)%p
        nonzero=np.flatnonzero(A[r+1:,j])+r+1
        if len(nonzero):
            A[nonzero,j:]=(A[nonzero,j:]-A[nonzero,j:j+1]*A[r,j:])%p
        r+=1
    return r,len(R),len(C)

def main():
    for p in PRIMES:
        assert p>2 and all(p%k for k in range(2,isqrt(p)+1))
    print('PREFIX459 EXACT CERTIFICATE; frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d')
    for m in (7,8,9):
        d=m+1;B=comb(d+6,6);total=0;parts=[];count=0
        for t in range(6):
            ranks=[rank_mod(m,t,p) for p in PRIMES]
            assert ranks[0][1:]==ranks[1][1:]
            delta=(m-t+3)//2
            assert ranks[0][2]-ranks[0][0]==delta
            assert ranks[1][0]==ranks[0][0]
            total+=comb(5,t)*ranks[0][0]
            count+=comb(5,t)*ranks[0][2]
            parts.append((t,ranks[0][1],ranks[0][2],ranks[0][0],delta))
        assert count==B and total==B-16*m
        print(f'd={d}, q>={d}, W_size={sum(comb(4,j)*comb(m-j+6,6) for j in range(5))}, B={B}, boundary_rank={total}, defect={16*m}')
        print('t,rows,cols,rank_mod_32003_and_32009,defect:',parts)
        print(f'R_{d}(q)={B}*q-{16*m}; PASS')
    print('PREFIX459 ALL PASS (integer finite-field elimination)')

if __name__=='__main__':main()
