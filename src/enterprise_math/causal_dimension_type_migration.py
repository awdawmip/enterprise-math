"""Intrinsic dimension-type migration with separate split and healing spectra.

On retained primitive states, an old local-causal partition P_old and a new
intrinsic partition P_new need not refine one another.  Dimension extension may
both reveal distinctions and heal/merge distinctions when the present geometry
is re-evaluated without retaining lamination provenance.

Let P_common be the common refinement labelled by `(old_type,new_type)`.  Define
P011-style nonnegative spectra

    R_k = J_k(P_old) - J_k(P_common)   # distinctions revealed by the lift
    H_k = J_k(P_new) - J_k(P_common)   # old distinctions healed in the new view

Keeping R and H separate avoids signed cancellation.  If provenance/old
observation is declared persistent, only the R side is allowed; if only current
intrinsic geometry is observed, both mechanisms are legitimate.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import comb

from .causal_primitive_link_profile import (
    Vector,
    neighborhood_signature,
    primitive_direction_graph,
)


def _collision(sizes: tuple[int, ...], maximum_order: int) -> tuple[int, ...]:
    return tuple(
        sum(comb(size, order) for size in sizes if size >= order)
        for order in range(1, maximum_order + 1)
    )


@dataclass(frozen=True)
class TypeMigrationProfile:
    incidence: tuple[tuple[tuple[int, int], int], ...]
    old_type_sizes: tuple[int, ...]
    new_retained_type_sizes: tuple[int, ...]
    common_refinement_sizes: tuple[int, ...]
    revelation_spectrum: tuple[int, ...]
    healing_spectrum: tuple[int, ...]
    old_type_count: int
    new_retained_type_count: int
    common_type_count: int
    has_split: bool
    has_merge: bool


def intrinsic_type_migration(
    old_vectors: tuple[Vector, ...],
    new_vectors: tuple[Vector, ...],
    maximum_order: int = 4,
) -> TypeMigrationProfile:
    if not old_vectors or not new_vectors:
        raise ValueError("primitive vector families must be non-empty")
    if len(new_vectors[0]) != len(old_vectors[0]) + 1:
        raise ValueError("new primitive vectors must add exactly one coordinate")
    if isinstance(maximum_order, bool) or not isinstance(maximum_order, int) or maximum_order < 1:
        raise ValueError("maximum_order must be a positive integer")

    old_adj = primitive_direction_graph(old_vectors)
    new_adj = primitive_direction_graph(new_vectors)
    new_set = set(new_vectors)

    old_sig = {v: neighborhood_signature(old_adj, v) for v in old_vectors}
    new_sig = {}
    for old in old_vectors:
        lifted = old + (0,)
        if lifted not in new_set:
            raise ValueError("new primitive shell must retain old shell under x->(x,0)")
        new_sig[old] = neighborhood_signature(new_adj, lifted)

    old_ids: dict[object, int] = {}
    new_ids: dict[object, int] = {}
    incidence = Counter()
    old_sizes = Counter()
    new_sizes = Counter()
    for old in old_vectors:
        old_id = old_ids.setdefault(old_sig[old], len(old_ids))
        new_id = new_ids.setdefault(new_sig[old], len(new_ids))
        old_sizes[old_id] += 1
        new_sizes[new_id] += 1
        incidence[(old_id, new_id)] += 1

    common_sizes = tuple(incidence.values())
    old_size_tuple = tuple(old_sizes.values())
    new_size_tuple = tuple(new_sizes.values())
    j_old = _collision(old_size_tuple, maximum_order)
    j_new = _collision(new_size_tuple, maximum_order)
    j_common = _collision(common_sizes, maximum_order)
    revelation = tuple(a - c for a, c in zip(j_old, j_common))
    healing = tuple(b - c for b, c in zip(j_new, j_common))

    row_targets = Counter()
    col_sources = Counter()
    for (old_id, new_id), count in incidence.items():
        if count:
            row_targets[old_id] += 1
            col_sources[new_id] += 1

    return TypeMigrationProfile(
        incidence=tuple(sorted(incidence.items())),
        old_type_sizes=tuple(sorted(old_size_tuple, reverse=True)),
        new_retained_type_sizes=tuple(sorted(new_size_tuple, reverse=True)),
        common_refinement_sizes=tuple(sorted(common_sizes, reverse=True)),
        revelation_spectrum=revelation,
        healing_spectrum=healing,
        old_type_count=len(old_sizes),
        new_retained_type_count=len(new_sizes),
        common_type_count=len(common_sizes),
        has_split=any(value > 1 for value in row_targets.values()),
        has_merge=any(value > 1 for value in col_sources.values()),
    )
