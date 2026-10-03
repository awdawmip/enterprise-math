"""Exact positive-rational BRC holonomy and skeleton/thickness tools.

Foundation extraction of main-backed PRs #1132/#1133.  Positive rational
weights are represented by prime valuations before any logarithmic readout.
The integer factorization routine here is an exact reference implementation,
not a factoring-speedup claim.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

from .brc_weighted_recurrent import RationalInput

RationalEdge = tuple[int, int, RationalInput]


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    result = Fraction(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


def _factor_positive_integer(value: int) -> dict[int, int]:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("factorization input must be a positive integer")
    n = value
    factors: dict[int, int] = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    p = 3
    while p <= isqrt(n):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def rational_prime_valuations(value: RationalInput) -> tuple[tuple[int, int], ...]:
    """Return the finite-support prime valuation coordinates of ``q>0``."""
    q = _positive_fraction("value", value)
    valuations: dict[int, int] = {}
    for prime, exponent in _factor_positive_integer(q.numerator).items():
        valuations[prime] = valuations.get(prime, 0) + exponent
    for prime, exponent in _factor_positive_integer(q.denominator).items():
        valuations[prime] = valuations.get(prime, 0) - exponent
    return tuple(sorted((prime, exponent) for prime, exponent in valuations.items() if exponent))


def rational_from_prime_valuations(valuations: Mapping[int, int] | Sequence[tuple[int, int]]) -> Fraction:
    """Reconstruct a positive rational from finite prime valuation coordinates."""
    items = valuations.items() if isinstance(valuations, Mapping) else valuations
    numerator = 1
    denominator = 1
    seen: set[int] = set()
    for prime, exponent in items:
        if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
            raise ValueError("prime coordinates require integer primes >=2")
        if prime in seen:
            raise ValueError("duplicate prime coordinate")
        seen.add(prime)
        # Exact primality check is intentionally simple/reference-grade.
        if any(prime % d == 0 for d in range(2, isqrt(prime) + 1)):
            raise ValueError(f"{prime} is not prime")
        if isinstance(exponent, bool) or not isinstance(exponent, int):
            raise TypeError("valuation exponents must be integers")
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime ** (-exponent)
    return Fraction(numerator, denominator)


@dataclass(frozen=True)
class RationalPowerDecomposition:
    modulus: int
    value: Fraction
    skeleton: int
    thickness: Fraction
    skeleton_valuations: tuple[tuple[int, int], ...]

    def verify(self) -> bool:
        if self.modulus < 2 or self.value <= 0 or self.skeleton <= 0 or self.thickness <= 0:
            return False
        if self.value != self.skeleton * self.thickness**self.modulus:
            return False
        return all(0 <= exponent < self.modulus for _, exponent in self.skeleton_valuations)


def rational_power_skeleton_thickness(value: RationalInput, modulus: int) -> RationalPowerDecomposition:
    """Return unique ``q=s_m*t^m`` with positive m-power-free integer skeleton."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 2:
        raise ValueError("modulus must be an integer >=2")
    q = _positive_fraction("value", value)
    valuations = dict(rational_prime_valuations(q))
    skeleton = 1
    thickness_num = 1
    thickness_den = 1
    remainders: list[tuple[int, int]] = []
    for prime, exponent in sorted(valuations.items()):
        quotient, remainder = divmod(exponent, modulus)
        if remainder:
            skeleton *= prime**remainder
            remainders.append((prime, remainder))
        if quotient >= 0:
            thickness_num *= prime**quotient
        else:
            thickness_den *= prime ** (-quotient)
    decomposition = RationalPowerDecomposition(
        modulus=modulus,
        value=q,
        skeleton=skeleton,
        thickness=Fraction(thickness_num, thickness_den),
        skeleton_valuations=tuple(remainders),
    )
    if not decomposition.verify():
        raise AssertionError("rational power skeleton/thickness reconstruction failed")
    return decomposition


def rational_squarefree_skeleton_thickness(value: RationalInput) -> RationalPowerDecomposition:
    """Convenience ``m=2`` decomposition: squarefree parity skeleton + thickness."""
    return rational_power_skeleton_thickness(value, 2)


