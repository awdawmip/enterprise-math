"""Exact witness certificate for the classical high-quality P025 abc triple.

The fixed triple is

    2 + 3^10 * 109 = 23^5.

This module proves its relation-conditioned non-degenerate L-infinity witness
precision is exactly 601 by reducing the additive lattice to an explicit
unimodular basis and excluding every non-degenerate vector of radius <= 600.

The lattice reduction / restricted-minimum viewpoint is established prior art.
The value 601 and its exact finite certificate are a P025 instance result, not
an abc proof or a historical novelty claim about lattice algorithms.
"""

from __future__ import annotations

from math import gcd

from .abc_support import abc_support_state, radical
from .abc_witness_precision import (
    additive_relation_vector,
    witness_coordinates,
    wronskian_relation_vector,
)
from .witness_precision_bracket import abc_demand_floor, sparse_two_coordinate_upper_bound


CLASSIC_A = 2
CLASSIC_B = 3**10 * 109
CLASSIC_C = 23**5
CLASSIC_RADIUS = 601


def classic_triple() -> tuple[int, int, int]:
    """Return the fixed high-quality abc triple."""
    if CLASSIC_A + CLASSIC_B != CLASSIC_C:
        raise AssertionError("classic abc identity failed")
    abc_support_state(CLASSIC_A, CLASSIC_B, CLASSIC_C)
    return CLASSIC_A, CLASSIC_B, CLASSIC_C


def classic_high_quality_profile() -> dict[str, int | bool]:
    """Return exact rational-quality data for exponent 3/2."""
    a, b, c = classic_triple()
    rad_abc = radical(a * b * c)
    return {
        "radical": rad_abc,
        "c_squared": c**2,
        "radical_cubed": rad_abc**3,
        "high_quality_3_over_2": c**2 > rad_abc**3,
    }


