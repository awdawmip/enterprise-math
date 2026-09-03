"""Exact Newton-recursion carriers for Weighted-BRC critical characteristic jets.

This module implements WBRC-T52/T53 only.  It deliberately does not provide a
complete Puiseux solver or a generic algebraic-number field.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, lcm
from typing import Iterable, Sequence

from .brc_critical_degeneracy import (
    CriticalRootSelector,
    _p_gcd,
    _p_trim,
    _root_count,
    _sturm_sequence,
    smallest_positive_root_selector,
)
from .brc_rational_holonomy import rational_from_prime_valuations, rational_prime_valuations

RationalInput = int | Fraction
Poly = tuple[Fraction, ...]


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    out = _fraction(name, value)
    if out <= 0:
        raise ValueError(f"{name} must be positive")
    return out


def _trim(poly: Sequence[RationalInput]) -> Poly:
    values = tuple(_fraction("coefficient", value) for value in poly)
    if not values:
        return (Fraction(0, 1),)
    work = list(values)
    while len(work) > 1 and work[-1] == 0:
        work.pop()
    return tuple(work)


def _poly_add(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return _trim(
        tuple(
            (left[i] if i < len(left) else Fraction(0, 1))
            + (right[i] if i < len(right) else Fraction(0, 1))
            for i in range(n)
        )
    )


def _poly_scale(poly: Poly, scalar: Fraction) -> Poly:
    return _trim(tuple(scalar * value for value in poly))


def _poly_mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0, 1) for _ in range(len(left) + len(right) - 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return _trim(tuple(out))


def _poly_eval(poly: Poly, x: Fraction) -> Fraction:
    out = Fraction(0, 1)
    for coefficient in reversed(poly):
        out = out * x + coefficient
    return out


def _poly_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Fraction(0, 1),)
    return _trim(tuple(Fraction(i, 1) * poly[i] for i in range(1, len(poly))))


def _factorial(value: int) -> int:
    out = 1
    for item in range(2, value + 1):
        out *= item
    return out


def _poly_derivative_n(poly: Poly, order: int) -> Poly:
    out = poly
    for _ in range(order):
        out = _poly_derivative(out)
    return out


def _taylor_coefficient_polynomial(poly: Poly, order: int) -> Poly:
    return _poly_scale(_poly_derivative_n(poly, order), Fraction(1, _factorial(order)))


@dataclass(frozen=True)
class RationalValuationScale:
    """Exact positive multiplicative scale with rational prime valuations."""

    valuations: tuple[tuple[int, Fraction], ...] = ()

    def __post_init__(self) -> None:
        normalized: dict[int, Fraction] = {}
        for prime, exponent in self.valuations:
            if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
                raise TypeError("scale primes must be integers >=2")
            exp = _fraction("valuation exponent", exponent)
            if exp:
                normalized[prime] = normalized.get(prime, Fraction(0, 1)) + exp
        object.__setattr__(
            self,
            "valuations",
            tuple(sorted((prime, exponent) for prime, exponent in normalized.items() if exponent)),
        )

    @classmethod
    def one(cls) -> "RationalValuationScale":
        return cls(())

    @classmethod
    def from_rational(cls, value: RationalInput) -> "RationalValuationScale":
        q = _positive_fraction("scale", value)
        return cls(tuple((prime, Fraction(exponent, 1)) for prime, exponent in rational_prime_valuations(q)))

    def multiply(self, other: "RationalValuationScale") -> "RationalValuationScale":
        return RationalValuationScale(self.valuations + other.valuations)

    def power(self, exponent: RationalInput) -> "RationalValuationScale":
        exp = _fraction("power", exponent)
        return RationalValuationScale(tuple((prime, value * exp) for prime, value in self.valuations))

    def root(self, degree: int) -> "RationalValuationScale":
        if isinstance(degree, bool) or not isinstance(degree, int) or degree <= 0:
            raise ValueError("root degree must be a positive integer")
        return self.power(Fraction(1, degree))

    def compare(self, other: "RationalValuationScale") -> int:
        quotient = self.multiply(other.power(-1))
        common = 1
        for _, exponent in quotient.valuations:
            common = lcm(common, exponent.denominator)
        coords: list[tuple[int, int]] = []
        for prime, exponent in quotient.valuations:
            integral = exponent * common
            if integral.denominator != 1:
                raise AssertionError("valuation denominator was not cleared")
            coords.append((prime, integral.numerator))
        value = rational_from_prime_valuations(tuple(coords))
        return (value > 1) - (value < 1)

    def as_rational_power(self, power: int) -> Fraction:
        if isinstance(power, bool) or not isinstance(power, int) or power <= 0:
            raise ValueError("power must be a positive integer")
        coords: list[tuple[int, int]] = []
        for prime, exponent in self.valuations:
            integral = exponent * power
            if integral.denominator != 1:
                raise ValueError("power does not clear all valuation denominators")
            coords.append((prime, integral.numerator))
        return rational_from_prime_valuations(tuple(coords))


@dataclass(frozen=True)
class SelectedRootEvaluationAlgebra:
    """Exact evaluation algebra tied to one selected real root."""

    selector_polynomial: tuple[int, ...]
    selector: CriticalRootSelector

    def __post_init__(self) -> None:
        if not self.selector_polynomial or self.selector_polynomial[0] != 1:
            raise ValueError("selector polynomial must be ascending integer coefficients with constant one")
        if tuple(self.selector.polynomial) != tuple(self.selector_polynomial):
            raise ValueError("selector does not belong to selector_polynomial")
        if not self.selector.verify_interval():
            raise ValueError("invalid selected-root interval")

    @classmethod
    def from_polynomial(
        cls,
        polynomial: Sequence[int],
        *,
        max_width: RationalInput = Fraction(1, 4096),
    ) -> "SelectedRootEvaluationAlgebra":
        values = tuple(polynomial)
        selector = smallest_positive_root_selector(values, max_width=max_width)
        return cls(values, selector)

    @property
    def polynomial(self) -> Poly:
        return tuple(Fraction(value, 1) for value in self.selector_polynomial)

    def coefficient(self, polynomial: Sequence[RationalInput]) -> Poly:
        return _trim(polynomial)

    def add(self, left: Poly, right: Poly) -> Poly:
        return _poly_add(_trim(left), _trim(right))

    def multiply(self, left: Poly, right: Poly) -> Poly:
        return _poly_mul(_trim(left), _trim(right))

    def scale(self, coefficient: Poly, scalar: RationalInput) -> Poly:
        return _poly_scale(_trim(coefficient), _fraction("scalar", scalar))

    def zero(self, coefficient: Poly) -> bool:
        poly = _trim(coefficient)
        if poly == (Fraction(0, 1),):
            return True
        p0 = self.polynomial
        gcd = _p_gcd(p0, poly)
        if len(gcd) <= 1:
            return False
        if self.selector.is_rational:
            assert self.selector.exact_root is not None
            return _poly_eval(poly, self.selector.exact_root) == 0
        sequence = _sturm_sequence(gcd)
        return _root_count(sequence, self.selector.lower, self.selector.upper) > 0

    def equal(self, left: Poly, right: Poly) -> bool:
        return self.zero(_poly_add(_trim(left), _poly_scale(_trim(right), Fraction(-1, 1))))

    def sign(self, coefficient: Poly) -> int:
        poly = _trim(coefficient)
        if self.zero(poly):
            return 0
        if self.selector.is_rational:
            assert self.selector.exact_root is not None
            value = _poly_eval(poly, self.selector.exact_root)
            return (value > 0) - (value < 0)
        for power in range(10, 64):
            selector = smallest_positive_root_selector(
                self.selector_polynomial,
                max_width=Fraction(1, 2**power),
            )
            sequence = _sturm_sequence(poly)
            if _root_count(sequence, selector.lower, selector.upper) == 0:
                midpoint = (selector.lower + selector.upper) / 2
                value = _poly_eval(poly, midpoint)
                if value == 0:
                    continue
                return (value > 0) - (value < 0)
        raise AssertionError("selected-root coefficient sign isolation did not converge")


EvalPolynomial = tuple[Poly, ...]
EvalJet = tuple[tuple[RationalValuationScale, EvalPolynomial], ...]
RationalJet = tuple[tuple[RationalValuationScale, Poly], ...]


@dataclass(frozen=True)
class RationalNewtonStep:
    scale: RationalValuationScale
    jet: RationalJet
    edge_polynomial: Poly


@dataclass(frozen=True)
class SelectedRootNewtonStep:
    scale: RationalValuationScale
    jet: EvalJet
    edge_polynomial: EvalPolynomial


def _sort_scale_items(items: Iterable[tuple[RationalValuationScale, object]]) -> tuple:
    values = list(items)
    # Small jets are the intended Foundation use.  Exact pairwise insertion avoids floats.
    out: list[tuple[RationalValuationScale, object]] = []
    for item in values:
        position = 0
        while position < len(out) and item[0].compare(out[position][0]) < 0:
            position += 1
        out.insert(position, item)
    return tuple(out)


def _max_scale(scales: Sequence[RationalValuationScale]) -> RationalValuationScale:
    if not scales:
        raise ValueError("no Newton candidate scales")
    best = scales[0]
    for scale in scales[1:]:
        if scale.compare(best) > 0:
            best = scale
    return best


def _rational_poly_vanish_order(poly: Poly, root: Fraction) -> int:
    current = _trim(poly)
    order = 0
    while _poly_eval(current, root) == 0:
        current = _poly_derivative(current)
        order += 1
        if current == (Fraction(0, 1),):
            return 10**9
    return order


def rational_newton_step(
    jet: Sequence[tuple[RationalValuationScale, Sequence[RationalInput]]],
    selected_root: RationalInput,
    multiplicity: int,
) -> RationalNewtonStep:
    """One exact Newton step when the translated selected root is rational."""
    root = _fraction("selected_root", selected_root)
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 2:
        raise ValueError("multiplicity must be an integer >=2")
    normalized = [(scale, _trim(poly)) for scale, poly in jet]
    one = RationalValuationScale.one()
    base_poly = next((poly for scale, poly in normalized if scale == one), None)
    if base_poly is None or _rational_poly_vanish_order(base_poly, root) != multiplicity:
        raise ValueError("scale-one polynomial does not have requested multiple selected root")
    candidates: list[RationalValuationScale] = []
    for scale, poly in normalized:
        if scale == one:
            continue
        q = _rational_poly_vanish_order(poly, root)
        if q < multiplicity:
            candidates.append(scale.root(multiplicity - q))
    theta = _max_scale(candidates)
    raw: dict[RationalValuationScale, list[Fraction]] = {}
    for scale, poly in normalized:
        for order in range(len(poly)):
            coefficient = _poly_eval(_poly_derivative_n(poly, order), root) / _factorial(order)
            if coefficient == 0:
                continue
            residual = scale.multiply(theta.power(order - multiplicity))
            if residual.compare(one) > 0:
                raise AssertionError("Newton residual scale exceeded one")
            values = raw.setdefault(residual, [])
            while len(values) <= order:
                values.append(Fraction(0, 1))
            values[order] += coefficient
    frozen = tuple(
        (scale, _trim(values))
        for scale, values in _sort_scale_items(raw.items())
        if any(values)
    )
    edge = next(poly for scale, poly in frozen if scale == one)
    return RationalNewtonStep(theta, frozen, edge)


def _evalpoly_derivative(poly: EvalPolynomial, algebra: SelectedRootEvaluationAlgebra) -> EvalPolynomial:
    if len(poly) <= 1:
        return ((Fraction(0, 1),),)
    values = tuple(algebra.scale(poly[i], i) for i in range(1, len(poly)))
    work = list(values)
    while len(work) > 1 and algebra.zero(work[-1]):
        work.pop()
    return tuple(work)


def _evalpoly_at_rational(poly: EvalPolynomial, root: Fraction, algebra: SelectedRootEvaluationAlgebra) -> Poly:
    out: Poly = (Fraction(0, 1),)
    for coefficient in reversed(poly):
        out = algebra.add(algebra.scale(out, root), coefficient)
    return out


def selected_root_polynomial_vanish_order(
    polynomial: EvalPolynomial,
    rational_root: RationalInput,
    algebra: SelectedRootEvaluationAlgebra,
) -> int:
    root = _fraction("rational_root", rational_root)
    current = polynomial
    order = 0
    while algebra.zero(_evalpoly_at_rational(current, root, algebra)):
        current = _evalpoly_derivative(current, algebra)
        order += 1
        if len(current) == 1 and algebra.zero(current[0]):
            return 10**9
    return order


def selected_root_first_newton_step(
    expansion: Sequence[tuple[RationalInput, Sequence[RationalInput]]],
    algebra: SelectedRootEvaluationAlgebra,
    multiplicity: int,
) -> SelectedRootNewtonStep:
    """First Newton step around an exact algebraic selected root."""
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 2:
        raise ValueError("multiplicity must be an integer >=2")
    normalized = [(Fraction(base), _trim(poly)) for base, poly in expansion]
    p0 = algebra.polynomial
    # The caller supplies the multiplicity to keep this API independent of a full factorization.
    if algebra.zero(_poly_derivative_n(p0, multiplicity)):
        raise ValueError("requested multiplicity is too small for selected root")
    if not all(algebra.zero(_poly_derivative_n(p0, order)) for order in range(multiplicity)):
        raise ValueError("requested multiplicity does not match selected root")
    candidates: list[RationalValuationScale] = []
    contacts: dict[Fraction, int] = {}
    for base, poly in normalized:
        if base == 1:
            continue
        q = 0
        while q < multiplicity and algebra.zero(_poly_derivative_n(poly, q)):
            q += 1
        contacts[base] = q
        if q < multiplicity:
            candidates.append(RationalValuationScale.from_rational(base).root(multiplicity - q))
    theta = _max_scale(candidates)
    one = RationalValuationScale.one()
    raw: dict[RationalValuationScale, list[Poly]] = {}
    for base, poly in normalized:
        scale = RationalValuationScale.from_rational(base)
        for order in range(len(poly)):
            coefficient = _taylor_coefficient_polynomial(poly, order)
            # T53 semantic-zero-first law.
            if algebra.zero(coefficient):
                continue
            residual = scale.multiply(theta.power(order - multiplicity))
            if residual.compare(one) > 0:
                raise AssertionError("semantic nonzero Newton residual scale exceeded one")
            values = raw.setdefault(residual, [])
            while len(values) <= order:
                values.append((Fraction(0, 1),))
            values[order] = algebra.add(values[order], coefficient)
    frozen_items: list[tuple[RationalValuationScale, EvalPolynomial]] = []
    for scale, coefficients in raw.items():
        work = list(coefficients)
        while len(work) > 1 and algebra.zero(work[-1]):
            work.pop()
        if not all(algebra.zero(coefficient) for coefficient in work):
            frozen_items.append((scale, tuple(work)))
    frozen = _sort_scale_items(frozen_items)
    edge = next(poly for scale, poly in frozen if scale == one)
    return SelectedRootNewtonStep(theta, frozen, edge)


def selected_root_rational_newton_step(
    jet: EvalJet,
    rational_root: RationalInput,
    multiplicity: int,
    algebra: SelectedRootEvaluationAlgebra,
) -> SelectedRootNewtonStep:
    """Continue a selected-root jet through a rational translated multiple root."""
    root = _fraction("rational_root", rational_root)
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 2:
        raise ValueError("multiplicity must be an integer >=2")
    one = RationalValuationScale.one()
    base_poly = next((poly for scale, poly in jet if scale == one), None)
    if base_poly is None or selected_root_polynomial_vanish_order(base_poly, root, algebra) != multiplicity:
        raise ValueError("scale-one selected-root polynomial does not have requested multiple root")
    candidates: list[RationalValuationScale] = []
    for scale, poly in jet:
        if scale == one:
            continue
        q = selected_root_polynomial_vanish_order(poly, root, algebra)
        if q < multiplicity:
            candidates.append(scale.root(multiplicity - q))
    theta = _max_scale(candidates)
    raw: dict[RationalValuationScale, list[Poly]] = {}
    for scale, poly in jet:
        current = poly
        for order in range(len(poly)):
            coefficient = _evalpoly_at_rational(current, root, algebra)
            coefficient = algebra.scale(coefficient, Fraction(1, _factorial(order)))
            if not algebra.zero(coefficient):
                residual = scale.multiply(theta.power(order - multiplicity))
                if residual.compare(one) > 0:
                    raise AssertionError("selected-root Newton residual scale exceeded one")
                values = raw.setdefault(residual, [])
                while len(values) <= order:
                    values.append((Fraction(0, 1),))
                values[order] = algebra.add(values[order], coefficient)
            current = _evalpoly_derivative(current, algebra)
    frozen_items: list[tuple[RationalValuationScale, EvalPolynomial]] = []
    for scale, coefficients in raw.items():
        work = list(coefficients)
        while len(work) > 1 and algebra.zero(work[-1]):
            work.pop()
        if not all(algebra.zero(coefficient) for coefficient in work):
            frozen_items.append((scale, tuple(work)))
    frozen = _sort_scale_items(frozen_items)
    edge = next(poly for scale, poly in frozen if scale == one)
    return SelectedRootNewtonStep(theta, frozen, edge)


__all__ = [
    "RationalValuationScale",
    "SelectedRootEvaluationAlgebra",
    "RationalNewtonStep",
    "SelectedRootNewtonStep",
    "rational_newton_step",
    "selected_root_first_newton_step",
    "selected_root_rational_newton_step",
    "selected_root_polynomial_vanish_order",
]
