#!/usr/bin/env python3
"""Exact finite checks of gauge-invariant signed-link recovery on native V5 triplets."""
from collections import defaultdict
from itertools import product
import json

S=list(product((-1,1),repeat=3))
A=[a for a in S if a[0]*a[1]*a[2]==-1]
def update(s,a):
    return tuple(a[(j-1)%3]*s[(j-1)%3] for j in range(3))
def link(s,a):
    return tuple(s[i]*a[i]*s[(i+1)%3] for i in range(3))

results={}
for j in range(3):
    readings=defaultdict(set)
    calibrated=defaultdict(lambda:defaultdict(set))
    preserved=defaultdict(set)
    for s,a,b in product(S,A,A):
        y=(s[j],update(s,a)[j],update(update(s,a),b)[j])
        rr=link(s,a)
        delta=a[(j-1)%3]*b[(j-1)%3]
        assert rr[(j-1)%3]==y[0]*y[1]
        assert rr[(j-2)%3]==delta*y[1]*y[2]
        assert rr[j]==-delta*y[0]*y[2]
        readings[y].add(rr)
        calibrated[y][delta].add(rr)
        if a[(j-1)%3]==b[(j-1)%3]:
            preserved[y].add(rr)
    assert len(readings)==8 and all(len(v)==2 for v in readings.values())
    assert all(set(v)=={-1,1} and all(len(x)==1 for x in v.values())
               for v in calibrated.values())
    assert all(len(v)==1 for v in preserved.values())
    longer=defaultdict(set)
    for s,word in product(S,product(A,repeat=5)):
        state=s
        observed=[state[j]]
        for a in word:
            state=update(state,a)
            observed.append(state[j])
        longer[tuple(observed)].add(link(s,word[0]))
    assert len(longer)==64 and all(len(v)==2 for v in longer.values())
    results[f'axis{j}']={
       '3_read_words':8,
       'unmarked_initial_link_states':2,
       'known_relative_edge_bit_link_states':1,
       '6_read_words':64,
       'initial_link_states_per_6_read_word':2,
       '5_step_histories_checked':8*4**5}
print(json.dumps({'model':'named V5 signed source/edge carrier',
                  'statement':'conditional fixed-axis gauge-invariant link recovery',
                  'results':results,'status':'PASS'},indent=2))
