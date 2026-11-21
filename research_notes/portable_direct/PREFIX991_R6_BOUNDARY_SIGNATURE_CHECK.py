"""PREFIX-991: exact WBRC-T36 last-port boundary histogram check.
Standalone Python 3, fractions + integer Counter. Auxiliary signed-source
observer, not native X6 dynamics.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path

WORDS = ((6, 24, 6, -3), (6, 24, 8, 40))
def u(h):
    return Fraction({0: 1, 1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13}.get(h, 17+h))
def v(a, mode):
    return Fraction(1 if mode == "port_only" else (2 if a[3] == 1 else 3))

def build(word):
    p = max(abs(c) for c in word).bit_length() + 1
    sources = {q: tuple((q, i, j, sign)
              for i in range(p) for j in range(1, p)
              for sign in (1, -1) if (1 << i) - sign * (1 << j) == c)
              for q, c in enumerate(word)}
    ports = tuple(sorted({a[2] for group in sources.values() for a in group}))
    starts = tuple((0, 1 + sum((1 << j) for k, j in enumerate(ports) if mask >> k & 1))
                   for mask in range(1 << len(ports)))
    pending, seen, edges = deque(starts), set(starts), {}
    while pending:
        state = pending.popleft()
        q, x = state
        row = []
        for a in sources[q]:
            if (x >> a[2] & 1) != (1 - a[3]) // 2:
                continue
            target = ((q + 1) % len(word), x ^ (1 << a[2]))
            row.append((a, target))
            if target not in seen:
                seen.add(target)
                pending.append(target)
        edges[state] = tuple(sorted(row))
    return p, ports, starts, edges

def direct(starts, edges, length, mode, initial_h=0):
    cur = Counter({(state, initial_h, Fraction(1)): 1 for state in starts})
    for _ in range(length):
        nxt = Counter()
        for (state, hist, mass), count in cur.items():
            for a, target in edges[state]:
                nxt[(target, a[2], mass*u(hist)*v(a, mode))] += count
        cur = nxt
    return cur

def delayed(starts, edges, length, mode, initial_h=0):
    if length == 0:
        return Counter({(state, initial_h, Fraction(1)): 1 for state in starts})
    cur = Counter({(state, Fraction(1)): 1 for state in starts})
    for _ in range(length - 1):
        nxt = Counter()
        for (state, mass), count in cur.items():
            for a, target in edges[state]:
                nxt[(target, mass*u(a[2])*v(a, mode))] += count
        cur = nxt
    ans = Counter()
    for (state, mass), count in cur.items():
        for a, target in edges[state]:
            ans[(target, a[2], mass*u(initial_h)*v(a, mode))] += count
    return ans

def glue(starts, edges, n, m, mode):
    first = delayed(starts, edges, n, mode)
    @lru_cache(None)
    def right(state, port):
        return delayed((state,), edges, m, mode, port)
    ans = Counter()
    for (state, port, mass), count in first.items():
        for (last, last_port, mass2), count2 in right(state, port).items():
            ans[(last, last_port, mass*mass2)] += count*count2
    return ans

def witness(starts, edges):
    for origin in starts:
        current = {(origin, 0): ()}
        for length in range(1, 12):
            nxt = {}
            for (state, port), path in current.items():
                for a, target in edges[state]:
                    nxt.setdefault((target, a[2]), path + (a,))
            current = nxt
            buckets = defaultdict(list)
            for (state, port), path in current.items():
                buckets[state].append((port, path))
            for state, options in buckets.items():
                for k, (port1, path1) in enumerate(options):
                    for port2, path2 in options[k+1:]:
                        if port1 == port2 or u(port1) == u(port2) or not edges[state]:
                            continue
                        a, target = edges[state][0]
                        return {
                            "initial": list(origin), "steps": length,
                            "same_old_state": list(state),
                            "last_ports": [port1, port2],
                            "path_1": [list(x) for x in path1],
                            "path_2": [list(x) for x in path2],
                            "common_next_named_source": list(a),
                            "port_only_next_weights": [str(u(port1)), str(u(port2))],
                            "signed_source_next_weights": [
                                str(u(port1)*v(a, "signed_source")),
                                str(u(port2)*v(a, "signed_source"))]
                        }

def summarize(hist):
    weights = Counter()
    for (_, _, mass), count in hist.items():
        weights[mass] += count
    encoded = [[str(weight), count] for weight, count in sorted(weights.items())]
    return {
        "count": sum(weights.values()),
        "total_mass": str(sum((weight*count for weight, count in weights.items()), Fraction(0))),
        "distinct_weights": len(weights),
        "terminal_cells": len(hist),
        "histogram_sha256": hashlib.sha256(
            json.dumps(encoded, separators=(",", ":")).encode()).hexdigest()
    }

def main():
    result = {
        "schema": "PREFIX991_R6_TERMINAL_PORT_WBRC_SIGNATURE_V1",
        "scope": "auxiliary signed-source positive BRC histogram",
        "arithmetic": "exact Fraction and integer multiplicity",
        "tested_lengths": [0, 12],
        "tested_gluing_splits": [[1, 1], [2, 3], [3, 4]],
        "families": []
    }
    for word in WORDS:
        p, ports, starts, edges = build(word)
        item = {"word": list(word), "width": p, "ports": ports,
                "initial_states": len(starts), "old_reachable_states": len(edges)}
        for mode in ("port_only", "signed_source"):
            for n in range(13):
                assert direct(starts, edges, n, mode) == delayed(starts, edges, n, mode)
            for n, m in ((1, 1), (2, 3), (3, 4)):
                assert direct(starts, edges, n+m, mode) == glue(starts, edges, n, m, mode)
            item[mode] = {str(n): summarize(delayed(starts, edges, n, mode))
                          for n in (4, 7, 8, 12)}
        item["port_obstruction"] = witness(starts, edges)
        assert item["port_obstruction"]
        result["families"].append(item)
    out = Path(__file__).with_name("PREFIX991_R6_EXACT_RESULTS.json")
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf8")
    print("PASS: 2 source words, 2 BRC positive laws, lengths 0..12, 3 gluing splits")
    for item in result["families"]:
        print(item["word"], item["old_reachable_states"],
              item["port_only"]["8"], item["signed_source"]["8"])

if __name__ == "__main__":
    main()