@dataclass(frozen=True)
class RationalTreeGaugeNormalForm:
    vertex_count: int
    root: int
    tree_edge_indices: tuple[int, ...]
    non_tree_edge_indices: tuple[int, ...]
    vertex_potentials: tuple[Fraction, ...]
    normalized_edge_weights: tuple[Fraction, ...]

    def fundamental_holonomies(self) -> tuple[tuple[int, Fraction], ...]:
        return tuple((index, self.normalized_edge_weights[index]) for index in self.non_tree_edge_indices)

    def prime_coordinates(self) -> tuple[tuple[int, tuple[tuple[int, int], ...]], ...]:
        return tuple(
            (index, rational_prime_valuations(self.normalized_edge_weights[index]))
            for index in self.non_tree_edge_indices
        )


def rational_tree_gauge_normal_form(
    vertex_count: int,
    edges: Sequence[RationalEdge],
    root: int,
    tree_edge_indices: Sequence[int],
) -> RationalTreeGaugeNormalForm:
    """Fix root scale 1 and gauge every declared spanning-tree edge to weight 1.

    Edge gauge convention: ``q'_(s->t)=q*h_t/h_s``.
    The tree is treated as an underlying undirected spanning tree; edge
    orientations are preserved only in the rational transport equations.
    """
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count < 1:
        raise ValueError("vertex_count must be a positive integer")
    if isinstance(root, bool) or not isinstance(root, int) or not 0 <= root < vertex_count:
        raise ValueError("root out of range")
    normalized_edges: list[tuple[int, int, Fraction]] = []
    for source, target, raw_weight in edges:
        if isinstance(source, bool) or isinstance(target, bool):
            raise TypeError("edge endpoints must be integer indices")
        if not (isinstance(source, int) and isinstance(target, int) and 0 <= source < vertex_count and 0 <= target < vertex_count):
            raise ValueError("edge endpoint out of range")
        normalized_edges.append((source, target, _positive_fraction("edge weight", raw_weight)))

    tree = tuple(tree_edge_indices)
    if len(tree) != vertex_count - 1 or len(set(tree)) != len(tree):
        raise ValueError("tree_edge_indices must contain exactly vertex_count-1 distinct edges")
    if any(isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(normalized_edges) for index in tree):
        raise ValueError("tree edge index out of range")

    adjacency: list[list[tuple[int, int, bool]]] = [[] for _ in range(vertex_count)]
    for index in tree:
        source, target, _ = normalized_edges[index]
        if source == target:
            raise ValueError("a spanning tree cannot contain a self-loop")
        adjacency[source].append((target, index, True))
        adjacency[target].append((source, index, False))

    potentials: list[Fraction | None] = [None] * vertex_count
    potentials[root] = Fraction(1, 1)
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        assert potentials[vertex] is not None
        for neighbor, edge_index, forward in adjacency[vertex]:
            source, target, weight = normalized_edges[edge_index]
            if forward:
                assert vertex == source and neighbor == target
                candidate = potentials[vertex] / weight
            else:
                assert vertex == target and neighbor == source
                candidate = potentials[vertex] * weight
            if potentials[neighbor] is None:
                potentials[neighbor] = candidate
                queue.append(neighbor)
            elif potentials[neighbor] != candidate:
                raise ValueError("tree edges are not an underlying spanning tree")
    if any(value is None for value in potentials):
        raise ValueError("tree edges do not connect every vertex")
    final_potentials = tuple(value for value in potentials if value is not None)

    normalized_weights = tuple(
        weight * final_potentials[target] / final_potentials[source]
        for source, target, weight in normalized_edges
    )
    if any(normalized_weights[index] != 1 for index in tree):
        raise AssertionError("tree gauge normalization failed")
    tree_set = set(tree)
    non_tree = tuple(index for index in range(len(normalized_edges)) if index not in tree_set)
    return RationalTreeGaugeNormalForm(
        vertex_count=vertex_count,
        root=root,
        tree_edge_indices=tree,
        non_tree_edge_indices=non_tree,
        vertex_potentials=final_potentials,
        normalized_edge_weights=normalized_weights,
    )
