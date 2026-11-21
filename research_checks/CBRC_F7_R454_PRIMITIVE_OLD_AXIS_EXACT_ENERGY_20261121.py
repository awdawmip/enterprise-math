#!/usr/bin/env python3
"""Exact rational independent graph check for Driver F7 r454 (old-axis subsystem).

This checker verifies r454's finite rational formula against the *full explicitly
constructed primitive old-axis graph*, including both fixed marked scalar points.
It checks all edge inequalities and solves each path by an exact optimal witness.
It does not check every original four-coordinate F7 inequality or prove the
all-L theorem by finite testing.
"""

from collections import defaultdict
from fractions import Fraction
from math import gcd


def F(n: int) -> Fraction:
    return Fraction((n // 2) * (n - n // 2), n) if n else Fraction(0)


def predicted_energy(L: int) -> Fraction:
    X = 3 * L - 2

    def length(t: int, residue: int) -> int:
        return 1 + (X - residue) // (3 * t)

    result = 1 + F(L - 2) + F(L) + 1 + F(L - 3) + 3 * F(L - 1)
    result += F(2 * length(2, 3))
    for t in range(2, L):
        d = 3 * t
        for r in range(1, (d + 1) // 2):
            if gcd(r, t) == 1:
                result += 2 * F(length(t, r) + length(t, d - r))
    return result


def free_path_values(n: int) -> list[Fraction]:
    if n % 2 == 0:
        return [Fraction(1, 2)] * n
    k = n // 2
    return [
        Fraction(k, n) if j % 2 == 0 else Fraction(k + 1, n)
        for j in range(n)
    ]


def exact_graph_energy(L: int) -> tuple[Fraction, int, int]:
    X = 3 * L - 2
    marks = {(1, -1), (2, 1)}
    edges = defaultdict(set)

    for t in range(1, L):
        d = 3 * t
        for x in range(1, X + 1):
            if gcd(x, t) != 1:
                continue
            edges[(x, t)]
            edges[(x, -t)]
            opposite_xs = [x - d, x + d]
            if t >= 2:
                opposite_xs.append(d - x)
            for y in opposite_xs:
                if 1 <= y <= X and gcd(y, t) == 1:
                    a, b = (x, t), (y, -t)
                    edges[a].add(b)
                    edges[b].add(a)

    seen = set()
    values = {}
    components = 0
    for start in edges:
        if start in seen:
            continue
        stack = [start]
        nodes = {start}
        while stack:
            v = stack.pop()
            for w in edges[v]:
                if w not in nodes:
                    nodes.add(w)
                    stack.append(w)
        seen.update(nodes)
        components += 1

        assert all(len(edges[v]) <= 2 for v in nodes)
        endpoints = [v for v in nodes if len(edges[v]) <= 1]
        assert endpoints, "Every finite component must be a path"
        first = next((v for v in endpoints if v in marks), endpoints[0])
        order = [first]
        previous = None
        while len(order) < len(nodes):
            onward = [v for v in edges[order[-1]] if v != previous]
            assert len(onward) == 1
            previous = order[-1]
            order.append(onward[0])
        assert len(set(order)) == len(nodes)

        if any(v in marks for v in order):
            assert order[0] in marks and len(order) >= 2
            assignment = [Fraction(0), Fraction(1)]
            assignment += free_path_values(len(order) - 2)
        else:
            assignment = free_path_values(len(order))
        values.update(zip(order, assignment))

    assert values[(1, -1)] == values[(2, 1)] == 0
    for v in edges:
        for w in edges[v]:
            assert values[v] + values[w] >= 1

    energy = sum((v * v for v in values.values()), Fraction(0))
    return energy, len(values), components


def main() -> None:
    for L in (3, 4, 5, 6, 8, 10, 15, 20, 50, 100):
        from_graph, vertices, components = exact_graph_energy(L)
        from_formula = predicted_energy(L)
        assert from_graph == from_formula, (L, from_graph, from_formula)
        print(f"L={L:3d}  Q(L)={str(from_formula):>29}  "
              f"vertices={vertices:6d}  paths={components:5d}  exact=PASS")


if __name__ == "__main__":
    main()
