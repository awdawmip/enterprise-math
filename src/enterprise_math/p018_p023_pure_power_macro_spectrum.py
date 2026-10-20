"""Pure-prime-power macro spectra for quotient-word compilers.

A pure-power macro family contains only generators ``p**e`` supported on a
single prime direction.  Because such macros never mix prime-factor
coordinates, exact word length splits into independent exponent coin problems.

For each prime ``p``, let ``D_p`` be the set of available exponent blocks:
``1`` for the literal prime together with every macro exponent ``e`` for which
``p**e`` is stored.  The directional cost of exponent ``a`` is the minimum
number of coins from ``D_p`` summing to ``a``.

The directional hard-shell sequence records the smallest ``p**a`` whose exact
coin cost is ``k``.  Its multiplicative successive ratios are the directional
``marginal prices``.  The global hard shell for a pure-power ISA is obtained by
merging all directional marginal-price streams and multiplying the ``k``
smallest prices.  Uncompressed prime directions contribute the constant stream
``p,p,p,...``.

This executable oracle makes the finite transient/stable code-design phases
visible without committing the Lean layer to a general coin-system library.
It is cross-checked against an independent shortest-product recursion.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
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


def _factor_prime_power(n: int) -> tuple[int, int] | None:
    """Return ``(p,e)`` iff ``n=p**e`` with prime ``p`` and ``e>=1``."""
    if n < 2:
        return None
    for p in range(2, n + 1):
        if not _is_prime(p):
            continue
        value = p
        e = 1
        while value < n:
            value *= p
            e += 1
        if value == n:
            return p, e
        if p * p > n:
            break
    return None


def first_primes(count: int) -> tuple[int, ...]:
    _require_natural("count", count)
    out: list[int] = []
    n = 2
    while len(out) < count:
        if _is_prime(n):
            out.append(n)
        n += 1
    return tuple(out)


def normalize_pure_power_macros(macros) -> tuple[int, ...]:
    normalized = tuple(sorted(set(macros)))
    for macro in normalized:
        pp = _factor_prime_power(macro)
        if pp is None or pp[1] < 2:
            raise ValueError("every macro must be a composite prime power")
    return normalized


def exponent_denominations(macros, prime: int) -> tuple[int, ...]:
    """Available exponent-block sizes along one prime direction."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    normalized = normalize_pure_power_macros(macros)
    exponents = {1}
    for macro in normalized:
        p, e = _factor_prime_power(macro)  # type: ignore[misc]
        if p == prime:
            exponents.add(e)
    return tuple(sorted(exponents))


def exponent_coin_cost(exponent: int, denominations) -> int:
    """Exact unbounded coin cost of one prime exponent."""
    _require_natural("exponent", exponent)
    denoms = tuple(sorted(set(denominations)))
    if not denoms or denoms[0] != 1:
        raise ValueError("denominations must contain 1")
    cost = [0] + [exponent + 1] * exponent
    for a in range(1, exponent + 1):
        cost[a] = 1 + min(cost[a - d] for d in denoms if d <= a)
    return cost[exponent]


def directional_shell_exponent(macros, prime: int, cost: int) -> int:
    """Smallest exponent with exact directional word cost ``cost``."""
    _require_natural("cost", cost)
    if cost == 0:
        return 0
    denoms = exponent_denominations(macros, prime)
    # A witness always occurs before (max denomination)*cost + cost.
    upper = max(denoms) * cost + cost
    for exponent in range(1, upper + 1):
        if exponent_coin_cost(exponent, denoms) == cost:
            return exponent
    raise AssertionError("directional shell witness not found")


def directional_marginal_prices(macros, prime: int, count: int) -> tuple[int, ...]:
    """First ``count`` multiplicative increments of the directional shell."""
    _require_natural("count", count)
    if count == 0:
        return ()
    exponents = [directional_shell_exponent(macros, prime, k) for k in range(count + 1)]
    return tuple(prime ** (exponents[k] - exponents[k - 1]) for k in range(1, count + 1))


