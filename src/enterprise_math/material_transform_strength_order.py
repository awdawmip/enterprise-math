"""Ordering of finite material transforms by physical activation depth.

The original E001 material curve algebra uses

    H_p(r;A) = floor(r^p/A^(p-1)),
    G_p(r;A) = R_p(r*A^(p-1)).

For every ``0<=r<=A`` and positive integer ``p``:

    H_p(r;A) <= r <= G_p(r;A).

The first inequality follows from ``r^(p-1)<=A^(p-1)``.  For the second,
``r^p <= r*A^(p-1)``, so the integer p-th root is at least ``r``.

Consequently, for any nondecreasing base response branch and any declared
response threshold ``R`` (for example the physical one-tick strength threshold
from ``material_strength_depth``), the first positive depth reaching ``R`` is
ordered

    k_soft <= k_base <= k_hard,

whenever the respective activation depths exist.  ``None`` is treated as no
activation inside the represented finite material domain.

Thus curve composition has a direct world-engine meaning: root/softening can
move the physically active material layer outward, while power/hardening can
move it inward, without changing geometry or the threshold itself.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import hardening_branch, hardening_sample, softening_branch, softening_sample


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _activation_depth(samples: tuple[int, ...], threshold: int) -> int | None:
    for depth, sample in enumerate(samples[1:], start=1):
        if sample >= threshold:
            return depth
    return None


def _depth_key(depth: int | None) -> int:
    return 10**18 if depth is None else depth


@dataclass(frozen=True)
class MaterialTransformSampleOrder:
    sample: int
    amplitude: int
    power: int
    hardening_sample: int
    base_sample: int
    softening_sample: int


@dataclass(frozen=True)
class MaterialTransformActivationOrder:
    amplitude: int
    power: int
    required_response_sample: int
    base_branch: tuple[int, ...]
    hardening_branch: tuple[int, ...]
    softening_branch: tuple[int, ...]
    softening_activation_depth: int | None
    base_activation_depth: int | None
    hardening_activation_depth: int | None


def material_transform_sample_order(
    sample: int,
    amplitude: int,
    power: int,
) -> MaterialTransformSampleOrder:
    _nonnegative("sample", sample)
    _positive("amplitude", amplitude)
    _positive("power", power)
    if sample > amplitude:
        raise ValueError("sample must not exceed amplitude")
    hard = hardening_sample(sample, amplitude, power)
    soft = softening_sample(sample, amplitude, power)
    if not hard <= sample <= soft:
        raise AssertionError("finite material transform order failed")
    return MaterialTransformSampleOrder(
        sample=sample,
        amplitude=amplitude,
        power=power,
        hardening_sample=hard,
        base_sample=sample,
        softening_sample=soft,
    )


def material_transform_activation_order(
    base_samples: tuple[int, ...] | list[int],
    amplitude: int,
    power: int,
    required_response_sample: int,
) -> MaterialTransformActivationOrder:
    """Compare first positive threshold depth after H_p / identity / G_p."""
    _positive("amplitude", amplitude)
    _positive("power", power)
    _nonnegative("required_response_sample", required_response_sample)
    if required_response_sample > amplitude:
        raise ValueError("required_response_sample must not exceed amplitude")
    base = tuple(base_samples)
    if not base:
        raise ValueError("base branch must be nonempty")
    if any(
        isinstance(sample, bool)
        or not isinstance(sample, int)
        or sample < 0
        or sample > amplitude
        for sample in base
    ):
        raise ValueError("base samples must be integers in 0..amplitude")
    if any(left > right for left, right in zip(base, base[1:])):
        raise ValueError("base branch must be nondecreasing")
    hard = hardening_branch(base, amplitude, power)
    soft = softening_branch(base, amplitude, power)
    hard_depth = _activation_depth(hard, required_response_sample)
    base_depth = _activation_depth(base, required_response_sample)
    soft_depth = _activation_depth(soft, required_response_sample)
    if not _depth_key(soft_depth) <= _depth_key(base_depth) <= _depth_key(hard_depth):
        raise AssertionError("material transform activation depths violated H<=id<=G order")
    return MaterialTransformActivationOrder(
        amplitude=amplitude,
        power=power,
        required_response_sample=required_response_sample,
        base_branch=base,
        hardening_branch=hard,
        softening_branch=soft,
        softening_activation_depth=soft_depth,
        base_activation_depth=base_depth,
        hardening_activation_depth=hard_depth,
    )
