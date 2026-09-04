"""Exact non-split monic-quadratic selectors for Weighted-BRC Newton edges.

Implements WBRC-T62/T63.  Smallest-real selection uses the exact quantities
D=a^2-4b, L=-a-2r and R=r^2+ar+b.  Smallest-positive selection uses the
quadratic Sturm variation on the open interval (0,r), with an equivalent
radical-free compact chamber.  No competing quadratic root is materialized.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence, TypeAlias

from .brc_newton_schedule_strata import RationalAffineForm

RationalInput: TypeAlias = int | Fraction


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


def quadratic_sturm_variation(values: Sequence[RationalInput]) -> int:
    """Sign variation after deleting zero entries, exactly over Q."""
    signs: list[int] = []
    for raw in values:
        value = _fraction("Sturm value", raw)
        if value:
            signs.append((value > 0) - (value < 0))
    return sum(left != right for left, right in zip(signs, signs[1:]))


@dataclass(frozen=True)
class QuadraticSelectorState:
    """Exact selector data for Q(y)=y^2+a*y+b against declared root r."""

    a: Fraction
    b: Fraction
    declared_root: Fraction

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", _fraction("a", self.a))
        object.__setattr__(self, "b", _fraction("b", self.b))
        object.__setattr__(self, "declared_root", _fraction("declared_root", self.declared_root))

    @property
    def discriminant(self) -> Fraction:
        return self.a * self.a - 4 * self.b

    @property
    def left_margin(self) -> Fraction:
        return -self.a - 2 * self.declared_root

    @property
    def root_value(self) -> Fraction:
        r = self.declared_root
        return r * r + self.a * r + self.b

    @property
    def fixed_multiplicity(self) -> bool:
        return self.root_value != 0

    @property
    def identity_holds(self) -> bool:
        return self.left_margin * self.left_margin - self.discriminant == 4 * self.root_value

    @property
    def smallest_real_selected(self) -> bool:
        if not self.fixed_multiplicity:
            return False
        return self.discriminant < 0 or (self.left_margin > 0 and self.root_value > 0)

    @property
    def positive_left_variation(self) -> int:
        if self.declared_root <= 0:
            raise ValueError("declared_root must be positive for smallest-positive selection")
        return quadratic_sturm_variation((self.b, self.a, self.discriminant))

    @property
    def positive_right_variation(self) -> int:
        if self.declared_root <= 0:
            raise ValueError("declared_root must be positive for smallest-positive selection")
        if not self.fixed_multiplicity:
            raise ValueError("Q(declared_root) must be nonzero for open-interval Sturm count")
        return quadratic_sturm_variation(
            (self.root_value, 2 * self.declared_root + self.a, self.discriminant)
        )

    @property
    def positive_interval_root_count(self) -> int:
        """Number of distinct Q-roots in the open interval (0,r)."""
        if self.declared_root <= 0:
            raise ValueError("declared_root must be positive for smallest-positive selection")
        if not self.fixed_multiplicity:
            raise ValueError("Q(declared_root) must be nonzero for open-interval Sturm count")
        count = self.positive_left_variation - self.positive_right_variation
        if count < 0 or count > 2:
            raise AssertionError("quadratic Sturm interval count left its valid range")
        return count

    @property
    def smallest_positive_selected(self) -> bool:
        if self.declared_root <= 0 or not self.fixed_multiplicity:
            return False
        return self.positive_interval_root_count == 0

    @property
    def smallest_positive_compact_selected(self) -> bool:
        if self.declared_root <= 0 or not self.fixed_multiplicity:
            return False
        r = self.declared_root
        return self.b * self.root_value >= 0 and (
            self.b < 0
            or self.root_value < 0
            or self.discriminant < 0
            or self.a >= 0
            or self.a <= -2 * r
        )

    @property
    def positive_formula_consistent(self) -> bool:
        return self.smallest_positive_selected == self.smallest_positive_compact_selected

    @property
    def chamber_signature(self) -> tuple[int, int, int]:
        """Signs of (D,L,R) as -1/0/+1 for exact chamber diagnostics."""
        values = (self.discriminant, self.left_margin, self.root_value)
        return tuple((value > 0) - (value < 0) for value in values)  # type: ignore[return-value]


@dataclass(frozen=True)
class AffineQuadraticSelectorFamily:
    """Monic quadratic cofactor with rational-affine a(lambda), b(lambda)."""

    a_form: RationalAffineForm
    b_form: RationalAffineForm
    declared_root: Fraction

    def __post_init__(self) -> None:
        if not isinstance(self.a_form, RationalAffineForm) or not isinstance(self.b_form, RationalAffineForm):
            raise TypeError("a_form and b_form must be RationalAffineForm")
        if self.a_form.parameter_count != self.b_form.parameter_count:
            raise ValueError("a_form and b_form must share one parameter count")
        object.__setattr__(self, "declared_root", _fraction("declared_root", self.declared_root))

    @property
    def parameter_count(self) -> int:
        return self.a_form.parameter_count

    def evaluate(self, parameters: Sequence[RationalInput]) -> QuadraticSelectorState:
        return QuadraticSelectorState(
            self.a_form.evaluate(parameters),
            self.b_form.evaluate(parameters),
            self.declared_root,
        )


def quadratic_selector_state(
    a: RationalInput,
    b: RationalInput,
    declared_root: RationalInput,
) -> QuadraticSelectorState:
    return QuadraticSelectorState(_fraction("a", a), _fraction("b", b), _fraction("declared_root", declared_root))


def quadratic_fixed_multiplicity(
    a: RationalInput,
    b: RationalInput,
    declared_root: RationalInput,
) -> bool:
    return quadratic_selector_state(a, b, declared_root).fixed_multiplicity


def quadratic_smallest_real_selected(
    a: RationalInput,
    b: RationalInput,
    declared_root: RationalInput,
) -> bool:
    return quadratic_selector_state(a, b, declared_root).smallest_real_selected


def quadratic_positive_interval_root_count(
    a: RationalInput,
    b: RationalInput,
    declared_root: RationalInput,
) -> int:
    return quadratic_selector_state(a, b, declared_root).positive_interval_root_count


def quadratic_smallest_positive_selected(
    a: RationalInput,
    b: RationalInput,
    declared_root: RationalInput,
) -> bool:
    return quadratic_selector_state(a, b, declared_root).smallest_positive_selected


def quadratic_smallest_positive_compact_selected(
    a: RationalInput,
    b: RationalInput,
    declared_root: RationalInput,
) -> bool:
    return quadratic_selector_state(a, b, declared_root).smallest_positive_compact_selected


def evaluate_affine_quadratic_selector(
    family: AffineQuadraticSelectorFamily,
    parameters: Sequence[RationalInput],
) -> QuadraticSelectorState:
    if not isinstance(family, AffineQuadraticSelectorFamily):
        raise TypeError("family must be AffineQuadraticSelectorFamily")
    return family.evaluate(parameters)


__all__ = [
    "QuadraticSelectorState",
    "AffineQuadraticSelectorFamily",
    "quadratic_sturm_variation",
    "quadratic_selector_state",
    "quadratic_fixed_multiplicity",
    "quadratic_smallest_real_selected",
    "quadratic_positive_interval_root_count",
    "quadratic_smallest_positive_selected",
    "quadratic_smallest_positive_compact_selected",
    "evaluate_affine_quadratic_selector",
]
