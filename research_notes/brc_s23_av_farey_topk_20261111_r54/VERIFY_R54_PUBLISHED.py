"""R54: certified Farey-neighbor top-k upper-phase generation, exact integer tests."""
from math import gcd, isqrt
from heapq import heappush, heapreplace
from random import Random

def bracket(p,q,K):
    assert 0<p<q and K>=1
    a,i,c,j=0,1,1,1
    blocks=0
    while i+j<=K:
        blocks+=1
        if (a+c)*q<p*(i+j):
            lo,hi=1,(K-i)//j
            while lo<hi:
                v=(lo+hi+1)//2
                if (a+v*c)*q<p*(i+v*j):lo=v
                else:hi=v-1
            a,i=a+lo*c,i+lo*j
        else:
            assert (a+c)*q>p*(i+j)
            lo,hi=1,(K-j)//i
            while lo<hi:
                v=(lo+hi+1)//2
                if (c+v*a)*q>p*(j+v*i):lo=v
                else:hi=v-1
            c,j=c+lo*a,j+lo*i
    assert i*c-j*a==1 and a*q<p*i and c*q>p*j and i+j>K
    return (a,i,c,j),blocks

def order(p,q,K,k):
    (a,i,c,j),blocks=bracket(p,q,K)
    out=[];s=j
    for _ in range(k):
        out.append(s)
        s=s-i if s>i else (s+j if s+j<=K else s+j-i)
    return out,(a,i,c,j),blocks

def oracle(p,q,K,k):
    heap=[]
    for s in range(1,K+1):
        e=q-(s*p)%q
        if len(heap)<k:heappush(heap,(-e,s))
        elif e<-heap[0][0]:heapreplace(heap,(-e,s))
    return [s for ne,s in sorted(heap,reverse=True)]

def check(p,q,K,k):
    got,params,blocks=order(p,q,K,k)
    assert got==oracle(p,q,K,k),(p,q,K,k,got)
    if k==K:assert len(set(got))==K
    return params,blocks,got

def run():
    n=0
    for q in range(3,41):
        for p in range(1,q):
            if gcd(p,q)>1:continue
            for K in range(1,q):
                check(p,q,K,K);n+=1
    assert n==12620
    rng=Random(540111)
    for _ in range(300):
        K=rng.randrange(12,800)
        check(rng.randrange(1,1000003),1000003,K,K)
    D=10**30;r=isqrt(2*D*D)
    assert r*r<2*D*D<(r+1)*(r+1)
    lo=r-D;hi=lo+1
    for K in [12,20,50,352,1000]:
        (a,i,c,j),_,got=check(lo+hi,2*D,K,K)
        assert a*D<lo*i and a*D<hi*i and c*D>lo*j and c*D>hi*j
        if K==12: assert got[:7]==[12,7,2,9,4,11,6]
    A=262204504569236716045286;B=A+1;D=10**24
    for K,k in [(352,352),(100000,10),(1000000,12)]:
        params,blocks,got=check(A+B,2*D,K,k)
        a,i,c,j=params
        assert a*D<A*i and a*D<B*i and c*D>A*j and c*D>B*j
        print('S23',K,k,'Farey',params,'quotient_blocks',blocks,'top',got[:12])
        if K==352:
            assert params==(43,164,59,225)
            assert got[:5]==[225,61,286,122,347]
            assert (K-i,K-j,i+j-K)==(188,127,37)
    print('PASS_R54_EXACT',n,'exhaustive rational instances, 300 random, 8 interval-certified families')

if __name__=='__main__':run()
