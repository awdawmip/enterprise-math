"""Full k-smooth cores for states in one open square basin.

For k^2 < n < (k+1)^2, collect every prime factor <= k with its full
multiplicity into S_k(n). The remaining tail Q_k(n)=n/S_k(n) is forced to be
1 or a single prime > k: two remaining factors > k would already have product
at least (k+1)^2.

This is a finite integer classification, not a primality heuristic. It is the
multiplicity-preserving refinement needed by the mirror CRT route.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime, primes_up_to


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _factor_integer(n: int) -> dict[int, int]:
    """Return the exact prime factorization of n>0 as an exponent dictionary."""
    _require_positive("n", n)
    if n == 1:
        return {}
    remaining = n
    factors: dict[int, int] = {}
    for prime in primes_up_to(isqrt(n)):
        if prime * prime > remaining:
            break
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            factors[prime] = exponent
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def square_basin_smooth_core(k: int, n: int) -> dict[str, object]:
    """Return the full small-prime core and unique possible large tail.

    S_k(n)=product_{p<=k} p^{v_p(n)}.  The residual tail is asserted to be
    either one or a single prime strictly greater than k.
    """
    _require_positive("k", k)
    _require_positive("n", n)
    if not k * k < n < (k + 1) * (k + 1):
        raise ValueError("n must lie strictly between k^2 and (k+1)^2")

    factors = _factor_integer(n)
    smooth_factors = {p: e for p, e in factors.items() if p <= k}
    tail_factors = {p: e for p, e in factors.items() if p > k}

    smooth_core = 1
    for prime, exponent in smooth_factors.items():
        smooth_core *= prime**exponent
    large_tail = n // smooth_core

    if large_tail != 1:
        if not is_prime(large_tail) or large_tail <= k:
            raise AssertionError("square-basin tail is not one prime > k")
        if tail_factors != {large_tail: 1}:
            raise AssertionError("large-tail factorization is not singleton prime support")
    elif tail_factors:
        raise AssertionError("tail factorization survived after unit tail")

    state_is_prime = is_prime(n)
    if state_is_prime != (smooth_core == 1):
        raise AssertionError("smooth-core primality criterion failed")

    if large_tail > 1 and smooth_core > k:
        raise AssertionError("large-prime tail left a smooth core above k")

    return {
        "k": k,
        "n": n,
        "smooth_core": smooth_core,
        "large_tail": large_tail,
        "smooth_prime_powers": tuple(sorted(smooth_factors.items())),
        "state_is_prime": state_is_prime,
        "fully_k_smooth": large_tail == 1,
    }


def square_basin_smooth_core_profile(k: int) -> dict[str, object]:
    """Classify the complete open k-th square basin by full smooth core."""
    _require_positive("k", k)
    states = [
        square_basin_smooth_core(k, n)
        for n in range(k * k + 1, (k + 1) * (k + 1))
    ]
    primes = [int(data["n"]) for data in states if data["state_is_prime"]]
    composites = [int(data["n"]) for data in states if not data["state_is_prime"]]
    fully_smooth = [int(data["n"]) for data in states if data["fully_k_smooth"]]
    prime_tail_composites = [
        int(data["n"])
        for data in states
        if not data["state_is_prime"] and int(data["large_tail"]) > 1
    ]
    if len(primes) + len(composites) != 2 * k:
        raise AssertionError("smooth-core profile lost square-basin states")
    return {
        "k": k,
        "states": states,
        "primes": primes,
        "composites": composites,
        "fully_k_smooth_composites": fully_smooth,
        "prime_tail_composites": prime_tail_composites,
    }
