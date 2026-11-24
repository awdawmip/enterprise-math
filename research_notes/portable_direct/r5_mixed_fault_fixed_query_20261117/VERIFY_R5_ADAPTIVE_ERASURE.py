#!/usr/bin/env python3
"""R5 exact retry-policy adversarial-erasure dynamic program."""
from functools import lru_cache
BUDGETS=(214,223,294)
@lru_cache(None)
def worst(i,e):
    if i==len(BUDGETS): return 0
    k=BUDGETS[i]
    answered=k+worst(i+1,e)
    return max(answered,k+worst(i,e-1)) if e else answered

for e in range(16):
    assert worst(0,e)==731+294*e,(e,worst(0,e))
print("PASS_R5_ADAPTIVE_VISIBLE_ERASURE_ALL_E_STRUCTURAL_AND_0_TO_15_RETRY_DP")
