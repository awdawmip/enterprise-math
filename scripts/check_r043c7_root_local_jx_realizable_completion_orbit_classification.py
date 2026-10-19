#!/usr/bin/env python3
"""Exact R043-C7 fixed two-shell trace-carrier checker.

This checker verifies only finite native-incidence facts and two explicit
counterexamples to small abstract-G0-radius locality. The global structural
support theorem is proved in the research return.
"""
from __future__ import annotations
from collections import Counter, deque
import json

Point = tuple[int, int, int]
ROOT: Point = (0, 0, 0)

FCC_DIRS: list[Point] = []
for zero in range(3):
    others = [i for i in range(3) if i != zero]
    for a in (-1, 1):
        for b in (-1, 1):
            v = [0, 0, 0]
            v[others[0]] = a
            v[others[1]] = b
            FCC_DIRS.append(tuple(v))
FCC_DIRS_T = tuple(sorted(FCC_DIRS))
TRI_DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def fcc_neighbors(p: Point) -> tuple[Point, ...]:
    x, y, z = p
    return tuple((x + dx, y + dy, z + dz) for dx, dy, dz in FCC_DIRS_T)


def hcp_neighbors(p: Point) -> tuple[Point, ...]:
    i, j, k = p
    out = [(i + di, j + dj, k) for di, dj in TRI_DIRS]
    offsets = ((0, 0), (-1, 0), (0, -1)) if k % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    for dk in (-1, 1):
        for di, dj in offsets:
            out.append((i + di, j + dj, k + dk))
    return tuple(out)


def frontier(C, neighbors) -> set[Point]:
    C = set(C)
    out: set[Point] = set()
    for p in C:
        out.update(neighbors(p))
    return out - C


def connected(C, neighbors) -> bool:
    C = set(C)
    if not C:
        return False
    seen = {next(iter(C))}
    q = list(seen)
    while q:
        p = q.pop()
        for u in neighbors(p):
            if u in C and u not in seen:
                seen.add(u)
                q.append(u)
    return len(seen) == len(C)


def carrier(neighbors):
    shell = set(neighbors(ROOT))
    second = set()
    for z in shell:
        second.update(neighbors(z))
    second.discard(ROOT)
    second -= shell
    link_edges = {
        frozenset((a, b))
        for a in shell
        for b in neighbors(a)
        if b in shell and a != b
    }
    link_degrees = Counter(sum(u in shell for u in neighbors(a)) for a in shell)
    trace_hist = Counter(len(set(neighbors(q)) & shell) for q in second)
    support_capture = all(
        u == ROOT or u in shell or u in second
        for z in shell
        for u in neighbors(z)
    )
    return shell, second, link_edges, link_degrees, trace_hist, support_capture


def g0_dist_to_old_endpoint(C, z, y, neighbors) -> dict:
    C = set(C)
    F = frontier(C, neighbors)
    Z = set(neighbors(ROOT)) - C - F
    if ROOT not in F:
        raise AssertionError("root_not_frontier")
    if z not in Z:
        raise AssertionError("z_not_new_zero_weight_site")
    if y not in F - {ROOT}:
        raise AssertionError("y_not_surviving_old_frontier")
    if y not in neighbors(z):
        raise AssertionError("z_y_not_native_contact")
    dist = {ROOT: 0}
    q = deque([ROOT])
    while q:
        p = q.popleft()
        for u in neighbors(p):
            if u in F and u not in dist:
                dist[u] = dist[p] + 1
                q.append(u)
    shell, second, *_ = carrier(neighbors)
    if z not in shell or y not in shell | second:
        raise AssertionError("two_shell_capture_failed")
    return {
        "occupied_size": len(C),
        "connected": connected(C, neighbors),
        "z": list(z),
        "y": list(y),
        "g0_distance_root_to_y": dist[y],
        "native_two_shell_captured": True,
    }


def main() -> None:
    worlds = {}
    expected = {
        "fcc": {
            "second_shell_slots": 42,
            "link_edges": 24,
            "link_degree_hist": {4: 12},
            "trace_size_hist": {1: 12, 2: 24, 4: 6},
        },
        "hcp": {
            "second_shell_slots": 44,
            "link_edges": 24,
            "link_degree_hist": {4: 12},
            "trace_size_hist": {1: 18, 2: 18, 3: 2, 4: 6},
        },
    }
    for name, neighbors in (("fcc", fcc_neighbors), ("hcp", hcp_neighbors)):
        shell, second, link_edges, link_degrees, trace_hist, support_capture = carrier(neighbors)
        row = {
            "root_shell_slots": len(shell),
            "second_shell_slots": len(second),
            "two_shell_carrier_slots_excluding_root": len(shell | second),
            "link_edges": len(link_edges),
            "link_degree_hist": dict(sorted(link_degrees.items())),
            "trace_size_hist": dict(sorted(trace_hist.items())),
            "support_capture": support_capture,
            "max_second_shell_trace_size": max(trace_hist),
        }
        exp = expected[name]
        row["pass"] = (
            row["root_shell_slots"] == 12
            and row["second_shell_slots"] == exp["second_shell_slots"]
            and row["link_edges"] == exp["link_edges"]
            and row["link_degree_hist"] == exp["link_degree_hist"]
            and row["trace_size_hist"] == exp["trace_size_hist"]
            and support_capture
        )
        worlds[name] = row

    fcc_C = {
        (0, -3, -1),
        (0, -1, 1),
        (1, -3, 0),
        (1, -2, 1),
    }
    hcp_C = {
        (-1, 1, 0),
        (-1, 1, 1),
        (0, 1, 2),
        (1, 0, 2),
        (1, 0, 3),
        (1, 1, 3),
        (2, -2, 1),
        (2, -1, 2),
    }
    witnesses = {
        "fcc_graph_radius_2_shortcut_refutation": {
            "occupied": [list(p) for p in sorted(fcc_C)],
            **g0_dist_to_old_endpoint(fcc_C, (0, -1, -1), (0, -2, -2), fcc_neighbors),
            "expected_distance": 3,
        },
        "hcp_graph_radius_3_shortcut_refutation": {
            "occupied": [list(p) for p in sorted(hcp_C)],
            **g0_dist_to_old_endpoint(hcp_C, (1, -1, 0), (2, -2, 0), hcp_neighbors),
            "expected_distance": 4,
        },
    }
    witness_pass = all(
        w["connected"] and w["g0_distance_root_to_y"] == w["expected_distance"]
        for w in witnesses.values()
    )
    ok = all(row["pass"] for row in worlds.values()) and witness_pass
    payload = {
        "schema": "ENTERPRISE_MATH_R043C7_TWO_SHELL_TRACE_CARRIER_CHECK_V1",
        "task_id": "RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION",
        "theorem_checked": "Every J_x edge is supported on the fixed native two-shell carrier S_x union Q_x; second-shell old incidences are root-shell traces of size at most four.",
        "worlds": worlds,
        "graph_radius_shortcut_counterexamples": witnesses,
        "pass": ok,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
