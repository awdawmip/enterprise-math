"""Cross-route R007 overlap-field geometry for prime/collapse research.

This module deliberately consumes the exact overlap and natural-hull machinery
from ``r007_residue_extension_csp``. It packages later R007 results:

1. a top-level naturality pressure kernel for repeated operation checks;
2. Euclidean quotient/remainder coding by coprime overlap-caterpillar leaves;
3. multiscale overlap nerves whose connectivity recovers the gcd meet object;
4. atomic interval metrics whose reduced denominators recover the lcm join;
5. first-disconnect and prime-power splitting interpretations for prime tooling.

All geometry is exact integer/rational arithmetic. The arithmetic identities are
not claimed as faster gcd, lcm, factorization, or primality algorithms.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd, lcm
from typing import Sequence

import r007_residue_extension_csp as base

ResidueMap = tuple[int, ...]
Cell = tuple[int, int]


def naturality_kernel(r: int) -> tuple[tuple[ResidueMap, ...], ...]:
    """Precompile K_ij(z), the maximal top pressure from j to i."""
    if r < 1:
        raise ValueError("r must be positive")
    table = [[[0 for _ in range(r)] for _ in range(r)] for _ in range(r)]
    for j in range(r):
        for z in range(r):
            seed = [0] * r
            seed[j] = z
            labels = base.lower_overlap_closure(seed, r)
            for i in range(r):
                table[i][j][z] = labels[(r, i)]
    return tuple(
        tuple(tuple(table[i][j]) for j in range(r))
        for i in range(r)
    )


def hull_from_kernel(
    fixed: Sequence[int], kernel: Sequence[Sequence[Sequence[int]]]
) -> ResidueMap:
    """Apply a precompiled pressure kernel to a scale-r operation."""
    r = len(fixed)
    if len(kernel) != r or any(len(row) != r for row in kernel):
        raise ValueError("kernel shape does not match the scale")
    return tuple(
        max(kernel[i][j][fixed[j]] for j in range(r))
        for i in range(r)
    )


def kernel_is_idempotent(kernel: Sequence[Sequence[Sequence[int]]]) -> bool:
    """Check K tensor K = K over pointwise max and unary-map composition."""
    r = len(kernel)
    for i in range(r):
        for j in range(r):
            for z in range(r):
                composed = max(
                    kernel[i][k][kernel[k][j][z]]
                    for k in range(r)
                )
                if composed != kernel[i][j][z]:
                    return False
    return True


def fine_side_leaf_multiplicities(d: int, e: int) -> tuple[int, ...]:
    """Fine-side leaf counts for coprime scales ``1 <= d < e``."""
    if not (1 <= d < e) or gcd(d, e) != 1:
        raise ValueError("require coprime scales 1<=d<e")
    counts: list[int] = []
    for i in range(d):
        leaf_count = 0
        for j in range(e):
            if not base.cells_overlap(d, i, e, j):
                continue
            degree = sum(base.cells_overlap(d, k, e, j) for k in range(d))
            if degree == 1:
                leaf_count += 1
        counts.append(leaf_count)
    return tuple(counts)


def lower_mechanical_word(d: int, s: int) -> tuple[int, ...]:
    """Rational lower mechanical word of slope ``s/d``."""
    if not (0 < s < d):
        raise ValueError("require 0<s<d")
    return tuple(((i + 1) * s) // d - (i * s) // d for i in range(d))


def uniform_leaf_pruning_signature(d: int, e: int) -> tuple[int, int, ResidueMap]:
    """Read the first Euclidean quotient/remainder from the overlap caterpillar.

    For ``e=q*d+s`` with coprime ``d<e``, removing ``q-1`` fine-side leaves
    from every d-cell leaves exactly the leaf multiplicities of ``B(d,d+s)``.
    The residual word is the lower mechanical word of slope ``s/d`` plus the
    forced leaf at the left endpoint.
    """
    if not (1 <= d < e) or gcd(d, e) != 1:
        raise ValueError("require coprime scales 1<=d<e")
    q, s = divmod(e, d)
    leaves = fine_side_leaf_multiplicities(d, e)
    residual = tuple(value - (q - 1) for value in leaves)
    expected = list(lower_mechanical_word(d, s))
    expected[0] += 1
    if residual != tuple(expected):
        raise AssertionError("Euclidean leaf-pruning identity failed")
    return q, s, residual


def mechanical_one_positions(d: int, s: int) -> tuple[int, ...]:
    """Positions ``ceil(k*d/s)-1`` of the lower mechanical word's ones."""
    return tuple(i for i, bit in enumerate(lower_mechanical_word(d, s)) if bit)


def euclidean_gap_recursion(d: int, s: int) -> tuple[int, int, tuple[int, ...]]:
    """Read the next Euclidean step from gaps between mechanical-word ones.

    With ``d=a*s+t`` and virtual one-position ``p_0=-1``, the gaps satisfy
    ``p_k-p_(k-1)=a+epsilon_k``. For ``t>0`` the binary epsilon sequence is
    the upper mechanical word of slope ``t/s``; ``t=0`` is the terminal case.
    """
    if not (0 < s < d) or gcd(d, s) != 1:
        raise ValueError("require coprime 0<s<d")
    a, t = divmod(d, s)
    positions = mechanical_one_positions(d, s)
    virtual = (-1,) + positions
    gaps = tuple(virtual[k] - virtual[k - 1] for k in range(1, len(virtual)))
    epsilon = tuple(gap - a for gap in gaps)
    if t == 0:
        if s != 1 or any(epsilon):
            raise AssertionError("terminal Euclidean gap code failed")
    else:
        expected = tuple(
            (k * t + s - 1) // s - ((k - 1) * t + s - 1) // s
            for k in range(1, s + 1)
        )
        if epsilon != expected:
            raise AssertionError("mechanical Euclidean recursion failed")
    return a, t, epsilon


