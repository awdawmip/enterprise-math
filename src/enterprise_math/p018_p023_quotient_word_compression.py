"""Multiplicative compression geometry for bounded quotient-word languages.

Assume root order ``r>=2`` and keep every bounded prime quotient generator.
Additional composite generators act as macro instructions.

For one positive boundary ``b``, every use of a composite generator ``g``
replaces ``Omega(g)`` prime actions by one macro action.  If a multiset of
macros packs into the prime-exponent vector of ``b``, its exact saving is

    sum_g (Omega(g)-1) x_g.

The shortest word over ``primes union macros`` is therefore exactly

    Omega(b) - max_packing_saving(b, macros).

This makes finite-horizon separation a packing inequality on every bounded
r-power-free boundary.  At the penultimate prime horizon L_r(N)-1 it collapses
further to a set-cover problem on the maximal-Omega boundaries by
power-free semiprime divisors.

All prime-factor, packing, and finite set-cover ingredients are prior
mathematics.  This module is only the quotient-root specialization.
"""

from __future__ import annotations

from itertools import combinations
from collections.abc import Iterable

from .p018_p023_power_free_action_basis import (
    is_r_power_free,
    minimal_root_quotient_action_basis,
)
from .p018_p023_quotient_word_basis import (
    omega_with_multiplicity,
    prime_generator_basis,
    prime_generator_required_horizon,
    quotient_word_language_separates_bounded_domain,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_root_exp(root_exp: int) -> None:
    if isinstance(root_exp, bool) or not isinstance(root_exp, int) or root_exp < 2:
        raise ValueError("root_exp must be an integer at least 2")


def prime_exponent_vector(n: int) -> tuple[tuple[int, int], ...]:
    """Return the exact prime-exponent vector of a positive integer."""
    _require_positive("n", n)
    remaining = n
    divisor = 2
    result: list[tuple[int, int]] = []
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            result.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result.append((remaining, 1))
    return tuple(result)


def normalize_composite_macros(macros: Iterable[int]) -> tuple[int, ...]:
    """Return sorted distinct composite macro generators."""
    normalized = tuple(sorted(set(macros)))
    for value in normalized:
        _require_positive("macro", value)
        factors = prime_exponent_vector(value)
        if value < 4 or (len(factors) == 1 and factors[0][1] == 1):
            raise ValueError("macro generators must be composite")
    return normalized


def macro_compression_weight(macro: int) -> int:
    """Exact number of prime actions saved by one use of ``macro``."""
    _require_positive("macro", macro)
    total = omega_with_multiplicity(macro)
    if total < 2:
        raise ValueError("macro must be composite")
    return total - 1


def max_macro_compression(boundary: int, macros: Iterable[int]) -> int:
    """Maximum exact prime-action saving obtainable inside ``boundary``.

    A macro can be used repeatedly, but the total consumed prime exponents may
    not exceed the exponent vector of ``boundary``.
    """
    _require_positive("boundary", boundary)
    normalized = normalize_composite_macros(macros)
    boundary_exp = dict(prime_exponent_vector(boundary))

    usable: list[tuple[dict[int, int], int]] = []
    for macro in normalized:
        if boundary % macro != 0:
            continue
        usable.append(
            (dict(prime_exponent_vector(macro)), macro_compression_weight(macro))
        )

    best = 0

    def visit(index: int, remaining: dict[int, int], saving: int) -> None:
        nonlocal best
        if index == len(usable):
            best = max(best, saving)
            return
        exponents, weight = usable[index]
        max_uses = min(
            (remaining.get(prime, 0) // exponent for prime, exponent in exponents.items()),
            default=0,
        )
        for count in range(max_uses + 1):
            next_remaining = remaining.copy()
            for prime, exponent in exponents.items():
                next_remaining[prime] -= count * exponent
            visit(index + 1, next_remaining, saving + count * weight)

    visit(0, boundary_exp, 0)
    return best


def shortest_prime_macro_word_length(
    boundary: int, macros: Iterable[int]
) -> int:
    """Exact shortest product-word length over bounded primes plus ``macros``."""
    _require_positive("boundary", boundary)
    return omega_with_multiplicity(boundary) - max_macro_compression(
        boundary, macros
    )


def prime_macro_language_separates_at_horizon(
    max_state: int, root_exp: int, macros: Iterable[int], horizon: int
) -> bool:
    """Check the exact packing criterion for bounded quotient-root separation."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    normalized = normalize_composite_macros(macros)
    return all(
        shortest_prime_macro_word_length(boundary, normalized) <= horizon
        for boundary in minimal_root_quotient_action_basis(max_state, root_exp)
        if boundary >= 2
    )


def maximal_omega_power_free_boundaries(
    max_state: int, root_exp: int
) -> tuple[int, ...]:
    """Return bounded power-free boundaries attaining the prime-only horizon."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    level = prime_generator_required_horizon(max_state, root_exp)
    return tuple(
        boundary
        for boundary in minimal_root_quotient_action_basis(max_state, root_exp)
        if boundary >= 2 and omega_with_multiplicity(boundary) == level
    )


def power_free_semiprime_candidates(
    max_state: int, root_exp: int
) -> tuple[int, ...]:
    """Return bounded r-power-free integers with total prime multiplicity two."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    return tuple(
        value
        for value in range(4, max_state + 1)
        if omega_with_multiplicity(value) == 2
        and is_r_power_free(value, root_exp)
    )


def semiprime_covers_maximal_boundaries(
    max_state: int, root_exp: int, semiprimes: Iterable[int]
) -> bool:
    """Check the exact penultimate-horizon set-cover condition."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    chosen = tuple(sorted(set(semiprimes)))
    candidates = set(power_free_semiprime_candidates(max_state, root_exp))
    if not set(chosen) <= candidates:
        raise ValueError("every selected value must be a bounded power-free semiprime")
    maxima = maximal_omega_power_free_boundaries(max_state, root_exp)
    return all(any(boundary % d == 0 for d in chosen) for boundary in maxima)


def minimum_penultimate_semiprime_cover(
    max_state: int, root_exp: int
) -> tuple[int, ...]:
    """Return one minimum semiprime cover of maximal-Omega boundaries.

    This is an exact finite oracle, not a polynomial-time complexity claim.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    level = prime_generator_required_horizon(max_state, root_exp)
    if level <= 1:
        return ()
    candidates = power_free_semiprime_candidates(max_state, root_exp)
    for size in range(len(candidates) + 1):
        for chosen in combinations(candidates, size):
            if semiprime_covers_maximal_boundaries(
                max_state, root_exp, chosen
            ):
                return chosen
    raise AssertionError("maximal boundary semiprime cover must exist when level>=2")


def penultimate_minimum_extra_count(max_state: int, root_exp: int) -> int:
    """Exact minimum number of composite macros at horizon L_r(N)-1."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    level = prime_generator_required_horizon(max_state, root_exp)
    if level <= 1:
        return 0
    return len(minimum_penultimate_semiprime_cover(max_state, root_exp))


def binary_penultimate_single_macro_solutions(
    max_state: int, root_exp: int
) -> tuple[int, ...]:
    """Exact one-macro minimum alphabets in the binary present-root regime.

    Let ``L=floor(log2 N)>=3`` and assume ``N<2^r``.  At horizon ``L-1``,
    primes alone fail but one composite macro suffices.  The complete list of
    single macros is

    * ``2^j`` for ``2<=j<=L`` if ``N < 3*2^(L-1)``;
    * ``2^j`` for ``2<=j<=L-1`` otherwise.

    The only boundaries with Omega exactly L below ``2^(L+1)`` are ``2^L``
    and, when present, ``3*2^(L-1)``.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    if max_state >= 2**root_exp:
        raise ValueError("binary present-root regime requires max_state < 2^root_exp")
    if max_state < 8:
        raise ValueError("penultimate one-macro theorem requires floor(log2 N)>=3")
    level = max_state.bit_length() - 1
    threshold = 3 * 2 ** (level - 1)
    largest_exponent = level if max_state < threshold else level - 1
    return tuple(2**exponent for exponent in range(2, largest_exponent + 1))


def direct_prime_macro_separator(
    max_state: int, root_exp: int, macros: Iterable[int], horizon: int
) -> bool:
    """Independent bridge to the literal reachable-product separator."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    normalized = normalize_composite_macros(macros)
    generators = prime_generator_basis(max_state) + normalized
    return quotient_word_language_separates_bounded_domain(
        max_state, root_exp, generators, horizon
    )


def omega_filtered_macro_alphabet(
    max_state: int, root_exp: int, macro_capacity: int
) -> tuple[int, ...]:
    """Canonical nested macro alphabet with at most ``macro_capacity`` primes.

    Every generator is a nontrivial bounded r-power-free semantic action whose
    total prime multiplicity is at most ``macro_capacity``.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_positive("macro_capacity", macro_capacity)
    return tuple(
        boundary
        for boundary in minimal_root_quotient_action_basis(max_state, root_exp)
        if boundary >= 2
        and omega_with_multiplicity(boundary) <= macro_capacity
    )


def omega_filtered_boundary_word_length(
    boundary: int, macro_capacity: int
) -> int:
    """Exact shortest length under the Omega-filtered macro alphabet.

    For an r-power-free boundary, partition its prime multiset into blocks of
    size at most ``macro_capacity``.  Every block product remains an
    r-power-free divisor, while no generator can contribute more than
    ``macro_capacity`` prime factors.
    """
    _require_positive("boundary", boundary)
    _require_positive("macro_capacity", macro_capacity)
    total = omega_with_multiplicity(boundary)
    return (total + macro_capacity - 1) // macro_capacity


def omega_filtered_required_horizon(
    max_state: int, root_exp: int, macro_capacity: int
) -> int:
    """Exact worst composition horizon of the Omega-filtered alphabet."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_positive("macro_capacity", macro_capacity)
    prime_horizon = prime_generator_required_horizon(max_state, root_exp)
    return (prime_horizon + macro_capacity - 1) // macro_capacity


def omega_filtered_separates_at_horizon(
    max_state: int,
    root_exp: int,
    macro_capacity: int,
    horizon: int,
) -> bool:
    """Exact storage-depth product law for the canonical Omega filtration."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_positive("macro_capacity", macro_capacity)
    _require_natural("horizon", horizon)
    prime_horizon = prime_generator_required_horizon(max_state, root_exp)
    return macro_capacity * horizon >= prime_horizon


def omega_filtered_composite_macros(
    max_state: int, root_exp: int, macro_capacity: int
) -> tuple[int, ...]:
    """Composite part of the canonical Omega-filtered alphabet."""
    alphabet = omega_filtered_macro_alphabet(
        max_state, root_exp, macro_capacity
    )
    primes = set(prime_generator_basis(max_state))
    return tuple(value for value in alphabet if value not in primes)
