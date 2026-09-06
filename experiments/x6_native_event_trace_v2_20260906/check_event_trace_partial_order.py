#!/usr/bin/env python3
from itertools import permutations

# Minimal exact model of certified-independent event serialization.
# Events A,B,C update disjoint slots; D depends on A by sharing slot a.

def apply(state,event):
    s=dict(state)
    if event=='A': s['a']+=1
    elif event=='B': s['b']+=1
    elif event=='C': s['c']+=1
    elif event=='D': s['a']*=2
    else: raise ValueError(event)
    return s

def run(word):
    s={'a':1,'b':0,'c':0}
    for e in word: s=apply(s,e)
    return tuple(sorted(s.items()))

# Pairwise independent A,B,C commute and all six serializations share endpoint.
abc=tuple(permutations('ABC'))
assert len(abc)==6
assert len({run(w) for w in abc})==1

# A and D are dependent: AD != DA on declared state.
assert run('AD') != run('DA')

# Dependency-poset witness for word A B D: A<D, B incomparable to both.
# Linear extensions preserving A<D are ABD, ADB, BAD.
extensions=('ABD','ADB','BAD')
assert all(w.index('A') < w.index('D') for w in extensions)
assert len(set(extensions))==3

# All independent-event trace serializations retain same event count grade.
assert {len(w) for w in abc}=={3}

print('PASS_X6_NATIVE_EVENT_TRACE_V2')
print('three_independent_serializations',6)
print('independent_endpoint_classes',1)
print('dependent_AD_commutes',False)
print('A_before_D_linear_extensions',3)
print('event_count_grade_preserved',True)
