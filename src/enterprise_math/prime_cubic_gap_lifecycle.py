"""Exact cubic cofactor-gap lifecycle tools for R005-B.

This module owns the arithmetic specialization of one consecutive cofactor-prime
gap as the cubic factor horizon moves through it.  Generic forced-core,
hitting-set and witness-language semantics remain R005-A/A2/A4 ownership.

All routines are exact integer helpers.  No asymptotic prime-gap theorem is
implemented here.
"""

from .legendre import is_prime
from .prime_collapse_field import factor_horizon
from .prime_cubic_boundary import previous_prime_at_most
from .prime_horizon_gap import next_prime_after


PRE_HORIZON = "PRE_HORIZON"
HORIZON_INSIDE = "HORIZON_INSIDE"
RETIRED = "RETIRED"


def _integer_cuberoot(n: int) -> int:
    """Return floor(cuberoot(n)) by exact integer binary search."""
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


def _ceil_cuberoot(n: int) -> int:
    """Return ceil(cuberoot(n)) exactly."""
    root = _integer_cuberoot(n)
    return root if root**3 == n else root + 1


def _validate_consecutive_prime_gap(a: int, b: int) -> None:
    if a < 2 or b <= a or not is_prime(a) or not is_prime(b):
        raise ValueError("a<b must be prime")
    if next_prime_after(a) != b:
        raise ValueError("a and b must be consecutive primes")


def cubic_first_horizon_at_least(t: int) -> int:
    """Return the least k with F_3(k)>=t.

    Since F_3(k)=floor(sqrt((k+1)^3-1)), the exact inverse is

        ceil(cuberoot(t^2+1)) - 1.
    """
    if t < 1:
        raise ValueError("t must be positive")
    return _ceil_cuberoot(t * t + 1) - 1


def cubic_last_pre_horizon_k(a: int) -> int:
    """Return the largest k with F_3(k)<a."""
    if a < 2:
        raise ValueError("a must be at least 2")
    return _integer_cuberoot(a * a) - 1


def cubic_gap_phase(k: int, a: int, b: int) -> str:
    """Classify a fixed consecutive prime gap relative to the cubic horizon."""
    if k < 1:
        raise ValueError("k must be positive")
    _validate_consecutive_prime_gap(a, b)
    horizon = factor_horizon(k, 3)
    if horizon < a:
        return PRE_HORIZON
    if horizon < b:
        return HORIZON_INSIDE
    return RETIRED


def cubic_horizon_crossing_interval(a: int, b: int) -> tuple[int, int]:
    """Return inclusive k interval on which a<=F_3(k)<b.

    The interval may be empty, represented by lower>upper, if one horizon jump
    skips the whole prime gap.
    """
    _validate_consecutive_prime_gap(a, b)
    return (
        cubic_first_horizon_at_least(a),
        cubic_first_horizon_at_least(b) - 1,
    )


def cubic_pre_gap_activation_margin(k: int, a: int, b: int) -> int:
    """Return the exact numerator-sign margin for a pre-horizon reciprocal gap.

    With g=b-a, the real reciprocal interval

        U/b < q <= A/a

    has positive width exactly when

        g*k^2 > 3*a*(k+1).

    The returned integer is the left side minus the right side.
    """
    if k < 1:
        raise ValueError("k must be positive")
    _validate_consecutive_prime_gap(a, b)
    return (b - a) * k * k - 3 * a * (k + 1)


def cubic_pre_gap_critical_length(a: int) -> int:
    """Return the least integer gap length that can activate before horizon entry.

    Let K_-(a) be the last k with F_3(k)<a.  Since k^2/(k+1) is increasing,
    some pre-horizon real reciprocal interval can open iff the gap length g
    satisfies

        g*K_-^2 > 3*a*(K_-+1).

    Hence the exact least integer g is

        1 + floor(3*a*(K_-+1)/K_-^2).
    """
    if a < 2 or not is_prime(a):
        raise ValueError("a must be prime")
    k_last = cubic_last_pre_horizon_k(a)
    if k_last < 3:
        raise ValueError("a has no cubic pre-horizon state with k>=3")
    return 1 + (3 * a * (k_last + 1)) // (k_last * k_last)


def cubic_pre_gap_activation_interval(
    a: int, b: int
) -> tuple[int, int] | None:
    """Return the inclusive pre-horizon k interval with positive real q-width.

    The predicate is monotone in k, so activation (if any) is a terminal
    interval ending at K_-(a).
    """
    _validate_consecutive_prime_gap(a, b)
    k_last = cubic_last_pre_horizon_k(a)
    if k_last < 3:
        return None
    if cubic_pre_gap_activation_margin(k_last, a, b) <= 0:
        return None

    lo = 3
    hi = k_last
    while lo < hi:
        mid = (lo + hi) // 2
        if cubic_pre_gap_activation_margin(mid, a, b) > 0:
            hi = mid
        else:
            lo = mid + 1
    return lo, k_last


def cubic_reciprocal_candidate_interval(
    k: int, a: int, b: int
) -> tuple[int, int]:
    """Return exact integer q interval captured by one PRE_HORIZON prime gap.

    For A=k^3 and U=(k+1)^3-1, T-A16's e=1 failure interval is

        U/b < q <= A/a.

    Thus the integer slice is

        [floor(U/b)+1, floor(A/a)].

    PRE_HORIZON guarantees this is in the lower cofactor-gap band.
    """
    _validate_consecutive_prime_gap(a, b)
    if cubic_gap_phase(k, a, b) != PRE_HORIZON:
        raise ValueError("gap must be strictly ahead of the cubic factor horizon")
    lower = k**3
    upper = (k + 1) ** 3 - 1
    return upper // b + 1, lower // a


def cubic_gap_max_captured_prime(k: int, a: int, b: int) -> int | None:
    """Return the largest prime in the reciprocal q slice, if one exists."""
    lower_q, upper_q = cubic_reciprocal_candidate_interval(k, a, b)
    if lower_q > upper_q or upper_q < 2:
        return None
    q = previous_prime_at_most(upper_q)
    return q if q >= lower_q else None


def cubic_gap_full_nonforced_witness(k: int, a: int, b: int) -> int | None:
    """Return a full non-forced lower-band witness when boundary compression proves it.

    If the reciprocal slice contains a prime q>k, then q has no singleton
    candidate-support certificate of any allowed factor form:

    - q^2<A because PRE_HORIZON gives a>F_3(k)>sqrt(A) and q<=A/a;
    - q^e>U for every e>=3 because integer q>k implies q>=k+1;
    - q^2*r>U for every prime r>F because q>=k+1 and F+1>=k+1;
    - the e=1 route is blocked by the consecutive cofactor gap (a,b).

    The one-large-prime horizon normal form then excludes every remaining
    singleton-support form.
    """
    q = cubic_gap_max_captured_prime(k, a, b)
    if q is None or q <= k:
        return None
    return q
