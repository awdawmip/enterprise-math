"""Finite exact explorer for the R007 divisibility-residue naturality tower.

The global residue-naturality problem can be encoded without floating point as
cell-overlap preservation among finite rational partitions.  The key fourth-
stage result is stronger than the earlier compactness bound: compatibility on
scales ``1..r`` is already sufficient for a scale-``r`` residue map to extend
to all larger scales.  The finite prefix CSP is moreover min/max closed, so
arc consistency is complete and no backtracking is needed.
"""

from __future__ import annotations

from collections import deque
from itertools import product
from math import gcd
from typing import Iterator, Mapping, Sequence

ResidueMap = tuple[int, ...]
Cell = tuple[int, int]  # (scale, cell index)
Family = dict[int, ResidueMap]


def cells_overlap(d: int, i: int, e: int, j: int) -> bool:
    """Whether the d-cell i and e-cell j overlap in positive length."""
    if d < 1 or e < 1 or not (0 <= i < d) or not (0 <= j < e):
        raise ValueError("invalid scale/cell")
    return i * e < (j + 1) * d and j * d < (i + 1) * e


def overlap_neighbors(d: int, i: int, e: int) -> tuple[int, ...]:
    """All e-cells overlapping one d-cell; they form an integer interval."""
    return tuple(j for j in range(e) if cells_overlap(d, i, e, j))


def overlap_edge_count(d: int, e: int) -> int:
    return sum(cells_overlap(d, i, e, j) for i in range(d) for j in range(e))


def _overlap_graph(d: int, e: int) -> dict[tuple[int, int], list[tuple[int, int]]]:
    vertices = [(0, i) for i in range(d)] + [(1, j) for j in range(e)]
    adj = {v: [] for v in vertices}
    for i in range(d):
        for j in range(e):
            if cells_overlap(d, i, e, j):
                adj[(0, i)].append((1, j))
                adj[(1, j)].append((0, i))
    return adj


def overlap_components(d: int, e: int) -> list[set[tuple[int, int]]]:
    """Connected components of the bipartite cell-overlap graph B(d,e)."""
    adj = _overlap_graph(d, e)
    seen: set[tuple[int, int]] = set()
    components: list[set[tuple[int, int]]] = []
    for start in adj:
        if start in seen:
            continue
        component = {start}
        stack = [start]
        seen.add(start)
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    component.add(w)
                    stack.append(w)
        components.append(component)
    return components


def overlap_component_count(d: int, e: int) -> int:
    return len(overlap_components(d, e))


def overlap_component_profiles(d: int, e: int) -> list[tuple[int, int, int]]:
    """Per-component counts ``(#d-cells,#e-cells,#edges)``."""
    adj = _overlap_graph(d, e)
    profiles: list[tuple[int, int, int]] = []
    for component in overlap_components(d, e):
        left = sum(side == 0 for side, _ in component)
        right = sum(side == 1 for side, _ in component)
        edges = sum(len(adj[v]) for v in component) // 2
        profiles.append((left, right, edges))
    return sorted(profiles)


def coprime_overlap_is_caterpillar(d: int, e: int) -> bool:
    """Check the stronger coprime geometry: B(d,e) is a caterpillar tree."""
    if gcd(d, e) != 1:
        raise ValueError("caterpillar statement is for coprime scales")
    adj = _overlap_graph(d, e)
    vertices = set(adj)
    edges = sum(len(vs) for vs in adj.values()) // 2
    if edges != len(vertices) - 1 or overlap_component_count(d, e) != 1:
        return False
    core = {v for v in vertices if len(adj[v]) > 1}
    if len(core) <= 2:
        return True
    core_degrees = {v: sum(w in core for w in adj[v]) for v in core}
    if any(deg not in (1, 2) for deg in core_degrees.values()):
        return False
    return sum(deg == 1 for deg in core_degrees.values()) == 2


