"""Minimum-union formulation of quotient-word primitive storage.

For every nontrivial semantic target ``b``, choose one multiplicative witness
partition ``F_b`` of length at most the execution horizon.  The union of the
primitive types appearing in those witnesses is itself a separating normalized
alphabet.  Conversely, every separating normalized alphabet contains at least
one such witness for every target.

Therefore exact minimum storage is

    min |union_b F_b|,  with F_b in Pi_h(b).

This module implements that equivalent search coordinate independently from
the generator-subset enumeration in ``p018_p023_quotient_word_storage``.
The two exponential oracles are intended to cross-check one another.
"""

from __future__ import annotations

from .p018_p023_quotient_word_storage import (
    forced_prime_storage_core,
    minimum_storage_alphabets,
    storage_partition_constraints,
)


def _minimal_witness_type_sets(
    partitions: tuple[tuple[int, ...], ...],
) -> tuple[frozenset[int], ...]:
    """Collapse partitions to undominated primitive-type sets.

    Multiplicity remains encoded by the fact that each returned set came from
    an actually valid multiplicative partition.  If one valid witness type-set
    strictly contains another for the same target, the larger set can never
    improve a minimum-union objective and is discarded.
    """
    edges = {frozenset(partition) for partition in partitions}
    minimal = {
        edge
        for edge in edges
        if not any(other < edge for other in edges)
    }
    return tuple(
        sorted(minimal, key=lambda edge: (len(edge), tuple(sorted(edge))))
    )


def minimum_storage_alphabets_via_witness_union(
    max_state: int,
    root_exp: int,
    horizon: int,
) -> tuple[tuple[int, ...], ...]:
    """Return all minimum alphabets by selecting one witness edge per target.

    This is an exact branch-and-bound oracle over witness hyperedges.  It is
    algorithmically independent from enumerating subsets of all candidate
    generators.
    """
    raw_constraints = storage_partition_constraints(
        max_state, root_exp, horizon
    )
    constraints: list[tuple[int, tuple[frozenset[int], ...]]] = []
    for boundary, partitions in raw_constraints:
        edges = _minimal_witness_type_sets(partitions)
        if not edges:
            return ()
        constraints.append((boundary, edges))

    # Hard constraints first tends to expose lower bounds earlier.
    constraints.sort(
        key=lambda item: (
            len(item[1]),
            min((len(edge) for edge in item[1]), default=0),
            item[0],
        )
    )

    initial = frozenset(forced_prime_storage_core(max_state))
    best_size = float("inf")
    solutions: set[tuple[int, ...]] = set()

    def visit(index: int, chosen: frozenset[int]) -> None:
        nonlocal best_size
        if len(chosen) > best_size:
            return

        # Skip constraints already witnessed by the current dictionary.
        while index < len(constraints):
            _boundary, edges = constraints[index]
            if any(edge <= chosen for edge in edges):
                index += 1
            else:
                break

        if index == len(constraints):
            normalized = tuple(sorted(chosen))
            if len(chosen) < best_size:
                best_size = len(chosen)
                solutions.clear()
            if len(chosen) == best_size:
                solutions.add(normalized)
            return

        _boundary, edges = constraints[index]
        for edge in edges:
            visit(index + 1, chosen | edge)

    visit(0, initial)
    return tuple(sorted(solutions))


def minimum_storage_size_via_witness_union(
    max_state: int, root_exp: int, horizon: int
) -> int | None:
    """Exact minimum storage cardinality in the witness-union coordinates."""
    solutions = minimum_storage_alphabets_via_witness_union(
        max_state, root_exp, horizon
    )
    if not solutions:
        return None
    return len(solutions[0])


def witness_union_oracle_matches_subset_oracle(
    max_state: int, root_exp: int, horizon: int
) -> bool:
    """Cross-check the two exact storage optimization coordinates."""
    return set(
        minimum_storage_alphabets_via_witness_union(
            max_state, root_exp, horizon
        )
    ) == set(minimum_storage_alphabets(max_state, root_exp, horizon))
