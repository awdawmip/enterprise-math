"""Finite CSP explorer for the R007 divisibility-residue naturality tower.

The global theorem is infinitary, but every fixed finite scale prefix is a
finite-domain constraint problem.  This module deliberately avoids floating
point geometry: cell intersections are tested by cross multiplication.
"""

from __future__ import annotations

from collections import deque
from itertools import product
from math import gcd
from typing import Iterable, Iterator, Sequence

ResidueMap = tuple[int, ...]
Cell = tuple[int, int]  # (scale, cell index)


def cells_overlap(d: int, i: int, e: int, j: int) -> bool:
    """Whether [i/d,(i+1)/d) and [j/e,(j+1)/e) overlap in positive length."""
    if d < 1 or e < 1 or not (0 <= i < d) or not (0 <= j < e):
        raise ValueError("invalid scale/cell")
    return i * e < (j + 1) * d and j * d < (i + 1) * e


def overlap_edge_count(d: int, e: int) -> int:
    return sum(cells_overlap(d, i, e, j) for i in range(d) for j in range(e))


def overlap_component_count(d: int, e: int) -> int:
    """Connected components of the bipartite cell-overlap graph B(d,e)."""
    vertices = [(0, i) for i in range(d)] + [(1, j) for j in range(e)]
    adj = {v: [] for v in vertices}
    for i in range(d):
        for j in range(e):
            if cells_overlap(d, i, e, j):
                adj[(0, i)].append((1, j))
                adj[(1, j)].append((0, i))
    seen: set[tuple[int, int]] = set()
    components = 0
    for start in vertices:
        if start in seen:
            continue
        components += 1
        stack = [start]
        seen.add(start)
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return components


def pair_compatible(f: Sequence[int], d: int, g: Sequence[int], e: int) -> bool:
    """Colored graph-endomorphism criterion for two residue scales."""
    if len(f) != d or len(g) != e:
        raise ValueError("map length must equal its scale")
    for i in range(d):
        for j in range(e):
            if cells_overlap(d, i, e, j) and not cells_overlap(d, f[i], e, g[j]):
                return False
    return True