def pure_power_macro_spectrum(macros, count: int) -> tuple[int, ...]:
    """First ``count`` global marginal prices for a pure-power ISA.

    It is enough to include the first ``count + number_of_macro_primes + 2``
    prime directions: later literal primes are too large to enter the prefix.
    """
    _require_natural("count", count)
    normalized = normalize_pure_power_macros(macros)
    macro_primes = {_factor_prime_power(m)[0] for m in normalized}  # type: ignore[index]
    primes = first_primes(count + len(macro_primes) + 2)
    streams: list[int] = []
    for p in primes:
        streams.extend(directional_marginal_prices(normalized, p, count))
    return tuple(sorted(streams)[:count])


def pure_power_macro_shell(macros, cost: int) -> int:
    """Closed spectral hard shell: product of the first ``cost`` prices."""
    _require_natural("cost", cost)
    return prod(pure_power_macro_spectrum(macros, cost), start=1)


def _prime_divisors(n: int) -> tuple[int, ...]:
    x = n
    d = 2
    out: list[int] = []
    while d * d <= x:
        if x % d == 0:
            out.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        out.append(x)
    return tuple(out)


def direct_shortest_word_length(n: int, macros) -> int:
    """Independent exact shortest word length over all primes plus macros."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    normalized = normalize_pure_power_macros(macros)

    @lru_cache(maxsize=None)
    def visit(value: int) -> int:
        if value == 1:
            return 0
        options = [1 + visit(value // p) for p in _prime_divisors(value)]
        options.extend(1 + visit(value // m) for m in normalized if value % m == 0)
        return min(options)

    return visit(n)


def direct_pure_power_macro_shell(macros, cost: int) -> int:
    """Brute-force the first integer of exact word cost ``cost``."""
    predicted = pure_power_macro_shell(macros, cost)
    for n in range(1, predicted + 1):
        if direct_shortest_word_length(n, macros) == cost:
            return n
    raise AssertionError("spectral shell had no exact-cost witness")


def spectrum_matches_direct(macros, cost: int) -> bool:
    return pure_power_macro_shell(macros, cost) == direct_pure_power_macro_shell(macros, cost)


def predicted_budget_three_threshold(horizon: int) -> tuple[int, tuple[int, ...]]:
    """Current pure-power budget-three optimizer prediction.

    Horizon two is excluded because the globally optimal triple is mixed
    (`{4,6,9}`), not a pure-power family.
    """
    if horizon < 3:
        raise ValueError("pure-power budget-three phase starts at horizon 3")
    if horizon <= 5:
        macros = (4, 8, 9)
    else:
        macros = (8, 9, 25)
    return pure_power_macro_shell(macros, horizon + 1), macros


def pure_power_budget_optimizer(horizon: int, macro_budget: int, max_prime: int = 7,
                                max_exponent: int = 5):
    """Exhaustive optimizer inside the pure-prime-power class."""
    if horizon < 1 or macro_budget < 0:
        raise ValueError("invalid horizon or budget")
    candidates: list[int] = []
    for p in first_primes(max_prime):
        for e in range(2, max_exponent + 1):
            candidates.append(p ** e)
    best = -1
    optimizers: list[tuple[int, ...]] = []
    for macros in combinations(sorted(set(candidates)), macro_budget):
        threshold = pure_power_macro_shell(macros, horizon + 1)
        if threshold > best:
            best = threshold
            optimizers = [macros]
        elif threshold == best:
            optimizers.append(macros)
    return best, tuple(optimizers)


# Regression points that expose the finite transient -> stable transition.
assert pure_power_macro_spectrum((4, 9), 6) == (2, 3, 4, 4, 4, 4)
assert pure_power_macro_spectrum((8, 9), 7) == (2, 2, 3, 5, 5, 5, 5)
assert pure_power_macro_spectrum((4, 8, 9), 7) == (2, 3, 5, 5, 5, 5, 5)
assert pure_power_macro_spectrum((8, 9, 25), 8) == (2, 2, 3, 5, 7, 7, 7, 7)

for _h in range(3, 9):
    _threshold, _macros = predicted_budget_three_threshold(_h)
    assert spectrum_matches_direct(_macros, _h + 1)

# Candidate crossing: transient wins through h=5; stable wins from h=6.
for _h in range(3, 6):
    assert pure_power_macro_shell((4, 8, 9), _h + 1) >= pure_power_macro_shell((8, 9, 25), _h + 1)
for _h in range(6, 10):
    assert pure_power_macro_shell((8, 9, 25), _h + 1) >= pure_power_macro_shell((4, 8, 9), _h + 1)
