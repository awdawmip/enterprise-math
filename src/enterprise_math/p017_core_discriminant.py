"""Signed full-core collision discriminant for P017.

For a lower mirror side M-r use signed point x=+r; for an upper side M+r use
x=-r.  Its exact full k-smooth core D then divides M-x.  Hence for any two
signed incidences, gcd(D_i,D_j) divides x_i-x_j; anchor survival makes all signed
points and full cores odd, so 2*gcd(D_i,D_j) divides the difference.

Multiplying over pairs yields a Vandermonde divisibility law coupling prime-power
resource reuse to radius geometry.
"""

from __future__ import annotations

from math import gcd

from .p017_core_cell_lattice import exact_full_core_pair


def _signed_incidence(k: int, radius: int, side: str) -> tuple[int, int]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    if side not in ("lower", "upper"):
        raise ValueError("side must be 'lower' or 'upper'")
    center = k * (k + 1)
    if gcd(radius, center) != 1:
        raise ValueError("radius must survive the anchor sieve")
    lower, upper = exact_full_core_pair(k, radius)
    if side == "lower":
        return radius, lower
    return -radius, upper


def signed_core_discriminant(
    k: int, incidences: tuple[tuple[int, str], ...]
) -> dict[str, object]:
    """CG05: full-core collision product divides the signed Vandermonde.

    For m distinct signed incidences (x_i,D_i),

        2^(m choose 2) * product_{i<j} gcd(D_i,D_j)
            | product_{i<j} |x_i-x_j|.

    The left side is a prime-power collision budget.  At a fixed prime p its
    exponent contributed by the core-overlap product is

        sum_{i<j} min(v_p(D_i), v_p(D_j)).
    """
    if not incidences:
        raise ValueError("at least one signed incidence is required")
    if len(set(incidences)) != len(incidences):
        raise ValueError("signed incidences must be distinct")

    points: list[int] = []
    cores: list[int] = []
    for radius, side in incidences:
        point, core = _signed_incidence(k, radius, side)
        if point in points:
            raise ValueError("signed coordinates must be distinct")
        points.append(point)
        cores.append(core)

    overlap_product = 1
    vandermonde = 1
    pair_data: list[tuple[int, int, int, int]] = []
    pair_count = 0
    for i, left in enumerate(points):
        for j in range(i + 1, len(points)):
            right = points[j]
            shared = gcd(cores[i], cores[j])
            difference = abs(left - right)
            if difference % (2 * shared) != 0:
                raise AssertionError("signed full-core gcd violated radius-difference divisibility")
            overlap_product *= shared
            vandermonde *= difference
            pair_count += 1
            pair_data.append((i, j, shared, difference))

    required = (2**pair_count) * overlap_product
    if vandermonde % required != 0:
        raise AssertionError("full-core collision discriminant failed")

    return {
        "k": k,
        "points": tuple(points),
        "cores": tuple(cores),
        "pair_count": pair_count,
        "core_overlap_product": overlap_product,
        "vandermonde": vandermonde,
        "required_divisor": required,
        "quotient": vandermonde // required,
        "pairs": tuple(pair_data),
    }


def prime_power_overlap_exponent(cores: tuple[int, ...], prime: int) -> int:
    """Return sum_{i<j} min(v_p(D_i),v_p(D_j)) for one prime."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be an integer >= 2")
    exponents: list[int] = []
    for core in cores:
        if isinstance(core, bool) or not isinstance(core, int) or core <= 0:
            raise ValueError("cores must be positive integers")
        value = core
        exponent = 0
        while value % prime == 0:
            exponent += 1
            value //= prime
        exponents.append(exponent)
    return sum(
        min(exponents[i], exponents[j])
        for i in range(len(exponents))
        for j in range(i + 1, len(exponents))
    )
