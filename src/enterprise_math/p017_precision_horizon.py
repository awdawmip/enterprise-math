"""Proof-relevant factor precision for the P017 square-basin bridge.

Stage 4 used the full tested-factor set D_y(n).  For the primality predicate, much
of that state information is unnecessary.  This module studies two compressions:

* the least visible factor, which preserves compatible projection across cutoffs;
* a one-bit "some factor is visible" state, which preserves single-level
  primality proof power but generally does not form a compatible precision chain.

It also defines the minimal survivor-prime factor horizon of one square basin.
Prime sieving, least prime factors, and semiprime factorization are classical;
the P018 contribution under test is the proof-precision organization.
"""

from __future__ import annotations

from .adaptive_precision import conflict_multiplicity
from .core import integer_nth_root
from .factor_precision import (
    factor_survivors,
    factor_witness_state,
    first_factor_shell,
    smallest_prime_factor,
    square_basin,
)
from .legendre import is_prime, primes_up_to
from .precision_system import refinement_projection


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def least_witness_state(n: int, cutoff: int) -> int:
    """Return the least tested prime divisor <=cutoff, or 0 if none is visible."""
    _require_positive("n", n)
    _require_natural("cutoff", cutoff)
    witnesses = factor_witness_state(n, cutoff)
    return witnesses[0] if witnesses else 0


def project_least_witness(state: int, cutoff: int) -> int:
    """Project a finer least-witness state back to a lower cutoff."""
    _require_natural("state", state)
    _require_natural("cutoff", cutoff)
    if state == 0:
        return 0
    return state if state <= cutoff else 0


def least_witness_compatibility(n: int, low: int, high: int) -> bool:
    """Verify ell_low is the projection of ell_high."""
    _require_positive("n", n)
    _require_natural("low", low)
    _require_natural("high", high)
    if low > high:
        raise ValueError("low cutoff must not exceed high cutoff")
    return project_least_witness(least_witness_state(n, high), low) == least_witness_state(
        n, low
    )


def factor_witness_bit(n: int, cutoff: int) -> int:
    """Return 1 iff some tested prime <=cutoff divides n, otherwise 0."""
    return int(bool(factor_witness_state(n, cutoff)))


def factor_state_primality_conflicts(k: int, n: int, cutoff: int) -> dict[str, int]:
    """Compare primality conflict under full, least, and one-bit factor states."""
    _require_positive("k", k)
    _require_positive("n", n)
    _require_natural("cutoff", cutoff)
    states = list(square_basin(k))
    if n not in states:
        raise ValueError("n must lie in the open square basin")
    effective = min(cutoff, k)
    predicate = is_prime
    full = lambda state: factor_witness_state(state, effective)
    least = lambda state: least_witness_state(state, effective)
    bit = lambda state: factor_witness_bit(state, effective)
    result = {
        "full": conflict_multiplicity(states, full, predicate, n),
        "least": conflict_multiplicity(states, least, predicate, n),
        "bit": conflict_multiplicity(states, bit, predicate, n),
    }
    if len(set(result.values())) != 1:
        raise AssertionError("factor-state compression changed primality conflict")
    return result


def least_witness_refines_full_projection(k: int, cutoff: int) -> bool:
    """Verify the full tested-factor observation refines the least-witness state."""
    _require_positive("k", k)
    _require_natural("cutoff", cutoff)
    effective = min(cutoff, k)
    states = list(square_basin(k))
    full = lambda n: factor_witness_state(n, effective)
    least = lambda n: least_witness_state(n, effective)
    projection = refinement_projection(states, least, full)
    return bool(projection) or all(least(n) == 0 for n in states)


def witness_bit_chain_is_compatible(
    states: list[int], low: int, high: int
) -> bool:
    """Whether the high-cutoff one-bit state refines the low-cutoff one-bit state."""
    _require_natural("low", low)
    _require_natural("high", high)
    if low > high:
        raise ValueError("low cutoff must not exceed high cutoff")
    low_obs = lambda n: factor_witness_bit(n, low)
    high_obs = lambda n: factor_witness_bit(n, high)
    try:
        refinement_projection(states, low_obs, high_obs)
    except ValueError:
        return False
    return True


def survivor_prime_horizon(k: int) -> int:
    """Smallest cutoff after which every factor survivor is prime.

    Equivalently, this is the maximum least-prime-factor among composite states in
    the open square basin, with value 0 if the basin contains no composites.
    """
    _require_positive("k", k)
    composite_spfs = [
        smallest_prime_factor(n)
        for n in square_basin(k)
        if not is_prime(n)
    ]
    return max(composite_spfs, default=0)


def survivor_prime_horizon_data(k: int) -> dict[str, object]:
    """Verify minimality, the root-factor upper bound, and the shell identity."""
    _require_positive("k", k)
    horizon = survivor_prime_horizon(k)
    primes = [n for n in square_basin(k) if is_prime(n)]
    survivors = factor_survivors(k, horizon)
    if survivors != primes:
        raise AssertionError("survivor-prime horizon did not isolate basin primes")
    if horizon > k:
        raise AssertionError("square-basin root-factor horizon was exceeded")
    if horizon > 0:
        earlier = factor_survivors(k, horizon - 1)
        if all(is_prime(n) for n in earlier):
            raise AssertionError("survivor-prime horizon was not minimal")
    nonempty_shell_primes = [
        p for p in primes_up_to(k) if first_factor_shell(k, p)
    ]
    shell_horizon = max(nonempty_shell_primes, default=0)
    if shell_horizon != horizon:
        raise AssertionError("last nonempty first-factor shell mismatched horizon")
    return {
        "k": k,
        "horizon": horizon,
        "slack": k - horizon,
        "prime_survivors": primes,
        "last_nonempty_shell": shell_horizon,
    }


def cutoff_is_survivor_prime_complete(k: int, cutoff: int) -> bool:
    """Return whether no composite survives the tested-factor cutoff."""
    _require_positive("k", k)
    _require_natural("cutoff", cutoff)
    return all(is_prime(n) for n in factor_survivors(k, cutoff))


def high_factor_shell_semiprimes(k: int, prime: int) -> list[tuple[int, int]]:
    """Classify a high least-factor shell as p*q semiprimes.

    When p^3 exceeds the square-basin upper endpoint, a basin state with smallest
    prime factor p cannot contain three prime factors counted with multiplicity.
    Because p<=k makes p^2 lie at or below k^2, every shell state is p*q with q a
    prime strictly larger than p.
    """
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <=k")
    upper = (k + 1) * (k + 1) - 1
    threshold = integer_nth_root(upper, 3)
    if prime <= threshold:
        raise ValueError("prime must lie above the cube-root shell threshold")
    result: list[tuple[int, int]] = []
    for n in first_factor_shell(k, prime):
        if n % prime != 0:
            raise AssertionError("shell state lost its defining prime")
        q = n // prime
        if not is_prime(q) or q <= prime:
            raise AssertionError("high factor shell is not semiprime p*q")
        result.append((n, q))
    return result


def root_observation_is_primality_inert(k: int) -> bool:
    """Verify R_2(n)=k is constant throughout the open square basin."""
    _require_positive("k", k)
    values = {integer_nth_root(n, 2) for n in square_basin(k)}
    return values == {k}
