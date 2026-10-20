"""Signed full-core collision discriminant for P017.

For a lower mirror side M-r use signed point x=+r; for an upper side M+r use
x=-r.  Its exact full k-smooth core D then divides M-x.  Hence for any two
signed incidences, gcd(D_i,D_j) divides x_i-x_j; anchor survival makes all signed
points and full cores odd, so 2*gcd(D_i,D_j) divides the difference.

Multiplying over pairs yields a Vandermonde divisibility law coupling prime-power
resource reuse to radius geometry.  CG11 resolves the product law into exact
prime-power collision levels and gives an explicit finite multiplicity capacity
at every level p^e.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to
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


def _valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def prime_power_overlap_exponent(cores: tuple[int, ...], prime: int) -> int:
    """Return sum_{i<j} min(v_p(D_i),v_p(D_j)) for one prime."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be an integer >= 2")
    exponents: list[int] = []
    for core in cores:
        if isinstance(core, bool) or not isinstance(core, int) or core <= 0:
            raise ValueError("cores must be positive integers")
        exponents.append(_valuation(core, prime))
    return sum(
        min(exponents[i], exponents[j])
        for i in range(len(exponents))
        for j in range(i + 1, len(exponents))
    )


def prime_power_collision_capacity(
    k: int,
    incidences: tuple[tuple[int, str], ...],
    prime: int,
) -> dict[str, object]:
    """CG11: exact p^e collision spectrum with finite signed-radius capacity.

    Let m_{p,e} be the number of selected signed exact-core incidences whose
    full core is divisible by p^e.  Because every such signed point x satisfies

        x = M (mod p^e)

    and anchor-surviving signed radii are odd while M=k(k+1) is even, all these
    points lie in one residue class modulo 2*p^e.  The signed interval

        -(k-1) <= x <= k-1

    therefore gives the exact universal packing bound

        m_{p,e} <= floor((k-1)/p^e)+1.

    The p-adic exponent of the CG05 core-overlap product decomposes exactly as

        sum_{i<j} min(v_p(D_i),v_p(D_j))
          = sum_{e>=1} binom(m_{p,e},2).

    Consequently prime powers above k-1 cannot be reused at all: their capacity
    is one.  The returned ``universal_collision_bound`` sums the binomial
    capacities over all nontrivial reusable levels p^e<=k-1.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if not incidences:
        raise ValueError("at least one signed incidence is required")
    if len(set(incidences)) != len(incidences):
        raise ValueError("signed incidences must be distinct")
    if isinstance(prime, bool) or not isinstance(prime, int):
        raise ValueError("prime must be an integer")
    if prime not in primes_up_to(k) or prime == 2:
        raise ValueError("prime must be an odd prime <= k")
    center = k * (k + 1)
    if center % prime == 0:
        raise ValueError("prime must be transverse to the square-basin center")

    points: list[int] = []
    cores: list[int] = []
    for radius, side in incidences:
        point, core = _signed_incidence(k, radius, side)
        if point in points:
            raise ValueError("signed coordinates must be distinct")
        points.append(point)
        cores.append(core)

    exponents = [_valuation(core, prime) for core in cores]
    max_exponent = max(exponents, default=0)
    level_data: list[dict[str, int]] = []
    level_collision_sum = 0
    power = prime
    for exponent in range(1, max_exponent + 1):
        indices = [i for i, value in enumerate(exponents) if value >= exponent]
        multiplicity = len(indices)
        capacity = (k - 1) // power + 1
        if multiplicity > capacity:
            raise AssertionError("prime-power reuse exceeds signed-radius packing capacity")

        if indices:
            expected_residue = (center + power) % (2 * power)
            residues = {points[i] % (2 * power) for i in indices}
            if residues != {expected_residue}:
                raise AssertionError("prime-power incidences do not share one signed residue class")

        collisions = multiplicity * (multiplicity - 1) // 2
        level_collision_sum += collisions
        level_data.append(
            {
                "exponent": exponent,
                "power": power,
                "multiplicity": multiplicity,
                "capacity": capacity,
                "collisions": collisions,
            }
        )
        power *= prime

    actual_overlap = prime_power_overlap_exponent(tuple(cores), prime)
    if level_collision_sum != actual_overlap:
        raise AssertionError("prime-power level collisions do not reconstruct p-adic overlap exponent")

    universal_collision_bound = 0
    power = prime
    while power <= k - 1:
        capacity = (k - 1) // power + 1
        universal_collision_bound += capacity * (capacity - 1) // 2
        power *= prime
    if actual_overlap > universal_collision_bound:
        raise AssertionError("actual p-adic overlap exceeds universal collision capacity")

    return {
        "k": k,
        "prime": prime,
        "points": tuple(points),
        "cores": tuple(cores),
        "levels": tuple(level_data),
        "actual_overlap_exponent": actual_overlap,
        "universal_collision_bound": universal_collision_bound,
    }
