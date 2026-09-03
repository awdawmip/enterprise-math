"""Finite cyclic rotation refinement for the Enterprise Euler/precision-pi line.

The exact layer is combinatorial and integer-first:

* a cyclic orientation readout has state group ``C_N``;
* one barycentric phase refinement embeds ``C_N`` into ``C_(2N)`` by ``k -> 2k``;
* every refined state is uniquely ``2*k + epsilon``;
* refined addition contains the binary carry ``epsilon*eta``;
* the extension ``0 -> C_N -> C_(2N) -> C_2 -> 0`` splits iff ``N`` is odd.

The Decimal trace and Viete routines use only the algebraic recursion
``c_0=-1`` and ``c_(n+1)^2=(1+c_n)/2`` with the positive branch. They do
not use the numerical value of pi. ``effective_character`` is deliberately
marked as an external archimedean readout and is only a consistency check.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from math import gcd


class RotationRefinementError(ValueError):
    """Raised when a finite cyclic-refinement contract is violated."""


@dataclass(frozen=True)
class RefinementCoordinates:
    """Unique coordinates ``j = 2*coarse + detail`` in ``C_(2N)``."""

    coarse: int
    detail: int


@dataclass(frozen=True)
class RotationCompletionEnclosure:
    """Finite algebraic enclosure for the rotation-completion constant."""

    depth: int
    lower: Decimal
    upper: Decimal
    tail_defect_bound: Decimal
    next_trace_coordinate: Decimal


def _modulus(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise RotationRefinementError("cyclic modulus must be an integer >= 2")
    return n


def _bit(value: int) -> int:
    if isinstance(value, bool):
        value = int(value)
    if not isinstance(value, int) or value not in (0, 1):
        raise RotationRefinementError("detail coordinate must be 0 or 1")
    return value


def refinement_embedding(index: int, modulus: int) -> int:
    """Embed ``C_N`` into ``C_(2N)`` by retaining old phases as even states."""

    n = _modulus(modulus)
    return (2 * (int(index) % n)) % (2 * n)


def refinement_coordinates(index: int, modulus: int) -> RefinementCoordinates:
    """Return the unique ``(coarse, detail)`` with ``j=2*coarse+detail``."""

    n = _modulus(modulus)
    j = int(index) % (2 * n)
    return RefinementCoordinates(j // 2, j % 2)


def refined_index(coarse: int, detail: int, modulus: int) -> int:
    """Recompose one refined state from its coarse phase and one precision bit."""

    n = _modulus(modulus)
    e = _bit(detail)
    return (2 * (int(coarse) % n) + e) % (2 * n)


def refinement_carry(left_detail: int, right_detail: int) -> int:
    """The exact carry generated when two new midpoint states are added."""

    return _bit(left_detail) * _bit(right_detail)


def add_refinement_coordinates(
    left: RefinementCoordinates,
    right: RefinementCoordinates,
    modulus: int,
) -> RefinementCoordinates:
    """Add states in ``C_(2N)`` in ``(coarse, detail)`` coordinates.

    The law is ``(k,e)+(l,f)=(k+l+e*f, e+f mod 2)``. Thus the new bit is
    not an independent direct-product coordinate when ``N`` is even.
    """

    n = _modulus(modulus)
    e = _bit(left.detail)
    f = _bit(right.detail)
    return RefinementCoordinates(
        (left.coarse + right.coarse + e * f) % n,
        (e + f) % 2,
    )


def refinement_extension_splits(modulus: int) -> bool:
    """Whether ``0 -> C_N -> C_(2N) -> C_2 -> 0`` splits as groups."""

    return _modulus(modulus) % 2 == 1


def splitting_section_generator(modulus: int) -> int | None:
    """Return the order-two odd state defining a split, if it exists."""

    n = _modulus(modulus)
    return n if n % 2 == 1 else None


def element_order(index: int, modulus: int) -> int:
    """Exact additive order of ``index`` in ``C_N``."""

    n = _modulus(modulus)
    j = int(index) % n
    return 1 if j == 0 else n // gcd(n, j)


def half_turn(modulus: int) -> int:
    """The unique half-turn in ``C_N``; requires even ``N``."""

    n = _modulus(modulus)
    if n % 2:
        raise RotationRefinementError("an exact half-turn requires even modulus")
    return n // 2


def half_turn_roots_after_refinement(modulus: int) -> tuple[int, int]:
    """The two square roots of the embedded half-turn in ``C_(2N)``."""

    n = _modulus(modulus)
    if n % 2:
        raise RotationRefinementError("coarse half-turn requires even modulus")
    positive = n // 2
    negative = positive + n
    target = refinement_embedding(half_turn(n), n)
    if (2 * positive) % (2 * n) != target or (2 * negative) % (2 * n) != target:
        raise AssertionError("internal half-turn root certificate failed")
    return positive, negative


def positive_half_arc_root(modulus: int) -> int:
    """Choose the midpoint on the declared positive arc from identity to half-turn."""

    return half_turn_roots_after_refinement(modulus)[0]


def dyadic_modulus(depth: int, *, base_modulus: int = 6) -> int:
    """Modulus after ``depth`` binary subdivisions of the coarse gate cycle."""

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise RotationRefinementError("depth must be a nonnegative integer")
    base = _modulus(base_modulus)
    if base % 2:
        raise RotationRefinementError("base modulus must contain a half-turn")
    return base * (2**depth)


def dyadic_half_turn_root(depth: int, *, base_modulus: int = 6) -> tuple[int, int]:
    """Return ``(modulus,index)`` for the positive iterated half-turn root.

    For the Enterprise six-gate base, the index remains 3 while its order
    doubles at every refinement.
    """

    n = dyadic_modulus(depth, base_modulus=base_modulus)
    root = base_modulus // 2
    target = half_turn(n)
    if ((2**depth) * root) % n != target:
        raise AssertionError("iterated root certificate failed")
    return n, root


def trace_coordinates(depth: int, *, precision: int = 80) -> tuple[Decimal, ...]:
    """Return ``c_0,...,c_depth`` from the positive trace recursion.

    ``c_0=-1`` is the half-turn trace. ``c_1=0`` is the quarter-turn trace.
    No numerical value of pi is used.
    """

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise RotationRefinementError("depth must be a nonnegative integer")
    if precision < 20:
        raise RotationRefinementError("precision must be at least 20 decimal digits")
    with localcontext() as ctx:
        ctx.prec = precision + 12
        values = [Decimal(-1)]
        for _ in range(depth):
            values.append(((Decimal(1) + values[-1]) / Decimal(2)).sqrt())
        ctx.prec = precision
        return tuple(+value for value in values)


def trace_coordinate(depth: int, *, precision: int = 80) -> Decimal:
    """The normalized reversal-even trace at one refinement depth."""

    return trace_coordinates(depth, precision=precision)[-1]


def viete_factors(depth: int, *, precision: int = 80) -> tuple[Decimal, ...]:
    """Return the finite positive trace factors ``c_2,...,c_depth``."""

    if depth < 2:
        raise RotationRefinementError("Viete depth must be at least 2")
    values = trace_coordinates(depth, precision=precision)
    return values[2:]


def rotation_pi_approximant(depth: int, *, precision: int = 80) -> Decimal:
    """Finite rotation-completion readout ``2 / product(c_2,...,c_depth)``."""

    factors = viete_factors(depth, precision=precision + 12)
    with localcontext() as ctx:
        ctx.prec = precision + 12
        product = Decimal(1)
        for factor in factors:
            product *= factor
        value = Decimal(2) / product
        ctx.prec = precision
        return +value


def rotation_completion_enclosure(
    depth: int, *, precision: int = 80
) -> RotationCompletionEnclosure:
    """A finite enclosure for the limit of the algebraic rotation readouts.

    Let ``a_n=1-c_n``. The exact recursion gives
    ``a_(n+1)=a_n/(2*(1+c_(n+1)))``. Hence all ratios are at most
    ``1-sqrt(2)/2`` and ``sum_(j>m) a_j <= sqrt(2)*(1-c_(m+1))``.
    The elementary product bound then yields the returned interval.
    """

    if depth < 2:
        raise RotationRefinementError("enclosure depth must be at least 2")
    with localcontext() as ctx:
        ctx.prec = precision + 16
        values = trace_coordinates(depth + 1, precision=precision + 12)
        lower = rotation_pi_approximant(depth, precision=precision + 12)
        sqrt_two = Decimal(2).sqrt()
        bound = sqrt_two * (Decimal(1) - values[depth + 1])
        if not (Decimal(0) < bound < Decimal(1)):
            raise AssertionError("tail defect bound must lie strictly between 0 and 1")
        upper = lower / (Decimal(1) - bound)
        ctx.prec = precision
        return RotationCompletionEnclosure(
            depth=depth,
            lower=+lower,
            upper=+upper,
            tail_defect_bound=+bound,
            next_trace_coordinate=+values[depth + 1],
        )


def all_refinement_states(modulus: int) -> tuple[RefinementCoordinates, ...]:
    """Enumerate every refined state once in canonical coordinates."""

    n = _modulus(modulus)
    return tuple(refinement_coordinates(j, n) for j in range(2 * n))


def effective_character(depth: int) -> complex:
    """External archimedean character value for the positive root state.

    This function is not part of the native finite derivation: it uses the
    classical complex exponential only to check the bridge to Euler/Viete.
    """

    import cmath
    import math

    n, root = dyadic_half_turn_root(depth)
    return cmath.exp(2j * math.pi * root / n)


def euler_even_odd(value: complex) -> tuple[complex, complex]:
    """Reversal-even and reversal-odd parts of a nonzero character value."""

    if value == 0:
        raise RotationRefinementError("character value must be nonzero")
    inverse = 1 / value
    return (value + inverse) / 2, (value - inverse) / 2


def finite_euler_coordinates(depth: int) -> tuple[complex, complex, complex]:
    """Return ``(u,c,s)`` with exact-form target ``u=c+i*s`` numerically."""

    if depth < 1:
        raise RotationRefinementError("the real sine coordinate uses the refined i frame")
    u = effective_character(depth)
    even, odd = euler_even_odd(u)
    return u, even, odd / 1j
