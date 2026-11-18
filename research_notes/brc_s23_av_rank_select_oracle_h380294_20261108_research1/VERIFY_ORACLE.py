#!/usr/bin/env python3
"""Certified rank/select and adjacency in triangular likelihood threshold set.
For finite horizons H<=380294, a fixed rational convergent preserves all
real threshold comparisons. Complexity: each rank O(log H+log q), selection
O(log((p+q)H) * (log H+log q)); no quadratic threshold enumeration.
"""
from fractions import Fraction
from random import Random
from time import perf_counter
from math import gcd

Q = 10**26
LO = 545569623581288298975349314
HI = LO + 1
P, D = 2074774, 380295  # convergent for r = ln 7 / ln(10/7)

def enclosure(z, terms=45):
    s=Fraction(0);term=z
    for i in range(terms):
        s+=2*term/(2*i+1)
        term*=z*z
    return s,s+2*term/((2*terms+1)*(1-z*z))

def prove_r_enclosure():
    l2,u2=enclosure(Fraction(1,3))
    l9,u9=enclosure(Fraction(1,9))
    l15,u15=enclosure(Fraction(1,15))
    a,b=3*l2-u15,3*u2-l15
    c,d=l9+l15,u9+u15
    assert Fraction(LO,Q)<a/d and b/c<Fraction(HI,Q)
    return True

def certify_h(H):
    assert 1<=H<D and gcd(P,D)==1
    assert max(abs(LO*D-P*Q), abs(HI*D-P*Q))*H < Q
    return True

def floor_sum(n,m,a,b):
    """sum_{i=0}^{n-1} floor((a*i+b)/m), signed a,b."""
    assert n>=0 and m>0
    aa,a=divmod(a,m); bb,b=divmod(b,m)
    res=aa*n*(n-1)//2+bb*n
    while True:
        if a>=m:
            res+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            res+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:return res
        n=y//m
        b=y%m
        m,a=a,m

def count_lt(H, boundary):
    """Number of pairs (v,j), v,j>=0, v+j<=H, with P*v-D*j<boundary."""
    def jmin(v):return (P*v-boundary)//D + 1
    def first_yes(predicate):
        l,r=0,H+1
        while l<r:
            mid=(l+r)//2
            if predicate(mid):r=mid
            else:l=mid+1
        return l
    A=first_yes(lambda v:jmin(v)>0)  # full rows v<A
    B=first_yes(lambda v:jmin(v)>H-v) # empty rows v>=B
    assert 0<=A<=B<=H+1
    n=B-A
    full=A*(H+1)-A*(A-1)//2
    middle=n*H-(A+B-1)*n//2 - floor_sum(n,D,P,P*A-boundary)
    total=full+middle
    assert 0<=total<=(H+1)*(H+2)//2
    return total

def key_to_pair(H,K):
    v= (K*pow(P,-1,D))%D
    assert v<=H
    j=(P*v-K)//D
    assert 0<=j<=H-v and K==P*v-D*j
    return v,j

def select(H,rank):
    M=(H+1)*(H+2)//2
    assert 0<=rank<M
    low=-D*H
    high=P*H+1
    # count_lt(H,first_key)=0 and count_lt(H,last_key+1)=M
    while low+1<high:
        mid=(low+high)//2
        if count_lt(H,mid)>rank:high=mid
        else:low=mid
    K=high-1
    assert count_lt(H,K)==rank
    return key_to_pair(H,K)

def rank(H,v,j):
    assert 0<=v<=H and 0<=j<=H-v
    return count_lt(H,P*v-D*j)

def successor(H,v,j):
    index=rank(H,v,j)
    if index+1==(H+1)*(H+2)//2:return None
    return select(H,index+1)

def brute(H):
    return sorted((P*v-D*j,v,j) for v in range(H+1) for j in range(H-v+1))

if __name__=='__main__':
    start=perf_counter()
    assert prove_r_enclosure()
    assert certify_h(380294)
    print('PASS_ENCLOSURE',LO,HI,'Q',Q,flush=True)
    print('CERTIFIED_H_MAX',380294,'CONVERGENT',P,D,flush=True)
    for H in (1,2,3,10,80,150):
        exact=brute(H)
        for idx,(_,v,j) in enumerate(exact):
            assert rank(H,v,j)==idx
            assert select(H,idx)==(v,j)
            if idx+1<len(exact):assert successor(H,v,j)==exact[idx+1][1:]
            else:assert successor(H,v,j) is None
        print('PASS_EXHAUSTIVE',H,len(exact),flush=True)
    rng=Random(81211)
    for H in (7000,100000,380294):
        assert certify_h(H)
        M=(H+1)*(H+2)//2
        for _ in range(250):
            idx=rng.randrange(M)
            a=select(H,idx)
            assert rank(H,*a)==idx
            if idx+1<M:
                b=successor(H,*a)
                assert rank(H,*b)==idx+1
                assert P*b[0]-D*b[1]>P*a[0]-D*a[1]
        print('PASS_ORDER_STATISTIC',H,'TOTAL',M,'QUERIES',250,flush=True)
    for H,ids in [(7000,[0,1,100,7000,100000,12255250,24510498,24510500]),(100000,[0,1,100000,2500000000,5000049999]),(380294,[0,30000,10000000,30000000000,72311900000])]:
        M=(H+1)*(H+2)//2
        for idx in ids:
            if idx>=M:continue
            a=select(H,idx)
            b=select(H,idx+1) if idx+1<M else None
            print('ADJACENCY',H,idx,a,b, ((b[0]-a[0],b[1]-a[1]) if b else None),flush=True)
    print('PASS_S23_AV_CERTIFIED_RANK_SELECT_ADJACENCY','elapsed',round(perf_counter()-start,3),flush=True)
