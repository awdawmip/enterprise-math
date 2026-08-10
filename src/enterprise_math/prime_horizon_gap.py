"""Exact R005-B horizon-gap / exclusive-cofactor primitives.

These helpers isolate the arithmetic boundary between the p-power factor
horizon and an e=1 exclusive divisor certificate.  They intentionally do not
reimplement R005-A forced-core / hitting-set semantics.

All routines use integer arithmetic.  No asymptotic prime-gap theorem is
assumed here.
"""

from math import isqrt

from .legendre import is_prime, primes_up_to
from .prime_collapse_field import factor_horizon


COFACTOR_GAP = "COFACTOR_GAP"
HORIZON_GAP = "HORIZON_GAP"


def next_prime_after(n: int) -> int:
    """Return the least prime strictly larger than ``n``."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    q = max(2, n + 1)
    while not is_prime(q):
        q += 1
    return q


def _integer_cuberoot(n: int) -> int:
    """Return floor(cuberoot(n)) exactly by integer binary search."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    lo = 0
    hi = 1
    while hi**3 <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def _validate_candidate(k: int, power: int, q: int) -> int:
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    horizon = factor_horizon(k, power)
    if q < 2 or not is_prime(q):
        raise ValueError("q must be prime")
    if q > horizon:
        raise ValueError("q must not exceed the factor horizon")
    return horizon


def exclusive_cofactor_regime(k: int, power: int, q: int) -> str:
    """Classify the e=1 exclusive-certificate lower boundary for ``q``.

    Put ``A=k**power`` and ``F=factor_horizon(k,power)``.

    - ``COFACTOR_GAP``: ``A/q >= F`` (equivalently ``q*F <= A``), so the
      first eligible exclusive cofactor is controlled by the next prime above
      ``floor(A/q)``.
    - ``HORIZON_GAP``: ``A/q < F`` (equivalently ``q*F > A``), so candidate
      exclusion itself moves the lower boundary to the first prime above F.
    """
    horizon = _validate_candidate(k, power, q)
    return HORIZON_GAP if q * horizon > k**power else COFACTOR_GAP


