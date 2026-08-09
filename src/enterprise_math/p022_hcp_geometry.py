"""Exact integer coordinate model for the HCP contact graph used by P022.

Vertices are triples ``(q, r, k)``.  Each fixed ``k`` is a triangular lattice
with axial coordinates ``(q,r)``.  Even layers are A layers and odd layers are
B layers in the ABAB close-packed stacking.

Every vertex has six in-layer neighbors and three neighbors in each adjacent
layer, hence degree 12.  The model is purely combinatorial; no floating-point
sphere centers are required.
"""

from __future__ import annotations

from functools import lru_cache

HCPPoint = tuple[int, int, int]


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
    same_layer = (
        (q + 1, r, k),
        (q - 1, r, k),
        (q, r + 1, k),
        (q, r - 1, k),
        (q + 1, r - 1, k),
        (q - 1, r + 1, k),
    )
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

    Write ``|k|=2m`` for an even target layer.  Every pair of cross-layer
    moves can realize one triangular-lattice step (or zero), so the mandatory
    vertical motion absorbs up to ``m`` units of horizontal triangular
    distance ``h``.  Hence

        d = m + max(m, h).

    Write ``|k|=2m+1`` for an odd target layer.  The unpaired A->B move lands
    in the base triangle S={(0,0),(-1,0),(0,-1)} and each remaining pair can
    realize one triangular step.  If ``tau`` is distance to S, then

        d = m + 1 + max(m, tau).

    The lower bound follows by pairing all cross-layer moves: two such moves
    change horizontal triangular distance by at most one, while an odd path
    has one unpaired A/B offset.  Monotone vertical paths attain the bounds.
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
    # |k| cannot exceed path length.  For the horizontal coordinates, the odd
    # layer base triangle can shift q/r by one, so radius+1 is a safe exact
    # finite enumeration box before filtering by hcp_graph_distance.
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

    It retains path multiplicity without enumerating complete path objects.
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


def hcp_shell_count(radius: int) -> int:
    """Exact number of HCP vertices at native graph radius ``radius``."""
    return len(hcp_shell(radius))


def hcp_shell_total_geodesic_paths(radius: int) -> int:
    """Total shortest-path multiplicity over one HCP graph shell."""
    return sum(hcp_geodesic_path_count(point) for point in hcp_shell(radius))


def hcp_shell_multiplicity_spectrum(radius: int) -> tuple[tuple[int, int], ...]:
    """Return sorted ``(path_multiplicity, endpoint_count)`` pairs for a shell."""
    counts: dict[int, int] = {}
    for point in hcp_shell(radius):
        multiplicity = hcp_geodesic_path_count(point)
        counts[multiplicity] = counts.get(multiplicity, 0) + 1
    return tuple(sorted(counts.items()))
