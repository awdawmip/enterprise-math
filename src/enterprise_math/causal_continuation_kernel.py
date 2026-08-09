"""Minimal finite witness state for coupled causal composition.

Witness identity is not primitive.  Given a coarse/marginal class r, witnesses
inside that class may be collapsed exactly when they have the same full future
continuation signature.  The minimal finite counting state is therefore the
typed multiplicity field

    kappa(r, tau) = number of current witnesses in coarse class r
                    with continuation type tau.

Anonymous kappa(r) is sufficient iff only one continuation type occurs in each
coarse fiber.  Full witness identity is unnecessary whenever multiple witnesses
share one continuation type.

This module uses only finite integer counts.  A continuation type may be any
hashable label already known to identify equal future signatures for the
future-language under study.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

Witness = Hashable
Coarse = Hashable
ContinuationType = Hashable
Target = Hashable


def typed_continuation_kernel(
    witness_to_coarse: dict[Witness, Coarse],
    witness_to_type: dict[Witness, ContinuationType],
) -> dict[tuple[Coarse, ContinuationType], int]:
    """Return kappa(r,tau) from explicit current witnesses."""
    if not isinstance(witness_to_coarse, dict) or not witness_to_coarse:
        raise ValueError("witness_to_coarse must be a non-empty dict")
    if set(witness_to_type) != set(witness_to_coarse):
        raise ValueError("witness_to_type must define exactly the current witnesses")
    result: dict[tuple[Coarse, ContinuationType], int] = defaultdict(int)
    for witness, coarse in witness_to_coarse.items():
        tau = witness_to_type[witness]
        try:
            hash(witness)
            hash(coarse)
            hash(tau)
        except TypeError as error:
            raise ValueError("witness, coarse, and continuation labels must be hashable") from error
        result[(coarse, tau)] += 1
    return dict(result)


def anonymous_coupling_kernel(
    typed_kernel: dict[tuple[Coarse, ContinuationType], int],
) -> dict[Coarse, int]:
    """Forget continuation type: kappa(r)=sum_tau kappa(r,tau)."""
    result: dict[Coarse, int] = defaultdict(int)
    for (coarse, _), count in typed_kernel.items():
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError("typed multiplicities must be positive integers")
        result[coarse] += count
    return dict(result)


def continuation_type_counts_by_coarse(
    typed_kernel: dict[tuple[Coarse, ContinuationType], int],
) -> dict[Coarse, int]:
    """Number of distinct future continuation types inside each coarse class."""
    types: dict[Coarse, set[ContinuationType]] = defaultdict(set)
    for (coarse, tau), count in typed_kernel.items():
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError("typed multiplicities must be positive integers")
        types[coarse].add(tau)
    return {coarse: len(values) for coarse, values in types.items()}


def anonymous_kernel_is_future_sufficient(
    typed_kernel: dict[tuple[Coarse, ContinuationType], int],
) -> bool:
    """Whether kappa(r) plus one induced future profile per r is exact.

    This is true exactly when every represented coarse fiber contains one
    continuation-signature type.
    """
    return all(
        count == 1
        for count in continuation_type_counts_by_coarse(typed_kernel).values()
    )


def compose_typed_kernel(
    typed_kernel: dict[tuple[Coarse, ContinuationType], int],
    continuation_profile: dict[tuple[ContinuationType, Target], int],
) -> dict[tuple[Coarse, Target], int]:
    """Count exact next-stage witnesses using continuation-type incidence.

    If one current witness of type tau has p(tau,z) continuations to z, then
    kappa(r,tau) such witnesses contribute kappa(r,tau)*p(tau,z).
    """
    result: dict[tuple[Coarse, Target], int] = defaultdict(int)
    types = {tau for (_, tau) in typed_kernel}
    profile_types = {tau for (tau, _) in continuation_profile}
    if not types <= profile_types:
        raise ValueError("continuation_profile must define every used continuation type")
    for (coarse, tau), current_count in typed_kernel.items():
        if isinstance(current_count, bool) or not isinstance(current_count, int) or current_count <= 0:
            raise ValueError("typed multiplicities must be positive integers")
        for (profile_tau, target), next_count in continuation_profile.items():
            if profile_tau != tau:
                continue
            if isinstance(next_count, bool) or not isinstance(next_count, int) or next_count < 0:
                raise ValueError("continuation counts must be non-negative integers")
            if next_count:
                result[(coarse, target)] += current_count * next_count
    return dict(result)


def induced_single_profile_per_coarse(
    typed_kernel: dict[tuple[Coarse, ContinuationType], int],
    continuation_profile: dict[tuple[ContinuationType, Target], int],
) -> dict[tuple[Coarse, Target], int]:
    """Return the unique future profile per coarse class when anonymity is safe.

    The profile is stored once, not multiplied by the number of witnesses.
    """
    if not anonymous_kernel_is_future_sufficient(typed_kernel):
        raise ValueError("some coarse class contains multiple continuation types")
    result: dict[tuple[Coarse, Target], int] = {}
    for coarse, _ in anonymous_coupling_kernel(typed_kernel).items():
        taus = {tau for (r, tau) in typed_kernel if r == coarse}
        tau = next(iter(taus))
        for (profile_tau, target), count in continuation_profile.items():
            if profile_tau == tau and count:
                result[(coarse, target)] = count
    return result


def compose_anonymous_when_safe(
    typed_kernel: dict[tuple[Coarse, ContinuationType], int],
    continuation_profile: dict[tuple[ContinuationType, Target], int],
) -> dict[tuple[Coarse, Target], int]:
    """Exact anonymous composition in the one-type-per-coarse regime."""
    multiplicity = anonymous_coupling_kernel(typed_kernel)
    induced = induced_single_profile_per_coarse(typed_kernel, continuation_profile)
    return {
        (coarse, target): multiplicity[coarse] * count
        for (coarse, target), count in induced.items()
    }
