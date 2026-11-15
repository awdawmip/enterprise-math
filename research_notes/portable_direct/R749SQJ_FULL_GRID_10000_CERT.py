#!/usr/bin/env python3
"""Exact full-grid Kolmogorov comparison for every 1<=r<=10000."""
from math import prod
import json

M={1:3,2:4,3:6,4:4,5:3,6:2,7:1}
LIMIT=10000
q=[0]*LIMIT
q[0]=1
for w,n in M.items():
    for _ in range(n):
        for t in range(w,LIMIT):
            q[t]+=q[t-w]
C=[0]*(LIMIT+1)
for r in range(1,LIMIT+1):
    C[r]=C[r-1]+q[r-1]
P=[r**23 for r in range(LIMIT+1)]
assert prod(w**n for w,n in M.items())==94058496000
for t in range(1,LIMIT):
    assert C[t+1]*P[t]<=C[t]*P[t+1],t
# Normalized-count monotonicity and exact monotonic p_k prove every
# post-jump CDF discrepancy is at most p_0, for all r<=LIMIT.
negative_endpoints=0
for r in range(1,LIMIT+1):
    atom=C[r]-(C[r-3] if r>3 else 0)
    cap=atom*P[r]
    for k in range(1,(r-1)//3+1):
        t=r-3*k
        # Pre-jump negative deviation is C_t/C_r-(t/r)^23.
        assert C[t]*P[r]-P[t]*C[r] <= cap,(r,k)
        negative_endpoints+=1
print(json.dumps({
 "result":"PASS","frozen_science":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
 "all_positive_integer_r_verified":[1,LIMIT],
 "ratio_monotonicity_inequalities":LIMIT-1,
 "negative_endpoint_integer_comparisons":negative_endpoints,
 "positive_endpoints":"PROVED_IN_RANGE_BY_NORMALIZED_RATIO_MONOTONICITY_AND_SOURCE_COUNT_INJECTION",
 "conclusion":"EXACT_KOLMOGOROV_MAXIMUM_AT_ZERO_ATOM_FOR_ALL_1_LE_R_LE_10000",
 "larger_r":"EVENTUAL_THEOREM_WITH_UNSPECIFIED_CUTOFF; global all-r claim remains open"
},indent=2,sort_keys=True))
