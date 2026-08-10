"""Exact finite periodic certificates for rational stationary local-window laws.

This research module studies one narrow FQ-007 resource boundary: a fixed
finite local-window observation language can be reproduced forever by a finite
ex-ante deterministic latent system whenever its stationary block law is
rational.

A length-k block count table is interpreted as a directed multigraph on
length-(k-1) words.  Stationarity is exactly flow balance.  A balanced finite
directed multigraph decomposes into directed cycles.  Uniform random phase on
each resulting periodic cycle, mixed with exact rational cycle weights,
reconstructs the declared k-window law at every time.

All calculations are finite and integer/Fraction exact.  This is classical
circulation/Eulerian-cycle mathematics used as a project-local certificate; no
generic novelty is claimed and no physical ontology is inferred.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Hashable, Mapping, Sequence
from fractions import Fraction

Symbol = Hashable
Block = tuple[Symbol, ...]
Vertex = tuple[Symbol, ...]
Cycle = tuple[Block, ...]


def _validated_positive_counts(
    block_counts: Mapping[Block, int],
) -> tuple[dict[Block, int], int, int]:
    if not block_counts:
        raise ValueError("block count table must be nonempty")
    widths = {len(block) for block in block_counts}
    if len(widths) != 1:
        raise ValueError("all blocks must have one common width")
    width = next(iter(widths))
    if width <= 0:
        raise ValueError("block width must be positive")

    positive: dict[Block, int] = {}
    for block, count in block_counts.items():
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("block counts must be non-negative integers")
        if count:
            positive[tuple(block)] = count
    if not positive:
        raise ValueError("block count table must have positive total mass")
    total = sum(positive.values())
    return positive, width, total


def stationary_block_counts_balanced(block_counts: Mapping[Block, int]) -> bool:
    """Return whether integer k-block counts have matching prefix/suffix flow."""
    positive, width, _ = _validated_positive_counts(block_counts)
    if width == 1:
        return True

    outgoing: defaultdict[Vertex, int] = defaultdict(int)
    incoming: defaultdict[Vertex, int] = defaultdict(int)
    for block, count in positive.items():
        outgoing[block[:-1]] += count
        incoming[block[1:]] += count
    vertices = set(outgoing) | set(incoming)
    return all(outgoing[vertex] == incoming[vertex] for vertex in vertices)


def decompose_stationary_block_counts(block_counts: Mapping[Block, int]) -> tuple[Cycle, ...]:
    """Decompose balanced integer k-block counts into closed directed cycles.

    Each positive block is treated as that many edge copies from its length-(k-1)
    prefix to suffix.  The returned cycles use every edge copy exactly once.
    """
    positive, width, total = _validated_positive_counts(block_counts)
    if not stationary_block_counts_balanced(positive):
        raise ValueError("block counts must satisfy stationary prefix/suffix balance")

    outgoing: defaultdict[Vertex, list[Block]] = defaultdict(list)
    for block, count in positive.items():
        outgoing[block[:-1]].extend([block] * count)

    remaining = total
    cycles: list[Cycle] = []
    while remaining:
        starts = [vertex for vertex, edges in outgoing.items() if edges]
        if not starts:
            raise AssertionError("positive remaining edge count must expose an outgoing edge")
        start = min(starts, key=repr)
        current = start
        cycle: list[Block] = []
        while True:
            if not outgoing[current]:
                raise AssertionError("balanced residual graph cannot strand an open walk")
            block = outgoing[current].pop()
            cycle.append(block)
            remaining -= 1
            current = block[1:] if width > 1 else ()
            if current == start:
                break
        cycles.append(tuple(cycle))

    used = Counter(block for cycle in cycles for block in cycle)
    if used != Counter(positive):
        raise AssertionError("cycle decomposition must use every block copy exactly once")
    return tuple(cycles)


def cycle_period_symbols(cycle: Sequence[Block]) -> tuple[Symbol, ...]:
    """Return one periodic symbol word whose cyclic k-windows are ``cycle``."""
    edges = tuple(tuple(block) for block in cycle)
    if not edges:
        raise ValueError("cycle must be nonempty")
    width = len(edges[0])
    if width <= 0 or any(len(block) != width for block in edges):
        raise ValueError("cycle blocks must have one positive common width")
    for left, right in zip(edges, edges[1:] + edges[:1]):
        if width > 1 and left[1:] != right[:-1]:
            raise ValueError("cycle blocks do not form a closed shift-compatible walk")
    return tuple(block[0] for block in edges)


def cyclic_window_counts(period: Sequence[Symbol], width: int) -> dict[Block, int]:
    """Count cyclic length-``width`` windows, one starting at each phase."""
    symbols = tuple(period)
    if not symbols:
        raise ValueError("period must be nonempty")
    if isinstance(width, bool) or not isinstance(width, int) or width <= 0:
        raise ValueError("width must be a positive integer")
    size = len(symbols)
    counts: Counter[Block] = Counter()
    for start in range(size):
        block = tuple(symbols[(start + offset) % size] for offset in range(width))
        counts[block] += 1
    return dict(counts)


def periodic_cycle_mixture_block_law(cycles: Sequence[Cycle]) -> dict[Block, Fraction]:
    """Exact k-window law of the cycle-length weighted random-phase mixture.

    A cycle of length L is selected with weight L / D, where D is the total
    number of edge copies, and then one of its L phases is selected uniformly.
    Equivalently every edge-copy phase across all cycles receives mass 1 / D.
    """
    cycle_tuple = tuple(tuple(tuple(block) for block in cycle) for cycle in cycles)
    if not cycle_tuple or any(not cycle for cycle in cycle_tuple):
        raise ValueError("at least one nonempty cycle is required")
    widths = {len(block) for cycle in cycle_tuple for block in cycle}
    if len(widths) != 1 or next(iter(widths)) <= 0:
        raise ValueError("all cycle blocks must have one positive common width")
    width = next(iter(widths))
    total = sum(len(cycle) for cycle in cycle_tuple)

    law: defaultdict[Block, Fraction] = defaultdict(Fraction)
    for cycle in cycle_tuple:
        period = cycle_period_symbols(cycle)
        counts = cyclic_window_counts(period, width)
        for block, count in counts.items():
            law[block] += Fraction(count, total)
    return dict(law)


def stationary_rational_window_presampling_certificate(
    block_counts: Mapping[Block, int],
) -> tuple[tuple[Cycle, ...], dict[Block, Fraction]]:
    """Return a finite periodic certificate reproducing a rational local law."""
    positive, _, total = _validated_positive_counts(block_counts)
    cycles = decompose_stationary_block_counts(positive)
    law = periodic_cycle_mixture_block_law(cycles)
    expected = {block: Fraction(count, total) for block, count in positive.items()}
    if law != expected:
        raise AssertionError("periodic cycle mixture must reproduce the declared block law")
    return cycles, law


def uniform_full_support_window_rank(alphabet_size: int, width: int) -> int:
    """Exact deterministic-atom rank for the uniform full-support k-window law.

    The target has ``alphabet_size ** width`` positive k-block outputs at a fixed
    time, so any static deterministic mixture needs at least that many atoms.
    Balanced all-one block counts attain the same bound by the periodic-cycle
    construction above.
    """
    for name, value in (("alphabet_size", alphabet_size), ("width", width)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    return alphabet_size**width
