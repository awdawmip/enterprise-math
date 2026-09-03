"""Exact real-root handoff and Newton-scale resonance tools for Weighted-BRC.

Foundation extraction of WBRC-T54/T55.  This module deliberately leaves
WBRC-T41 smallest-positive critical-root semantics unchanged.  Translated
real roots are supplied by exact rational isolating intervals, and Newton
resonance diagnostics preserve source atoms only as an optional diagnostic
surface; the residual jet itself remains the canonical transformed state.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Sequence, TypeAlias

from .brc_critical_degeneracy import _p_gcd, _root_count, _sturm_sequence
from .brc_newton_recursion import (
    RationalValuationScale,
    RationalNewtonStep,
    _add,
    _derivative,
    _derivative_n,
    _eval,
    _factorial,
    _max_scale,
    _mul,
    _scale,
    _sort_items,
    _trim,
    rational_newton_step,
)

RationalInput: TypeAlias = int | Fraction
Poly: TypeAlias = tuple[Fraction, ...]
RealEvalPolynomial: TypeAlias = tuple[Poly, ...]
RealEvalJet: TypeAlias = tuple[tuple[RationalValuationScale, RealEvalPolynomial], ...]
RationalJet: TypeAlias = tuple[tuple[RationalValuationScale, Poly], ...]


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


def _cauchy_bound(poly: Poly) -> Fraction:
    values = _trim(poly)
    if len(values) <= 1 or values[-1] == 0:
        raise ValueError("nonconstant polynomial required")
    leading = abs(values[-1])
    return Fraction(1) + max((abs(value) / leading for value in values[:-1]), default=Fraction(0))


@dataclass(frozen=True)
class RealRootSelector:
    """One exactly isolated real root of a rational polynomial.

    Unlike WBRC-T41's ``CriticalRootSelector``, this carrier has no built-in
    smallest-positive-root meaning.  Its semantics are exactly the supplied
    single-root rational interval (or an exact rational root).
    """

    polynomial: Poly
    lower: Fraction
    upper: Fraction
    exact_root: Fraction | None = None
    selector: str = "ISOLATED_REAL_ROOT"

    def __post_init__(self) -> None:
        poly = _trim(self.polynomial)
        object.__setattr__(self, "polynomial", poly)
        object.__setattr__(self, "lower", _fraction("lower", self.lower))
        object.__setattr__(self, "upper", _fraction("upper", self.upper))
        if self.exact_root is not None:
            object.__setattr__(self, "exact_root", _fraction("exact_root", self.exact_root))
        if not self.verify_interval():
            raise ValueError("invalid isolated-real-root selector")

    @classmethod
    def from_interval(
        cls,
        polynomial: Sequence[RationalInput],
        lower: RationalInput,
        upper: RationalInput,
    ) -> "RealRootSelector":
        return cls(_trim(polynomial), _fraction("lower", lower), _fraction("upper", upper))

    @classmethod
    def from_exact_root(
        cls,
        polynomial: Sequence[RationalInput],
        root: RationalInput,
    ) -> "RealRootSelector":
        value = _fraction("root", root)
        return cls(_trim(polynomial), value, value, value)

    @property
    def is_rational(self) -> bool:
        return self.exact_root is not None

    def verify_interval(self) -> bool:
        if len(self.polynomial) <= 1:
            return False
        if self.exact_root is not None:
            return self.lower == self.upper == self.exact_root and _eval(self.polynomial, self.exact_root) == 0
        if not self.lower < self.upper:
            return False
        if _eval(self.polynomial, self.lower) == 0 or _eval(self.polynomial, self.upper) == 0:
            return False
        return _root_count(_sturm_sequence(self.polynomial), self.lower, self.upper) == 1

    def refine(self) -> "RealRootSelector":
        if self.is_rational:
            return self
        midpoint = (self.lower + self.upper) / 2
        value = _eval(self.polynomial, midpoint)
        if value == 0:
            return RealRootSelector.from_exact_root(self.polynomial, midpoint)
        sequence = _sturm_sequence(self.polynomial)
        if _root_count(sequence, self.lower, midpoint) > 0:
            return RealRootSelector(self.polynomial, self.lower, midpoint)
        return RealRootSelector(self.polynomial, midpoint, self.upper)


@dataclass(frozen=True)
class RealRootEvaluationAlgebra:
    """Exact rational-polynomial evaluations at one selected real root."""

    selector: RealRootSelector

    def coefficient(self, polynomial: Sequence[RationalInput]) -> Poly:
        return _trim(polynomial)

    def add(self, left: Poly, right: Poly) -> Poly:
        return _add(_trim(left), _trim(right))

    def multiply(self, left: Poly, right: Poly) -> Poly:
        return _mul(_trim(left), _trim(right))

    def scale(self, coefficient: Poly, scalar: RationalInput) -> Poly:
        return _scale(_trim(coefficient), _fraction("scalar", scalar))

    def zero(self, coefficient: Poly) -> bool:
        poly = _trim(coefficient)
        if poly == (Fraction(0),):
            return True
        if self.selector.is_rational:
            assert self.selector.exact_root is not None
            return _eval(poly, self.selector.exact_root) == 0
        gcd = _p_gcd(self.selector.polynomial, poly)
        if len(gcd) <= 1:
            return False
        return _root_count(_sturm_sequence(gcd), self.selector.lower, self.selector.upper) > 0

    def equal(self, left: Poly, right: Poly) -> bool:
        return self.zero(_add(_trim(left), _scale(_trim(right), Fraction(-1))))

    def sign(self, coefficient: Poly) -> int:
        poly = _trim(coefficient)
        if self.zero(poly):
            return 0
        selector = self.selector
        if selector.is_rational:
            assert selector.exact_root is not None
            value = _eval(poly, selector.exact_root)
            return (value > 0) - (value < 0)
        for _ in range(256):
            if _root_count(_sturm_sequence(poly), selector.lower, selector.upper) == 0:
                value = _eval(poly, (selector.lower + selector.upper) / 2)
                if value:
                    return (value > 0) - (value < 0)
            selector = selector.refine()
            if selector.is_rational:
                assert selector.exact_root is not None
                value = _eval(poly, selector.exact_root)
                if value:
                    return (value > 0) - (value < 0)
        raise AssertionError("selected-real-root sign isolation did not converge")

    def vanish_order(self, polynomial: Sequence[RationalInput]) -> int:
        current = _trim(polynomial)
        order = 0
        while self.zero(current):
            current = _derivative(current)
            order += 1
            if current == (Fraction(0),):
                return 10**9
        return order


@dataclass(frozen=True)
class RealRootNewtonStep:
    scale: RationalValuationScale
    jet: RealEvalJet
    edge_polynomial: RealEvalPolynomial


def _evalpoly_trim(poly: RealEvalPolynomial, algebra: RealRootEvaluationAlgebra) -> RealEvalPolynomial:
    values = list(poly)
    while len(values) > 1 and algebra.zero(values[-1]):
        values.pop()
    return tuple(values) if values else ((Fraction(0),),)


def _evalpoly_derivative(poly: RealEvalPolynomial, algebra: RealRootEvaluationAlgebra) -> RealEvalPolynomial:
    if len(poly) <= 1:
        return ((Fraction(0),),)
    return _evalpoly_trim(tuple(algebra.scale(poly[i], i) for i in range(1, len(poly))), algebra)


def _evalpoly_at_rational(poly: RealEvalPolynomial, root: Fraction, algebra: RealRootEvaluationAlgebra) -> Poly:
    out: Poly = (Fraction(0),)
    for coefficient in reversed(poly):
        out = algebra.add(algebra.scale(out, root), coefficient)
    return out


def real_root_polynomial_vanish_order(
    polynomial: RealEvalPolynomial,
    rational_root: RationalInput,
    algebra: RealRootEvaluationAlgebra,
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


def _freeze_eval(raw, algebra: RealRootEvaluationAlgebra) -> RealEvalJet:
    items = []
    for scale, coefficients in raw.items():
        poly = _evalpoly_trim(tuple(coefficients), algebra)
        if not all(algebra.zero(coefficient) for coefficient in poly):
            items.append((scale, poly))
    return _sort_items(items)


def real_root_handoff_step(
    jet: Sequence[tuple[RationalValuationScale, Sequence[RationalInput]]],
    algebra: RealRootEvaluationAlgebra,
    multiplicity: int,
) -> RealRootNewtonStep:
    """Translate a rational-coefficient Newton jet at one selected real root."""
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 2:
        raise ValueError("multiplicity must be an integer >=2")
    normalized = [(scale, _trim(poly)) for scale, poly in jet]
    one = RationalValuationScale.one()
    base_poly = next((poly for scale, poly in normalized if scale == one), None)
    if base_poly is None or algebra.vanish_order(base_poly) != multiplicity:
        raise ValueError("scale-one polynomial does not have requested selected-root multiplicity")
    candidates = []
    for scale, poly in normalized:
        if scale == one:
            continue
        q = algebra.vanish_order(poly)
        if q < multiplicity:
            candidates.append(scale.root(multiplicity - q))
    theta = _max_scale(candidates)
    raw: dict[RationalValuationScale, list[Poly]] = {}
    for scale, poly in normalized:
        for order in range(len(poly)):
            coefficient = _scale(_derivative_n(poly, order), Fraction(1, _factorial(order)))
            if algebra.zero(coefficient):
                continue
            residual = scale.multiply(theta.power(order - multiplicity))
            if residual.compare(one) > 0:
                raise AssertionError("Newton residual scale exceeded one")
            values = raw.setdefault(residual, [])
            while len(values) <= order:
                values.append((Fraction(0),))
            values[order] = algebra.add(values[order], coefficient)
    frozen = _freeze_eval(raw, algebra)
    edge = next(poly for scale, poly in frozen if scale == one)
    return RealRootNewtonStep(theta, frozen, edge)


def real_root_rational_newton_step(
    jet: RealEvalJet,
    selected_root: RationalInput,
    multiplicity: int,
    algebra: RealRootEvaluationAlgebra,
) -> RealRootNewtonStep:
    """Continue one single-real-root evaluation jet through a rational root."""
    root = _fraction("selected_root", selected_root)
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 2:
        raise ValueError("multiplicity must be an integer >=2")
    one = RationalValuationScale.one()
    base_poly = next((poly for scale, poly in jet if scale == one), None)
    if base_poly is None or real_root_polynomial_vanish_order(base_poly, root, algebra) != multiplicity:
        raise ValueError("scale-one evaluation polynomial has wrong rational-root multiplicity")
    candidates = []
    for scale, poly in jet:
        if scale == one:
            continue
        q = real_root_polynomial_vanish_order(poly, root, algebra)
        if q < multiplicity:
            candidates.append(scale.root(multiplicity - q))
    theta = _max_scale(candidates)
    raw: dict[RationalValuationScale, list[Poly]] = {}
    for scale, poly in jet:
        current = poly
        for order in range(len(poly)):
            coefficient = _evalpoly_at_rational(current, root, algebra)
            if order:
                coefficient = algebra.scale(coefficient, Fraction(1, _factorial(order)))
            if not algebra.zero(coefficient):
                residual = scale.multiply(theta.power(order - multiplicity))
                if residual.compare(one) > 0:
                    raise AssertionError("Newton residual scale exceeded one")
                values = raw.setdefault(residual, [])
                while len(values) <= order:
                    values.append((Fraction(0),))
                values[order] = algebra.add(values[order], coefficient)
            current = _evalpoly_derivative(current, algebra)
    frozen = _freeze_eval(raw, algebra)
    edge = next(poly for scale, poly in frozen if scale == one)
    return RealRootNewtonStep(theta, frozen, edge)


def evaluate_at_coefficient(
    polynomial: Sequence[Poly],
    candidate: Poly,
    algebra: Any,
) -> Poly:
    """Horner-evaluate an evaluation-polynomial at one supplied algebra element."""
    out: Poly = (Fraction(0),)
    for coefficient in reversed(tuple(polynomial)):
        out = algebra.add(algebra.multiply(out, candidate), coefficient)
    return out


def verify_absorbed_root_zero(
    polynomial: Sequence[Poly],
    candidate: Poly,
    algebra: Any,
) -> bool:
    """Verify only the semantic root equation E(candidate)=0.

    Selected-real-branch identification is an independent certificate and is
    deliberately not inferred by this function.
    """
    return bool(algebra.zero(evaluate_at_coefficient(polynomial, candidate, algebra)))


@dataclass(frozen=True)
class NewtonPushforwardAtom:
    source_index: int
    source_scale: RationalValuationScale
    taylor_order: int
    coefficient: Fraction
    residual_scale: RationalValuationScale


@dataclass(frozen=True)
class NewtonResonanceFiber:
    residual_scale: RationalValuationScale
    polynomial: Poly
    atoms: tuple[NewtonPushforwardAtom, ...]

    @property
    def resonant(self) -> bool:
        return len({(atom.source_index, atom.taylor_order) for atom in self.atoms}) > 1


@dataclass(frozen=True)
class NewtonPushforwardAnalysis:
    step: RationalNewtonStep
    fibers: tuple[NewtonResonanceFiber, ...]

    @property
    def edge_fiber(self) -> NewtonResonanceFiber:
        one = RationalValuationScale.one()
        return next(fiber for fiber in self.fibers if fiber.residual_scale == one)


def newton_atoms_resonate(
    left: NewtonPushforwardAtom,
    right: NewtonPushforwardAtom,
    theta: RationalValuationScale,
) -> bool:
    """Exact valuation form of sigma1/sigma2 = theta^(k2-k1)."""
    quotient = left.source_scale.multiply(right.source_scale.power(-1))
    predicted = theta.power(right.taylor_order - left.taylor_order)
    return quotient.compare(predicted) == 0 and left.residual_scale.compare(right.residual_scale) == 0


def rational_newton_pushforward(
    jet: Sequence[tuple[RationalValuationScale, Sequence[RationalInput]]],
    selected_root: RationalInput,
    multiplicity: int,
) -> NewtonPushforwardAnalysis:
    """Return the production Newton step together with exact source-scale fibers."""
    root = _fraction("selected_root", selected_root)
    normalized = [(scale, _trim(poly)) for scale, poly in jet]
    step = rational_newton_step(normalized, root, multiplicity)
    raw: dict[RationalValuationScale, list[Fraction]] = {}
    atoms_by_scale: dict[RationalValuationScale, list[NewtonPushforwardAtom]] = {}
    for source_index, (scale, poly) in enumerate(normalized):
        for order in range(len(poly)):
            coefficient = _eval(_derivative_n(poly, order), root) / _factorial(order)
            if coefficient == 0:
                continue
            residual = scale.multiply(step.scale.power(order - multiplicity))
            values = raw.setdefault(residual, [])
            while len(values) <= order:
                values.append(Fraction(0))
            values[order] += coefficient
            atoms_by_scale.setdefault(residual, []).append(
                NewtonPushforwardAtom(source_index, scale, order, coefficient, residual)
            )
    fibers = tuple(
        NewtonResonanceFiber(
            scale,
            _trim(raw[scale]),
            tuple(atoms_by_scale[scale]),
        )
        for scale, _ in _sort_items(raw.items())
        if any(raw[scale])
    )
    production = {scale: poly for scale, poly in step.jet}
    reconstructed = {fiber.residual_scale: fiber.polynomial for fiber in fibers}
    if production != reconstructed:
        raise AssertionError("Newton pushforward diagnostic did not reproduce production step")
    return NewtonPushforwardAnalysis(step, fibers)


__all__ = [
    "RealRootSelector",
    "RealRootEvaluationAlgebra",
    "RealRootNewtonStep",
    "real_root_handoff_step",
    "real_root_rational_newton_step",
    "real_root_polynomial_vanish_order",
    "evaluate_at_coefficient",
    "verify_absorbed_root_zero",
    "NewtonPushforwardAtom",
    "NewtonResonanceFiber",
    "NewtonPushforwardAnalysis",
    "newton_atoms_resonate",
    "rational_newton_pushforward",
]
