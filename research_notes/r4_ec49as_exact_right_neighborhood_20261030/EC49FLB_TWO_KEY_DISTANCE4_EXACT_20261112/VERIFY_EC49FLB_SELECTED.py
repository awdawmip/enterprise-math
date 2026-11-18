#!/usr/bin/env python3
"""Independently check six EC49FLB cases with EC49FKY Python native-trie code."""
from pathlib import Path
import os,sys,json
HERE=Path(__file__).resolve().parent
PRIOR=HERE.parent/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112'
# Reuse the earlier independently implemented Python DP, not C++.
sys.path.insert(0,str(PRIOR))
previous=os.getcwd()
try:
    os.chdir(PRIOR)  # previous module loads its own exact stored input
    import VERIFY_SCAN_INDEPENDENT as verifier
finally:
    os.chdir(previous)
cases=json.loads((HERE/'EC49FLB_CASE_INDEX.json').read_text())
expected=json.loads((HERE/'COSTS_EC49FLB.json').read_text())['costs_in_order']
assert len(cases)==len(expected)==410
verifier.SETS=[{'keyset':s['keyset']} for s in cases]
verifier.CPP={i:v for i,v in enumerate(expected)}
for i in [6,14,222,234,266,300]:
    verifier.verify(i)
print('EC49FLB_SELECTED_INDEPENDENT_TRIE_PASS')