def first_exclusive_cofactor_prime(k: int, power: int, q: int) -> int:
    """Return the least prime cofactor that could give singleton q-support.

    If ``A=k**p`` and ``F=F_p(k)``, an e=1 singleton-support certificate must
    have prime cofactor

        r > max(F, A/q).

    Therefore the first possible cofactor is exactly

        nextprime(max(F, floor(A/q))).
    """
    horizon = _validate_candidate(k, power, q)
    lower = max(horizon, k**power // q)
    return next_prime_after(lower)


def exclusive_cofactor_certificate(k: int, power: int, q: int) -> int | None:
    """Return the least e=1 singleton-support certificate, if it fits.

    The returned integer is ``q*r`` where ``r`` is the first eligible prime
    above both the factor horizon and ``A/q``.  It exists exactly when
    ``q*r <= U=(k+1)^p-1``.  Strict lower-basin membership is automatic from
    the choice ``r > floor(A/q)``.
    """
    r = first_exclusive_cofactor_prime(k, power, q)
    upper = (k + 1) ** power - 1
    n = q * r
    return n if n <= upper else None


def is_pure_cofactor_cap_candidate(k: int, power: int, q: int) -> bool:
    """Return whether q lies in the theorem-safe pure horizon cofactor cap.

    Besides the horizon-gap condition ``q*F>A``, the inequalities exclude all
    singleton-support basin forms except ``q*r`` with one prime ``r>F``:

    - ``q^2 <= A`` excludes q^2 from the basin;
    - ``q^3 > U`` excludes every higher pure power;
    - ``q^2*(F+1) > U`` excludes q^a*r with a>=2 and r>F.

    On this cap, q is forced in R005-A's singleton-support sense exactly when
    ``q*nextprime(F) <= U``.
    """
    horizon = _validate_candidate(k, power, q)
    lower = k**power
    upper = (k + 1) ** power - 1
    return (
        q * q <= lower
        and q**3 > upper
        and q * q * (horizon + 1) > upper
        and q * horizon > lower
    )


def pure_cofactor_cap_certificate(k: int, power: int, q: int) -> int | None:
    """Return the unique-form q*r certificate on the pure cap, if it exists."""
    if not is_pure_cofactor_cap_candidate(k, power, q):
        raise ValueError("q is not in the pure cofactor cap")
    horizon = factor_horizon(k, power)
    r = next_prime_after(horizon)
    n = q * r
    upper = (k + 1) ** power - 1
    return n if n <= upper else None


def pure_cofactor_cap_nonforced_interval(k: int, power: int) -> tuple[int, int]:
    """Return the exact integer interval containing all non-forced pure-cap q.

    Let ``R=nextprime(F)`` and ``S=floor(sqrt(A))``.  The pure-cap conditions
    plus non-forcing are exactly the strict inequalities

        q > A/F,
        q^3 > U,
        q^2*(F+1) > U,
        q > U/R,

    together with ``q<=S`` and primality.  Therefore the eligible integer slice
    is the contiguous interval ``[L,S]`` where

        L = 1 + max(
            floor(A/F),
            floor(cuberoot(U)),
            floor(sqrt(floor(U/(F+1)))),
            floor(U/R),
        ).

    Since ``A<U``, ``S<=F`` and the candidate bound q<=F is automatic.
    The interval can be empty when ``L>S``.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    lower_basin = k**power
    upper_basin = (k + 1) ** power - 1
    horizon = factor_horizon(k, power)
    root_lower = isqrt(lower_basin)
    successor = next_prime_after(horizon)
    lower_q = 1 + max(
        lower_basin // horizon,
        _integer_cuberoot(upper_basin),
        isqrt(upper_basin // (horizon + 1)),
        upper_basin // successor,
    )
    return lower_q, root_lower


def cubic_pure_cap_nonforced_interval(k: int) -> tuple[int, int]:
    """Return the collapsed p=3 non-forced pure-cap interval for k>=3.

    In the cubic case the horizon inequality ``q*F>A`` already forces q>k.
    Hence q>=k+1, which automatically implies both ``q^3>U`` and
    ``q^2*(F+1)>U``.  The generic four-cutoff compiler therefore reduces to

        L = 1 + max(floor(k^3/F), floor(U/R)),
        S = floor(sqrt(k^3)).
    """
    if k < 3:
        raise ValueError("cubic collapsed interval requires k>=3")
    lower_basin = k**3
    upper_basin = (k + 1) ** 3 - 1
    horizon = factor_horizon(k, 3)
    successor = next_prime_after(horizon)
    return (
        1 + max(lower_basin // horizon, upper_basin // successor),
        isqrt(lower_basin),
    )


def pure_cofactor_cap_nonforced_candidates(k: int, power: int) -> tuple[int, ...]:
    """Enumerate exactly the prime slice of non-forced pure-cap candidates."""
    lower_q, upper_q = pure_cofactor_cap_nonforced_interval(k, power)
    if lower_q > upper_q:
        return ()
    return tuple(q for q in primes_up_to(upper_q) if q >= lower_q)


def horizon_drift_components(k: int, power: int) -> tuple[int, int, int]:
    """Return ``(d, rho, S)`` for the exact horizon-gap decomposition.

    With

        S=floor(sqrt(A)),
        F=floor(sqrt(U)),
        d=F-S,
        rho=U-F^2,

    the exact protecting-gap threshold satisfies

        G = U/S - F = d + (d^2 + rho)/S.

    ``rho`` is the upper endpoint's remainder above the lower horizon square.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    lower = k**power
    upper = (k + 1) ** power - 1
    root_lower = isqrt(lower)
    horizon = factor_horizon(k, power)
    drift = horizon - root_lower
    remainder = upper - horizon * horizon
    return drift, remainder, root_lower


def horizon_gap_threshold(k: int, power: int) -> tuple[int, int]:
    """Return the exact rational threshold ``G=(U/S)-F`` as (num, den).

    Here ``S=floor(sqrt(A))``, ``A=k^p``, ``U=(k+1)^p-1`` and ``F=isqrt(U)``.
    A non-forced pure horizon-cap candidate q<=S requires

        nextprime(F) * S > U,

    equivalently a right-of-horizon prime-free gap exceeding ``G``.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    lower = k**power
    upper = (k + 1) ** power - 1
    horizon = factor_horizon(k, power)
    root_lower = isqrt(lower)
    return upper - horizon * root_lower, root_lower


def horizon_successor_exceeds_threshold(k: int, power: int) -> bool:
    """Check the exact integer form ``nextprime(F)*floor(sqrt(A)) > U``."""
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    lower = k**power
    upper = (k + 1) ** power - 1
    horizon = factor_horizon(k, power)
    return next_prime_after(horizon) * isqrt(lower) > upper
