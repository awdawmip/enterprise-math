#!/usr/bin/env python3
"""Deterministically recover all exact priced-signature classes and multiplicities.
Input is the stdout of R5_TWO_MORE_F01_CENSUS.cpp, no floating-point or hashes.
"""
import sys
from collections import Counter
pairs={}
counts=Counter()
inp=sys.argv[1] if len(sys.argv)>1 else "R5_TWO_MORE_F01_RESULTS.csv"
for line in open(inp):
    if line.startswith('#') or not line.strip():continue
    t,u,c,*values=map(int,line.strip().split(','))
    pairs.setdefault(c,(t,u))
    counts[c]+=1
assert len(pairs)==1490 and sum(counts.values())==30628
assert set(pairs)==set(range(1490))
with open("R5_TWO_MORE_REPS.csv","w") as f:
    for c in range(1490):
        t,u=pairs[c]
        f.write(f"{c},{t},{u},{counts[c]}\n")
print("PASS_R5_REPS",len(pairs),sum(counts.values()))