def preserves_divisor_partition(f: Sequence[int], r: int, d: int) -> bool:
    """Whether f:R_r->R_r descends through the canonical projection r->d."""
    if r % d:
        raise ValueError("d must divide r")
    if len(f) != r:
        raise ValueError("map length must equal r")
    block = r // d
    for a in range(d):
        images = {f[s] // block for s in range(a * block, (a + 1) * block)}
        if len(images) != 1:
            return False
    return True


def internally_coherent(f: Sequence[int], r: int) -> bool:
    return all(preserves_divisor_partition(f, r, d) for d in range(1, r + 1) if r % d == 0)


def path_nonexpansive(f: Sequence[int]) -> bool:
    return all(abs(f[i + 1] - f[i]) <= 1 for i in range(len(f) - 1))


def path_maps(r: int) -> Iterator[ResidueMap]:
    """Generate the necessary path-1-Lipschitz candidates without r^r brute force."""
    if r < 1:
        raise ValueError("r must be positive")
    seq: list[int] = []

    def rec() -> Iterator[ResidueMap]:
        if len(seq) == r:
            yield tuple(seq)
            return
        if not seq:
            values = range(r)
        else:
            last = seq[-1]
            values = range(max(0, last - 1), min(r - 1, last + 1) + 1)
        for value in values:
            seq.append(value)
            yield from rec()
            seq.pop()

    yield from rec()


def _constraint_graph(scales: Sequence[int]) -> tuple[list[Cell], dict[Cell, list[Cell]]]:
    variables = [(d, i) for d in scales for i in range(d)]
    neighbors: dict[Cell, list[Cell]] = {v: [] for v in variables}
    for pos, x in enumerate(variables):
        d, i = x
        for y in variables[pos + 1 :]:
            e, j = y
            if cells_overlap(d, i, e, j):
                neighbors[x].append(y)
                neighbors[y].append(x)
    return variables, neighbors


def finite_prefix_extendable(fixed: Sequence[int], r: int, max_scale: int) -> bool:
    """Exact CSP decision for extension over scales 1..max_scale (plus r)."""
    if len(fixed) != r or max_scale < 1:
        raise ValueError("invalid fixed map / max_scale")
    scales = sorted(set(range(1, max_scale + 1)) | {r})
    variables, neighbors = _constraint_graph(scales)
    domains: dict[Cell, set[int]] = {}
    for d, i in variables:
        domains[(d, i)] = {fixed[i]} if d == r else set(range(d))

    def revise(dom: dict[Cell, set[int]], x: Cell, y: Cell) -> bool:
        dx, _ = x
        dy, _ = y
        keep = {
            a
            for a in dom[x]
            if any(cells_overlap(dx, a, dy, b) for b in dom[y])
        }
        if keep == dom[x]:
            return False
        dom[x] = keep
        return True

    def ac3(dom: dict[Cell, set[int]], initial: Iterable[tuple[Cell, Cell]] | None = None) -> bool:
        queue = deque(
            initial
            if initial is not None
            else ((x, y) for x in variables for y in neighbors[x])
        )
        while queue:
            x, y = queue.popleft()
            if revise(dom, x, y):
                if not dom[x]:
                    return False
                for z in neighbors[x]:
                    if z != y:
                        queue.append((z, x))
        return True

    if not ac3(domains):
        return False

    def search(dom: dict[Cell, set[int]]) -> bool:
        undecided = [v for v in variables if len(dom[v]) > 1]
        if not undecided:
            return True
        variable = min(undecided, key=lambda v: len(dom[v]))
        for value in sorted(dom[variable]):
            nxt = {v: set(vals) for v, vals in dom.items()}
            nxt[variable] = {value}
            arcs = [(z, variable) for z in neighbors[variable]] + [
                (variable, z) for z in neighbors[variable]
            ]
            if ac3(nxt, arcs) and search(nxt):
                return True
        return False

    return search(domains)


def finite_prefix_image(r: int, max_scale: int) -> list[ResidueMap]:
    """All path-pruned scale-r maps surviving the exact finite prefix CSP."""
    return [f for f in path_maps(r) if finite_prefix_extendable(f, r, max_scale)]


def prime_power_internal_count(p: int, exponent: int) -> int:
    """Size of the internal-coherence monoid at r=p^exponent.

    Along the prime-power divisor chain this is an iterated full-transformation
    wreath product.  If E_a=log_p M_a, then E_a=p+p^2+...+p^a.
    """
    if p < 2 or exponent < 1:
        raise ValueError("require p>=2 and exponent>=1")
    power_sum = sum(p**j for j in range(1, exponent + 1))
    return p**power_sum


def self_check() -> dict[str, int]:
    overlap_cases = 0
    prime_freedom_cases = 0
    prefix_cases = 0

    for d in range(1, 15):
        for e in range(1, 15):
            g = gcd(d, e)
            assert overlap_edge_count(d, e) == d + e - g
            assert overlap_component_count(d, e) == g
            overlap_cases += 1

    primes = {2, 3, 5, 7}
    for r in range(2, 9):
        if r in primes:
            assert all(internally_coherent(f, r) for f in product(range(r), repeat=r))
        else:
            proper = next(d for d in range(2, r) if r % d == 0)
            block = r // proper
            witness = [0] * r
            witness[1] = block
            assert not internally_coherent(witness, r)
        prime_freedom_cases += 1

    expected_prefix_counts = {2: 4, 3: 17, 4: 40, 5: 195, 6: 182}
    for r, expected in expected_prefix_counts.items():
        survivors = finite_prefix_image(r, r)
        assert len(survivors) == expected
        assert all(finite_prefix_extendable(f, r, r + 1) for f in survivors)
        prefix_cases += len(survivors)

    assert prime_power_internal_count(2, 1) == 4
    assert prime_power_internal_count(2, 2) == 64
    assert prime_power_internal_count(3, 1) == 27

    return {
        "overlap_cases": overlap_cases,
        "prime_freedom_cases": prime_freedom_cases,
        "prefix_survivor_cases": prefix_cases,
    }


if __name__ == "__main__":
    print(self_check())
