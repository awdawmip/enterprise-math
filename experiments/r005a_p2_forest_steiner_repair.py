#!/usr/bin/env python3
"""R005-A forest + partial-Steiner residual repair verifier."""

from __future__ import annotations

import importlib.util
from itertools import combinations, product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


amb = load("ambient", HERE / "r005a_p2_ambient_shadow_complex.py")
family = amb.family


def is_forest(edges):
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
    return True


def forest_vertex_cover_size(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)

    seen = set()
    total = 0
    for root in list(adj):
        if root in seen:
            continue
        parent = {root: None}
        order = [root]
        seen.add(root)
        for v in order:
            for w in adj[v]:
                if w == parent[v]:
                    continue
                if w in seen:
                    raise AssertionError("not a forest")
                seen.add(w)
                parent[w] = v
                order.append(w)

        dp0 = {}
        dp1 = {}
        for v in reversed(order):
            children = [w for w in adj[v] if parent.get(w) == v]
            dp0[v] = sum(dp1[w] for w in children)
            dp1[v] = 1 + sum(min(dp0[w], dp1[w]) for w in children)
        total += min(dp0[root], dp1[root])
    return total


def branch_repair_number(blocks):
    e2 = [tuple(s) for s in blocks if len(s) == 2]
    e3 = [tuple(s) for s in blocks if len(s) == 3]
    assert is_forest(e2)

    if not e3:
        return forest_vertex_cover_size(e2), 1

    best = None
    branches = 0
    for picks in product(*e3):
        branches += 1
        selected = set(picks)
        remaining = [e for e in e2 if not (set(e) & selected)]
        value = len(selected) + forest_vertex_cover_size(remaining)
        if best is None or value < best:
            best = value
    return best, branches


def brute_tau(blocks):
    if not blocks:
        return 0
    vertices = sorted(set().union(*map(set, blocks)))
    for r in range(1, len(vertices) + 1):
        for choice in combinations(vertices, r):
            selected = set(choice)
            if all(selected & set(block) for block in blocks):
                return r
    raise AssertionError


def main():
    basins = sorted({k for k, _, _ in family.CERTIFICATES})
    ambient_e2 = ambient_e3 = residual_e2 = residual_e3 = 0
    total_branches = 0
    rows = []

    for k in basins:
        h = amb.ambient_blocks(k)
        ambient2 = [s for s in h if len(s) == 2]
        ambient3 = [s for s in h if len(s) == 3]
        assert is_forest(ambient2)

        vertices = set().union(*(set(s) for s in h)) if h else set()
        nf = amb.nonforced_vertices(k, vertices)
        residual = [s for s in h if set(s) <= nf]
        r2 = [s for s in residual if len(s) == 2]
        r3 = [s for s in residual if len(s) == 3]
        assert is_forest(r2)

        tau_branch, branches = branch_repair_number(residual)
        tau_brute = brute_tau(residual)
        assert tau_branch == tau_brute

        ambient_e2 += len(ambient2)
        ambient_e3 += len(ambient3)
        residual_e2 += len(r2)
        residual_e3 += len(r3)
        total_branches += branches
        rows.append({
            "k": k,
            "ambient_repeated_edges": len(ambient2),
            "ambient_squarefree_triangles": len(ambient3),
            "residual_repeated_edges": len(r2),
            "residual_squarefree_triangles": len(r3),
            "repair_tau": tau_branch,
            "repair_branches": branches,
        })

    assert ambient_e2 == 148
    assert ambient_e3 == 2349
    assert residual_e2 == 45
    assert residual_e3 == 5

    result = {
        "status": "R005-A FOREST + PARTIAL-STEINER REPAIR DECOMPOSITION EXACT CHECK",
        "verified_basins": len(basins),
        "ambient_repeated_edges": ambient_e2,
        "ambient_squarefree_triangles": ambient_e3,
        "residual_repeated_edges": residual_e2,
        "residual_squarefree_triangles": residual_e3,
        "all_ambient_repeated_graphs_are_forests": True,
        "all_residual_repeated_graphs_are_forests": True,
        "branch_repair_equals_bruteforce_tau": True,
        "total_triangle_choice_branches_current_family": total_branches,
        "theorems": {
            "normal_form": "H_k = repeated forest G_k union squarefree partial Steiner triple system T_k",
            "residual_shadow": "R_k = H_k[NF_k]",
            "repair_algorithm": "enumerate one selected vertex per residual 3-edge; after unioning selections, solve minimum vertex cover on remaining repeated forest",
            "parameterized_complexity": "O(3^s * poly(v)) where s is the number of residual squarefree 3-edges",
            "repeated_only": "if s=0, repair is forest vertex cover and equals maximum matching by classical Konig on forests",
        },
        "rows": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
