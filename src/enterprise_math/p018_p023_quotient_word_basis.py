"""Finite quotient-word generator languages for quotient-root observations.

Fix root order ``r>=1`` and primitive positive quotient generators ``G``.
A literal word ``(a1,...,am)`` acts by successive floor quotients. Exact floor
arithmetic flattens the word to one denominator product:

    (...((q//a1)//a2)...//am) = q//(a1*...*am).

Combining this with the canonical bounded power-free action-basis theorem gives
an exact finite-horizon language criterion: words of length at most ``h``
separate all exact states ``0,...,N`` iff their reachable denominator products
contain every positive ``r``-power-free integer at most ``N``.

Classical multiplicative bases are prior mathematics. This module is only an
integer-only executable specification of the quotient-root specialization.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from .p018_p023_power_free_action_basis import (
    action_basis_separates_bounded_domain,
    is_r_power_free,
    minimal_root_quotient_action_basis,
    root_quotient_observation,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def normalize_positive_generators(generators: Iterable[int]) -> tuple[int, ...]:
    """Return sorted distinct positive primitive quotient generators."""
    normalized = tuple(sorted(set(generators)))
    for value in normalized:
        _require_positive("generator", value)
    return normalized


def quotient_word_product(word: Sequence[int]) -> int:
    """Return the denominator product compiled from one quotient word."""
    product = 1
    for action in word:
        _require_positive("action", action)
        product *= action
    return product


def quotient_word_state(q: int, word: Sequence[int]) -> int:
    """Execute successive exact floor quotients literally."""
    _require_natural("q", q)
    state = q
    for action in word:
        _require_positive("action", action)
        state //= action
    return state


def reachable_quotient_products(
    generators: Iterable[int], horizon: int, *, max_product: int | None = None
) -> tuple[int, ...]:
    """Return products reachable by words of length at most ``horizon``.

    The empty word contributes denominator 1. ``max_product`` may be used to
    prune products that cannot distinguish states in a bounded domain.
    """
    _require_natural("horizon", horizon)
    if max_product is not None:
        _require_natural("max_product", max_product)
    gens = normalize_positive_generators(generators)

    reachable = {1}
    frontier = {1}
    for _ in range(horizon):
        frontier = {
            product * action
            for product in frontier
            for action in gens
            if max_product is None or product * action <= max_product
        }
        reachable.update(frontier)
        if not frontier:
            break
    return tuple(sorted(reachable))


def quotient_word_language_covers_power_free_boundaries(
    max_state: int, root_exp: int, generators: Iterable[int], horizon: int
) -> bool:
    """Check the exact multiplicative-coverage side of the bridge theorem."""
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    _require_natural("horizon", horizon)
    reachable = set(
        reachable_quotient_products(generators, horizon, max_product=max_state)
    )
    required = set(minimal_root_quotient_action_basis(max_state, root_exp))
    return required <= reachable


def quotient_word_language_separates_bounded_domain(
    max_state: int, root_exp: int, generators: Iterable[int], horizon: int
) -> bool:
    """Check exact state separation using the effective reachable products."""
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    _require_natural("horizon", horizon)
    products = reachable_quotient_products(
        generators, horizon, max_product=max_state
    )
    return action_basis_separates_bounded_domain(max_state, root_exp, products)


def prime_generator_basis(max_state: int) -> tuple[int, ...]:
    """Return all primes at most ``max_state`` by elementary trial division."""
    _require_natural("max_state", max_state)
    primes: list[int] = []
    for candidate in range(2, max_state + 1):
        is_prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            primes.append(candidate)
    return tuple(primes)


def omega_with_multiplicity(n: int) -> int:
    """Return the total number of prime factors of ``n``, with multiplicity."""
    _require_positive("n", n)
    remaining = n
    count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            remaining //= divisor
            count += 1
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        count += 1
    return count


def prime_generator_required_horizon(max_state: int, root_exp: int) -> int:
    """Exact horizon needed by the bounded prime generator set.

    This is ``max Omega(b)`` over positive ``r``-power-free ``b<=N``. The
    empty word covers boundary/action 1 with length zero.
    """
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    return max(
        (
            omega_with_multiplicity(b)
            for b in range(1, max_state + 1)
            if is_r_power_free(b, root_exp)
        ),
        default=0,
    )


def binary_present_observation_regime(max_state: int, root_exp: int) -> bool:
    """Return whether ``N < 2^r``, the two-class present-root regime."""
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    return max_state < 2**root_exp


def direct_quotient_word_signature(
    q: int, root_exp: int, words: Iterable[Sequence[int]]
) -> tuple[int, ...]:
    """Reference-only literal-word signature for small regression domains."""
    _require_natural("q", q)
    _require_positive("root_exp", root_exp)
    signature = []
    for word in words:
        state = quotient_word_state(q, word)
        signature.append(root_quotient_observation(state, 1, root_exp))
    return tuple(signature)
