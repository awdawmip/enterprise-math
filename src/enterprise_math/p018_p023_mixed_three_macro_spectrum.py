"""Exact mixed exponent-cost geometry for the budget-three code ``{8,9,10}``.

The pure-power macro spectrum splits by prime direction.  The macro ``10=2*5``
breaks that product structure: it couples the 2-adic and 5-adic coordinates.
This module records the exact finite-dimensional replacement.

For ``A=v_2(n)`` and ``C=v_5(n)``, using ``z`` copies of 10 leaves ``A-z``
two-tokens and ``C-z`` five-tokens.  The remaining two-tokens are encoded by
literal 2s and ``8=2^3``; the exact cost for exponent ``a`` is
``a//3 + a%3``.  Hence

    cost_25(A,C)
      = min_{0 <= z <= min(A,C)}
          z + ((A-z)//3 + (A-z)%3) + (C-z).

The 3-adic coordinate is independent and has exact cost ``B//2+B%2`` because
``9=3^2`` is available.  All prime factors above five remain literal.

The resulting hard shell has two internal phases:

* costs 3 through 8: ``12 * 7^(k-3)``;
* costs at least 9: ``3 * 5^(k-1)``.

Thus the same fixed ISA changes its controlling hard direction before the
budget-three *optimizer* later changes from the mixed code to the stable pure
q=7 ladder ``{8,9,25}``.

All number-theoretic ingredients here are elementary factorization and finite
coin optimization.  This is an executable theorem-discovery/regression oracle,
not a novelty claim.
"""

from __future__ import annotations

from functools import lru_cache


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _prime_factorization(n: int) -> dict[int, int]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    x = n
    p = 2
    out: dict[int, int] = {}
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def two_block_three_cost(exponent: int) -> int:
    """Exact exponent cost with block sizes 1 and 3 (literal 2 and macro 8)."""
    _require_natural("exponent", exponent)
    return exponent // 3 + exponent % 3


def three_block_two_cost(exponent: int) -> int:
    """Exact exponent cost with block sizes 1 and 2 (literal 3 and macro 9)."""
    _require_natural("exponent", exponent)
    return exponent // 2 + exponent % 2


def two_five_mixed_cost(v2: int, v5: int) -> int:
    """Exact coupled cost for 2/5 exponents under literal 2,5 and macros 8,10."""
    _require_natural("v2", v2)
    _require_natural("v5", v5)
    return min(
        z + two_block_three_cost(v2 - z) + (v5 - z)
        for z in range(min(v2, v5) + 1)
    )


def prime_eight_nine_ten_cost(n: int) -> int:
    """Exact shortest word length over all literal primes plus macros 8,9,10."""
    factors = _prime_factorization(n)
    v2 = factors.pop(2, 0)
    v3 = factors.pop(3, 0)
    v5 = factors.pop(5, 0)
    residual_literals = sum(factors.values())
    return (
        two_five_mixed_cost(v2, v5)
        + three_block_two_cost(v3)
        + residual_literals
    )


def prime_eight_nine_ten_hard_shell(cost: int) -> int:
    """Closed form for the least positive integer of exact ``{8,9,10}`` cost."""
    _require_natural("cost", cost)
    if cost == 0:
        return 1
    if cost == 1:
        return 2
    if cost == 2:
        return 4
    if cost <= 8:
        return 12 * 7 ** (cost - 3)
    return 3 * 5 ** (cost - 1)


def prime_eight_nine_ten_first_fail(horizon: int) -> int:
    """First state needing more than ``horizon`` instructions."""
    _require_natural("horizon", horizon)
    return prime_eight_nine_ten_hard_shell(horizon + 1)


def _omega(n: int) -> int:
    return sum(_prime_factorization(n).values())


@lru_cache(maxsize=None)
def direct_shortest_word_length(n: int) -> int:
    """Independent recursion for primes plus 8,9,10, used only as a check."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0
    best = _omega(n)
    for macro in (8, 9, 10):
        if n % macro == 0:
            best = min(best, 1 + direct_shortest_word_length(n // macro))
    return best


def formula_matches_direct(limit: int) -> bool:
    """Cross-check the closed pointwise cost against the independent recursion."""
    _require_natural("limit", limit)
    return all(
        prime_eight_nine_ten_cost(n) == direct_shortest_word_length(n)
        for n in range(1, limit + 1)
    )


def shell_matches_scan(max_cost: int) -> bool:
    """Cross-check shell values by one monotone integer scan."""
    _require_natural("max_cost", max_cost)
    if max_cost == 0:
        return True
    targets = {
        k: prime_eight_nine_ten_hard_shell(k)
        for k in range(1, max_cost + 1)
    }
    first: dict[int, int] = {}
    limit = max(targets.values())
    for n in range(1, limit + 1):
        c = prime_eight_nine_ten_cost(n)
        if 1 <= c <= max_cost and c not in first:
            first[c] = n
    return all(first.get(k) == value for k, value in targets.items())


# Cheap import-time regression points expose both internal shell phases.
assert two_five_mixed_cost(2, 0) == 2
assert two_five_mixed_cost(3, 0) == 1
assert two_five_mixed_cost(1, 1) == 1
assert prime_eight_nine_ten_hard_shell(7) == 28_812
assert prime_eight_nine_ten_hard_shell(8) == 201_684
assert prime_eight_nine_ten_hard_shell(9) == 1_171_875
assert prime_eight_nine_ten_hard_shell(10) == 5_859_375
