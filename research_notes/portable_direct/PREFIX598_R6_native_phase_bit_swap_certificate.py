#!/usr/bin/env python3
"""PREFIX-598-R6 exact native phase-bit swap and action-label provenance.

Imports unchanged original PREFIX-565 BRC edge and retains full seven rewards,
exact next original port, primitive action labels where indicated; stdlib only.
"""
from collections import Counter
import json
from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN, PHASES, NEXT, ACTIONS, ROOTS, TARGET, edge
)
assert SCIENCE_PIN == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(PHASES)==48 and len(NEXT)==48 and len(ACTIONS)==6 and len(ROOTS)==9
assert TARGET == 4
PREDECESSORS = (3,14,15)
PAIRS = ((3,14),(3,15),(14,15))
assert {i for i,ns in enumerate(NEXT) if TARGET in ns} == set(PREDECESSORS)
assert PHASES[3] == (0,-6,1)
assert PHASES[14] == (1,-4,1)
assert PHASES[15] == (1,-5,1)
assert NEXT[3] == (4,16,20)
assert NEXT[14] == (20,4,8)
assert NEXT[15] == (16,4,8)
assert tuple(NEXT[p].index(TARGET) for p in PREDECESSORS) == (0,1,1)
assert all(PHASES[p][2] == 1 for p in PREDECESSORS)
def swap_ports(p,q):
    return ((2*p,2*q+1),(2*p+1,2*q))
def count(root,starts,with_action):
    if with_action:
        return Counter((a,*edge(port,a,root)) for port in starts for a in ACTIONS)
    return Counter(edge(port,a,root) for port in starts for a in ACTIONS)

cases=[]
for ir,root in enumerate(ROOTS):
    for p,q in PAIRS:
        left,right=swap_ports(p,q)
        l=count(root,left,False);r=count(root,right,False)
        assert l==r and sum(l.values())==12
        la=count(root,left,True);ra=count(root,right,True)
        diff={key:la[key]-ra[key] for key in la.keys()|ra.keys()
              if la[key]!=ra[key]}
        expected=4 if NEXT[p].index(TARGET)!=NEXT[q].index(TARGET) else 0
        assert len(diff)==expected
        assert all(port==2*TARGET+1 and a[1]==1
                   for (a,port,w) in diff)
        cases.append(dict(root_index=ir,phases=[p,q],
                          reward_next_port_equal=True,
                          action_aware_difference_atoms=len(diff)))
assert len(cases)==27
assert sum(z['action_aware_difference_atoms'] for z in cases)==9*8
out=dict(status='ALL_CHECKS_PASS',science_pin=SCIENCE_PIN,
  native_source='PREFIX565_positive_marginal_certificate.py',
  native_source_git_blob='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41',
  gate_target_phase=TARGET,
  native_predecessor_phases=list(PREDECESSORS),
  distinct_phase_pairs=3,root_count=9,
  raw_reward_and_original_next_port_count_equalities=27,
  action_labeled_count_comparisons=27,
  action_labeled_equalities=9,
  action_labeled_four_atom_witness_cases=18,
  checked_cases=cases)
print('ALL_CHECKS_PASS')
print(json.dumps(out,indent=2,ensure_ascii=False))
