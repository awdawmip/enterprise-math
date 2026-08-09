"""Exact finite-band predicates on hidden scalar A3 fibers.

For an integer linear scalar observable z=w^T c+b and a coordinate partition,
the hidden variation inside one coarse fiber is the subgroup q*Z, where q is
the gcd of within-block coefficient differences. Thus the fiber values are

    z0 + q*Z.

For the finite band predicate |z|<=R:
- q=0: z is coarse-readable and the predicate is exact normally;
- q>0: unsupported values always exist because the progression is unbounded;
  supported values exist iff the least absolute representative of z0 mod q is
  at most R.

State-local residue shortcuts do not generally survive an all-state requirement:
if the band predicate is nonconstant on the full integer domain, a partition is
globally exact iff the scalar observable itself descends.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .linear_observation_quotient import refine_partition_for_linear_observations
from .linear_relation_quotient import Partition


@dataclass(frozen=True)
class HiddenBandProfile:
    hidden_step: int
    least_absolute_residue: int
    radius: int
    has_supported_value: bool
    has_unsupported_value: bool
    exact: bool
    exact_value: bool | None


@dataclass(frozen=True)
class GlobalBandProfile:
    scalar_image_step: int
    least_absolute_residue: int
    radius: int
    has_supported_state: bool
    has_unsupported_state: bool
    globally_constant: bool
    constant_value: bool | None


def _require_weights(weights: tuple[int, ...]) -> None:
    if not isinstance(weights, tuple) or not weights:
        raise ValueError("weights must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in weights):
        raise ValueError("weights must be integers")


def scalar_hidden_step(weights: tuple[int, ...], partition: Partition) -> int:
    """Return q>=0 with w(K_A)=q*Z for a scalar linear observable."""
    _require_weights(weights)
    flattened = [index for group in partition for index in group]
    if any(not isinstance(group, tuple) or not group for group in partition):
        raise ValueError("partition groups must be non-empty tuples")
    if sorted(flattened) != list(range(len(weights))):
        raise ValueError("partition must cover every coordinate exactly once")

    step = 0
    for group in partition:
        anchor = group[0]
        for coordinate in group[1:]:
            step = gcd(step, abs(weights[coordinate] - weights[anchor]))
    return step


def scalar_global_image_step(weights: tuple[int, ...]) -> int:
    """Return g>=0 with w(Z^k)=g*Z."""
    _require_weights(weights)
    step = 0
    for value in weights:
        step = gcd(step, abs(value))
    return step


def least_absolute_residue(value: int, modulus: int) -> int:
    """Minimum |value+modulus*t| over integer t, for modulus>0."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")
    residue = value % modulus
    return min(residue, modulus - residue)


def hidden_band_profile(
    base_value: int, hidden_step: int, radius: int
) -> HiddenBandProfile:
    """Exact support/ambiguity profile of |z|<=radius on z0+q*Z."""
    if isinstance(base_value, bool) or not isinstance(base_value, int):
        raise ValueError("base_value must be an integer")
    if (
        isinstance(hidden_step, bool)
        or not isinstance(hidden_step, int)
        or hidden_step < 0
    ):
        raise ValueError("hidden_step must be a non-negative integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")

    if hidden_step == 0:
        supported = abs(base_value) <= radius
        return HiddenBandProfile(
            hidden_step=0,
            least_absolute_residue=abs(base_value),
            radius=radius,
            has_supported_value=supported,
            has_unsupported_value=not supported,
            exact=True,
            exact_value=supported,
        )

    nearest = least_absolute_residue(base_value, hidden_step)
    supported = nearest <= radius
    unsupported = True
    return HiddenBandProfile(
        hidden_step=hidden_step,
        least_absolute_residue=nearest,
        radius=radius,
        has_supported_value=supported,
        has_unsupported_value=unsupported,
        exact=not supported,
        exact_value=False if not supported else None,
    )


def hidden_band_profile_for_partition(
    weights: tuple[int, ...],
    partition: Partition,
    base_value: int,
    radius: int,
) -> HiddenBandProfile:
    """Compute the band profile directly from a scalar observable and partition."""
    return hidden_band_profile(
        base_value,
        scalar_hidden_step(weights, partition),
        radius,
    )


def global_band_profile(
    weights: tuple[int, ...], bias: int, radius: int
) -> GlobalBandProfile:
    """Truth variability of |w^T c+bias|<=radius over the full lattice Z^k."""
    _require_weights(weights)
    if isinstance(bias, bool) or not isinstance(bias, int):
        raise ValueError("bias must be an integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")

    image_step = scalar_global_image_step(weights)
    if image_step == 0:
        supported = abs(bias) <= radius
        return GlobalBandProfile(
            scalar_image_step=0,
            least_absolute_residue=abs(bias),
            radius=radius,
            has_supported_state=supported,
            has_unsupported_state=not supported,
            globally_constant=True,
            constant_value=supported,
        )

    nearest = least_absolute_residue(bias, image_step)
    supported = nearest <= radius
    # A nonzero global image b+gZ is unbounded, so unsupported states exist.
    unsupported = True
    return GlobalBandProfile(
        scalar_image_step=image_step,
        least_absolute_residue=nearest,
        radius=radius,
        has_supported_state=supported,
        has_unsupported_state=unsupported,
        globally_constant=not supported,
        constant_value=False if not supported else None,
    )


def band_partition_globally_exact(
    weights: tuple[int, ...],
    bias: int,
    radius: int,
    partition: Partition,
) -> bool:
    """Whether one partition gives an exact band truth value on every coarse fiber."""
    profile = global_band_profile(weights, bias, radius)
    if profile.globally_constant:
        return True
    return scalar_hidden_step(weights, partition) == 0


def minimum_global_band_partition(
    weights: tuple[int, ...],
    bias: int,
    radius: int,
    initial_partition: Partition,
) -> Partition:
    """Coarsest refinement exact for the finite-band predicate on all Z^k states.

    If the predicate is globally constant, no refinement is required. Otherwise
    global exactness is equivalent to exact scalar observability, so the
    ordinary block-constant linear-observation refinement is complete.
    """
    profile = global_band_profile(weights, bias, radius)
    if profile.globally_constant:
        return initial_partition
    return refine_partition_for_linear_observations((weights,), initial_partition)
