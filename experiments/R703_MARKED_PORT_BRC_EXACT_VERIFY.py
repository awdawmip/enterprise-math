#!/usr/bin/env python3
"""R703 exact source-gate quotient checker. Candidate dynamics, NOT X6 physical evolution."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import math

N=(24,18,6,12)
W=(96,5,92,47)
ALPHA=F(1,2)
BETA=F(1,118)
TOTAL=2*24*19*7*13

def rank(k):
    b,h,t,c,z=k
    return ((((b*24+h)*19+t)*7+c)*13+z)

def unrank(n):
    z=n%13;n//=13
    c=n%7;n//=7
    t=n%19;n//=19
    h=n%24;n//=24
    return (n,h,t,c,z)

def moments(k):
    b,h,t,c,z=k
    v=(b+h,t,c,z)
    return (sum(v),sum(a*w for a,w in zip(v,W)),b)

def rows(k):
    b,h,t,c,z=k
    out={(1-b,h,t,c,z):ALPHA}
    for s,ct in [((b,h+1,t,c,z),23-h),((b,h-1,t,c,z),h),
                 ((b,h,t+1,c,z),18-t),((b,h,t-1,c,z),t),
                 ((b,h,t,c+1,z),6-c),((b,h,t,c-1,z),c),
                 ((b,h,t,c,z+1),12-z),((b,h,t,c,z-1),z)]:
        if ct:out[s]=F(ct)*BETA
    assert sum(out.values(),F())==1
    return out

def expect(n):
    return (1-(1-2*ALPHA)**n)/2 + F(59,2)*(1-(1-2*BETA)**n)

def main():
    seen=set()
    for i in range(TOTAL):
        k=unrank(i)
        assert rank(k)==i
        m=moments(k)
        assert m not in seen
        seen.add(m)
        rows(k)
    assert len(seen)==82992 and (2**16<TOTAL<=2**17)
    q=(1,0,0,0,0);r=(0,1,0,0,0)
    assert moments(q)[:2]==moments(r)[:2]==(1,96)
    def down(k):
        e=k[0]+k[1]
        return sum((p for x,p in rows(k).items() if x[0]+x[1]==e-1),F())
    assert down(q)==F(1,2) and down(r)==F(1,118)
    zero=(0,0,0,0,0)
    law={zero:F(1)}
    for n in range(9):
        assert sum(law.values(),F())==1
        assert sum((sum((k[0]+k[1],k[2],k[3],k[4]))*p for k,p in law.items()),F())==expect(n)
        if n==2: assert law[zero]==F(15,59)
        if n<8:
            out=defaultdict(F)
            for k,p in law.items():
                for nxt,w in rows(k).items():out[nxt]+=p*w
            law=dict(out)
    print("R703_MARKED_BRC_LUMPABILITY_EXACT_PASS",TOTAL,"return2=15/59")
if __name__=="__main__":main()
