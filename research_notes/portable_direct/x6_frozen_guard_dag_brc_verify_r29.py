#!/usr/bin/env python3
"""Exact bounded Boolean-BRC check for R29 frozen-guard DAG theorem.
No external dependencies. Event labels retain source identity and signed Port.
"""
import json
from itertools import product


def closure_data(n, g, parents, returns, guards):
    closures = []
    for a in range(g):
        clos = 1 << a
        for b in range(a):
            if parents[a] & (1 << b):
                clos |= closures[b]
        closures.append(clos)
    rows = []
    for a, cm in enumerate(closures):
        req = rel = 0
        for b in range(g):
            if cm & (1 << b):
                req |= returns[b]
                rel |= guards[b]
        rows.append((2*req.bit_count()+cm.bit_count(), rel, cm, req))
    return rows


def exact_languages(n, g, parents, returns, guards, hidden):
    # State: plus-phase mask, completed-return mask, one-use gate mask.
    initial = (0, 0, 0)
    frontier = {(): initial}
    words = {()}
    layers = [frozenset(words)]
    for _ in range(2*n+g):
        new = {}
        for word, (plus, done, gates) in frontier.items():
            for i in range(n):
                bit=1<<i
                if not (plus & bit):
                    new[word + (f'B{i}+',)] = (plus|bit, done, gates)
                elif not (done & bit):
                    new[word + (f'B{i}-',)] = (plus, done|bit, gates)
            for a in range(g):
                bit=1<<a
                if gates & bit: continue
                if (gates & parents[a]) != parents[a]: continue
                if (done & returns[a]) != returns[a]: continue
                if (hidden & guards[a]) != guards[a]: continue
                new[word+(f'A{a}+',)] = (plus,done,gates|bit)
        frontier = new
        words.update(new)
        layers.append(frozenset(words))
    return layers


def verify(n,g,parents,returns,guards):
    rows=closure_data(n,g,parents,returns,guards)
    L=[exact_languages(n,g,parents,returns,guards,s) for s in range(1<<n)]
    comparisons=0
    for h in range(2*n+g+1):
        def sig(s):
            return tuple(a for a,(d,req,*_) in enumerate(rows) if d<=h and (s&req)==req)
        for s in range(1<<n):
            for t in range(s+1,1<<n):
                assert (L[s][h]==L[t][h]) == (sig(s)==sig(t)), (n,g,parents,returns,guards,h,s,t)
                comparisons+=1
        for s in range(1<<n):
            for a,(d,req,_,_) in enumerate(rows):
                present=any(f'A{a}+' in w for w in L[s][d] if len(w)<=d)
                assert present == ((s&req)==req), (n,g,parents,returns,guards,s,a)
                if d>0:
                    earlier=any(f'A{a}+' in w for w in L[s][d-1])
                    assert not earlier
    return comparisons


# Exhaust all DAGs on 2 ordered gate vertices, and all source masks for
# returns and frozen guards at both gate vertices. Every hidden state tested.
total=0
comparisons=0
for p1 in range(2):
    parents=(0,p1)
    for r0,r1,h0,h1 in product(range(4),repeat=4):
        comparisons += verify(2,2,parents,(r0,r1),(h0,h1))
        total+=1

# Branch-and-join case with three sources, two guarded parents and a join.
# Both guards at depth 5, join at depth 9 (shared source B1 prepared once).
branch=closure_data(3,3,(0,0,3),(3,6,0),(3,6,0))
assert [row[0] for row in branch] == [5,5,9]
branch_comparisons=verify(3,3,(0,0,3),(3,6,0),(3,6,0))

# Reset counterexample: B0+/B0-; A0+ requires theta0=1 and resets
# theta0=0, A1+ requires A0+ and the CURRENT theta0=1, hence impossible.
# The hypothetical frozen-guard model admits A1+ at depth 4.
reset_static=closure_data(1,2,(0,1),(1,0),(1,1))
assert reset_static[1][0]==4 and reset_static[1][1]==1
def reset_successor_states(state):
    plus, returned, gates, current_bit = state
    nxt=[]
    if plus==0:
        nxt.append((1, returned, gates, current_bit, 'B0+'))
    if plus and not returned:
        nxt.append((plus, 1, gates, current_bit, 'B0-'))
    if returned and not (gates&1) and current_bit:
        nxt.append((plus, returned, gates|1, 0, 'A0+'))  # irrevocable reset
    if (gates&1) and not (gates&2) and current_bit:
        nxt.append((plus, returned, gates|2, current_bit, 'A1+'))
    return nxt

seen={(0,0,0,1)}
todo=list(seen)
actual_reset_a1_reachable=False
while todo:
    state=todo.pop()
    for *st,label in reset_successor_states(state):
        if label=='A1+': actual_reset_a1_reachable=True
        st=tuple(st)
        if st not in seen:
            seen.add(st)
            todo.append(st)
assert not actual_reset_a1_reachable

res={
    'schema':'EM_X6_R29_EXACT_BOOLEAN_BRC_CHECK_V1',
    'domain':{'sources':2,'one_use_gate_events':2,
              'parents':'all ordered acyclic edges (0->1 optional)',
              'return_masks':'all 4 masks per gate','guard_masks':'all 4 masks per gate',
              'hidden_histories':'all 4 initial bit assignments',
              'word_horizons':'all 0..6 inclusive',
              'observations':'successful fully source/signed-Port labelled words'},
    'controllers_checked':total,'language_equivalence_pair_checks':comparisons,
    'branch_join':{'sources':3,'gates':3,'earliest_gate_depths':[r[0] for r in branch],
                   'language_equivalence_pair_checks':branch_comparisons},
    'reset_boundary':{'frozen_predicted_A1_first_depth':4,
                      'mutable_guard_actual_A1_reachable':actual_reset_a1_reachable},
    'arithmetic':'exact integer and finite language set equality',
    'result':'PASS'
}
print(json.dumps(res,ensure_ascii=False,indent=2))
