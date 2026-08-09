"""Minimal bounded future-action basis for quotient-root observations.

Fix a positive root order ``r`` and the observation family

    O_a(q) = R_r(floor(q/a)),    a >= 1.

On the bounded exact state domain ``0 <= q <= N``, the full positive action
family is far larger than necessary.  The unique inclusion-minimal action set
whose joint signatures separate every exact state is precisely the set of
``r``-th-power-free positive integers up to ``N``.

The key local boundary fact is exact: action ``a`` distinguishes adjacent
states ``q-1`` and ``q`` iff

    q = a * t**r

for some positive integer ``t``.  Hence every ``r``-power-free boundary ``b``
forces action ``a=b`` itself, while every other boundary is covered by the
power-free kernel in its canonical decomposition ``q = b*t**r``.

This module is an integer-only executable specification for the P018/P023
bridge.  Classical power-free decomposition is prior mathematics; historical
novelty of the future-action-basis packaging is unverified.
"""

from __future__ import annotations

from collections.abc import Iterable

from .core import integer_nth_root


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def is_r_power_free(n: int, root_exp: int) -> bool:
    """Return whether ``n`` is not divisible by any nontrivial ``r``-th power."""
    _require_positive("n", n)
    _require_positive("root_exp", root_exp)

    if root_exp == 1:
        return n == 1

    t = 2
    while t**root_exp <= n:
        if n % (t**root_exp) == 0:
            return False
        t += 1
    return True


def r_power_free_kernel(n: int, root_exp: int) -> int:
    """Return the canonical ``r``-power-free kernel ``b`` in ``n=b*t**r``."""
    _require_positive("n", n)
    _require_positive("root_exp", root_exp)

    if root_exp == 1:
        return 1

    remaining = n
    kernel = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            kernel *= prime ** (exponent % root_exp)
        prime = 3 if prime == 2 else prime + 2

    if remaining > 1:
        kernel *= remaining
    return kernel


def root_quotient_observation(q: int, action: int, root_exp: int) -> int:
    """Return ``R_r(floor(q/action))`` with exact integer semantics."""
    _require_natural("q", q)
    _require_positive("action", action)
    _require_positive("root_exp", root_exp)
    return integer_nth_root(q // action, root_exp)


def adjacent_boundary_actions(q: int, root_exp: int) -> tuple[int, ...]:
    """Return all actions that distinguish the adjacent boundary ``q-1 | q``.

    The returned actions are exactly ``q/t**r`` over positive ``t`` for which
    ``t**r`` divides ``q``.
    """
    _require_positive("q", q)
    _require_positive("root_exp", root_exp)

    actions: set[int] = set()
    top = integer_nth_root(q, root_exp)
    for t in range(1, top + 1):
        power = t**root_exp
        if q % power == 0:
            actions.add(q // power)
    return tuple(sorted(actions))


def action_distinguishes_adjacent_boundary(q: int, action: int, root_exp: int) -> bool:
    """Return whether one action distinguishes exact states ``q-1`` and ``q``."""
    _require_positive("q", q)
    _require_positive("action", action)
    _require_positive("root_exp", root_exp)
    return root_quotient_observation(q - 1, action, root_exp) != root_quotient_observation(
        q, action, root_exp
    )


def minimal_root_quotient_action_basis(max_state: int, root_exp: int) -> tuple[int, ...]:
    """Return the unique inclusion-minimal exact action basis on ``[0,N]``."""
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    return tuple(
        b for b in range(1, max_state + 1) if is_r_power_free(b, root_exp)
    )


def root_quotient_signature(
    q: int, actions: Iterable[int], root_exp: int
) -> tuple[int, ...]:
    """Return the joint quotient-root observation signature for ``q``."""
    _require_natural("q", q)
    _require_positive("root_exp", root_exp)
    normalized = tuple(actions)
    for action in normalized:
        _require_positive("action", action)
    return tuple(root_quotient_observation(q, action, root_exp) for action in normalized)


def action_basis_separates_bounded_domain(
    max_state: int, root_exp: int, actions: Iterable[int]
) -> bool:
    """Return whether the action signatures are injective on ``0,...,N``."""
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    normalized = tuple(dict.fromkeys(actions))
    for action in normalized:
        _require_positive("action", action)

    seen: set[tuple[int, ...]] = set()
    for q in range(max_state + 1):
        signature = root_quotient_signature(q, normalized, root_exp)
        if signature in seen:
            return False
        seen.add(signature)
    return True


def contains_forced_power_free_basis(
    max_state: int, root_exp: int, actions: Iterable[int]
) -> bool:
    """Check the exact theorem criterion for bounded signature injectivity."""
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    action_set = set(actions)
    for action in action_set:
        _require_positive("action", action)
    return set(minimal_root_quotient_action_basis(max_state, root_exp)) <= action_set
