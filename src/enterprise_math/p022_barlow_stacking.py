"""Barlow close-packed stacking graphs and exact geodesic coefficient formulas.

A close-packed layer is a triangular lattice.  Each interface chooses one of
two triangular holes for the next layer; encode that choice by a sign ``-1``
or ``+1``.  Any bi-infinite sign sequence gives a Barlow stacking.  Periodic
patterns are represented here by a nonempty tuple of signs.

The key P022 observation is that the complete horizontal witness polynomial of
a monotone vertical segment is the product of the interface polynomials.  This
gives exact graph distance and shortest-path multiplicity by a finite
coefficient search, while keeping the state integer/combinatorial.
"""

from __future__ import annotations

from math import comb

BarlowPoint = tuple[int, int, int]
StackingPattern = tuple[int, ...]
LaurentPolynomial = dict[tuple[int, int], int]

_TRIANGULAR_STEPS = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, -1),
    (-1, 1),
)
_MINUS_OFFSETS = ((0, 0), (-1, 0), (0, -1))
_PLUS_OFFSETS = ((0, 0), (1, 0), (0, 1))


def _require_point(point: BarlowPoint) -> None:
    if not isinstance(point, tuple) or len(point) != 3:
        raise ValueError("Barlow point must be an integer triple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in point):
        raise ValueError("Barlow coordinates must be integers")


def _require_pattern(pattern: StackingPattern) -> None:
    if not isinstance(pattern, tuple) or not pattern:
        raise ValueError("stacking pattern must be a nonempty tuple")
    if any(sign not in (-1, 1) for sign in pattern):
        raise ValueError("stacking signs must be -1 or +1")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def triangular_distance(q: int, r: int) -> int:
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, r)):
        raise ValueError("triangular coordinates must be integers")
    return max(abs(q), abs(r), abs(q + r))


def stacking_sign(pattern: StackingPattern, interface: int) -> int:
    """Sign of the upward interface ``interface -> interface+1``."""
    _require_pattern(pattern)
    if isinstance(interface, bool) or not isinstance(interface, int):
        raise ValueError("interface index must be an integer")
    return pattern[interface % len(pattern)]


def _offsets(sign: int) -> tuple[tuple[int, int], ...]:
    if sign == -1:
        return _MINUS_OFFSETS
    if sign == 1:
        return _PLUS_OFFSETS
    raise ValueError("stacking sign must be -1 or +1")


def barlow_neighbors(point: BarlowPoint, pattern: StackingPattern) -> tuple[BarlowPoint, ...]:
    """Return the twelve contact neighbors for a periodic Barlow stacking."""
    _require_point(point)
    _require_pattern(pattern)
    q, r, k = point
    same = tuple((q + dq, r + dr, k) for dq, dr in _TRIANGULAR_STEPS)

    up_sign = stacking_sign(pattern, k)
    up = tuple((q + dq, r + dr, k + 1) for dq, dr in _offsets(up_sign))

    # The downward edge is the inverse of the upward interface below it.
    below_sign = stacking_sign(pattern, k - 1)
    down = tuple(
        (q - dq, r - dr, k - 1) for dq, dr in _offsets(below_sign)
    )

    result = same + up + down
    if len(set(result)) != 12:
        raise AssertionError("every Barlow contact vertex must have degree twelve")
    return result


def _poly_multiply(left: LaurentPolynomial, right: LaurentPolynomial) -> LaurentPolynomial:
    output: LaurentPolynomial = {}
    for (left_q, left_r), left_count in left.items():
        for (right_q, right_r), right_count in right.items():
            key = (left_q + right_q, left_r + right_r)
            output[key] = output.get(key, 0) + left_count * right_count
    return output


def _triangular_polynomial() -> LaurentPolynomial:
    return {step: 1 for step in _TRIANGULAR_STEPS}


def _interface_polynomial(sign: int) -> LaurentPolynomial:
    return {offset: 1 for offset in _offsets(sign)}


def effective_vertical_signs(pattern: StackingPattern, target_layer: int) -> tuple[int, ...]:
    """Interface signs seen by a monotone path from layer zero to target.

    Downward traversal inverts the upward interface offsets, so its effective
    polynomial sign is negated.
    """
    _require_pattern(pattern)
    if isinstance(target_layer, bool) or not isinstance(target_layer, int):
        raise ValueError("target layer must be an integer")
    if target_layer > 0:
        return tuple(stacking_sign(pattern, interface) for interface in range(target_layer))
    if target_layer < 0:
        return tuple(
            -stacking_sign(pattern, interface)
            for interface in range(-1, target_layer - 1, -1)
        )
    return ()


def stacking_prefix_counts(pattern: StackingPattern, target_layer: int) -> tuple[int, int]:
    """Return ``(minus_count, plus_count)`` on the effective monotone segment."""
    signs = effective_vertical_signs(pattern, target_layer)
    return signs.count(-1), signs.count(1)


