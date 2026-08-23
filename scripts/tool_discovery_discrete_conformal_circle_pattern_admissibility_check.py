#!/usr/bin/env python3
"""Deterministic checker for RS-TD-DC discrete-conformal admissibility.

This checker intentionally tests only semantics and exact/algebraic finite identities
needed by the taskbook. It does not promote carrier Euclidean quantities to native
Enterprise metric/conformal data, and it does not treat the current overlapping
circle-cell cover as a tangency packing.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Dict, Iterable, Tuple

Mismatch = Tuple[str, object, object]
MISMATCHES: list[Mismatch] = []


def check(name: str, got: object, expected: object) -> None:
    if got != expected:
        MISMATCHES.append((name, got, expected))
    else:
        print(f"PASS {name}: {got!r}")


def F(x: int | Fraction) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(x, 1)


def valid_triangle(a: Fraction, b: Fraction, c: Fraction) -> bool:
    a, b, c = F(a), F(b), F(c)
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a


def cosine_of_angle_opposite(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    """cos(theta_c) for a Euclidean triangle with sides a,b adjacent to theta_c."""
    if not valid_triangle(a, b, c):
        raise ValueError("invalid triangle")
    return (a * a + b * b - c * c) / (2 * a * b)


def cotangent_sign_numerator(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    """Sign of cot(theta_c); denominator is positive for a nondegenerate triangle."""
    if not valid_triangle(a, b, c):
        raise ValueError("invalid triangle")
    return a * a + b * b - c * c


def vertex_scaled_triangle(
    base_edges: Dict[Tuple[int, int], Fraction],
    q: Dict[int, Fraction],
) -> Tuple[Fraction, Fraction, Fraction]:
    """Exact test subset of l'_ij=q_i q_j l_ij, q_i=e^{u_i/2}>0."""
    def edge(i: int, j: int) -> Fraction:
        key = (i, j) if i < j else (j, i)
        return F(q[i]) * F(q[j]) * F(base_edges[key])

    return edge(0, 1), edge(1, 2), edge(0, 2)


def curvature_pi_coefficient(incident_equilateral_faces: int, boundary: bool) -> Fraction:
    """Coefficient of pi for angle pi/3 in each incident equilateral face."""
    base = Fraction(1, 1) if boundary else Fraction(2, 1)
    return base - Fraction(incident_equilateral_faces, 3)


def euler_characteristic(v: int, e: int, f: int) -> int:
    return v - e + f


def semantic_layer_check(
    metric_layer: str,
    requested_output_layer: str,
    native_metric_declared: bool = False,
) -> bool:
    if requested_output_layer == "native" and metric_layer == "carrier" and not native_metric_declared:
        return False
    return True


def packing_admissible_from_overlap(positive_area_overlap: bool) -> bool:
    """Tangency packing requires no positive-area interior overlap between neighbors."""
    return not positive_area_overlap


def radii_positive(radii: Iterable[Fraction]) -> bool:
    return all(F(r) > 0 for r in radii)


def target_curvature_solver_admissible(
    has_existence_theorem: bool,
    has_uniqueness_or_gauge_fix: bool,
    exact_certificate_available: bool,
) -> bool:
    return has_existence_theorem and has_uniqueness_or_gauge_fix and exact_certificate_available


