#!/usr/bin/env python3
"""Independent exact min-plus subset convolution on all 2^18 future subsets.
Requires unchanged VERIFY_EC49FNY_INDEPENDENT.py from PR #2343.
Usage: python VERIFY_ALL_SUBSETS.py master_and_radius3_cases.txt
"""
import hashlib
import sys
from pathlib import Path
import VERIFY_EC49FNY_INDEPENDENT as native

MASKS=(0,5,138,8192)
H_EXPECTED=(59,75,89,102,113,118,126,131,134,137,140,143,146,149,151,153,155,156)
MASTER_SHA="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
INF=10**9

def check(source):
    assert hashlib.sha256(source.read_bytes()).hexdigest()==MASTER_SHA
    words,keys=native.frozen(source,case=32279)
    profiles={r:native.table(words,keys,r) for r in native.ROOTS}
    used=0
    for m in MASKS:
        assert used&m==0
        used|=m
    U=tuple(l for l in range(24) if not used>>l&1)
    assert len(U)==18
    N=1<<len(U)
    dp=[INF]*N
    dp[0]=0
    for j,r in enumerate(native.ROOTS):
        names,indices,D,nodes=profiles[r]
        bit=[1<<indices[l] if l in indices else 0 for l in U]
        eligible=sum(1<<i for i,b in enumerate(bit) if b)
        base=0
        for l in range(24):
            if MASKS[j]>>l&1:base|=1<<indices[l]
        mapped=[0]*N
        cost=[INF]*N
        cost[0]=D[base]
        for s in range(1,N):
            q=s&-s
            i=q.bit_length()-1
            mapped[s]=mapped[s^q]|bit[i]
            if s&~eligible==0:
                cost[s]=D[base|mapped[s]]
        nxt=[INF]*N
        for s in range(N):
            subset=s&eligible
            t=subset
            while True:
                candidate=dp[s^t]+cost[t]
                if candidate<nxt[s]:nxt[s]=candidate
                if t==0:break
                t=(t-1)&subset
        dp=nxt
    H=tuple(max(dp[s] for s in range(1,N) if s.bit_count()==h)
            for h in range(1,len(U)+1))
    assert H==H_EXPECTED
    assert sum(dp[s]>155 for s in range(1,N))==1
    assert dp[N-1]==156
    print("EC49FOC_ALL_SUBSETS_PASS",N,"H",H,"strict_subsets",1)

if __name__=="__main__":
    assert len(sys.argv)==2
    check(Path(sys.argv[1]))
