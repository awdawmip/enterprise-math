"""Integer + typed residual extensions of the existing BRC arithmetic facade.

Research candidate, not a new BRC family or a migration of every caller.
The source carrier is intentionally not reduced: value equality is explicit.
No approximate scalar is accepted; rational, algebraic and enclosure residuals
are different types. Geometry/branch provenance is owned by the caller.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

from .exact_arithmetic import (
    BRCDivisionTrace, BRCRootTrace, DivisionExpr, RootExpr,
    brc_evaluate_division, brc_evaluate_root, brc_scaled_evaluate,
)


def _integer(name: str, value: int, minimum: int | None = None) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an exact integer, not a conversion")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")


@dataclass(frozen=True)
class SignedDivisionExpr:
    """Signed, unreduced exact source. Structural equality is not value equality."""
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        _integer("numerator", self.numerator)
        _integer("denominator", self.denominator, 1)

    def negative(self) -> SignedDivisionExpr:
        return SignedDivisionExpr(-self.numerator, self.denominator)

    def reciprocal(self) -> SignedDivisionExpr:
        if self.numerator == 0:
            raise ZeroDivisionError("the reciprocal of zero is undefined")
        sign = -1 if self.numerator < 0 else 1
        return SignedDivisionExpr(sign * self.denominator, abs(self.numerator))

    def plus(self, other: SignedDivisionExpr) -> SignedDivisionExpr:
        if not isinstance(other, SignedDivisionExpr):
            raise TypeError("signed exact source required")
        return SignedDivisionExpr(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def times(self, other: SignedDivisionExpr) -> SignedDivisionExpr:
        if not isinstance(other, SignedDivisionExpr):
            raise TypeError("signed exact source required")
        return SignedDivisionExpr(self.numerator * other.numerator,
                                  self.denominator * other.denominator)

    def compare_value(self, other: SignedDivisionExpr) -> int:
        if not isinstance(other, SignedDivisionExpr):
            raise TypeError("signed exact source required")
        difference = (self.numerator * other.denominator
                      - other.numerator * self.denominator)
        return (difference > 0) - (difference < 0)

    def at_scale(self, scale: int) -> IntegerResidual:
        return brc_signed_scaled_evaluate(self, scale)


class CertifiedOrder(Enum):
    LESS = "LESS"
    EQUAL = "EQUAL"
    GREATER = "GREATER"
    UNRESOLVED = "UNRESOLVED"

    def __bool__(self) -> bool:
        raise TypeError("compare the explicit CertifiedOrder member; no truth coercion")


@dataclass(frozen=True)
class RationalEnclosure:
    """Closed exact endpoints. Overlap is not evidence of equality.

    This type checks interval consistency, not the truth of a caller's external
    claim that an unknown quantity belongs to it. BRC root/rational producers
    below supply that claim through their reconstruction certificates.
    """
    lower: SignedDivisionExpr
    upper: SignedDivisionExpr

    def __post_init__(self) -> None:
        if not isinstance(self.lower, SignedDivisionExpr) or not isinstance(self.upper, SignedDivisionExpr):
            raise TypeError("signed exact endpoints required")
        if self.lower.compare_value(self.upper) > 0:
            raise ValueError("reversed interval")

    @property
    def is_point(self) -> bool:
        return self.lower.compare_value(self.upper) == 0

    def compare(self, other: RationalEnclosure) -> CertifiedOrder:
        if not isinstance(other, RationalEnclosure):
            raise TypeError("exact enclosure required")
        if self.upper.compare_value(other.lower) < 0:
            return CertifiedOrder.LESS
        if self.lower.compare_value(other.upper) > 0:
            return CertifiedOrder.GREATER
        if self.is_point and other.is_point and self.lower.compare_value(other.lower) == 0:
            return CertifiedOrder.EQUAL
        return CertifiedOrder.UNRESOLVED

    def contains(self, value: SignedDivisionExpr) -> bool:
        return self.lower.compare_value(value) <= 0 and value.compare_value(self.upper) <= 0

    def contains_enclosure(self, other: RationalEnclosure) -> bool:
        return (self.lower.compare_value(other.lower) <= 0
                and other.upper.compare_value(self.upper) <= 0)


def _validate_division_trace(trace: BRCDivisionTrace, n: int, d: int) -> None:
    if not isinstance(trace, BRCDivisionTrace):
        raise TypeError("BRC division trace required")
    for name in ("numerator", "denominator", "quotient", "remainder", "collapsed_numerator"):
        _integer(name, getattr(trace, name), 0)
    if (trace.numerator != n or trace.denominator != d
        or trace.collapsed_numerator != d * trace.quotient
        or trace.reconstruct() != n or not 0 <= trace.remainder < d):
        raise ValueError("invalid or mismatched BRC division trace")


@dataclass(frozen=True)
class IntegerResidual:
    """Exact value x = index/scale + remainder/(denominator*scale).

    source.numerator*scale = index*source.denominator + remainder,
    with 0 <= remainder < source.denominator. Negative values use FLOOR,
    not truncation toward zero. Remainder is exact information, not an error bar.
    """
    source: SignedDivisionExpr
    scale: int
    index: int
    remainder: int
    magnitude_trace: BRCDivisionTrace

    def __post_init__(self) -> None:
        if not isinstance(self.source, SignedDivisionExpr):
            raise TypeError("signed exact source required")
        _integer("scale", self.scale, 1)
        _integer("index", self.index)
        _integer("remainder", self.remainder, 0)
        n, d = self.source.numerator, self.source.denominator
        _validate_division_trace(self.magnitude_trace, abs(n) * self.scale, d)
        if self.remainder >= d or n * self.scale != self.index * d + self.remainder:
            raise ValueError("integer-residual reconstruction failed")

    @property
    def denominator(self) -> int:
        return self.source.denominator

    @property
    def additive_residual(self) -> SignedDivisionExpr:
        return SignedDivisionExpr(self.remainder, self.denominator * self.scale)

    @property
    def on_grid(self) -> bool:
        return self.remainder == 0

    def enclosure(self) -> RationalEnclosure:
        lo = SignedDivisionExpr(self.index, self.scale)
        hi = lo if self.on_grid else SignedDivisionExpr(self.index + 1, self.scale)
        return RationalEnclosure(lo, hi)

    def refine(self, factor: int) -> IntegerResidual:
        """Integer-multiple refinement, preserving the original unreduced source."""
        _integer("factor", factor, 1)
        result = self.source.at_scale(self.scale * factor)
        carry = brc_evaluate_division(DivisionExpr(factor * self.remainder, self.denominator))
        if (result.index != factor * self.index + carry.quotient
            or result.remainder != carry.remainder):
            raise ArithmeticError("refinement carry law failed")
        return result

    def to_wire(self) -> dict[str, str]:
        """Decimal strings prevent an intermediate binary-number JSON parser."""
        return {"schema": "EM_INTEGER_RESIDUAL_V1", "kind": "EXACT_RATIONAL",
                "numerator": str(self.source.numerator), "denominator": str(self.denominator),
                "scale": str(self.scale), "index": str(self.index), "remainder": str(self.remainder)}

    @classmethod
    def from_wire(cls, record: dict[str, str]) -> IntegerResidual:
        keys = {"schema", "kind", "numerator", "denominator", "scale", "index", "remainder"}
        if not isinstance(record, dict) or set(record) != keys:
            raise ValueError("unexpected wire schema fields")
        if record["schema"] != "EM_INTEGER_RESIDUAL_V1" or record["kind"] != "EXACT_RATIONAL":
            raise ValueError("wrong residual schema or kind")
        values = {}
        for key in ("numerator", "denominator", "scale", "index", "remainder"):
            text = record[key]
            if not isinstance(text, str) or re.fullmatch(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)", text) is None:
                raise ValueError("canonical decimal integer strings required")
            values[key] = int(text)
        out = SignedDivisionExpr(values["numerator"], values["denominator"]).at_scale(values["scale"])
        if out.index != values["index"] or out.remainder != values["remainder"]:
            raise ValueError("wire reconstruction certificate is inconsistent")
        return out


def brc_signed_scaled_evaluate(source: SignedDivisionExpr, scale: int) -> IntegerResidual:
    if not isinstance(source, SignedDivisionExpr):
        raise TypeError("signed exact source required")
    _integer("scale", scale, 1)
    positive = brc_scaled_evaluate(DivisionExpr(abs(source.numerator), source.denominator), scale)
    q, r = positive.scaled_value, positive.residual_numerator
    if source.numerator < 0:
        q, r = (-q - 1, source.denominator - r) if r else (-q, 0)
    return IntegerResidual(source, scale, q, r, positive.trace)


@dataclass(frozen=True)
class RationalRootResidual:
    """Nonnegative rational root with POLYNOMIAL, not additive, residual.

    For x = root_degree(n/d): n*scale**degree = d*index**degree + residual.
    The residual is in radicand units; residual/(d*scale) is NOT x-index/scale.
    """
    source: SignedDivisionExpr
    degree: int
    scale: int
    index: int
    residual: int
    division_trace: BRCDivisionTrace
    root_trace: BRCRootTrace

    def __post_init__(self) -> None:
        if not isinstance(self.source, SignedDivisionExpr):
            raise TypeError("signed exact source required")
        _integer("numerator", self.source.numerator, 0)
        for name in ("degree", "scale"):
            _integer(name, getattr(self, name), 1)
        _integer("index", self.index, 0)
        _integer("residual", self.residual, 0)
        n, d, k = self.source.numerator, self.source.denominator, self.degree
        scaled = n * self.scale**k
        _validate_division_trace(self.division_trace, scaled, d)
        t = self.root_trace
        if not isinstance(t, BRCRootTrace):
            raise TypeError("BRC root trace required")
        for name in ("radicand", "degree", "root_index", "collapsed_radicand", "remainder", "next_power"):
            _integer(name, getattr(t, name), 0)
        if (t.radicand != self.division_trace.quotient or t.degree != k
            or t.root_index != self.index or t.collapsed_radicand != self.index**k
            or t.next_power != (self.index + 1)**k or t.reconstruct() != t.radicand
            or not 0 <= t.remainder < t.basin_width):
            raise ValueError("invalid or mismatched root trace")
        width = d * ((self.index + 1)**k - self.index**k)
        if scaled != d * self.index**k + self.residual or self.residual >= width:
            raise ValueError("root polynomial residual certificate failed")

    @property
    def on_grid(self) -> bool:
        return self.residual == 0

    def enclosure(self) -> RationalEnclosure:
        lo = SignedDivisionExpr(self.index, self.scale)
        hi = lo if self.on_grid else SignedDivisionExpr(self.index + 1, self.scale)
        return RationalEnclosure(lo, hi)

    def refine(self, factor: int) -> RationalRootResidual:
        _integer("factor", factor, 1)
        return brc_rational_root_scaled_evaluate(self.source, self.degree, self.scale * factor)


def brc_rational_root_scaled_evaluate(source: SignedDivisionExpr, degree: int,
                                      scale: int) -> RationalRootResidual:
    if not isinstance(source, SignedDivisionExpr):
        raise TypeError("signed exact source required")
    _integer("numerator", source.numerator, 0)
    _integer("degree", degree, 1)
    _integer("scale", scale, 1)
    scaled = source.numerator * scale**degree
    division_trace = brc_evaluate_division(DivisionExpr(scaled, source.denominator))
    root_trace = brc_evaluate_root(RootExpr(division_trace.quotient, degree))
    q = root_trace.root_index
    return RationalRootResidual(source, degree, scale, q,
                                scaled - source.denominator * q**degree,
                                division_trace, root_trace)
