"""Target-free Cell polygon completion certificates for Euler rotation.

The finite construction starts from the six-direction rotor

    c_0 = 1/2,  s_0 = sqrt(3)/2,

and repeatedly takes the positive normalized adjacency bisector

    c_{n+1} = sqrt((1+c_n)/2),
    s_{n+1} = s_n/(2*c_{n+1}).

At level n there are N_n = 6*2^n phase states.  The quantities

    lower_n = N_n*s_n/2
    upper_n = N_n*tau_n,  tau_n=s_n/(1+c_n)

are respectively the exact normalized areas of the regular polygon inscribed
in and circumscribed about the unit rotation-character circle.  No value of pi
and no trigonometric function is used by the construction.

The current Cell radius r satisfies r^2=1/3.  The first Cell/gate refinement is
n=1 (a twelve-phase polygon), where lower_1=3 exactly, so the corresponding
physical dodecagon has area r^2*3=1.

This module is a finite checker/readout.  It does not identify the character
plane with the primitive native metric plane and it does not promote refined
boundary points to native Cell states.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction

from .euler_native_bisector import QRadial, radial


@dataclass(frozen=True)
class ExactCellPolygonCertificate:
    """Exact Q(r), r^2=1/3, data for the C6 and C12 levels."""

    c6_scalar: QRadial
    c6_skew: QRadial
    c6_tau: QRadial
    c6_lower: QRadial
    c6_upper: QRadial
    c12_scalar: QRadial
    c12_skew: QRadial
    c12_tau: QRadial
    c12_lower: QRadial
    c12_upper: QRadial
    physical_c12_lower: QRadial
    physical_c12_upper: QRadial

    @property
    def valid(self) -> bool:
        r = radial()
        one = QRadial.coerce(1)
        return (
            r * r == QRadial.coerce(Fraction(1, 3))
            and self.c6_scalar * self.c6_scalar
            + self.c6_skew * self.c6_skew
            == one
            and self.c12_scalar * self.c12_scalar
            + self.c12_skew * self.c12_skew
            == one
            and self.c6_tau * (1 + self.c6_scalar) == self.c6_skew
            and self.c12_tau * (1 + self.c12_scalar) == self.c12_skew
            and self.c6_lower == QRadial(Fraction(0), Fraction(9, 2))
            and self.c6_upper == QRadial(Fraction(0), Fraction(6))
            and self.c12_lower == QRadial.coerce(3)
            and self.c12_upper == QRadial(Fraction(24), Fraction(-36))
            and self.physical_c12_lower == one
            and self.physical_c12_upper == QRadial(Fraction(8), Fraction(-12))
        )


def exact_cell_polygon_certificate() -> ExactCellPolygonCertificate:
    """Return exact initial polygon bounds in Q(r), where r=1/sqrt(3)."""

    r = radial()
    c6 = QRadial.coerce(Fraction(1, 2))
    s6 = Fraction(3, 2) * r
    tau6 = r
    lower6 = Fraction(9, 2) * r
    upper6 = 6 * r

    c12 = Fraction(3, 2) * r
    s12 = QRadial.coerce(Fraction(1, 2))
    tau12 = QRadial.coerce(2) - 3 * r
    lower12 = QRadial.coerce(3)
    upper12 = 12 * tau12
    radius_sq = r * r

    return ExactCellPolygonCertificate(
        c6_scalar=c6,
        c6_skew=s6,
        c6_tau=tau6,
        c6_lower=lower6,
        c6_upper=upper6,
        c12_scalar=c12,
        c12_skew=s12,
        c12_tau=tau12,
        c12_lower=lower12,
        c12_upper=upper12,
        physical_c12_lower=radius_sq * lower12,
        physical_c12_upper=radius_sq * upper12,
    )


@dataclass(frozen=True)
class PolygonLevel:
    level: int
    sides: int
    precision: int
    scalar: Decimal
    skew: Decimal
    cayley: Decimal
    lower_area: Decimal
    upper_area: Decimal
    width: Decimal

    @property
    def residual_lower_from_three(self) -> Decimal:
        with localcontext() as context:
            context.prec = self.precision
            return +(self.lower_area - Decimal(3))

    @property
    def residual_upper_from_three(self) -> Decimal:
        with localcontext() as context:
            context.prec = self.precision
            return +(self.upper_area - Decimal(3))


def _require_level(level: int) -> None:
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")


def _close(left: Decimal, right: Decimal, tolerance: Decimal) -> bool:
    return abs(left - right) <= tolerance


def cell_polygon_levels(max_level: int, *, precision: int = 100) -> list[PolygonLevel]:
    """Generate the C_(6*2^n) polygon tower without pi or trigonometry."""

    _require_level(max_level)
    if precision < 40:
        raise ValueError("precision must be at least 40 decimal digits")

    with localcontext() as context:
        context.prec = precision
        two = Decimal(2)
        c = Decimal(1) / two
        s = Decimal(3).sqrt() / two
        result: list[PolygonLevel] = []

        for level in range(max_level + 1):
            sides = 6 * (2**level)
            tau = s / (1 + c)
            lower = Decimal(sides) * s / two
            upper = Decimal(sides) * tau
            result.append(
                PolygonLevel(
                    level=level,
                    sides=sides,
                    precision=precision,
                    scalar=+c,
                    skew=+s,
                    cayley=+tau,
                    lower_area=+lower,
                    upper_area=+upper,
                    width=+(upper - lower),
                )
            )

            next_c = ((1 + c) / two).sqrt()
            next_s = s / (two * next_c)
            c, s = next_c, next_s

        return result


def complex_pair_mul(
    left: tuple[Decimal, Decimal], right: tuple[Decimal, Decimal]
) -> tuple[Decimal, Decimal]:
    """Multiply (a+bJ)(c+dJ) with J^2=-1 in the active Decimal context."""

    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def complex_pair_pow(
    value: tuple[Decimal, Decimal], exponent: int
) -> tuple[Decimal, Decimal]:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a non-negative integer")
    result = (Decimal(1), Decimal(0))
    base = value
    while exponent:
        if exponent & 1:
            result = complex_pair_mul(result, base)
        base = complex_pair_mul(base, base)
        exponent >>= 1
    return result


def regular_vertices(level: PolygonLevel) -> list[tuple[Decimal, Decimal]]:
    """Return powers of the finite rotor, starting from the identity vertex."""

    with localcontext() as context:
        context.prec = level.precision
        step = (level.scalar, level.skew)
        current = (Decimal(1), Decimal(0))
        vertices: list[tuple[Decimal, Decimal]] = []
        for _ in range(level.sides):
            vertices.append((+current[0], +current[1]))
            current = complex_pair_mul(current, step)
        return vertices


def polygon_area(
    vertices: list[tuple[Decimal, Decimal]], *, precision: int = 100
) -> Decimal:
    """Shoelace area of a cyclic polygon in a controlled Decimal context."""

    if len(vertices) < 3:
        raise ValueError("at least three vertices are required")
    with localcontext() as context:
        context.prec = precision
        total = Decimal(0)
        for current, following in zip(vertices, vertices[1:] + vertices[:1]):
            total += current[0] * following[1] - current[1] * following[0]
        return +(abs(total) / 2)


def tangent_intersection(
    first: tuple[Decimal, Decimal],
    second: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    """Intersect tangents first·x=1 and second·x=1 in the active context."""

    a, b = first
    c, d = second
    determinant = a * d - b * c
    if determinant == 0:
        raise ZeroDivisionError("consecutive tangent lines must not be parallel")
    return (d - b) / determinant, (a - c) / determinant


def circumscribed_vertices(level: PolygonLevel) -> list[tuple[Decimal, Decimal]]:
    with localcontext() as context:
        context.prec = level.precision
        unit_vertices = regular_vertices(level)
        return [
            tuple(
                +coordinate
                for coordinate in tangent_intersection(
                    unit_vertices[index],
                    unit_vertices[(index + 1) % level.sides],
                )
            )
            for index in range(level.sides)
        ]


def verify_level(level: PolygonLevel, *, tolerance: Decimal | None = None) -> bool:
    """Check all local finite identities for one generated level."""

    if tolerance is None:
        tolerance = Decimal("1e-70")

    with localcontext() as context:
        context.prec = level.precision
        c = level.scalar
        s = level.skew
        tau = level.cayley
        lower = level.lower_area
        upper = level.upper_area

        half_turn = complex_pair_pow((c, s), level.sides // 2)
        full_turn = complex_pair_pow((c, s), level.sides)
        return (
            _close(c * c + s * s, Decimal(1), tolerance)
            and _close(tau * (1 + c), s, tolerance)
            and _close(tau * s, 1 - c, tolerance)
            and _close(upper - lower, lower * tau * tau, tolerance)
            and _close(half_turn[0], Decimal(-1), tolerance)
            and _close(half_turn[1], Decimal(0), tolerance)
            and _close(full_turn[0], Decimal(1), tolerance)
            and _close(full_turn[1], Decimal(0), tolerance)
        )


def verify_polygon_areas(
    level: PolygonLevel, *, tolerance: Decimal | None = None
) -> bool:
    """Check shoelace areas against the closed lower/upper formulas."""

    if tolerance is None:
        tolerance = Decimal("1e-60")
    with localcontext() as context:
        context.prec = level.precision
        inner = polygon_area(regular_vertices(level), precision=level.precision)
        outer = polygon_area(
            circumscribed_vertices(level), precision=level.precision
        )
        return _close(inner, level.lower_area, tolerance) and _close(
            outer, level.upper_area, tolerance
        )


def width_refinement_factor(
    previous: PolygonLevel, following: PolygonLevel
) -> Decimal:
    """Return W_(n+1)/W_n for consecutive levels."""

    if following.level != previous.level + 1:
        raise ValueError("levels must be consecutive")
    with localcontext() as context:
        context.prec = max(previous.precision, following.precision)
        return +(following.width / previous.width)


def theoretical_width_refinement_factor(following: PolygonLevel) -> Decimal:
    with localcontext() as context:
        context.prec = following.precision
        return +((1 - following.cayley**4) / 4)


def residual_interval_from_three(level: PolygonLevel) -> tuple[Decimal, Decimal]:
    """Finite interval for the unresolved completion residual L-3."""

    if level.level < 1:
        raise ValueError("the exact baseline 3 first occurs at the C12 level")
    return level.residual_lower_from_three, level.residual_upper_from_three


def physical_cell_area_interval(level: PolygonLevel) -> tuple[Decimal, Decimal]:
    """Scale normalized polygon areas by the current Cell radius squared 1/3."""

    with localcontext() as context:
        context.prec = level.precision
        radius_sq = Decimal(1) / Decimal(3)
        return +(radius_sq * level.lower_area), +(radius_sq * level.upper_area)


def refinement_report(
    max_level: int = 8, *, precision: int = 100
) -> list[dict[str, str | int]]:
    """Return a serialization-friendly finite certificate table."""

    levels = cell_polygon_levels(max_level, precision=precision)
    report: list[dict[str, str | int]] = []
    for level in levels:
        physical_lower, physical_upper = physical_cell_area_interval(level)
        report.append(
            {
                "level": level.level,
                "sides": level.sides,
                "lower": str(level.lower_area),
                "upper": str(level.upper_area),
                "width": str(level.width),
                "residual_lower_from_3": str(level.residual_lower_from_three),
                "residual_upper_from_3": str(level.residual_upper_from_three),
                "physical_cell_lower": str(physical_lower),
                "physical_cell_upper": str(physical_upper),
            }
        )
    return report
