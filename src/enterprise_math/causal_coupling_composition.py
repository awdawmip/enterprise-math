"""Composition of causal coupling with witness-sensitive continuations.

A one-layer coupling kernel only stores anonymous multiplicities of joint
signature classes over a marginal fiber.  That is enough for one forgetting
step but not generally for a later composition: different joint witnesses in the
same marginal fiber may have different continuation profiles.

If every witness inside one marginal fiber has the same continuation profile,
identity can be safely erased and the composed multiplicity is simply

    kappa_parent(r) * continuation_profile(r,c).

Otherwise the anonymous kernel is not future-safe; exact composition requires
witness incidence or a finer quotient.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable


Joint = Hashable
Marginal = Hashable
NextClass = Hashable
Profile = dict[NextClass, int]


def _validate_profile(profile: Profile) -> None:
    if not isinstance(profile, dict):
        raise ValueError("continuation profiles must be dicts")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in profile.values()
    ):
        raise ValueError("continuation multiplicities must be non-negative integers")


def aggregate_continuations(
    joint_to_marginal: dict[Joint, Marginal],
    continuations: dict[Joint, Profile],
) -> dict[tuple[Marginal, NextClass], int]:
    """Exact next-stage multiplicity while retaining intermediate witness identity."""
    if not isinstance(joint_to_marginal, dict) or not joint_to_marginal:
        raise ValueError("joint_to_marginal must be a non-empty dict")
    if set(continuations) != set(joint_to_marginal):
        raise ValueError("continuations must be defined for every joint witness")
    result: dict[tuple[Marginal, NextClass], int] = defaultdict(int)
    for joint, marginal in joint_to_marginal.items():
        profile = continuations[joint]
        _validate_profile(profile)
        for next_class, count in profile.items():
            result[(marginal, next_class)] += count
    return dict(result)


def continuation_profiles_uniform_on_fibers(
    joint_to_marginal: dict[Joint, Marginal],
    continuations: dict[Joint, Profile],
) -> bool:
    """Whether every witness in one marginal fiber has the same continuation profile."""
    if set(continuations) != set(joint_to_marginal):
        raise ValueError("continuations must be defined for every joint witness")
    seen: dict[Marginal, Profile] = {}
    for joint, marginal in joint_to_marginal.items():
        profile = continuations[joint]
        _validate_profile(profile)
        normalized = {key: value for key, value in profile.items() if value != 0}
        if marginal in seen and seen[marginal] != normalized:
            return False
        seen[marginal] = normalized
    return True


def anonymous_uniform_composition(
    joint_to_marginal: dict[Joint, Marginal],
    continuations: dict[Joint, Profile],
) -> dict[tuple[Marginal, NextClass], int]:
    """Compose after erasing witness identity, only when uniformity proves it safe."""
    if not continuation_profiles_uniform_on_fibers(joint_to_marginal, continuations):
        raise ValueError("witness identity is required: continuation profiles are non-uniform")

    fiber_counts: dict[Marginal, int] = defaultdict(int)
    representative: dict[Marginal, Profile] = {}
    for joint, marginal in joint_to_marginal.items():
        fiber_counts[marginal] += 1
        representative[marginal] = {
            key: value for key, value in continuations[joint].items() if value != 0
        }

    result: dict[tuple[Marginal, NextClass], int] = {}
    for marginal, count in fiber_counts.items():
        for next_class, multiplicity in representative[marginal].items():
            result[(marginal, next_class)] = count * multiplicity
    return result
