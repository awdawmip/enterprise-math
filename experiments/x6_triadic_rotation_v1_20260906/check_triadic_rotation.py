#!/usr/bin/env python3
"""Exact finite checks for X6 triadic signed-C6 rotation research.

This checker reuses the current signed-X6 BRC multiplicity implementation and
independently implements only the finite signed-permutation/frame algebra that
is new in this research note.
"""
from __future__ import annotations

from collections import deque
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BRC_PATH = ROOT / "experiments" / "x6_signed_native_spatial_v16_20260905" / "signed_brc.py"
spec = spec_from_file_location("x6_signed_brc", BRC_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load existing signed_brc.py")
brc = module_from_spec(spec)
spec.loader.exec_module(brc)

N = 6
IDENTITY = tuple(range(1, N + 1))


def compose(g, h):
    """Signed permutation g after h; image list uses +/- 1-based axes."""
    out = []
    for x in h:
        sign = 1 if x > 0 else -1
        y = g[abs(x) - 1]
        out.append(sign * y)
    return tuple(out)


def power(g, k):
    out = IDENTITY
    for _ in range(k):
        out = compose(g, out)
    return out


def q_triad(S):
    """Q=-rho on selected oriented ascending triple S=(i,j,k)."""
    i, j, k = S
    q = list(IDENTITY)
    q[i] = -(j + 1)
    q[j] = -(k + 1)
    q[k] = -(i + 1)
    return tuple(q)


def act(g, z):
    out = [0] * N
    for i, coeff in enumerate(z):
        if coeff == 0:
            continue
        image = g[i]
        out[abs(image) - 1] += (1 if image > 0 else -1) * coeff
    return tuple(out)


def unit(i, sign=1):
    out = [0] * N
    out[i] = sign
    return tuple(out)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def perm_parity(g):
    p = [abs(x) - 1 for x in g]
    inversions = sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N))
    return inversions % 2


def main():
    triples = tuple(combinations(range(N), 3))
    local_checks = 0

    for S in triples:
        q = q_triad(S)
        assert power(q, 6) == IDENTITY
        q3 = power(q, 3)
        for i in range(N):
            expected = unit(i, -1 if i in S else 1)
            assert act(q3, unit(i)) == expected

        a0 = unit(S[0])
        orbit = [a0]
        for _ in range(5):
            orbit.append(act(q, orbit[-1]))
        assert len(set(orbit)) == 6
        assert act(q, orbit[-1]) == a0

        outer_states = []
        for r in range(6):
            a = orbit[r]
            b = orbit[(r + 1) % 6]
            d = sub(b, a)
            assert brc.shortest_event_count(d) == 2
            assert brc.shortest_path_multiplicity(d) == 2
            m = add(a, b)
            assert brc.shortest_event_count(sub(m, a)) == 1
            assert brc.shortest_event_count(sub(b, m)) == 1
            outer_states.extend((a, m))
            local_checks += 1
        assert len(set(outer_states)) == 12

    generators = tuple(q_triad(S) for S in triples)
    group = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for g in generators:
            nxt = compose(g, current)
            if nxt not in group:
                group.add(nxt)
                queue.append(nxt)

    assert len(group) == 23040
    assert all(perm_parity(g) == 0 for g in group)

    pure_sign_patterns = {
        tuple(1 if x < 0 else 0 for x in g)
        for g in group
        if tuple(abs(x) for x in g) == IDENTITY
    }
    assert len(pure_sign_patterns) == 64

    # Shortest-fiber composition obstruction: Q followed by Q^-1.
    q = q_triad((0, 1, 2))
    q_inv = power(q, 5)
    a = unit(0)
    b = act(q, a)
    assert act(q_inv, b) == a
    assert brc.shortest_event_count(sub(b, a)) == 2
    assert brc.shortest_event_count(sub(a, b)) == 2
    assert brc.shortest_event_count(sub(a, a)) == 0

    print("PASS_X6_TRIADIC_ROTATION_GENERATORS")
    print("three_axis_selections", len(triples))
    print("macro_edges_checked", local_checks)
    print("generated_group_order", len(group))
    print("pure_sign_subgroup_order", len(pure_sign_patterns))
    print("expected_structure", "(C2)^6 semidirect A6")
    print("shortest_rotation_fiber_composition", "NOT_CLOSED")


if __name__ == "__main__":
    main()
