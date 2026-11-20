#!/usr/bin/env python3
"""Exact crosscheck of the first N^92 overlap count, no external libraries."""
from math import comb

def brute(m):
    ab=bc=abc=0
    for a in range(m):
      for b in range(m):
       for c in range(m):
        for d in range(m):
         v=comb(c+2,2)*comb(d+2,2)
         A=a+b+c<m
         B=a+c+d<m
         C=b+c+d<m
         ab+=v*(A and B)
         bc+=v*(B and C)
         abc+=v*(A and B and C)
    return ab,bc,abc

def collapsed(m):
    ab=sum(comb(c+2,2)*(r+1)*comb(r+3,3)
           for c in range(m) for r in range(m-c))
    bc=sum(comb(s+5,5)*(m-s)**2 for s in range(m))
    abc=0
    for c in range(m):
      for d in range(m-c):
        r=m-1-c-d
        h=max(r-d,0)
        count=(r+1)**2-h*(h+1)//2
        abc+=comb(c+2,2)*comb(d+2,2)*count
    return ab,bc,abc

for m in (1,2,3,4,5,8,17):
    a=brute(m)
    b=collapsed(m)
    assert a==b,(m,a,b)
    ab,bc,abc=a
    R=abc-2*ab-bc
    assert R<0
    print(f"PASS m={m}, AB=AC={ab}, BC={bc}, ABC={abc}, R={R}")
