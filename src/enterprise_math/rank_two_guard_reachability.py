"""Exact rank-two guard-lattice threshold reachability for A3.

A rank-two hidden guard-image lattice L in Z^r is reduced to an exact integer
basis h1,h2. A threshold pattern on an affine coset g+L then becomes a finite
system of integer halfplanes in parameters (s,t):

    g + s*h1 + t*h2.

The 2D solver is exact. It classifies the recession cone and returns a witness
via one of three certificates:
- a strict integer recession direction;
- a one-dimensional recession ray/line plus a 1D integer quotient;
- bounded polygon enumeration over the smaller exact integer coordinate span.

No floating point or rational arithmetic is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd

from .guard_image_lattice import IntMatrix, integer_matrix_rank


Vector = tuple[int, ...]
Halfplane = tuple[int, int, int]


@dataclass(frozen=True)
class RankTwoPatternWitness:
    basis: tuple[Vector, Vector]
    parameters: tuple[int, int]
    scores: Vector
    certificate_mode: str
    bounded_scan_width: int | None = None


def _extended_gcd(left: int, right: int) -> tuple[int, int, int]:
    """Return g>=0 and x,y with x*left+y*right=g."""
    old_r, r = abs(left), abs(right)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if old_r == 0:
        return 0, 0, 0
    return (
        old_r,
        old_s if left >= 0 else -old_s,
        old_t if right >= 0 else -old_t,
    )


def _bezout_gcd(values: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Return gcd(values) and coefficients realizing it."""
    divisor = 0
    coefficients: tuple[int, ...] = ()
    for value in values:
        next_divisor, left, right = _extended_gcd(divisor, value)
        coefficients = tuple(left * coefficient for coefficient in coefficients) + (right,)
        divisor = next_divisor
    return divisor, coefficients


def _linear_combination(coefficients: tuple[int, ...], vectors: IntMatrix) -> Vector:
    return tuple(
        sum(coefficient * vector[index] for coefficient, vector in zip(coefficients, vectors))
        for index in range(len(vectors[0]))
    )


def _require_rank_two_generators(generators: IntMatrix) -> int:
    if not isinstance(generators, tuple) or not generators:
        raise ValueError("generators must be a non-empty tuple")
    width = len(generators[0])
    if width == 0:
        raise ValueError("generator coordinate dimension must be positive")
    if any(not isinstance(row, tuple) or len(row) != width for row in generators):
        raise ValueError("generators must have a common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in generators
        for value in row
    ):
        raise ValueError("generator entries must be integers")
    if integer_matrix_rank(generators, width) != 2:
        raise ValueError("generators must span rank two")
    return width


def _projection_pair(generators: IntMatrix) -> tuple[int, int]:
    width = len(generators[0])
    for left in range(width):
        for right in range(left + 1, width):
            for first, second in combinations(generators, 2):
                if first[left] * second[right] - second[left] * first[right] != 0:
                    return left, right
    raise AssertionError("rank-two lattice must have a rank-two coordinate projection")


def rank_two_lattice_basis(generators: IntMatrix) -> tuple[Vector, Vector]:
    """Return an exact deterministic Z-basis of the generated rank-two lattice.

    The lexicographically first rank-two coordinate projection is used. Its
    projected lattice is put in row-Hermite form `(a,b),(0,c)` with `a,c>0`
    and `0<=b<c`; injectivity of that projection on the rational rank-two span
    lifts the projected basis uniquely to the full lattice.
    """
    _require_rank_two_generators(generators)
    first_coordinate, second_coordinate = _projection_pair(generators)

    first_values = tuple(row[first_coordinate] for row in generators)
    first_divisor, first_coefficients = _bezout_gcd(first_values)
    if first_divisor <= 0:
        raise AssertionError("rank-two projection must have nonzero first gcd")
    first_raw = _linear_combination(first_coefficients, generators)
    if first_raw[first_coordinate] != first_divisor:
        raise AssertionError("Bezout first basis reconstruction failed")

    residuals = []
    residual_second_values = []
    for generator in generators:
        first_value = generator[first_coordinate]
        if first_value % first_divisor != 0:
            raise AssertionError("first divisor must divide every projected first coordinate")
        multiplier = first_value // first_divisor
        residual = tuple(
            generator[index] - multiplier * first_raw[index]
            for index in range(len(generator))
        )
        if residual[first_coordinate] != 0:
            raise AssertionError("residual first coordinate must vanish")
        residuals.append(residual)
        residual_second_values.append(residual[second_coordinate])

    second_divisor, second_coefficients = _bezout_gcd(tuple(residual_second_values))
    if second_divisor <= 0:
        raise AssertionError("rank-two projection must have nonzero residual gcd")
    second_basis = _linear_combination(second_coefficients, tuple(residuals))
    if (
        second_basis[first_coordinate] != 0
        or second_basis[second_coordinate] != second_divisor
    ):
        raise AssertionError("Bezout second basis reconstruction failed")

    quotient = first_raw[second_coordinate] // second_divisor
    first_basis = tuple(
        first_raw[index] - quotient * second_basis[index]
        for index in range(len(first_raw))
    )
    projected_second = first_basis[second_coordinate]
    if not (
        first_basis[first_coordinate] == first_divisor
        and 0 <= projected_second < second_divisor
    ):
        raise AssertionError("projected basis must be in row-Hermite form")
    return first_basis, second_basis


