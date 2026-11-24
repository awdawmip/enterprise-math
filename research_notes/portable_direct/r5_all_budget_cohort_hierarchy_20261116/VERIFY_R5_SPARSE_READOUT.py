#!/usr/bin/env python3
"""Independent sparse-evaluator check for the R5 all-budget cohort JSON on stdin.
Usage: python VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py | python VERIFY_R5_SPARSE_READOUT.py
"""
import sys,json
D=json.load(sys.stdin)
rows=D['all_budget_coefficients']
assert len(rows)==101
assert {int(k) for k in rows}==set(range(214,315))
union=set(); entries=0;checked=0
for k,record in rows.items():
    a={int(t):int(v) for t,v in record.items()}
    assert a and all(v>0 and 0<=t<256 for t,v in a.items())
    union.update(a);entries+=len(a)
    dense=[a.get(t,0) for t in range(256)]
    for i in range(8):
        for t in range(256):
            if t&(1<<i):dense[t]+=dense[t^(1<<i)]
    for b in range(256):
        sparse=sum(v for t,v in a.items() if (t&b)==t)
        assert sparse==dense[b],(k,b)
        checked+=1
assert len(union)==25 and entries==512
assert checked==25856
print(json.dumps({'status':'PASS_R5_SPARSE_READOUT_ALL_25856','stored_nonzero_integer_coefficients':entries,'dense_count_values':checked,'entry_ratio':50.5,'total_distinct_requirement_masks':len(union)},sort_keys=True))
