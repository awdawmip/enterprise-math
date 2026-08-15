#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import defaultdict

V = tuple(range(4))
ADJ = {i: tuple(sorted({(i - 1) % 4, (i + 1) % 4})) for i in V}

def is_adjacent(x, y):
    return y in ADJ[x]

def walk_count(a, b, n):
    current = {a: 1}
    for _ in range(n):
        nxt = defaultdict(int)
        for x, count in current.items():
            for y in ADJ[x]:
                nxt[y] += count
        current = nxt
    return current.get(b, 0)

def phi(x):
    return (x + 1) % 4

def state_phi(s):
    return (phi(s[0]), phi(s[1]))

STATES = tuple((a, b) for a in V for b in V if a != b)

def elementary_moves(s):
    a, b = s
    out = []
    for na in ADJ[a]:
        if na != b:
            out.append({"from": s, "to": (na, b), "marker": "A"})
    for nb in ADJ[b]:
        if nb != a:
            out.append({"from": s, "to": (a, nb), "marker": "B"})
    out.sort(key=lambda m: (m["to"], m["marker"]))
    return out

def spectrum12(s):
    a, b = s
    return (walk_count(a, b, 1), walk_count(a, b, 2))

def e_strict(s):
    w1, w2 = spectrum12(s)
    return abs(w1 - 1) + abs(w2 - 0)

def e_plateau(s):
    w1, w2 = spectrum12(s)
    return 2 * w1 + w2

def accepted_graph(energy, allow_equal):
    graph = {s: [] for s in STATES}
    for s in STATES:
        for move in elementary_moves(s):
            t = tuple(move["to"])
            good = energy(t) <= energy(s) if allow_equal else energy(t) < energy(s)
            if good:
                graph[s].append(t)
        graph[s].sort()
    return graph

def find_cycle(graph):
    color = {v: 0 for v in graph}
    stack = []
    pos = {}
    def dfs(v):
        color[v] = 1
        pos[v] = len(stack)
        stack.append(v)
        for w in graph[v]:
            if color[w] == 0:
                r = dfs(w)
                if r:
                    return r
            elif color[w] == 1:
                i = pos[w]
                return stack[i:] + [w]
        stack.pop()
        pos.pop(v, None)
        color[v] = 2
        return None
    for v in graph:
        if color[v] == 0:
            r = dfs(v)
            if r:
                return r
    return None

