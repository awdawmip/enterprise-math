"""Exact arithmetic runtime facade for Enterprise Math.

Division and roots may remain unevaluated structural states. Whenever a
quotient-derived or root-derived value is materialized, evaluation must pass
through the BRC facade below and return an explicit collapse trace.

This module is an operational tool. It does not assert or prove a new BRC
mathematical theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import collapse, integer_nth_root
from .division import euclidean_state, multiple_collapse


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class DivisionExpr:
    """An exact unevaluated natural-number division node ``numerator / denominator``.

    The numerator and denominator are intentionally not gcd-reduced. Keeping
    the literal carrier preserves structural information such as ``2/4`` versus
    ``1/2`` even when both have the same classical rational value.
    """

    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        _require_natural("numerator", self.numerator)
        _require_positive("denominator", self.denominator)


@dataclass(frozen=True)
class RootExpr:
    """An exact unevaluated natural-number p-th-root node ``ROOT_p(radicand)``."""

    radicand: int
    degree: int = 2

    def __post_init__(self) -> None:
        _require_natural("radicand", self.radicand)
        _require_positive("degree", self.degree)


@dataclass(frozen=True)
class BRCDivisionTrace:
    """Required evidence emitted by one materialized division evaluation."""

    numerator: int
    denominator: int
    quotient: int
    remainder: int
    collapsed_numerator: int
    evaluation_kind: str = "BRC_DIVISION_EVALUATION"

    def reconstruct(self) -> int:
        """Reconstruct the evaluated numerator from quotient and remainder."""
        return self.denominator * self.quotient + self.remainder


@dataclass(frozen=True)
class BRCRootTrace:
    """Required evidence emitted by one materialized root evaluation."""

    radicand: int
    degree: int
    root_index: int
    collapsed_radicand: int
    remainder: int
    next_power: int
    evaluation_kind: str = "BRC_ROOT_EVALUATION"

    def reconstruct(self) -> int:
        """Reconstruct the evaluated radicand from collapsed state and remainder."""
        return self.collapsed_radicand + self.remainder

    @property
    def basin_width(self) -> int:
        return self.next_power - self.collapsed_radicand

    @property
    def exact(self) -> bool:
        return self.remainder == 0


@dataclass(frozen=True)
class BRCScaledReadout:
    """Exact finite-scale division readout before textual formatting."""

    source: DivisionExpr
    scale: int
    trace: BRCDivisionTrace

    @property
    def scaled_value(self) -> int:
        return self.trace.quotient

    @property
    def residual_numerator(self) -> int:
        return self.trace.remainder

    @property
    def residual_denominator(self) -> int:
        return self.source.denominator * self.scale


@dataclass(frozen=True)
class BRCRootScaledReadout:
    """Exact finite-scale root readout before textual formatting."""

    source: RootExpr
    scale: int
    trace: BRCRootTrace

    @property
    def scaled_value(self) -> int:
        return self.trace.root_index

    @property
    def scaled_radicand(self) -> int:
        return self.source.radicand * self.scale**self.source.degree

    @property
    def residual_radicand(self) -> int:
        return self.trace.remainder


@dataclass(frozen=True)
class DecimalReadout:
    """UI/readout representation derived from an integer-scale BRC division."""

    text: str
    digits: int
    scaled: BRCScaledReadout

    @property
    def exact(self) -> bool:
        return self.scaled.residual_numerator == 0


@dataclass(frozen=True)
class RootDecimalReadout:
    """UI/readout representation derived from an integer-scale BRC root collapse."""

    text: str
    digits: int
    scaled: BRCRootScaledReadout

    @property
    def exact(self) -> bool:
        return self.scaled.trace.exact


def division(numerator: int, denominator: int) -> DivisionExpr:
    """Construct a DIV node without calculating it."""
    return DivisionExpr(numerator, denominator)


def root(radicand: int, degree: int = 2) -> RootExpr:
    """Construct a ROOT node without calculating it."""
    return RootExpr(radicand, degree)


def add_divisions(left: DivisionExpr, right: DivisionExpr) -> DivisionExpr:
    """Carry two DIV states through exact addition without evaluating division."""
    return DivisionExpr(
        left.numerator * right.denominator + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


def multiply_divisions(left: DivisionExpr, right: DivisionExpr) -> DivisionExpr:
    """Carry two DIV states through exact multiplication without evaluation."""
    return DivisionExpr(
        left.numerator * right.numerator,
        left.denominator * right.denominator,
    )


def scale_division(expr: DivisionExpr, factor: int) -> DivisionExpr:
    """Multiply a DIV state by an exact natural-number factor without evaluation."""
    _require_natural("factor", factor)
    return DivisionExpr(expr.numerator * factor, expr.denominator)


def compare_divisions(left: DivisionExpr, right: DivisionExpr) -> int:
    """Compare DIV states by cross multiplication without materializing a quotient."""
    lhs = left.numerator * right.denominator
    rhs = right.numerator * left.denominator
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return 1
    return 0


def brc_evaluate_division(expr: DivisionExpr) -> BRCDivisionTrace:
    """Materialize division only through the BRC runtime boundary.

    The underlying P007 primitives compute the reversible Euclidean state and
    same-state-space multiple collapse. The facade packages both as mandatory
    evaluation evidence so callers cannot receive a quotient without the BRC
    trace.
    """
    quotient, remainder = euclidean_state(expr.numerator, expr.denominator)
    collapsed = multiple_collapse(expr.numerator, expr.denominator)
    trace = BRCDivisionTrace(
        numerator=expr.numerator,
        denominator=expr.denominator,
        quotient=quotient,
        remainder=remainder,
        collapsed_numerator=collapsed,
    )
    if trace.reconstruct() != expr.numerator:
        raise AssertionError("BRC division trace failed exact reconstruction")
    if collapsed != expr.denominator * quotient:
        raise AssertionError("BRC collapsed numerator disagrees with quotient")
    if not 0 <= remainder < expr.denominator:
        raise AssertionError("BRC remainder escaped the Euclidean basin")
    return trace


def brc_evaluate_root(expr: RootExpr) -> BRCRootTrace:
    """Materialize a p-th root only through the BRC runtime boundary.

    The existing integer root and perfect-power collapse primitives are reused
    after the BRC trigger. The trace retains the chosen root index, collapsed
    p-th-power state, residual radicand, and the next basin boundary.
    """
    root_index = integer_nth_root(expr.radicand, expr.degree)
    collapsed = collapse(expr.radicand, expr.degree)
    next_power = (root_index + 1) ** expr.degree
    trace = BRCRootTrace(
        radicand=expr.radicand,
        degree=expr.degree,
        root_index=root_index,
        collapsed_radicand=collapsed,
        remainder=expr.radicand - collapsed,
        next_power=next_power,
    )
    if trace.reconstruct() != expr.radicand:
        raise AssertionError("BRC root trace failed exact reconstruction")
    if collapsed != root_index**expr.degree:
        raise AssertionError("BRC root collapse disagrees with root index")
    if not collapsed <= expr.radicand < next_power:
        raise AssertionError("BRC root state escaped its collapse basin")
    if not 0 <= trace.remainder < trace.basin_width:
        raise AssertionError("BRC root remainder escaped the collapse basin")
    return trace


def brc_scaled_evaluate(expr: DivisionExpr, scale: int) -> BRCScaledReadout:
    """Evaluate ``scale * expr`` using arbitrary-precision integer arithmetic.

    Python ``int`` is arbitrary precision. No float, Decimal, or Fraction state
    is introduced. The only quotient materialization occurs inside
    ``brc_evaluate_division``.
    """
    _require_positive("scale", scale)
    scaled_expr = DivisionExpr(expr.numerator * scale, expr.denominator)
    return BRCScaledReadout(
        source=expr,
        scale=scale,
        trace=brc_evaluate_division(scaled_expr),
    )


def brc_scaled_evaluate_root(expr: RootExpr, scale: int) -> BRCRootScaledReadout:
    """Evaluate a finite-scale root using only arbitrary-precision integers.

    For degree p, the scaled radicand is ``n * scale**p``. Its BRC root index is
    exactly ``floor(scale * n**(1/p))`` in classical readout language, but the
    runtime never constructs a floating root.
    """
    _require_positive("scale", scale)
    scaled_expr = RootExpr(
        expr.radicand * scale**expr.degree,
        expr.degree,
    )
    return BRCRootScaledReadout(
        source=expr,
        scale=scale,
        trace=brc_evaluate_root(scaled_expr),
    )


def decimal_scale(digits: int) -> int:
    """Return the arbitrary-precision integer scale ``10**digits``."""
    _require_natural("digits", digits)
    return 10**digits


def _decimal_text_from_scaled_integer(value: int, digits: int) -> str:
    raw = str(value)
    if digits == 0:
        return raw
    padded = raw.zfill(digits + 1)
    return f"{padded[:-digits]}.{padded[-digits:]}"


def brc_decimal_readout(expr: DivisionExpr, digits: int) -> DecimalReadout:
    """Produce a finite decimal readout only after integer-scale BRC evaluation."""
    scale = decimal_scale(digits)
    scaled = brc_scaled_evaluate(expr, scale)
    text = _decimal_text_from_scaled_integer(scaled.scaled_value, digits)
    return DecimalReadout(text=text, digits=digits, scaled=scaled)


def brc_root_decimal_readout(expr: RootExpr, digits: int) -> RootDecimalReadout:
    """Produce a finite root readout only after integer-scale BRC root evaluation."""
    scale = decimal_scale(digits)
    scaled = brc_scaled_evaluate_root(expr, scale)
    text = _decimal_text_from_scaled_integer(scaled.scaled_value, digits)
    return RootDecimalReadout(text=text, digits=digits, scaled=scaled)


def brc_is_integral(expr: DivisionExpr) -> tuple[bool, BRCDivisionTrace]:
    """Decide divisibility through BRC and return the trace used for the decision."""
    trace = brc_evaluate_division(expr)
    return trace.remainder == 0, trace


def brc_integer_value(expr: DivisionExpr) -> tuple[int, BRCDivisionTrace]:
    """Materialize an exact integer value through BRC, rejecting nonintegral DIV."""
    trace = brc_evaluate_division(expr)
    if trace.remainder != 0:
        raise ValueError("division state is not integral at the requested evaluation")
    return trace.quotient, trace


def brc_is_perfect_power(expr: RootExpr) -> tuple[bool, BRCRootTrace]:
    """Decide perfect-power membership through the BRC root trace."""
    trace = brc_evaluate_root(expr)
    return trace.exact, trace


def brc_root_integer_value(expr: RootExpr) -> tuple[int, BRCRootTrace]:
    """Materialize an exact integer root through BRC, rejecting non-perfect powers."""
    trace = brc_evaluate_root(expr)
    if not trace.exact:
        raise ValueError("root state is not integral at the requested evaluation")
    return trace.root_index, trace
