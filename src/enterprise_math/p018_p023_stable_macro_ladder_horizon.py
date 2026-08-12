"""Exact finite-state horizon formulas for the stable macro prime ladder.

This companion module turns the shell oracle in
``p018_p023_stable_macro_ladder`` into an exact bounded-domain depth oracle.
For a fixed optional macro budget ``s`` let

    q = next prime,
    T = number of cheap residual literal-prime slots,
    C = product of all cheap residual slots.

The exact canonical shell is already given by ``stable_macro_ladder_shell``.
Once all cheap slots have been consumed (``k>=T``), it has the tail form

    M_s(k) = C * q**(k-T).

Hence, whenever ``N>=C``, the exact canonical ladder horizon is

    T + floor_log_q(floor(N/C)).

This is intentionally separate from the universal lower bound: the lower bound
holds for *every* presentation with at most ``s`` optional macros, whereas this
file evaluates one explicit canonical construction.
"""

from __future__ import annotations

from .p018_p023_stable_macro_ladder import (
    direct_shortest_ladder_word_length,
    stable_macro_ladder_shell,
    stable_macro_ladder_tail_data,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def floor_log(base: int, n: int) -> int:
    """Return the largest ``k`` with ``base**k <= n``."""
    if isinstance(base, bool) or not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer at least 2")
    _require_positive("n", n)
    exponent = 0
    power = 1
    while power * base <= n:
        power *= base
        exponent += 1
    return exponent


def stable_macro_ladder_required_horizon(max_state: int, macro_budget: int) -> int:
    """Exact canonical ladder horizon obtained from the exact shell sequence."""
    _require_natural("max_state", max_state)
    _require_natural("macro_budget", macro_budget)
    if max_state < 1:
        return 0
    horizon = 0
    while stable_macro_ladder_shell(macro_budget, horizon + 1) <= max_state:
        horizon += 1
    return horizon


def stable_macro_ladder_tail_horizon(max_state: int, macro_budget: int) -> int:
    """Closed-form exact horizon once the state bound reaches the tail core.

    Requires ``max_state >= C`` where ``(q,T,C)`` is returned by
    ``stable_macro_ladder_tail_data``.
    """
    _require_positive("max_state", max_state)
    _require_natural("macro_budget", macro_budget)
    q, transition, constant = stable_macro_ladder_tail_data(macro_budget)
    if max_state < constant:
        raise ValueError("tail formula requires max_state >= tail constant C")
    return transition + floor_log(q, max_state // constant)


def stable_macro_ladder_tail_formula_matches_shell(
    max_state: int, macro_budget: int
) -> bool:
    """Cross-check tail closed form against the independent shell scan."""
    return stable_macro_ladder_tail_horizon(
        max_state, macro_budget
    ) == stable_macro_ladder_required_horizon(max_state, macro_budget)


def direct_stable_macro_ladder_required_horizon(
    max_state: int, macro_budget: int
) -> int:
    """Independent direct bounded-state horizon from shortest-word search."""
    _require_natural("max_state", max_state)
    _require_natural("macro_budget", macro_budget)
    return max(
        (
            direct_shortest_ladder_word_length(boundary, macro_budget)
            for boundary in range(1, max_state + 1)
        ),
        default=0,
    )


def stable_macro_ladder_horizon_matches_direct(
    max_state: int, macro_budget: int
) -> bool:
    """Cross-check shell-derived horizon with direct per-target shortest words."""
    return stable_macro_ladder_required_horizon(
        max_state, macro_budget
    ) == direct_stable_macro_ladder_required_horizon(max_state, macro_budget)


def next_prime_log_lower_bound(max_state: int, macro_budget: int) -> int:
    """Universal next-prime logarithmic lower bound for any ``s``-macro ISA.

    This is the executable numeric side of the Lean obstruction theorem; it is
    not a claim that the canonical ladder always attains this lower bound
    exactly at finite state size.
    """
    _require_positive("max_state", max_state)
    _require_natural("macro_budget", macro_budget)
    q, _transition, _constant = stable_macro_ladder_tail_data(macro_budget)
    return floor_log(q, max_state)
