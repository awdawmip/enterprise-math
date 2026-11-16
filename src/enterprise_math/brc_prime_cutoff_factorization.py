"""Exact prime-cutoff factorization for the BRC Möbius/divisor connection.

For an integer cutoff y, split every integer uniquely into its y-smooth part
(all prime factors <=y) and its y-rough part (all prime factors >y).  At the
Dirichlet-incidence level this gives exact factorizations

    1 = Z_<=y * Z_>y,
    mu = mu_<=y * mu_>y,

and logarithmic connection identities

    mu_<=y * L(Z_<=y) = Lambda_<=y,
    mu_>y  * L(Z_>y)  = Lambda_>y.

These are finite algebraic identities.  They do not estimate the remaining
large-prime observer and do not prove RH.
"""
from __future__ import annotations

from dataclasses import dataclass

from .brc_count_centered_carry import (
    PrimeValuations,
    _require_positive_int,
    factor_positive_integer,
    mobius,
)


def prime_cutoff_parts(value: int, cutoff: int) -> tuple[int, int]:
    """Return the unique (smooth_part, rough_part) across a prime cutoff."""
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    smooth = 1
    rough = 1
    for prime, exponent in factor_positive_integer(n):
        target = prime**exponent
        if prime <= y:
            smooth *= target
        else:
            rough *= target
    if smooth * rough != n:
        raise AssertionError("prime cutoff factorization failed")
    return smooth, rough


def small_divisor_lift(value: int, cutoff: int) -> int:
    """Coefficient of Z_<=y: 1 exactly on y-smooth integers."""
    _smooth, rough = prime_cutoff_parts(value, cutoff)
    return int(rough == 1)


def rough_divisor_lift(value: int, cutoff: int) -> int:
    """Coefficient of Z_>y: 1 exactly on y-rough integers."""
    smooth, _rough = prime_cutoff_parts(value, cutoff)
    return int(smooth == 1)


def small_mobius(value: int, cutoff: int) -> int:
    """Coefficient of mu_<=y, supported on y-smooth squarefree integers."""
    return mobius(value) if small_divisor_lift(value, cutoff) else 0


def rough_mobius(value: int, cutoff: int) -> int:
    """Coefficient of mu_>y, supported on y-rough squarefree integers."""
    return mobius(value) if rough_divisor_lift(value, cutoff) else 0


def _divisors(value: int) -> tuple[int, ...]:
    n = _require_positive_int("value", value)
    out = [1]
    for prime, exponent in factor_positive_integer(n):
        old = tuple(out)
        power = 1
        for _ in range(exponent):
            power *= prime
            out.extend(d * power for d in old)
    return tuple(sorted(out))


def cutoff_mobius_convolution(value: int, cutoff: int) -> int:
    """Exact (mu_<=y * mu_>y)(n), equal to mu(n)."""
    n = _require_positive_int("value", value)
    return sum(
        small_mobius(d, cutoff) * rough_mobius(n // d, cutoff)
        for d in _divisors(n)
    )


def cutoff_divisor_lift_convolution(value: int, cutoff: int) -> int:
    """Exact (Z_<=y * Z_>y)(n), equal to one."""
    n = _require_positive_int("value", value)
    return sum(
        small_divisor_lift(d, cutoff) * rough_divisor_lift(n // d, cutoff)
        for d in _divisors(n)
    )


def _valuation_add(target: dict[int, int], prime: int, amount: int) -> None:
    if amount:
        target[prime] = target.get(prime, 0) + amount
        if target[prime] == 0:
            del target[prime]


def cutoff_log_connection_valuations(
    value: int,
    cutoff: int,
    *,
    rough: bool = False,
) -> PrimeValuations:
    """Formal prime-log coordinates of mu_side * L(Z_side) at one integer.

    The result is ``((p,1),)`` when ``value`` is a positive power of a prime p
    on the selected side of the cutoff, and empty otherwise.  This is the
    exact finite-coordinate version of the truncated von Mangoldt connection.
    """
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    mu_side = rough_mobius if rough else small_mobius
    z_side = rough_divisor_lift if rough else small_divisor_lift
    coefficients: dict[int, int] = {}
    for d in _divisors(n):
        mu_d = mu_side(d, y)
        q = n // d
        if mu_d == 0 or z_side(q, y) == 0:
            continue
        for prime, exponent in factor_positive_integer(q):
            _valuation_add(coefficients, prime, mu_d * exponent)
    return tuple(sorted(coefficients.items()))


def expected_cutoff_lambda_valuations(
    value: int,
    cutoff: int,
    *,
    rough: bool = False,
) -> PrimeValuations:
    """Expected formal log coordinate for Lambda on one cutoff side."""
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    factors = factor_positive_integer(n)
    if len(factors) != 1:
        return ()
    prime, _exponent = factors[0]
    belongs = prime > y if rough else prime <= y
    return ((prime, 1),) if belongs else ()


@dataclass(frozen=True)
class PrimeCutoffCertificate:
    value: int
    cutoff: int
    smooth_part: int
    rough_part: int
    mobius_recoalesced: int
    divisor_lift_recoalesced: int
    small_connection: PrimeValuations
    rough_connection: PrimeValuations

    def verify(self) -> bool:
        return (
            self.smooth_part * self.rough_part == self.value
            and self.mobius_recoalesced == mobius(self.value)
            and self.divisor_lift_recoalesced == 1
            and self.small_connection
            == expected_cutoff_lambda_valuations(self.value, self.cutoff)
            and self.rough_connection
            == expected_cutoff_lambda_valuations(self.value, self.cutoff, rough=True)
        )


def prime_cutoff_certificate(value: int, cutoff: int) -> PrimeCutoffCertificate:
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    smooth, rough_part = prime_cutoff_parts(n, y)
    state = PrimeCutoffCertificate(
        value=n,
        cutoff=y,
        smooth_part=smooth,
        rough_part=rough_part,
        mobius_recoalesced=cutoff_mobius_convolution(n, y),
        divisor_lift_recoalesced=cutoff_divisor_lift_convolution(n, y),
        small_connection=cutoff_log_connection_valuations(n, y),
        rough_connection=cutoff_log_connection_valuations(n, y, rough=True),
    )
    if not state.verify():
        raise AssertionError("prime cutoff connection certificate failed")
    return state


def rough_mobius_degree(value: int, cutoff: int) -> int | None:
    """Number of rough prime factors when rough_mobius is nonzero, else None."""
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    if rough_mobius(n, y) == 0:
        return None
    return len(factor_positive_integer(n))


def rough_linear_on_block(block_max: int, cutoff: int) -> bool:
    """Sufficient exact check that rough Möbius support has degree <=1.

    If ``cutoff**2 >= block_max`` then two distinct primes strictly above the
    cutoff cannot have product <=block_max.  Prime powers are absent from
    Möbius support, so only 1 and single rough primes survive.
    """
    m = _require_positive_int("block_max", block_max)
    y = _require_positive_int("cutoff", cutoff)
    return y * y >= m
