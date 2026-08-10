"""Exact minimum nondegenerate derivative radius for 1-2-1 support triples.

Consider a primitive abc triple whose prime-coordinate blocks have support
sizes ``(1,2,1)``.  The additive relation has the form

    A*x + B1*y + B2*z = C*w.

Let ``g=gcd(B1,B2)``.  For fixed ``w``, the first coordinate satisfies

    A*x == C*w (mod g).

All bounded solutions of this one congruence are enumerated exactly.  Once
``x`` is fixed, division by ``g`` leaves a coprime two-variable equation

    (B1/g)*y + (B2/g)*z = (C*w-A*x)/g,

whose full integer solution line is intersected with the L-infinity box.
Wronskian degeneracy depends only on the block derivative values, hence only on
``x,w`` after additivity, not on the choice along the ``y,z`` solution line.

This gives an exact O(R) feasibility oracle for radius R (up to tiny congruence
multiplicity), rather than enumerating the four-dimensional witness cube.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_support import abc_support_state
from .abc_unit_relation import raw_block_derivative_coefficients


@dataclass(frozen=True)
class OneTwoOneWitness:
    abc: tuple[int, int, int]
    radius: int
    coordinates: tuple[int, int, int, int]
    derivative_values: tuple[int, int, int]
    wronskian: int


@dataclass(frozen=True)
class OneTwoOneMuResult:
    abc: tuple[int, int, int]
    mu: int
    witness: OneTwoOneWitness
    lower_radius_infeasible: bool


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def _ceil_div(numerator: int, positive_denominator: int) -> int:
    if positive_denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // positive_denominator)


def _affine_parameter_interval(
    origin: int, step: int, radius: int
) -> tuple[int, int] | None:
    """Return integer t with ``|origin+step*t|<=radius``."""
    if step == 0:
        return None if abs(origin) > radius else (-10**100, 10**100)
    if step < 0:
        origin = -origin
        step = -step
    lower = _ceil_div(-radius - origin, step)
    upper = (radius - origin) // step
    if lower > upper:
        return None
    return lower, upper


def _bounded_coprime_pair_solution(
    p: int, q: int, target: int, radius: int
) -> tuple[int, int] | None:
    """Solve ``p*y+q*z=target`` inside the symmetric radius box."""
    if gcd(p, q) != 1:
        raise ValueError("pair coefficients must be coprime")
    g, s, t = _extended_gcd(p, q)
    if g != 1:
        raise AssertionError("coprime coefficients lost Bezout identity")
    y0 = s * target
    z0 = t * target
    # y=y0+q*k, z=z0-p*k.
    first = _affine_parameter_interval(y0, q, radius)
    second = _affine_parameter_interval(z0, -p, radius)
    if first is None or second is None:
        return None
    lower = max(first[0], second[0])
    upper = min(first[1], second[1])
    if lower > upper:
        return None
    # Any k in the intersection works.  Choose the endpoint with smaller box
    # radius merely for a stable deterministic witness.
    candidates = {lower, upper}
    k = min(
        candidates,
        key=lambda value: (
            max(abs(y0 + q * value), abs(z0 - p * value)),
            abs(value),
            value,
        ),
    )
    y = y0 + q * k
    z = z0 - p * k
    if p * y + q * z != target or max(abs(y), abs(z)) > radius:
        raise AssertionError("bounded pair solver escaped its equation/box")
    return y, z


def _congruence_values_in_box(
    coefficient: int, rhs: int, modulus: int, radius: int
) -> tuple[int, ...]:
    """Return all x in [-R,R] solving ``coefficient*x == rhs mod modulus``."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    d = gcd(coefficient, modulus)
    if rhs % d:
        return ()
    reduced_modulus = modulus // d
    if reduced_modulus == 1:
        residue = 0
    else:
        inverse = pow(coefficient // d, -1, reduced_modulus)
        residue = ((rhs // d) * inverse) % reduced_modulus
    lower_k = _ceil_div(-radius - residue, reduced_modulus)
    upper_k = (radius - residue) // reduced_modulus
    return tuple(
        residue + k * reduced_modulus
        for k in range(lower_k, upper_k + 1)
    )


def one_two_one_coefficients(
    a: int, b: int, c: int
) -> tuple[int, int, int, int]:
    """Return ``(A,B1,B2,C)`` for an abc triple with support sizes (1,2,1)."""
    abc_support_state(a, b, c)
    blocks = tuple(raw_block_derivative_coefficients(n) for n in (a, b, c))
    if tuple(len(block) for block in blocks) != (1, 2, 1):
        raise ValueError("require prime-coordinate support sizes exactly (1,2,1)")
    A = blocks[0][0][1]
    B1 = blocks[1][0][1]
    B2 = blocks[1][1][1]
    C = blocks[2][0][1]
    return A, B1, B2, C


def one_two_one_witness_at_radius(
    a: int, b: int, c: int, radius: int
) -> OneTwoOneWitness | None:
    """Return one exact nondegenerate witness in the radius box, if it exists."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    A, B1, B2, C = one_two_one_coefficients(a, b, c)
    pair_gcd = gcd(B1, B2)
    p = B1 // pair_gcd
    q = B2 // pair_gcd
    if gcd(p, q) != 1:
        raise AssertionError("pair gcd reduction failed")

    for w in range(-radius, radius + 1):
        for x in _congruence_values_in_box(A, C * w, pair_gcd, radius):
            numerator = C * w - A * x
            if numerator % pair_gcd:
                raise AssertionError("congruence reduction failed divisibility")
            target = numerator // pair_gcd
            pair = _bounded_coprime_pair_solution(p, q, target, radius)
            if pair is None:
                continue
            y, z = pair
            derivative_a = A * x
            derivative_b = B1 * y + B2 * z
            derivative_c = C * w
            if derivative_a + derivative_b != derivative_c:
                raise AssertionError("1-2-1 witness escaped additive relation")
            wronskian = a * derivative_b - b * derivative_a
            if wronskian == 0:
                continue
            coordinates = (x, y, z, w)
            actual_radius = max(abs(value) for value in coordinates)
            if actual_radius > radius:
                raise AssertionError("1-2-1 witness escaped requested radius")
            return OneTwoOneWitness(
                abc=(a, b, c),
                radius=actual_radius,
                coordinates=coordinates,
                derivative_values=(derivative_a, derivative_b, derivative_c),
                wronskian=wronskian,
            )
    return None


def exact_one_two_one_mu(
    a: int, b: int, c: int, upper_bound: int
) -> OneTwoOneMuResult:
    """Binary-search exact mu using the monotone bounded feasibility oracle."""
    if (
        isinstance(upper_bound, bool)
        or not isinstance(upper_bound, int)
        or upper_bound <= 0
    ):
        raise ValueError("upper_bound must be a positive integer")
    if one_two_one_witness_at_radius(a, b, c, upper_bound) is None:
        raise ValueError("supplied upper bound contains no nondegenerate witness")
    lower = 1
    upper = upper_bound
    while lower < upper:
        mid = (lower + upper) // 2
        if one_two_one_witness_at_radius(a, b, c, mid) is None:
            lower = mid + 1
        else:
            upper = mid
    mu = lower
    witness = one_two_one_witness_at_radius(a, b, c, mu)
    if witness is None:
        raise AssertionError("binary search ended on infeasible mu")
    lower_infeasible = (
        mu == 1 or one_two_one_witness_at_radius(a, b, c, mu - 1) is None
    )
    if not lower_infeasible:
        raise AssertionError("reported mu was not minimal")
    return OneTwoOneMuResult(
        abc=(a, b, c),
        mu=mu,
        witness=witness,
        lower_radius_infeasible=lower_infeasible,
    )