def rank_two_basis_coordinates(
    vector: Vector, basis: tuple[Vector, Vector]
) -> tuple[int, int] | None:
    """Return integer coordinates of vector in the supplied rank-two basis."""
    if not isinstance(vector, tuple) or not vector:
        raise ValueError("vector must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError("vector entries must be integers")
    if (
        not isinstance(basis, tuple)
        or len(basis) != 2
        or any(not isinstance(row, tuple) or len(row) != len(vector) for row in basis)
    ):
        raise ValueError("basis must contain two vectors matching vector dimension")
    if integer_matrix_rank(basis, len(vector)) != 2:
        raise ValueError("basis vectors must be rank two")

    first, second = basis
    pair = None
    for left in range(len(vector)):
        for right in range(left + 1, len(vector)):
            determinant = first[left] * second[right] - second[left] * first[right]
            if determinant != 0:
                pair = (left, right, determinant)
                break
        if pair is not None:
            break
    if pair is None:
        raise AssertionError("rank-two basis must have a nonzero coordinate minor")

    left, right, determinant = pair
    first_numerator = vector[left] * second[right] - second[left] * vector[right]
    second_numerator = first[left] * vector[right] - vector[left] * first[right]
    if first_numerator % determinant != 0 or second_numerator % determinant != 0:
        return None
    first_coordinate = first_numerator // determinant
    second_coordinate = second_numerator // determinant
    reconstructed = tuple(
        first_coordinate * first[index] + second_coordinate * second[index]
        for index in range(len(vector))
    )
    if reconstructed != vector:
        return None
    return first_coordinate, second_coordinate


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def _primitive_direction(vector: tuple[int, int]) -> tuple[int, int]:
    divisor = gcd(abs(vector[0]), abs(vector[1]))
    if divisor == 0:
        return (0, 0)
    return vector[0] // divisor, vector[1] // divisor


def _dot(normal: tuple[int, int], vector: tuple[int, int]) -> int:
    return normal[0] * vector[0] + normal[1] * vector[1]


def _recession_boundary_rays(
    constraints: tuple[Halfplane, ...],
) -> tuple[tuple[int, int], ...]:
    normals = tuple((left, right) for left, right, _ in constraints if left or right)
    rays = set()
    for normal in normals:
        left, right = normal
        for candidate in ((right, -left), (-right, left)):
            direction = _primitive_direction(candidate)
            if direction != (0, 0) and all(
                _dot(other, direction) >= 0 for other in normals
            ):
                rays.add(direction)
    return tuple(sorted(rays))


def _strict_recession_direction(
    constraints: tuple[Halfplane, ...],
) -> tuple[int, int] | None:
    normals = tuple((left, right) for left, right, _ in constraints if left or right)
    if not normals:
        return None
    rays = _recession_boundary_rays(constraints)
    candidates = set()
    for normal in normals:
        candidates.add(_primitive_direction(normal))
        candidates.add(_primitive_direction((-normal[0], -normal[1])))
    for first, second in combinations(rays, 2):
        candidate = _primitive_direction(
            (first[0] + second[0], first[1] + second[1])
        )
        if candidate != (0, 0):
            candidates.add(candidate)
    normal_sum = (
        sum(normal[0] for normal in normals),
        sum(normal[1] for normal in normals),
    )
    if normal_sum != (0, 0):
        candidates.add(_primitive_direction(normal_sum))

    for direction in candidates:
        if direction != (0, 0) and all(
            _dot(normal, direction) > 0 for normal in normals
        ):
            return direction
    return None


def _solve_integer_line_inequalities(
    constraints: tuple[tuple[int, int], ...],
) -> tuple[int, int | None, int | None] | None:
    """Solve alpha*q >= bound over q in Z."""
    lower: int | None = None
    upper: int | None = None
    for coefficient, bound in constraints:
        if coefficient > 0:
            candidate = _ceil_div(bound, coefficient)
            lower = candidate if lower is None else max(lower, candidate)
        elif coefficient < 0:
            candidate = (-bound) // (-coefficient)
            upper = candidate if upper is None else min(upper, candidate)
        elif bound > 0:
            return None
    if lower is not None and upper is not None and lower > upper:
        return None
    value = lower if lower is not None else (upper if upper is not None else 0)
    if upper is not None and value > upper:
        value = upper
    return value, lower, upper


def _fraction_less(left: tuple[int, int], right: tuple[int, int]) -> bool:
    return left[0] * right[1] < right[0] * left[1]


def _fraction_min(values: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    result = values[0]
    for value in values[1:]:
        if _fraction_less(value, result):
            result = value
    return result


def _fraction_max(values: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    result = values[0]
    for value in values[1:]:
        if _fraction_less(result, value):
            result = value
    return result


def _solve_other_coordinate(
    constraints: tuple[Halfplane, ...],
    fixed_coordinate: int,
    fixed_value: int,
) -> tuple[int, int] | None:
    line_constraints = []
    if fixed_coordinate == 0:
        for left, right, bound in constraints:
            line_constraints.append((right, bound - left * fixed_value))
    else:
        for left, right, bound in constraints:
            line_constraints.append((left, bound - right * fixed_value))
    solved = _solve_integer_line_inequalities(tuple(line_constraints))
    if solved is None:
        return None
    other = solved[0]
    return (fixed_value, other) if fixed_coordinate == 0 else (other, fixed_value)


def _solve_integer_halfplanes_2d(
    constraints: tuple[Halfplane, ...],
) -> tuple[tuple[int, int], str, int | None] | None:
    """Return integer witness, exact certificate mode, and bounded scan width."""
    clean = []
    for left, right, bound in constraints:
        if left == 0 and right == 0:
            if bound > 0:
                return None
        else:
            clean.append((left, right, bound))
    clean_constraints = tuple(clean)
    if not clean_constraints:
        return (0, 0), "trivial", None

    strict_direction = _strict_recession_direction(clean_constraints)
    if strict_direction is not None:
        multiplier = 0
        for left, right, bound in clean_constraints:
            growth = left * strict_direction[0] + right * strict_direction[1]
            if growth <= 0:
                raise AssertionError("strict recession direction must grow every constraint")
            multiplier = max(multiplier, _ceil_div(bound, growth))
        multiplier = max(multiplier, 0)
        witness = (
            multiplier * strict_direction[0],
            multiplier * strict_direction[1],
        )
        return witness, "strict_recession", None

    rays = _recession_boundary_rays(clean_constraints)
    if rays:
        direction = rays[0]
        normal = (-direction[1], direction[0])
        divisor, first, second = _extended_gcd(normal[0], normal[1])
        if divisor != 1:
            raise AssertionError("perpendicular to primitive direction must be primitive")
        section = (first, second)

        quotient_constraints = []
        for left, right, bound in clean_constraints:
            growth = left * direction[0] + right * direction[1]
            if growth < 0:
                raise AssertionError("chosen recession ray must be feasible")
            if growth == 0:
                quotient_constraints.append(
                    (left * section[0] + right * section[1], bound)
                )
        quotient = _solve_integer_line_inequalities(tuple(quotient_constraints))
        if quotient is None:
            return None
        quotient_value = quotient[0]
        base = (
            quotient_value * section[0],
            quotient_value * section[1],
        )
        parameter = 0
        for left, right, bound in clean_constraints:
            growth = left * direction[0] + right * direction[1]
            residual = bound - left * base[0] - right * base[1]
            if growth == 0:
                if residual > 0:
                    raise AssertionError("quotient constraints must handle zero-growth faces")
            else:
                parameter = max(parameter, _ceil_div(residual, growth))
        witness = (
            base[0] + parameter * direction[0],
            base[1] + parameter * direction[1],
        )
        return witness, "recession_ray_or_line", None

    vertices = []
    for first_index, second_index in combinations(range(len(clean_constraints)), 2):
        left, right, bound = clean_constraints[first_index]
        other_left, other_right, other_bound = clean_constraints[second_index]
        determinant = left * other_right - other_left * right
        if determinant == 0:
            continue
        first_numerator = bound * other_right - other_bound * right
        second_numerator = left * other_bound - other_left * bound
        if determinant < 0:
            determinant = -determinant
            first_numerator = -first_numerator
            second_numerator = -second_numerator
        if all(
            check_left * first_numerator + check_right * second_numerator
            >= check_bound * determinant
            for check_left, check_right, check_bound in clean_constraints
        ):
            vertices.append((first_numerator, second_numerator, determinant))

    if not vertices:
        return None

    first_values = tuple((first, divisor) for first, _, divisor in vertices)
    second_values = tuple((second, divisor) for _, second, divisor in vertices)
    first_min = _fraction_min(first_values)
    first_max = _fraction_max(first_values)
    second_min = _fraction_min(second_values)
    second_max = _fraction_max(second_values)
    first_lower = _ceil_div(first_min[0], first_min[1])
    first_upper = first_max[0] // first_max[1]
    second_lower = _ceil_div(second_min[0], second_min[1])
    second_upper = second_max[0] // second_max[1]
    if first_lower > first_upper or second_lower > second_upper:
        return None

    first_width = first_upper - first_lower + 1
    second_width = second_upper - second_lower + 1
    if first_width <= second_width:
        for first_value in range(first_lower, first_upper + 1):
            witness = _solve_other_coordinate(clean_constraints, 0, first_value)
            if witness is not None:
                return witness, "bounded_scan", first_width
    else:
        for second_value in range(second_lower, second_upper + 1):
            witness = _solve_other_coordinate(clean_constraints, 1, second_value)
            if witness is not None:
                return witness, "bounded_scan", second_width
    return None


def rank_two_threshold_pattern_witness(
    base_scores: Vector,
    generators: IntMatrix,
    true_flags: tuple[bool, ...],
) -> RankTwoPatternWitness | None:
    """Return an exact fine-score witness for a threshold pattern on g+L."""
    if not isinstance(base_scores, tuple) or not base_scores:
        raise ValueError("base_scores must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in base_scores
    ):
        raise ValueError("base_scores entries must be integers")
    if len(true_flags) != len(base_scores) or any(
        not isinstance(flag, bool) for flag in true_flags
    ):
        raise ValueError("true_flags must be booleans matching base_scores")
    _require_rank_two_generators(generators)
    if len(generators[0]) != len(base_scores):
        raise ValueError("generator dimension must match guard-score dimension")

    first_basis, second_basis = rank_two_lattice_basis(generators)
    constraints = []
    for base, first_step, second_step, wants_true in zip(
        base_scores, first_basis, second_basis, true_flags
    ):
        if wants_true:
            constraints.append((first_step, second_step, -base))
        else:
            constraints.append((-first_step, -second_step, base + 1))
    solved = _solve_integer_halfplanes_2d(tuple(constraints))
    if solved is None:
        return None
    parameters, mode, scan_width = solved
    first_parameter, second_parameter = parameters
    scores = tuple(
        base_scores[index]
        + first_parameter * first_basis[index]
        + second_parameter * second_basis[index]
        for index in range(len(base_scores))
    )
    if not all(
        (score >= 0) if wants_true else (score < 0)
        for score, wants_true in zip(scores, true_flags)
    ):
        raise AssertionError("rank-two halfplane witness must realize the pattern")
    return RankTwoPatternWitness(
        basis=(first_basis, second_basis),
        parameters=parameters,
        scores=scores,
        certificate_mode=mode,
        bounded_scan_width=scan_width,
    )


def rank_two_threshold_pattern_reachable(
    base_scores: Vector,
    generators: IntMatrix,
    true_flags: tuple[bool, ...],
) -> bool:
    """Whether a threshold pattern occurs in a rank-two affine guard lattice."""
    return rank_two_threshold_pattern_witness(base_scores, generators, true_flags) is not None
