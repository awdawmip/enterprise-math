#!/usr/bin/env python3
"""R754 finite checker: signed X6 triads and three serial V29 PASS events."""
from itertools import combinations, product, permutations
from collections import Counter
import json

N=6
ports=[(i,s) for i in range(N) for s in (-1,1)]

def canonical_cycle(seq):
    return min(tuple(seq[k:]+seq[:k]) for k in range(3))

def edges(cyc):
    a,b,c=cyc
    return ((a,b),(b,c),(c,a))

def delta(edge):
    a,b=edge
    return {a:1,b:-1}

def add(*maps):
    d=Counter()
    for m in maps: d.update(m)
    return tuple(sorted((p,n) for p,n in d.items() if n))

def schedules(E):
    return list(permutations(E))

def permute_port(p,g):
    return (g[p[0]],p[1])

def permute_cycle(c,g):
    return canonical_cycle([permute_port(p,g) for p in c])

def cyclic_orders(E):
    return {tuple(E[k:]+E[:k]) for k in range(3)}

X=set()
for axes in combinations(range(N),3):
    for sig in product((-1,1),repeat=3):
        p=tuple(zip(axes,sig))
        for reverse in (False,True):
            w=list(p)
            if reverse:w[1],w[2]=w[2],w[1]
            X.add(canonical_cycle(w))
assert len(X)==320
states=sorted(X)
trace_count=0
min_support_count=0
schedule_classes=Counter()
for x in states:
    E=edges(x)
    assert len(set(E))==3
    Ts={}
    for sch in schedules(E):
        u1=add(delta(sch[0]))
        u2=add(delta(sch[0]),delta(sch[1]))
        u3=add(delta(sch[0]),delta(sch[1]),delta(sch[2]))
        assert len(u1)==2 and len(u2)==2 and u3==()
        assert u1!=u2
        assert (u1,u2) not in Ts
        Ts[(u1,u2)]=sch
        trace_count+=1
        schedule_classes['forward' if sch in cyclic_orders(E) else 'reverse']+=1
    assert len(Ts)==6
    if len({s for _,s in x})==1: min_support_count+=1
assert trace_count==1920
assert min_support_count==80
assert schedule_classes=={'forward':960,'reverse':960}

# Covariance checks: all 320 triads and all 720 axis permutations.
covariance=0
for g in permutations(range(N)):
    for x in states:
        y=permute_cycle(x,g)
        assert y in X
        Ex=edges(x)
        Ey=edges(y)
        assert {tuple(map(lambda p:permute_port(p,g),edge)) for edge in Ex}==set(Ey)
        P={tuple((permute_port(a,g),permute_port(b,g)) for a,b in sch) for sch in cyclic_orders(Ex)}
        assert P==cyclic_orders(Ey)
        covariance+=1
assert covariance==230400

# A uniform-sign cycle is fixed by cyclic axis permutation, which fixes no ordering.
x=canonical_cycle([(0,1),(1,1),(2,1)])
G=(1,2,0,3,4,5)
assert permute_cycle(x,G)==x
E=edges(x)
for sch in schedules(E):
    moved=tuple((permute_port(a,G),permute_port(b,G)) for a,b in sch)
    assert moved != sch

# Conditional S3 counterexample; no native frame assignment is asserted.
def compose(p,q):
    return tuple(p[q[i]] for i in range(3))
id3=(0,1,2)
a=(1,0,2);b=(0,2,1)
assert compose(a,b)!=compose(b,a)

res={
'schema':'R754_X6_TRIADIC_SERIALIZATION_EXACT_V1',
'status':'PASS',
'candidate_model_only':True,
'axes':6,'signed_ports':12,'triadic_cyclic_states':len(states),
'serial_paths':trace_count,
'schedules_per_state':6,
'forward_serial_paths':schedule_classes['forward'],
'reverse_serial_paths':schedule_classes['reverse'],
'uniform_sign_stabilizer_states':min_support_count,
'covariance_state_permutation_checks':covariance,
'prefix_u_minimum_nonzero_entries':2,
'prefix_u_maximum_nonzero_entries':2,
'full_cycle_final_u_zero':True,
'frame_conditional_noncommuting_pair':True,
'v39_frame_assignment_native_authorized':False,
'notes':'Count-only V29 PASS algebra; not TRIADIC_CLOSURE_E and not V39 based-loop packet.'}
print(json.dumps(res,sort_keys=True,indent=2))
