#!/usr/bin/env python3
"""Exact S23/AV finite-future occupancy: h=218..241.
Logs only propose ordering and lookup; each assertion uses exact integers.
"""
from bisect import bisect_right
from math import comb, log
L7,L10=log(7),log(10)
def saturation(h):
    T=sorted(((i,s) for s in range(h+1) for i in range(s+1)),
             key=lambda v:v[0]*L10-v[1]*L7)
    vlogs=[i*L10-s*L7 for i,s in T];m=len(T)
    assert m==comb(h+2,2)
    limit=8*h+8
    s7=[7**j for j in range(limit+h+3)]
    s10=[10**j for j in range(limit+h+3)]
    def t_lt(a,b):
        i,s=a;j,t=b
        return s10[i]*s7[t]<s10[j]*s7[s]
    assert all(t_lt(a,b) for a,b in zip(T,T[1:]))
    tail=0
    while s7[tail+h]>=s10[tail]:tail+=1
    assert tail>0 and s7[tail-1+h]>=s10[tail-1] and s7[tail+h]<s10[tail]
    first=[-1]*(m+1); witness=[None]*(m+1);missing=m+1
    for n in range(1,limit+1):
        for k in range(n+1):
            ell=n-k
            idx=bisect_right(vlogs,n*L7-k*L10)
            def below(j):
                i,s=T[j];return s7[n+s]<s10[k+i]
            while idx>0 and below(idx-1):idx-=1
            while idx<m and not below(idx):idx+=1
            assert idx==0 or not below(idx-1)
            assert idx==m or below(idx)
            if first[idx]<0:
                first[idx]=n;witness[idx]=(k,ell);missing-=1
        if not missing:
            assert n==max(first) and n>=tail
            last=[j for j,x in enumerate(first) if x==n]
            return n,tail,m+1,[(T[j-1] if j else None,T[j] if j<m else None,witness[j]) for j in last]
    raise AssertionError(('NO_SATURATION',h,missing))
def gap_certificate():
    k=0
    for ell in range(79):
        while 7**(k+ell+148)>=10**k:k+=1
        assert 7**(k+ell+148)<10**k
        if k>0:assert 7**(k-1+ell+148)>=10**(k-1)
        if ell<78:assert 7**(k+ell+219)<=10**(k+60)
        else:
            assert (k,ell)==(1233,78)
            assert 7**(k+ell+219)>10**(k+60)
    assert 1233+78==1311
    print('SCALED_GAP_CERTIFICATE: earliest prefix=(1233,78), length=1311; PASS')
def main():
    gap_certificate()
    for h in range(218,242):
        n,tail,count,last=saturation(h)
        if 219<=h<=240:
            assert n==1311 and last==[((60,219),(0,148),(1233,78))]
        if h==218:assert (n,tail)==(1190,1190)
        if h==241:assert (n,tail)==(1315,1315)
        print(f'h={h} N={n} n_tail={tail} excess={n-tail} intervals={count} final_gap={last}; PASS',flush=True)
    print('PASS_S23_AV_H219_240_THIRD_EXACT_SCALED_GAP_PLATEAU_20261108')
if __name__=='__main__':main()
