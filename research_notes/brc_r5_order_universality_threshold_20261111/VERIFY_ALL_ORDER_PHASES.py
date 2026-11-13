#!/usr/bin/env python3
"""R5 complete rational phase scan: 1145 subset thresholds, 1144 live jumps.
Imports the same frozen parent witness and threshold census, Python stdlib only.
"""
import contextlib, io, runpy, hashlib
from pathlib import Path
from math import factorial
from fractions import Fraction as F

with contextlib.redirect_stdout(io.StringIO()):
    p=runpy.run_path(str(Path(__file__).with_name("VERIFY_ORDER_THRESHOLD.py")))
phase=p["phase"]; thresholds=p["thresholds"]
T=p["T"]; eps_max=p["eps_max"]
assert T==32768 and len(phase)==1145

# rank[S] is the index (one-based) of the exact first-zero value for subset S.
# If no coordinate hits zero in the ray, the sentinel is len(phase)+1.
rank=[len(phase)+1]*T
for n,q in enumerate(phase,1):
    for mask,coord in thresholds[q]:
        assert rank[mask]==len(phase)+1
        rank[mask]=n
assert sum(r<=len(phase) for r in rank)==25958
assert rank[0]==len(phase)+1

# At epsilon strictly above the i-th breakpoint, exactly the masks with
# rank <= i have become infeasible. The chain DP counts every legal order once.
def count_orders(after):
    w=[0]*T;w[0]=1
    for mask in range(1,T):
        if rank[mask]<=after: continue
        s=0;z=mask
        while z:
            bit=z&(-z)
            s+=w[mask^bit]
            z^=bit
        w[mask]=s
    return w[-1]

counts=[count_orders(i) for i in range(len(phase))]
assert counts[0]==factorial(15)
assert counts[1]==1307238912000
assert counts[2]==1307021184000
assert counts[-1]==3514190816
assert all(counts[i]>counts[i+1] for i in range(len(counts)-1))
losses=[counts[i-1]-counts[i] for i in range(1,len(counts))]
largest=max(losses);largest_phase=losses.index(largest)+1
assert (largest,largest_phase)==(380759849184,607)
assert (counts[606],counts[607])==(851207682192,470447833008)
assert eps_max*phase[largest_phase-1]==F(155682221,377131868400000000)
assert sum(losses)==counts[0]-counts[-1]
assert phase[-1]==1

# Deterministic full ledger, reconstructed by the verifier on demand.
rows=[f'{i} {eps_max*phase[i-1]} {counts[i-1]} {counts[i] if i<len(counts) else "ENDPOINT"}'
      for i in range(1,len(phase)+1)]
digest=hashlib.sha256(("\n".join(rows)+"\n").encode()).hexdigest()
print("DISTINCT_FEASIBILITY_THRESHOLDS_ON_CLOSED_RAY",len(phase))
print("DISTINCT_SUBSET_MASKS_HITTING_THRESHOLD",sum(r<=len(phase) for r in rank))
print("INTERIOR_BREAKPOINTS_WITH_TRUE_ORDER_COUNT_DROP",len(phase)-1)
print("INTERIOR_REDUNDANT_BREAKPOINTS",0)
print("FIRST_UNIVERSAL_THRESHOLD",eps_max*phase[0])
print("ALL_PERMUTATIONS_AT_START",counts[0])
print("AFTER_FIRST_THRESHOLD",counts[1])
print("AFTER_SECOND_THRESHOLD",counts[2])
print("LARGEST_DROP_PHASE",largest_phase)
print("LARGEST_DROP_EPSILON",eps_max*phase[largest_phase-1])
print("LARGEST_DROP_EXACT",largest)
print("LARGEST_DROP_COUNT_BEFORE",counts[largest_phase-1])
print("LARGEST_DROP_COUNT_AFTER",counts[largest_phase])
print("ENDPOINT_VALID_PERMUTATIONS",counts[-1])
print("CANONICAL_PHASE_LEDGER_SHA256",digest)
print("PASS_R5_EXACT_ALL_1144_INTERIOR_ORDER_COUNT_TRANSITIONS")
