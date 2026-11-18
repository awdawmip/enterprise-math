#!/usr/bin/env python3
"""Finite exact q=9 h=7/h=8 127-window period tests on the 85-state BRC quotient.

No full 729-state high-index convolution is needed. The result is a finite
certificate; separately verified spectral recurrence is needed for all n.
"""
import argparse
import json
import sys
sys.set_int_max_str_digits(100000)
from time import perf_counter
from R762FD_Q9_SIX_BRANCH_ORBIT_VERIFY import build


def verify(h):
    q=9
    L,N={7:(13122,26),8:(39366,27)}[h]
    r=127
    _,keys,T,_=build(q)
    assert len(keys)==85 and L%q==0
    f=lambda n:max(0,n//3-2)
    K=f(N+r-1+L)+h
    modulus=3**K
    states={}
    v=[int(k==(0,0,0)) for k in keys]
    indices=set(range(N-1,N+r)) | {n+L for n in range(N-1,N+r)}
    start=perf_counter()
    for n in range(N+r-1+L+1):
        if n in indices:
            states[n]=v[:]
        if n==N+r-1+L:
            break
        v=[sum(v[j] for j in row)%modulus for row in T]
    recurrence_seconds=perf_counter()-start

    checks=0
    bad=[]
    first_preperiod_witnesses=[]
    scale=3**(L//3)
    for n in range(N-1,N+r):
        power=3**(f(n+L)+h)
        for k,(a,b) in enumerate(zip(states[n],states[n+L])):
            equal=(b-scale*a)%power==0
            checks+=1
            if n<N:
                if not equal and len(first_preperiod_witnesses)<5:
                    first_preperiod_witnesses.append({
                       "n":n,"orbit_index":k,"key":list(keys[k]),
                       "normalized_residue_low":(a//3**f(n))%3**h,
                       "normalized_residue_high":(b//3**f(n+L))%3**h})
            elif not equal:
                bad.append((n,k))
    assert not bad, bad[:3]
    assert first_preperiod_witnesses,'expected first excluded n to fail'
    return {
       "h":h,"q":q,"L":L,"N":N,"window_n":[N,N+r-1],
       "first_excluded_n":N-1,"first_excluded_witnesses_first_five":first_preperiod_witnesses,
       "modulus_power_3_exponent":K,"modulus_decimal_digits":len(str(modulus)),
       "orbit_classes":len(keys),"matrix_nonzero_entries":405,
       "full_terminal_comparisons_in_window":729*r,
       "reduced_orbit_comparisons_in_window":85*r,
       "congruences_checked_including_excluded_time":checks,
       "periodic_window_result":"PASS",
       "excluded_time_result":"NONPERIODIC_WITNESS_VERIFIED",
       "seconds_full_run_local":round(perf_counter()-start,3),
       "seconds_orbit_recurrence_local":round(recurrence_seconds,3)
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--h',type=int,choices=[7,8],required=True)
    args=p.parse_args()
    print(json.dumps({"schema":"R762FD_Q9_STATIONARY_85_PERIOD_WINDOW_V1",
      "result":verify(args.h),
      "arithmetic":"Python exact integers modulo 3^K; all 85 orbit states computed from the six original BRC steps",
      "mathematical_scope":"Finite 127-window only; general all-n period uses earlier author-side spectral recurrence (NOT_REVIEWED)",
      "review":"NOT_REVIEWED"},sort_keys=True,indent=2))


if __name__=='__main__':
    main()
