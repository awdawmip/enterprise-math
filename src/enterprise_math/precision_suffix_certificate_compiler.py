"""Backward suffix compiler for staged deterministic certificate states.

This is a finite specialization of the P023 future-safe quotient principle applied to
certificate state itself.  It computes the coarsest exact certificate partition needed
at every program point and produces exact erasure-failure witnesses.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable, Iterable, Mapping, Sequence, Tuple

Partition = Tuple[Tuple[int, ...], ...]


def _canon(blocks: Iterable[Iterable[int]]) -> Partition:
    return tuple(sorted((tuple(sorted(block)) for block in blocks if tuple(block)), key=lambda b: b[0]))


def partition_from_labels(labels: Sequence[Hashable]) -> Partition:
    groups = defaultdict(list)
    for i, label in enumerate(labels):
        groups[label].append(i)
    return _canon(groups.values())


def class_map(partition: Partition) -> dict[int, int]:
    out = {}
    for i, block in enumerate(partition):
        for x in block:
            out[x] = i
    return out


def suffix_partitions(functions: Sequence[Sequence[int]], observations: Sequence[Sequence[Hashable]]) -> Tuple[Partition, ...]:
    """Return the coarsest suffix-safe certificate partition at every program point.

    `functions[i][x]` is the deterministic next certificate state from point i to i+1.
    `observations[i][x]` is the typed observation required at point i.
    """
    if len(observations) != len(functions) + 1:
        raise ValueError("need one observation surface at every point")
    n = len(observations[0])
    if any(len(obs) != n for obs in observations):
        raise ValueError("all certificate carriers must have the same finite size in this reference")
    if any(len(f) != n or any(y < 0 or y >= n for y in f) for f in functions):
        raise ValueError("invalid deterministic stage map")

    parts = [None] * len(observations)
    parts[-1] = partition_from_labels(observations[-1])
    for i in range(len(functions) - 1, -1, -1):
        qnext = class_map(parts[i + 1])
        labels = [(observations[i][x], qnext[functions[i][x]]) for x in range(n)]
        parts[i] = partition_from_labels(labels)
    return tuple(parts)


def erasure_safe(erasure: Partition, suffix_safe: Partition) -> bool:
    """True iff every erasure class lies inside one suffix-safe class."""
    qe = class_map(erasure)
    qs = class_map(suffix_safe)
    states = sorted(qe)
    return all(qe[x] != qe[y] or qs[x] == qs[y] for x in states for y in states)


def erasure_failure_witness(erasure: Partition, suffix_safe: Partition):
    qe = class_map(erasure)
    qs = class_map(suffix_safe)
    states = sorted(qe)
    for x in states:
        for y in states:
            if qe[x] == qe[y] and qs[x] != qs[y]:
                return x, y
    return None
