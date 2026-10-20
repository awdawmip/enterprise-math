"""Exact small-domain resource layers for quotient-word repair compilers.

This executable oracle separates three storage quantities at fixed horizon:

* ``direction_demand``: pure-prime hard directions ``p**(h+1) <= N``;
* ``divisor_cover``: minimum candidate macro types whose divisor neighborhoods
  hit every semantic target that is prime-hard at horizon ``h``;
* ``exact_macro_storage``: true minimum optional composite dictionary size from
  the normalized quotient-word storage oracle.

The inequalities

    direction_demand <= divisor_cover <= exact_macro_storage

expose two independent overheads:

    mixed_divisor_overhead = divisor_cover - direction_demand
    residual_depth_overhead = exact_macro_storage - divisor_cover

The first is visible from divisibility alone.  The second is invisible to set
cover and comes from residual bounded-depth word constraints.

This module is an exact exponential oracle for small finite domains, not a
large-scale optimizer or novelty claim.
"""

from __future__ import annotations

from itertools import combinations

from .p018_p023_quotient_word_basis import (
    omega_with_multiplicity,
    prime_generator_basis,
)
from .p018_p023_quotient_word_storage import (
    minimum_composite_storage_count,
    semantic_storage_candidates,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_root_exp(root_exp: int) -> None:
    if isinstance(root_exp, bool) or not isinstance(root_exp, int) or root_exp < 2:
        raise ValueError("root_exp must be an integer at least 2")


def pure_direction_demand(max_state: int, horizon: int) -> int:
    """Number of prime directions whose ``(h+1)``-st power is in the domain."""
    _require_natural("max_state", max_state)
    _require_natural("horizon", horizon)
    return sum(
        prime ** (horizon + 1) <= max_state
        for prime in prime_generator_basis(max_state)
    )


def prime_hard_semantic_targets(
    max_state: int, root_exp: int, horizon: int
) -> tuple[int, ...]:
    """Normalized semantic targets not reachable prime-only within ``h``."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    return tuple(
        boundary
        for boundary in semantic_storage_candidates(max_state, root_exp)
        if omega_with_multiplicity(boundary) > horizon
    )


def useful_composite_candidates(
    max_state: int, root_exp: int, horizon: int
) -> tuple[int, ...]:
    """Semantic composite candidates that divide at least one prime-hard target."""
    hard = prime_hard_semantic_targets(max_state, root_exp, horizon)
    primes = set(prime_generator_basis(max_state))
    return tuple(
        candidate
        for candidate in semantic_storage_candidates(max_state, root_exp)
        if candidate not in primes and any(target % candidate == 0 for target in hard)
    )


def minimum_global_divisor_cover(
    max_state: int, root_exp: int, horizon: int
) -> tuple[int, tuple[int, ...]]:
    """Exact minimum divisor hitting set for all prime-hard semantic targets."""
    hard = prime_hard_semantic_targets(max_state, root_exp, horizon)
    if not hard:
        return 0, ()
    candidates = useful_composite_candidates(max_state, root_exp, horizon)
    for size in range(len(candidates) + 1):
        for chosen in combinations(candidates, size):
            if all(any(target % macro == 0 for macro in chosen) for target in hard):
                return size, chosen
    raise AssertionError("self-target candidates should always make the cover feasible")


def repair_resource_layers(
    max_state: int, root_exp: int, horizon: int
) -> dict[str, object]:
    """Return the exact three-layer storage decomposition for a small domain."""
    direction = pure_direction_demand(max_state, horizon)
    cover_size, cover = minimum_global_divisor_cover(
        max_state, root_exp, horizon
    )
    exact = minimum_composite_storage_count(max_state, root_exp, horizon)
    if exact is None:
        raise AssertionError("positive semantic domains have a finite normalized presentation")
    if not (direction <= cover_size <= exact):
        raise AssertionError("repair hierarchy inequality violated")
    return {
        "max_state": max_state,
        "root_exp": root_exp,
        "horizon": horizon,
        "direction_demand": direction,
        "divisor_cover": cover_size,
        "divisor_cover_witness": cover,
        "exact_macro_storage": exact,
        "mixed_divisor_overhead": cover_size - direction,
        "residual_depth_overhead": exact - cover_size,
        "prime_hard_targets": prime_hard_semantic_targets(
            max_state, root_exp, horizon
        ),
    }


# Orthogonal strict witnesses from the proof-shaped resource decomposition.
assert repair_resource_layers(18, 5, 2)["direction_demand"] == 1
assert repair_resource_layers(18, 5, 2)["divisor_cover"] == 2
assert repair_resource_layers(18, 5, 2)["exact_macro_storage"] == 2
assert repair_resource_layers(18, 5, 2)["mixed_divisor_overhead"] == 1
assert repair_resource_layers(18, 5, 2)["residual_depth_overhead"] == 0

assert repair_resource_layers(27, 5, 2)["direction_demand"] == 2
assert repair_resource_layers(27, 5, 2)["divisor_cover"] == 2
assert repair_resource_layers(27, 5, 2)["exact_macro_storage"] == 3
assert repair_resource_layers(27, 5, 2)["mixed_divisor_overhead"] == 0
assert repair_resource_layers(27, 5, 2)["residual_depth_overhead"] == 1
