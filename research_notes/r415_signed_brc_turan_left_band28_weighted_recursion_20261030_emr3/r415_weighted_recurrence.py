#!/usr/bin/env python3
"""R415 independent binomial-weighted recurrence proof checker.
Identity is derived exactly from R414 delta recursion; integer-only checks
are extra finite verification and are NOT the proof of universal scope.
"""
from math import comb

def cat(n):
    return comb(2*n,n)//(n+1)

def triangle(n):
    previous=[]
    for r in range(n+1):
        row=[0]*(r+1)
        row[r]=cat(r)
        for s in range(r-1,-1,-1):
            row[s]=row[s+1]-2*previous[s]
        yield r,row,previous
        previous=row

count=0
for r,row,prev in triangle(160):
    if r==0: continue
    for s in range(r):
        b=lambda rr,ss: comb(rr+ss,2*ss)
        lhs=(2*s+2)*(2*s+1)*b(r,s+1)*row[s+1]
        rhs=(r+s+1)*((r-s)*b(r,s)*row[s]+2*(r+s)*b(r-1,s)*prev[s])
        assert lhs==rhs,(r,s)
        count+=1
print('R415_WEIGHTED_RECURRENCE_PASS',count,'exact integer identities r<=160')
