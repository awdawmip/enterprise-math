"""Exact integer coordinate model for the HCP contact graph used by P022.

Vertices are triples ``(q, r, k)``. Each fixed ``k`` is a triangular lattice
with axial coordinates ``(q,r)``. Even layers are A layers and odd layers are
B layers in the ABAB close-packed stacking.

Every vertex has six in-layer neighbors and three neighbors in each adjacent
layer, hence degree 12. The model is purely combinatorial; no floating-point
sphere centers are required.

Besides the exact graph-distance formula, the module provides two independent
ways to count shortest paths:

1. inward dynamic programming on the graph metric;
2. a Laurent-coefficient formula obtained by separating monotone cross-layer
   moves from in-layer triangular moves.

Their agreement is a useful internal check on the P022 multiplicity results.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb

HCPPoint = tuple[int, int, int]
LaurentPolynomial = dict[tuple[int, int], int]

_TRIANGULAR_STEPS = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, -1),
    (-1, 1),
)


def _require_point(point: HCPPoint) -> None:
    if not isinstance(point, tuple) or len(point) != 3:
        raise ValueError("HCP point must be an integer triple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in point):
        raise ValueError("HCP coordinates must be integers")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def triangular_distance(q: int, r: int) -> int:
    """Graph distance from zero in one triangular close-packed layer."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, r)):
        raise ValueError("triangular coordinates must be integers")
    return max(abs(q), abs(r), abs(q + r))


def hcp_neighbors(point: HCPPoint) -> tuple[HCPPoint, ...]:
    """Return the 12 contact neighbors in the ABAB HCP graph."""
    _require_point(point)
    q, r, k = point
    same_layer = tuple((q + dq, r + dr, k) for dq, dr in _TRIANGULAR_STEPS)
    if k % 2 == 0:
        cross_offsets = ((0, 0), (-1, 0), (0, -1))
    else:
        cross_offsets = ((0, 0), (1, 0), (0, 1))
    cross_layer = tuple(
        (q + dq, r + dr, next_k)
        for next_k in (k - 1, k + 1)
        for dq, dr in cross_offsets
    )
    result = same_layer + cross_layer
    if len(set(result)) != 12:
        raise AssertionError("HCP contact graph must have twelve distinct neighbors")
    return result


def _distance_to_b_layer_base_triangle(q: int, r: int) -> int:
    """Triangular distance from (q,r) to {(0,0),(-1,0),(0,-1)}."""
    return min(
        triangular_distance(q, r),
        triangular_distance(q + 1, r),
        triangular_distance(q, r + 1),
    )


def hcp_graph_distance(point: HCPPoint) -> int:
    """Exact contact-graph distance from the origin ``(0,0,0)``.

    Write ``|k|=2m`` for an even target layer. Every pair of cross-layer
    moves can realize one triangular-lattice step (or zero), so the mandatory
    vertical motion absorbs up to ``m`` units of horizontal triangular
    distance ``h``. Hence

        d = m + max(m, h).

    Write ``|k|=2m+1`` for an odd target layer. The unpaired A->B move lands
    in the base triangle S={(0,0),(-1,0),(0,-1)} and each remaining pair can
    realize one triangular step. If ``tau`` is distance to S, then

        d = m + 1 + max(m, tau).

    Lower bound: pair the cross-layer steps of any path. Each pair changes the
    triangular coordinate by at most one, while an odd path has one unpaired
    base-triangle offset. The remaining displacement must be supplied by
    in-layer steps. Monotone vertical paths attain the bound.
    """
    _require_point(point)
    q, r, k = point
    vertical = abs(k)
    if vertical % 2 == 0:
        half = vertical // 2
        horizontal = triangular_distance(q, r)
        return half + max(half, horizontal)
    half = (vertical - 1) // 2
    triangle_distance = _distance_to_b_layer_base_triangle(q, r)
    return half + 1 + max(half, triangle_distance)


def hcp_shell(radius: int) -> tuple[HCPPoint, ...]:
    """Enumerate exactly the radius shell using the closed distance formula."""
    _require_natural("radius", radius)
    if radius == 0:
        return ((0, 0, 0),)
    # |k| cannot exceed path length. For horizontal coordinates, the odd-layer
    # base triangle can shift q/r by one, so radius+1 is a safe finite box.
    bound = radius + 1
    return tuple(
        (q, r, k)
        for k in range(-radius, radius + 1)
        for q in range(-bound, bound + 1)
        for r in range(-bound, bound + 1)
        if hcp_graph_distance((q, r, k)) == radius
    )