def _primitive_row(row: tuple[int, ...]) -> tuple[int, ...]:
    content = 0
    for value in row:
        content = gcd(content, abs(value))
    if content == 0:
        raise ValueError("row must be nonzero")
    normalized = tuple(value // content for value in row)
    for value in normalized:
        if value == 0:
            continue
        if value < 0:
            normalized = tuple(-entry for entry in normalized)
        break
    return normalized


def classic_generator_rows() -> dict[str, object]:
    """Return the exact prime coordinates and primitive generator rows."""
    a, b, c = classic_triple()
    coordinates = witness_coordinates(a, b, c)
    alpha = additive_relation_vector(a, b, c)
    beta = wronskian_relation_vector(a, b, c)
    expected_coordinates = (2, 3, 23, 109)
    expected_alpha = (1, 21_454_470, -1_399_205, 59_049)
    expected_beta = (-327, 2_180, 0, 6)
    if coordinates != expected_coordinates:
        raise AssertionError("unexpected prime-coordinate ordering")
    if alpha != expected_alpha:
        raise AssertionError("unexpected primitive additive row")
    if beta != expected_beta:
        raise AssertionError("unexpected primitive degeneracy row")
    return {"coordinates": coordinates, "alpha": alpha, "beta": beta}


def classic_canonical_kernel_basis() -> tuple[tuple[int, ...], ...]:
    """Return the obvious Z-basis of ker(alpha) using alpha_0=1."""
    alpha = tuple(classic_generator_rows()["alpha"])
    if alpha[0] != 1:
        raise AssertionError("classic additive row no longer has unit first coordinate")
    basis = (
        (-alpha[1], 1, 0, 0),
        (-alpha[2], 0, 1, 0),
        (-alpha[3], 0, 0, 1),
    )
    for vector in basis:
        if sum(a * x for a, x in zip(alpha, vector, strict=True)) != 0:
            raise AssertionError("canonical kernel basis left ker(alpha)")
    return basis


def _det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def classic_reduced_kernel_basis() -> dict[str, object]:
    """Return a small exact unimodular basis of the additive witness lattice."""
    canonical = classic_canonical_kernel_basis()
    transform = (
        (3, 46, 0),
        (0, 23, 545),
        (-20, -310, -79),
    )
    determinant = _det3(transform)
    if determinant != -1:
        raise AssertionError("reduction matrix must be unimodular")

    reduced: list[tuple[int, ...]] = []
    for row in transform:
        vector = tuple(
            sum(row[j] * canonical[j][i] for j in range(3)) for i in range(4)
        )
        reduced.append(vector)
    reduced_basis = tuple(reduced)
    expected = (
        (20, 3, 46, 0),
        (10, 0, 23, 545),
        (721, -20, -310, -79),
    )
    if reduced_basis != expected:
        raise AssertionError("unexpected reduced kernel basis")

    beta = tuple(classic_generator_rows()["beta"])
    beta_values = tuple(
        sum(beta[i] * vector[i] for i in range(4)) for vector in reduced_basis
    )
    if beta_values != (0, 0, -279_841):
        raise AssertionError("unexpected degeneracy values on reduced basis")

    return {
        "canonical_basis": canonical,
        "transform": transform,
        "transform_determinant": determinant,
        "basis": reduced_basis,
        "beta_values": beta_values,
    }


def classic_basis_vector(A: int, B: int, C: int) -> tuple[int, int, int, int]:
    """Return A*v1+B*v2+C*v3 in the reduced basis."""
    for name, value in (("A", A), ("B", B), ("C", C)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    basis = tuple(classic_reduced_kernel_basis()["basis"])
    return tuple(A * basis[0][i] + B * basis[1][i] + C * basis[2][i] for i in range(4))


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def classic_radius_600_obstruction_table() -> tuple[dict[str, int], ...]:
    """Return the ten exact interval contradictions excluding radius <= 600.

    If a non-degenerate witness x=A*v1+B*v2+C*v3 had norm <=600, the primitive
    beta row first gives |C|<=5.  Sign symmetry lets us take C>0.  The fourth
    coordinate then forces B in {0,1}.  For each remaining pair (C,B), the
    first coordinate forces an upper bound on A and the third coordinate forces
    a strictly larger lower bound.
    """
    rows: list[dict[str, int]] = []
    radius = 600
    for C in range(1, 6):
        for B in (0, 1):
            # x_2 = 20A + 10B + 721C.
            upper_A = (radius - 10 * B - 721 * C) // 20
            # x_23 = 46A + 23B - 310C.
            lower_A = _ceil_div(-radius - 23 * B + 310 * C, 46)
            if lower_A <= upper_A:
                raise AssertionError("radius-600 interval obstruction unexpectedly feasible")
            rows.append(
                {
                    "C": C,
                    "B": B,
                    "A_lower_from_p23": lower_A,
                    "A_upper_from_p2": upper_A,
                    "gap": lower_A - upper_A,
                }
            )
    expected = (
        (1, 0, -6, -7),
        (1, 1, -6, -7),
        (2, 0, 1, -43),
        (2, 1, 0, -43),
        (3, 0, 8, -79),
        (3, 1, 7, -79),
        (4, 0, 14, -115),
        (4, 1, 14, -115),
        (5, 0, 21, -151),
        (5, 1, 21, -151),
    )
    actual = tuple(
        (row["C"], row["B"], row["A_lower_from_p23"], row["A_upper_from_p2"])
        for row in rows
    )
    if actual != expected:
        raise AssertionError("unexpected obstruction table")
    return tuple(rows)


def classic_exact_witness_precision() -> dict[str, object]:
    """Return a fully checkable exact certificate that the witness precision is 601."""
    rows = classic_generator_rows()
    reduced = classic_reduced_kernel_basis()
    beta = tuple(rows["beta"])
    beta_l1 = sum(abs(value) for value in beta)
    if beta_l1 != 2_513:
        raise AssertionError("unexpected beta L1 norm")

    # If ||x||_infinity <= 600, then |beta*x| <= 2513*600.  In the reduced
    # basis beta*x=-279841*C, hence |C|<=5 because 6*279841 is already larger.
    bound_product = beta_l1 * 600
    if not (5 * 279_841 <= bound_product < 6 * 279_841):
        raise AssertionError("C-bound arithmetic failed")

    # For C in 1..5 (after sign symmetry), |545B-79C|<=600 gives B in {0,1}:
    # the lower endpoint is always > -1 and upper endpoint always < 2.
    if not ((-600 + 79) > -545 and (600 + 79 * 5) < 2 * 545):
        raise AssertionError("uniform B-bound arithmetic failed")

    obstruction = classic_radius_600_obstruction_table()

    # Explicit non-degenerate witness at radius 601.
    coefficients = (6, 0, -1)
    witness = classic_basis_vector(*coefficients)
    if witness != (-601, 38, 586, 79):
        raise AssertionError("unexpected radius-601 witness")
    witness_radius = max(abs(value) for value in witness)
    if witness_radius != CLASSIC_RADIUS:
        raise AssertionError("explicit witness has wrong radius")
    alpha = tuple(rows["alpha"])
    if sum(alpha[i] * witness[i] for i in range(4)) != 0:
        raise AssertionError("explicit witness is not relation-adapted")
    beta_value = sum(beta[i] * witness[i] for i in range(4))
    if beta_value != 279_841:
        raise AssertionError("explicit witness is degenerate or has unexpected beta value")

    demand = abc_demand_floor(*classic_triple())
    sparse = sparse_two_coordinate_upper_bound(*classic_triple())
    if demand["lambda_abc"] != 597:
        raise AssertionError("unexpected arithmetic demand floor")
    if sparse["U2"] != 59_049:
        raise AssertionError("unexpected two-coordinate upper certificate")

    # The first reduced basis vector is a nonzero additive witness of radius 46,
    # so rho<=46<lambda.  Therefore max(lambda,rho)=lambda without solving rho.
    additive_witness = tuple(reduced["basis"])[0]
    additive_radius = max(abs(value) for value in additive_witness)
    if additive_radius != 46 or additive_radius >= 597:
        raise AssertionError("unexpected additive-radius certificate")

    return {
        "triple": classic_triple(),
        "coordinates": rows["coordinates"],
        "alpha": rows["alpha"],
        "beta": rows["beta"],
        "reduced_basis": reduced["basis"],
        "transform_determinant": reduced["transform_determinant"],
        "beta_values": reduced["beta_values"],
        "beta_l1": beta_l1,
        "radius_600_C_bound": 5,
        "radius_600_obstruction_table": obstruction,
        "explicit_coefficients": coefficients,
        "explicit_witness": witness,
        "mu": CLASSIC_RADIUS,
        "lambda_abc": int(demand["lambda_abc"]),
        "additive_radius_upper_certificate": additive_radius,
        "combined_floor": 597,
        "nondegeneracy_overhead_over_certified_floor": CLASSIC_RADIUS - 597,
        "U2": int(sparse["U2"]),
        "high_quality": classic_high_quality_profile(),
    }
