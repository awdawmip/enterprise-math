#!/usr/bin/env python3
"""Exhaustive 0..9-step V17 directed-ledger holonomy fibers; exact integers only.
No claim of native TRIADIC_CLOSURE_E Cell/Link/Port admissibility.
"""
from itertools import permutations
from collections import defaultdict, Counter
import json

AXES = tuple(range(1,7))
FRAMES = tuple(permutations(AXES,3))
FRAME_INDEX = {f:i for i,f in enumerate(FRAMES)}
ARCS = tuple((a,b) for a in AXES for b in AXES if a != b)
ARC_INDEX = {a:i for i,a in enumerate(ARCS)}
BASE = FRAME_INDEX[(1,2,3)]
SLOT_BITS = 7
COUNT_BITS = 4  # 0..9 fits; no packed-digit carry for the checked horizon
STEPS = tuple(tuple((FRAME_INDEX[f[:p]+(b,)+f[p+1:]],1 << (COUNT_BITS*ARC_INDEX[(f[p],b)]))
                    for p in range(3) for b in AXES if b not in f) for f in FRAMES)
assert len(FRAMES) == 120 and len(ARCS) == 30
assert all(len(x) == 9 for x in STEPS)

W8 = (
 '123 523 521 523 513 523 123 423 123',
 '123 423 413 453 451 452 412 432 132',
 '123 523 521 523 513 543 143 243 213',
 '123 523 521 524 514 534 134 234 231',
 '123 523 513 543 541 542 142 342 312',
 '123 523 521 524 514 524 124 324 321',
)
W9 = (
 '123 523 521 523 543 513 523 513 523 123',
 '123 523 513 523 521 541 542 512 532 132',
 '123 523 521 523 543 143 243 143 243 213',
 '123 143 243 241 245 215 235 135 235 231',
 '123 523 513 523 521 541 542 142 342 312',
 '123 143 243 241 245 145 345 315 325 321',
)

def ledger(path):
    frames = [tuple(map(int,word)) for word in path.split()]
    assert frames[0] == (1,2,3) and set(frames[-1]) == {1,2,3}
    counts = [0]*30
    for f,g in zip(frames,frames[1:]):
        changes = [i for i in range(3) if f[i] != g[i]]
        assert len(changes) == 1
        p = changes[0]
        assert g[p] not in f
        counts[ARC_INDEX[(f[p],g[p])]] += 1
    return tuple(counts),frames[-1]

for family in (W8,W9):
    assert len({ledger(path)[0] for path in family}) == 1
    assert {ledger(path)[1] for path in family} == set(permutations((1,2,3)))
    assert all(len(path.split()) == len(family[0].split()) for path in family)

expected = {
 0:(1,1,[(1,1)],1), 1:(0,0,[],9),
 2:(9,9,[(1,9)],63), 3:(36,36,[(1,36)],411),
 4:(369,171,[(1,171)],2403),
 5:(2952,684,[(1,540),(2,144)],12888),
 6:(26937,2571,[(1,1563),(2,936),(4,72)],63471),
 7:(239148,8748,[(1,3276),(2,4392),(3,360),(4,486),(5,234)],288495),
 8:(2155617,28209,[(1,7281),(2,13461),(3,1314),(4,3258),(5,1872),(6,1023)],1202043),
 9:(19371024,84996,[(1,11958),(2,38622),(3,4236),(4,10608),(5,8670),(6,10902)],4549824),
}

def run():
    # State key encodes (30 exact counts, ordered frame). Merge only identical pairs.
    states = {BASE:1}
    table=[]
    for m in range(10):
        fibers=defaultdict(set)
        based_paths=0
        for key,multiplicity in states.items():
            frame=FRAMES[key&127]
            if set(frame)=={1,2,3}:
                fibers[key>>SLOT_BITS].add(frame)
                based_paths += multiplicity
        size_hist=Counter(map(len,fibers.values()))
        got=(based_paths,len(fibers),sorted(size_hist.items()),len(states))
        assert got==expected[m], (m,got,expected[m])
        table.append({'m':m,'all_paths':9**m,'based_return_paths':based_paths,
          'distinct_directed_ledgers':len(fibers),
          'holonomy_fiber_sizes':dict(sorted(size_hist.items())),
          'max_holonomies_per_ledger':max(size_hist,default=0),
          'worst_case_repair_bits': (max(size_hist,default=1)-1).bit_length(),
          'state_keys':len(states)})
        if m==9:break
        new_states=defaultdict(int)
        for key,multiplicity in states.items():
            frame_index=key&127
            h=key>>SLOT_BITS
            for new_frame,delta in STEPS[frame_index]:
                new_states[((h+delta)<<SLOT_BITS)|new_frame]+=multiplicity
        states=new_states
    print(json.dumps({
      'schema':'ENTERPRISE_MATH_R762BX_V17_UNIFORM_LEDGER_REPAIR_V1',
      'task_id':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
      'model':'conditional ordered V17 three-slot label replacements; full directed axis-context ledger',
      'base_frame':[1,2,3], 'axis_count':6, 'arcs':30, 'exact_horizon':'m=0..9',
      'verification':'full exact enumeration of every reachable (frame,H) plus path multiplicity',
      'table':table,
      'witness_8':list(W8),'witness_9':list(W9),
      'all_m_ge_8_proof':'m=8 and 9 six-fiber witnesses; append identical 2-step 1->4->1 or 3-step 1->4->5->1 slot loops after each witness; every integer >=10 is 8+2a+3b',
      'status':'AUTHOR_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED',
      'native_event_predicate':'UNRESOLVED'
    },ensure_ascii=False,indent=2))

if __name__ == '__main__':run()
