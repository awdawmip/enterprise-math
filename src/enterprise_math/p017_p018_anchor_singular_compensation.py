"""P017 residual hard-core: exact anchor/singular compensation on finite wheels.

P017 #150 gives the local forbidden lift-index count for every odd prime p:

    nu_p = 1  if p divides M*S,
    nu_p = 2  otherwise,

where M=k(k+1), S=ab is the coprime full-core product, and gcd(M,S)=1.
For a finite odd-prime wheel W the exact locally allowed density is therefore

    prod_p (p-nu_p)/p.

Compare this with the independent two-prime baseline

    prod_p ((p-1)/p)^2.

Their ratio (the finite-wheel singular factor) is

    prod_{p|MS} p/(p-1)
    * prod_{p∤MS} p(p-2)/(p-1)^2.

The anchor-surviving radius density contributed by wheel primes dividing M is

    prod_{p|M} (p-1)/p.

Because gcd(M,S)=1, multiplying anchor density by the singular factor cancels
**every M-prime inflation exactly, prime by prime**.  The normalized ratio is

    prod_{p|S} p/(p-1)
    * prod_{p∤MS} p(p-2)/(p-1)^2.

This identifies the correct analytic normalization for any later global sieve
bound: anchor sparsity and M-dependent prime-pair singular inflation are not two
independent effects.

There is a second exact identity.  If the wheel contains every prime divisor of
S, then

    (1/S) * prod_{p|S} p/(p-1) = 1/phi(S).

Thus the natural cell-length weight k/(2S), after core-prime singular
normalization, becomes k/(2 phi(S)).  This does not prove a prime-pair upper
bound; it fixes the arithmetic weight that such an upper bound must carry.

All returned rational quantities are represented by reduced integer
numerator/denominator pairs.  No float or true division is used.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _reduced_pair(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def _multiply_pairs(*pairs: tuple[int, int]) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for left, right in pairs:
        numerator *= left
        denominator *= right
    return _reduced_pair(numerator, denominator)


def _validated_wheel(primes: tuple[int, ...]) -> tuple[int, ...]:
    if not primes:
        raise ValueError("wheel primes must be nonempty")
    if len(set(primes)) != len(primes):
        raise ValueError("wheel primes must be distinct")
    normalized = tuple(sorted(primes))
    for prime in normalized:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime < 3
            or prime % 2 == 0
            or not is_prime(prime)
        ):
            raise ValueError("wheel entries must be distinct odd primes")
    return normalized


def euler_phi(value: int) -> int:
    """Return phi(value) by exact trial factorization."""
    _require_positive("value", value)
    remaining = value
    result = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result -= result // prime
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


def finite_wheel_compensation(
    center: int,
    core_product: int,
    primes: tuple[int, ...],
) -> dict[str, object]:
    """Return the exact finite-wheel anchor/singular compensation identity."""
    _require_positive("center", center)
    _require_positive("core_product", core_product)
    wheel = _validated_wheel(primes)
    if gcd(center, core_product) != 1:
        raise ValueError("center and full-core product must be coprime")

    allowed_count = 1
    wheel_modulus = 1
    baseline_numerator = 1
    baseline_denominator = 1
    anchor_numerator = 1
    anchor_denominator = 1
    core_numerator = 1
    core_denominator = 1
    generic_numerator = 1
    generic_denominator = 1
    local_rows: list[dict[str, int | str]] = []

    for prime in wheel:
        divides_center = center % prime == 0
        divides_core = core_product % prime == 0
        if divides_center and divides_core:
            raise AssertionError("coprime center/core product shared a wheel prime")

        exceptional = divides_center or divides_core
        forbidden = 1 if exceptional else 2
        allowed = prime - forbidden
        if allowed <= 0:
            raise AssertionError("odd local wheel unexpectedly lost every residue")

        allowed_count *= allowed
        wheel_modulus *= prime
        baseline_numerator *= (prime - 1) ** 2
        baseline_denominator *= prime * prime

        if divides_center:
            anchor_numerator *= prime - 1
            anchor_denominator *= prime
        if divides_core:
            core_numerator *= prime
            core_denominator *= prime - 1
        if not exceptional:
            generic_numerator *= prime * (prime - 2)
            generic_denominator *= (prime - 1) ** 2

        local_rows.append(
            {
                "prime": prime,
                "kind": (
                    "CENTER" if divides_center else "CORE" if divides_core else "GENERIC"
                ),
                "forbidden_count": forbidden,
                "allowed_count": allowed,
            }
        )

    allowed_density = _reduced_pair(allowed_count, wheel_modulus)
    baseline_density = _reduced_pair(baseline_numerator, baseline_denominator)

    # (A/P) / (B/P^2) = A*P/B.
    singular_factor = _reduced_pair(
        allowed_count * wheel_modulus,
        baseline_numerator,
    )
    anchor_density = _reduced_pair(anchor_numerator, anchor_denominator)
    anchor_normalized = _multiply_pairs(anchor_density, singular_factor)
    residual_product = _multiply_pairs(
        _reduced_pair(core_numerator, core_denominator),
        _reduced_pair(generic_numerator, generic_denominator),
    )
    if anchor_normalized != residual_product:
        raise AssertionError("M-prime singular inflation did not cancel anchor density")

    return {
        "center": center,
        "core_product": core_product,
        "wheel_primes": wheel,
        "wheel_modulus": wheel_modulus,
        "allowed_class_count": allowed_count,
        "allowed_density": allowed_density,
        "independent_pair_baseline_density": baseline_density,
        "finite_singular_factor": singular_factor,
        "anchor_density": anchor_density,
        "anchor_normalized_singular_factor": anchor_normalized,
        "core_inflation_factor": _reduced_pair(core_numerator, core_denominator),
        "generic_twin_factor": _reduced_pair(generic_numerator, generic_denominator),
        "local_rows": tuple(local_rows),
    }


def core_weight_totient_identity(
    core_product: int,
    primes: tuple[int, ...],
) -> dict[str, object]:
    """Certify (1/S)*prod_{p|S}p/(p-1)=1/phi(S).

    The supplied wheel must contain every prime divisor of S.  Extra odd primes
    are allowed and ignored by the core factor.
    """
    _require_positive("core_product", core_product)
    wheel = _validated_wheel(primes)
    if core_product % 2 == 0:
        raise ValueError("residual anchor-surviving full-core products are odd")

    remaining = core_product
    core_numerator = 1
    core_denominator = 1
    for prime in wheel:
        if remaining % prime != 0:
            continue
        core_numerator *= prime
        core_denominator *= prime - 1
        while remaining % prime == 0:
            remaining //= prime
    if remaining != 1:
        raise ValueError("wheel does not contain every prime divisor of core_product")

    normalized_cell_weight = _reduced_pair(
        core_numerator,
        core_denominator * core_product,
    )
    phi = euler_phi(core_product)
    totient_weight = _reduced_pair(1, phi)
    if normalized_cell_weight != totient_weight:
        raise AssertionError("core singular inflation did not convert 1/S to 1/phi(S)")

    return {
        "core_product": core_product,
        "phi": phi,
        "core_inflation_factor": _reduced_pair(core_numerator, core_denominator),
        "normalized_cell_weight": normalized_cell_weight,
        "totient_weight": totient_weight,
    }
