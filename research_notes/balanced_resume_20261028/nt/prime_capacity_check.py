#!/usr/bin/env python3
"""Small exact check of the finite part; not a proof of Nagura's theorem."""
import json
from math import isqrt
from pathlib import Path

T = (1, 2, 3, 4, 6, 9)

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

PRIMES = tuple(q for q in range(5, 228) if prime(q))
assert PRIMES[-1] == 227

def classes(h):
    # Every nonzero state has q <= h, so q <= 225 suffices in this range.
    # The certified prime 227 supplies the zero state for every h <= 225.
    return {max((0,) + tuple(t for t in T if q*t <= h)) for q in PRIMES}

tables = [
    (45, 62, {1:[23,31,37], 2:[17,23], 3:[13,17], 4:[11], 6:[7]}),
    (66, 225, {1:[61,113], 2:[31,43,61,89], 3:[19,23,29,37,47,61],
               4:[13,19,23,31,43], 6:[11,13,19,23,31]})
]
interval_tables = []
for lo,hi,table in tables:
    rows=[]
    for t,qs in table.items():
        u=T[T.index(t)+1]
        assert all(prime(q) and q>=5 for q in qs)
        intervals=[(q*t,q*u-1) for q in qs]
        assert all(any(a<=h<=b for a,b in intervals) for h in range(lo,hi+1))
        rows.append({'state':t,'primes':qs,'intervals':intervals})
    interval_tables.append({'range':[lo,hi],'rows':rows})

counts={h:len(classes(h)) for h in range(1,226)}
assert classes(27)=={0,1,2,3,4}
assert classes(28)=={0,1,2,4}
assert all(counts[h]==6 for h in (63,64,65))
assert all((counts[h]==7)==(45<=h<=62 or h>=66) for h in counts)
result={
    'status':'EXACT_FINITE_CHECK_PASS',
    'thresholds_checked':225,
    'finite_prime_bound':227,
    'prime_count':len(PRIMES),
    'all_finite_primes':PRIMES,
    'capacity_27':counts[27], 'capacity_28':counts[28],
    'capacity_62':counts[62], 'capacity_63':counts[63],
    'last_nonfull_in_checked_range':max(h for h in counts if counts[h]<7),
    'finite_full_capacity_ranges':[[45,62],[66,225]],
    'interval_tables':interval_tables,
    'counts':counts,
    'infinite_tail':'PAPER_PROOF_USING_NAGURA_X_GT_25_NOT_FINITE_SCAN',
    'old_scientific_runs_repeated':False
}
path=Path(__file__).with_name('prime_capacity_check_result.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['counts','interval_tables','all_finite_primes']},indent=2))
