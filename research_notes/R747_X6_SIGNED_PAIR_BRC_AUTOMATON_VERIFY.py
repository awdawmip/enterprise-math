#!/usr/bin/env python3
"""R747 exact signed-Port pair automaton checker (finite integer/set arithmetic)."""
from itertools import combinations, permutations
from collections import Counter
import json

ports=tuple((i,s) for i in range(6) for s in (-1,1))
V=tuple(frozenset((p,q)) for p,q in combinations(ports,2) if p[0]!=q[0])
assert len(V)==60
index={v:i for i,v in enumerate(V)}
def adjacent(v,w):
    return len(v&w)==1 and len({p[0] for p in v|w})==3
edges={(v,w) for v in V for w in V if adjacent(v,w)}
assert len(edges)==960
assert all(sum((v,w) in edges for w in V)==16 for v in V)
assert all(sum((v,w) in edges for v in V)==16 for w in V)
def successor(v,w):
    assert (v,w) in edges
    u=v^w
    assert len(u)==2 and (w,u) in edges and (u,v) in edges
    return u
genuine=set(); spurious=set()
for v,w in edges:
    for u in V:
        if (w,u) not in edges or (u,v) not in edges: continue
        cyc=(v,w,u)
        key=min((cyc,cyc[1:]+cyc[:1],cyc[2:]+cyc[:2]),key=lambda t:tuple(index[x] for x in t))
        (genuine if u==successor(v,w) else spurious).add(key)
assert (len(genuine),len(spurious))==(320,1920)
assert not genuine&spurious
assert all(len(set.intersection(*(set(z) for z in cyc)))==0 and len(set.union(*(set(z) for z in cyc)))==3 for cyc in genuine)
assert all(len(set.intersection(*(set(z) for z in cyc)))==1 and len(set.union(*(set(z) for z in cyc)))==4 for cyc in spurious)
root={v:Counter() for v in V}
for family,name in ((genuine,'genuine'),(spurious,'star')):
    for cyc in family:
        for v in cyc:root[v][name]+=1
assert all(c=={'genuine':16,'star':96} for c in root.values())
assert all(successor(w,successor(v,w))==v for v,w in edges)
checks=0
for permutation in permutations(range(6)):
    act=lambda v:frozenset((permutation[i],s) for i,s in v)
    for v,w in edges:
        av,aw=act(v),act(w)
        assert (av,aw) in edges and successor(av,aw)==act(successor(v,w))
        checks+=1
assert checks==691200
ex=(frozenset(((0,1),(1,1))),frozenset(((0,1),(2,1))),frozenset(((0,1),(3,1))))
assert all((ex[i],ex[(i+1)%3]) in edges for i in range(3))
assert ex[2]!=successor(*ex[:2])
result={
"schema":"EM_R747_SIGNED_PORT_PAIR_BRC_AUTOMATON_EXACT_V1",
"status":"PASS","axes":6,"signed_ports":12,"visible_signed_pairs":60,
"oriented_triads":320,"incidence_lifts":960,"outdegree":16,"indegree":16,
"rooted_three_step_closed_walks":6720,
"genuine_rooted_three_step_closed_walks":960,
"spurious_rooted_three_step_closed_walks":5760,
"directed_cycle_classes_total":2240,
"genuine_directed_cycle_classes":320,
"spurious_star_directed_cycle_classes":1920,
"rooted_loops_per_visible_pair":{"all":112,"genuine":16,"star":96},
"first_order_hidden_state_repair_bits":4,
"second_order_edge_states":960,"deterministic_second_order_period":3,
"axis_permutations":720,"covariance_checks":checks,
"uniform_resampled_branch_three_return_fraction":"7/256",
"frozen_input_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
"task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
"status_scope":"exact finite C1 candidate Port dynamics; native V29/V39 update not tested"}
print(json.dumps(result,indent=2,ensure_ascii=False))
