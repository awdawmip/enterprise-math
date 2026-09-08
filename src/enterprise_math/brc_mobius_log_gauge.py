"""Exact logarithmic gauge transfer for the Möbius/BRC deconvolution.

The centered carry geometry satisfies the exact inverse relation

    sum_{d<=x} mu(d) K_gamma(x/d) = c_1(x) - gamma_c.

At an integer scale n the right side is -gamma_c.  Therefore the logarithmic
observer coefficient can be gauge-shifted by the common scale log(n):

    sum mu(d) log(d) K_gamma(n/d)
      = -gamma_c log(n)
        - sum mu(d) K_gamma(n/d) log(n/d).

This module records that exact finite identity without evaluating logarithms.
It moves the logarithmic weight from the arithmetic divisor coordinate d to
the reciprocal geometry coordinate n/d.  It is an observer/deconvolution
identity, not positive path mass and not an asymptotic or RH estimate.
"""
from __future__ import annotations

from dataclasses import dataclass

from .brc_count_centered_carry import (
    GammaAffine,
    GammaLogForm,
    PrimeValuations,
    _require_positive_int,
    centered_geometry_ratio,
    direct_gamma_centered_prime_error_form,
    factor_positive_integer,
    mobius,
    mobius_divisor_deconvolution_form,
)


def rational_log_valuations(numerator: int, denominator: int) -> PrimeValuations:
    """Prime-valuation vector of the positive rational ``numerator/denominator``."""
    numerator = _require_positive_int("numerator", numerator)
    denominator = _require_positive_int("denominator", denominator)
    values: dict[int, int] = {}
    for prime, exponent in factor_positive_integer(numerator):
        values[prime] = values.get(prime, 0) + exponent
    for prime, exponent in factor_positive_integer(denominator):
        values[prime] = values.get(prime, 0) - exponent
    return tuple(sorted((p, e) for p, e in values.items() if e))


@dataclass(frozen=True)
class MobiusLogGaugeTerm:
    """One signed reciprocal-geometry term ``mu(d) K(n/d) log(n/d)``."""

    divisor: int
    mobius_value: int
    geometry: GammaAffine
    log_ratio_valuations: PrimeValuations

    def prime_log_coefficients(self) -> tuple[tuple[int, GammaAffine], ...]:
        return tuple(
            (prime, self.geometry.scale(self.mobius_value * exponent))
            for prime, exponent in self.log_ratio_valuations
            if exponent
        )


@dataclass(frozen=True)
class MobiusLogGaugeTransfer:
    """Exact endpoint-log gauge transfer at one integer scale."""

    n: int
    geometry_remainder: GammaAffine
    inversion_sum: GammaAffine
    terms: tuple[MobiusLogGaugeTerm, ...]

    @property
    def expected_inversion_sum(self) -> GammaAffine:
        # c_1(n)-gamma_c = -gamma_c for integer n.
        return GammaAffine(0, -1)

    def as_form(self) -> GammaLogForm:
        """Compile ``-K(n)+gamma_c log n+sum mu K log(n/d)`` formally."""
        coefficients: dict[int, GammaAffine] = {}

        # + gamma_c log n
        for prime, exponent in factor_positive_integer(self.n):
            term = GammaAffine(0, exponent)
            coefficients[prime] = coefficients.get(prime, GammaAffine()) + term

        # + sum_d mu(d) K(n/d) log(n/d)
        for item in self.terms:
            for prime, coefficient in item.prime_log_coefficients():
                coefficients[prime] = coefficients.get(prime, GammaAffine()) + coefficient

        log_terms = tuple(
            sorted(
                (prime, coefficient)
                for prime, coefficient in coefficients.items()
                if coefficient != GammaAffine()
            )
        )
        return GammaLogForm(constant=self.geometry_remainder, log_terms=log_terms)

    def verify(self) -> bool:
        if self.n <= 0:
            return False
        if self.inversion_sum != self.expected_inversion_sum:
            return False
        compiled = self.as_form()
        return (
            compiled.equivalent(mobius_divisor_deconvolution_form(self.n))
            and compiled.equivalent(direct_gamma_centered_prime_error_form(self.n))
        )


def mobius_log_gauge_transfer(n: int) -> MobiusLogGaugeTransfer:
    """Return and verify the exact ``log d -> log(n/d)`` gauge transfer."""
    n = _require_positive_int("n", n)
    inversion_sum = GammaAffine()
    terms: list[MobiusLogGaugeTerm] = []
    for d in range(1, n + 1):
        mu = mobius(d)
        if mu == 0:
            continue
        geometry = centered_geometry_ratio(n, d)
        inversion_sum = inversion_sum + geometry.scale(mu)
        terms.append(
            MobiusLogGaugeTerm(
                divisor=d,
                mobius_value=mu,
                geometry=geometry,
                log_ratio_valuations=rational_log_valuations(n, d),
            )
        )

    state = MobiusLogGaugeTransfer(
        n=n,
        geometry_remainder=-centered_geometry_ratio(n),
        inversion_sum=inversion_sum,
        terms=tuple(terms),
    )
    if not state.verify():
        raise AssertionError("Mobius logarithmic gauge transfer verification failed")
    return state
