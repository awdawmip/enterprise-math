"""Prime-ladder stable macro construction for quotient-word compilers.

This module explores the large-state/high-root scaling regime with a fixed
budget ``s`` of optional composite macro types beyond the forced prime core.

Let ``q`` be the ``(s+1)``-st prime (zero-indexed: ``s=0 -> q=2``).  For each
smaller prime ``p<q`` choose the least exponent ``e`` with ``p**e >= q`` and
store the pure-power macro ``p**e``.  The resulting canonical macro family has
exactly ``s`` types.

For each compressed prime coordinate, fewer than ``e`` literal copies remain
after maximal block packing.  Collect those possible cheap residual slots:
``p`` repeated ``e-1`` times.  Sort all such slots as

    c_1 <= ... <= c_T < q.

Every other instruction in the canonical shortest word has multiplicative
value at least ``q``.  Therefore the predicted exact hard shell at cost ``k``
is

    M_s(k) = product(first min(k,T) cheap slots) * q**(k-min(k,T)).

In particular, once ``k>=T`` the shell obeys the exact tail recurrence

    M_s(k+1) = q * M_s(k),

so the stable execution-depth base is the next prime ``q``.

A converse asymptotic obstruction is immediate: with only ``s`` arbitrary
macro types, among the first ``s+1`` prime directions at least one prime has no
pure-power macro dedicated to it.  Its powers still require one literal prime
instruction per exponent token, so no ``s``-macro presentation can have stable
hard-shell base greater than the ``(s+1)``-st prime.

All multiplicative-basis and word-metric ingredients are prior mathematics.
This executable module is the quotient-root compiler specialization and a
regression oracle for the emerging Stage131 stable-resource law.
"""

from __future__ import annotations

from functools import lru_cache
from math import prod


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def first_primes(count: int) -> tuple[int, ...]:
    """Return the first ``count`` primes."""
    _require_natural("count", count)
    result: list[int] = []
    n = 2
    while len(result) < count:
        if _is_prime(n):
            result.append(n)
        n += 1
    return tuple(result)


def least_power_exponent_reaching(base: int, threshold: int) -> int:
    """Least positive ``e`` such that ``base**e >= threshold``."""
    if base < 2 or threshold < 2:
        raise ValueError("base and threshold must be at least 2")
    e = 1
    value = base
    while value < threshold:
        value *= base
        e += 1
    return e


def stable_macro_ladder(macro_budget: int) -> tuple[int, tuple[int, ...]]:
    """Return ``(stable_base, canonical_macros)`` for a macro budget.

    ``stable_base`` is the next prime ``q``.  The macros are the least pure
    prime powers reaching ``q`` for every smaller prime.
    """
    _require_natural("macro_budget", macro_budget)
    primes = first_primes(macro_budget + 1)
    q = primes[-1]
    macros = tuple(
        p ** least_power_exponent_reaching(p, q)
        for p in primes[:-1]
    )
    return q, macros


def stable_macro_ladder_cheap_slots(macro_budget: int) -> tuple[int, ...]:
    """Return sorted residual literal-prime slots below the stable base."""
    _require_natural("macro_budget", macro_budget)
    primes = first_primes(macro_budget + 1)
    q = primes[-1]
    slots: list[int] = []
    for p in primes[:-1]:
        exponent = least_power_exponent_reaching(p, q)
        slots.extend([p] * (exponent - 1))
    return tuple(sorted(slots))


def stable_macro_ladder_shell(macro_budget: int, cost: int) -> int:
    """Predicted exact hard-shell minimum at instruction cost ``cost``."""
    _require_natural("macro_budget", macro_budget)
    _require_natural("cost", cost)
    if cost == 0:
        return 1
    q, _ = stable_macro_ladder(macro_budget)
    cheap = stable_macro_ladder_cheap_slots(macro_budget)
    used = min(cost, len(cheap))
    return prod(cheap[:used], start=1) * q ** (cost - used)


def stable_macro_ladder_tail_data(macro_budget: int) -> tuple[int, int, int]:
    """Return ``(q,T,C)`` with tail shell ``C*q**(k-T)`` for ``k>=T``."""
    q, _ = stable_macro_ladder(macro_budget)
    cheap = stable_macro_ladder_cheap_slots(macro_budget)
    return q, len(cheap), prod(cheap, start=1)


def _prime_divisors(n: int) -> tuple[int, ...]:
    result: list[int] = []
    d = 2
    remaining = n
    while d * d <= remaining:
        if remaining % d == 0:
            result.append(d)
            while remaining % d == 0:
                remaining //= d
        d += 1
    if remaining > 1:
        result.append(remaining)
    return tuple(result)


def direct_shortest_ladder_word_length(n: int, macro_budget: int) -> int:
    """Independent exact shortest length over all primes plus ladder macros."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    _, macros = stable_macro_ladder(macro_budget)

    @lru_cache(maxsize=None)
    def visit(value: int) -> int:
        if value == 1:
            return 0
        options = [1 + visit(value // p) for p in _prime_divisors(value)]
        options.extend(
            1 + visit(value // macro)
            for macro in macros
            if value % macro == 0
        )
        return min(options)

    return visit(n)


def direct_stable_macro_ladder_shell(macro_budget: int, cost: int) -> int:
    """Brute-force the first integer whose exact ladder word length is ``cost``.

    Search stops at the closed-form predicted shell, making disagreement fail
    loudly rather than silently expanding an unbounded scan.
    """
    _require_natural("macro_budget", macro_budget)
    _require_natural("cost", cost)
    if cost == 0:
        return 1
    predicted = stable_macro_ladder_shell(macro_budget, cost)
    for n in range(2, predicted + 1):
        if direct_shortest_ladder_word_length(n, macro_budget) == cost:
            return n
    raise AssertionError("predicted ladder shell contained no cost-level witness")


def stable_macro_ladder_shell_matches_direct(macro_budget: int, cost: int) -> bool:
    """Cross-check closed-form shell against the independent shortest-word path."""
    return stable_macro_ladder_shell(
        macro_budget, cost
    ) == direct_stable_macro_ladder_shell(macro_budget, cost)
