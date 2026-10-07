"""BRC-gated logarithm runtime for Enterprise Math.

``LN`` and ``LOG`` remain symbolic until a finite-scale readout is requested.
Materialization uses exact rational interval refinement only. No float,
Decimal, Fraction, native division, or direct root primitive is used here.

This module is operational infrastructure. It does not modify the canonical
R023 Boolean-support BRC theorem family and does not claim a new logarithm
collapse theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .exact_arithmetic import (
    BRCDivisionTrace,
    BRCRootTrace,
    DivisionExpr,
    brc_evaluate_division,
    brc_integer_value,
    brc_is_perfect_power,
    decimal_scale,
    division,
    root,
)


def _require_positive_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_positive_argument(name: str, value: DivisionExpr) -> None:
    if value.numerator <= 0:
        raise ValueError(f"{name} must be a positive rational DIV state")


@dataclass(frozen=True)
class LnExpr:
    """Unevaluated natural-logarithm node over a positive rational DIV state."""

    argument: DivisionExpr

    def __post_init__(self) -> None:
        _require_positive_argument("argument", self.argument)


@dataclass(frozen=True)
class LogExpr:
    """Unevaluated logarithm node ``LOG_base(argument)`` over positive rationals."""

    argument: DivisionExpr
    base: DivisionExpr

    def __post_init__(self) -> None:
        _require_positive_argument("argument", self.argument)
        _require_positive_argument("base", self.base)
        if self.base.numerator == self.base.denominator:
            raise ValueError("logarithm base must not equal one")


@dataclass(frozen=True)
class BRCLogPowerRelationTrace:
    """Exact boundary proof for a rational logarithm value.

    If the requested scale boundary reduces to ``m/n``, exactness is certified
    without constructing ``argument**n`` or ``base**m``. Reduced argument and
    base carriers are proved to be the m-th and n-th powers of one common
    positive rational root through the existing BRC root facade.
    """

    boundary_numerator: int
    boundary_denominator: int
    reduced_argument_numerator: int
    reduced_argument_denominator: int
    reduced_base_numerator: int
    reduced_base_denominator: int
    common_root_numerator: int
    common_root_denominator: int
    reduction_traces: tuple[BRCDivisionTrace, ...]
    root_traces: tuple[BRCRootTrace, ...]
    evaluation_kind: str = "BRC_LOG_EXACT_POWER_RELATION"


@dataclass(frozen=True)
class BRCLogarithmTrace:
    """Exact finite-scale evidence for one LN or LOG materialization."""

    operation: str
    scale: int
    sign: int
    magnitude_index: int
    lower_numerator: int
    lower_denominator: int
    upper_numerator: int
    upper_denominator: int
    terms: int
    range_power_argument: int
    range_power_base: int | None
    lower_floor_trace: BRCDivisionTrace
    upper_floor_trace: BRCDivisionTrace
    exact_boundary: bool
    boundary_proof: BRCLogPowerRelationTrace | None
    evaluation_kind: str

    @property
    def scaled_value(self) -> int:
        """Return the signed finite-scale truncation toward zero."""
        return self.sign * self.magnitude_index


@dataclass(frozen=True)
class BRCLogScaledReadout:
    """Finite-scale logarithm readout before decimal punctuation."""

    source: LnExpr | LogExpr
    trace: BRCLogarithmTrace

    @property
    def scale(self) -> int:
        return self.trace.scale

    @property
    def scaled_value(self) -> int:
        return self.trace.scaled_value


@dataclass(frozen=True)
class LogDecimalReadout:
    """Human decimal text derived from a BRC logarithm trace."""

    text: str
    digits: int
    scaled: BRCLogScaledReadout

    @property
    def exact(self) -> bool:
        return self.scaled.trace.exact_boundary


@dataclass(frozen=True)
class _Ratio:
    """Non-negative exact rational bound kept as literal integer carrier."""

    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        if self.numerator < 0 or self.denominator <= 0:
            raise ValueError(
                "internal ratio must be non-negative with positive denominator"
            )


_ZERO = _Ratio(0, 1)


def ln(argument: DivisionExpr) -> LnExpr:
    """Construct ``LN(argument)`` without evaluating it."""
    return LnExpr(argument)


def logarithm(argument: DivisionExpr, base: DivisionExpr) -> LogExpr:
    """Construct ``LOG_base(argument)`` without evaluating it."""
    return LogExpr(argument=argument, base=base)


def log10(argument: DivisionExpr) -> LogExpr:
    """Construct base-ten LOG without evaluating it."""
    return logarithm(argument, division(10, 1))


def _ratio_add(left: _Ratio, right: _Ratio) -> _Ratio:
    return _Ratio(
        left.numerator * right.denominator + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


def _ratio_multiply(left: _Ratio, right: _Ratio) -> _Ratio:
    return _Ratio(
        left.numerator * right.numerator,
        left.denominator * right.denominator,
    )


def _ratio_scale(value: _Ratio, factor: int) -> _Ratio:
    if factor < 0:
        raise ValueError("ratio scale factor must be non-negative")
    return _Ratio(value.numerator * factor, value.denominator)


def _ratio_divide_positive(numerator: _Ratio, denominator: _Ratio) -> _Ratio:
    if denominator.numerator <= 0:
        raise ValueError("ratio divisor must be strictly positive")
    return _Ratio(
        numerator.numerator * denominator.denominator,
        numerator.denominator * denominator.numerator,
    )


def _atanh_log_bounds(
    z_numerator: int,
    z_denominator: int,
    terms: int,
) -> tuple[_Ratio, _Ratio]:
    """Bound ``log((1+z)/(1-z))`` for ``0 <= z < 1``.

    The lower bound is the first ``terms`` positive atanh-series terms. The
    upper bound adds the exact-rational remainder majorant

    ``2*z**(2*terms+1) / ((2*terms+1)*(1-z**2))``.
    """
    _require_positive_integer("terms", terms)
    if z_numerator < 0 or z_numerator >= z_denominator:
        raise ValueError("atanh logarithm coordinate must satisfy 0 <= z < 1")
    if z_numerator == 0:
        return _ZERO, _ZERO

    z_squared = _Ratio(
        z_numerator * z_numerator,
        z_denominator * z_denominator,
    )
    polynomial = _Ratio(1, 2 * terms - 1)
    index = terms - 2
    while index >= 0:
        polynomial = _ratio_add(
            _Ratio(1, 2 * index + 1),
            _ratio_multiply(z_squared, polynomial),
        )
        index -= 1

    lower = _ratio_multiply(
        _Ratio(2 * z_numerator, z_denominator),
        polynomial,
    )

    exponent = 2 * terms + 1
    z_power = _Ratio(
        pow(z_numerator, exponent),
        pow(z_denominator, exponent),
    )
    one_minus_z_squared = _Ratio(
        z_denominator * z_denominator - z_numerator * z_numerator,
        z_denominator * z_denominator,
    )
    remainder_upper = _Ratio(
        2 * z_power.numerator * one_minus_z_squared.denominator,
        z_power.denominator
        * (2 * terms + 1)
        * one_minus_z_squared.numerator,
    )
    return lower, _ratio_add(lower, remainder_upper)


def _magnitude_orientation(value: DivisionExpr) -> tuple[int, int, int]:
    """Return sign(log(value)) and a ratio >= 1 carrying its magnitude."""
    if value.numerator == value.denominator:
        return 0, 1, 1
    if value.numerator > value.denominator:
        return 1, value.numerator, value.denominator
    return -1, value.denominator, value.numerator


def _ln_magnitude_bounds(
    value: DivisionExpr,
    terms: int,
) -> tuple[int, int, _Ratio, _Ratio]:
    """Return sign, binary range coordinate, and bounds for ``abs(ln value)``."""
    sign, numerator, denominator = _magnitude_orientation(value)
    if sign == 0:
        return 0, 0, _ZERO, _ZERO

    power = max(0, numerator.bit_length() - denominator.bit_length())
    while numerator < denominator * (1 << power):
        power -= 1
    while numerator >= denominator * (1 << (power + 1)):
        power += 1

    reduced_denominator = denominator * (1 << power)
    z_numerator = numerator - reduced_denominator
    z_denominator = numerator + reduced_denominator

    ln_two_lower, ln_two_upper = _atanh_log_bounds(1, 3, terms)
    local_lower, local_upper = _atanh_log_bounds(
        z_numerator,
        z_denominator,
        terms,
    )
    lower = _ratio_add(_ratio_scale(ln_two_lower, power), local_lower)
    upper = _ratio_add(_ratio_scale(ln_two_upper, power), local_upper)
    return sign, power, lower, upper


def _scaled_floor_trace(value: _Ratio, scale: int) -> BRCDivisionTrace:
    return brc_evaluate_division(
        division(value.numerator * scale, value.denominator)
    )


def _reduce_ratio_with_brc(
    numerator: int,
    denominator: int,
) -> tuple[int, int, tuple[BRCDivisionTrace, ...]]:
    common = gcd(numerator, denominator)
    if common == 1:
        return numerator, denominator, ()
    reduced_numerator, numerator_trace = brc_integer_value(
        division(numerator, common)
    )
    reduced_denominator, denominator_trace = brc_integer_value(
        division(denominator, common)
    )
    return (
        reduced_numerator,
        reduced_denominator,
        (numerator_trace, denominator_trace),
    )


def _perfect_power_root_with_brc(
    value: int,
    degree: int,
) -> tuple[int | None, tuple[BRCRootTrace, ...]]:
    if degree == 1:
        return value, ()
    if value == 1:
        return 1, ()
    if degree >= value.bit_length():
        return None, ()
    exact, trace = brc_is_perfect_power(root(value, degree))
    if not exact:
        return None, ()
    return trace.root_index, (trace,)


def _exact_log_boundary_relation(
    argument: DivisionExpr,
    base: DivisionExpr,
    boundary_index: int,
    scale: int,
) -> BRCLogPowerRelationTrace | None:
    """Certify ``abs(log_base(argument)) == boundary_index/scale`` when true."""
    if boundary_index <= 0:
        return None

    common = gcd(boundary_index, scale)
    boundary_numerator, boundary_num_trace = brc_integer_value(
        division(boundary_index, common)
    )
    boundary_denominator, boundary_den_trace = brc_integer_value(
        division(scale, common)
    )

    _, argument_numerator, argument_denominator = _magnitude_orientation(argument)
    _, base_numerator, base_denominator = _magnitude_orientation(base)

    (
        argument_numerator,
        argument_denominator,
        argument_reduction_traces,
    ) = _reduce_ratio_with_brc(argument_numerator, argument_denominator)
    (
        base_numerator,
        base_denominator,
        base_reduction_traces,
    ) = _reduce_ratio_with_brc(base_numerator, base_denominator)

    argument_root_numerator, argument_num_root_traces = _perfect_power_root_with_brc(
        argument_numerator,
        boundary_numerator,
    )
    if argument_root_numerator is None:
        return None
    argument_root_denominator, argument_den_root_traces = _perfect_power_root_with_brc(
        argument_denominator,
        boundary_numerator,
    )
    if argument_root_denominator is None:
        return None
    base_root_numerator, base_num_root_traces = _perfect_power_root_with_brc(
        base_numerator,
        boundary_denominator,
    )
    if base_root_numerator is None:
        return None
    base_root_denominator, base_den_root_traces = _perfect_power_root_with_brc(
        base_denominator,
        boundary_denominator,
    )
    if base_root_denominator is None:
        return None

    if (
        argument_root_numerator * base_root_denominator
        != argument_root_denominator * base_root_numerator
    ):
        return None

    return BRCLogPowerRelationTrace(
        boundary_numerator=boundary_numerator,
        boundary_denominator=boundary_denominator,
        reduced_argument_numerator=argument_numerator,
        reduced_argument_denominator=argument_denominator,
        reduced_base_numerator=base_numerator,
        reduced_base_denominator=base_denominator,
        common_root_numerator=argument_root_numerator,
        common_root_denominator=argument_root_denominator,
        reduction_traces=(
            boundary_num_trace,
            boundary_den_trace,
            *argument_reduction_traces,
            *base_reduction_traces,
        ),
        root_traces=(
            *argument_num_root_traces,
            *argument_den_root_traces,
            *base_num_root_traces,
            *base_den_root_traces,
        ),
    )


def _zero_trace(
    operation: str,
    source_scale: int,
    range_power_base: int | None,
) -> BRCLogarithmTrace:
    zero_floor = _scaled_floor_trace(_ZERO, source_scale)
    return BRCLogarithmTrace(
        operation=operation,
        scale=source_scale,
        sign=0,
        magnitude_index=0,
        lower_numerator=0,
        lower_denominator=1,
        upper_numerator=0,
        upper_denominator=1,
        terms=0,
        range_power_argument=0,
        range_power_base=range_power_base,
        lower_floor_trace=zero_floor,
        upper_floor_trace=zero_floor,
        exact_boundary=True,
        boundary_proof=None,
        evaluation_kind=f"BRC_{operation}_INTERVAL_EVALUATION",
    )


def brc_evaluate_ln(expr: LnExpr, scale: int = 1) -> BRCLogarithmTrace:
    """Materialize LN only as a BRC-certified finite-scale interval collapse."""
    _require_positive_integer("scale", scale)
    sign, _, _ = _magnitude_orientation(expr.argument)
    if sign == 0:
        return _zero_trace("LN", scale, None)

    terms = 4
    while True:
        sign, range_power, lower, upper = _ln_magnitude_bounds(
            expr.argument,
            terms,
        )
        lower_floor = _scaled_floor_trace(lower, scale)
        upper_floor = _scaled_floor_trace(upper, scale)
        if lower_floor.quotient == upper_floor.quotient:
            return BRCLogarithmTrace(
                operation="LN",
                scale=scale,
                sign=sign,
                magnitude_index=lower_floor.quotient,
                lower_numerator=lower.numerator,
                lower_denominator=lower.denominator,
                upper_numerator=upper.numerator,
                upper_denominator=upper.denominator,
                terms=terms,
                range_power_argument=range_power,
                range_power_base=None,
                lower_floor_trace=lower_floor,
                upper_floor_trace=upper_floor,
                exact_boundary=False,
                boundary_proof=None,
                evaluation_kind="BRC_LN_INTERVAL_EVALUATION",
            )
        terms *= 2


def brc_evaluate_log(expr: LogExpr, scale: int = 1) -> BRCLogarithmTrace:
    """Materialize LOG through two LN interval carriers plus BRC boundary checks."""
    _require_positive_integer("scale", scale)
    argument_sign, _, _ = _magnitude_orientation(expr.argument)
    base_sign, _, _ = _magnitude_orientation(expr.base)
    if argument_sign == 0:
        _, base_power, _, _ = _ln_magnitude_bounds(expr.base, 4)
        return _zero_trace("LOG", scale, base_power)

    sign = argument_sign * base_sign
    terms = 4
    while True:
        _, argument_power, argument_lower, argument_upper = _ln_magnitude_bounds(
            expr.argument,
            terms,
        )
        _, base_power, base_lower, base_upper = _ln_magnitude_bounds(
            expr.base,
            terms,
        )
        lower = _ratio_divide_positive(argument_lower, base_upper)
        upper = _ratio_divide_positive(argument_upper, base_lower)
        lower_floor = _scaled_floor_trace(lower, scale)
        upper_floor = _scaled_floor_trace(upper, scale)

        if lower_floor.quotient == upper_floor.quotient:
            return BRCLogarithmTrace(
                operation="LOG",
                scale=scale,
                sign=sign,
                magnitude_index=lower_floor.quotient,
                lower_numerator=lower.numerator,
                lower_denominator=lower.denominator,
                upper_numerator=upper.numerator,
                upper_denominator=upper.denominator,
                terms=terms,
                range_power_argument=argument_power,
                range_power_base=base_power,
                lower_floor_trace=lower_floor,
                upper_floor_trace=upper_floor,
                exact_boundary=False,
                boundary_proof=None,
                evaluation_kind="BRC_LOG_INTERVAL_EVALUATION",
            )

        if upper_floor.quotient == lower_floor.quotient + 1:
            boundary_index = upper_floor.quotient
            boundary_proof = _exact_log_boundary_relation(
                expr.argument,
                expr.base,
                boundary_index,
                scale,
            )
            if boundary_proof is not None:
                return BRCLogarithmTrace(
                    operation="LOG",
                    scale=scale,
                    sign=sign,
                    magnitude_index=boundary_index,
                    lower_numerator=lower.numerator,
                    lower_denominator=lower.denominator,
                    upper_numerator=upper.numerator,
                    upper_denominator=upper.denominator,
                    terms=terms,
                    range_power_argument=argument_power,
                    range_power_base=base_power,
                    lower_floor_trace=lower_floor,
                    upper_floor_trace=upper_floor,
                    exact_boundary=True,
                    boundary_proof=boundary_proof,
                    evaluation_kind="BRC_LOG_INTERVAL_EVALUATION",
                )
        terms *= 2


def _decimal_text_from_magnitude(
    magnitude: int,
    sign: int,
    digits: int,
) -> str:
    raw = str(magnitude)
    if digits == 0:
        text = raw
    else:
        padded = raw.zfill(digits + 1)
        text = f"{padded[:-digits]}.{padded[-digits:]}"
    if sign < 0:
        return f"-{text}"
    return text


def brc_ln_decimal_readout(expr: LnExpr, digits: int) -> LogDecimalReadout:
    """Produce decimal LN text only after exact BRC interval collapse."""
    scale = decimal_scale(digits)
    trace = brc_evaluate_ln(expr, scale)
    scaled = BRCLogScaledReadout(source=expr, trace=trace)
    return LogDecimalReadout(
        text=_decimal_text_from_magnitude(
            trace.magnitude_index,
            trace.sign,
            digits,
        ),
        digits=digits,
        scaled=scaled,
    )


def brc_log_decimal_readout(expr: LogExpr, digits: int) -> LogDecimalReadout:
    """Produce decimal LOG text only after exact BRC interval collapse."""
    scale = decimal_scale(digits)
    trace = brc_evaluate_log(expr, scale)
    scaled = BRCLogScaledReadout(source=expr, trace=trace)
    return LogDecimalReadout(
        text=_decimal_text_from_magnitude(
            trace.magnitude_index,
            trace.sign,
            digits,
        ),
        digits=digits,
        scaled=scaled,
    )
