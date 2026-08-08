"""CRT idempotent encoding of centered mirror support.

The Chinese-remainder/idempotent facts used here are classical algebra.  The
project-specific pressure-test constraint is the bounded integer lift
``1 <= r < k`` tied to the square-basin center M=k(k+1).

Nothing in this module proves Legendre's conjecture.
"""

from __future__ import annotations

from math import gcd

from .alexander_descent import squarefree_product
from .legendre import anchor_product
from .mirror import anchor_pair_survival, mirror_pair, mirror_support_separation


def mirror_pairwise_coprime(k: int, r: int) -> dict[str, int]:
    """Verify that an anchor-surviving mirror triple is pairwise coprime.

    For a surviving radius r, gcd(r,k(k+1))=1.  The two mirror states are odd,
    and every common divisor of M-r and M+r must then divide both M and r.
    """
    lower, upper, center = mirror_pair(k, r)
    anchor = anchor_pair_survival(k, r)
    if not bool(anchor["survives"]):
        raise ValueError("radius must survive the anchor sieve")

    center_radius = gcd(center, r)
    lower_center = gcd(lower, center)
    upper_center = gcd(upper, center)
    lower_upper = gcd(lower, upper)
    if (center_radius, lower_center, upper_center, lower_upper) != (1, 1, 1, 1):
        raise AssertionError("surviving mirror triple must be pairwise coprime")
    return {
        "center_radius_gcd": center_radius,
        "lower_center_gcd": lower_center,
        "upper_center_gcd": upper_center,
        "lower_upper_gcd": lower_upper,
    }


def mirror_idempotent(k: int, r: int) -> dict[str, object]:
    """Encode the two nonempty transverse supports by one CRT idempotent.

    Let D be the square-free product of all transverse small primes occurring on
    either side.  If both sides have nonempty support, M is invertible mod D and

        u = r*M^{-1} (mod D),
        u^2 = 1 (mod D),
        e = (1+u)/2 (mod D),
        e^2 = e (mod D).

    The lower support is exactly the prime set where e=1; the upper support is
    exactly the set where e=0.
    """
    mirror_pairwise_coprime(k, r)
    data = mirror_support_separation(k, r)
    lower_support = sorted(data["lower_support"])
    upper_support = sorted(data["upper_support"])
    if not lower_support or not upper_support:
        raise ValueError("both transverse supports must be nonempty")

    support = sorted(lower_support + upper_support)
    modulus = squarefree_product(support)
    center = int(data["center"])
    if gcd(center, modulus) != 1:
        raise AssertionError("transverse support modulus must be coprime to center")
    if modulus % 2 == 0:
        raise AssertionError("transverse support modulus must be odd")

    center_inverse = pow(center, -1, modulus)
    involution = (r * center_inverse) % modulus
    if (involution * involution) % modulus != 1 % modulus:
        raise AssertionError("normalized mirror radius must square to one")

    inverse_two = pow(2, -1, modulus)
    idempotent = ((1 + involution) * inverse_two) % modulus
    if (idempotent * idempotent - idempotent) % modulus != 0:
        raise AssertionError("mirror CRT selector must be idempotent")

    lower_product = squarefree_product(lower_support)
    upper_product = squarefree_product(upper_support)
    if gcd(idempotent - 1, modulus) != lower_product:
        raise AssertionError("idempotent failed to recover lower support")
    if gcd(idempotent, modulus) != upper_product:
        raise AssertionError("idempotent failed to recover upper support")
    if lower_product * upper_product != modulus:
        raise AssertionError("support partition failed to factor modulus")

    lower, upper, _center = mirror_pair(k, r)
    if gcd(center - r, modulus) != lower_product:
        raise AssertionError("lower mirror gcd failed to recover support")
    if gcd(center + r, modulus) != upper_product:
        raise AssertionError("upper mirror gcd failed to recover support")
    if lower != center - r or upper != center + r:
        raise AssertionError("mirror state reconstruction failed")

    return {
        "radius": r,
        "center": center,
        "modulus": modulus,
        "support": support,
        "lower_support": lower_support,
        "upper_support": upper_support,
        "lower_product": lower_product,
        "upper_product": upper_product,
        "involution": involution,
        "idempotent": idempotent,
    }


def bounded_idempotent_lifts(
    k: int, support: list[int], idempotent: int, require_anchor_survival: bool = True
) -> list[int]:
    """Return all radii 1<=r<k realizing a fixed CRT idempotent sign pattern.

    For D=product(support), e^2=e mod D and u=2e-1, every realizing radius is

        r = k(k+1) * u (mod D).

    Thus the radii form one arithmetic progression modulo D.  The optional
    anchor filter retains only genuine surviving mirror radii.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if not support or len(support) != len(set(support)):
        raise ValueError("support must be nonempty and distinct")
    modulus = squarefree_product(sorted(support))
    center = k * (k + 1)
    if gcd(center, modulus) != 1:
        raise ValueError("support modulus must be transverse to the center")
    if modulus % 2 == 0:
        raise ValueError("transverse support modulus must be odd")
    if isinstance(idempotent, bool) or not isinstance(idempotent, int):
        raise ValueError("idempotent must be an integer")
    e = idempotent % modulus
    if (e * e - e) % modulus != 0:
        raise ValueError("value is not idempotent modulo the support product")
    if e in (0, 1):
        raise ValueError("a two-sided mirror partition requires a nontrivial idempotent")

    involution = (2 * e - 1) % modulus
    residue = (center * involution) % modulus
    if residue == 0:
        raise AssertionError("transverse bounded lift cannot have zero residue")

    lifts: list[int] = []
    radius = residue
    while radius < k:
        if radius >= 1:
            if not require_anchor_survival or gcd(radius, anchor_product(k)) == 1:
                lifts.append(radius)
        radius += modulus
    return lifts


def bounded_lift_capacity(k: int, support: list[int], idempotent: int) -> dict[str, int]:
    """Return the unfiltered and anchor-surviving bounded-lift capacities."""
    modulus = squarefree_product(sorted(support))
    center = k * (k + 1)
    e = idempotent % modulus
    if (e * e - e) % modulus != 0 or e in (0, 1):
        raise ValueError("a nontrivial idempotent is required")
    if gcd(center, modulus) != 1:
        raise ValueError("support modulus must be transverse to the center")

    involution = (2 * e - 1) % modulus
    first = (center * involution) % modulus
    if first == 0 or first >= k:
        unfiltered = 0
    else:
        unfiltered = 1 + (k - 1 - first) // modulus
    surviving = len(bounded_idempotent_lifts(k, support, e, True))
    if surviving > unfiltered:
        raise AssertionError("anchor filtering cannot increase lift capacity")
    return {
        "modulus": modulus,
        "first_radius": first,
        "unfiltered_capacity": unfiltered,
        "surviving_capacity": surviving,
    }
