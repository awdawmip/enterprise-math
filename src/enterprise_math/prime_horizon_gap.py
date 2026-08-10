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


def pure_cofactor_cap_nonforced_candidates(k: int, power: int) -> tuple[int, ...]:
    """Enumerate pure-cap candidate primes with no singleton-support witness.

    This is an exact bounded explorer, not an efficient large-scale search.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    upper_q = min(factor_horizon(k, power), isqrt(k**power))
    return tuple(
        q
        for q in primes_up_to(upper_q)
        if is_pure_cofactor_cap_candidate(k, power, q)
        and pure_cofactor_cap_certificate(k, power, q) is None
    )


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
