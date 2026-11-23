#!/usr/bin/env python3
"""R762KC: exact parity-surjectivity certificate and 42-event construction."""
from itertools import combinations, permutations
import json

AXES=tuple(range(6))
PORTS=tuple(p for p in combinations(AXES,2) if p!=(0,1))
COLORS=tuple(combinations(AXES,3))
FORCED=tuple((0,1,i) for i in range(2,6))
FLEX=tuple(c for c in COLORS if c not in FORCED)
INDEX={p:i for i,p in enumerate(PORTS)}
EVEN={x for x in range(1<<14) if x.bit_count()%2==0}

def edges(color):
    p=tuple(v for v in combinations(color,2) if v in INDEX)
    return tuple(combinations(p,2))

def boundary(edge):
    return (1<<INDEX[edge[0]]) ^ (1<<INDEX[edge[1]])

def connected(edge_list):
    adj={p:set() for p in PORTS}
    for a,b in edge_list:
        adj[a].add(b);adj[b].add(a)
    seen={PORTS[0]}; stack=[PORTS[0]]
    while stack:
        v=stack.pop()
        for w in adj[v]-seen:
            seen.add(w);stack.append(w)
    return len(seen)==len(PORTS)

def layers_for_pair(pair):
    remaining=tuple(c for c in FLEX if c not in pair)
    layers=[{0}]
    for c in remaining:
        choices=tuple(boundary(e) for e in edges(c))
        layers.append({x^b for x in layers[-1] for b in choices})
    assert layers[-1] == EVEN, (pair,len(layers[-1]))
    # Every nonzero-boundary triangle is a spanning two-edge path.
    all_triangle_edges=[e for c in remaining for e in edges(c)]
    assert connected(all_triangle_edges), pair
    return remaining,layers

def witness_choices(pair,remaining,layers):
    singles={c:edges(c)[0] for c in pair}
    target=0
    for c in FORCED:target^=boundary(edges(c)[0])
    for e in singles.values():target^=boundary(e)
    chosen={}
    cur=target
    for i in range(len(remaining)-1,-1,-1):
        c=remaining[i]
        e=next(e for e in edges(c) if (cur^boundary(e)) in layers[i])
        chosen[c]=e
        cur^=boundary(e)
    assert cur==0
    return singles,chosen

def witness(pair,f,triple,singles,chosen):
    assert f in FORCED and len(triple)==6 and set(triple)<=set(FLEX)-set(pair)
    events=[]
    for c in COLORS:
        options=edges(c)
        if c in FORCED:
            actual=(options[0],)*(3 if c==f else 1)
        elif c in singles:
            actual=(singles[c],)
        else:
            selected=chosen[c]
            different=next(e for e in options if e!=selected)
            if c in triple:
                actual=(selected,different,different)
            else:
                actual=tuple(e for e in options if e!=selected)
        expected=(3 if c==f else 1) if c in FORCED else 1 if c in singles else 3 if c in triple else 2
        assert len(actual)==expected and all(e in options for e in actual)
        events.extend(actual)
    deg={p:0 for p in PORTS}
    for a,b in events:
        deg[a]+=1;deg[b]+=1
    assert len(events)==42 and all(d>0 and d%2==0 for d in deg.values())
    assert connected(events)
    return events

def main():
    from math import comb
    tested=0
    reachable_sizes=[]
    orbit_sizes=[]
    pairset={frozenset(pair) for pair in combinations(FLEX,2)}
    group=[(p0,p1)+tail for p0,p1 in ((0,1),(1,0)) for tail in permutations((2,3,4,5))]
    while pairset:
        pair=min(pairset,key=lambda p:tuple(sorted(p)))
        orbit={frozenset(tuple(sorted(g[x] for x in c)) for c in pair) for g in group}
        assert orbit<=pairset
        orbit_sizes.append(len(orbit));pairset-=orbit
    assert len(orbit_sizes)==8 and sorted(orbit_sizes)==[6,6,6,6,24,24,24,24]
    for pair in combinations(FLEX,2):
        remaining,layers=layers_for_pair(pair)
        reachable_sizes.append(len(layers[-1]))
        singles,chosen=witness_choices(pair,remaining,layers)
        candidates=list(combinations(remaining,6))
        assert len(candidates)==comb(14,6)==3003
        # Extreme selections suffice as a concrete code regression; proof applies to all T.
        for f in FORCED:
            for t in (candidates[0],candidates[-1]):
                witness(pair,f,t,singles,chosen)
                tested+=1
    print(json.dumps({
        'schema':'ENTERPRISE_MATH_R762KC_EVIDENCE_V1',
        'frozen_P000_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'model':'unsigned composite Port-Euler; inactive Port 01',
        'all_singleton_pairs':len(reachable_sizes),
        'stabilizer_orbits':len(orbit_sizes),
        'orbit_sizes':sorted(orbit_sizes),
        'exact_reachable_parity_states_each':min(reachable_sizes),
        'even_parity_states_total':len(EVEN),
        'connected_support_unions':120,
        'witness_regression_cases':tested,
        'all_labeled_target_inventories_by_construction':4*comb(16,2)*comb(14,6),
        'marked_44_to_42_cases':5*4*comb(16,2)*comb(14,6),
        'assertion_failures':0,
        'independent_review':'NOT_REVIEWED'
    },sort_keys=True,ensure_ascii=False))

if __name__=='__main__': main()
