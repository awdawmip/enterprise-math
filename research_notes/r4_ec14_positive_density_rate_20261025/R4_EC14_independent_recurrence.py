#!/usr/bin/env python3
"""Independent integer recurrence derived from EC13 rational BRC series.
Verifies new EC14 finite bound by integer cross multiplication, not floats.
"""
from math import comb
from R4_EC14_verify import count_dp


def recurrence(nmax):
    s={(0,0):1,(2,1):-1,(3,1):-1,(5,2):1}
    clean=[]
    for n in range(nmax+1):
        row=[0]*(n+1)
        for j in range(n+1):
            def c(ni,ji):
                return clean[ni][ji] if 0<=ni<len(clean) and 0<=ji<=ni else 0
            row[j]=c(n-1,j)+c(n-1,j-1)-2*c(n-4,j-2)+c(n-6,j-3)+s.get((n,j),0)
            assert row[j]>=0,(n,j,row[j])
        clean.append(row)
    return clean


def run():
    nmax=200
    rec=recurrence(nmax)
    dp,_=count_dp(nmax)
    count=0
    for n in range(nmax+1):
        for j in range(n+1):
            assert rec[n][j]==dp[n].get(j,0),(n,j,rec[n][j],dp[n].get(j,0))
            count+=1
        assert rec[n][0]==1 and rec[n][n]==1
        if 1<=n<=200:
            # Exact inequality using q = 1-(min(j,n-j)/n)^2
            b=n//2
            for j in range(1,n):
                lhs=rec[n][j]*n**(2*b)
                rhs=(n+1)*comb(n,j)*(n*n-min(j,n-j)**2)**b
                assert lhs<=rhs,(n,j)
    print(f'PASS: recurrence from EC13, {count} coefficients vs 8-state DP; exact inequality for all n<=200 and 1<=j<n')

if __name__=='__main__':run()
