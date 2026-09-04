"""Exact affine-parameter schedule-validity tools for Weighted-BRC Newton jets.

Implements WBRC-T59 only.  The module constructs and evaluates rational affine
Taylor/contact/edge constraints for declared rational-root Newton schedules.
It does not choose a preferred root among multiple roots and is not a generic
constructible-set decomposition engine.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Sequence, TypeAlias

from .brc_newton_fiber_quotient import NewtonFiberCoordinate
from .brc_newton_recursion import RationalValuationScale

RationalInput: TypeAlias = int | Fraction


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


@dataclass(frozen=True)
class RationalAffineForm:
    """Affine form c0 + c1*lambda1 + ... + cd*lambdad over Q."""

    coefficients: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if not self.coefficients:
            raise ValueError("affine form must contain a constant coefficient")
        normalized = tuple(_fraction("affine coefficient", value) for value in self.coefficients)
        object.__setattr__(self, "coefficients", normalized)

    @classmethod
    def constant(cls, value: RationalInput, parameter_count: int) -> "RationalAffineForm":
        if isinstance(parameter_count, bool) or not isinstance(parameter_count, int):
            raise TypeError("parameter_count must be an integer")
        if parameter_count < 0:
            raise ValueError("parameter_count must be non-negative")
        return cls((_fraction("constant", value),) + (Fraction(0),) * parameter_count)

    @property
    def parameter_count(self) -> int:
        return len(self.coefficients) - 1

    @property
    def is_identically_zero(self) -> bool:
        return all(value == 0 for value in self.coefficients)

    def add(self, other: "RationalAffineForm") -> "RationalAffineForm":
        if not isinstance(other, RationalAffineForm):
            raise TypeError("other must be RationalAffineForm")
        if other.parameter_count != self.parameter_count:
            raise ValueError("affine forms must have the same parameter count")
        return RationalAffineForm(tuple(a + b for a, b in zip(self.coefficients, other.coefficients)))

    def scale(self, scalar: RationalInput) -> "RationalAffineForm":
        q = _fraction("scalar", scalar)
        return RationalAffineForm(tuple(q * value for value in self.coefficients))

    def evaluate(self, parameters: Sequence[RationalInput]) -> Fraction:
        values = tuple(_fraction("parameter", value) for value in parameters)
        if len(values) != self.parameter_count:
            raise ValueError("parameter count mismatch")
        return self.coefficients[0] + sum(
            (coefficient * value for coefficient, value in zip(self.coefficients[1:], values)),
            Fraction(0),
        )


@dataclass(frozen=True)
class AffinePolynomial:
    """Polynomial in the Newton variable with affine parameter coefficients."""

    coefficients: tuple[RationalAffineForm, ...]

    def __post_init__(self) -> None:
        if not self.coefficients:
            raise ValueError("affine polynomial must contain at least one coefficient")
        if any(not isinstance(value, RationalAffineForm) for value in self.coefficients):
            raise TypeError("polynomial coefficients must be RationalAffineForm")
        parameter_count = self.coefficients[0].parameter_count
        if any(value.parameter_count != parameter_count for value in self.coefficients):
            raise ValueError("polynomial coefficients must share one parameter count")
        values = list(self.coefficients)
        while len(values) > 1 and values[-1].is_identically_zero:
            values.pop()
        object.__setattr__(self, "coefficients", tuple(values))

    @property
    def parameter_count(self) -> int:
        return self.coefficients[0].parameter_count

    @property
    def degree(self) -> int:
        return len(self.coefficients) - 1

    def evaluate(self, parameters: Sequence[RationalInput]) -> tuple[Fraction, ...]:
        values = [coefficient.evaluate(parameters) for coefficient in self.coefficients]
        while len(values) > 1 and values[-1] == 0:
            values.pop()
        return tuple(values)


@dataclass(frozen=True)
class AffineNewtonLayer:
    scale: RationalValuationScale
    polynomial: AffinePolynomial

    def __post_init__(self) -> None:
        if not isinstance(self.scale, RationalValuationScale):
            raise TypeError("scale must be RationalValuationScale")
        if not isinstance(self.polynomial, AffinePolynomial):
            raise TypeError("polynomial must be AffinePolynomial")


@dataclass(frozen=True)
class AffineRootMultiplicityConstraints:
    """Exact affine conditions for one declared rational root multiplicity."""

    zero_forms: tuple[RationalAffineForm, ...]
    nonzero_form: RationalAffineForm

    def holds(self, parameters: Sequence[RationalInput]) -> bool:
        return all(form.evaluate(parameters) == 0 for form in self.zero_forms) and self.nonzero_form.evaluate(parameters) != 0


def _zero_form(parameter_count: int) -> RationalAffineForm:
    return RationalAffineForm.constant(0, parameter_count)


def affine_taylor_form(
    polynomial: AffinePolynomial,
    root: RationalInput,
    order: int,
) -> RationalAffineForm:
    if not isinstance(polynomial, AffinePolynomial):
        raise TypeError("polynomial must be AffinePolynomial")
    if isinstance(order, bool) or not isinstance(order, int):
        raise TypeError("order must be an integer")
    if order < 0:
        raise ValueError("order must be non-negative")
    x0 = _fraction("root", root)
    output = _zero_form(polynomial.parameter_count)
    for degree in range(order, len(polynomial.coefficients)):
        factor = Fraction(comb(degree, order)) * x0 ** (degree - order)
        output = output.add(polynomial.coefficients[degree].scale(factor))
    return output


def affine_contact_order(
    polynomial: AffinePolynomial,
    root: RationalInput,
    multiplicity: int,
    parameters: Sequence[RationalInput],
) -> int | None:
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int):
        raise TypeError("multiplicity must be an integer")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    for order in range(multiplicity):
        if affine_taylor_form(polynomial, root, order).evaluate(parameters) != 0:
            return order
    return None


def _validate_layers(layers: Sequence[AffineNewtonLayer]) -> tuple[AffineNewtonLayer, ...]:
    normalized = tuple(layers)
    if not normalized:
        raise ValueError("layers must be nonempty")
    if any(not isinstance(layer, AffineNewtonLayer) for layer in normalized):
        raise TypeError("layers must contain AffineNewtonLayer")
    parameter_count = normalized[0].polynomial.parameter_count
    if any(layer.polynomial.parameter_count != parameter_count for layer in normalized):
        raise ValueError("all layers must share one parameter count")
    return normalized


def affine_selected_newton_scale(
    layers: Sequence[AffineNewtonLayer],
    root: RationalInput,
    multiplicity: int,
    parameters: Sequence[RationalInput],
) -> RationalValuationScale:
    normalized = _validate_layers(layers)
    one = RationalValuationScale.one()
    candidates: list[RationalValuationScale] = []
    for layer in normalized:
        if layer.scale == one:
            continue
        order = affine_contact_order(layer.polynomial, root, multiplicity, parameters)
        if order is not None:
            candidates.append(layer.scale.root(multiplicity - order))
    if not candidates:
        raise ValueError("no strict Newton candidate on this parameter point")
    best = candidates[0]
    for candidate in candidates[1:]:
        if candidate.compare(best) > 0:
            best = candidate
    return best


def affine_edge_polynomial(
    layers: Sequence[AffineNewtonLayer],
    root: RationalInput,
    multiplicity: int,
    theta: RationalValuationScale,
) -> AffinePolynomial:
    normalized = _validate_layers(layers)
    if not isinstance(theta, RationalValuationScale):
        raise TypeError("theta must be RationalValuationScale")
    parameter_count = normalized[0].polynomial.parameter_count
    coefficients: list[RationalAffineForm] = []
    one = RationalValuationScale.one()
    for layer in normalized:
        for order in range(len(layer.polynomial.coefficients)):
            coefficient = affine_taylor_form(layer.polynomial, root, order)
            if coefficient.is_identically_zero:
                continue
            residual = layer.scale.multiply(theta.power(order - multiplicity))
            if residual == one:
                while len(coefficients) <= order:
                    coefficients.append(_zero_form(parameter_count))
                coefficients[order] = coefficients[order].add(coefficient)
    if not coefficients:
        coefficients = [_zero_form(parameter_count)]
    return AffinePolynomial(tuple(coefficients))


def affine_root_multiplicity_constraints(
    edge: AffinePolynomial,
    root: RationalInput,
    multiplicity: int,
) -> AffineRootMultiplicityConstraints:
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int):
        raise TypeError("multiplicity must be an integer")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    zero_forms = tuple(affine_taylor_form(edge, root, order) for order in range(multiplicity))
    nonzero = affine_taylor_form(edge, root, multiplicity)
    return AffineRootMultiplicityConstraints(zero_forms, nonzero)


def affine_first_newton_residual(
    layers: Sequence[AffineNewtonLayer],
    root: RationalInput,
    multiplicity: int,
    theta: RationalValuationScale,
) -> tuple[tuple[NewtonFiberCoordinate, RationalAffineForm], ...]:
    normalized = _validate_layers(layers)
    accumulated: dict[NewtonFiberCoordinate, RationalAffineForm] = {}
    parameter_count = normalized[0].polynomial.parameter_count
    for layer in normalized:
        for order in range(len(layer.polynomial.coefficients)):
            coefficient = affine_taylor_form(layer.polynomial, root, order)
            if coefficient.is_identically_zero:
                continue
            coordinate = NewtonFiberCoordinate(
                layer.scale.multiply(theta.power(order - multiplicity)),
                order,
            )
            accumulated[coordinate] = accumulated.get(coordinate, _zero_form(parameter_count)).add(coefficient)
    return tuple(
        (coordinate, accumulated[coordinate])
        for coordinate in sorted(accumulated, key=lambda c: (c.residual_scale.valuations, c.taylor_degree))
        if not accumulated[coordinate].is_identically_zero
    )


def affine_scheduled_newton_substitution(
    state: Sequence[tuple[NewtonFiberCoordinate, RationalAffineForm]],
    root: RationalInput,
    multiplicity: int,
    theta: RationalValuationScale,
) -> tuple[tuple[NewtonFiberCoordinate, RationalAffineForm], ...]:
    normalized = tuple(state)
    if not normalized:
        return ()
    if any(not isinstance(coordinate, NewtonFiberCoordinate) or not isinstance(value, RationalAffineForm) for coordinate, value in normalized):
        raise TypeError("state must contain NewtonFiberCoordinate/RationalAffineForm pairs")
    parameter_count = normalized[0][1].parameter_count
    if any(value.parameter_count != parameter_count for _, value in normalized):
        raise ValueError("state affine forms must share one parameter count")
    x0 = _fraction("root", root)
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int):
        raise TypeError("multiplicity must be an integer")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    if not isinstance(theta, RationalValuationScale):
        raise TypeError("theta must be RationalValuationScale")

    accumulated: dict[NewtonFiberCoordinate, RationalAffineForm] = {}
    for coordinate, coefficient in normalized:
        degree = coordinate.taylor_degree
        for new_degree in range(degree + 1):
            factor = Fraction(comb(degree, new_degree)) * x0 ** (degree - new_degree)
            if factor == 0:
                continue
            new_coordinate = NewtonFiberCoordinate(
                coordinate.residual_scale.multiply(theta.power(new_degree - multiplicity)),
                new_degree,
            )
            accumulated[new_coordinate] = accumulated.get(new_coordinate, _zero_form(parameter_count)).add(
                coefficient.scale(factor)
            )
    return tuple(
        (coordinate, accumulated[coordinate])
        for coordinate in sorted(accumulated, key=lambda c: (c.residual_scale.valuations, c.taylor_degree))
        if not accumulated[coordinate].is_identically_zero
    )


def evaluate_affine_layers(
    layers: Sequence[AffineNewtonLayer],
    parameters: Sequence[RationalInput],
) -> tuple[tuple[RationalValuationScale, tuple[Fraction, ...]], ...]:
    normalized = _validate_layers(layers)
    return tuple((layer.scale, layer.polynomial.evaluate(parameters)) for layer in normalized)


def evaluate_affine_state(
    state: Sequence[tuple[NewtonFiberCoordinate, RationalAffineForm]],
    parameters: Sequence[RationalInput],
) -> tuple[tuple[NewtonFiberCoordinate, Fraction], ...]:
    output = []
    for coordinate, coefficient in state:
        if not isinstance(coordinate, NewtonFiberCoordinate) or not isinstance(coefficient, RationalAffineForm):
            raise TypeError("state must contain NewtonFiberCoordinate/RationalAffineForm pairs")
        value = coefficient.evaluate(parameters)
        if value:
            output.append((coordinate, value))
    return tuple(output)


__all__ = [
    "RationalAffineForm",
    "AffinePolynomial",
    "AffineNewtonLayer",
    "AffineRootMultiplicityConstraints",
    "affine_taylor_form",
    "affine_contact_order",
    "affine_selected_newton_scale",
    "affine_edge_polynomial",
    "affine_root_multiplicity_constraints",
    "affine_first_newton_residual",
    "affine_scheduled_newton_substitution",
    "evaluate_affine_layers",
    "evaluate_affine_state",
]
