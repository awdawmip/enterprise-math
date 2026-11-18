#!/usr/bin/env python3
"""Incremental exact prefix-cell occupancy certificate at H=30001."""
from math import gcd
from time import perf_counter

P1,D1=2074774,380295
P2,D2=24900305,4564093
Q=10**26
LO=545569623581288298975349314
HI=LO+1

def ceildiv(a,b):return -((-a)//b)

def floor_sum_signed(n,m,a,b):
    assert n>=0 and m>0 and a>=0
    total=0
    q,b=divmod(b,m)
    total+=n*q
    while True:
        if a>=m:
            total+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            total+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:return total
        n=y//m
        b=y%m
        a,m=m,a

def rank_lt(H,p,d,m):
    A=max(0,min(H+1,ceildiv(m,p)))
    B=max(0,min(H+1,ceildiv(d*H+m,p+d)))
    assert 0<=A<=B<=H+1
    n=B-A
    return A*(H+1)-A*(A-1)//2+n*H-n*(A+B-1)//2-floor_sum_signed(n,d,p,p*A-m)

def select(H,p,d,s):
    assert 0<=s<(H+1)*(H+2)//2
    low=-d*H
    high=p*H+2
    while low+1<high:
        mid=(low+high)//2
        if rank_lt(H,p,d,mid)>s:high=mid
        else:low=mid
    key=high-1
    v=(key*pow(p,-1,d))%d
    j=(p*v-key)//d
    assert 0<=v and 0<=j and v+j<=H
    return v,j

def occupancy(n,left,right):
    vL,jL=left
    vR,jR=right
    X=-P2*vR+D2*jR
    Y=-P2*vL+D2*jL
    assert X<Y
    return rank_lt(n,P2,D2,Y)-rank_lt(n,P2,D2,X+1)

def test_small():
    from random import Random
    rnd=Random(1732)
    for h in [0,1,2,3,7,20,44]:
        keys=sorted((P1*v-D1*j,v,j) for v in range(h+1) for j in range(h-v+1))
        for i,(key,v,j) in enumerate(keys):
            assert rank_lt(h,P1,D1,key)==i
            assert select(h,P1,D1,i)==(v,j)
            assert rank_lt(h,P1,D1,key+1)==i+1
        for _ in range(30):
            m=rnd.randint(-D1*h-500,P1*h+500)
            expected=sum(P1*v-D1*j<m for v in range(h+1) for j in range(h-v+1))
            assert rank_lt(h,P1,D1,m)==expected
        prefix=[P2*l-D2*k for l in range(h+1) for k in range(h-l+1)]
        for i in range(len(keys)-1):
            left=keys[i][1:]
            right=keys[i+1][1:]
            X=-P2*right[0]+D2*right[1]
            Y=-P2*left[0]+D2*left[1]
            assert occupancy(h,left,right)==sum(X<K<Y for K in prefix)
    print('PASS small brute rank/select and occupancy')

def run(H=30001,n=2455069):
    t0=perf_counter()
    assert H<D1 and n+H<D2
    for p,d,h in [(P1,D1,H),(P2,D2,n+H)]:
        assert gcd(p,d)==1
        assert h*max(abs(LO*d-p*Q),abs(HI*d-p*Q))<Q
    M=(H+1)*(H+2)//2
    seen=set()
    checked=0
    min_occ=None
    min_pos=None
    first_zero=None
    for v in range(H+1):
        point=(v,H-v)
        key=P1*v-D1*(H-v)
        rank=rank_lt(H,P1,D1,key)
        for idx in (rank-1,rank):
            if idx<0 or idx>=M-1 or idx in seen:continue
            seen.add(idx)
            left=select(H,P1,D1,idx)
            right=select(H,P1,D1,idx+1)
            assert left==point or right==point
            oc=occupancy(n,left,right)
            checked+=1
            if min_occ is None or oc<min_occ:
                min_occ,min_pos=oc,(left,right,idx)
            if oc==0 and first_zero is None:
                first_zero=(left,right,idx)
        if v%5000==0:
            print('progress',v,'distinct_cells',len(seen),'seconds',round(perf_counter()-t0,2),flush=True)
    assert n*LO>H*Q
    assert n*Q>H*HI
    print('ENDPOINT',H,'prefix',n,'newpoints',H+1,'affected',len(seen),'checked',checked,'minocc',min_occ,'firstzero',first_zero,'minpos',min_pos,'elapsed',round(perf_counter()-t0,4))
    assert checked==len(seen)==60002
    assert first_zero is None
    print('PASS_S23_AV_EXACT_N_H30001_ENDPOINT')

if __name__=='__main__':
    test_small()
    run()