def _normalize_scales(scales: Sequence[int]) -> tuple[int, ...]:
    levels = tuple(dict.fromkeys(scales))
    if not levels or any(d < 1 for d in levels):
        raise ValueError("require nonempty positive scales")
    return levels


def gcd_many(scales: Sequence[int]) -> int:
    """Greatest common divisor of a nonempty scale family."""
    levels = _normalize_scales(scales)
    value = levels[0]
    for d in levels[1:]:
        value = gcd(value, d)
    return value


def lcm_many(scales: Sequence[int]) -> int:
    """Least common multiple of a nonempty scale family."""
    levels = _normalize_scales(scales)
    value = 1
    for d in levels:
        value = lcm(value, d)
    return value


def multiscale_overlap_components(scales: Sequence[int]) -> list[set[Cell]]:
    """Connected components of the 1-skeleton of the multiscale overlap nerve."""
    levels = _normalize_scales(scales)
    vertices = [(d, i) for d in levels for i in range(d)]
    adj: dict[Cell, list[Cell]] = {v: [] for v in vertices}
    for x, y in combinations(vertices, 2):
        d, i = x
        e, j = y
        if d != e and base.cells_overlap(d, i, e, j):
            adj[x].append(y)
            adj[y].append(x)
    seen: set[Cell] = set()
    components: list[set[Cell]] = []
    for start in vertices:
        if start in seen:
            continue
        component = {start}
        seen.add(start)
        stack = [start]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    component.add(y)
                    stack.append(y)
        components.append(component)
    return components


def multiscale_overlap_component_count(scales: Sequence[int]) -> int:
    """Number of connected components; exactly ``gcd(scales)``."""
    return len(multiscale_overlap_components(scales))


def meet_component_label(d: int, i: int, meet_scale: int) -> int:
    """Canonical R_d -> R_g label when ``g=meet_scale`` divides ``d``."""
    if meet_scale < 1 or d % meet_scale or not (0 <= i < d):
        raise ValueError("invalid meet projection")
    return i // (d // meet_scale)


def multiscale_meet_projection(scales: Sequence[int]) -> dict[Cell, int]:
    """Component quotient identified with the canonical gcd-scale object R_g."""
    levels = _normalize_scales(scales)
    g = gcd_many(levels)
    return {
        (d, i): meet_component_label(d, i, g)
        for d in levels
        for i in range(d)
    }


def common_refinement_atom_count(scales: Sequence[int]) -> int:
    """Atom count of overlaid grids by inclusion-exclusion of subset gcds."""
    levels = _normalize_scales(scales)
    total = 0
    n = len(levels)
    for mask in range(1, 1 << n):
        subset = [levels[i] for i in range(n) if mask & (1 << i)]
        term = gcd_many(subset)
        total += term if len(subset) % 2 else -term
    return total


def multiscale_simplex_counts(scales: Sequence[int]) -> tuple[int, ...]:
    """f-vector of the colored interval-overlap nerve."""
    levels = _normalize_scales(scales)
    counts = [0] * len(levels)
    n = len(levels)
    for mask in range(1, 1 << n):
        subset = [levels[i] for i in range(n) if mask & (1 << i)]
        counts[len(subset) - 1] += common_refinement_atom_count(subset)
    return tuple(counts)


def multiscale_nerve_euler_characteristic(scales: Sequence[int]) -> int:
    """Euler characteristic of the full multiscale overlap nerve."""
    return sum(
        count if dim % 2 == 0 else -count
        for dim, count in enumerate(multiscale_simplex_counts(scales))
    )


def overlaid_grid_boundaries(scales: Sequence[int]) -> tuple[Fraction, ...]:
    """Sorted union of all grid boundaries, constructed directly as rationals."""
    levels = _normalize_scales(scales)
    return tuple(
        sorted({Fraction(k, d) for d in levels for k in range(d + 1)})
    )


def atomic_interval_lengths(scales: Sequence[int]) -> tuple[Fraction, ...]:
    """Positive lengths of the atomic intervals cut out by all scale boundaries."""
    boundaries = overlaid_grid_boundaries(scales)
    return tuple(
        boundaries[i + 1] - boundaries[i]
        for i in range(len(boundaries) - 1)
    )


def metric_join_scale(scales: Sequence[int]) -> int:
    """Recover the lcm join from reduced denominators of atomic interval lengths.

    This function does not call ``lcm_many(scales)``. It constructs the rational
    geometry first, then takes the lcm of the reduced atom-length denominators.
    The theorem is that this equals the least uniform refinement scale resolving
    every input grid boundary.
    """
    value = 1
    for length in atomic_interval_lengths(scales):
        value = lcm(value, length.denominator)
    return value


def meet_join_signature(scales: Sequence[int]) -> tuple[int, int]:
    """Return ``(gcd meet, lcm join)`` extracted from overlap topology/metric."""
    return multiscale_overlap_component_count(scales), metric_join_scale(scales)


def first_disconnect_scale(n: int) -> int:
    """First d>=2 with disconnected B(n,d); exactly the smallest prime factor."""
    if n < 2:
        raise ValueError("n must be at least 2")
    for d in range(2, n + 1):
        if base.overlap_component_count(n, d) > 1:
            return d
    raise AssertionError("B(n,n) is always disconnected for n>=2")


def prime_by_lower_scale_connectivity(n: int) -> bool:
    """Topological trial-division characterization of primality."""
    if n < 2:
        return False
    return first_disconnect_scale(n) == n
