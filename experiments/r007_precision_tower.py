"""Exact finite-precision tower for the R007 gcd/lcm observation calculus.

This is executable evidence for theorem targets, not a formal proof.

For the bounded primitive scale language U_N={1,...,N}, the observational
envelope is L_N=lcm(1,...,N), and the canonical visible state is

    q_N(x) = gcd(x, L_N).

The tower changes only at prime powers.  Its inverse-limit completion is the
classical supernatural/Steinitz exponent space; the helpers below only model
finite-support profiles, allowing ``None`` as an infinite exponent.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, lcm
from typing import Iterable, Mapping


def factor_exponents(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def p_adic_valuation(n: int, p: int) -> int:
    if n < 1 or p < 2:
        raise ValueError("require n>=1 and p>=2")
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def divisor_count(n: int) -> int:
    result = 1
    for exponent in factor_exponents(n).values():
        result *= exponent + 1
    return result


def big_omega(n: int) -> int:
    return sum(factor_exponents(n).values())


def little_omega(n: int) -> int:
    return len(factor_exponents(n))


def positive_divisors(n: int) -> tuple[int, ...]:
    values = [1]
    for p, exponent in factor_exponents(n).items():
        values = [
            value * p**power
            for value in values
            for power in range(exponent + 1)
        ]
    return tuple(sorted(values))


def lcm_ceiling(N: int) -> int:
    """L_N = lcm(1,...,N), with L_0=L_1=1."""
    if N < 0:
        raise ValueError("N must be nonnegative")
    result = 1
    for value in range(2, N + 1):
        result = lcm(result, value)
    return result


def prime_power_tick(N: int) -> tuple[int, int] | None:
    """Return (p,k) iff N=p^k for a prime p and k>=1."""
    if N < 2:
        return None
    factors = factor_exponents(N)
    if len(factors) != 1:
        return None
    p, exponent = next(iter(factors.items()))
    return p, exponent


def precision_projection(x: int, N: int) -> int:
    """Visible divisor state at bounded primitive scale N."""
    if x < 1:
        raise ValueError("x must be positive")
    return gcd(x, lcm_ceiling(N))


def recovery_threshold(x: int) -> int:
    """Least N with q_N(x)=x: the largest prime-power token of x."""
    if x < 1:
        raise ValueError("x must be positive")
    factors = factor_exponents(x)
    return max((p**exponent for p, exponent in factors.items()), default=1)


def first_distinguishing_precision(x: int, y: int) -> int | None:
    """Least N with q_N(x) != q_N(y); None exactly when x=y."""
    if x < 1 or y < 1:
        raise ValueError("x and y must be positive")
    if x == y:
        return None
    fx = factor_exponents(x)
    fy = factor_exponents(y)
    primes = set(fx) | set(fy)
    return min(
        p ** (min(fx.get(p, 0), fy.get(p, 0)) + 1)
        for p in primes
        if fx.get(p, 0) != fy.get(p, 0)
    )


def precision_resources(N: int) -> tuple[int, int, int]:
    """(visible classes, full-action basis storage, worst basis depth)."""
    ceiling = lcm_ceiling(N)
    return divisor_count(ceiling), big_omega(ceiling), little_omega(ceiling)


def tick_split_profile(N: int) -> tuple[int, int, int] | None:
    """At a prime-power tick, return (old classes, classes split, new classes).

    If N=p^k then exactly 1/k of the old divisor classes are saturated on the
    p-coordinate and each of those splits into two.
    """
    tick = prime_power_tick(N)
    if tick is None:
        return None
    _p, k = tick
    old_count = divisor_count(lcm_ceiling(N - 1))
    if old_count % k != 0:
        raise AssertionError("prime-power split divisibility invariant failed")
    split = old_count // k
    return old_count, split, old_count + split


def future_envelope(probes: Iterable[int]) -> int:
    result = 1
    for probe in probes:
        if probe < 1:
            raise ValueError("probes must be positive")
        result = lcm(result, probe)
    return result


def one_step_signature(x: int, probes: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(gcd(x, probe) for probe in probes)


def composite_output(x: int, word: tuple[int, ...]) -> int:
    """Final state after a nonempty word of gcd-mask actions."""
    if not word:
        raise ValueError("word must be nonempty")
    result = x
    for probe in word:
        result = gcd(result, probe)
    return result


def subset_trace(x: int, probes: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    """All distinct nonempty subset-word outputs (order/repetition are immaterial)."""
    trace: dict[tuple[int, ...], int] = {}
    for size in range(1, len(probes) + 1):
        for indices in combinations(range(len(probes)), size):
            word = tuple(probes[index] for index in indices)
            trace[indices] = composite_output(x, word)
    return trace


def synthetic_local_unit(probes: tuple[int, ...]) -> int:
    """The observational envelope, i.e. the least local unit mask for the probes."""
    return future_envelope(probes)


def local_unit_is_executable(probes: tuple[int, ...]) -> bool:
    """Whether the local unit is already one of the normalized primitive masks."""
    if not probes:
        return False
    return synthetic_local_unit(probes) in probes


def supernatural_projection(
    exponents: Mapping[int, int | None], N: int
) -> int:
    """Finite q_N projection of a finite-support supernatural profile.

    ``None`` denotes an infinite exponent.  Missing primes have exponent zero.
    """
    if N < 0:
        raise ValueError("N must be nonnegative")
    ceiling = factor_exponents(lcm_ceiling(N))
    result = 1
    for p, beta in ceiling.items():
        alpha = exponents.get(p, 0)
        visible = beta if alpha is None else min(alpha, beta)
        result *= p**visible
    return result


def prime_power_tokens(n: int) -> frozenset[tuple[int, int]]:
    """Birkhoff token ideal I(n)={(p,k):1<=k<=v_p(n)}."""
    if n < 1:
        raise ValueError("n must be positive")
    return frozenset(
        (p, level)
        for p, exponent in factor_exponents(n).items()
        for level in range(1, exponent + 1)
    )


def precision_token_ball(N: int) -> frozenset[tuple[int, int]]:
    """All prime-power tokens with numeric weight p^k <= N."""
    return prime_power_tokens(lcm_ceiling(N))


def maximal_prime_power_basis(N: int) -> tuple[int, ...]:
    """One maximal p-power <=N for each prime p<=N.

    Their lcm is L_N.  Distinct members have pairwise product >N, so no
    bounded primitive scale <=N can witness two of these maximal prime ceilings
    simultaneously; hence this basis has minimum cardinality among sublanguages
    of {1,...,N} with envelope L_N.
    """
    if N < 1:
        raise ValueError("N must be positive")
    ceiling_factors = factor_exponents(lcm_ceiling(N))
    return tuple(sorted(p**exponent for p, exponent in ceiling_factors.items()))
