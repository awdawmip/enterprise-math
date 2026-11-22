#!/usr/bin/env python3
"""Exact R5 29/32/43 phase-signature census; model and root-zero theorems pinned in RESEARCH.md."""
from collections import Counter
from math import lcm
A={0,54,55,56,57}
B={0,60,61,62,63}
C={0,37,38,39,40,41,42}
S={2492,2493,2494,4988,6144,8638,8639,8640,11132,11133,11134,11135,11136,13628,13629,13630,16124,17280,19774,19775,19776}
P=lcm(58,64,43)
def sig(m):
    return (int(m%58 in A),int(m%64 in B),int(m%43 in C))
def triples_crt():
    for a in sorted(A):
        for b in sorted(B):
            if (a-b)%2: continue
            r=(a+58*(21*((b-a)//2)%32))%1856
            for c in sorted(C):
                yield (r+1856*(37*(c-r)%43))%P
def main():
    assert P==79808
    cnt=Counter(sig(m) for m in range(P))
    expected={(0,0,0):56304,(0,0,1):10948,(0,1,0):4752,(0,1,1):924,(1,0,0):5292,(1,0,1):1029,(1,1,0):468,(1,1,1):91}
    assert cnt==expected
    R=set(triples_crt())
    assert len(R)==91
    assert R=={m for m in range(P) if sig(m)==(1,1,1)}
    assert all(sig(s)==(1,1,1) for s in S)
    missing=sorted((m or P) for m in R if (m or P) not in S)
    assert len(missing)==70 and missing[0]==22268
    assert all(any(sig(m)!=sig(m+d) for m in range(P))
               for d in range(1,P) if P%d==0)
    first={''.join(map(str,k)):next(m for m in range(1,P+1) if sig(m)==k) for k in expected}
    assert first=={'000':1,'001':37,'010':60,'011':124,'100':54,'101':170,'110':576,'111':2492}
    print('ALL CHECKS PASS; least signature period=',P)
    print('phase counts:',{''.join(map(str,k)):v for k,v in sorted(cnt.items())})
    print('triple classes=',len(R),'already witnessed=',len(S),'remaining=',len(missing))
    print('first missing:',missing[:12])
if __name__=='__main__':
    main()
