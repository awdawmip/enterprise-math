"""Balanced Chen mirror criterion for the P017 consecutive-square basin.

For an anchor-surviving mirror radius r, P017 L043 gives

    gcd(M-r,M+r)=1,       M=k(k+1).

Both mirror states are odd and greater than one.  Hence if both were composite,
each would have at least two prime factors counted with multiplicity.  Therefore

    Omega((M-r)(M+r)) <= 3

forces at least one mirror side to be prime.  More precisely the pair is either
prime x prime or prime x P2, where P2 denotes an integer having at most two
prime factors counted with multiplicity.

This strong sufficient condition has an exact additive interpretation.  Put
N=2M.  A mirror witness is equivalent to a **balanced Chen representation**

    N = p + P2,
    |p-M| < k,

with p prime.  The second summand lies at the same distance from M.  Conversely,
any such balanced representation automatically has an anchor-surviving radius:
if g divides both M and r=|p-M|, then g divides p; since g<=r<k<p, one has g=1.

The balanced window has radius k asymptotic to N^(1/2)/sqrt(2).  This is much
narrower than currently known general centered Chen theorems and is recorded as
a research target, not as a proved all-k statement.

Independent discovery pressure found no failure of the Omega<=3 mirror target
for 4<=k<=3000.  That finite observation is TEST evidence only.  The stronger
requirement that both mirror sides be prime is false already at finite scales;
for example k=17 has no symmetric prime mirror pair, while r=1 gives
305=5*61 and 307 prime and therefore an Omega=3 balanced-Chen witness.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_center, surviving_mirror_triple


def big_omega(value: int) -> int:
    """Return the number of prime factors counted with multiplicity."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    count = 0
    while remaining % 2 == 0:
        remaining //= 2
        count += 1
    divisor = 3
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            remaining //= divisor
            count += 1
        divisor += 2
    if remaining > 1:
        count += 1
    return count


def mirror_product_omega(k: int, radius: int) -> dict[str, object]:
    """Return the exact multiplicative depth of one surviving mirror pair."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1<=radius<k")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    lower, upper = mirror_pair(k, radius)
    surviving_mirror_triple(k, radius)  # consumes the existing pairwise-coprime theorem
    lower_omega = big_omega(lower)
    upper_omega = big_omega(upper)
    total = lower_omega + upper_omega
    lower_prime = is_prime(lower)
    upper_prime = is_prime(upper)
    if (lower_omega == 1) != lower_prime or (upper_omega == 1) != upper_prime:
        raise AssertionError("Omega=1 failed primality equivalence")
    if total <= 3 and not (lower_prime or upper_prime):
        raise AssertionError("coprime odd mirror pair with Omega<=3 has no prime side")
    return {
        "k": k,
        "radius": radius,
        "center": mirror_center(k),
        "lower_state": lower,
        "upper_state": upper,
        "lower_omega": lower_omega,
        "upper_omega": upper_omega,
        "mirror_product_omega": total,
        "lower_prime": lower_prime,
        "upper_prime": upper_prime,
        "omega_at_most_three_forces_prime_side": total <= 3,
    }


def balanced_chen_mirror_witness(k: int, radius: int) -> dict[str, object]:
    """Certify the exact prime+P2 interpretation when total mirror Omega<=3."""
    data = mirror_product_omega(k, radius)
    if int(data["mirror_product_omega"]) > 3:
        raise ValueError("mirror product must have Omega<=3")
    M = int(data["center"])
    lower = int(data["lower_state"])
    upper = int(data["upper_state"])
    if bool(data["lower_prime"]):
        prime = lower
        almost_prime = upper
        prime_side = "lower"
    elif bool(data["upper_prime"]):
        prime = upper
        almost_prime = lower
        prime_side = "upper"
    else:  # protected by mirror_product_omega
        raise AssertionError("Omega<=3 witness has no prime side")
    p2_omega = big_omega(almost_prime)
    if p2_omega > 2:
        raise AssertionError("opposite summand is not P2")
    N = 2 * M
    if prime + almost_prime != N:
        raise AssertionError("mirror pair failed balanced additive reconstruction")
    if abs(prime - M) != radius or abs(almost_prime - M) != radius:
        raise AssertionError("balanced Chen summands lost common mirror radius")
    return {
        **data,
        "even_target": N,
        "prime_summand": prime,
        "p2_summand": almost_prime,
        "p2_omega": p2_omega,
        "prime_side": prime_side,
        "balanced_window_radius": radius,
        "balanced_window_ceiling": k - 1,
        "balanced_chen_representation": True,
        "legendre_certificate": True,
    }


def least_mirror_product_omega(k: int) -> dict[str, object]:
    """Bounded discovery diagnostic: minimize total Omega over surviving radii."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    best: dict[str, object] | None = None
    symmetric_prime_pair = False
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        row = mirror_product_omega(k, radius)
        if bool(row["lower_prime"]) and bool(row["upper_prime"]):
            symmetric_prime_pair = True
        if best is None or int(row["mirror_product_omega"]) < int(best["mirror_product_omega"]):
            best = row
    if best is None:
        raise AssertionError("no anchor-surviving mirror radius")
    return {
        "k": k,
        "least_mirror_product_omega": int(best["mirror_product_omega"]),
        "least_witness_radius": int(best["radius"]),
        "least_witness_lower": int(best["lower_state"]),
        "least_witness_upper": int(best["upper_state"]),
        "omega_at_most_three_witness": int(best["mirror_product_omega"]) <= 3,
        "symmetric_prime_pair_exists": symmetric_prime_pair,
        "best_row": best,
    }
