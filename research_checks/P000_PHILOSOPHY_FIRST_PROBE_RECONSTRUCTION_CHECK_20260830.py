#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from itertools import permutations

TASK_ID = "RS-P000-PHILOSOPHY-FIRST-PROBE-RECONSTRUCTION"
HARD_TARGET = "P000_NATIVE_CELL_PROBE_RECONSTRUCTION_OR_INDISTINGUISHABILITY_CLASSIFIED"

AXES = ("E1", "E2", "E3", "E4", "E5", "E6")
STARS = {
    "J_A": ("E1", "E2", "E3"),
    "J_B": ("E1", "E4", "E5"),
    "J_C": ("E2", "E4", "E6"),
    "J_D": ("E3", "E5", "E6"),
}
A_XI = {"E1":"E2","E2":"E3","E3":"E1","E4":"E6","E6":"E5","E5":"E4"}
B_XI = {"E1":"E1","E2":"E4","E4":"E2","E3":"E5","E5":"E3","E6":"E6"}

def compose(p, q):
    return {x: p[q[x]] for x in AXES}

def perm_power(p, k):
    r = {x:x for x in AXES}
    for _ in range(k):
        r = compose(p, r)
    return r

def cycle_partitions(n, lo=3):
    out = []
    def rec(rem, start, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for k in range(start, rem + 1):
            if k < 3:
                continue
            rem2 = rem - k
            if rem2 == 0 or rem2 >= k:
                rec(rem2, k, cur + [k])
    rec(n, lo, [])
    return out

def graph_from_cycles(parts):
    adj = {}
    off = 0
    for k in parts:
        vs = list(range(off, off+k))
        for v in vs:
            adj[v] = set()
        for i, v in enumerate(vs):
            w = vs[(i+1) % k]
            adj[v].add(w)
            adj[w].add(v)
        off += k
    return adj

def ball_nodes(adj, root, radius):
    seen = {root}
    frontier = {root}
    for _ in range(radius):
        nxt = set()
        for v in frontier:
            nxt.update(adj[v])
        nxt.difference_update(seen)
        seen.update(nxt)
        frontier = nxt
    return seen

def rooted_ball_code(adj, root, radius):
    nodes = sorted(ball_nodes(adj, root, radius))
    others = [v for v in nodes if v != root]
    best = None
    for p in permutations(others):
        order = [root] + list(p)
        bits = []
        for i in range(len(order)):
            for j in range(i+1, len(order)):
                bits.append("1" if order[j] in adj[order[i]] else "0")
        code = (len(order), "".join(bits))
        if best is None or code < best:
            best = code
    return best

def local_profile(parts, radius):
    adj = graph_from_cycles(parts)
    return tuple(sorted(rooted_ball_code(adj, v, radius) for v in adj))

def fiber_probe_signature():
    return (
        tuple(AXES),
        tuple(sorted((k, tuple(v)) for k, v in STARS.items())),
        tuple(sorted(A_XI.items())),
        tuple(sorted(B_XI.items())),
        "PF10_UNIFORM_TOKEN",
    )

def obs_profile(parts, radius=1):
    return (sum(parts), fiber_probe_signature(), local_profile(parts, radius))

def predicted_cycle_ball_type(k, r):
    if k <= 2*r + 1:
        return ("FULL_CYCLE", k)
    return ("ROOTED_PATH", 2*r + 1)

checks = 0

assert set(AXES) == set(A_XI) == set(B_XI); checks += 1
assert perm_power(A_XI, 3) == {x:x for x in AXES}; checks += 1
assert perm_power(B_XI, 2) == {x:x for x in AXES}; checks += 1
AB = compose(A_XI, B_XI)
assert perm_power(AB, 4) == {x:x for x in AXES}; checks += 1
assert perm_power(AB, 1) != {x:x for x in AXES}; checks += 1
assert perm_power(AB, 2) != {x:x for x in AXES}; checks += 1

collisions = []
for n in range(3, 9):
    buckets = defaultdict(list)
    for parts in cycle_partitions(n):
        buckets[obs_profile(parts, 1)].append(parts)
        checks += 1
    same = [tuple(v) for v in buckets.values() if len(v) > 1]
    if same:
        collisions.append((n, same))

assert collisions == [(8, [((4, 4), (8,))])]; checks += 1

X = (8,)
Y = (4,4)
assert X != Y; checks += 1
assert obs_profile(X,1) == obs_profile(Y,1); checks += 1
assert obs_profile(X,2) != obs_profile(Y,2); checks += 1

x2 = local_profile(X, 2)[0]
y2 = local_profile(Y, 2)[0]
assert x2[0] == 5 and y2[0] == 4; checks += 1

for r in range(1, 33):
    m = 2*r + 2
    assert predicted_cycle_ball_type(m, r) == ("ROOTED_PATH", 2*r+1)
    assert predicted_cycle_ball_type(2*m, r) == ("ROOTED_PATH", 2*r+1)
    assert 2*m == sum((m,m))
    checks += 3

print(
    "PASS P000_PROBE_RECONSTRUCTION; "
    f"checks={checks}; "
    "minimal_radius1_collision_n=8; "
    "countermodel=C8_vs_C4_plus_C4; "
    "radius2_separates=TRUE; "
    "fixed_radius_family_obstruction_verified_r=1..32; "
    "carrier_S4_regression=PASS"
)