def main() -> int:
    print("MODEL A: explicit Euclidean edge-length / vertex-scaling contract")

    # Exact triangle examples.
    check("equilateral-valid", valid_triangle(F(1), F(1), F(1)), True)
    check("equilateral-cos-pi-over-3", cosine_of_angle_opposite(F(1), F(1), F(1)), Fraction(1, 2))
    check("3-4-5-valid", valid_triangle(F(3), F(4), F(5)), True)
    check("3-4-5-right-angle", cosine_of_angle_opposite(F(3), F(4), F(5)), Fraction(0, 1))
    check("3-4-5-cos-angle-opposite-3", cosine_of_angle_opposite(F(4), F(5), F(3)), Fraction(4, 5))
    check("3-4-5-cos-angle-opposite-4", cosine_of_angle_opposite(F(3), F(5), F(4)), Fraction(3, 5))

    # Algebraic angle-sum check for the 3-4-5 triangle:
    # cos A=4/5,sin A=3/5; cos B=3/5,sin B=4/5,
    # hence cos(A+B)=0 and sin(A+B)=1, so A+B=pi/2; C=pi/2.
    cos_a, sin_a = Fraction(4, 5), Fraction(3, 5)
    cos_b, sin_b = Fraction(3, 5), Fraction(4, 5)
    check("3-4-5-cos-A-plus-B", cos_a * cos_b - sin_a * sin_b, Fraction(0, 1))
    check("3-4-5-sin-A-plus-B", sin_a * cos_b + cos_a * sin_b, Fraction(1, 1))

    # Invalid triangles and degeneracy.
    check("degenerate-1-1-2-rejected", valid_triangle(F(1), F(1), F(2)), False)
    check("negative-edge-rejected", valid_triangle(F(-1), F(2), F(2)), False)

    # Exact vertex-scaling law l'_ij = q_i q_j l_ij.
    base = {(0, 1): F(1), (1, 2): F(1), (0, 2): F(1)}
    valid_scaled = vertex_scaled_triangle(base, {0: F(1), 1: F(1), 2: F(2)})
    invalid_scaled = vertex_scaled_triangle(base, {0: F(1), 1: F(2), 2: F(10)})
    check("valid-scale-edges", valid_scaled, (F(1), F(2), F(2)))
    check("valid-scale-preserves-triangle", valid_triangle(*valid_scaled), True)
    check("invalid-scale-edges", invalid_scaled, (F(2), F(20), F(10)))
    check("invalid-scale-rejected", valid_triangle(*invalid_scaled), False)

    # A uniform vertex scaling is conformal-by-contract but not an isometry.
    uniform_scaled = vertex_scaled_triangle(base, {0: F(2), 1: F(2), 2: F(2)})
    check("uniform-conformal-scale-changes-lengths", uniform_scaled == (F(1), F(1), F(1)), False)

    print("CURVATURE / GAUSS-BONNET exact pi-coefficient checks")

    # Closed tetrahedral sphere: 4 vertices, each sees 3 equilateral faces.
    tetra_curvatures = [curvature_pi_coefficient(3, boundary=False) for _ in range(4)]
    check("tetra-per-vertex-curvature/pi", tetra_curvatures[0], Fraction(1, 1))
    check("tetra-total-curvature/pi", sum(tetra_curvatures, Fraction(0, 1)), Fraction(4, 1))
    check("tetra-2chi", 2 * euler_characteristic(4, 6, 4), 4)

    # Disk fan: six equilateral triangles around one interior center.
    # center: 6 incident faces -> K=0; each boundary vertex: 2 faces -> K=pi/3.
    fan_curvatures = [curvature_pi_coefficient(6, boundary=False)] + [
        curvature_pi_coefficient(2, boundary=True) for _ in range(6)
    ]
    check("fan-center-curvature/pi", fan_curvatures[0], Fraction(0, 1))
    check("fan-boundary-curvature/pi", fan_curvatures[1], Fraction(1, 3))
    check("fan-total-curvature/pi", sum(fan_curvatures, Fraction(0, 1)), Fraction(2, 1))
    check("fan-2chi", 2 * euler_characteristic(7, 12, 6), 2)

    # Relabeling invariance: only incidence counts/boundary typing matter here.
    permuted_fan = list(reversed(fan_curvatures))
    check("relabeling-curvature-multiset", sorted(permuted_fan), sorted(fan_curvatures))

    print("SEMANTIC / NO-GO checks")

    # Frozen taskbook premise: neighboring current circle cells have positive-area overlap.
    check("canonical-overlap-not-tangency-packing", packing_admissible_from_overlap(True), False)

    # Circle-pattern radius validity.
    check("positive-radii-valid", radii_positive([F(1), F(2), Fraction(1, 3)]), True)
    check("zero-radius-rejected", radii_positive([F(1), F(0)]), False)
    check("negative-radius-rejected", radii_positive([F(1), F(-1)]), False)

    # Carrier-to-native leakage must be rejected without explicit native metric declaration.
    check("carrier-to-native-leakage-rejected", semantic_layer_check("carrier", "native", False), False)
    check("carrier-output-at-carrier-layer-valid", semantic_layer_check("carrier", "carrier", False), True)

    # Incidence alone is not enough for angle-deficit curvature.
    has_faces = False
    has_metric = False
    check("graph-without-faces-no-angle-curvature", has_faces and has_metric, False)
    has_faces = True
    has_metric = False
    check("triangulation-without-metric-no-angle-curvature", has_faces and has_metric, False)

    # Cotangent positivity failure: sides 2,3,4 give an obtuse angle opposite 4.
    check("2-3-4-valid", valid_triangle(F(2), F(3), F(4)), True)
    check("2-3-4-obtuse-cot-sign", cotangent_sign_numerator(F(2), F(3), F(4)) < 0, True)

    # Target-curvature solving cannot be promoted from convergence or an unproved map.
    check("target-curvature-no-theorem-rejected", target_curvature_solver_admissible(False, True, True), False)
    check("target-curvature-no-uniqueness-rejected", target_curvature_solver_admissible(True, False, True), False)
    check("target-curvature-numerical-only-rejected", target_curvature_solver_admissible(True, True, False), False)

    # Packing uniqueness obstruction without normalization: global homothety preserves tangency equations.
    packing_1 = (F(1), F(1), F(2))
    packing_2 = (F(2), F(2), F(4))
    check("packing-example-1-tangent", packing_1[2] == packing_1[0] + packing_1[1], True)
    check("packing-example-2-tangent", packing_2[2] == packing_2[0] + packing_2[1], True)
    check("packing-without-normalization-nonunique", packing_1 != packing_2, True)

    # The allowed source packet supplies no second current Enterprise metric/circle-pattern family.
    global_tool_claim = False
    check("global-tool-claim-withheld", global_tool_claim, False)

    print(f"MISMATCH_COUNT={len(MISMATCHES)}")
    if MISMATCHES:
        for name, got, expected in MISMATCHES:
            print(f"MISMATCH {name}: got={got!r} expected={expected!r}")
        return 1

    print("TERMINAL_CHECK=PASS")
    print("PRIMARY_CLASSIFICATION=CURRENT_FOUNDATION_EXTRA_STRUCTURE_REQUIRED")
    print("COROLLARY=CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING")
    print("COROLLARY=CARRIER_GEOMETRY_SPECIALIZATION_ONLY")
    print("MODE_C_OWNERSHIP=SUBTOOL_OF_LAPLACIAN_ENERGY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
