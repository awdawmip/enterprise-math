#!/usr/bin/env python3
"""R270: exact positive BRC finite certificate, formal slots only."""
from collections import Counter
from itertools import product
import json

EDGE={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
NEXT=((1,0),(2,0),(2,2))
CHANNELS=tuple((q,h) for q in range(3) for h in (0,1))
BASE={7:((1,-3),(2,2,3,1,1,9)),8:((1,0),(1,6,1,9,2,16)),9:((-1,-1),(1,19,2,20,4,28))}
def step(s,a):
    q,r,e,k=s;t,z,b=EDGE[q][int(a)]
    return t,NEXT[r][int(a)],z*e,z*k+b
def walk(w):
    x=(0,0,1,0)
    for a in w:x=step(x,a)
    return x
def propagate(old):
    new=Counter()
    for state,c in old.items():
        for a in (0,1):new[step(state,a)]+=c
    return new
def channel_fiber(p,g):
    count=Counter()
    for (q,r,e,k),v in p.items():
        if (e,k)==g:count[(q,int(r==2))]+=v
    return tuple(count[c] for c in CHANNELS)
def main():
    p=Counter({(0,0,1,0):1}); samples={}
    for n in range(161):
        assert sum(p.values())==2**n
        if n<=12:
            raw=Counter(walk(word) for word in product('01',repeat=n))
            assert raw==p
        if n==30:assert p[(0,0,1,-4)]==16482
        if n>=7:
            K=(n-7)//30;t=n-30*K;j=7+(t-7)%3;h=(t-j)//3
            (e,k),b=BASE[j];g=(e,k-e*(4*K+h))
            got=channel_fiber(p,g)
            assert all(got[c]>=16482**K*b[c] for c in range(6))
            if n in BASE:assert got==BASE[n][1]
            if n in (7,8,9,30,37,38,39,67,97,160):
                samples[str(n)]={"K":K,"j":j,"h":h,"effect":g,"six_channel_counts":got}
        if n<160:p=propagate(p)
    assert walk('101')==(0,0,1,-1)
    print(json.dumps({"status":"PASS","depth":"0..160","brute_word_count":8191,
          "reset_count_length30_effect_plus_minus4":16482,"samples":samples,
          "scope":"formal positive BRC; author-only; not native X6"},indent=2))
if __name__=="__main__":main()
