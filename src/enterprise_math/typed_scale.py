"""Typed scale transitions for Enterprise Math.

Scale projection changes the scale tag. Treating it as an untyped endomap would
create spurious iteration dynamics, so the scale factor is part of the state.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import collapse


@dataclass(frozen=True, order=True)
class ScaleState:
    scale: int
    value: int

    def __post_init__(self) -> None:
        if isinstance(self.scale, bool) or not isinstance(self.scale, int) or self.scale <= 0:
            raise ValueError("scale must be a positive integer")
        if isinstance(self.value, bool) or not isinstance(self.value, int) or self.value < 0:
            raise ValueError("value must be a non-negative integer")


def project_tagged(state: ScaleState, target_scale: int) -> ScaleState:
    """Canonically project a tagged state to a coarser divisor scale."""
    if isinstance(target_scale, bool) or not isinstance(target_scale, int) or target_scale <= 0:
        raise ValueError("target_scale must be a positive integer")
    if state.scale % target_scale != 0:
        raise ValueError("target_scale must divide the current scale")
    ratio = state.scale // target_scale
    return ScaleState(target_scale, state.value // ratio)


def collapse_tagged(state: ScaleState, exponent: int) -> ScaleState:
    """Apply perfect-power collapse without changing the scale tag."""
    return ScaleState(state.scale, collapse(state.value, exponent))


def is_strict_rank_decrease(before: ScaleState, after: ScaleState) -> bool:
    """Check the canonical lexicographic rank decrease (scale first, then value)."""
    return (after.scale, after.value) < (before.scale, before.value)
