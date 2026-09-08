"""Exact, bounded signed-X6 valuation observer using existing positive BRC.

Auxiliary research implementation, not a registered tool family. Digit carry
matrices for multinomial valuations are classical (Rowland, Theorem 3).
The observer forgets endpoint identities and prime-coprime units explicitly.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import comb

from enterprise_math.brc_histogram import (
    WeightHistogram,
    histogram_recoalesce,
    histogram_serial,
)
from enterprise_math.legendre import is_prime


class ComputationBudgetExceeded(RuntimeError):
    """A declared execution bound was reached, not a mathematical no-result."""


def _integer(name: str, value: int, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


def digits_lsd(n: int, p: int) -> tuple[int, ...]:
    digits = []
    while n:
        n, digit = divmod(n, p)
        digits.append(digit)
    return tuple(digits or [0])


@lru_cache(maxsize=256)
def _digit_coefficients(p: int, active: int, newly_active: int) -> tuple[int, ...]:
    """Coefficients of U_p(x)^active (U_p(x)-1)^newly_active."""
    coefficients = [1]
    for index in range(active + newly_active):
        next_coefficients = [0] * (len(coefficients) + p - 1)
        allowed_digits = range(p) if index < active else range(1, p)
        for degree, count in enumerate(coefficients):
            for digit in allowed_digits:
                next_coefficients[degree + digit] += count
        coefficients = next_coefficients
    return tuple(coefficients)


@dataclass(frozen=True)
class SignedValuationSpectrum:
    radius: int
    prime: int
    digits: tuple[int, ...]
    signed_histogram: WeightHistogram
    signed_by_active: tuple[tuple[int, WeightHistogram], ...]

    def valuation_counts(self) -> dict[int, int]:
        result = {}
        for valuations, count in self.signed_histogram.prime_valuation_terms():
            if not valuations:
                result[0] = count
            else:
                if len(valuations) != 1 or valuations[0][0] != self.prime:
                    raise AssertionError("projected BRC must contain only powers of p")
                result[valuations[0][1]] = count
        return result


def signed_valuation_spectrum(
    radius: int,
    prime: int,
    *,
    max_prime: int = 31,
    max_digits: int = 256,
) -> SignedValuationSpectrum:
    """Count endpoints by vp(N!/prod |z_i|!), using at most 42 carry/active states.

    The output BRC weight is p**vp(C), not the original endpoint weight C.
    Counts enumerate signed endpoints, not ordered unit-step paths. Resource
    bounds are implementation limits and do not restrict the mathematical N0
    domain. No division-free or factoring-complexity claim is made.
    """
    radius = _integer("radius", radius, 0)
    prime = _integer("prime", prime, 2)
    max_prime = _integer("max_prime", max_prime, 2)
    max_digits = _integer("max_digits", max_digits, 1)
    if prime > max_prime:
        raise ComputationBudgetExceeded("prime exceeds declared coefficient budget")
    if not is_prime(prime):
        raise ValueError("prime must be prime; composite radii remain admissible")
    if radius >= prime**max_digits:
        raise ComputationBudgetExceeded("radius exceeds declared digit budget")
    digits = digits_lsd(radius, prime)
    zero = WeightHistogram(())
    states = {(0, 0): WeightHistogram.from_counts({1: 1})}
    for digit in digits:
        next_states = {}
        for (carry, active), history in states.items():
            for newly_active in range(7 - active):
                coefficients = _digit_coefficients(prime, active, newly_active)
                choices = comb(6 - active, newly_active)
                for next_carry in range(6):
                    digit_sum = digit + prime * next_carry - carry
                    if not 0 <= digit_sum < len(coefficients):
                        continue
                    multiplicity = choices * coefficients[digit_sum]
                    if not multiplicity:
                        continue
                    edge = WeightHistogram.from_counts({prime**next_carry: multiplicity})
                    contribution = histogram_serial(history, edge)
                    state = (next_carry, active + newly_active)
                    next_states[state] = histogram_recoalesce(
                        next_states.get(state, zero), contribution
                    )
        states = next_states
    signed = zero
    signed_by_active = []
    for active in range(7):
        history = states.get((0, active), zero)
        if history.is_zero:
            continue
        signs = WeightHistogram.from_counts({1: 2**active})
        contribution = histogram_serial(history, signs)
        signed_by_active.append((active, contribution))
        signed = histogram_recoalesce(signed, contribution)
    return SignedValuationSpectrum(radius, prime, digits, signed, tuple(signed_by_active))
