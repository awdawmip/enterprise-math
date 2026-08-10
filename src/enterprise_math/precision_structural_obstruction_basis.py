"""Finite structural obstruction duality for typed future-language compilers.

This module does not implement hypergraph transversal algorithms as new mathematics.
It provides the R004 reduction from a monotone retained-generator adequacy oracle to
minimal deletion cuts, canonical obstruction witnesses, and minimal retained bases.
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Callable, FrozenSet, Hashable, Iterable, Sequence, Tuple, TypeVar

G = TypeVar("G", bound=Hashable)
W = TypeVar("W")


def powerset(items: Sequence[G]) -> Tuple[FrozenSet[G], ...]:
    xs = tuple(items)
    out = []
    for r in range(len(xs) + 1):
        out.extend(frozenset(c) for c in combinations(xs, r))
    return tuple(out)


def inclusion_minimal_sets(family: Iterable[FrozenSet[G]]) -> Tuple[FrozenSet[G], ...]:
    unique = set(family)
    mins = [s for s in unique if not any(t < s for t in unique)]
    return tuple(sorted(mins, key=lambda s: (len(s), tuple(sorted(map(repr, s))))))


def minimal_failure_cuts(
    generators: Sequence[G],
    adequate_retained: Callable[[FrozenSet[G]], bool],
) -> Tuple[FrozenSet[G], ...]:
    """Return inclusion-minimal deletion sets whose removal breaks adequacy."""
    universe = frozenset(generators)
    failures = []
    for deleted in powerset(tuple(generators)):
        retained = universe - deleted
        if not adequate_retained(retained):
            failures.append(deleted)
    return inclusion_minimal_sets(failures)


def minimal_transversals(
    generators: Sequence[G],
    cut_family: Iterable[FrozenSet[G]],
) -> Tuple[FrozenSet[G], ...]:
    """Return inclusion-minimal retained sets meeting every nonempty cut edge."""
    cuts = tuple(cut_family)
    if any(not edge for edge in cuts):
        return tuple()
    hits = []
    for retained in powerset(tuple(generators)):
        if all(retained & edge for edge in cuts):
            hits.append(retained)
    return inclusion_minimal_sets(hits)


def carrier_bases_from_cuts(
    generators: Sequence[G],
    carrier_cuts: Iterable[FrozenSet[G]],
) -> Tuple[FrozenSet[G], ...]:
    return minimal_transversals(generators, carrier_cuts)


def canonical_cut_witness(
    generators: Sequence[G],
    cut: FrozenSet[G],
    compile_retained: Callable[[FrozenSet[G]], W],
) -> W:
    """Compile after deleting exactly cut; for a minimal carrier cut this is P_H."""
    return compile_retained(frozenset(generators) - cut)


def kill_set(
    generators: Sequence[G],
    world: W,
    stable: Callable[[G, W], bool],
) -> FrozenSet[G]:
    return frozenset(g for g in generators if not stable(g, world))


def canonical_cut_kill_identity(
    generators: Sequence[G],
    cut: FrozenSet[G],
    compile_retained: Callable[[FrozenSet[G]], W],
    stable: Callable[[G, W], bool],
) -> bool:
    world = canonical_cut_witness(generators, cut, compile_retained)
    return kill_set(generators, world, stable) == cut


def joint_adequacy_cuts(
    generators: Sequence[G],
    carrier_ok: Callable[[FrozenSet[G]], bool],
    semantic_ok: Callable[[FrozenSet[G]], bool],
) -> Tuple[FrozenSet[G], ...]:
    """Minimal cuts for carrier AND semantic adequacy.

    The failure family is the union of the two upward-closed failure families, so
    the minimal joint cuts are the inclusion-minimal members of the union of the
    two minimal cut clutters.
    """
    carrier = minimal_failure_cuts(generators, carrier_ok)
    semantic = minimal_failure_cuts(generators, semantic_ok)
    return inclusion_minimal_sets((*carrier, *semantic))


def minimal_adequate_instruction_sets(
    generators: Sequence[G],
    carrier_ok: Callable[[FrozenSet[G]], bool],
    semantic_ok: Callable[[FrozenSet[G]], bool],
) -> Tuple[FrozenSet[G], ...]:
    cuts = joint_adequacy_cuts(generators, carrier_ok, semantic_ok)
    return minimal_transversals(generators, cuts)


def blocker_duality_holds(generators: Sequence[G], clutter: Iterable[FrozenSet[G]]) -> bool:
    """Finite verification of b(b(C))=C for an inclusion-minimal cut family."""
    c = inclusion_minimal_sets(clutter)
    b = minimal_transversals(generators, c)
    bb = minimal_transversals(generators, b)
    return set(bb) == set(c)


def sperner_cut_bound(generator_count: int) -> int:
    if generator_count < 0:
        raise ValueError("generator_count must be nonnegative")
    return comb(generator_count, generator_count // 2)
