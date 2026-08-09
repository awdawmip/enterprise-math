"""Coarsest bounded deletion signature for Boolean conflict repair.

Let a finite labeled conflict graph encode pairwise incompatibility.  The future
language may delete at most ``h`` labels, then observes only whether every
conflict edge has lost an endpoint.  Equivalently, it asks whether the deletion
set is a vertex cover.

The Boolean future function is upward closed under inclusion of deleted labels,
so it is determined uniquely by its inclusion-minimal successful deletion sets.
For a graph these are exactly the inclusion-minimal vertex covers of size at
most ``h``.

Therefore the canonical bounded future signature is the antichain of minimal
covers within the horizon.  Different conflict graphs with the same such
antichain are indistinguishable for this declared future language.  In
particular:

* empty graph -> signature contains the empty cover and every future succeeds;
* vertex-cover number > h -> signature is empty and every allowed future fails.

This is a finite monotone-Boolean/antichain specialization of the project's
future-signature viewpoint.  Minimal vertex covers and antichain normal forms
are established combinatorics, not a novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

ConflictEdge = tuple[int, int]


@dataclass(frozen=True)
class ConflictFutureSignature:
    labels: tuple[int, ...]
    deletion_horizon: int
    minimal_successful_deletions: tuple[frozenset[int], ...]


def _validate_graph(
    labels: tuple[int, ...] | list[int],
    conflict_edges: tuple[ConflictEdge, ...] | list[ConflictEdge],
    deletion_horizon: int,
) -> tuple[tuple[int, ...], tuple[ConflictEdge, ...]]:
    label_tuple = tuple(sorted(labels))
    if not label_tuple:
        raise ValueError("at least one label is required")
    if len(label_tuple) != len(set(label_tuple)):
        raise ValueError("labels must be unique")
    if any(isinstance(label, bool) or not isinstance(label, int) for label in label_tuple):
        raise ValueError("labels must be integers")
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
        or deletion_horizon >= len(label_tuple)
    ):
        raise ValueError("deletion_horizon must lie in 0..len(labels)-1")

    label_set = set(label_tuple)
    normalized: set[ConflictEdge] = set()
    for left, right in conflict_edges:
        if left == right:
            raise ValueError("conflict edges must connect distinct labels")
        if left not in label_set or right not in label_set:
            raise ValueError("conflict edge endpoint not in labels")
        normalized.add(tuple(sorted((left, right))))
    return label_tuple, tuple(sorted(normalized))


def is_vertex_cover(
    conflict_edges: tuple[ConflictEdge, ...] | list[ConflictEdge],
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> bool:
    removed = frozenset(removed_labels)
    return all(left in removed or right in removed for left, right in conflict_edges)


def compile_conflict_future_signature(
    labels: tuple[int, ...] | list[int],
    conflict_edges: tuple[ConflictEdge, ...] | list[ConflictEdge],
    deletion_horizon: int,
) -> ConflictFutureSignature:
    """Return all inclusion-minimal successful deletion sets inside the horizon."""
    label_tuple, edges = _validate_graph(labels, conflict_edges, deletion_horizon)
    minimal: list[frozenset[int]] = []
    for count in range(deletion_horizon + 1):
        for candidate in combinations(label_tuple, count):
            removed = frozenset(candidate)
            if not is_vertex_cover(edges, removed):
                continue
            if any(existing.issubset(removed) for existing in minimal):
                continue
            minimal.append(removed)
    return ConflictFutureSignature(
        labels=label_tuple,
        deletion_horizon=deletion_horizon,
        minimal_successful_deletions=tuple(
            sorted(minimal, key=lambda item: (len(item), tuple(sorted(item))))
        ),
    )


def conflict_future_succeeds(
    signature: ConflictFutureSignature,
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> bool:
    """Evaluate bounded repair success from the antichain signature alone."""
    removed = frozenset(removed_labels)
    if not removed.issubset(signature.labels):
        raise ValueError("removed labels must belong to the signature")
    if len(removed) > signature.deletion_horizon:
        raise ValueError("removal set exceeds deletion horizon")
    return any(
        minimum.issubset(removed)
        for minimum in signature.minimal_successful_deletions
    )
