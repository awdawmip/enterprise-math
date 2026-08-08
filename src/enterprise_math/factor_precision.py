"""Prime-factor precision as a second P018 precision axis.

At factor cutoff y, the state records which tested primes p<=y divide n.  Raising
y adds possible divisibility witnesses; projection back to a lower cutoff simply
forgets witnesses above that cutoff.  Composite certificates persist as soon as
a witness appears.  On a consecutive-square basin, the integer-root factor
horizon k makes the finite terminal cutoff y=k complete for primality.

The sieve and smallest-prime-factor partition are classical mathematics.  P018
uses them to exhibit a non-scale precision axis with the same persistent-proof
logic as the finite precision-cell calculus.
"""

from __future__ import annotations

from .legendre import is_prime, primes_up_to

COMPOSITE = "COMPOSITE"
PRIME = "PRIME"
UNRESOLVED = "UNRESOLVED"


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def factor_witness_state(n: int, cutoff: int) -> tuple[int, ...]:
    """Return tested prime divisors p<=cutoff of n."""
    _require_positive("n", n)
    _require_natural("cutoff", cutoff)
    return tuple(p for p in primes_up_to(cutoff) if n % p == 0)


def project_factor_precision(
    witness_state: tuple[int, ...], cutoff: int
) -> tuple[int, ...]:
    """Forget factor witnesses above a lower cutoff."""
    _require_natural("cutoff", cutoff)
    if any(
        isinstance(p, bool) or not isinstance(p, int) or p < 2
        for p in witness_state
    ):
        raise ValueError("witness_state must contain prime-like integers >=2")
    return tuple(p for p in witness_state if p <= cutoff)


def factor_precision_compatibility(n: int, low: int, high: int) -> bool:
    """Verify D_low(n) is the projection of D_high(n)."""
    _require_positive("n", n)
    _require_natural("low", low)
    _require_natural("high", high)
    if low > high:
        raise ValueError("low cutoff must not exceed high cutoff")
    low_state = factor_witness_state(n, low)
    high_state = factor_witness_state(n, high)
    return project_factor_precision(high_state, low) == low_state


def factor_certificate(
    n: int, cutoff: int, complete_horizon: int | None = None
) -> str:
    """Return COMPOSITE, PRIME, or UNRESOLVED at one factor precision.

    A nonempty witness state is a permanent composite certificate.  An empty
    state becomes a prime certificate only once a supplied finite completeness
    horizon has been reached.
    """
    _require_positive("n", n)
    _require_natural("cutoff", cutoff)
    witnesses = factor_witness_state(n, cutoff)
    if witnesses:
        return COMPOSITE
    if complete_horizon is not None:
        _require_natural("complete_horizon", complete_horizon)
        if cutoff >= complete_horizon:
            return PRIME
    return UNRESOLVED


def factor_certificate_profile(
    n: int, cutoffs: list[int], complete_horizon: int
) -> list[str]:
    """Return persistent proof status along an increasing factor-precision chain."""
    _require_positive("n", n)
    _require_natural("complete_horizon", complete_horizon)
    if not cutoffs:
        raise ValueError("at least one cutoff is required")
    previous = -1
    decided: str | None = None
    profile: list[str] = []
    for cutoff in cutoffs:
        _require_natural("cutoff", cutoff)
        if cutoff < previous:
            raise ValueError("cutoffs must be nondecreasing")
        status = factor_certificate(n, cutoff, complete_horizon)
        if decided is not None and status != decided:
            raise AssertionError("a factor-precision certificate was overturned")
        if status != UNRESOLVED:
            decided = status
        profile.append(status)
        previous = cutoff
    return profile


def square_basin(k: int) -> range:
    """Return the open consecutive-square basin k^2<n<(k+1)^2."""
    _require_positive("k", k)
    return range(k * k + 1, (k + 1) * (k + 1))