def p_adic_valuation(n: int, p: int) -> int:
    if n < 1 or p < 2:
        raise ValueError("require n>=1 and p>=2")
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def prime_power_component_signature(n: int, p: int, k: int) -> int:
    """Component count against scale p^k: p^min(v_p(n),k) for prime p."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    return overlap_component_count(n, p**k)


def pair_compatible(f: Sequence[int], d: int, g: Sequence[int], e: int) -> bool:
    """Colored overlap-graph endomorphism criterion for two residue scales."""
    if len(f) != d or len(g) != e:
        raise ValueError("map length must equal its scale")
    for i in range(d):
        for j in range(e):
            if cells_overlap(d, i, e, j) and not cells_overlap(d, f[i], e, g[j]):
                return False
    return True


def family_compatible(family: Mapping[int, Sequence[int]]) -> bool:
    """Pairwise overlap preservation for every scale pair in a finite family."""
    levels = sorted(family)
    if any(len(family[d]) != d for d in levels):
        raise ValueError("map length must equal its scale")
    for pos, d in enumerate(levels):
        for e in levels[pos + 1 :]:
            if not pair_compatible(family[d], d, family[e], e):
                return False
    return True


def common_bridge_exists(a: Cell, b: Cell, h: int) -> bool:
    """Whether some h-cell overlaps both source cells a and b."""
    if h < 1:
        raise ValueError("h must be positive")
    d, i = a
    e, j = b
    return any(
        cells_overlap(d, i, h, k) and cells_overlap(e, j, h, k)
        for k in range(h)
    )


def bridge_dominance_holds(n: int) -> bool:
    """Exhaustively verify the R007 Farey bridge-descent lemma at level n.

    For old cells A,B,A',B' of levels < n, if an n-cell can bridge A,B but no
    n-cell can bridge A',B', then some older h<n already distinguishes them.
    The mathematical proof uses Farey neighbors and their mediant; this helper
    is only a finite regression oracle for small n.
    """
    if n < 2:
        raise ValueError("n must be at least 2")
    old = [(d, i) for d in range(1, n) for i in range(d)]
    source_pairs = [
        (a, b) for a in old for b in old if common_bridge_exists(a, b, n)
    ]
    target_pairs = [
        (a, b) for a in old for b in old if not common_bridge_exists(a, b, n)
    ]
    for a, b in source_pairs:
        for ap, bp in target_pairs:
            if not any(
                common_bridge_exists(a, b, h)
                and not common_bridge_exists(ap, bp, h)
                for h in range(1, n)
            ):
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
    return all(
        preserves_divisor_partition(f, r, d)
        for d in range(1, r + 1)
        if r % d == 0
    )


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


def overlap_relation_minmax_closed(d: int, e: int) -> bool:
    """Whether O_(d,e) is closed under coordinatewise min and max."""
    relation = [
        (a, b)
        for a in range(d)
        for b in range(e)
        if cells_overlap(d, a, e, b)
    ]
    relation_set = set(relation)
    for a in relation:
        for b in relation:
            if (min(a[0], b[0]), min(a[1], b[1])) not in relation_set:
                return False
            if (max(a[0], b[0]), max(a[1], b[1])) not in relation_set:
                return False
    return True


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


def _ac3_domains(
    fixed: Sequence[int], r: int, max_scale: int
) -> tuple[list[Cell], dict[Cell, list[Cell]], dict[Cell, set[int]]] | None:
    """Run arc consistency on the finite overlap CSP."""
    if len(fixed) != r or max_scale < 1:
        raise ValueError("invalid fixed map / max_scale")
    scales = sorted(set(range(1, max_scale + 1)) | {r})
    variables, neighbors = _constraint_graph(scales)
    domains: dict[Cell, set[int]] = {
        (d, i): ({fixed[i]} if d == r else set(range(d)))
        for d, i in variables
    }

    def revise(x: Cell, y: Cell) -> bool:
        dx, _ = x
        dy, _ = y
        keep = {
            a
            for a in domains[x]
            if any(cells_overlap(dx, a, dy, b) for b in domains[y])
        }
        if keep == domains[x]:
            return False
        domains[x] = keep
        return True

    queue = deque((x, y) for x in variables for y in neighbors[x])
    while queue:
        x, y = queue.popleft()
        if revise(x, y):
            if not domains[x]:
                return None
            for z in neighbors[x]:
                if z != y:
                    queue.append((z, x))
    return variables, neighbors, domains


def finite_prefix_assignment(
    fixed: Sequence[int], r: int, max_scale: int
) -> dict[Cell, int] | None:
    """Exact finite-prefix solution by AC-3 followed by coordinatewise minima.

    No search/backtracking is required. Each binary overlap relation is closed
    under coordinatewise minimum. After arc consistency, for an edge x--y the
    minimum of D_x has some support y1 and the minimum of D_y has some support
    x1; min-closure makes (min D_x,min D_y) a supported pair. Thus the
    simultaneous domain minima satisfy every edge constraint.
    """
    state = _ac3_domains(fixed, r, max_scale)
    if state is None:
        return None
    variables, neighbors, domains = state
    assignment = {v: min(domains[v]) for v in variables}
    for x in variables:
        dx, _ = x
        for y in neighbors[x]:
            dy, _ = y
            if not cells_overlap(dx, assignment[x], dy, assignment[y]):
                raise AssertionError("min-closed AC completeness invariant failed")
    return assignment


def finite_prefix_completion(
    fixed: Sequence[int], r: int, max_scale: int
) -> Family | None:
    """Return the least AC-derived compatible family on the requested prefix."""
    assignment = finite_prefix_assignment(fixed, r, max_scale)
    if assignment is None:
        return None
    scales = sorted(set(range(1, max_scale + 1)) | {r})
    family = {
        d: tuple(assignment[(d, i)] for i in range(d))
        for d in scales
    }
    if not family_compatible(family):
        raise AssertionError("finite prefix completion is not compatible")
    return family


def finite_prefix_extendable(fixed: Sequence[int], r: int, max_scale: int) -> bool:
    """Exact CSP decision for extension over scales 1..max_scale (plus r)."""
    return finite_prefix_assignment(fixed, r, max_scale) is not None


def extend_family_one_step(family: Mapping[int, Sequence[int]], n: int) -> ResidueMap:
    """Construct the least scale-n extension of a compatible 1..n-1 family.

    R007's Farey bridge-descent theorem proves that the allowed target n-cell
    intervals for each source n-cell have nonempty total intersection. This
    executable constructor chooses the minimum allowed target independently for
    each new source cell.
    """
    if sorted(family) != list(range(1, n)):
        raise ValueError("family must contain exactly scales 1..n-1")
    if not family_compatible(family):
        raise ValueError("family is not compatible")

    image: list[int] = []
    for i in range(n):
        allowed = set(range(n))
        for d, f in family.items():
            for j in range(d):
                if cells_overlap(n, i, d, j):
                    allowed.intersection_update(overlap_neighbors(d, f[j], n))
        if not allowed:
            raise AssertionError("Farey one-step extension theorem violated")
        image.append(min(allowed))

    result = tuple(image)
    for d, f in family.items():
        if not pair_compatible(result, n, f, d):
            raise AssertionError("constructed extension failed compatibility")
    return result


def extend_family_through(family: Mapping[int, Sequence[int]], max_scale: int) -> Family:
    """Iterate the one-step theorem through a finite target scale."""
    out: Family = {d: tuple(f) for d, f in family.items()}
    if not out:
        raise ValueError("family must be nonempty")
    expected = list(range(1, max(out) + 1))
    if sorted(out) != expected:
        raise ValueError("initial family must be a consecutive prefix")
    for n in range(max(out) + 1, max_scale + 1):
        out[n] = extend_family_one_step(out, n)
    return out


def globally_extendable(fixed: Sequence[int], r: int) -> bool:
    """Exact global decision: the universal obstruction cutoff is N_r=r."""
    return finite_prefix_extendable(fixed, r, r)


def finite_prefix_image(r: int, max_scale: int) -> list[ResidueMap]:
    """All path-pruned scale-r maps surviving the exact finite prefix CSP."""
    return [f for f in path_maps(r) if finite_prefix_extendable(f, r, max_scale)]


def prime_power_internal_count(p: int, exponent: int) -> int:
    """Size of the internal-coherence monoid at r=p^exponent."""
    if p < 2 or exponent < 1:
        raise ValueError("require p>=2 and exponent>=1")
    power_sum = sum(p**j for j in range(1, exponent + 1))
    return p**power_sum


def self_check() -> dict[str, int]:
    overlap_cases = 0
    lattice_cases = 0
    bridge_levels = 0
    prime_freedom_cases = 0
    prefix_cases = 0
    constructive_extensions = 0

    for d in range(1, 15):
        for e in range(1, 15):
            g = gcd(d, e)
            assert overlap_edge_count(d, e) == d + e - g
            assert overlap_component_count(d, e) == g
            expected_profile = (d // g, e // g, d // g + e // g - 1)
            assert overlap_component_profiles(d, e) == [expected_profile] * g
            if g == 1:
                assert coprime_overlap_is_caterpillar(d, e)
            overlap_cases += 1

    for d in range(1, 9):
        for e in range(1, 9):
            assert overlap_relation_minmax_closed(d, e)
            lattice_cases += 1

    for n in range(2, 8):
        assert bridge_dominance_holds(n)
        bridge_levels += 1

    primes = {2, 3, 5, 7}
    for r in range(2, 9):
        if r in primes:
            assert all(
                internally_coherent(f, r)
                for f in product(range(r), repeat=r)
            )
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
        assert all(globally_extendable(f, r) for f in survivors)
        prefix_cases += len(survivors)
        for f in survivors:
            family = finite_prefix_completion(f, r, r)
            assert family is not None
            extended = extend_family_through(family, r + 2)
            assert family_compatible(extended)
            constructive_extensions += 1

    for n in range(2, 40):
        for p in (2, 3, 5, 7):
            for k in range(0, 5):
                assert prime_power_component_signature(n, p, k) == p ** min(
                    p_adic_valuation(n, p), k
                )

    assert prime_power_internal_count(2, 1) == 4
    assert prime_power_internal_count(2, 2) == 64
    assert prime_power_internal_count(3, 1) == 27

    return {
        "overlap_cases": overlap_cases,
        "overlap_lattice_cases": lattice_cases,
        "bridge_levels": bridge_levels,
        "prime_freedom_cases": prime_freedom_cases,
        "prefix_survivor_cases": prefix_cases,
        "constructive_extensions": constructive_extensions,
    }


if __name__ == "__main__":
    print(self_check())
