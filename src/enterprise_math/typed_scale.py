"""Typed scale transitions for Enterprise Math.

A scale projection changes the scale tag. Treating it as an untyped endomap
would create spurious repeated-division dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import collapse
from .scale_algebra import project_scale_factor


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
    """Canonically project a tagged state to a comparable coarser scale."""
    projected = project_scale_factor(state.value, state.scale, target_scale)
    return ScaleState(target_scale, projected)


def collapse_tagged(state: ScaleState, exponent: int) -> ScaleState:
    """Apply perfect-power collapse without changing the scale tag."""
    return ScaleState(state.scale, collapse(state.value, exponent))


def strict_rank_decrease(before: ScaleState, after: ScaleState) -> bool:
    """Canonical lexicographic rank decrease: scale first, then coordinate."""
    return (after.scale, after.value) < (before.scale, before.value)
