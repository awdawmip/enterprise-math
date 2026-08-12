"""Cutoff-uniform mirror cross-overlap prime separator.

Fix an anchor-surviving mirror pair around M=k(k+1) and any cutoff 2<=z<k.
Call a side z-rough when it has no transverse prime <=z.  On a z-rough side let

    c_z(n)=#{z<p<=k : p transverse and p|n}.

Every composite state in the open square basin has a prime factor <=k.  Hence
on a z-rough side

    side prime <=> c_z(n)=0,
    side composite => c_z(n)>=1.

For a radius on which both sides are z-rough, put x=c_z(M-r), y=c_z(M+r).
Then the degree-two weight

    Q_z(r)=1-x*y

has the exact sign semantics

    Q_z(r)>0  <=> at least one mirror side is prime,
    both sides composite => Q_z(r)<=0.

Thus with R_rr(z) the number of double-z-rough radii and

    X_cross(z)=sum x*y,

one has the sufficient certificate

    R_rr(z)-X_cross(z)>0 => a basin prime exists.

The independent local model on medium primes has

    E[x*y] = sum_{p!=q, z<p,q<=k} 1/(pq)
           = L_z^2 - sum_p 1/p^2,

relative to the double-rough base, where L_z=sum 1/p.  For power cutoffs
z=k^alpha this tends log^2(1/alpha).  Hence a positive asymptotic local margin
requires alpha>e^(-1).

This positive-double-rough route has a classical sieve incompatibility: a
standard dimension-two DHR lower sieve has sifting limit beta_2>4.  If the
radius sequence supplies level at most D~k, then s=log D/log z<=1/alpha, so
lower-sieve positivity requires alpha<1/4.  Since e^(-1)>1/4, the local-margin
and ordinary dimension-two lower-sieve regions do not overlap.  This prior-art
comparison is a negative routing boundary, not an internal reproof of DHR.

The exact finite separator itself is elementary and independent of that
asymptotic comparison.
"""

from __future__ import annotations

from fractions import Fraction

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports


def _split_count(support: list[int] | tuple[int, ...], cutoff: int) -> tuple[int, int]:
    low = sum(int(p) <= cutoff for p in support)
    high = len(support) - low
    return low, high


def mirror_cross_cutoff_point(k: int, radius: int, cutoff: int) -> dict[str, object]:
    """Return the exact 1-x*y separator on one double-z-rough mirror radius."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (2 <= cutoff < k):
        raise ValueError("cutoff must satisfy 2<=cutoff<k")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower_state, upper_state = mirror_pair(k, radius)
    lower_support, upper_support = mirror_transverse_supports(k, radius)
    lower_low, x = _split_count(lower_support, cutoff)
    upper_low, y = _split_count(upper_support, cutoff)
    double_rough = lower_low == 0 and upper_low == 0
    if not double_rough:
        return {
            "k": k,
            "radius": radius,
            "cutoff": cutoff,
            "double_rough": False,
            "lower_high_support_count": x,
            "upper_high_support_count": y,
            "quadratic_separator": None,
        }

    lower_prime = is_prime(lower_state)
    upper_prime = is_prime(upper_state)
    if not lower_prime and x < 1:
        raise AssertionError("double-rough lower composite has no high support prime")
    if not upper_prime and y < 1:
        raise AssertionError("double-rough upper composite has no high support prime")
    separator = 1 - x * y
    prime_side = lower_prime or upper_prime
    if (separator > 0) != prime_side:
        raise AssertionError("cross-cutoff separator lost exact prime-side sign semantics")

    return {
        "k": k,
        "radius": radius,
        "cutoff": cutoff,
        "double_rough": True,
        "lower_state": lower_state,
        "upper_state": upper_state,
        "lower_high_support_count": x,
        "upper_high_support_count": y,
        "cross_overlap_multiplicity": x * y,
        "quadratic_separator": separator,
        "lower_prime": lower_prime,
        "upper_prime": upper_prime,
        "prime_side": prime_side,
        "positive_iff_prime_side": True,
    }


def mirror_cross_cutoff_profile(k: int, cutoff: int) -> dict[str, object]:
    """Aggregate R_rr-X_cross and verify its sufficient prime-certificate semantics."""
    double_rough = 0
    cross = 0
    rows: list[dict[str, object]] = []
    prime_in_double_rough = False
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        row = mirror_cross_cutoff_point(k, radius, cutoff)
        rows.append(row)
        if not bool(row["double_rough"]):
            continue
        double_rough += 1
        cross += int(row["cross_overlap_multiplicity"])
        prime_in_double_rough = prime_in_double_rough or bool(row["prime_side"])
    separator_sum = double_rough - cross
    if separator_sum > 0 and not prime_in_double_rough:
        raise AssertionError("positive aggregate separator fired without a double-rough prime side")
    return {
        "k": k,
        "cutoff": cutoff,
        "double_rough_radius_count": double_rough,
        "cross_overlap_sum": cross,
        "aggregate_separator": separator_sum,
        "positive_is_prime_certificate": separator_sum <= 0 or prime_in_double_rough,
        "prime_side_inside_double_rough_subsystem": prime_in_double_rough,
        "rows": tuple(rows),
    }


def cross_local_model(k: int, cutoff: int) -> dict[str, object]:
    """Return the exact finite medium-prime local-model coefficient 1-(L^2-Q2)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (2 <= cutoff < k):
        raise ValueError("cutoff must satisfy 2<=cutoff<k")
    M = k * (k + 1)
    primes: list[int] = []
    for value in range(cutoff + 1, k + 1):
        if value % 2 == 0 or M % value == 0:
            continue
        trial = 3
        prime = value >= 3
        while trial * trial <= value:
            if value % trial == 0:
                prime = False
                break
            trial += 2
        if prime:
            primes.append(value)
    L = sum((Fraction(1, p) for p in primes), start=Fraction(0, 1))
    Q2 = sum((Fraction(1, p * p) for p in primes), start=Fraction(0, 1))
    cross_ratio = L * L - Q2
    return {
        "k": k,
        "cutoff": cutoff,
        "medium_transverse_primes": tuple(primes),
        "harmonic_mass_L": L,
        "diagonal_square_mass_Q2": Q2,
        "ordered_cross_overlap_local_ratio": cross_ratio,
        "quadratic_separator_local_coefficient": Fraction(1, 1) - cross_ratio,
        "positive_local_model_margin": cross_ratio < 1,
        "dimension_two_standard_sieve_warning": (
            "For power cutoffs z=k^alpha, local positivity needs alpha>e^-1, "
            "whereas a DHR dimension-two lower sieve with level D~k needs alpha<1/4; "
            "these regions are disjoint."
        ),
    }