def stacking_prefix_imbalance(pattern: StackingPattern, target_layer: int) -> int:
    """Integer ``plus_count-minus_count`` for the root-to-layer segment."""
    minus_count, plus_count = stacking_prefix_counts(pattern, target_layer)
    return plus_count - minus_count


def vertical_witness_polynomial(
    pattern: StackingPattern, target_layer: int
) -> LaurentPolynomial:
    """Horizontal displacement polynomial of the minimal vertical segment."""
    polynomial: LaurentPolynomial = {(0, 0): 1}
    for sign in effective_vertical_signs(pattern, target_layer):
        polynomial = _poly_multiply(polynomial, _interface_polynomial(sign))
    return polynomial


def vertical_witness_polynomial_from_counts(
    minus_count: int, plus_count: int
) -> LaurentPolynomial:
    """Same vertical polynomial using only cumulative sign counts.

    This makes the task-relative compression explicit: for root-to-one-layer
    distance and geodesic-count queries, order inside the traversed stacking
    prefix is invisible because Laurent multiplication is commutative.
    """
    _require_natural("minus_count", minus_count)
    _require_natural("plus_count", plus_count)
    polynomial: LaurentPolynomial = {(0, 0): 1}
    for _ in range(minus_count):
        polynomial = _poly_multiply(polynomial, _interface_polynomial(-1))
    for _ in range(plus_count):
        polynomial = _poly_multiply(polynomial, _interface_polynomial(1))
    return polynomial


def _poly_power(base: LaurentPolynomial, exponent: int) -> LaurentPolynomial:
    _require_natural("exponent", exponent)
    result: LaurentPolynomial = {(0, 0): 1}
    power = dict(base)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = _poly_multiply(result, power)
        remaining //= 2
        if remaining:
            power = _poly_multiply(power, power)
    return result


def barlow_distance_and_geodesic_count(
    point: BarlowPoint, pattern: StackingPattern
) -> tuple[int, int]:
    """Return exact ``(distance, shortest_path_count)`` from the root.

    Any vertical backtracking contains matched crossings of layer interfaces.
    A matched crossing pair has horizontal displacement in the support of
    ``B_- B_+ = A+3``, i.e. triangular distance at most one. Replacing every
    such pair by at most one in-layer move strictly shortens the path. Hence a
    geodesic crosses exactly ``|k|`` interfaces monotonically.

    Let ``P_k`` be the resulting vertical witness polynomial. Because ``P_k``
    always contains the zero monomial, at most ``h(q,r)`` extra in-layer steps
    are needed. Let ``t_*`` be the least t with

        [x^q y^r] P_k A^t > 0.

    Then distance is ``|k|+t_*``. The coefficient counts the ordered choices
    internal to the vertical and horizontal subsequences, and ``C(|k|+t,t)``
    interleaves those subsequences.
    """
    _require_point(point)
    _require_pattern(pattern)
    q, r, k = point
    vertical = vertical_witness_polynomial(pattern, k)
    triangular = _triangular_polynomial()
    horizontal_bound = triangular_distance(q, r)
    horizontal_power: LaurentPolynomial = {(0, 0): 1}

    for in_layer in range(horizontal_bound + 1):
        coefficient = _poly_multiply(vertical, horizontal_power).get((q, r), 0)
        if coefficient > 0:
            distance = abs(k) + in_layer
            return distance, comb(distance, in_layer) * coefficient
        horizontal_power = _poly_multiply(horizontal_power, triangular)

    raise AssertionError("triangular in-layer motion must eventually reach every coordinate")


def barlow_graph_distance(point: BarlowPoint, pattern: StackingPattern) -> int:
    return barlow_distance_and_geodesic_count(point, pattern)[0]


def barlow_geodesic_path_count(point: BarlowPoint, pattern: StackingPattern) -> int:
    return barlow_distance_and_geodesic_count(point, pattern)[1]


def barlow_shell(radius: int, pattern: StackingPattern) -> tuple[BarlowPoint, ...]:
    """Exact finite shell enumeration for a periodic close-packed stacking."""
    _require_natural("radius", radius)
    _require_pattern(pattern)
    if radius == 0:
        return ((0, 0, 0),)
    # Every contact step changes triangular coordinate distance by at most one.
    return tuple(
        (q, r, k)
        for k in range(-radius, radius + 1)
        for q in range(-radius, radius + 1)
        for r in range(-radius, radius + 1)
        if barlow_graph_distance((q, r, k), pattern) == radius
    )


def barlow_shell_multiplicity_spectrum(
    radius: int, pattern: StackingPattern
) -> tuple[tuple[int, int], ...]:
    counts: dict[int, int] = {}
    for point in barlow_shell(radius, pattern):
        multiplicity = barlow_geodesic_path_count(point, pattern)
        counts[multiplicity] = counts.get(multiplicity, 0) + 1
    return tuple(sorted(counts.items()))


def barlow_shell_total_geodesic_paths(radius: int, pattern: StackingPattern) -> int:
    return sum(
        multiplicity * endpoint_count
        for multiplicity, endpoint_count in barlow_shell_multiplicity_spectrum(
            radius, pattern
        )
    )
