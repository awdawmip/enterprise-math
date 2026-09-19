"""Candidate integer/residual adapter for the existing BRC exact facade.

This is a domain-facade extension, not a replacement arithmetic foundation.
No binary floating state is accepted. Arithmetic source, observation scale and
provenance remain separate. Numeric equality never authorizes native-state or
branch-history collapse. General algebraic/analytic closure is NOT implemented.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Literal

from .exact_arithmetic import (
    BRCRootScaledReadout, DivisionExpr, RootExpr, add_divisions,
    brc_integer_value, brc_scaled_evaluate, brc_scaled_evaluate_root,
    multiply_divisions,
)


def _integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer, not an approximate input")


def _positive(name: str, value: int) -> None:
    _integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


@dataclass(frozen=True, slots=True)
class Origin:
    """Shared immutable expression nodes; caller labels are not attestations.

    These nodes preserve scalar expression history, NOT a complete native path.
    Native branch identity and multiplicity must still be carried by their owner.
    """
    operation: str
    literal: tuple[int, int]
    parents: tuple[Origin, ...] = ()
    label: str = ""

    def __post_init__(self) -> None:
        if self.operation not in ("INPUT", "ADD", "MUL", "NEG", "RECIPROCAL"):
            raise ValueError("unsupported source operation")
        if not isinstance(self.literal, tuple) or len(self.literal) != 2:
            raise TypeError("literal must be a signed numerator/positive denominator pair")
        _integer("literal numerator", self.literal[0])
        _positive("literal denominator", self.literal[1])
        if not isinstance(self.parents, tuple) or any(not isinstance(p, Origin) for p in self.parents):
            raise TypeError("parents must be an immutable Origin tuple")
        if not isinstance(self.label, str):
            raise TypeError("label must be a string")


@dataclass(frozen=True, slots=True)
class SignedDivisionSource:
    """Signed extension of the upstream natural DivisionExpr, without reduction."""
    magnitude: DivisionExpr
    sign: int
    origin: Origin

    def __post_init__(self) -> None:
        if not isinstance(self.magnitude, DivisionExpr) or not isinstance(self.origin, Origin):
            raise TypeError("source requires a DivisionExpr and an Origin")
        _integer("sign", self.sign)
        if self.sign not in (-1, 0, 1):
            raise ValueError("sign must be -1, 0 or 1")
        if (self.magnitude.numerator == 0) != (self.sign == 0):
            raise ValueError("zero magnitude and zero sign must agree")
        if self.origin.literal != (self.numerator, self.denominator):
            raise ValueError("source literal and arithmetic carrier must agree")

    @classmethod
    def from_pair(cls, numerator: int, denominator: int = 1, *, label: str = "") -> SignedDivisionSource:
        _integer("numerator", numerator)
        _positive("denominator", denominator)
        return cls._make(numerator, denominator, Origin("INPUT", (numerator, denominator), label=label))

    @classmethod
    def _make(cls, numerator: int, denominator: int, origin: Origin) -> SignedDivisionSource:
        return cls(DivisionExpr(abs(numerator), denominator), (numerator > 0) - (numerator < 0), origin)

    @property
    def numerator(self) -> int:
        return self.sign * self.magnitude.numerator

    @property
    def denominator(self) -> int:
        return self.magnitude.denominator

    def value_key(self) -> tuple[int, int]:
        """A rational-value observer only; must NOT be used as a native state key."""
        divisor = gcd(self.magnitude.numerator, self.denominator)
        numerator, _ = brc_integer_value(DivisionExpr(self.magnitude.numerator, divisor))
        denominator, _ = brc_integer_value(DivisionExpr(self.denominator, divisor))
        return self.sign * numerator, denominator

    def compare_value(self, other: SignedDivisionSource) -> int:
        if not isinstance(other, SignedDivisionSource):
            raise TypeError("comparison requires an exact source")
        difference = self.numerator * other.denominator - other.numerator * self.denominator
        return (difference > 0) - (difference < 0)

    def add(self, other: SignedDivisionSource) -> SignedDivisionSource:
        if not isinstance(other, SignedDivisionSource):
            raise TypeError("addition requires an exact source")
        if self.sign == other.sign:
            raw = add_divisions(self.magnitude, other.magnitude)
            numerator, denominator = self.sign * raw.numerator, raw.denominator
        else:
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
        return self._make(numerator, denominator, Origin("ADD", (numerator, denominator), (self.origin, other.origin)))

    def multiply(self, other: SignedDivisionSource) -> SignedDivisionSource:
        if not isinstance(other, SignedDivisionSource):
            raise TypeError("multiplication requires an exact source")
        raw = multiply_divisions(self.magnitude, other.magnitude)
        numerator = self.sign * other.sign * raw.numerator
        return self._make(numerator, raw.denominator, Origin("MUL", (numerator, raw.denominator), (self.origin, other.origin)))

    def negate(self) -> SignedDivisionSource:
        pair = (-self.numerator, self.denominator)
        return self._make(*pair, Origin("NEG", pair, (self.origin,)))

    def reciprocal(self) -> SignedDivisionSource:
        if self.sign == 0:
            raise ZeroDivisionError("zero has no reciprocal")
        pair = (self.sign * self.denominator, self.magnitude.numerator)
        return self._make(*pair, Origin("RECIPROCAL", pair, (self.origin,)))

    def readout(self, scale: int = 1) -> IntegerResidual:
        return IntegerResidual.evaluate(self, scale)


@dataclass(frozen=True, slots=True)
class IntegerResidual:
    """Exact x=(q+r/d)/S with S*n=d*q+r and 0<=r<d.

    The residual is r/(d*S) in value units, not r/d and never a tolerance.
    q uses Euclidean floor convention even when n is negative.
    """
    source: SignedDivisionSource
    scale: int
    quotient: int
    remainder: int

    def __post_init__(self) -> None:
        if not isinstance(self.source, SignedDivisionSource):
            raise TypeError("source must be SignedDivisionSource")
        _positive("scale", self.scale)
        _integer("quotient", self.quotient)
        _integer("remainder", self.remainder)
        if not 0 <= self.remainder < self.denominator:
            raise ValueError("remainder escaped its Euclidean basin")
        if self.denominator * self.quotient + self.remainder != self.scale * self.source.numerator:
            raise ValueError("source/scale/reconstruction mismatch")

    @property
    def denominator(self) -> int:
        return self.source.denominator

    @property
    def exact_at_scale(self) -> bool:
        return self.remainder == 0

    @classmethod
    def evaluate(cls, source: SignedDivisionSource, scale: int = 1) -> IntegerResidual:
        if not isinstance(source, SignedDivisionSource):
            raise TypeError("source must be SignedDivisionSource")
        _positive("scale", scale)
        readout = brc_scaled_evaluate(source.magnitude, scale)
        quotient, remainder = readout.trace.quotient, readout.trace.remainder
        if source.sign < 0:
            quotient = -quotient - int(remainder != 0)
            remainder = 0 if remainder == 0 else source.denominator - remainder
        return cls(source, scale, quotient, remainder)

    def refine(self, factor: int) -> IntegerResidual:
        """Exact residual-only update: q'=t*q+floor(t*r/d), r'=t*r mod d."""
        _positive("factor", factor)
        tail = brc_scaled_evaluate(DivisionExpr(self.remainder, self.denominator), factor)
        return IntegerResidual(self.source, self.scale * factor,
            self.quotient * factor + tail.trace.quotient, tail.trace.remainder)

    def rescale(self, scale: int) -> IntegerResidual:
        """Arbitrary scales re-evaluate the exact source; no rounding feed-back."""
        return self.evaluate(self.source, scale)

    def add(self, other: IntegerResidual) -> IntegerResidual:
        if not isinstance(other, IntegerResidual):
            raise TypeError("addition requires IntegerResidual")
        return self.source.add(other.source).readout(self.scale)

    def multiply(self, other: IntegerResidual) -> IntegerResidual:
        if not isinstance(other, IntegerResidual):
            raise TypeError("multiplication requires IntegerResidual")
        return self.source.multiply(other.source).readout(self.scale)

    def enclosure(self) -> RationalInterval:
        return RationalInterval(self.quotient, self.quotient + int(self.remainder != 0), self.scale)

    def transport_record(self) -> dict[str, object]:
        """All potentially large integers use decimal strings across JSON clients.

        Scalar readout ONLY: full provenance/native state needs a separate owner
        record. No claim that this small record can recover a whole branch graph.
        """
        return {"schema": "EM_INTEGER_RESIDUAL_READOUT_V1", "source_n": str(self.source.numerator),
            "source_d": str(self.denominator), "scale": str(self.scale),
            "quotient": str(self.quotient), "remainder": str(self.remainder),
            "origin_label": self.source.origin.label,
            "provenance_scope": "SCALAR_READOUT_ONLY"}


IntervalRelation = Literal["LT", "EQ", "GT", "UNKNOWN"]


@dataclass(frozen=True, slots=True)
class RationalInterval:
    """Closed [lower/denominator,upper/denominator]; endpoints are exact integers.

    Construction checks ordering, not an external measurement's credibility.
    ``UNKNOWN`` is mandatory for unresolved overlap; overlap never means equal.
    """
    lower: int
    upper: int
    denominator: int

    def __post_init__(self) -> None:
        _integer("lower", self.lower)
        _integer("upper", self.upper)
        _positive("denominator", self.denominator)
        if self.lower > self.upper:
            raise ValueError("interval endpoints reversed")

    def relation(self, other: RationalInterval) -> IntervalRelation:
        if not isinstance(other, RationalInterval):
            raise TypeError("interval comparison requires RationalInterval")
        if self.upper * other.denominator < other.lower * self.denominator:
            return "LT"
        if self.lower * other.denominator > other.upper * self.denominator:
            return "GT"
        if self.lower == self.upper and other.lower == other.upper and self.lower * other.denominator == other.lower * self.denominator:
            return "EQ"
        return "UNKNOWN"

    def contains(self, source: SignedDivisionSource) -> bool:
        if not isinstance(source, SignedDivisionSource):
            raise TypeError("containment requires an exact source")
        return self.lower * source.denominator <= source.numerator * self.denominator <= self.upper * source.denominator

    def add(self, other: RationalInterval) -> RationalInterval:
        if not isinstance(other, RationalInterval):
            raise TypeError("addition requires RationalInterval")
        return RationalInterval(self.lower * other.denominator + other.lower * self.denominator,
            self.upper * other.denominator + other.upper * self.denominator,
            self.denominator * other.denominator)

    def multiply(self, other: RationalInterval) -> RationalInterval:
        if not isinstance(other, RationalInterval):
            raise TypeError("multiplication requires RationalInterval")
        products = (self.lower * other.lower, self.lower * other.upper,
                    self.upper * other.lower, self.upper * other.upper)
        return RationalInterval(min(products), max(products), self.denominator * other.denominator)


@dataclass(frozen=True, slots=True)
class RootResidual:
    """Polynomial residual R=n*S**p-k**p, NOT the additive numerical tail.

    This initial adapter covers nonnegative integer radicands only, matching the
    upstream RootExpr scope. General algebraic expressions remain a later unit.
    """
    readout: BRCRootScaledReadout

    def __post_init__(self) -> None:
        if not isinstance(self.readout, BRCRootScaledReadout):
            raise TypeError("root state requires the upstream root readout")
        s, t = self.readout, self.readout.trace
        if not isinstance(s.source, RootExpr):
            raise TypeError("root source must be RootExpr")
        _positive("scale", s.scale)
        for name in ("radicand", "degree", "root_index", "collapsed_radicand", "remainder", "next_power"):
            _integer(name, getattr(t, name))
        k, p, n = t.root_index, s.source.degree, s.source.radicand
        if k < 0 or t.degree != p or t.radicand != n * s.scale**p or t.collapsed_radicand != k**p or t.next_power != (k+1)**p:
            raise ValueError("root readout/source mismatch")
        if t.remainder != t.radicand - k**p or not 0 <= t.remainder < (k+1)**p-k**p:
            raise ValueError("root polynomial residual mismatch")

    @classmethod
    def evaluate(cls, radicand: int, degree: int = 2, scale: int = 1) -> RootResidual:
        return cls(brc_scaled_evaluate_root(RootExpr(radicand, degree), scale))

    @property
    def polynomial_residual(self) -> int:
        return self.readout.trace.remainder

    def refine(self, factor: int) -> RootResidual:
        _positive("factor", factor)
        s = self.readout
        return RootResidual(brc_scaled_evaluate_root(s.source, s.scale * factor))

    def enclosure(self) -> RationalInterval:
        k = self.readout.trace.root_index
        return RationalInterval(k, k + int(self.polynomial_residual != 0), self.readout.scale)

    def compare_to_rational(self, source: SignedDivisionSource) -> int:
        if not isinstance(source, SignedDivisionSource):
            raise TypeError("root comparison requires an exact rational source")
        if source.sign < 0:
            return 1
        n, p = self.readout.source.radicand, self.readout.source.degree
        delta = n * source.denominator**p - source.numerator**p
        return (delta > 0) - (delta < 0)


@dataclass(frozen=True, slots=True)
class PhaseLabel:
    """Exact rational turns plus original winding; NOT a complex amplitude.

    Phase comparison is a declared periodic observer and cannot collapse path
    histories. Cyclotomic amplitudes/quantum probabilities are not implemented.
    """
    turns: SignedDivisionSource

    def __post_init__(self) -> None:
        if not isinstance(self.turns, SignedDivisionSource):
            raise TypeError("phase label requires an exact turn source")

    def same_phase(self, other: PhaseLabel) -> bool:
        if not isinstance(other, PhaseLabel):
            raise TypeError("phase comparison requires PhaseLabel")
        left, right = self.turns.readout(), other.turns.readout()
        return left.remainder * right.denominator == right.remainder * left.denominator

    def add(self, other: PhaseLabel) -> PhaseLabel:
        if not isinstance(other, PhaseLabel):
            raise TypeError("phase addition requires PhaseLabel")
        return PhaseLabel(self.turns.add(other.turns))


@dataclass(frozen=True, slots=True)
class NativeProjection6:
    """Observer adapter only, not a definition/replacement of native geometry.

    Keeps six signed integer coordinates, literal depth/denominator, common depth
    and a caller-owned path key. No native angle, metric, rotation or quotient is
    inferred by this class. A path key must resolve in the real provenance owner.
    """
    endpoint: tuple[int, ...]
    denominator: int
    common_depth: int
    path_key: str

    def __post_init__(self) -> None:
        if not isinstance(self.endpoint, tuple) or len(self.endpoint) != 6:
            raise ValueError("exactly six native coordinates are required")
        for value in self.endpoint:
            _integer("native coordinate", value)
        _positive("denominator", self.denominator)
        _integer("common_depth", self.common_depth)
        if self.common_depth < 0:
            raise ValueError("common depth must be nonnegative")
        if not isinstance(self.path_key, str) or not self.path_key:
            raise ValueError("explicit owner-resolvable path_key is required")

    def observe(self, scale: int = 1) -> tuple[IntegerResidual, ...]:
        _positive("scale", scale)
        return tuple(SignedDivisionSource.from_pair(v, self.denominator,
            label=f"{self.path_key}:axis-{i}:depth-{self.common_depth}").readout(scale)
            for i, v in enumerate(self.endpoint))
