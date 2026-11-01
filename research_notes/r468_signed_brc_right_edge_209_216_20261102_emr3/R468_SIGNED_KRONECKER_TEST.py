#!/usr/bin/env python3
"""Independent signed polynomial multiplication regression for R468 exact engine."""
import json,random
import R468_EXACT_KERNEL as k
seed=20261102
rng=random.Random(seed)
case_count=0
max_degree=0
for length in (36, 48, 72):
    for _ in range(40):
        bits=rng.choice([0,10,40,120,300])
        bound=1<<bits
        a=[rng.randrange(-bound,bound+1) for _ in range(length)]
        b=[rng.randrange(-bound,bound+1) for _ in range(length+5)]
        assert k.mul(a,b)==k.slow(a,b)
        case_count+=1;max_degree=max(max_degree,len(a)+len(b)-2)
# Independently exercise the pure-Python signed Kronecker path for large polynomials.
lib=k._lib
k._lib=None
for length in (36,48):
    for _ in range(10):
        a=[rng.randrange(-10**10,10**10) for _ in range(length)]
        b=[rng.randrange(-10**10,10**10) for _ in range(length+3)]
        assert k.mul(a,b)==k.slow(a,b)
        case_count+=1
k._lib=lib
result={'schema':'R468_KRONECKER_MULTIPLICATION_TEST_V1','result':'EXACT_PASS','deterministic_seed':seed,'cases':case_count,'cases_gmp':120,'cases_python_fallback':20,'tested_signed_coefficients':True,'max_degree':max_degree,'integer_arithmetic_only':True}
open('R468_KRONECKER_TEST_EVIDENCE.json','w').write(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
