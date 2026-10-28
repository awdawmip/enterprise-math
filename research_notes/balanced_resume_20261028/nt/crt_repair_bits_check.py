#!/usr/bin/env python3
"""Enumerate actual six-cell payloads and group their full prefix signatures."""
import json
from collections import defaultdict
from pathlib import Path

K=(10,1,4,5,11,14)

def compositions(total,n):
    if n==1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in compositions(total-a,n-1):
                yield (a,)+tail

def baseline(x):
    a,b,c,d,e,f=x
    return (a+b+c,d+e+f,a+d,b+e,c+f,b+c)

results=[]
total_checked=0
for mass in range(13):
    fibers=defaultdict(set)
    for x in compositions(mass,6):
        sig=tuple(sum(v for v,k in zip(x,K) if k<h) for h in range(16))
        fibers[baseline(x)].add(sig)
        total_checked+=1
    for s,sigs in fibers.items():
        r1,r2,g0,g1,g4,carry=s
        lo=max(0,carry-g4);hi=min(carry,g1)
        assert r1+r2==g0+g1+g4
        assert r1>=carry and g0-r1+carry>=0
        assert len(sigs)==hi-lo+1
        assert {sig[3] for sig in sigs}==set(range(lo,hi+1))
    maximum=max(map(len,fibers.values()))
    assert maximum==mass//2+1
    results.append({'mass':mass,'baseline_count':len(fibers),'max_fiber':maximum,
                    'worst_bits':(maximum-1).bit_length()})

out={'status':'EXACT_ENUMERATION_PASS','payloads_checked':total_checked,
     'mass_range':[0,12],'all_16_prefixes_compared':True,'results':results,
     'general_mass_claim':'PAPER_PROOF_NOT_EXTRAPOLATION_FROM_SCAN',
     'old_scientific_runs_repeated':False}
Path(__file__).with_name('crt_repair_bits_check_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
