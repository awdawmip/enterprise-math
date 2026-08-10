"""Endpoint-only circulation defect of finite sliding-window records.

For a finite record x_0,...,x_(N-1) and window width k>=2, each observed
k-block is an edge from its length-(k-1) prefix to suffix.  Interior vertex
incidences telescope.  The complete outgoing-minus-incoming defect is therefore

    +1 at the initial (k-1)-prefix,
    -1 at the terminal (k-1)-suffix,
    0 elsewhere,

with cancellation when the two endpoint words coincide.

Adding the k-1 wraparound blocks produced by periodic repetition closes this
boundary defect and yields the exact cyclic window counts.  This is finite
integer bookkeeping, not a stochastic or ontological assumption.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Hashable, Mapping, Sequence
from fractions import Fraction

Symbol = Hashable
Block = tuple[Symbol, ...]
Vertex = tuple[Symbol, ...]


def _validated_record(record: Sequence[Symbol], width: int) -> tuple[tuple[Symbol, ...], int]:
    symbols = tuple(record)
    if not symbols:
        raise ValueError("record must be nonempty")
    if isinstance(width, bool) or not isinstance(width, int) or width <= 0 or width > len(symbols):
        raise ValueError("width must satisfy 1 <= width <= record length")
    return symbols, width


def linear_window_counts(record: Sequence[Symbol], width: int) -> dict[Block, int]:
    """Count non-wrapping length-k windows in a finite record."""
    symbols, width = _validated_record(record, width)
    counts: Counter[Block] = Counter()
    for start in range(len(symbols) - width + 1):
        counts[tuple(symbols[start : start + width])] += 1
    return dict(counts)


def cyclic_window_counts(record: Sequence[Symbol], width: int) -> dict[Block, int]:
    """Count one cyclic length-k window from every record position."""
    symbols, width = _validated_record(record, width)
    size = len(symbols)
    counts: Counter[Block] = Counter()
    for start in range(size):
        counts[
            tuple(symbols[(start + offset) % size] for offset in range(width))
        ] += 1
    return dict(counts)


def flow_defect_from_block_counts(block_counts: Mapping[Block, int]) -> dict[Vertex, int]:
    """Return outgoing-minus-incoming flow at every nonzero-defect vertex."""
    if not block_counts:
        raise ValueError("block count table must be nonempty")
    widths = {len(block) for block in block_counts}
    if len(widths) != 1:
        raise ValueError("all blocks must have one common width")
    width = next(iter(widths))
    if width <= 0:
        raise ValueError("block width must be positive")
    if any(
        isinstance(count, bool) or not isinstance(count, int) or count < 0
        for count in block_counts.values()
    ):
        raise ValueError("block counts must be non-negative integers")

    if width == 1:
        return {}

    defect: defaultdict[Vertex, int] = defaultdict(int)
    for block, count in block_counts.items():
        if not count:
            continue
        defect[tuple(block[:-1])] += count
        defect[tuple(block[1:])] -= count
    return {vertex: value for vertex, value in defect.items() if value}


def linear_record_flow_defect(record: Sequence[Symbol], width: int) -> dict[Vertex, int]:
    """Flow defect of the ordinary non-wrapping sliding windows."""
    return flow_defect_from_block_counts(linear_window_counts(record, width))


def endpoint_flow_defect(record: Sequence[Symbol], width: int) -> dict[Vertex, int]:
    """Closed form: initial prefix source minus terminal suffix sink."""
    symbols, width = _validated_record(record, width)
    if width == 1:
        return {}
    start = tuple(symbols[: width - 1])
    end = tuple(symbols[-(width - 1) :])
    if start == end:
        return {}
    return {start: 1, end: -1}


def periodic_wrap_blocks(record: Sequence[Symbol], width: int) -> tuple[Block, ...]:
    """The k-1 cyclic windows missing from the linear record count."""
    symbols, width = _validated_record(record, width)
    if width == 1:
        return ()
    size = len(symbols)
    first_wrap_start = size - width + 1
    return tuple(
        tuple(symbols[(start + offset) % size] for offset in range(width))
        for start in range(first_wrap_start, size)
    )


def periodically_closed_window_counts(record: Sequence[Symbol], width: int) -> dict[Block, int]:
    """Add the exact wrap blocks and return the balanced cyclic count table."""
    counts = Counter(linear_window_counts(record, width))
    counts.update(periodic_wrap_blocks(record, width))
    result = dict(counts)
    if result != cyclic_window_counts(record, width):
        raise AssertionError("linear counts plus wrap blocks must equal cyclic counts")
    if flow_defect_from_block_counts(result):
        raise AssertionError("periodic closure must eliminate the endpoint flow defect")
    return result


def boundary_window_fraction(record: Sequence[Symbol], width: int) -> Fraction:
    """Exact wrap-window fraction (k-1)/N in the periodicized record."""
    symbols, width = _validated_record(record, width)
    return Fraction(width - 1, len(symbols))
