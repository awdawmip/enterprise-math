"""GCD/LCM as dual causal shadows of operation/structure compatibility.

Two different causal questions generate the classical arithmetic pair.

1. One structure, many additive future generators U.  For a fixed-block quotient
   to forget detail exactly, its block capacity d must divide every generator.
   The largest compatible block is therefore gcd(U).

2. One shared additive translation acting across several quotient structures
   whose safe translation monoids are T_i*N0.  The translation must be a multiple
   of every T_i.  The smallest positive synchronizing operation is therefore
   lcm(T_i).

Thus gcd and lcm appear from opposite compatibility directions rather than from
an a priori precision lattice.
"""

from __future__ import annotations

from math import gcd, lcm


def _validate_positive_tuple(values: tuple[int, ...], name: str) -> None:
    if not isinstance(values, tuple) or not values:
        raise ValueError(f"{name} must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) or value <= 0 for value in values):
        raise ValueError(f"{name} must contain positive integers")


def coarsest_block_scale_for_actions(generators: tuple[int, ...]) -> int:
    """Largest d such that every additive generator is a whole d-block action."""
    _validate_positive_tuple(generators, "generators")
    result = generators[0]
    for value in generators[1:]:
        result = gcd(result, value)
    return result


def smallest_shared_safe_translation(structure_periods: tuple[int, ...]) -> int:
    """Smallest positive translation that is safe for every cyclic safe monoid T_i*N0."""
    _validate_positive_tuple(structure_periods, "structure_periods")
    result = structure_periods[0]
    for value in structure_periods[1:]:
        result = lcm(result, value)
    return result


def action_language_compatible_with_block(
    generators: tuple[int, ...],
    block_capacity: int,
) -> bool:
    _validate_positive_tuple(generators, "generators")
    if isinstance(block_capacity, bool) or not isinstance(block_capacity, int) or block_capacity <= 0:
        raise ValueError("block_capacity must be positive")
    return all(value % block_capacity == 0 for value in generators)


def translation_compatible_with_structures(
    translation: int,
    structure_periods: tuple[int, ...],
) -> bool:
    _validate_positive_tuple(structure_periods, "structure_periods")
    if isinstance(translation, bool) or not isinstance(translation, int) or translation < 0:
        raise ValueError("translation must be non-negative")
    return all(translation % period == 0 for period in structure_periods)


def dual_compatibility_certificate(
    generators: tuple[int, ...],
    structure_periods: tuple[int, ...],
) -> tuple[int, int]:
    """Return `(max block scale for actions, min shared operation for structures)`."""
    return (
        coarsest_block_scale_for_actions(generators),
        smallest_shared_safe_translation(structure_periods),
    )
