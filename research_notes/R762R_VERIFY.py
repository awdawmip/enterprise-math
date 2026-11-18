#!/usr/bin/env python3
"""R762R finite exact checker: signed native three-port star-event candidate."""
from itertools import combinations, permutations, product
from collections import defaultdict
import json

N = 6
AXES = tuple(range(N))
ZERO = (0,)*N

def signed_triads():
    for axes in combinations(AXES,3):
        for signs in product((-1,1),repeat=3):
            yield tuple((i,s) for i,s in zip(axes,signs))

def rotate_order(order):
    return order[1:] + order[:1]

def apply_port(c,port,positive=True):
    axis,sign=port
    out=list(c)
    out[axis]+=sign if positive else -sign
    return tuple(out)

def trace(c,order):
    positions=[c]
    x=c
    for port in order:
        x=apply_port(x,port)
        positions.append(x)
        x=apply_port(x,port,False)
        positions.append(x)
    return tuple(positions)

def perm_port(port,pi):
    return (pi[port[0]],port[1])

def perm_cell(c,pi):
    z=[0]*N
    for i,v in enumerate(c):z[pi[i]]=v
    return tuple(z)

def edge_current(positions):
    curr=defaultdict(int)
    for u,v in zip(positions,positions[1:]):
        diff=[i for i in AXES if u[i]!=v[i]]
        assert len(diff)==1
        i=diff[0]; delta=v[i]-u[i]
        assert abs(delta)==1
        base=u if delta==1 else v
        curr[(base,i)]+=delta
    return {k:v for k,v in curr.items() if v}

n_triads=n_orders=n_cycles=0
for triad in signed_triads():
    n_triads+=1
    orders=tuple(permutations(triad))
    assert len(orders)==6 and len(set(orders))==6
    n_orders+=len(orders)
    orbit=set()
    for order in orders:
        tr=trace(ZERO,order)
        assert len(tr)==7 and tr[0]==tr[-1]==ZERO
        assert {tr[i] for i in (1,3,5)}=={apply_port(ZERO,p) for p in triad}
        assert not edge_current(tr)
        p1=rotate_order(order)
        p2=rotate_order(p1)
        assert rotate_order(p2)==order and len({order,p1,p2})==3
        orbit.add(frozenset((order,p1,p2)))
    assert len(orbit)==2
    n_cycles+=len(orbit)
    first={o[0] for o in orders}
    two={(o[0],rotate_order(o)[0]) for o in orders}
    assert len(first)==3 and len(two)==6
    assert all(sum(o[0]==p for o in orders)==2 for p in triad)
    for pi in permutations(AXES):
        reordered=tuple(sorted((perm_port(p,pi) for p in triad)))
        assert len(reordered)==3
        for order in orders:
            image=tuple(perm_port(p,pi) for p in order)
            assert rotate_order(image)==tuple(perm_port(p,pi) for p in rotate_order(order))
            assert trace(ZERO,image)==tuple(perm_cell(c,pi) for c in trace(ZERO,order))
assert n_triads==160 and n_orders==960 and n_cycles==320
result={"schema":"EM_R762R_AUTHOR_SIDE_EXACT_ENUM_V1", "scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389","signed_triads":n_triads,"ordered_lifts":n_orders,"three_event_cycles":n_cycles,"orders_per_triad":6,"cyclic_classes_per_triad":2,"microsteps_per_event":6,"source_first_observation_single_fiber":2,"source_first_observation_two_round_fiber":1,"S6_permutations_tested_per_triad":720,"S6_trace_equivariance_checks":n_orders*720,"verified":True,"scope":"typed candidate star-excursion witness, not admitted physical TRIADIC_CLOSURE_E or V29/V39 native ledger"}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
