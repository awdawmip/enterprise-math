#!/usr/bin/env python3
"""R762FZ six-axis finite exact covariance and orbit certificate.
Only named BRC candidate branch permutations are tested; no signed native event grant.
"""
from itertools import permutations, combinations
from collections import Counter
import json

AXES=tuple(range(6))
BASE_STARS=((0,1,2),(0,3,4),(1,3,5),(2,4,5))
ALL_TRIPLES=tuple(combinations(AXES,3))
PERMS=tuple(permutations(AXES))

def triple(t): return tuple(sorted(t))
def frame(ts): return tuple(sorted(triple(t) for t in ts))
def act(p,t): return triple(p[i] for i in t)
def act_frame(p,f): return frame(act(p,t) for t in f)
def sign_cycles(t):
    a,b,c=t
    return ((a,b,c),(a,c,b))
def rot(a):
    i=a.index(min(a))
    return tuple(a[i:]+a[:i])
def act_cycle(p,c): return rot(tuple(p[i] for i in c))

F=tuple(sorted({act_frame(p,BASE_STARS) for p in PERMS}))
assert len(F)==30
M=tuple((f,miss) for f in F for miss in f)
assert len(M)==120
S=set(ALL_TRIPLES)
assert set(t for f in F for t in f)==S
full_freq=Counter(t for f in F for t in f)
mark_freq=Counter(t for f,miss in M for t in f if t!=miss)
assert set(full_freq)==S and set(full_freq.values())=={6}
assert set(mark_freq)==S and set(mark_freq.values())=={18}

F0=frame(BASE_STARS)
F0_stab=[p for p in PERMS if act_frame(p,F0)==F0]
assert len(F0_stab)==24
m0=F0[0]
M0_stab=[p for p in F0_stab if act(p,m0)==m0]
assert len(M0_stab)==6

base_branches=set(c for t in F0 for c in sign_cycles(t))
assert len(base_branches)==8
assert {act_cycle(p,c) for p in F0_stab for c in base_branches}==base_branches
assert len({act_cycle(p,next(iter(base_branches))) for p in F0_stab})==8
marked_branches=set(c for t in F0 if t!=m0 for c in sign_cycles(t))
assert len(marked_branches)==6
assert {act_cycle(p,c) for p in M0_stab for c in marked_branches}==marked_branches
assert len({act_cycle(p,next(iter(marked_branches))) for p in M0_stab})==6

frame_covariance=0
marked_covariance=0
for p in PERMS:
    for f in F:
        got={act_cycle(p,c) for t in f for c in sign_cycles(t)}
        target={c for t in act_frame(p,f) for c in sign_cycles(t)}
        assert got==target
        frame_covariance+=1
    for f,miss in M:
        got={act_cycle(p,c) for t in f if t!=miss for c in sign_cycles(t)}
        pf=act_frame(p,f); pmiss=act(p,miss)
        target={c for t in pf if t!=pmiss for c in sign_cycles(t)}
        assert got==target
        marked_covariance+=1

ori_counts_F=Counter(c for f in F for t in f for c in sign_cycles(t))
ori_counts_M=Counter(c for f,miss in M for t in f if t!=miss for c in sign_cycles(t))
assert len(ori_counts_F)==len(ori_counts_M)==40
assert set(ori_counts_F.values())=={6}
assert set(ori_counts_M.values())=={18}
assert 30*8==40*6 and 120*6==40*18

output={
 'schema':'R762FZ_EXACT_ENUMERATION_V1','status':'PASS',
 'axes':6,'permutations':len(PERMS),'unoriented_triples':len(ALL_TRIPLES),
 'oriented_triads':len(ori_counts_F),
 'frames':len(F),'frame_stabilizer_order':len(F0_stab),
 'marked_frames':len(M),'marked_frame_stabilizer_order':len(M0_stab),
 'star_triple_occurrences_per_frame_orbit':6,
 'three_star_occurrences_per_marked_frame_orbit':18,
 'full_frame_oriented_branch_occurrences':6,
 'marked_frame_oriented_branch_occurrences':18,
 'full_frame_covariance_cases':frame_covariance,
 'marked_frame_covariance_cases':marked_covariance,
 'unmarked_branch_S4_orbit_size':8,
 'marked_branch_S3_orbit_size':6,
 'conditional_average_per_oriented_triads':'1/40',
 'method':'Exhaustive 720 S6 relabelings of 6 native axis labels; all 30 frames and 120 marked frames; exact cycles and counts',
 'scope':'Finite combinatorial BRC carrier and symmetry only; signed TRIADIC_CLOSURE_E permission not asserted',
 'review':'NOT_REVIEWED'
}
print(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True))