def square_basin_factor_certificate(k: int, n: int, cutoff: int) -> str:
    """Use the exact square-basin factor horizon k as terminal precision."""
    _require_positive("k", k)
    _require_positive("n", n)
    _require_natural("cutoff", cutoff)
    if n not in square_basin(k):
        raise ValueError("n must lie strictly between k^2 and (k+1)^2")
    if cutoff > k:
        cutoff = k
    status = factor_certificate(n, cutoff, k)
    if cutoff == k:
        actual = PRIME if is_prime(n) else COMPOSITE
        if status != actual:
            raise AssertionError("square-basin factor horizon failed")
    return status


def factor_survivors(k: int, cutoff: int) -> list[int]:
    """Return basin states with no tested prime factor <= cutoff."""
    _require_positive("k", k)
    _require_natural("cutoff", cutoff)
    effective = min(cutoff, k)
    tested = primes_up_to(effective)
    return [
        n
        for n in square_basin(k)
        if all(n % p != 0 for p in tested)
    ]


def factor_survivor_profile(k: int, cutoffs: list[int]) -> list[int]:
    """Return the nonincreasing survivor count along factor precision."""
    _require_positive("k", k)
    if not cutoffs:
        raise ValueError("at least one cutoff is required")
    previous_cutoff = -1
    counts: list[int] = []
    last: int | None = None
    for cutoff in cutoffs:
        _require_natural("cutoff", cutoff)
        if cutoff < previous_cutoff:
            raise ValueError("cutoffs must be nondecreasing")
        count = len(factor_survivors(k, cutoff))
        if last is not None and count > last:
            raise AssertionError("factor survivors cannot increase with precision")
        counts.append(count)
        last = count
        previous_cutoff = cutoff
    return counts


def smallest_prime_factor(n: int) -> int:
    """Return the least prime divisor of n>1."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1:
        raise ValueError("n must be an integer >1")
    for p in primes_up_to(n):
        if n % p == 0:
            return p
    raise AssertionError("least prime factor not found")


def first_factor_shell(k: int, prime: int) -> list[int]:
    """Return basin composites first certified when prime enters the cutoff."""
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <=k")
    return [
        n
        for n in square_basin(k)
        if n % prime == 0
        and all(n % q != 0 for q in primes_up_to(prime - 1))
    ]


def factor_precision_partition(k: int) -> dict[str, object]:
    """Partition the basin into disjoint first-factor shells plus final primes."""
    _require_positive("k", k)
    shells = {
        p: first_factor_shell(k, p)
        for p in primes_up_to(k)
    }
    final_survivors = factor_survivors(k, k)
    primes = [n for n in square_basin(k) if is_prime(n)]
    if final_survivors != primes:
        raise AssertionError("terminal factor survivors must equal basin primes")

    shell_states = [n for states in shells.values() for n in states]
    all_states = list(square_basin(k))
    if len(shell_states) != len(set(shell_states)):
        raise AssertionError("first-factor shells must be disjoint")
    if sorted(shell_states + final_survivors) != all_states:
        raise AssertionError("factor-precision shells do not partition the basin")
    return {
        "shells": shells,
        "final_survivors": final_survivors,
        "prime_count": len(final_survivors),
        "composite_count": len(shell_states),
        "basin_size": len(all_states),
    }


def p017_p018_bridge(k: int) -> dict[str, int]:
    """Return the exact first-witness-shell form of the P017 prime count.

    The open square basin has size 2k.  Every composite exits at the precision
    equal to its least prime factor, which is <=k.  The remaining states at the
    terminal factor horizon are exactly the primes.
    """
    data = factor_precision_partition(k)
    shell_total = sum(len(states) for states in data["shells"].values())
    prime_count = int(data["prime_count"])
    if prime_count != 2 * k - shell_total:
        raise AssertionError("P017/P018 factor-shell bridge identity failed")
    return {
        "basin_size": 2 * k,
        "first_factor_shell_total": shell_total,
        "terminal_survivors": prime_count,
    }
