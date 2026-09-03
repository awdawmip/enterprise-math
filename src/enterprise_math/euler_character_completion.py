"""Finite certificates for the uniqueness of the Euler character completion.

This module contains no numerical value of pi and uses no trigonometric
function.  It checks the finite algebra supporting three statements:

1. A normalized quadratic form invariant under the quarter-turn
   (x,y) -> (-y,x) is necessarily x^2+y^2.
2. The Cell-rooted inner/outer polygon bounds evolve by geometric and
   harmonic mean steps.
3. The Cell-rooted longitudinal factors telescope to the lower polygon
   precision values, while the dyadic chord mesh tends to zero with an
   explicit algebraic bound.

The final identification of the metric completion with the unit circle and of
its common polygon limit with geometric pi is standard planar completion, not
performed numerically here.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction

from .euler_cell_polygon_pi import PolygonLevel, cell_polygon_levels


@dataclass(frozen=True)
class QuadraticFormCertificate:
    """Coefficient certificate for q(x,y)=a*x^2+2*b*x*y+c*y^2."""

    a: Fraction
    b: Fraction
    c: Fraction

    def evaluate(self, x: Fraction, y: Fraction) -> Fraction:
        return self.a * x * x + 2 * self.b * x * y + self.c * y * y

    def quarter_turn_evaluate(self, x: Fraction, y: Fraction) -> Fraction:
        return self.evaluate(-y, x)

    def invariant_on(self, samples: list[tuple[Fraction, Fraction]]) -> bool:
        return all(
            self.evaluate(x, y) == self.quarter_turn_evaluate(x, y)
            for x, y in samples
        )

    @property
    def normalized_identity(self) -> bool:
        return self.evaluate(Fraction(1), Fraction(0)) == 1

    @property
    def is_unique_normalized_solution(self) -> bool:
        return self.a == 1 and self.b == 0 and self.c == 1


def solve_normalized_quarter_turn_form(
    *,
    q10: Fraction = Fraction(1),
) -> QuadraticFormCertificate:
    """Solve the finite coefficient equations forced by J-isometry.

    Invariance at (1,0) gives c=a.  Invariance at (1,1) gives b=0.
    Normalization q(1,0)=q10 gives a=q10.  The project uses q10=1.
    """

    if q10 <= 0:
        raise ValueError("the identity normalization must be positive")
    return QuadraticFormCertificate(a=q10, b=Fraction(0), c=q10)


def character_norm_square(x: Fraction, y: Fraction) -> Fraction:
    return x * x + y * y


def character_mul(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """Multiply (x+yJ)(u+vJ) with J^2=-1."""

    x, y = left
    u, v = right
    return x * u - y * v, x * v + y * u


def verify_norm_multiplicativity(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> bool:
    product = character_mul(left, right)
    return character_norm_square(*product) == (
        character_norm_square(*left) * character_norm_square(*right)
    )


@dataclass(frozen=True)
class MeanRenormalizationStep:
    level: int
    lower: Decimal
    upper: Decimal
    next_lower: Decimal
    next_upper: Decimal
    geometric_residual: Decimal
    harmonic_residual: Decimal

    @property
    def valid(self) -> bool:
        return self.geometric_residual == 0 and self.harmonic_residual == 0


def _require_precision(precision: int) -> None:
    if isinstance(precision, bool) or not isinstance(precision, int) or precision < 40:
        raise ValueError("precision must be an integer of at least 40 digits")


def mean_renormalization_step(
    current: PolygonLevel,
    following: PolygonLevel,
) -> MeanRenormalizationStep:
    """Check a'²=a*b and b'=2*a'*b/(a'+b) in one Decimal context."""

    if following.level != current.level + 1:
        raise ValueError("polygon levels must be consecutive")
    precision = max(current.precision, following.precision)
    with localcontext() as context:
        context.prec = precision
        lower = +current.lower_area
        upper = +current.upper_area
        next_lower = +following.lower_area
        next_upper = +following.upper_area
        geometric_residual = +(next_lower * next_lower - lower * upper)
        harmonic_residual = +(
            next_upper * (next_lower + upper)
            - 2 * next_lower * upper
        )
        return MeanRenormalizationStep(
            level=current.level,
            lower=lower,
            upper=upper,
            next_lower=next_lower,
            next_upper=next_upper,
            geometric_residual=geometric_residual,
            harmonic_residual=harmonic_residual,
        )


def cell_mean_tower(max_level: int, *, precision: int = 100) -> list[MeanRenormalizationStep]:
    """Return geometric/harmonic certificates beginning at the physical C12 level."""

    _require_precision(precision)
    if isinstance(max_level, bool) or not isinstance(max_level, int) or max_level < 2:
        raise ValueError("max_level must be an integer at least two")
    levels = cell_polygon_levels(max_level, precision=precision)
    return [
        mean_renormalization_step(levels[index], levels[index + 1])
        for index in range(1, max_level)
    ]


def cell_viete_factors(max_level: int, *, precision: int = 100) -> list[Decimal]:
    """Return c_2,...,c_max_level from the Cell-rooted rotor tower."""

    _require_precision(precision)
    if isinstance(max_level, bool) or not isinstance(max_level, int) or max_level < 1:
        raise ValueError("max_level must be a positive integer")
    levels = cell_polygon_levels(max_level, precision=precision)
    return [levels[index].scalar for index in range(2, max_level + 1)]


def cell_viete_partial_product(max_level: int, *, precision: int = 100) -> Decimal:
    """Return product(c_2,...,c_max_level), with the empty product at level one."""

    factors = cell_viete_factors(max_level, precision=precision)
    with localcontext() as context:
        context.prec = precision
        product = Decimal(1)
        for factor in factors:
            product *= factor
        return +product


def verify_cell_viete_telescope(max_level: int, *, precision: int = 100) -> bool:
    """Check lower_n * product(c_2,...,c_n)=3 without using pi."""

    _require_precision(precision)
    levels = cell_polygon_levels(max_level, precision=precision)
    product = cell_viete_partial_product(max_level, precision=precision)
    with localcontext() as context:
        context.prec = precision
        tolerance = Decimal(1).scaleb(-(precision - 15))
        return abs(levels[max_level].lower_area * product - Decimal(3)) <= tolerance


def first_width_exact_decimal(*, precision: int = 100) -> Decimal:
    """Return 21-12*sqrt(3), the exact C12 polygon gap, as Decimal."""

    _require_precision(precision)
    with localcontext() as context:
        context.prec = precision
        return +(Decimal(21) - Decimal(12) * Decimal(3).sqrt())


def uniform_residual_width_bound(level: int, *, precision: int = 100) -> Decimal:
    """Return (21-12*sqrt(3))/4^(level-1) for level>=1."""

    _require_precision(precision)
    if isinstance(level, bool) or not isinstance(level, int) or level < 1:
        raise ValueError("level must be a positive integer")
    with localcontext() as context:
        context.prec = precision
        return +(first_width_exact_decimal(precision=precision) / (Decimal(4) ** (level - 1)))


def verify_uniform_residual_bound(max_level: int, *, precision: int = 100) -> bool:
    _require_precision(precision)
    if isinstance(max_level, bool) or not isinstance(max_level, int) or max_level < 1:
        raise ValueError("max_level must be a positive integer")
    levels = cell_polygon_levels(max_level, precision=precision)
    with localcontext() as context:
        context.prec = precision
        tolerance = Decimal(1).scaleb(-(precision - 15))
        return all(
            level.width <= uniform_residual_width_bound(level.level, precision=precision) + tolerance
            for level in levels[1:]
        )


def chord_mesh(level: int, *, precision: int = 100) -> Decimal:
    """Return ||K_level-1||=2*s_(level+1), computed from the next rotor."""

    _require_precision(precision)
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    levels = cell_polygon_levels(level + 1, precision=precision)
    with localcontext() as context:
        context.prec = precision
        return +(2 * levels[level + 1].skew)


def cayley_mesh_bound(level: int, *, precision: int = 100) -> Decimal:
    """Return 4*tau_1/2^level, an algebraic upper bound for the chord mesh."""

    _require_precision(precision)
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    levels = cell_polygon_levels(1, precision=precision)
    tau_one = levels[1].cayley
    with localcontext() as context:
        context.prec = precision
        return +(4 * tau_one / (Decimal(2) ** level))


def verify_mesh_bound(max_level: int, *, precision: int = 100) -> bool:
    _require_precision(precision)
    if isinstance(max_level, bool) or not isinstance(max_level, int) or max_level < 0:
        raise ValueError("max_level must be a non-negative integer")
    return all(
        chord_mesh(level, precision=precision) < cayley_mesh_bound(level, precision=precision)
        for level in range(max_level + 1)
    )


def phase_fraction(level: int, index: int) -> Fraction:
    """Canonical dyadic phase fraction index/(6*2^level), reduced modulo one."""

    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("index must be an integer")
    sides = 6 * (2**level)
    return Fraction(index % sides, sides)


def verify_phase_refinement(level: int, index: int) -> bool:
    """Check (level,index) and (level+1,2*index) encode the same phase."""

    return phase_fraction(level, index) == phase_fraction(level + 1, 2 * index)


def completion_report(max_level: int = 8, *, precision: int = 100) -> dict[str, object]:
    """Return a compact, serialization-friendly finite completion report."""

    form = solve_normalized_quarter_turn_form()
    levels = cell_polygon_levels(max_level, precision=precision)
    return {
        "quadratic_form": {
            "a": str(form.a),
            "b": str(form.b),
            "c": str(form.c),
            "normalized_unique": form.is_unique_normalized_solution,
        },
        "cell_c12": {
            "lower": str(levels[1].lower_area),
            "upper": str(levels[1].upper_area),
            "width": str(levels[1].width),
        },
        "viete_partial_product": str(
            cell_viete_partial_product(max_level, precision=precision)
        ),
        "lower_times_product": str(
            levels[max_level].lower_area
            * cell_viete_partial_product(max_level, precision=precision)
        ),
        "mesh": str(chord_mesh(max_level, precision=precision)),
        "mesh_bound": str(cayley_mesh_bound(max_level, precision=precision)),
        "mean_steps_valid": all(
            abs(step.geometric_residual) < Decimal(1).scaleb(-(precision - 15))
            and abs(step.harmonic_residual) < Decimal(1).scaleb(-(precision - 15))
            for step in cell_mean_tower(max_level, precision=precision)
        ),
    }
