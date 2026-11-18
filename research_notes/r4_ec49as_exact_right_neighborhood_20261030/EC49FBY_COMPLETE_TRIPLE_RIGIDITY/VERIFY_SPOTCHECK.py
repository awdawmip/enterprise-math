#!/usr/bin/env python3
"""Independent tuple-prefix implementation for selected EC49FBY triples."""
from itertools import product
from VERIFY_EC49FBY import candidates,W,observe,STEPS
def native(w):
    path=()
    out=set()
    for op in w:
        for x in STEPS[op]:
            path=path+(x,)
            out.add(path)
    return out
w={f'{h}:{observe(t)}':t for h,words in W.items() for t in words}
tests=[('4:1','7:1','7:4'),('7:1','7:2','7:4'),('7:1','7:4','8:4')]
for slots in tests:
    rest=set().union(*(native(v) for k,v in w.items() if k not in slots))
    cut=158-len(rest)
    pools=[[(native(x)-rest) for x in candidates(int(k.split(':')[0]))[int(k.split(':')[1])]] for k in slots]
    filtered=[[a for a in p if len(a)<cut] for p in pools]
    best=158
    for a,b,c in product(*filtered):
        best=min(best,len(rest|a|b|c))
    assert best==158
    print('SET_TRIPLE',slots,'minimum',best,'filtered_counts',[len(p) for p in filtered])
slots=('4:1','7:1','7:4')
rest=set().union(*(native(v) for k,v in w.items() if k not in slots))
pools=[[(native(x)-rest) for x in candidates(int(k.split(':')[0]))[int(k.split(':')[1])]] for k in slots]
best=158; pair_pruned=0; evaluated=0
for a in pools[0]:
    for b in pools[1]:
        if len(a|b)>=158-len(rest):
            pair_pruned+=1
            continue
        for c in pools[2]:
            evaluated+=1
            best=min(best,len(rest|a|b|c))
assert best==158
print('SET_PAIR_UNFILTERED','cartesian',len(pools[0])*len(pools[1])*len(pools[2]),'pair_pruned',pair_pruned,'third_evaluated',evaluated,'minimum',best)
