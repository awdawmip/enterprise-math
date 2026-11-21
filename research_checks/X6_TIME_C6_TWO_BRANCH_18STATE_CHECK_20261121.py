#!/usr/bin/env python3
"""Exact finite certificate for the frozen X6 C6 adjacent-shell two-branch native microtraces.
No physical branch-selection law or precision-fiber update is assumed.
"""
from collections import Counter
from itertools import product
from math import comb, ceil, log2
import json

def add(u,v): return tuple(x+y for x,y in zip(u,v))
def neg(u): return tuple(-x for x in u)
e=[tuple(int(i==j) for i in range(6)) for j in range(6)]
a=e[:3]+[neg(v) for v in e[:3]]
z=(0,)*6
outer=[add(a[r],a[(r+1)%6]) for r in range(6)]
assert len(set(a+outer+[z]))==13
assert all(sum(abs(u-v) for u,v in zip(a[r],g))==1 and sum(abs(u-v) for u,v in zip(g,a[(r+1)%6]))==1 for r in range(6) for g in (z,outer[r]))
states=[('S',r) for r in range(6)]+[('I',r) for r in range(6)]+[('O',r) for r in range(6)]
def output(s): return {'S':a[s[1]],'I':z,'O':outer[s[1]]}[s[0]]
def successors(s):
    typ,r=s
    return [('I',r),('O',r)] if typ=='S' else [('S',(r+1)%6)]
# Distinction by current Cell or by the set of next possible Cells.
for i,s in enumerate(states):
    for t in states[i+1:]:
        assert output(s)!=output(t) or {output(v) for v in successors(s)}!={output(v) for v in successors(t)}
assert len(states)==18
# Four individual concrete time-indexed path populations.
certificate={}
for W in (1,2):
    M=6*W
    seen=set(); bins=Counter(); full=0
    for bits in product((0,1),repeat=M):
        micro=[a[0]]
        for k,b in enumerate(bits):
            r=k%6
            micro.extend((z if b else outer[r],a[(r+1)%6]))
        assert len(micro)==12*W+1 and micro[0]==micro[-1]
        assert all(sum(abs(x-y) for x,y in zip(u,v))==1 for u,v in zip(micro,micro[1:]))
        seen.add(tuple(micro))
        bins[sum(bits)]+=1
        full+=1
    assert full==len(seen)==2**M
    assert all(bins[k]==comb(M,k) for k in range(M+1))
    certificate[str(W)]={"macro_edges":M,"native_microsteps":12*W,"branch_histories":len(seen),"pivot_visit_distribution":[bins[k] for k in range(M+1)],"minimum_bits_ordered_branch_provenance":M,"distinct_pivot_count_values":M+1,"minimum_bits_pivot_count":ceil(log2(M+1)),"all_outer_valid_C12_words":bins[0]}
# An inner intermediate state at the common pivot retains distinct next scheduled shell.
assert len({output(successors(('I',r))[0]) for r in range(6)})==6
result={"schema":"X6_TIME_C6_TWO_BRANCH_MICROTIME_CERT_V1","status":"EXACT_FINITE_EXECUTED","scientific_scope":"frozen selected X6 C6 shell cycle, both shortest native branches per macroedge; no claimed physical branch-choice law","native_spatial_axes":6,"shell_cells":6,"different_outer_gate_cells":6,"distinct_physical_cells_total":13,"distinct_minimal_Cell_future_Markov_states":18,"minimum_fixed_length_state_bits":5,"inner_pivot_states_sharing_same_current_Cell":6,"observer_horizon":"current and next native Cell, all permitted future branch choices; history observer separately","populations":certificate,"mismatches":0}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
