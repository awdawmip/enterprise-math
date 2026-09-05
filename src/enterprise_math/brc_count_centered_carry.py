"""Exact count-centered carry / valuation-holonomy tools for BRC research.

This module is an exact finite-arithmetic companion to the T0_BRC family.  It
keeps positive branch weights and signed observer/deconvolution data separately:

* carry selection and prime-power branch weights are positive/discrete;
* count-centering is represented exactly with ``Fraction`` or symbolic gamma;
* prime logarithms are retained as formal valuation/log coordinates;
* the Mobius-log deconvolver is a signed observer identity, not positive path mass.

No routine in this module proves an asymptotic bound or the Riemann hypothesis.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable, Mapping

PrimeValuations = tuple[tuple[int, int], ...]


def _require_positive_int(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def factor_positive_integer(value: int) -> PrimeValuations:
    """Return the prime factorization of one positive integer."""
    n = _require_positive_int("value", value)
    factors: dict[int, int] = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    p = 3
    while p <= isqrt(n):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return tuple(sorted(factors.items()))


def mobius(value: int) -> int:
    """Exact Mobius function on positive integers."""
    n = _require_positive_int("value", value)
    factors = factor_positive_integer(n)
    if any(exponent > 1 for _prime, exponent in factors):
        return 0
    return -1 if len(factors) % 2 else 1


def primes_up_to(limit: int) -> tuple[int, ...]:
    """Reference-grade exact sieve used by finite BRC certificates."""
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    if limit < 2:
        return ()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return tuple(i for i in range(2, limit + 1) if sieve[i])


def carry_bit(n: int, m: int) -> int:
    """Return floor(2n/m)-2 floor(n/m), always 0 or 1."""
    n = _require_positive_int("n", n)
    m = _require_positive_int("m", m)
    value = (2 * n) // m - 2 * (n // m)
    if value not in (0, 1):
        raise AssertionError("doubling carry must be Boolean")
    return value


def divisor_summatory(n: int) -> int:
    """Return sum_{m<=n} floor(n/m) by exact quotient grouping."""
    n = _require_positive_int("n", n)
    total = 0
    left = 1
    while left <= n:
        quotient = n // left
        right = n // quotient
        total += quotient * (right - left + 1)
        left = right + 1
    return total


def carry_count(n: int) -> int:
    """Number of old branches m<=n whose next doubling carry is one."""
    n = _require_positive_int("n", n)
    result = divisor_summatory(2 * n) - 2 * divisor_summatory(n) - n
    if not 0 <= result <= n:
        raise AssertionError("carry count outside population")
    return result


def count_centered_coefficient(n: int, m: int) -> Fraction:
    """Exact c_m(n)-A_n/n coefficient on the old population m<=n."""
    n = _require_positive_int("n", n)
    m = _require_positive_int("m", m)
    if m > n:
        raise ValueError("count-centered old-branch coefficient requires m<=n")
    count = carry_count(n)
    return Fraction(n * carry_bit(n, m) - count, n)


def prime_power_base(value: int) -> int | None:
    """Return p when value=p^a for a prime p, else None."""
    n = _require_positive_int("value", value)
    if n == 1:
        return None
    factors = factor_positive_integer(n)
    return factors[0][0] if len(factors) == 1 else None


def prime_power_branch_weight(value: int) -> int:
    """Positive BRC branch weight: p on p^a, otherwise 1."""
    base = prime_power_base(value)
    return 1 if base is None else base


def _valuation_tuple(mapping: Mapping[int, int]) -> PrimeValuations:
    return tuple(sorted((p, e) for p, e in mapping.items() if e))


def valuation_product(valuations: Iterable[tuple[int, int]]) -> Fraction:
    """Materialize a finite prime-valuation vector as a positive Fraction."""
    numerator = 1
    denominator = 1
    for prime, exponent in valuations:
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime ** (-exponent)
    return Fraction(numerator, denominator)


def old_population_valuations(n: int) -> PrimeValuations:
    """Valuations of product of positive branch weights on m<=n.

    This product equals lcm(1,...,n), but the routine stays on prime-power
    branch coordinates.
    """
    n = _require_positive_int("n", n)
    result: dict[int, int] = {}
    for p in primes_up_to(n):
        power = p
        exponent = 0
        while power <= n:
            exponent += 1
            if power > n // p:
                break
            power *= p
        result[p] = exponent
    return _valuation_tuple(result)


def selected_old_valuations(n: int) -> PrimeValuations:
    """Valuations of product of weights on selected old carry branches."""
    n = _require_positive_int("n", n)
    result: dict[int, int] = {}
    for p in primes_up_to(n):
        power = p
        exponent = 0
        while power <= n:
            exponent += carry_bit(n, power)
            if power > n // p:
                break
            power *= p
        if exponent:
            result[p] = exponent
    return _valuation_tuple(result)


@dataclass(frozen=True)
class CountCenteredHolonomy:
    """Exact old-vs-selected valuation wedge before logarithmic readout."""

    n: int
    selected_count: int
    population_valuations: PrimeValuations
    selected_valuations: PrimeValuations
    holonomy_valuations: PrimeValuations

    @property
    def alpha(self) -> Fraction:
        return Fraction(self.selected_count, self.n)

    @property
    def population_product(self) -> Fraction:
        return valuation_product(self.population_valuations)

    @property
    def selected_product(self) -> Fraction:
        return valuation_product(self.selected_valuations)

    @property
    def omega(self) -> Fraction:
        return valuation_product(self.holonomy_valuations)

    def verify(self) -> bool:
        if self.n <= 0 or not 0 <= self.selected_count <= self.n:
            return False
        population = dict(self.population_valuations)
        selected = dict(self.selected_valuations)
        expected = {
            p: self.n * selected.get(p, 0) - self.selected_count * population.get(p, 0)
            for p in set(population) | set(selected)
        }
        return self.holonomy_valuations == _valuation_tuple(expected)


def count_centered_holonomy(n: int) -> CountCenteredHolonomy:
    n = _require_positive_int("n", n)
    count = carry_count(n)
    population = old_population_valuations(n)
    selected = selected_old_valuations(n)
    pop = dict(population)
    sel = dict(selected)
    holonomy = _valuation_tuple(
        {
            p: n * sel.get(p, 0) - count * pop.get(p, 0)
            for p in set(pop) | set(sel)
        }
    )
    state = CountCenteredHolonomy(n, count, population, selected, holonomy)
    if not state.verify():
        raise AssertionError("count-centered holonomy verification failed")
    return state


@dataclass(frozen=True)
class GammaAffine:
    """Exact formal ``constant + gamma_c * gamma_coeff`` value."""

    constant: int = 0
    gamma_coeff: int = 0

    def __add__(self, other: "GammaAffine") -> "GammaAffine":
        return GammaAffine(
            self.constant + other.constant,
            self.gamma_coeff + other.gamma_coeff,
        )

    def __neg__(self) -> "GammaAffine":
        return GammaAffine(-self.constant, -self.gamma_coeff)

    def __sub__(self, other: "GammaAffine") -> "GammaAffine":
        return self + (-other)

    def scale(self, integer: int) -> "GammaAffine":
        if isinstance(integer, bool) or not isinstance(integer, int):
            raise TypeError("scale must be an integer")
        return GammaAffine(self.constant * integer, self.gamma_coeff * integer)


def centered_geometry_ratio(numerator: int, denominator: int = 1) -> GammaAffine:
    """Exact formal K_gamma(x) at rational x=numerator/denominator.

    K_gamma(x) = sum_{k<=x}(floor(2x/k)-2 floor(x/k)-gamma_c).
    No floating logarithm or irrational gamma value is materialized.
    """
    numerator = _require_positive_int("numerator", numerator)
    denominator = _require_positive_int("denominator", denominator)
    population = numerator // denominator
    carry_total = 0
    for k in range(1, population + 1):
        carry_total += (2 * numerator) // (denominator * k) - 2 * (
            numerator // (denominator * k)
        )
    return GammaAffine(carry_total, -population)


@dataclass(frozen=True)
class GammaLogForm:
    """Formal constant plus GammaAffine coefficients of natural logarithms."""

    constant: GammaAffine
    log_terms: tuple[tuple[int, GammaAffine], ...]

    def normalized_prime_terms(self) -> tuple[tuple[int, GammaAffine], ...]:
        coefficients: dict[int, GammaAffine] = {}
        for base, coefficient in self.log_terms:
            if base <= 1:
                raise ValueError("log bases must be integers >1")
            for prime, exponent in factor_positive_integer(base):
                term = coefficient.scale(exponent)
                coefficients[prime] = coefficients.get(prime, GammaAffine()) + term
        return tuple(
            sorted(
                (prime, coefficient)
                for prime, coefficient in coefficients.items()
                if coefficient != GammaAffine()
            )
        )

    def equivalent(self, other: "GammaLogForm") -> bool:
        return (
            self.constant == other.constant
            and self.normalized_prime_terms() == other.normalized_prime_terms()
        )


def direct_gamma_centered_prime_error_form(n: int) -> GammaLogForm:
    """Formal exact sum (c_m-gamma_c)(Lambda(m)-1) over m<=n."""
    n = _require_positive_int("n", n)
    geometry = centered_geometry_ratio(n)
    terms: list[tuple[int, GammaAffine]] = []
    for p in primes_up_to(n):
        power = p
        coefficient = GammaAffine()
        while power <= n:
            coefficient = coefficient + GammaAffine(carry_bit(n, power), -1)
            if power > n // p:
                break
            power *= p
        if coefficient != GammaAffine():
            terms.append((p, coefficient))
    return GammaLogForm(constant=-geometry, log_terms=tuple(terms))


def mobius_divisor_deconvolution_form(n: int) -> GammaLogForm:
    """Formal exact -sum_d b(d) K_gamma(n/d) with b(1)=1, b(d)=mu(d)log d."""
    n = _require_positive_int("n", n)
    constant = -centered_geometry_ratio(n)
    terms: list[tuple[int, GammaAffine]] = []
    for d in range(2, n + 1):
        mu = mobius(d)
        if mu == 0:
            continue
        coefficient = centered_geometry_ratio(n, d).scale(-mu)
        if coefficient != GammaAffine():
            terms.append((d, coefficient))
    return GammaLogForm(constant=constant, log_terms=tuple(terms))


@dataclass(frozen=True)
class HardPrimeSkeletonThickness:
    """n-th-power skeleton/thickness of the hard-prime holonomy."""

    n: int
    selected_count: int
    hard_primes: tuple[int, ...]
    unselected_hard_primes: tuple[int, ...]
    skeleton_valuations: PrimeValuations
    thickness_valuations: PrimeValuations

    def verify(self) -> bool:
        remainder = (-self.selected_count) % self.n
        if not 0 <= remainder < self.n:
            return False
        expected_skeleton = tuple((p, remainder) for p in self.hard_primes if remainder)
        if self.skeleton_valuations != expected_skeleton:
            return False
        expected_thickness: list[tuple[int, int]] = []
        for p in self.hard_primes:
            exponent = self.n * carry_bit(self.n, p) - self.selected_count
            quotient, residue = divmod(exponent, self.n)
            if residue != remainder:
                return False
            if quotient:
                expected_thickness.append((p, quotient))
        return self.thickness_valuations == tuple(expected_thickness)


def hard_prime_skeleton_thickness(n: int) -> HardPrimeSkeletonThickness:
    n = _require_positive_int("n", n)
    count = carry_count(n)
    root = isqrt(n)
    hard = tuple(p for p in primes_up_to(n) if p > root)
    unselected = tuple(p for p in hard if carry_bit(n, p) == 0)
    remainder = (-count) % n
    thickness: list[tuple[int, int]] = []
    for p in hard:
        exponent = n * carry_bit(n, p) - count
        quotient, residue = divmod(exponent, n)
        if residue != remainder:
            raise AssertionError("hard-prime residue mismatch")
        if quotient:
            thickness.append((p, quotient))
    state = HardPrimeSkeletonThickness(
        n=n,
        selected_count=count,
        hard_primes=hard,
        unselected_hard_primes=unselected,
        skeleton_valuations=tuple((p, remainder) for p in hard if remainder),
        thickness_valuations=tuple(thickness),
    )
    if not state.verify():
        raise AssertionError("hard-prime skeleton/thickness verification failed")
    return state


def divisor_count(value: int) -> int:
    """Exact divisor-count function tau(value)."""
    n = _require_positive_int("value", value)
    result = 1
    for _prime, exponent in factor_positive_integer(n):
        result *= exponent + 1
    return result


@dataclass(frozen=True)
class ReciprocalQuotientShell:
    """One exact d-shell for x=n/d under the fixed gamma-centered geometry.

    For every integer ``d`` in ``[lower_d, upper_d]`` we have
    ``floor(n/d)=quotient``.  Inside the shell the geometry has only one
    possible jump, at ``d<=midpoint_upper_d``:

    ``K_gamma(n/d) = base + (tau(2r+1)-1) * 1[d<=midpoint_upper_d]``.

    The ``-1`` is essential: when ``2x`` crosses the odd integer ``2r+1``,
    the divisor summatory function jumps by ``tau(2r+1)`` while the count of
    upper branches lying outside the old population jumps by one.
    """

    n: int
    quotient: int
    lower_d: int
    midpoint_upper_d: int
    upper_d: int
    base: GammaAffine
    jump: int

    @property
    def nonempty(self) -> bool:
        return self.lower_d <= self.upper_d

    def contains(self, d: int) -> bool:
        return self.nonempty and self.lower_d <= d <= self.upper_d

    def geometry(self, d: int) -> GammaAffine:
        if not self.contains(d):
            raise ValueError("d does not belong to this reciprocal quotient shell")
        return self.base + GammaAffine(self.jump if d <= self.midpoint_upper_d else 0, 0)


def reciprocal_quotient_shell(n: int, quotient: int, *, minimum_d: int = 2) -> ReciprocalQuotientShell:
    """Compile one exact reciprocal shell for the Mobius-log d-variable."""
    n = _require_positive_int("n", n)
    r = _require_positive_int("quotient", quotient)
    minimum_d = _require_positive_int("minimum_d", minimum_d)
    if r > n:
        raise ValueError("quotient cannot exceed n")
    lower = max(minimum_d, n // (r + 1) + 1)
    upper = n // r
    midpoint_upper = min(upper, (2 * n) // (2 * r + 1))
    base = GammaAffine(carry_count(r), -r)
    jump = divisor_count(2 * r + 1) - 1
    return ReciprocalQuotientShell(
        n=n,
        quotient=r,
        lower_d=lower,
        midpoint_upper_d=midpoint_upper,
        upper_d=upper,
        base=base,
        jump=jump,
    )


def reciprocal_shells(n: int, *, minimum_d: int = 2) -> tuple[ReciprocalQuotientShell, ...]:
    """Return all nonempty quotient shells covering ``minimum_d<=d<=n``."""
    n = _require_positive_int("n", n)
    minimum_d = _require_positive_int("minimum_d", minimum_d)
    if minimum_d > n:
        return ()
    shells: list[ReciprocalQuotientShell] = []
    d = minimum_d
    while d <= n:
        r = n // d
        shell = reciprocal_quotient_shell(n, r, minimum_d=minimum_d)
        if not shell.nonempty or not shell.contains(d):
            raise AssertionError("reciprocal shell compiler failed to cover current d")
        shells.append(shell)
        d = shell.upper_d + 1
    return tuple(shells)


def mobius_shell_deconvolution_form(n: int) -> GammaLogForm:
    """Same exact deconvolution as ``mobius_divisor_deconvolution_form``, shell-compiled.

    This implementation is deliberately formal: it groups the geometry by
    reciprocal quotient shells but retains the signed ``mu(d) log d`` observer
    coefficients without turning them into positive path mass.
    """
    n = _require_positive_int("n", n)
    constant = -centered_geometry_ratio(n)
    terms: list[tuple[int, GammaAffine]] = []
    for shell in reciprocal_shells(n):
        for d in range(shell.lower_d, shell.upper_d + 1):
            mu = mobius(d)
            if mu == 0:
                continue
            coefficient = shell.geometry(d).scale(-mu)
            if coefficient != GammaAffine():
                terms.append((d, coefficient))
    return GammaLogForm(constant=constant, log_terms=tuple(terms))
