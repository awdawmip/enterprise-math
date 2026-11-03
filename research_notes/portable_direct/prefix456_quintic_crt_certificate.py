"""Exact Q-ranks for the 5th-degree, N=q+3, final-history sector of native X6.
Modular full-rank lower bound + Hadamard/Chinese-remainder upper bound.
Requires NumPy (int64); run with: python prefix456_quintic_crt_certificate.py 2 3
and: python prefix456_quintic_crt_certificate.py 4 5
"""
import itertools
import math
import sys
import numpy as np

STEPS = [(1,0,0,0,0,0)] + [tuple(a if j==i else 0 for j in range(6))
    for i in range(1,6) for a in (1,-1)]

def W(n):
    points={(0,)*6}
    for _ in range(n):
        points={tuple(a+b for a,b in zip(v,s)) for v in points for s in STEPS}
    return points

W4 = [W(k) for k in range(5)]
MONOMIALS = [e for e in itertools.product(range(6), repeat=6) if sum(e)<=5]

def certificate_matrix(q):
    points=set()
    for ell in range(4//q+1):
        points.update((p[0]-ell*q,*p[1:]) for p in W4[4-ell*q])
    nodes=np.array(sorted(points), dtype=np.int64)
    powers=[np.stack([nodes[:,i]**k for k in range(6)],axis=1) for i in range(6)]
    A=np.empty((len(nodes),len(MONOMIALS)),dtype=np.int64)
    for col,exponents in enumerate(MONOMIALS):
        values=np.ones(len(nodes),dtype=np.int64)
        for axis,d in enumerate(exponents):
            if d: values *= powers[axis][:,d]
        A[:,col]=values
    assert A.shape[1]==462 and abs(A).max()<=1024
    return A,len(points)

def modular_rank(M,p):
    A=np.remainder(M,p)
    rows,cols=A.shape
    rank=0
    for j in range(cols):
        nz=np.flatnonzero(A[rank:,j])
        if len(nz)==0: continue
        pivot=rank+int(nz[0])
        if pivot!=rank: A[[rank,pivot]]=A[[pivot,rank]]
        inv=pow(int(A[rank,j]),-1,p)
        A[rank,j:]=(A[rank,j:]*inv)%p
        below=np.flatnonzero(A[rank+1:,j])+rank+1
        if len(below):
            A[below,j:]=(A[below,j:]-A[below,j,None]*A[rank,j:])%p
        rank+=1
        if rank==rows:break
    return rank

def is_prime(n):
    if n<=1:return False
    if n%2==0:return n==2
    for d in range(3,math.isqrt(n)+1,2):
        if n%d==0:return False
    return True

def primes(n):
    v=2147483647
    out=[]
    while len(out)<n:
        if is_prime(v):out.append(v)
        v-=2
    return out

EXPECTED={2:(805,420,66),3:(754,405,64),4:(744,399,64),5:(743,398,64)}

if __name__ == '__main__':
    qs=[int(a) for a in sys.argv[1:]] or [2,3,4,5]
    ps=primes(66)
    print('PREFIX456 exact quintic-rank CRT certificate')
    print('prime maximum',ps[0],'prime minimum',ps[-1], 'all_prime',all(is_prime(p) for p in ps))
    print('prime_list',','.join(str(p) for p in ps))
    for q in qs:
        count,rank,nprimes=EXPECTED[q]
        A,sz=certificate_matrix(q)
        assert sz==count
        pick=ps[:nprimes]
        product=math.prod(pick)
        column_norm_sq=sorted((sum(int(v)**2 for v in A[:,c]) for c in range(462)),reverse=True)
        hadamard_sq=math.prod(column_norm_sq[:rank+1])
        assert product*product>hadamard_sq
        ranks=[modular_rank(A,p) for p in pick]
        assert all(r==rank for r in ranks),(q,set(ranks))
        print('PASS q=',q,'support=',count,'rank_Q=',rank,'total_rank_Q=',(q-1)*462+rank,
            'defect=',462-rank,'primes=',nprimes,'P_squared_bits=',(product*product).bit_length(),
            'Hadamard_squared_bits=',hadamard_sq.bit_length(),flush=True)
    print('ALL_PASS')
