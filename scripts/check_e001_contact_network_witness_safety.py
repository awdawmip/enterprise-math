#!/usr/bin/env python3
"""Exact regression for E001 contact-network witness-safety quotient.

No external CAS is used.  The checker exhausts all labelled simple graphs on
1..5 vertices, verifies the incidence rank/cycle-nullity ledger exactly over Q,
and pressure-tests the minimal nonnegative triangle circulation.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json


def incidence(n, edges):
    B = [[0 for _ in edges] for _ in range(n)]
    for k, (u, v) in enumerate(edges):
        B[u][k] = -1
        B[v][k] = 1
    return B


def matvec(A, x):
    return tuple(sum(a*b for a, b in zip(row, x)) for row in A)


def rank_q(A):
    rows = [[Fraction(v) for v in row] for row in A]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if rows[i][c] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        p = rows[r][c]
        rows[r] = [v/p for v in rows[r]]
        for i in range(m):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a-f*b for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == m:
            break
    return r


def component_count(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    for u, v in edges:
        union(u, v)
    return len({find(i) for i in range(n)})


def exhaustive_graph_regression():
    graphs = cyclic = forests = 0
    first_cyclic = None
    for n in range(1, 6):
        universe = list(combinations(range(n), 2))
        for mask in range(1 << len(universe)):
            edges = [universe[i] for i in range(len(universe)) if (mask >> i) & 1]
            B = incidence(n, edges)
            c = component_count(n, edges)
            rank = rank_q(B)
            beta = len(edges) - n + c
            assert rank == n - c
            assert len(edges) - rank == beta
            graphs += 1
            if beta:
                cyclic += 1
                if first_cyclic is None:
                    first_cyclic = {"n": n, "edges": edges, "beta": beta}
            else:
                forests += 1
    assert first_cyclic == {"n": 3, "edges": [(0, 1), (0, 2), (1, 2)], "beta": 1}
    return graphs, forests, cyclic, first_cyclic


def triangle_pressure_test():
    # cyclic orientation 0->1, 1->2, 2->0
    B = [
        [-1, 0, 1],
        [ 1,-1, 0],
        [ 0, 1,-1],
    ]
    zero = (0, 0, 0)
    cycle = (1, 1, 1)
    assert matvec(B, cycle) == zero
    assert matvec(B, zero) == matvec(B, cycle)
    body_signature_zero = matvec(B, zero)
    body_signature_cycle = matvec(B, cycle)
    assert body_signature_zero == body_signature_cycle
    reservoir_zero = zero
    reservoir_cycle = cycle
    assert reservoir_zero != reservoir_cycle
    can_accept_edge0_zero = reservoir_zero[0] < 1
    can_accept_edge0_cycle = reservoir_cycle[0] < 1
    assert can_accept_edge0_zero and not can_accept_edge0_cycle
    return {
        "B": B,
        "j": zero,
        "j_prime": cycle,
        "Bj": body_signature_zero,
        "reservoir_after_j": reservoir_zero,
        "reservoir_after_j_prime": reservoir_cycle,
        "future_guard_edge0_accepts_after_j": can_accept_edge0_zero,
        "future_guard_edge0_accepts_after_j_prime": can_accept_edge0_cycle,
    }


def main():
    graphs, forests, cyclic, first_cyclic = exhaustive_graph_regression()
    triangle = triangle_pressure_test()
    report = {
        "schema": "E001_CONTACT_NETWORK_WITNESS_SAFETY_CHECK_V1",
        "status": "PASS",
        "exhaustive_simple_graphs_n_le_5": graphs,
        "forest_graphs": forests,
        "cyclic_graphs": cyclic,
        "first_cyclic_simple_graph": first_cyclic,
        "triangle_persistent_witness_counterexample": triangle,
        "verified_claims": [
            "rank(B)=V-c and nullity(B)=E-V+c for every tested graph",
            "the first cyclic simple graph is C3",
            "j=(0,0,0) and j'=(1,1,1) on cyclically oriented C3 have Bj=Bj'=0",
            "body-only future signatures are invariant under the cycle shift",
            "faithful per-contact cumulative reservoir state distinguishes the same-body-update witnesses",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
