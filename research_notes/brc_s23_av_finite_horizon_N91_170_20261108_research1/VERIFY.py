#!/usr/bin/env python3
"""S23/AV exact finite-future N(h), 91<=h<=170. Integer-only certificate.
All ordering and membership checks use exact powers of 7 and 10.
"""
from functools import cmp_to_key
from math import comb


def verify(h):
    max_n = 8*h+8
    p7 = [7**i for i in range(max_n+h+2)]
    p10 = [10**i for i in range(max_n+h+2)]
    t = [(i,s) for s in range(h+1) for i in range(s+1)]
    def compare(a,b):
        left=p10[a[0]]*p7[b[1]]
        right=p10[b[0]]*p7[a[1]]
        return (left>right)-(left<right)
    t.sort(key=cmp_to_key(compare))
    assert len(t)==comb(h+2,2)
    assert all(compare(t[j],t[j+1])<0 for j in range(len(t)-1))
    m=len(t)
    first=[-1]*(m+1)
    witness=[None]*(m+1)
    unfilled=m+1
    tail=0
    while p7[tail+h]>=p10[tail]: tail+=1
    assert tail>0 and p7[tail-1+h]>=p10[tail-1] and p7[tail+h]<p10[tail]
    for n in range(1,max_n+1):
        for k in range(n+1):
            ell=n-k
            lo,hi=0,m
            while lo<hi:
                mid=(lo+hi)//2
                i,s=t[mid]
                if p7[n+s]<p10[k+i]:hi=mid
                else:lo=mid+1
            if first[lo]<0:
                first[lo]=n
                witness[lo]=(k,ell)
                unfilled-=1
        if unfilled==0:
            assert max(first)==n and n>=tail
            last=[j for j,a in enumerate(first) if a==n]
            if 140<=h<=161:
                assert n==880 and len(last)==1
                j=last[0]
                assert (t[j-1],t[j],witness[j])==((60,140),(0,69),(802,78))
            else:
                assert n==tail and last==[0] and witness[0]==(n,0)
            return n,tail,m
    raise AssertionError((h,unfilled))


def verify_gap_140():
    assert 10**60 < 7**71
    first_k=0
    for ell in range(79):
        while 7**(first_k+ell+69)>=10**first_k:
            first_k+=1
        assert 7**(first_k+ell+69)<10**first_k
        if first_k>0:
            assert 7**(first_k-1+ell+69)>=10**(first_k-1)
        if ell<78:
            assert 7**(first_k+ell+140)<=10**(first_k+60), (ell,first_k)
        else:
            assert (ell,first_k)==(78,802)
            assert 7**(first_k+ell+140)>10**(first_k+60)
    assert 802+78==880


def main():
    verify_gap_140()
    found={}
    for h in range(91,171):
        n,tail,m=verify(h)
        found[h]=(n,tail,m)
        print(f'h={h}: N={n}; tail={tail}; intervals={m+1}; PASS',flush=True)
    assert all(found[h][0]==found[h][1] for h in list(range(91,140))+list(range(162,171)))
    assert all(found[h][0]==880 and found[h][1]<880 for h in range(140,162))
    assert (found[139][0],found[140][0],found[161][0],found[162][0])==(759,880,880,884)
    print('Exact interior-gap lemma: 140<=h<=161, gap=(10^60/7^140,7^-69), earliest prefix=(k,ell)=(802,78), n=880: PASS')
    print('PASS_S23_AV_FUTURE_H91_170_EXACT_INTEGER_CERTIFICATE_20261108')


if __name__=='__main__': main()