def main():
    adjacency_automorphism = all(is_adjacent(x,y) == is_adjacent(phi(x),phi(y)) for x in V for y in V)
    t1_checks = []
    for n in range(0, 9):
        ok = all(walk_count(phi(a), phi(b), n) == walk_count(a, b, n) for a in V for b in V)
        t1_checks.append({"n": n, "all_pairs_invariant": ok})

    orbit = []
    s = (0, 1)
    while s not in orbit:
        orbit.append(s)
        s = state_phi(s)
    orbit_info = []
    for s in orbit:
        orbit_info.append({
            "state": s,
            "spectrum_1_2": spectrum12(s),
            "strict_E": e_strict(s),
            "plateau_E": e_plateau(s),
            "collective_successor": state_phi(s),
            "collective_successor_is_one_marker_elementary": any(tuple(m["to"]) == state_phi(s) for m in elementary_moves(s)),
        })

    g_strict = accepted_graph(e_strict, allow_equal=False)
    strict_cycle = find_cycle(g_strict)
    strict_edges = [(s,t) for s, outs in g_strict.items() for t in outs]
    strict_sinks = sorted([s for s, outs in g_strict.items() if not outs])

    g_neutral = accepted_graph(e_plateau, allow_equal=True)
    neutral_cycle = find_cycle(g_neutral)
    neutral_edges = [(s,t) for s, outs in g_neutral.items() for t in outs]
    cycle_detail = []
    if neutral_cycle:
        for a,b in zip(neutral_cycle[:-1], neutral_cycle[1:]):
            marker = next(m["marker"] for m in elementary_moves(a) if tuple(m["to"]) == b)
            cycle_detail.append({
                "from": a,
                "to": b,
                "marker": marker,
                "from_spectrum_1_2": spectrum12(a),
                "to_spectrum_1_2": spectrum12(b),
                "from_E": e_plateau(a),
                "to_E": e_plateau(b),
            })

    alternating_cycle = [(0,1), (3,1), (3,2), (0,2), (0,1)]
    alternating_cycle_detail = []
    alternating_cycle_valid = True
    for a,b in zip(alternating_cycle[:-1], alternating_cycle[1:]):
        moves = [m for m in elementary_moves(a) if tuple(m["to"]) == b]
        if len(moves) != 1 or e_plateau(a) != e_plateau(b):
            alternating_cycle_valid = False
            break
        alternating_cycle_detail.append({
            "from": a,
            "to": b,
            "marker": moves[0]["marker"],
            "from_spectrum_1_2": spectrum12(a),
            "to_spectrum_1_2": spectrum12(b),
            "from_E": e_plateau(a),
            "to_E": e_plateau(b),
        })
    if alternating_cycle_valid:
        alternating_cycle_valid = [d["marker"] for d in alternating_cycle_detail] == ["A","B","A","B"]

    output = {
        "schema": "R059P_TINY_EXACT_VALIDATION_OUTPUT_V1",
        "generation": "R059P",
        "researcher_id": "EM-R059P-8A2C7D",
        "carrier": {
            "id": "TOY_C4_RELATIONAL",
            "packets": list(V),
            "adjacency": {str(k): list(v) for k,v in ADJ.items()},
            "geometry_claimed": False,
        },
        "path_window": [1, 2],
        "t1": {
            "phi": "i -> i+1 mod 4 (packet-label permutation preserving adjacency)",
            "adjacency_automorphism_verified": adjacency_automorphism,
            "walk_count_checks": t1_checks,
            "sample_orbit": orbit_info,
        },
        "t2_strict_model": {
            "mismatch": "e=abs(W1-1)+abs(W2-0)",
            "state_count": len(STATES),
            "energy_histogram": {
                str(e): sum(1 for s in STATES if e_strict(s)==e)
                for e in sorted({e_strict(s) for s in STATES})
            },
            "accepted_directed_edge_count": len(strict_edges),
            "cycle": strict_cycle,
            "cycle_absent": strict_cycle is None,
            "sink_count": len(strict_sinks),
            "sinks": strict_sinks,
            "max_specific_accepted_steps": 1,
        },
        "t3_neutral_model": {
            "mismatch": "e=2*W1+W2",
            "state_count": len(STATES),
            "distinct_E_values": sorted({e_plateau(s) for s in STATES}),
            "accepted_directed_edge_count": len(neutral_edges),
            "minimal_cycle": neutral_cycle,
            "cycle_found": neutral_cycle is not None,
            "minimal_cycle_detail": cycle_detail,
            "alternating_marker_4_cycle": alternating_cycle,
            "alternating_marker_4_cycle_valid": alternating_cycle_valid,
            "alternating_marker_4_cycle_detail": alternating_cycle_detail,
            "pair_spectra_change_along_cycle": len({spectrum12(s) for s in alternating_cycle[:-1]}) > 1,
            "macro_E_constant_along_cycle": len({e_plateau(s) for s in alternating_cycle[:-1]}) == 1,
        },
        "separation_checks": {
            "automorphism_orbit_exists": len(orbit) > 1,
            "automorphism_orbit_same_pair_spectrum": len({spectrum12(s) for s in orbit}) == 1,
            "collective_automorphism_successors_are_not_one_marker_elementary": all(
                not x["collective_successor_is_one_marker_elementary"] for x in orbit_info
            ),
            "neutral_cycle_uses_only_one_marker_elementary_updates": bool(neutral_cycle) and len(cycle_detail)==len(neutral_cycle)-1,
            "alternating_marker_4_cycle_valid": alternating_cycle_valid,
        },
        "status": "PASS",
    }
    if not adjacency_automorphism or not all(x["all_pairs_invariant"] for x in t1_checks):
        output["status"] = "FAIL"
    if strict_cycle is not None:
        output["status"] = "FAIL"
    if neutral_cycle is None or not alternating_cycle_valid:
        output["status"] = "FAIL"
    print(json.dumps(output, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
