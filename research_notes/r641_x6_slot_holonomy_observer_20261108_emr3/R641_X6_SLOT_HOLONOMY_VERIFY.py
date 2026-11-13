#!/usr/bin/env python3
"""R641: exact Johnson J(6,3) slot transport, histogram collision, minimal automaton.
Reimplements transport_slots/holonomy of enterprise-math V26/V27 source checker;
all arithmetic is exact integer and finite permutation combinatorics.
"""
import json
from collections import Counter, deque
from itertools import combinations, permutations
from pathlib import Path

BASE=(0,1,2)
TRIADS=tuple(combinations(range(6),3))
NEIGH={s: tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(TRIADS)==20 and all(len(n)==9 for n in NEIGH.values())

def step_slots(s, slots, t):
    assert t in NEIGH[s]
    before={x:slots[k] for k,x in enumerate(s)}
    shared=set(s)&set(t)
    leave=next(iter(set(s)-shared))
    enter=next(iter(set(t)-shared))
    after={x:before[x] for x in shared}
    after[enter]=before[leave]
    return tuple(after[x] for x in t)

# Independent direct dictionary implementation transcribed from the V26/V27 source.
def source_style_step(s, slots, t):
    slotmap = dict(zip(s, slots))
    common = set(s) & set(t)
    leave = next(iter(set(s)-common))
    enter = next(iter(set(t)-common))
    out = {a: slotmap[a] for a in common}
    out[enter] = slotmap[leave]
    return tuple(out[a] for a in t)

def walk(path):
    assert path[0]==BASE
    slots=(0,1,2)
    for s,t in zip(path,path[1:]): slots=step_slots(s,slots,t)
    return path[-1],slots

def hist(path):return Counter(zip(path[:-1],path[1:]))

def parity(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

# 3-step triangles anchored at BASE; nontrivial holonomies are transpositions.
triangles=[]
for b in NEIGH[BASE]:
    for c in NEIGH[b]:
        if BASE in NEIGH[c] and c!=BASE:
            path=(BASE,b,c,BASE)
            triangles.append((path,walk(path)[1]))
assert len(triangles)==36
counts=Counter(p for _,p in triangles)
transpositions=[(1,0,2),(0,2,1),(2,1,0)]
assert all(counts[t]==6 for t in transpositions)
assert counts[(0,1,2)]==18

# Exact pair of order-sensitive loops; their directed-edge histograms agree on swapping loops.
A=(BASE,(0,1,3),(0,2,3),BASE)
B=(BASE,(0,1,3),(1,2,3),BASE)
pa,pb=walk(A)[1],walk(B)[1]
AB=A+B[1:];BA=B+A[1:]
pab=walk(AB)[1];pba=walk(BA)[1]
assert pa==(0,2,1) and pb==(2,1,0)
assert pab==(1,2,0) and pba==(2,0,1)
assert pab!=pba and hist(AB)==hist(BA)
assert parity(pab)==parity(pba)==0

# All 6 permutations are attainable on closed walks of length <=6.
closed_h={p for _,p in triangles}
closed_h.add((0,1,2))
for path,p in triangles:
    for path2,q in triangles:
        closed_h.add(walk(path+path2[1:])[1])
assert closed_h==set(permutations((0,1,2)))

# Native finite deterministic state is (active-triad, current base-slot assignment).
start=(BASE,(0,1,2))
q=deque([start]); seen={start}
while q:
    s,slots=q.popleft()
    for t in NEIGH[s]:
        state=(t,step_slots(s,slots,t))
        if state not in seen:
            seen.add(state);q.append(state)
assert len(seen)==120
assert Counter(s for s,_ in seen)==Counter({s:6 for s in TRIADS})
transitions=sum(len(NEIGH[s]) for s,_ in seen)
assert transitions==1080
source_comparison_checks=0
for s,slots in seen:
    for t in NEIGH[s]:
        assert step_slots(s,slots,t)==source_style_step(s,slots,t)
        source_comparison_checks += 1
assert source_comparison_checks==1080

# Projection to (current triad, sign of slot permutation) is deterministic and has 40 states.
parity_summaries={(s,parity(p)) for s,p in seen}
assert len(parity_summaries)==40
parity_transition={}
for s,slots in seen:
    for t in NEIGH[s]:
        key=(s,parity(slots),t)
        value=parity(step_slots(s,slots,t))
        if key in parity_transition:assert parity_transition[key]==value
        else:parity_transition[key]=value
assert len(parity_transition)==360

# For all 36*35/2 unordered pairs of 3-cycles, compare composing in both orders.
noncommuting=0
for i,(p1,_) in enumerate(triangles):
    for p2,_ in triangles[i+1:]:
        x=walk(p1+p2[1:])[1];y=walk(p2+p1[1:])[1]
        assert hist(p1+p2[1:])==hist(p2+p1[1:])
        if x!=y: noncommuting+=1
assert noncommuting>0

result={
  "schema":"R641_X6_SLOT_HOLONOMY_EXACT_V1",
  "status":"PASS","marker":"R641_X6_ORDERED_HOLONOMY_120_STATE_EXACT_PASS",
  "origin":"2026-11-08",
  "typed_scope":"V26/V27 J(6,3) active-triad slot transport; not PF10 count evolution",
  "vertices":len(TRIADS),"degree":9,"directed_triads_edges":sum(map(len,NEIGH.values())),
  "base":BASE,"three_step_base_loops":len(triangles),
  "three_step_nonidentity_loops":sum(counts[p] for p in transpositions),
  "three_step_transposition_histogram":{str(p):counts[p] for p in transpositions},
  "three_step_identity_loops":counts[(0,1,2)],
  "witness_A":[list(s) for s in A],"witness_B":[list(s) for s in B],
  "holonomy_A":pa,"holonomy_B":pb,"holonomy_AB":pab,"holonomy_BA":pba,
  "same_directed_transition_histogram":hist(AB)==hist(BA),
  "all_closed_holonomies_reachable":len(closed_h),
  "minimal_full_open_state_count":len(seen),
  "reachable_state_outgoing_transitions":transitions,
  "independent_source_style_step_agreements":source_comparison_checks,
  "minimal_base_closed_holonomy_state_count":6,
  "minimal_triad_plus_parity_states":len(parity_summaries),
  "parity_quotient_update_rows":len(parity_transition),
  "unordered_three_step_loop_pairs":len(triangles)*(len(triangles)-1)//2,
  "noncommuting_loop_pairs":noncommuting,
  "proof_status":"Author exact finite construction; distinct mathematical proof supplied; unreviewed",
  "frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
  "source_V26":"enterprise-math@b62110008321d9147212cb89f2627ff613c2550d:experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py",
  "source_V26_file_blob":"5618dae00632f9f796d3f5a6a692c248ea699131"
}
Path(__file__).with_name('R641_EVIDENCE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['marker'],"states",len(seen),"noncommuting_pairs",noncommuting,"triangles",len(triangles),"parity_states",len(parity_summaries))
