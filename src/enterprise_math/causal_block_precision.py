"""Causal complete-block regime generating the P018 quotient/detail/carry calculus.

Assume a real LEGO construction has a complete block capacity d.  Complete
levels are V_d(k)=k*d.  P008 then gives

    root q = floor(n/d)
    collapse C_d(n)=d*q
    detail r=n-C_d(n)=n mod d.

Thus Euclidean quotient/detail is a shadow of completing as many actual d-unit
blocks as possible.  If e=m*d corresponds to grouping m d-blocks into one
superblock, then C_e(C_d(n))=C_e(n).  The divisibility order of P018 is therefore
causally generated exactly when the scale chain is backed by such nested block
assemblies.

Adding two quotient/detail states produces the usual carry
floor((r_x+r_y)/d); this is the same coherent pair-grade law studied in
`causal_grade_coherence.py`.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BlockPrecisionState:
    block_capacity: int
    complete_blocks: int
    detail_units: int

    @property
    def collapsed_units(self) -> int:
        return self.block_capacity * self.complete_blocks

    @property
    def exact_units(self) -> int:
        return self.collapsed_units + self.detail_units


def _require_capacity(capacity: int) -> None:
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("block capacity must be a positive integer")


def block_precision_state(units: int, block_capacity: int) -> BlockPrecisionState:
    if isinstance(units, bool) or not isinstance(units, int) or units < 0:
        raise ValueError("units must be a non-negative integer")
    _require_capacity(block_capacity)
    quotient, detail = divmod(units, block_capacity)
    return BlockPrecisionState(block_capacity, quotient, detail)


def complete_block_collapse(units: int, block_capacity: int) -> int:
    state = block_precision_state(units, block_capacity)
    return state.collapsed_units


def nested_block_projection_is_exact(
    units: int,
    fine_capacity: int,
    coarse_capacity: int,
) -> bool:
    """C_e(C_d(n))=C_e(n) when e is an integer multiple of d."""
    _require_capacity(fine_capacity)
    _require_capacity(coarse_capacity)
    if coarse_capacity % fine_capacity != 0:
        raise ValueError("coarse capacity must be an integer multiple of fine capacity")
    return complete_block_collapse(
        complete_block_collapse(units, fine_capacity),
        coarse_capacity,
    ) == complete_block_collapse(units, coarse_capacity)


def add_block_precision_states(
    left: BlockPrecisionState,
    right: BlockPrecisionState,
) -> tuple[BlockPrecisionState, int]:
    """Add two states at the same complete-block scale, returning `(sum, carry)`.

    The carry is the number of new complete d-blocks generated solely by the
    two detail reservoirs.
    """
    if left.block_capacity != right.block_capacity:
        raise ValueError("states must use the same block capacity")
    d = left.block_capacity
    detail_total = left.detail_units + right.detail_units
    carry, detail = divmod(detail_total, d)
    result = BlockPrecisionState(
        block_capacity=d,
        complete_blocks=left.complete_blocks + right.complete_blocks + carry,
        detail_units=detail,
    )
    if result.exact_units != left.exact_units + right.exact_units:
        raise AssertionError("block quotient/detail addition failed exact reconstruction")
    return result, carry


def regroup_block_state(
    state: BlockPrecisionState,
    coarse_capacity: int,
) -> BlockPrecisionState:
    """Project an exact d-block state into a nested superblock capacity e=m*d."""
    if coarse_capacity % state.block_capacity != 0:
        raise ValueError("coarse capacity must be a multiple of current block capacity")
    return block_precision_state(state.exact_units, coarse_capacity)
