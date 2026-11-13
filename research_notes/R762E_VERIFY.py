#!/usr/bin/env python3
"""R762E: exact finite-capacity three-triad port-state enumeration."""
from collections import Counter, deque
from itertools import product
import json

N=6
ID=tuple(range(N))
SUPPORTS=((0,1,2),(0,3,4),(1,3,5))
def compose(p,q): return tuple(p[q[i]] for i in range(N))
def triad(s):
    a,b,c=s
    p=list(ID);p[a],p[b],p[c]=b,c,a
    return tuple(p)
GENS=tuple(triad(s) for s in SUPPORTS)
def search(cap):
    start=(ID,(0,0,0));queue=deque([start]);dist={start:0}
    min_port={ID:0};layers=Counter({0:1})
    while queue:
        p,c=queue.popleft();d=dist[p,c]
        for i,g in enumerate(GENS):
            if c[i]>=cap: continue
            cc=tuple(c[k]+int(k==i) for k in range(3))
            pp=compose(p,g);node=(pp,cc)
            if node not in dist:
                dist[node]=d+1;layers[d+1]+=1;queue.append(node)
            if pp not in min_port: min_port[pp]=d+1
    return dist,min_port,layers

report={"schema":"R762E_BOUNDED_TRIADIC_CAPACITY_EXACT_V1",
        "parent_task":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
        "scope":"fixed candidate 012/034/135 three-cycle alphabet and uniform per-type budget",
        "supports":[list(s) for s in SUPPORTS],"capacity_cases":{}}
for cap,expected_joint,expected_port in ((1,16,16),(2,245,196),(3,2408,360)):
    states,ports,layers=search(cap)
    assert len(states)==expected_joint,(cap,len(states))
    assert len(ports)==expected_port,(cap,len(ports))
    assert sum(layers.values())==expected_joint
    # Independent exact-depth transition frontier.
    frontier={(ID,(0,0,0))}
    for depth in range(1,3*cap+1):
        next_frontier=set()
        for p,c in frontier:
            for i,g in enumerate(GENS):
                if c[i]<cap:
                    cc=tuple(c[k]+int(k==i) for k in range(3))
                    next_frontier.add((compose(p,g),cc))
        assert len(next_frontier)==layers[depth],(cap,depth)
        assert all(sum(c)==depth for p,c in next_frontier)
        frontier=next_frontier
    # Independent count-vector recursion, with a separate set per vector.
    dp={(0,0,0):{ID}}
    for c in product(range(cap+1),repeat=3):
        if c==(0,0,0):continue
        ps=set()
        for i,g in enumerate(GENS):
            if c[i]>0:
                prior=tuple(c[k]-int(k==i) for k in range(3))
                ps.update(compose(p,g) for p in dp[prior])
        dp[c]=ps
    assert sum(len(ps) for ps in dp.values())==expected_joint
    assert set(p for ps in dp.values() for p in ps)==set(ports)
    assert set((p,c) for c,ps in dp.items() for p in ps)==set(states)
    hist=Counter(ports.values())
    min_bits=(len(states)-1).bit_length()
    report["capacity_cases"][str(cap)]={
      "reachable_port_permutations":len(ports),
      "reachable_joint_states":len(states),
      "distinct_counter_vectors":len(dp),
      "max_shortest_port_events":max(ports.values()),
      "shortest_port_histogram":[hist[i] for i in range(max(hist)+1)],
      "joint_states_by_total_events":[layers[i] for i in range(3*cap+1)],
      "min_fixed_bits_for_port_and_legality_future":min_bits,
      "max_joint_fiber_over_port":max(Counter(p for p,c in states).values())
    }
assert len({p for p,c in search(3)[0]})==360
assert len({p for p,c in search(2)[0]})==196
witness=ID
for i in (0,0,1,0): witness=compose(witness,GENS[i])
assert witness==(0,1,3,4,2,5)
assert witness not in search(2)[1]
report["sharp_minimum_uniform_budget_to_reach_A6"]=3
report["capacity_two_unreachable_witness"]={
  "word_generator_indices":[0,0,1,0],
  "consumption":[3,1,0],
  "port_image":list(witness)
}
report["proof_method"]="complete tuple-permutation BFS, exact-depth propagation, independent count-vector DP; exact integers"
print(json.dumps(report,indent=2,sort_keys=True))
