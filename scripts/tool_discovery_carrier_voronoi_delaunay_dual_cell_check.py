#!/usr/bin/env python3
"""
Exact regression checker for:
RS-TD-VD-CARRIER-VORONOI-DELAUNAY-DUAL-CELL-CALCULUS

This checker is intentionally a discovery/regression artifact, not a native
Enterprise metric implementation.  All Euclidean/triangular calculations
below are explicitly carrier-layer calculations.

No floating-point geometry is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Any, Callable, Dict, FrozenSet, Iterable, Mapping, Sequence, Tuple

F = Fraction
Point = Tuple[Fraction, Fraction]

TERMINAL_CLASSIFICATION = "CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY"
GLOBAL_TOOL_CLAIM = False
SECOND_INDEPENDENT_ENTERPRISE_DISTANCE_FAMILY = False


class SemanticInputError(ValueError):
    pass


class SemanticLayerError(ValueError):
    pass


@dataclass(frozen=True)
class ExactDistanceSemantics:
    name: str
    layer: str
    score: Callable[[Any, Any], Fraction]


def P(x: int | Fraction, y: int | Fraction) -> Point:
    return (F(x), F(y))


def sqnorm(p: Point) -> Fraction:
    return p[0] * p[0] + p[1] * p[1]


def euclidean_sqdist(a: Point, b: Point) -> Fraction:
    return sqnorm((a[0] - b[0], a[1] - b[1]))


EUCLIDEAN_CARRIER = ExactDistanceSemantics(
    name="classical_euclidean_squared_distance",
    layer="carrier",
    score=euclidean_sqdist,
)


def nearest_sites(
    query: Any,
    sites: Mapping[str, Any],
    semantics: ExactDistanceSemantics | None,
    *,
    required_layer: str | None = None,
) -> Tuple[str, ...]:
    if semantics is None:
        raise SemanticInputError("MISSING_DISTANCE_COMPARATOR")
    if required_layer is not None and semantics.layer != required_layer:
        raise SemanticLayerError(
            f"SEMANTIC_LAYER_MISMATCH:{semantics.layer}!={required_layer}"
        )
    if not sites:
        return ()
    values = {label: semantics.score(query, site) for label, site in sites.items()}
    minimum = min(values.values())
    return tuple(sorted(label for label, value in values.items() if value == minimum))


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )


def circumcircle(a: Point, b: Point, c: Point) -> Tuple[Point, Fraction] | None:
    """Exact Cartesian Euclidean circumcircle using rational linear algebra."""
    ax, ay = a
    bx, by = b
    cx, cy = c
    a11 = 2 * (bx - ax)
    a12 = 2 * (by - ay)
    a21 = 2 * (cx - ax)
    a22 = 2 * (cy - ay)
    r1 = sqnorm(b) - sqnorm(a)
    r2 = sqnorm(c) - sqnorm(a)
    det = a11 * a22 - a12 * a21
    if det == 0:
        return None
    ux = (r1 * a22 - a12 * r2) / det
    uy = (a11 * r2 - r1 * a21) / det
    center = (ux, uy)
    return center, euclidean_sqdist(center, a)


def empty_circle_certificate(
    sites: Sequence[Tuple[str, Point]], triple: Sequence[str]
) -> Tuple[Point, Fraction, Tuple[str, ...], Tuple[str, ...], Tuple[str, ...]] | None:
    points = dict(sites)
    circle = circumcircle(*(points[label] for label in triple))
    if circle is None:
        return None
    center, radius2 = circle
    inside, boundary, outside = [], [], []
    for label, point in sites:
        d2 = euclidean_sqdist(center, point)
        if d2 < radius2:
            inside.append(label)
        elif d2 == radius2:
            boundary.append(label)
        else:
            outside.append(label)
    return (
        center,
        radius2,
        tuple(sorted(inside)),
        tuple(sorted(boundary)),
        tuple(sorted(outside)),
    )


def delaunay_cells(
    sites: Sequence[Tuple[str, Point]],
) -> Dict[FrozenSet[str], Tuple[Point, Fraction]]:
    """
    Return maximal non-collinear empty-circle boundary site sets.

    A cocircular k-tuple is retained as one k-site cell.  No diagonal is
    selected merely to force a triangulation.
    """
    labels = [label for label, _ in sites]
    valid: Dict[FrozenSet[str], Tuple[Point, Fraction]] = {}
    for triple in combinations(labels, 3):
        cert = empty_circle_certificate(sites, triple)
        if cert is None:
            continue
        center, radius2, inside, boundary, _ = cert
        if not inside:
            valid[frozenset(boundary)] = (center, radius2)
    keys = list(valid)
    maximal = [key for key in keys if not any(key < other for other in keys)]
    return {key: valid[key] for key in maximal}


def dual_adjacent(
    sites: Sequence[Tuple[str, Point]], left: str, right: str
) -> bool:
    """
    Exact test that two Cartesian Euclidean Voronoi cells share a 1D face.

    On the perpendicular bisector, every other nearest-site inequality becomes
    an affine inequality in one rational parameter t.  A singleton feasible
    t-set is only a Voronoi vertex, not codimension-one adjacency.
    """
    points = dict(sites)
    a, b = points[left], points[right]
    midpoint = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    v = (b[0] - a[0], b[1] - a[1])
    perp = (-v[1], v[0])
    lo: Fraction | None = None
    hi: Fraction | None = None

    def x_of(t: Fraction) -> Point:
        return (midpoint[0] + t * perp[0], midpoint[1] + t * perp[1])

    for label, other in sites:
        if label in (left, right):
            continue
        f0 = euclidean_sqdist(x_of(F(0)), a) - euclidean_sqdist(x_of(F(0)), other)
        f1 = euclidean_sqdist(x_of(F(1)), a) - euclidean_sqdist(x_of(F(1)), other)
        slope = f1 - f0
        intercept = f0
        if slope == 0:
            if intercept > 0:
                return False
        elif slope > 0:
            bound = -intercept / slope
            hi = bound if hi is None or bound < hi else hi
        else:
            bound = -intercept / slope
            lo = bound if lo is None or bound > lo else lo
        if lo is not None and hi is not None and lo > hi:
            return False

    # Empty or singleton is not a codimension-one shared face.
    return not (lo is not None and hi is not None and lo == hi)


def dual_edges(sites: Sequence[Tuple[str, Point]]) -> FrozenSet[FrozenSet[str]]:
    labels = [label for label, _ in sites]
    return frozenset(
        frozenset((a, b))
        for a, b in combinations(labels, 2)
        if dual_adjacent(sites, a, b)
    )


def convex_hull_labels(
    boundary: Iterable[str], sites: Sequence[Tuple[str, Point]]
) -> Tuple[str, ...]:
    points = dict(sites)
    ordered = sorted((points[label][0], points[label][1], label) for label in boundary)
    if len(ordered) <= 1:
        return tuple(item[2] for item in ordered)

    def cross(o: Tuple[Fraction, Fraction, str],
              a: Tuple[Fraction, Fraction, str],
              b: Tuple[Fraction, Fraction, str]) -> Fraction:
        return (
            (a[0] - o[0]) * (b[1] - o[1])
            - (a[1] - o[1]) * (b[0] - o[0])
        )

    lower = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    hull = lower[:-1] + upper[:-1]
    return tuple(item[2] for item in hull)


def delaunay_cell_edges(
    sites: Sequence[Tuple[str, Point]],
    cells: Mapping[FrozenSet[str], Tuple[Point, Fraction]],
) -> FrozenSet[FrozenSet[str]]:
    edges = set()
    for boundary in cells:
        hull = convex_hull_labels(boundary, sites)
        if len(hull) == 2:
            edges.add(frozenset(hull))
        elif len(hull) >= 3:
            for i, label in enumerate(hull):
                edges.add(frozenset((label, hull[(i + 1) % len(hull)])))
    return frozenset(edges)


# Exact triangular-lattice carrier quadratic form.
TRIANGULAR_G = ((F(1), F(1, 2)), (F(1, 2), F(1)))


def qform(v: Point, g=TRIANGULAR_G) -> Fraction:
    x, y = v
    return (
        g[0][0] * x * x
        + (g[0][1] + g[1][0]) * x * y
        + g[1][1] * y * y
    )


def triangular_carrier_sqdist(a: Point, b: Point) -> Fraction:
    return qform((a[0] - b[0], a[1] - b[1]))


TRIANGULAR_CENTER_CARRIER = ExactDistanceSemantics(
    name="triangular_center_classical_euclidean_carrier_qform",
    layer="carrier",
    score=triangular_carrier_sqdist,
)


def row_times_g(v: Point, g=TRIANGULAR_G) -> Point:
    x, y = v
    return (
        x * g[0][0] + y * g[1][0],
        x * g[0][1] + y * g[1][1],
    )


def q_circumcircle(a: Point, b: Point, c: Point) -> Tuple[Point, Fraction] | None:
    d1 = (b[0] - a[0], b[1] - a[1])
    d2 = (c[0] - a[0], c[1] - a[1])
    r1 = qform(b) - qform(a)
    r2 = qform(c) - qform(a)
    row1 = row_times_g(d1)
    row2 = row_times_g(d2)
    a11, a12 = 2 * row1[0], 2 * row1[1]
    a21, a22 = 2 * row2[0], 2 * row2[1]
    det = a11 * a22 - a12 * a21
    if det == 0:
        return None
    ux = (r1 * a22 - a12 * r2) / det
    uy = (a11 * r2 - r1 * a21) / det
    center = (ux, uy)
    return center, triangular_carrier_sqdist(center, a)


def metric_table_is_valid(
    points: Sequence[str], table: Mapping[Tuple[str, str], Fraction]
) -> bool:
    def d(a: str, b: str) -> Fraction:
        if a == b:
            return F(0)
        return table[tuple(sorted((a, b)))]

    for a in points:
        if d(a, a) != 0:
            return False
    for a, b in combinations(points, 2):
        if d(a, b) <= 0 or d(a, b) != d(b, a):
            return False
    for a in points:
        for b in points:
            for c in points:
                if d(a, c) > d(a, b) + d(b, c):
                    return False
    return True


def table_semantics(
    name: str, table: Mapping[Tuple[str, str], Fraction]
) -> ExactDistanceSemantics:
    def score(a: str, b: str) -> Fraction:
        if a == b:
            return F(0)
        return table[tuple(sorted((a, b)))]

    return ExactDistanceSemantics(name=name, layer="independent_test_metric", score=score)


class Check:
    def __init__(self) -> None:
        self.mismatches = []
        self.passes = []

    def expect(self, name: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passes.append(name)
        else:
            self.mismatches.append((name, detail))

    def expect_raises(self, name: str, exc: type[BaseException], fn: Callable[[], Any]) -> None:
        try:
            fn()
        except exc:
            self.passes.append(name)
        except Exception as error:
            self.mismatches.append((name, f"wrong exception: {error!r}"))
        else:
            self.mismatches.append((name, "expected exception not raised"))


def run() -> int:
    check = Check()

    generic = [
        ("A", P(0, 0)),
        ("B", P(4, 0)),
        ("C", P(0, 3)),
        ("D", P(5, 4)),
    ]
    generic_cells = delaunay_cells(generic)
    check.expect(
        "generic_delaunay_cells",
        set(generic_cells)
        == {frozenset(("A", "B", "C")), frozenset(("B", "C", "D"))},
        repr(generic_cells),
    )
    check.expect(
        "generic_primal_dual_adjacency",
        dual_edges(generic) == delaunay_cell_edges(generic, generic_cells),
    )
    for cell in generic_cells:
        triple = tuple(sorted(cell))[:3]
        cert = empty_circle_certificate(generic, triple)
        check.expect(
            f"empty_circle_{''.join(sorted(cell))}",
            cert is not None and cert[2] == () and frozenset(cert[3]) == cell,
            repr(cert),
        )

    generic_map = dict(generic)
    check.expect(
        "nearest_site_tie_preserved",
        nearest_sites(P(2, 0), generic_map, EUCLIDEAN_CARRIER) == ("A", "B"),
    )

    square = [
        ("A", P(0, 0)),
        ("B", P(2, 0)),
        ("C", P(2, 2)),
        ("D", P(0, 2)),
    ]
    square_cells = delaunay_cells(square)
    check.expect(
        "cocircular_four_site_cell_retained",
        set(square_cells) == {frozenset(("A", "B", "C", "D"))},
        repr(square_cells),
    )
    check.expect(
        "cocircular_tie_stratum",
        nearest_sites(P(1, 1), dict(square), EUCLIDEAN_CARRIER)
        == ("A", "B", "C", "D"),
    )
    square_edges = dual_edges(square)
    expected_square_edges = frozenset(
        {
            frozenset(("A", "B")),
            frozenset(("B", "C")),
            frozenset(("C", "D")),
            frozenset(("D", "A")),
        }
    )
    check.expect("degenerate_no_fake_diagonal", square_edges == expected_square_edges)
    check.expect(
        "degenerate_primal_dual_adjacency",
        square_edges == delaunay_cell_edges(square, square_cells),
    )

    relabeled = [
        ("q7", P(0, 0)),
        ("q3", P(4, 0)),
        ("q9", P(0, 3)),
        ("q1", P(5, 4)),
    ]
    original_coord_cells = {
        frozenset(dict(generic)[label] for label in cell) for cell in generic_cells
    }
    relabeled_cells = delaunay_cells(relabeled)
    relabeled_coord_cells = {
        frozenset(dict(relabeled)[label] for label in cell) for cell in relabeled_cells
    }
    check.expect(
        "relabeling_invariance_cells",
        original_coord_cells == relabeled_coord_cells,
    )

    inserted = generic + [("P", P(2, 1))]
    before_edges = dual_edges(generic)
    after_edges = dual_edges(inserted)
    changed = before_edges ^ after_edges
    new_neighbors = {
        next(iter(edge - {"P"})) for edge in after_edges if "P" in edge
    }
    local_vertices = new_neighbors | {"P"}
    check.expect(
        "local_insert_delta_certificate",
        all(edge <= local_vertices for edge in changed),
        repr(changed),
    )
    check.expect(
        "local_delete_restores",
        dual_edges([item for item in inserted if item[0] != "P"]) == before_edges,
    )

    center_window = [
        ("O", P(0, 0)),
        ("E1", P(1, 0)),
        ("E2", P(0, 1)),
        ("E3", P(-1, 1)),
        ("W", P(-1, 0)),
        ("S", P(0, -1)),
        ("SE", P(1, -1)),
    ]
    center_map = dict(center_window)
    check.expect(
        "center_carrier_six_unit_neighbors",
        all(
            triangular_carrier_sqdist(P(0, 0), point) == 1
            for label, point in center_window
            if label != "O"
        ),
    )
    check.expect(
        "center_carrier_voronoi_edge_tie",
        nearest_sites(P(F(1, 2), 0), center_map, TRIANGULAR_CENTER_CARRIER)
        == ("E1", "O"),
    )
    check.expect(
        "center_carrier_voronoi_vertex_tie",
        nearest_sites(P(F(1, 3), F(1, 3)), center_map, TRIANGULAR_CENTER_CARRIER)
        == ("E1", "E2", "O"),
    )
    qcircle = q_circumcircle(P(0, 0), P(1, 0), P(0, 1))
    check.expect(
        "center_carrier_exact_empty_circumdisk",
        qcircle == (P(F(1, 3), F(1, 3)), F(1, 3))
        and all(
            triangular_carrier_sqdist(qcircle[0], point) >= qcircle[1]
            for _, point in center_window
        ),
        repr(qcircle),
    )

    check.expect_raises(
        "missing_distance_rejected",
        SemanticInputError,
        lambda: nearest_sites(P(0, 0), generic_map, None),
    )
    check.expect_raises(
        "carrier_not_promoted_to_native_metric",
        SemanticLayerError,
        lambda: nearest_sites(
            P(0, 0),
            center_map,
            TRIANGULAR_CENTER_CARRIER,
            required_layer="native",
        ),
    )

    # Same finite set, two exact legitimate metric tables, opposite nearest site.
    # Therefore site labels alone do not determine a nearest-site structure.
    metric_points = ("X", "S1", "S2")
    metric1 = {
        ("S1", "S2"): F(3),
        ("S1", "X"): F(1),
        ("S2", "X"): F(2),
    }
    metric2 = {
        ("S1", "S2"): F(3),
        ("S1", "X"): F(2),
        ("S2", "X"): F(1),
    }
    check.expect("missing_distance_metric1_valid", metric_table_is_valid(metric_points, metric1))
    check.expect("missing_distance_metric2_valid", metric_table_is_valid(metric_points, metric2))
    metric_sites = {"S1": "S1", "S2": "S2"}
    nearest1 = nearest_sites("X", metric_sites, table_semantics("M1", metric1))
    nearest2 = nearest_sites("X", metric_sites, table_semantics("M2", metric2))
    check.expect(
        "missing_distance_counterexample_changes_nearest",
        nearest1 == ("S1",) and nearest2 == ("S2",),
        f"M1={nearest1}, M2={nearest2}",
    )

    check.expect(
        "classification_obeys_two_domain_gate",
        TERMINAL_CLASSIFICATION == "CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY"
        and not GLOBAL_TOOL_CLAIM
        and not SECOND_INDEPENDENT_ENTERPRISE_DISTANCE_FAMILY,
    )

    print("tool_discovery_carrier_voronoi_delaunay_dual_cell_check")
    for name in sorted(check.passes):
        print(f"PASS {name}")
    for name, detail in check.mismatches:
        print(f"MISMATCH {name}: {detail}")
    print(f"classification={TERMINAL_CLASSIFICATION}")
    print(f"mismatch_count={len(check.mismatches)}")
    return 0 if not check.mismatches else 1


if __name__ == "__main__":
    raise SystemExit(run())
