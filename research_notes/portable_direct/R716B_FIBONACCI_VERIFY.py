#!/usr/bin/env python3
"""Exact Fibonacci and profile-sum consistency for odd BRC bracelet counts."""
import json
from math import comb

def fib(n):
    # nonnegative integer fast doubling
    def fd(j):
        if j == 0: return 0, 1
        a,b=fd(j//2)
        c=a*(2*b-a); d=a*a+b*b
        return (d,c+d) if j&1 else (c,d)
    return fd(n)[0]

def profile_sum(k):
    return sum(comb(r+s,s)*comb(r+t,t)
               for r in range(k+1) for s in range(k-r+1)
               for t in (k-r-s,))

def main():
    data=[]
    for k in range(501):
        m=2*k+5
        q=4*fib(m-3)
        assert q>0
        if k>=2:
            assert q==3*(4*fib(m-5))-(4*fib(m-7))
        if k<=48:
            assert q==4*profile_sum(k)
        if k in (0,1,2,3,4,5,6,8,48,100,500):
            data.append({'m':m,'bracelet_count':str(q),'rooted_count':str(2*m*q)})
    print(json.dumps({'flag':'R716B_FIBONACCI_BRACELET_EXACT_PASS',
       'checked_odd_lengths':501,'m_min':5,'m_max':1005,'direct_profile_sum_count':49,
       'formula':'Q_m=4*F_(m-3), U_m=8*m*F_(m-3)',
       'examples':data},indent=2))
if __name__=='__main__':main()