@lru_cache(maxsize=None)
def hcp_geodesic_path_count(point: HCPPoint) -> int:
    """Number of shortest contact-graph paths from the origin to ``point``.

    The recurrence is exact and finite:

        g(0)=1,
        g(v)=sum_{u~v, d(u)=d(v)-1} g(u).
    """
    _require_point(point)
    distance = hcp_graph_distance(point)
    if distance == 0:
        if point != (0, 0, 0):
            raise AssertionError("only the origin has HCP graph distance zero")
        return 1
    inward = tuple(
        neighbor
        for neighbor in hcp_neighbors(point)
        if hcp_graph_distance(neighbor) == distance - 1
    )
    if not inward:
        raise AssertionError("every non-origin HCP state must have an inward neighbor")
    return sum(hcp_geodesic_path_count(neighbor) for neighbor in inward)


def _poly_multiply(left: LaurentPolynomial, right: LaurentPolynomial) -> LaurentPolynomial:
    output: LaurentPolynomial = {}
    for (left_q, left_r), left_count in left.items():
        for (right_q, right_r), right_count in right.items():
            key = (left_q + right_q, left_r + right_r)
            output[key] = output.get(key, 0) + left_count * right_count
    return output


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


def _triangular_step_polynomial() -> LaurentPolynomial:
    return {step: 1 for step in _TRIANGULAR_STEPS}


def _vertical_pair_polynomial() -> LaurentPolynomial:
    """Horizontal displacement counts of one A->B->A vertical pair.

    A vertical pair has six nonzero triangular displacements, each once, and
    zero displacement in three distinct ways. Hence its polynomial is A+3.
    """
    polynomial = _triangular_step_polynomial()
    polynomial[(0, 0)] = 3
    return polynomial


def _base_triangle_polynomial() -> LaurentPolynomial:
    return {(0, 0): 1, (-1, 0): 1, (0, -1): 1}


def hcp_geodesic_path_count_coefficient(point: HCPPoint) -> int:
    """Independent exact Laurent-coefficient formula for HCP shortest paths.

    A geodesic never needs vertical backtracking: two extra cross-layer steps
    cost two while producing at most one triangular unit of horizontal motion,
    which can be supplied by one in-layer step instead.

    For ``|k|=2m``, let ``t=max(0,h-m)``. There are ``2m`` monotone vertical
    steps and ``t`` in-layer steps. The vertical horizontal-displacement
    polynomial is ``(A+3)^m`` and the in-layer polynomial is ``A^t``.

    For ``|k|=2m+1``, one extra A->B step contributes the base-triangle
    polynomial ``B=1+x^-1+y^-1``.

    The factor ``C(d,t)`` chooses the positions of the in-layer steps among the
    total geodesic word while preserving both internal orders.
    """
    _require_point(point)
    q, r, k = point
    vertical = abs(k)
    triangular = _triangular_step_polynomial()
    pair = _vertical_pair_polynomial()

    if vertical % 2 == 0:
        half = vertical // 2
        in_layer = max(0, triangular_distance(q, r) - half)
        distance = vertical + in_layer
        polynomial = _poly_multiply(
            _poly_power(pair, half),
            _poly_power(triangular, in_layer),
        )
    else:
        half = (vertical - 1) // 2
        in_layer = max(0, _distance_to_b_layer_base_triangle(q, r) - half)
        distance = vertical + in_layer
        polynomial = _poly_multiply(
            _base_triangle_polynomial(),
            _poly_multiply(
                _poly_power(pair, half),
                _poly_power(triangular, in_layer),
            ),
        )

    return comb(distance, in_layer) * polynomial.get((q, r), 0)


def triangular_shell_total_geodesic_paths(radius: int) -> int:
    """Total geodesic words ending on a triangular-lattice radius shell."""
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return 6 * (2 ** radius) - 6


