"""Exact checkpoint-design objectives for Barlow prefix observations.

For positive segment lengths ell_j, the number of represented checkpoint
imbalance trajectories is ``prod_j (ell_j+1)``.  Discrete balancing maximizes
this image size under a fixed final-visible checkpoint budget, while the same
balanced schedule minimizes the already-proved order-two collision count.
"""

from __future__ import annotations

from .p022_barlow_precision_fibers import (
    balanced_checkpoint_layers,
    balanced_segment_lengths,
    equal_observation_ordered_pair_count,
    selected_observation_image_size,
)


def _require_budget(length: int, checkpoint_count: int) -> None:
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    if (
        isinstance(checkpoint_count, bool)
        or not isinstance(checkpoint_count, int)
        or checkpoint_count < 0
        or checkpoint_count > length
    ):
        raise ValueError("checkpoint_count must lie in 0..length")


def maximum_image_size_with_final_checkpoint(
    length: int, checkpoint_count: int
) -> int:
    """Maximum number of represented states with m checkpoints including N."""
    _require_budget(length, checkpoint_count)
    if checkpoint_count == 0:
        if length == 0:
            return 1
        raise ValueError("positive length requires a final checkpoint")
    result = 1
    for segment in balanced_segment_lengths(length, checkpoint_count):
        result *= segment + 1
    return result


def minimum_image_size_with_final_checkpoint(
    length: int, checkpoint_count: int
) -> int:
    """Minimum image size among final-visible m-checkpoint schedules.

    The extremal positive segment multiset is ``(1,...,1,N-m+1)``.
    """
    _require_budget(length, checkpoint_count)
    if checkpoint_count == 0:
        if length == 0:
            return 1
        raise ValueError("positive length requires a final checkpoint")
    return (2 ** (checkpoint_count - 1)) * (length - checkpoint_count + 2)


def maximum_image_size_with_checkpoint_count(
    length: int, checkpoint_count: int
) -> int:
    """Maximum image size when the final layer is optional.

    Extending the observed prefix strictly increases at least one factor, so an
    optimum always uses the final layer.  Balancing then gives the previous
    theorem.
    """
    _require_budget(length, checkpoint_count)
    if checkpoint_count == 0:
        return 1
    return maximum_image_size_with_final_checkpoint(length, checkpoint_count)


def minimum_image_size_with_checkpoint_count(
    length: int, checkpoint_count: int
) -> int:
    """Minimum image size with m checkpoints and optional final visibility.

    Every constrained segment has length at least one, hence contributes at
    least two observed net imbalances.  The minimum is ``2^m``, attained by
    checkpoints ``1,2,...,m`` with the longest possible hidden tail.
    """
    _require_budget(length, checkpoint_count)
    return 2 ** checkpoint_count


def balanced_schedule_joint_objectives(
    length: int, checkpoint_count: int
) -> tuple[tuple[int, ...], int, int]:
    """Return balanced layers, image size, and ordered pair-collision count."""
    _require_budget(length, checkpoint_count)
    if checkpoint_count == 0:
        if length == 0:
            return (), 1, 1
        raise ValueError("joint final-visible objective needs at least one checkpoint")
    layers = balanced_checkpoint_layers(length, checkpoint_count)
    image = selected_observation_image_size(length, layers)
    collision_pairs = equal_observation_ordered_pair_count(length, layers)
    return layers, image, collision_pairs
