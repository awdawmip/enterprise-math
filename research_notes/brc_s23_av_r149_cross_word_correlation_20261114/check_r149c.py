#!/usr/bin/env python3
"""R149C exhaustive integer gcd-waveform period/visibility check."""
from math import gcd
import json

def scaled_h(g,s,t,u,v,h):
    # 4*g*n*m*H at the same gcd and unit residue slopes (n,m irrelevant)
    return sum((2*((s*j+u)%g)-(g-1))*(2*((t*(j+h)+v)%g)-(g-1)) for j in range(g))

def period(seq):
    g=len(seq)
    return next(p for p in range(1,g+1) if all(seq[h]==seq[(h+p)%g] for h in range(g)))

cases=0
zeros_at_lag0=0
for g in range(2,13):
    units=[a for a in range(1,g) if gcd(a,g)==1]
    for s in units:
        for t in units:
            for u in range(g):
                for v in range(g):
                    seq=[scaled_h(g,s,t,u,v,h) for h in range(g)]
                    assert sum(seq)==0, (g,s,t,u,v)
                    assert period(seq)==g, (g,s,t,u,v,seq)
                    assert any(x!=0 for x in seq)
                    if seq[0]==0: zeros_at_lag0+=1
                    cases+=1
assert [scaled_h(5,1,1,0,1,h) for h in range(5)]==[0,-20,-20,0,40]
print(json.dumps({'status':'R149C_FULL_GCD_LAG_SUPPORT_PASS',
    'gcd_range':[2,12],
    'all_unit_slope_offset_cases':cases,
    'zero_lag_cases_with_nonzero_lag':zeros_at_lag0,
    'g5_zero_lag_exact_scaled_wave':[0,-20,-20,0,40]},indent=2))
