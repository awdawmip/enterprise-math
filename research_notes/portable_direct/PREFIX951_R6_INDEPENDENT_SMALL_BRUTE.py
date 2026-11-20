#!/usr/bin/env python3
"""Independent integer brute force for PREFIX-951 and Newton/Euler cross-check."""
import json
from pathlib import Path

def brute_diagonal(bits, core):
    half, mod = 1 << (bits-1), 1 << bits
    survivors, missing = [], []
    for a in range(half+1, mod, 2):
        valid = []
        for i in range(bits):
            for j in range(bits):
                d = (core*a ^ (1<<j)) - (1<<i)
                if d>0 and d%a==0:
                    valid.append((i,j,d//a))
        if valid:
            survivors.append(a)
        else:
            missing.append(a)
    return survivors, missing

def predicted_missing(bits, core):
    mod = 1<<bits
    h = 1<<(bits-1)
    e = (-pow(core, -1, mod))%mod
    return e if h<e<mod and not (e==h+1 and (core-(h-1))%mod==0) else None

small = []
for bits in range(3,9):
    half,mod = 1<<(bits-1),1<<bits
    for core in range(1,2*mod,2):
        present, missing = brute_diagonal(bits,core)
        ex = predicted_missing(bits,core)
        assert missing == ([ex] if ex is not None else []), (bits,core,missing,ex)
        assert len(present)+len(missing)==(1<<(bits-2))
        small.append((bits,core, len(missing)))

# Python's pow inverse and a direct modular inverse recurrence independent of C++ Newton steps
m=1<<19
ks=list(range(1,8192,2))
exc=[]
for k in ks:
    inv=pow(k,-1,m)
    assert (k*inv)%m == 1
    e=(-inv)%m
    if 1<<18 <e<m:
        exc.append(e)
assert len(exc)==2051 and len(set(exc))==2051
assert 131072-len(exc)==129021
for k in [1,3,5,7,9,11,15,17,19,21,23,8191]:
    e=(-pow(k,-1,m))%m
    print('k',k,'excluded',e if e>1<<18 else None,'pair_count',131072-(e>1<<18))
res={
 'schema':'PREFIX951_DIAGONAL_CORE_SATURATION_Q19_V1',
 'small_bruteforce':{
    'bit_widths':list(range(3,9)), 'odd_core_range':'1..(2^(bits+1)-1)',
    'test_cases':len(small),'max_bit_width':8,
    'all_direct_i_j_positive_quotient_tests_match':True,
    'rescue_case_bits7_core63_a65':(63*65^(1<<0))-(1<<6),
 },
 'Q19':{'all_odd_core_max':8191,'core_count':len(ks),'exception_count':len(exc),
        'universally_covered_diagonal_pairs':131072-len(exc),
        'at_most_one_core_missing_per_diagonal':True,
        'exception_values_first_16':sorted(exc)[:16],
        'exception_values_last_16':sorted(exc)[-16:]},
}
assert res['small_bruteforce']['rescue_case_bits7_core63_a65'] == 62*65
out=Path(__file__).with_name('prefix951_independent_results.json')
out.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'small_test_cases':len(small),'exceptional_count':len(exc),'universal_diagonals':131072-len(exc)}))
