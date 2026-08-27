#!/usr/bin/env python3
import math
from collections import Counter

def prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def A(s):return math.comb(2*s,s)**2*math.comb(3*s,s)

def wall(n,s):
    a=A(s);d0=1;hs=[]
    for k in (1,2,3):
        dk=math.gcd(a,n**k);hs.append(dk//d0);d0=dk
    return hs

def classify(p,q):
    n=p*q
    if p==3:return 'SMALL_PRIME_PRECHECK',3
    s=1
    while math.gcd(A(s),n)==1:s*=2
    g=math.gcd(A(s),n)
    assert 3*(s//2)<p<3*s<2*p and s<p
    if 1<g<n:return 'DIRECT_W1_SEPARATOR',g
    h=wall(n,s);assert h[0]==n and h[2]==1
    if 1<h[1]<n:return 'W1_SYNC_W2_SEPARATOR',h[1]
    cl='FULL_SYNC_HIGH_BIN_2S_3S' if h[1]==1 else 'FULL_SYNC_LOW_BIN_3S2_2S'
    if cl.startswith('FULL_SYNC_HIGH'):assert 2*s<p<q<3*s
    else:assert 3*s<2*p<2*q<4*s
    u=math.isqrt(n)//3+1
    assert u<p and p<3*u<q
    return cl,math.gcd(A(u),n)

def main():
    ps=[p for p in range(3,300) if p%2 and prime(p)]
    counts=Counter();cases=0
    for i,p in enumerate(ps):
        for q in ps[i+1:]:
            cl,d=classify(p,q);n=p*q
            assert 1<d<n and n%d==0
            counts[cl]+=1;cases+=1
    assert cases==1830
    expected={'DIRECT_W1_SEPARATOR':1370,'W1_SYNC_W2_SEPARATOR':202,'FULL_SYNC_HIGH_BIN_2S_3S':118,'FULL_SYNC_LOW_BIN_3S2_2S':80,'SMALL_PRIME_PRECHECK':60}
    assert dict(counts)==expected,(counts,expected)
    for p,q,s in ((7,11,4),(13,17,8),(29,37,16)):
        h=wall(p*q,s);assert h[0]==p*q and h[1]==p and h[2]==1
    print('PCF3_INDEPENDENT_CHECK_PASS semiprimes=1830 zero_failures counts='+str(dict(sorted(counts.items()))))
if __name__=='__main__':main()
