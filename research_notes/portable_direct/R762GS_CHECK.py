"""R762GS: exact future-Port observation quotients for the signed K4-STAR
moving-named-Port candidate (not the native TRIADIC_CLOSURE_E rule).
Python 3 standard library; exhaustive finite graph certificates, BRC multiplicity.
"""
import json
from collections import Counter, deque
from itertools import combinations, permutations

V = range(4)
E = tuple(combinations(V, 2))  # 01,02,03,12,13,23
I = tuple(range(6))
S = [tuple(E.index(tuple(sorted((v,u)))) for u in V if u != v) for v in V]

def cycle(star):
    q = list(I)
    a,b,c = star
    q[a],q[b],q[c] = b,c,a
    return tuple(q)

def mul(p,q):
    return tuple(p[q[i]] for i in I)

G = [cycle(star) for star in S]
N = [tuple(g.index(i) for i in I) for g in G]
P = [p for p in permutations(I) if sum(p[a]>p[b] for a in I for b in range(a+1,6))%2 == 0]
idx = {p:i for i,p in enumerate(P)}
assert len(P) == 360
A = tuple((v,s) for v in V for s in (-1,1))
transitions = {
    i: {(v,s):idx[mul(p, G[v] if s == 1 else N[v])]
        for v in E[p[0]] for s in (-1,1)}
    for i,p in enumerate(P)
}
assert all(len(row) == 4 for row in transitions.values())
initial = idx[I]
reachable = {initial}
queue = deque([initial])
while queue:
    i = queue.popleft()
    for j in transitions[i].values():
        if j not in reachable:
            reachable.add(j)
            queue.append(j)
absorbing = {i for i,p in enumerate(P) if p[0] == 5}
transient = reachable - absorbing
assert (len(reachable),len(transient),len(absorbing)) == (350,290,60)
assert all(set(transitions[i].values()) <= absorbing for i in absorbing)

H = []
for b in permutations(V):
    if set((b[0],b[1])) == {0,1}:
        H.append(tuple(E.index(tuple(sorted((b[u],b[v])))) for u,v in E))
assert len(H) == 4
def orbit(i):
    p = P[i]
    out = set()
    for h in H:
        inv = tuple(h.index(x) for x in I)
        out.add(idx[tuple(h[p[inv[x]]] for x in I)])
    return frozenset(out)
old_orbits = {orbit(i) for i in transient}
assert len(old_orbits) == 74
assert Counter(map(len,old_orbits)) == Counter({4:72,1:2})
port_labels_in_old_orbit = Counter(len({P[i][0] for i in o}) for o in old_orbits)
assert port_labels_in_old_orbit == Counter({4:60,1:14})

# Deterministic named action + Port trace partition.
colors = {i:P[i][0] for i in reachable}
trace_class_counts = [len(set(colors.values()))]
level_one = None
while True:
    sig = {i:(P[i][0], tuple(colors[transitions[i][a]] if a in transitions[i] else -1 for a in A))
           for i in reachable}
    labels = {s:k for k,s in enumerate(sorted(set(sig.values())))}
    new = {i:labels[sig[i]] for i in reachable}
    trace_class_counts.append(len(labels))
    if level_one is None:
        level_one = sig.copy()
    if len(labels) == len(set(colors.values())):
        assert all((colors[i] == colors[j]) == (new[i] == new[j])
                   for i in reachable for j in reachable)
        break
    colors = new
assert trace_class_counts == [6,131,291,291]
assert Counter(Counter(new.values()).values()) == Counter({1:290,60:1})
assert {i for i in reachable if list(new.values()).count(new[i]) > 1} == absorbing

count_depth = Counter()
for i in transient:
    for j in transient:
        if i >= j: continue
        d = 0 if P[i][0] != P[j][0] else (1 if level_one[i] != level_one[j] else 2)
        count_depth[d] += 1
assert count_depth == Counter({0:33600,1:8065,2:240})
assert sum(count_depth.values()) == 290*289//2

u = idx[(1,0,2,3,5,4)]
v = idx[(1,0,2,4,3,5)]
assert u in transient and v in transient
assert P[u][0] == P[v][0] == E.index((0,2))
assert level_one[u] == level_one[v]
for a in ((0,+1),(1,-1)):
    assert a in transitions[u] and a in transitions[v]
    u, v = transitions[u][a], transitions[v][a]
assert (E[P[u][0]], E[P[v][0]]) == ((2,3),(1,2))

# Unlabeled BRC: each permitted source branch has positive weight 1/4.
colors = {i:P[i][0] for i in reachable}
stochastic_class_counts = [len(set(colors.values()))]
while True:
    sig = {i:(P[i][0], tuple(sorted(Counter(colors[j] for j in transitions[i].values()).items())))
           for i in reachable}
    labels = {s:k for k,s in enumerate(sorted(set(sig.values())))}
    new = {i:labels[sig[i]] for i in reachable}
    stochastic_class_counts.append(len(labels))
    if len(labels) == len(set(colors.values())):
        break
    colors = new
assert stochastic_class_counts == [6,46,266,291,291]
assert Counter(Counter(new.values()).values()) == Counter({1:290,60:1})

# Full signed six-axis displacement on each admitted composite.
Hv = [tuple(int(i in S[v]) for i in I) for v in V]
def increment(i,v,s):
    p = P[i]
    return tuple(s*Hv[v][p.index(j)] for j in I)

colors = {i:P[i][0] for i in reachable}
cell_class_counts = [len(set(colors.values()))]
while True:
    sig = {i:(P[i][0], tuple((increment(i,v,s),colors[transitions[i][(v,s)]])
            if (v,s) in transitions[i] else None for v,s in A)) for i in reachable}
    labels = {s:k for k,s in enumerate(sorted(set(sig.values()),key=str))}
    new = {i:labels[sig[i]] for i in reachable}
    cell_class_counts.append(len(labels))
    if len(labels) == len(set(colors.values())):
        break
    colors = new
assert cell_class_counts == [6,320,350,350]
assert len(set(new.values())) == len(reachable)

out = {
    "schema":"R762GS_PORT_OBSERVER_MINIMAL_QUOTIENT_V1",
    "model":"MOVING_NAMED_PORT_K4_STAR_CANDIDATE",
    "task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
    "frozen_taskbook":"857280d1012943290d141d1317179c40ec3cbdf8",
    "frozen_science_p000":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "orientation_states":360,"reachable":350,"transient":290,"absorbing":60,
    "old_absorption_transient_H_orbits":74,
    "old_orbit_distinct_port_counts":{str(k):v for k,v in sorted(port_labels_in_old_orbit.items())},
    "named_trace_refinement_classes":trace_class_counts,
    "unlabeled_BRC_port_refinement_classes":stochastic_class_counts,
    "optimal_port_observer_state_count":291,
    "optimal_port_plus_cell_increment_state_count":350,
    "named_port_cell_increment_refinement_classes":cell_class_counts,
    "indistinguishable_absorbing_states":60,
    "transient_pair_min_distinguishing_length":{str(k):count_depth[k] for k in range(3)},
    "two_letter_witness":{"start_p":[[1,0,2,3,5,4],[1,0,2,4,3,5]],
                           "word":[[0,1],[1,-1]],"end_port_edges":[[2,3],[1,2]]},
    "author_check":"PASS","independent_review":"NOT_REVIEWED"
}
print(json.dumps(out,ensure_ascii=False,indent=2))
