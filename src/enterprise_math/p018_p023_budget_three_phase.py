"""Exact finite optimizer certificate for optional macro budget three.

This module implements the structural reduction proved on the Lean side rather
than brute-forcing arbitrary triples.

At every state threshold relevant to the budget-three phases, pure-prime
directions 2 and 3 are hard.  Hence any separator with at most three optional
composite macros contains a pure power ``2**a`` and a pure power ``3**b``.
There is at most one spare macro ``g``.

For a fixed pure pair, let ``t`` be its first horizon-hard target.  If adjoining
``g`` improves that first failure then ``g`` must divide ``t``.  This is the
executable counterpart of ``RootQuotientSpareMacroDivisibility.lean`` and
reduces the third-slot search to the composite divisors of one integer.

The finite classification discovered with this exact reduction is:

* h=2: first fail 32, optimizers {4,6,9} and {4,6,27};
* h=3,4: first fail 6*5^(h-1), optimizer {4,8,9};
* h=5,6,7: first fail 12*7^(h-2), optimizer {8,9,10};
* h=8: first fail 3*5^8, optimizer {8,9,10};
* h=9: first fail 60*7^6, optimizer {8,9,25}.

From h>=10 the stable {8,9,25} law is no longer merely executable: the
arbitrary-macro lower bound is proof-shaped Lean in
``RootQuotientThreeMacroStableOptimality.lean``.

This file makes no novelty claim; it is a finite theorem-discovery/regression
oracle.
"""

from __future__ import annotations

from functools import lru_cache
from math import isqrt, prod


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


@lru_cache(maxsize=None)
def _factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    x = n
    d = 2
    out: list[tuple[int, int]] = []
    while d * d <= x:
        e = 0
        while x % d == 0:
            x //= d
            e += 1
        if e:
            out.append((d, e))
        d += 1
    if x > 1:
        out.append((x, 1))
    return tuple(out)


def _valuation(n: int, p: int) -> int:
    return dict(_factorization(n)).get(p, 0)


def _omega(n: int) -> int:
    return sum(e for _p, e in _factorization(n))


def pure_pair_cost(n: int, exp_two: int, exp_three: int) -> int:
    """Exact word cost over primes plus ``2^a`` and ``3^b``."""
    if exp_two < 2 or exp_three < 2:
        raise ValueError("pure macro exponents must be at least two")
    v2 = _valuation(n, 2)
    v3 = _valuation(n, 3)
    return (
        _omega(n)
        - (exp_two - 1) * (v2 // exp_two)
        - (exp_three - 1) * (v3 // exp_three)
    )


def pure_pair_hard_shell(exp_two: int, exp_three: int, cost: int) -> int:
    """Exact hard shell from merged directional marginal-price streams."""
    _require_natural("cost", cost)
    if exp_two < 2 or exp_three < 2:
        raise ValueError("pure macro exponents must be at least two")
    prices = (
        [2] * (exp_two - 1)
        + [3] * (exp_three - 1)
        + [2 ** exp_two] * cost
        + [3 ** exp_three] * cost
        + [5] * cost
    )
    prices.sort()
    return prod(prices[:cost], start=1)


def composite_divisors(n: int) -> tuple[int, ...]:
    """Composite divisors at least four."""
    result: set[int] = set()
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            for value in (d, n // d):
                if value >= 4 and not _is_prime(value):
                    result.add(value)
    if n >= 4 and not _is_prime(n):
        result.add(n)
    return tuple(sorted(result))


def pair_plus_spare_cost(n: int, exp_two: int, exp_three: int, spare: int) -> int:
    """Exact cost after adjoining one arbitrary spare macro.

    Any word uses ``j`` copies of the spare macro and then a shortest word over
    the pure pair.  Multiplicative commutativity makes the formula exact.
    """
    if spare < 4 or _is_prime(spare):
        raise ValueError("spare must be composite")
    best = pure_pair_cost(n, exp_two, exp_three)
    quotient = n
    copies = 0
    while quotient % spare == 0:
        quotient //= spare
        copies += 1
        best = min(
            best,
            copies + pure_pair_cost(quotient, exp_two, exp_three),
        )
    return best


def first_fail_pair_plus_spare(
    horizon: int,
    exp_two: int,
    exp_three: int,
    spare: int,
    *,
    limit: int,
) -> int:
    """First exact failure, assuming ``limit`` reaches the desired certificate."""
    _require_natural("horizon", horizon)
    _require_natural("limit", limit)
    for n in range(2, limit + 1):
        if pair_plus_spare_cost(n, exp_two, exp_three, spare) > horizon:
            return n
    return limit + 1


def spare_candidates_from_first_pair_failure(
    horizon: int, exp_two: int, exp_three: int
) -> tuple[int, ...]:
    """Complete third-slot candidate set for any strict improvement of the pair."""
    first_fail = pure_pair_hard_shell(exp_two, exp_three, horizon + 1)
    macro_two = 2 ** exp_two
    macro_three = 3 ** exp_three
    return tuple(
        g
        for g in composite_divisors(first_fail)
        if g not in (macro_two, macro_three)
    )


def budget_three_phase_prediction(horizon: int) -> tuple[int, tuple[tuple[int, ...], ...]]:
    """Current exact finite/global classification by horizon."""
    _require_natural("horizon", horizon)
    if horizon < 2:
        raise ValueError("classification starts at horizon two")
    if horizon == 2:
        return 32, ((4, 6, 9), (4, 6, 27))
    if horizon <= 4:
        return 6 * 5 ** (horizon - 1), ((4, 8, 9),)
    if horizon <= 7:
        return 12 * 7 ** (horizon - 2), ((8, 9, 10),)
    if horizon == 8:
        return 3 * 5 ** 8, ((8, 9, 10),)
    return 60 * 7 ** (horizon - 3), ((8, 9, 25),)


def repair_kernel_below(
    horizon: int,
    exp_two: int,
    exp_three: int,
    state_threshold: int,
) -> tuple[int, int]:
    """GCD and count of pure-pair hard targets strictly below a threshold."""
    from math import gcd

    _require_natural("horizon", horizon)
    _require_natural("state_threshold", state_threshold)
    kernel = 0
    count = 0
    for n in range(2, state_threshold):
        if pure_pair_cost(n, exp_two, exp_three) > horizon:
            kernel = gcd(kernel, n)
            count += 1
    return kernel, count


# Cheap phase-boundary regressions.
assert budget_three_phase_prediction(2)[0] == 32
assert budget_three_phase_prediction(3)[0] == 150
assert budget_three_phase_prediction(4)[0] == 750
assert budget_three_phase_prediction(5)[0] == 4_116
assert budget_three_phase_prediction(6)[0] == 28_812
assert budget_three_phase_prediction(7)[0] == 201_684
assert budget_three_phase_prediction(8)[0] == 1_171_875
assert budget_three_phase_prediction(9)[0] == 7_058_940
