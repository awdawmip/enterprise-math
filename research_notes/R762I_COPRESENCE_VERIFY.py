#!/usr/bin/env python3
"""R762I parallel carrier occupancy: exact source-labeled event-order census.
Not a native TRIADIC_CLOSURE_E force admission or physical time law."""
import itertools
import json
import math
from collections import Counter
SOURCES=range(3)
events=tuple((i,d) for i in SOURCES for d in ('O','I'))
rows=[]
for seq in itertools.permutations(events):
    if not all(seq.index((i,'O'))<seq.index((i,'I')) for i in SOURCES):
        continue
    live=set()
    peak=0
    visits=[]
    for i,d in seq:
        if d=='O':
            assert i not in live
            live.add(i)
        else:
            assert i in live
            live.remove(i)
        peak=max(peak,len(live))
        visits.append(tuple(sorted(live)))
    assert not live
    rows.append((seq,peak,visits))
counts=Counter(peak for _,peak,_ in rows)
assert len(rows)==90 and counts=={1:6,2:48,3:36}
assert all((peak==3)==(set(seq[:3])=={(i,'O') for i in SOURCES}) for seq,peak,_ in rows)
assert all(peak<3 or sum(len(v)==3 for v in visits)==1 for _,peak,visits in rows)

def count(n):
    states={(0,0,0):1}  # opened mask, closed mask, peak
    for t in range(2*n):
        next_states=Counter()
        for (opened,closed,peak),v in states.items():
            for i in range(n):
                bit=1<<i
                if not opened&bit:
                    next_states[(opened|bit,closed,max(peak,(opened|bit).bit_count()-closed.bit_count()))]+=v
                elif not closed&bit:
                    next_states[(opened,closed|bit,peak)]+=v
        states=next_states
    assert all(o==c==(1<<n)-1 for o,c,_ in states)
    return Counter({k:v for (o,c,k),v in states.items()})

for n in range(1,7):
    h=count(n)
    assert sum(h.values())==math.factorial(2*n)//(2**n)
    assert h[n]==math.factorial(n)**2
assert count(3)==counts
result={
  "schema":"R762I_THREE_CARRIER_COPRESENCE_CENSUS_V1",
  "status":"AUTHOR_SIDE_EXACT_COMBINATORICS_NOT_NATIVE_FORCE_EVENT",
  "n3_ordered_source_chains":3,
  "valid_serial_event_schedules":90,
  "maximum_concurrent_port_occupancy_histogram":{str(k):v for k,v in sorted(counts.items())},
  "full_triad_copresence_schedules":36,
  "no_full_triad_copresence_schedules":54,
  "n_general_total":"(2n)!/2^n",
  "n_general_full_copresence":"(n!)^2",
  "n_general_full_copresence_fraction":"2^n/binomial(2n,n)",
  "coverage":"all 6!=720 permutations filtered by 3 precedence constraints, plus DP n=1..6",
  "physical_force_incidence":"UNTESTED",
  "heartbeat_time_and_V29_V39":"NOT_EXECUTED"
}
print(json.dumps(result,indent=2,sort_keys=True))
