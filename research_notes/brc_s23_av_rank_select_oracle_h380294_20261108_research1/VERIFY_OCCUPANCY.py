#!/usr/bin/env python3
"""Exact S23/AV prefix-cell occupancy without enumerating prefix states.
Requires VERIFY_ORACLE.py from the same directory. Fixed science and n<=2455069,
H<=380294. Integer tests and Euclidean floor sums only.
"""
from random import Random
from time import perf_counter
import VERIFY_ORACLE as m

BASE_P, BASE_D = m.P, m.D
P2, D2 = 24900305, 4564093
N = 2455069

def certify_prefix_projection(n,H):
    assert 0<=n<=N and 1<=H<=380294 and n+H < D2
    assert max(abs(m.LO*D2-P2*m.Q), abs(m.HI*D2-P2*m.Q))*(n+H)<m.Q

def count_prefix_in_gap(H,n,left,right):
    """Number of (k,l), k,l>=0,k+l<=n, with t(left)<k-r*l<t(right).
    left/right are exact adjacent threshold coordinates; adjacency is
    a separate precondition, not inferred by this count.
    """
    certify_prefix_projection(n,H)
    vl,jl=left;vr,jr=right
    assert 0<=vl<=H and 0<=jl<=H-vl
    assert 0<=vr<=H and 0<=jr<=H-vr
    # Under P2/D2, t(left)<t(right), so -t(right)<r*l-k<-t(left).
    x= -P2*vr+D2*jr
    y= -P2*vl+D2*jl
    assert x<y
    oldp,oldd=m.P,m.D
    try:
        m.P,m.D=P2,D2
        # Exclude both integer-key boundaries, including exact zero.
        return m.count_lt(n,y)-m.count_lt(n,x+1)
    finally:
        m.P,m.D=oldp,oldd

def minimal_prefix_by_residue(left,right):
    """Only valid with projected boundary gap of manageable integer width.
    Exhaust all integer keys strictly in the interval, then minimize k+l.
    """
    low= -P2*right[0]+D2*right[1]
    high= -P2*left[0]+D2*left[1]
    inv=pow(P2,-1,D2)
    out=[]
    for K in range(low+1,high):
        l=(K*inv)%D2
        k=(P2*l-K)//D2
        assert P2*l-D2*k==K
        if k>=0:out.append((k+l,K,k,l))
    return sorted(out)

if __name__=='__main__':
    t0=perf_counter()
    assert m.prove_r_enclosure()
    assert m.certify_h(380294)
    certify_prefix_projection(N,380294)
    print('PASS_TWO_RATIONAL_ORDER_CERTIFICATES',BASE_P,BASE_D,P2,D2)
    for H in (3,8,20):
        threshold=sorted((BASE_P*v-BASE_D*j,v,j) for v in range(H+1) for j in range(H-v+1))
        n=25
        prefix=sorted(P2*l-D2*k for l in range(n+1) for k in range(n-l+1))
        for ix in range(len(threshold)-1):
            left=threshold[ix][1:];right=threshold[ix+1][1:]
            got=count_prefix_in_gap(H,n,left,right)
            x=-P2*right[0]+D2*right[1]
            y=-P2*left[0]+D2*left[1]
            assert got==sum(x<K<y for K in prefix)
        print('PASS_EXHAUSTIVE_GAP_OCCUPANCY',H,len(threshold)-1)
    H=510
    assert m.successor(H,0,0)==(79,431)
    # At H=510 the gap t(0,0)<t(79,431) is adjacent.
    # Under P2/D2 the corresponding prefix key window is -12<K<0.
    assert P2*79-D2*431==12
    witnesses=minimal_prefix_by_residue((0,0),(79,431))
    assert len(witnesses)==11
    assert witnesses[0]==(N,-7,2074774,380295)
    assert count_prefix_in_gap(510,N-1,(0,0),(79,431))==0
    assert count_prefix_in_gap(510,N,(0,0),(79,431))==1
    print('PASS_COMPACT_N510_FIRST_ENTRY_CERTIFICATE',
          'gap',(0,0),(79,431),'keys',11,'minimum',witnesses[0])
    rng=Random(7612)
    for H in (7000,100000,200000,300000,380294):
        M=(H+1)*(H+2)//2
        ranks={0,1,2,3,4,5,10,100,1000,5000,100000,M//2,M-2,M-3,M-4,M-100,M-1000}
        ranks.update(rng.randrange(M-1) for _ in range(600))
        checks=[]
        for rk in ranks:
            if not 0<=rk<M-1:continue
            left=m.select(H,rk)
            right=m.select(H,rk+1)
            assert m.rank(H,*right)==rk+1
            checks.append(count_prefix_in_gap(H,N,left,right))
        assert min(checks)>=1
        print('PASS_SAMPLED_OCCUPANCY',H,'checked',len(checks),'minimum',min(checks))
    print('PASS_S23_AV_EXACT_PREFIX_GAP_OCCUPANCY',round(perf_counter()-t0,3))
