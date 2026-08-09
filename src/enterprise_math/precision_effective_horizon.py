"""Task-relative effective precision horizon for the R004 finite toy model.

This is an R004 consumer of the P018/P023 future-safe quotient idea, not a new
mother theory.  A declared fine-state future signature is sufficient at a
coarser scale exactly when it is constant on every projection fiber.  The least
such scale is a process/task-relative effective maximum: finer physical states
may exist, but the declared future language cannot use their extra distinctions.
"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Hashable

from enterprise_math.precision_genesis import projection, scale_chain


def signature_factors_through_scale(
    final_scale: int,
    candidate_scale: int,
    signatures: Sequence[Hashable],
) -> bool:
    if isinstance(final_scale, bool) or not isinstance(final_scale, int) or final_scale <= 0:
        raise ValueError("final_scale must be a positive integer")
    if isinstance(candidate_scale, bool) or not isinstance(candidate_scale, int) or candidate_scale <= 0:
        raise ValueError("candidate_scale must be a positive integer")
    if final_scale % candidate_scale:
        raise ValueError("candidate_scale must divide final_scale")
    signature = tuple(signatures)
    if len(signature) != final_scale:
        raise ValueError("toy signature needs one value per fine state")

    seen: dict[int, Hashable] = {}
    for state, value in enumerate(signature):
        coarse = projection(state, candidate_scale, final_scale)
        if coarse in seen and seen[coarse] != value:
            return False
        seen[coarse] = value
    return True


def least_sufficient_scale(
    final_scale: int, signatures: Sequence[Hashable]
) -> int:
    """Return the least binary toy scale through which the signature factors."""
    scales = scale_chain(final_scale)
    for candidate in scales:
        if signature_factors_through_scale(final_scale, candidate, signatures):
            return candidate
    # The final identity projection always has singleton fibers, so this branch
    # is unreachable after input validation.
    raise AssertionError("final scale must always be sufficient")


def effective_refinement_factor(
    final_scale: int, signatures: Sequence[Hashable]
) -> int:
    """How much finer the physical toy layer is than the task needs."""
    sufficient = least_sufficient_scale(final_scale, signatures)
    return final_scale // sufficient
