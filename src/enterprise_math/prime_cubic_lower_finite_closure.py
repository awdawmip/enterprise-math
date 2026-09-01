"""Finite cubic lower-cofactor closure arithmetic for R005-B.

This module contains exact integer reductions used to combine a verified prime-
gap prefix with the cubic lower cofactor-gap language.  It does not encode any
external computational prime-gap database as theorem truth; those premises stay
in the companion research note.
"""

from math import isqrt

from .legendre import is_prime
from .prime_collapse_field import factor_horizon
from .prime_cubic_boundary import previous_prime_at_most
from .prime_horizon_gap import next_prime_after


def _integer_cuberoot(n: int) -> int:
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
    r = _integer_cuberoot(n)
    return r if r**3 == n else r + 1


def cube_root_gap_supercritical(a: int, b: int) -> bool:
    """Return the exact integer test ``(b-a)^3 > 27*a``."""
    if a < 2 or b <= a:
        raise ValueError("require 2<=a<b")
    g = b - a
    return g**3 > 27 * a


def bounded_gap_real_activation_cutoff(max_gap: int) -> int:
    """Return the first a where ``g<=max_gap`` rules out cubic PRE activation.

    Any cubic lower/cofactor e=1 failure requires ``g^3>27*a``.  Hence if all
    relevant consecutive-prime gaps obey ``g<=G``, then every left endpoint
    ``a>=ceil(G^3/27)`` is automatically safe from this mechanism.
    """
    if max_gap <= 0:
        raise ValueError("max_gap must be positive")
    return (max_gap**3 + 26) // 27


def cubic_external_cofactor_k_limit(exhaustive_bound: int, max_gap: int) -> int:
    """Largest k covered by an external gap table through ``exhaustive_bound``.

    The largest lower-band cofactor point occurs at candidate q=2, namely
    ``x=k^3/2``.  The conservative endpoint condition is

        k^3/2 + max_gap < exhaustive_bound.

    Thus ``k^3 < 2*(exhaustive_bound-max_gap)`` and the answer is the largest
    integer strictly below that cube threshold.
    """
    if exhaustive_bound <= max_gap:
        raise ValueError("exhaustive_bound must exceed max_gap")
    target = 2 * (exhaustive_bound - max_gap)
    return _ceil_cuberoot(target) - 1


def cubic_lower_cofactor_interval(k: int, a: int, b: int) -> tuple[int, int]:
    """Return the exact integer q slice for a lower-band e=1 failure.

    T-A16 gives ``U/b < q <= A/a``.  The lower cofactor band additionally
    requires ``q*F<=A``.  Therefore the integer slice is

        [floor(U/b)+1, min(floor(A/a), floor(A/F))].

    The interval may be empty.  No primality assertion is made here.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if a < 2 or b <= a:
        raise ValueError("require 2<=a<b")
    lower = k**3
    upper = (k + 1) ** 3 - 1
    horizon = factor_horizon(k, 3)
    return upper // b + 1, min(lower // a, lower // horizon)


def cubic_lower_cofactor_boundary_prime(k: int, a: int, b: int) -> int | None:
    """Return the largest prime in the lower-band reciprocal slice, if any."""
    lo, hi = cubic_lower_cofactor_interval(k, a, b)
    if lo > hi or hi < 2:
        return None
    q = previous_prime_at_most(hi)
    return q if q >= lo else None


def lower_failure_requires_cube_root_gap(k: int, q: int, a: int, b: int) -> bool:
    """Verify the cubic necessary cube-root-gap inequality from failure data.

    Preconditions describe a lower-band e=1 failure:

    - q is prime and q*F<=A;
    - a<b are consecutive primes surrounding A/q;
    - q lies in the T-A16 failure interval, equivalently q*b>U.

    Under these assumptions the function returns the exact consequence

        (b-a)^3 > 27*a.

    A false return signals that the supplied tuple does not satisfy the claimed
    implication and is intended to be treated as an assertion failure by tests.
    """
    if k < 1 or q < 2 or not is_prime(q):
        raise ValueError("require positive k and prime q")
    if a < 2 or b <= a or not is_prime(a) or not is_prime(b):
        raise ValueError("require prime endpoints a<b")
    if next_prime_after(a) != b:
        raise ValueError("a,b must be consecutive primes")

    lower = k**3
    upper = (k + 1) ** 3 - 1
    horizon = factor_horizon(k, 3)
    x_floor = lower // q
    if not (q * horizon <= lower and a <= x_floor < b and q * b > upper):
        raise ValueError("tuple does not encode a lower-band e=1 failure")

    return cube_root_gap_supercritical(a, b)
