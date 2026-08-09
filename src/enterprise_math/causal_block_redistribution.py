"""Hidden relation rank created by forgetting separate block totals.

Partition m fine slots into k coarse blocks of sizes m_i.  If every block total
is retained, hidden motion is the direct sum of each within-block zero-sum
lattice, with rank

    sum_i (m_i-1) = m-k.

If the k block totals are then collapsed to one grand total, their differences
may move in the zero-sum coarse redistribution lattice

    K_k = {delta in Z^k : sum delta_i=0},

which has rank k-1.  The total hidden rank becomes

    (m-k) + (k-1) = m-1.

Thus joining two blocks and forgetting their separate totals creates exactly one
new cross-block hidden relation freedom.  More generally, forgetting k separate
totals down to one adds k-1 freedoms.  This is the relation-rank counterpart of
the LEGO fiber convolution law.
"""

from __future__ import annotations

from .causal_hidden_motion import hidden_motion_rank


def validate_block_sizes(block_sizes: tuple[int, ...]) -> None:
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    if any(
        isinstance(size, bool) or not isinstance(size, int) or size <= 0
        for size in block_sizes
    ):
        raise ValueError("block sizes must be positive integers")


def internal_hidden_rank(block_sizes: tuple[int, ...]) -> int:
    """Hidden rank when every coarse block total remains separately visible."""
    validate_block_sizes(block_sizes)
    return sum(hidden_motion_rank(size) for size in block_sizes)


def cross_block_redistribution_rank(block_count: int) -> int:
    """Rank created by forgetting k separate totals and retaining only their sum."""
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count <= 0:
        raise ValueError("block_count must be a positive integer")
    return block_count - 1


def grand_total_hidden_rank(block_sizes: tuple[int, ...]) -> int:
    validate_block_sizes(block_sizes)
    return internal_hidden_rank(block_sizes) + cross_block_redistribution_rank(
        len(block_sizes)
    )


def direct_slot_hidden_rank(block_sizes: tuple[int, ...]) -> int:
    """Rank from treating all fine slots as one grand-total fiber directly."""
    validate_block_sizes(block_sizes)
    return hidden_motion_rank(sum(block_sizes))


def rank_decomposition_identity(block_sizes: tuple[int, ...]) -> bool:
    """(m-k)+(k-1)=m-1 for the actual block partition."""
    return grand_total_hidden_rank(block_sizes) == direct_slot_hidden_rank(block_sizes)


def new_cross_freedom_when_two_blocks_merge(left_size: int, right_size: int) -> int:
    validate_block_sizes((left_size, right_size))
    before = internal_hidden_rank((left_size, right_size))
    after = grand_total_hidden_rank((left_size, right_size))
    return after - before
