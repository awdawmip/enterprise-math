#!/usr/bin/env python3
"""Independent integer coefficient DP, no 5-tuple enumeration or floating point."""
from pathlib import Path
from collections import defaultdict
from math import comb
P=Path(__file__).resolve().parent
data=(P/'MASKS_EC49FMB.txt').read_text().split()
n,full=map(int,data[:2])
rows=[(int(data[i]),int(data[i+1])) for i in range(2,len(data),2)]
assert n==92 and len(rows)==n and sum(seed for _,seed in rows)==5
dp=[defaultdict(int) for _ in range(6)]
dp[0][(0,0)]=1
for i,(mask,seed) in enumerate(rows):
    for k in range(min(i+1,5),0,-1):
        for (old,ss),num in list(dp[k-1].items()):
            dp[k][(old|mask,ss+seed)]+=num
expected=(1,192,6315,38169,62620,1137)
cover_by_key_count=[]
for k in range(6):
    cover_by_key_count.append(sum(num for (mask,ss),num in dp[k].items() if mask==full))
assert cover_by_key_count==[0,0,0,16,2004,108434]
cover=[]
for r in range(6):
    total=sum(num for (mask,ss),num in dp[5].items() if 5-ss==r)
    feasible=sum(num for (mask,ss),num in dp[5].items() if 5-ss==r and mask==full)
    assert total==comb(5,r)*comb(87,r)
    cover.append(feasible)
    print(r,total,feasible)
assert tuple(cover)==expected and sum(cover)==108434
print('GLOBAL_COEFFICIENT_DP_PASS',sum(cover),len(dp[5]),cover_by_key_count)
