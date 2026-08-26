"""Reconstructed four-support graph tail for the P017 Legendre pressure test.

This module recovers the mathematical object referenced by historical P017 L025
without relying on the missing ``four_support.py`` artifact.  It uses only the
already-established multiplicative threshold complex and Alexander-dual
threshold from P017 Supplements 03--04.

For a four-prime support P with G=prod(P)>2k and T=2k, put

    U = floor((G-1)/T).

Because every support prime is at most k<T, U is strictly smaller than every
three-prime subproduct of G.  Hence the Alexander-dual threshold complex
K(G,U) is a graph.  If V is its number of active vertices and E its number of
edges, then the original large Mobius tail is exactly

    tau = 1 - V + E.

When the dual graph is nonempty this is beta_1 - reduced_beta_0.  If the dual
graph has no vertices, the empty-complex correction +1 is essential.

The identities are exact finite arithmetic and do not prove Legendre's
conjecture.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import primes_up_to


def _validated_support(k: int, support: list[int] | tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    values = tuple(sorted(support))
    if len(values) != 4 or len(set(values)) != 4:
        raise ValueError("support must contain exactly four distinct primes")
    allowed = set(primes_up_to(k))
    if any(isinstance(p, bool) or not isinstance(p, int) or p not in allowed for p in values):
        raise ValueError("support entries must be distinct primes at most k")

    support_product = prod(values)
    threshold = 2 * k
    if support_product <= threshold:
        raise ValueError("four-support product must exceed 2k")
    dual_threshold = (support_product - 1) // threshold
    if dual_threshold < 1:
        raise AssertionError("dual threshold must be positive when G>2k")
    return values, support_product, threshold, dual_threshold


def _component_count(vertices: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> int:
    if not vertices:
        return 0
    adjacency = {vertex: set() for vertex in vertices}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)

    seen: set[int] = set()
    components = 0
    for start in vertices:
        if start in seen:
            continue
        components += 1
        stack = [start]
        seen.add(start)
        while stack:
            current = stack.pop()
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
    return components


def four_support_dual_graph(k: int, support: list[int] | tuple[int, ...]) -> dict[str, object]:
    """Return the exact Alexander-dual graph data for one four-prime support.

    The dual complex has a vertex p exactly when p<=U and an edge {p,q}
    exactly when pq<=U.  No three-prime face can occur.
    """
    values, support_product, threshold, dual_threshold = _validated_support(k, support)

    active_vertices = tuple(p for p in values if p <= dual_threshold)
    edges = tuple(
        (left, right)
        for left, right in combinations(active_vertices, 2)
        if left * right <= dual_threshold
    )

    # For every support prime p<=k<2k=T,
    # U < G/T < G/p.  Therefore every three-prime subproduct G/p exceeds U.
    triple_products = tuple(support_product // p for p in values)
    if any(triple <= dual_threshold for triple in triple_products):
        raise AssertionError("four-support dual complex unexpectedly contains a 2-simplex")

    components = _component_count(active_vertices, edges)
    vertex_count = len(active_vertices)
    edge_count = len(edges)
    positive_cycle_rank = edge_count - vertex_count + components if vertex_count else 0
    reduced_component_rank = components - 1 if vertex_count else 0
    empty_dual_correction = 1 if vertex_count == 0 else 0
    tail = positive_cycle_rank - reduced_component_rank + empty_dual_correction

    # Equivalent Euler form, valid uniformly including the empty dual graph.
    if tail != 1 - vertex_count + edge_count:
        raise AssertionError("graph-rank and Euler forms disagree")

    return {
        "k": k,
        "support": values,
        "support_product": support_product,
        "threshold": threshold,
        "dual_threshold": dual_threshold,
        "active_vertices": active_vertices,
        "edges": edges,
        "vertex_count": vertex_count,
        "edge_count": edge_count,
        "component_count": components,
        "positive_cycle_rank": positive_cycle_rank,
        "negative_rank": reduced_component_rank,
        "empty_dual_correction": empty_dual_correction,
        "tail": tail,
    }


def four_support_direct_mobius_tail(k: int, support: list[int] | tuple[int, ...]) -> int:
    """Compute the same large-region tail directly from the 16 divisors.

    This is deliberately independent of the graph formula and is used as a
    finite cross-check of the reconstructed L022 object.
    """
    values, _support_product, threshold, _dual_threshold = _validated_support(k, support)
    total = 0
    for depth in range(5):
        sign = -1 if depth % 2 else 1
        for face in combinations(values, depth):
            divisor = prod(face)
            if divisor > threshold:
                total += sign
    return total


def four_support_tail_certificate(k: int, support: list[int] | tuple[int, ...]) -> dict[str, object]:
    """Return graph data and verify it against the direct Mobius divisor tail."""
    graph = four_support_dual_graph(k, support)
    direct = four_support_direct_mobius_tail(k, support)
    if graph["tail"] != direct:
        raise AssertionError("reconstructed graph tail disagrees with direct Mobius tail")
    return {**graph, "direct_tail": direct}