def base_triangle_shell_total_geodesic_paths(radius: int) -> int:
    """Geodesic words of length ``radius`` moving outward from the B base triangle."""
    _require_natural("radius", radius)
    return 9 * (2 ** radius) - 6


def hcp_shell_count(radius: int) -> int:
    """Exact number of HCP vertices at native graph radius ``radius``."""
    return len(hcp_shell(radius))


def hcp_shell_total_geodesic_paths(radius: int) -> int:
    """Total shortest-path multiplicity over one HCP graph shell by endpoints."""
    return sum(hcp_geodesic_path_count(point) for point in hcp_shell(radius))


def hcp_shell_total_geodesic_paths_closed(radius: int) -> int:
    """Pure-integer finite-sum formula for the HCP shell geodesic total.

    Fix a target layer and separate mandatory monotone cross-layer steps from
    extra in-layer steps. For a non-extreme even layer ``|k|=2m<r``, reaching
    the shell boundary forces every vertical pair to use a nonzero triangular
    displacement, so the horizontal coefficient sum becomes the triangular
    shell geodesic total at radius ``r-m``. The interleaving factor is
    ``C(r,r-2m)``.

    For a non-extreme odd layer ``|k|=2m+1<r``, the analogous boundary is the
    distance shell around the three-point B base triangle, with total
    ``9*2^(r-m-1)-6``.

    Extreme layers have no in-layer steps; evaluating the vertical polynomials
    at one gives ``9^m`` for an even extreme layer and ``3*9^m`` for an odd
    extreme layer. The two signs of every nonzero k contribute equally.
    """
    _require_natural("radius", radius)
    if radius == 0:
        return 1

    total = 0

    # Even target layers k=+-2m, with k=0 counted only once.
    for half in range(radius // 2 + 1):
        in_layer = radius - 2 * half
        layer_copies = 1 if half == 0 else 2
        if in_layer > 0:
            total += (
                layer_copies
                * comb(radius, in_layer)
                * triangular_shell_total_geodesic_paths(radius - half)
            )
        else:
            total += layer_copies * (9 ** half)

    # Odd target layers k=+-(2m+1); there are always two copies.
    for half in range((radius - 1) // 2 + 1):
        in_layer = radius - (2 * half + 1)
        if in_layer > 0:
            total += (
                2
                * comb(radius, in_layer)
                * base_triangle_shell_total_geodesic_paths(radius - half - 1)
            )
        else:
            total += 6 * (9 ** half)

    return total


def hcp_shell_total_geodesic_paths_recurrence(radius: int) -> int:
    """Fixed integer recurrence equivalent to the finite-sum formula for r>=1.

    Initial values T_1..T_7 are

        12, 84, 384, 1524, 5592, 19812, 68808.

    For n>=8,

      T_n = 10 T_(n-1) - 35 T_(n-2) + 42 T_(n-3) + 28 T_(n-4)
            -112 T_(n-5) + 92 T_(n-6) - 24 T_(n-7).

    Its characteristic polynomial factors as

      (x-3)(x-2)(x-1)(x^2-2)(x^2-4x+2),

    so the dominant algebraic growth root is 2+sqrt(2). The recurrence itself
    remains an exact integer computation and does not use that real-number
    asymptotic description.
    """
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    values = [None, 12, 84, 384, 1524, 5592, 19812, 68808]
    if radius <= 7:
        result = values[radius]
        if result is None:
            raise AssertionError("radius-one indexing must be populated")
        return result
    for current in range(8, radius + 1):
        values.append(
            10 * values[current - 1]
            - 35 * values[current - 2]
            + 42 * values[current - 3]
            + 28 * values[current - 4]
            - 112 * values[current - 5]
            + 92 * values[current - 6]
            - 24 * values[current - 7]
        )
    result = values[radius]
    if result is None:
        raise AssertionError("recurrence result must be populated")
    return result


def hcp_shell_multiplicity_spectrum(radius: int) -> tuple[tuple[int, int], ...]:
    """Return sorted ``(path_multiplicity, endpoint_count)`` pairs for a shell."""
    counts: dict[int, int] = {}
    for point in hcp_shell(radius):
        multiplicity = hcp_geodesic_path_count(point)
        counts[multiplicity] = counts.get(multiplicity, 0) + 1
    return tuple(sorted(counts.items()))
