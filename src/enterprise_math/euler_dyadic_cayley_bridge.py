"""Target-free bridge from the dyadic Euler root tower to Cayley completion.

For the root state U_d = c_d + J s_d, define the Cayley coordinate

    tau_d = s_d / (1 + c_d).

Then U_d = (1 + J tau_d)/(1 - J tau_d), and U_d^(2^d) = -1.  The lower
readout P_d = 2^d s_d and upper readout Q_d = 2^(d+1) tau_d squeeze a common
completion constant without importing pi or trigonometric functions.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext

from .euler_rotation_refinement import (
    antisymmetric_trace,
    rotation_pi_approximant,
    symmetric_trace,
)

ComplexPair = tuple[Decimal, Decimal]


def _precision(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 20:
        raise ValueError("precision must be an integer at least 20")
    return value


def _depth(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("depth must be a positive integer")
    return value


def pair_mul(left: ComplexPair, right: ComplexPair) -> ComplexPair:
    """Multiply a+bJ and c+dJ under J^2=-1."""
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def pair_pow(value: ComplexPair, exponent: int) -> ComplexPair:
    """Exponentiation by squaring in the two-component character algebra."""
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a non-negative integer")
    result = Decimal(1), Decimal(0)
    base = value
    while exponent:
        if exponent & 1:
            result = pair_mul(result, base)
        base = pair_mul(base, base)
        exponent >>= 1
    return result


def cayley_parameter(depth: int, *, precision: int = 80) -> Decimal:
    """Return tau_d=s_d/(1+c_d), the finite half-phase coordinate."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        c = symmetric_trace(depth, precision=precision + 16)
        s = antisymmetric_trace(depth, precision=precision + 16)
        value = s / (Decimal(1) + c)
        context.prec = precision
        return +value


def cayley_character(parameter: Decimal, *, precision: int = 80) -> ComplexPair:
    """Return (1+Jt)/(1-Jt) as its exact algebraic coordinate formula."""
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        denominator = Decimal(1) + parameter * parameter
        value = (
            (Decimal(1) - parameter * parameter) / denominator,
            Decimal(2) * parameter / denominator,
        )
        context.prec = precision
        return +value[0], +value[1]


def root_character(depth: int, *, precision: int = 80) -> ComplexPair:
    """Return U_d=c_d+J s_d from the target-free nested-radical recursion."""
    depth = _depth(depth)
    precision = _precision(precision)
    return (
        symmetric_trace(depth, precision=precision),
        antisymmetric_trace(depth, precision=precision),
    )


def cayley_reconstruction_residual(depth: int, *, precision: int = 80) -> ComplexPair:
    """Numerical residual of C(tau_d)=U_d, evaluated without pi/trigonometry."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        cayley = cayley_character(
            cayley_parameter(depth, precision=precision + 16),
            precision=precision + 16,
        )
        root = root_character(depth, precision=precision + 16)
        value = cayley[0] - root[0], cayley[1] - root[1]
        context.prec = precision
        return +value[0], +value[1]


def finite_half_turn_residual(depth: int, *, precision: int = 80) -> ComplexPair:
    """Residual of C(tau_d)^(2^d)=-1 at finite depth."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 24
        root = cayley_character(
            cayley_parameter(depth, precision=precision + 24),
            precision=precision + 24,
        )
        value = pair_pow(root, 1 << depth)
        residual = value[0] + Decimal(1), value[1]
        context.prec = precision
        return +residual[0], +residual[1]


def lower_half_period(depth: int, *, precision: int = 80) -> Decimal:
    """Increasing chord/antisymmetric readout P_d=2^d s_d."""
    return rotation_pi_approximant(_depth(depth), precision=_precision(precision))


def upper_half_period(depth: int, *, precision: int = 80) -> Decimal:
    """Decreasing Cayley/tangent readout Q_d=2^(d+1) tau_d."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        value = (Decimal(2) ** (depth + 1)) * cayley_parameter(
            depth,
            precision=precision + 16,
        )
        context.prec = precision
        return +value


def upper_from_lower_identity(depth: int, *, precision: int = 80) -> Decimal:
    """Equivalent formula Q_d=2 P_d/(1+c_d)."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        lower = lower_half_period(depth, precision=precision + 16)
        c = symmetric_trace(depth, precision=precision + 16)
        value = Decimal(2) * lower / (Decimal(1) + c)
        context.prec = precision
        return +value


def squeeze_width(depth: int, *, precision: int = 80) -> Decimal:
    """Exact finite interval width Q_d-P_d."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        value = upper_half_period(depth, precision=precision + 16) - lower_half_period(
            depth,
            precision=precision + 16,
        )
        context.prec = precision
        return +value


def squeeze_width_identity(depth: int, *, precision: int = 80) -> Decimal:
    """Equivalent exact identity Q_d-P_d=P_d*tau_d^2."""
    depth = _depth(depth)
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 16
        lower = lower_half_period(depth, precision=precision + 16)
        tau = cayley_parameter(depth, precision=precision + 16)
        value = lower * tau * tau
        context.prec = precision
        return +value


@dataclass(frozen=True)
class DyadicCayleyCertificate:
    depth: int
    cayley_residual: ComplexPair
    half_turn_residual: ComplexPair
    lower: Decimal
    upper: Decimal
    upper_identity: Decimal
    width: Decimal
    width_identity: Decimal

    def valid(self, tolerance: Decimal) -> bool:
        return (
            max(abs(value) for value in self.cayley_residual) < tolerance
            and max(abs(value) for value in self.half_turn_residual) < tolerance
            and self.lower < self.upper
            and abs(self.upper - self.upper_identity) < tolerance
            and abs(self.width - self.width_identity) < tolerance
        )


def dyadic_cayley_certificate(
    depth: int,
    *,
    precision: int = 80,
) -> DyadicCayleyCertificate:
    """Return one target-free finite Euler/Cayley squeeze certificate."""
    depth = _depth(depth)
    precision = _precision(precision)
    return DyadicCayleyCertificate(
        depth=depth,
        cayley_residual=cayley_reconstruction_residual(depth, precision=precision),
        half_turn_residual=finite_half_turn_residual(depth, precision=precision),
        lower=lower_half_period(depth, precision=precision),
        upper=upper_half_period(depth, precision=precision),
        upper_identity=upper_from_lower_identity(depth, precision=precision),
        width=squeeze_width(depth, precision=precision),
        width_identity=squeeze_width_identity(depth, precision=precision),
    )
