#!/usr/bin/env python3
"""R678 finite certificate: V23-V27-V29 two-loop bias and potential dynamics.
All computations are exact finite combinatorics (integers and native X6 cell labels).
No numerical heartbeat propagation, pi, trigonometry or classical matrix propagator.
"""
import json
from collections import Counter
from itertools import combinations, product

AXES = tuple(range(6))
TRIADS = tuple(combinations(AXES, 3))
MATCHINGS = (
    ((0, 1), (2, 3), (4, 5)),
    ((0, 2), (1, 4), (3, 5)),
    ((0, 3), (1, 5), (2, 4)),
    ((0, 4), (1, 3), (2, 5)),
)

def field_eval(matching, triad):
    s = set(triad)
    bits = []
    for a, b in matching:
        if int(a in s) + int(b in s) != 1:
            return 0
        bits.append(int(b in s))
    return 1 if sum(bits) % 2 == 0 else -1

CODE = {s: tuple(field_eval(m, s) for m in MATCHINGS) for s in TRIADS}
NEIGH = {s: tuple(t for t in TRIADS if len(set(s) & set(t)) == 2) for s in TRIADS}
assert len(set(CODE.values())) == 20
assert all(len(v) == 9 for v in NEIGH.values())
assert CODE[(0, 1, 2)] == (0, 0, 1, 1)

def score(u, t):
    return sum(x*y for x, y in zip(u, CODE[t]))

def winner(u, s):
    m = max(score(u,t) for t in NEIGH[s])
    return tuple(t for t in NEIGH[s] if score(u,t) == m)

BRIDGES = ((0,2,1,3), (0,3,1,2), (1,2,0,3), (1,3,0,2))
assert all(set((b[0],b[2])) == {0,1} for b in BRIDGES)

# V29 two-loop ordered prefix: two loops start at shared o on port 0/2
# and return to o on that port. Each outstanding loop causes -e_port.
for a,b in product(range(6), repeat=2):
    for bridge in BRIDGES:
        u=[0]*4
        u[bridge[0]]-=a
        u[bridge[2]]-=b
        ws=winner(u,(0,1,2))
        if a==b==0:
            assert len(ws)==9
        else:
            assert len(ws)>=2

# All possible two-field supports: each corresponding witness S has three
# different projection values repeated exactly three times among 9 neighbors.
PAIR_WITNESS = {
 (0,1):(0,3,4), (0,2):(0,2,5), (0,3):(0,3,5),
 (1,2):(0,4,5), (1,3):(0,1,5), (2,3):(0,1,2),
}
pair_certificate={}
for pair,s in PAIR_WITNESS.items():
    sigs=Counter(tuple(CODE[t][i] for i in pair) for t in NEIGH[s])
    assert len(sigs)==3 and set(sigs.values())=={3}
    pair_certificate[f'{pair[0]}{pair[1]}']={
       'active_triad': ''.join(map(str,s)),
       'neighbor_projection_counts': {str(k):v for k,v in sorted(sigs.items())},
    }

# Exhaust all four-component integer biases of L1 norm 0 through 7.
search_counts={}
minimizers=[]
for k in range(8):
    tried=0;valid=0
    for v in product(range(-k,k+1),repeat=4):
        if sum(abs(x) for x in v)!=k:continue
        tried+=1
        if all(len(winner(v,s))==1 for s in TRIADS):
            valid+=1
            if k==7:minimizers.append(v)
    search_counts[str(k)]={'tested':tried,'universal_strict':valid}
assert all(search_counts[str(k)]['universal_strict']==0 for k in range(7))
assert len(minimizers)==48
witness=(-3,-2,-1,1)
assert witness in minimizers

# Unique best-neighbor selector for Omega=0, frozen u.
F={s:winner(witness,s)[0] for s in TRIADS}
GAPS=[]
for s in TRIADS:
    z=sorted((score(witness,t) for t in NEIGH[s]),reverse=True)
    assert z[0]>z[1]
    GAPS.append(z[0]-z[1])
visited=set();cycles=[]
for s in TRIADS:
    if s in visited:continue
    path=[];idx={};x=s
    while x not in idx and x not in visited:
        idx[x]=len(path);path.append(x);x=F[x]
    if x in idx:cycles.append(path[idx[x]:])
    visited.update(path)
assert cycles and all(len(c)==2 for c in cycles)

def slot_transport(slotmap,s,t):
    common=set(s)&set(t)
    leave=next(iter(set(s)-common))
    enter=next(iter(set(t)-common))
    out={i:slotmap[i] for i in common}
    out[enter]=slotmap[leave]
    return out

def holonomy(cycle):
    s=cycle[0];q={a:i for i,a in enumerate(s)}
    for i,x in enumerate(cycle):
        q=slot_transport(q,x,cycle[(i+1)%len(cycle)])
    return tuple(q[a] for a in s)
assert all(holonomy(c)==(0,1,2) for c in cycles)

result={
 'schema':'R678_V23_V27_V29_TRANSFER_ONLY_EXACT_V1',
 'status':'AUTHOR_SIDE_FINITE_CHECK',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'source_code':'V23 fields M0 M4 M8 M10 / V27 9-adjacent-neighbor rule',
 'two_loop_shared_cell':{
    'ports_A_B':[0,2],
    'bridge_count':len(BRIDGES),
    'prefix_exhaustion':'0<=outstanding A,B<=5 for each bridge',
    'prefix_012_unique_winners':0,
    'completed_block_u':'(0,0,0,0)',
    'completed_block_omega':'zero',
    'completed_block_maximizers':9,
 },
 'pair_projection_certificate':pair_certificate,
 'fixed_bias_zero_omega':{
    'L1_norm_search':search_counts,
    'minimal_universal_strict_L1_norm':7,
    'number_of_minimizers_at_norm_7':len(minimizers),
    'witness_u':witness,
    'witness_minimum_score_gap':min(GAPS),
    'witness_recurrent_cycles':[' -> '.join(''.join(map(str,t)) for t in c) for c in cycles],
    'witness_recurrent_holonomies':[list(holonomy(c)) for c in cycles],
 }
}
print(json.dumps(result,ensure_ascii=False,indent=2))
print('R678_TWO_LOOP_BIAS_OBSTRUCTION_AND_GRADIENT_HOLONOMY_PASS')
