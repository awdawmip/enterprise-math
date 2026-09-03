"""Exact critical-degeneracy BRC analysis and log-correction selectors.

Foundation extraction of main-backed PRs #1166-#1168.  This reference-grade
module keeps the proof surface exact: dominant branch ties, tropical critical
cycles, the integer critical-degeneracy matrix K, p_K(z)=det(I-zK), and the
smallest-positive-root selector.  It deliberately does not promote a floating
spectral primitive or a general algebraic-log evaluator.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations
from typing import Sequence, TypeAlias

from .brc_logarithm import LnExpr, ln
from .brc_weighted_recurrent import FiniteRecurrentMassAnalysis, finite_recurrent_mass_analysis
from .exact_arithmetic import division

RationalInput: TypeAlias = int | Fraction
ExplicitBranch: TypeAlias = tuple[int, int, RationalInput]
IntMatrix: TypeAlias = tuple[tuple[int, ...], ...]
RationalMatrix: TypeAlias = tuple[tuple[Fraction, ...], ...]
Poly: TypeAlias = tuple[Fraction, ...]  # ascending powers


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    out = Fraction(value)
    if out <= 0:
        raise ValueError(f"{name} must be positive")
    return out


def _nonnegative_integer_matrix(matrix: Sequence[Sequence[int]]) -> IntMatrix:
    rows = tuple(tuple(row) for row in matrix)
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError("matrix must be nonempty and square")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
            if value < 0:
                raise ValueError("matrix entries must be non-negative")
    return rows


def _trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _p_add(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return _trim(tuple(
        (left[i] if i < len(left) else Fraction(0, 1))
        + (right[i] if i < len(right) else Fraction(0, 1))
        for i in range(n)
    ))


def _p_mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0, 1) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return _trim(tuple(out))


def _p_scale(poly: Poly, scalar: Fraction) -> Poly:
    return _trim(tuple(scalar * value for value in poly))


def _p_eval(poly: Poly, x: Fraction) -> Fraction:
    result = Fraction(0, 1)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def _p_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Fraction(0, 1),)
    return _trim(tuple(Fraction(i, 1) * poly[i] for i in range(1, len(poly))))


def _p_divmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    numerator = _trim(numerator)
    denominator = _trim(denominator)
    if denominator == (Fraction(0, 1),):
        raise ZeroDivisionError("zero polynomial divisor")
    if len(numerator) < len(denominator):
        return (Fraction(0, 1),), numerator
    quotient = [Fraction(0, 1) for _ in range(len(numerator) - len(denominator) + 1)]
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and any(remainder):
        degree = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[degree] += factor
        for j, value in enumerate(denominator):
            remainder[degree + j] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return _trim(tuple(quotient)), _trim(tuple(remainder))


def _p_monic(poly: Poly) -> Poly:
    poly = _trim(poly)
    if poly == (Fraction(0, 1),):
        return poly
    return _p_scale(poly, Fraction(1, 1) / poly[-1])


def _p_gcd(left: Poly, right: Poly) -> Poly:
    left, right = _trim(left), _trim(right)
    while right != (Fraction(0, 1),):
        _, remainder = _p_divmod(left, right)
        left, right = right, remainder
    return _p_monic(left)


def _p_div_exact(poly: Poly, factor: Poly) -> Poly:
    quotient, remainder = _p_divmod(poly, factor)
    if remainder != (Fraction(0, 1),):
        raise AssertionError("polynomial division was not exact")
    return quotient


def _divisors(value: int) -> tuple[int, ...]:
    value = abs(value)
    if value == 0:
        return ()
    out: list[int] = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            out.append(candidate)
            if candidate * candidate != value:
                out.append(value // candidate)
        candidate += 1
    return tuple(sorted(out))


def _permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def _simple_cycles_from_support(support: Sequence[Sequence[bool]]) -> tuple[tuple[int, ...], ...]:
    n = len(support)
    cycles: list[tuple[int, ...]] = []
    for length in range(1, n + 1):
        for subset in combinations(range(n), length):
            smallest = subset[0]
            for perm in permutations(subset):
                if perm[0] != smallest:
                    continue
                if all(support[perm[i]][perm[(i + 1) % length]] for i in range(length)):
                    cycles.append(tuple(perm))
    return tuple(cycles)


def _cycle_product(cycle: Sequence[int], matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    product = Fraction(1, 1)
    for i, source in enumerate(cycle):
        product *= matrix[source][cycle[(i + 1) % len(cycle)]]
    return product


@dataclass(frozen=True)
class CriticalDegeneracyAnalysis:
    """Exact dominant-edge and tropical critical-graph data."""

    state_count: int
    dominant_mass_matrix: RationalMatrix
    dominant_tie_matrix: IntMatrix
    critical_cycles: tuple[tuple[int, ...], ...]
    reference_cycle: tuple[int, ...]
    reference_cycle_product: Fraction
    critical_edges: tuple[tuple[int, int], ...]
    critical_matrix: IntMatrix

    @property
    def reference_cycle_length(self) -> int:
        return len(self.reference_cycle)


@dataclass(frozen=True)
class CriticalRootSelector:
    """Exact smallest-positive-root state for ``p_K(z)``."""

    polynomial: tuple[int, ...]
    exact_root: Fraction | None
    lower: Fraction
    upper: Fraction
    selector: str = "SMALLEST_POSITIVE_REAL_ROOT"

    @property
    def is_rational(self) -> bool:
        return self.exact_root is not None

    def verify_interval(self) -> bool:
        if self.exact_root is not None:
            return self.lower == self.exact_root == self.upper and self.exact_root > 0
        return Fraction(0, 1) < self.lower < self.upper <= 1


@dataclass(frozen=True)
class CriticalLogCorrectionState:
    """Exact critical subleading correction before numeric log materialization."""

    critical_matrix: IntMatrix
    polynomial: tuple[int, ...]
    root: CriticalRootSelector


def critical_degeneracy_analysis(
    state_count: int,
    branches: Sequence[ExplicitBranch],
) -> CriticalDegeneracyAnalysis:
    """Build the exact tropical critical graph and integer degeneracy matrix K."""
    if isinstance(state_count, bool) or not isinstance(state_count, int) or state_count <= 0:
        raise ValueError("state_count must be a positive integer")
    cells: dict[tuple[int, int], list[Fraction]] = {}
    for source, target, raw_weight in branches:
        if isinstance(source, bool) or isinstance(target, bool):
            raise TypeError("branch endpoints must be integer indices")
        if not (
            isinstance(source, int)
            and isinstance(target, int)
            and 0 <= source < state_count
            and 0 <= target < state_count
        ):
            raise ValueError("branch endpoint out of range")
        weight = _positive_fraction("branch weight", raw_weight)
        cells.setdefault((source, target), []).append(weight)

    dominant = [[Fraction(0, 1) for _ in range(state_count)] for _ in range(state_count)]
    ties = [[0 for _ in range(state_count)] for _ in range(state_count)]
    support = [[False for _ in range(state_count)] for _ in range(state_count)]
    for (source, target), weights in cells.items():
        maximum = max(weights)
        dominant[source][target] = maximum
        ties[source][target] = sum(weight == maximum for weight in weights)
        support[source][target] = True

    cycles = _simple_cycles_from_support(support)
    if not cycles:
        raise ValueError("dominant support has no directed cycle")

    reference = cycles[0]
    reference_product = _cycle_product(reference, dominant)
    for cycle in cycles[1:]:
        product = _cycle_product(cycle, dominant)
        lhs = product ** len(reference)
        rhs = reference_product ** len(cycle)
        if lhs > rhs:
            reference = cycle
            reference_product = product

    r0 = len(reference)
    q0 = reference_product
    critical = tuple(
        cycle
        for cycle in cycles
        if _cycle_product(cycle, dominant) ** r0 == q0 ** len(cycle)
    )
    critical_edges: set[tuple[int, int]] = set()
    for cycle in critical:
        for index, source in enumerate(cycle):
            critical_edges.add((source, cycle[(index + 1) % len(cycle)]))

    k_matrix = [[0 for _ in range(state_count)] for _ in range(state_count)]
    for source, target in critical_edges:
        k_matrix[source][target] = ties[source][target]

    # Exact closure regression: every cycle inside the critical-edge union is critical.
    critical_support = [
        [((i, j) in critical_edges) for j in range(state_count)]
        for i in range(state_count)
    ]
    for cycle in _simple_cycles_from_support(critical_support):
        product = _cycle_product(cycle, dominant)
        if product**r0 != q0 ** len(cycle):
            raise AssertionError("critical-edge union created a subcritical directed cycle")

    return CriticalDegeneracyAnalysis(
        state_count=state_count,
        dominant_mass_matrix=tuple(tuple(row) for row in dominant),
        dominant_tie_matrix=tuple(tuple(row) for row in ties),
        critical_cycles=critical,
        reference_cycle=reference,
        reference_cycle_product=q0,
        critical_edges=tuple(sorted(critical_edges)),
        critical_matrix=tuple(tuple(row) for row in k_matrix),
    )


def criticality_polynomial(matrix: Sequence[Sequence[int]]) -> tuple[int, ...]:
    """Return exact ascending coefficients of ``det(I-zK)``."""
    normalized = _nonnegative_integer_matrix(matrix)
    n = len(normalized)
    total: Poly = (Fraction(0, 1),)
    for perm in permutations(range(n)):
        term: Poly = (Fraction(_permutation_sign(tuple(perm)), 1),)
        alive = True
        for i, j in enumerate(perm):
            if i == j:
                factor = (Fraction(1, 1), Fraction(-normalized[i][i], 1))
            elif normalized[i][j]:
                factor = (Fraction(0, 1), Fraction(-normalized[i][j], 1))
            else:
                alive = False
                break
            term = _p_mul(term, factor)
        if alive:
            total = _p_add(total, term)
    total = _trim(total)
    if total[0] != 1 or any(value.denominator != 1 for value in total):
        raise AssertionError("criticality polynomial lost integer constant-one form")
    return tuple(value.numerator for value in total)


def _rational_root_deflation(poly_int: tuple[int, ...]) -> tuple[tuple[Fraction, ...], Poly]:
    poly: Poly = tuple(Fraction(value, 1) for value in poly_int)
    if len(poly) <= 1:
        return (), poly
    roots: list[Fraction] = []
    for denominator in _divisors(poly_int[-1]):
        root = Fraction(1, denominator)
        while len(poly) > 1 and _p_eval(poly, root) == 0:
            roots.append(root)
            poly = _p_div_exact(poly, (-root, Fraction(1, 1)))
    return tuple(sorted(roots)), _trim(poly)


def _sturm_sequence(poly: Poly) -> tuple[Poly, ...]:
    poly = _trim(poly)
    derivative = _p_derivative(poly)
    gcd = _p_gcd(poly, derivative)
    squarefree = _p_div_exact(poly, gcd) if len(gcd) > 1 else poly
    squarefree = _trim(squarefree)
    if len(squarefree) <= 1:
        return (squarefree,)
    sequence = [squarefree, _p_derivative(squarefree)]
    while sequence[-1] != (Fraction(0, 1),):
        _, remainder = _p_divmod(sequence[-2], sequence[-1])
        if remainder == (Fraction(0, 1),):
            break
        next_poly = _p_scale(remainder, Fraction(-1, 1))
        scale = abs(next_poly[-1])
        if scale:
            next_poly = _p_scale(next_poly, Fraction(1, 1) / scale)
        sequence.append(next_poly)
    return tuple(sequence)


def _variations(sequence: Sequence[Poly], x: Fraction) -> int:
    signs: list[int] = []
    for poly in sequence:
        value = _p_eval(poly, x)
        if value > 0:
            signs.append(1)
        elif value < 0:
            signs.append(-1)
    return sum(signs[i] != signs[i - 1] for i in range(1, len(signs)))


def _root_count(sequence: Sequence[Poly], left: Fraction, right: Fraction) -> int:
    if not left < right:
        raise ValueError("root interval must have left < right")
    return _variations(sequence, left) - _variations(sequence, right)


def _isolate_smallest_irrational(poly: Poly, max_width: Fraction) -> tuple[Fraction, Fraction] | None:
    if len(poly) <= 1:
        return None
    sequence = _sturm_sequence(poly)
    if _root_count(sequence, Fraction(0, 1), Fraction(1, 1)) <= 0:
        return None
    left, right = Fraction(0, 1), Fraction(1, 1)
    for _ in range(4096):
        count = _root_count(sequence, left, right)
        if count == 1 and left > 0 and right - left <= max_width:
            if _root_count(sequence, Fraction(0, 1), left) != 0:
                raise AssertionError("isolated interval was not the smallest positive root")
            return left, right
        midpoint = (left + right) / 2
        if _p_eval(poly, midpoint) == 0:
            raise AssertionError("irrational factor unexpectedly hit a rational bisection endpoint")
        if _root_count(sequence, left, midpoint) > 0:
            right = midpoint
        else:
            left = midpoint
    raise AssertionError("irrational root isolation did not converge")


def smallest_positive_root_selector(
    polynomial: Sequence[int],
    *,
    max_width: RationalInput = Fraction(1, 4096),
) -> CriticalRootSelector:
    """Select the smallest positive real root in ``(0,1]`` exactly."""
    poly_int = tuple(polynomial)
    if not poly_int or poly_int[0] != 1:
        raise ValueError("polynomial must be ascending integer coefficients with constant term one")
    for value in poly_int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("polynomial coefficients must be integers")
    width = _positive_fraction("max_width", max_width)
    rational_roots, irrational_factor = _rational_root_deflation(poly_int)
    rational_candidates = tuple(root for root in rational_roots if 0 < root <= 1)
    rational_min = min(rational_candidates, default=None)
    irrational_interval = _isolate_smallest_irrational(irrational_factor, width)

    if rational_min is None and irrational_interval is None:
        raise ValueError("polynomial has no positive root in (0,1]")
    if irrational_interval is None:
        assert rational_min is not None
        return CriticalRootSelector(poly_int, rational_min, rational_min, rational_min)
    if rational_min is None:
        selector = CriticalRootSelector(poly_int, None, *irrational_interval)
        if not selector.verify_interval():
            raise AssertionError("invalid irrational root selector")
        return selector

    left, right = irrational_interval
    sequence = _sturm_sequence(irrational_factor)
    while left < rational_min < right:
        midpoint = (left + right) / 2
        if _p_eval(irrational_factor, midpoint) == 0:
            raise AssertionError("irrational factor hit rational midpoint")
        if _root_count(sequence, left, midpoint) > 0:
            right = midpoint
        else:
            left = midpoint
    if right <= rational_min:
        selector = CriticalRootSelector(poly_int, None, left, right)
    else:
        selector = CriticalRootSelector(poly_int, rational_min, rational_min, rational_min)
    if not selector.verify_interval():
        raise AssertionError("invalid smallest-positive-root selector")
    return selector


def critical_log_correction_state(matrix: Sequence[Sequence[int]]) -> CriticalLogCorrectionState:
    """Return the exact ``p_K + smallest-positive-root`` correction state."""
    normalized = _nonnegative_integer_matrix(matrix)
    polynomial = criticality_polynomial(normalized)
    root = smallest_positive_root_selector(polynomial)
    return CriticalLogCorrectionState(normalized, polynomial, root)


def _reachability(matrix: IntMatrix) -> list[list[bool]]:
    n = len(matrix)
    reach = [[matrix[i][j] > 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        reach[i][i] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return reach


def critical_graph_shaped(matrix: Sequence[Sequence[int]]) -> bool:
    """Whether every positive edge lies on a directed cycle."""
    normalized = _nonnegative_integer_matrix(matrix)
    if not any(value for row in normalized for value in row):
        return False
    reach = _reachability(normalized)
    return all(
        not value or reach[target][source]
        for source, row in enumerate(normalized)
        for target, value in enumerate(row)
    )


def critical_log_zero(matrix: Sequence[Sequence[int]]) -> bool:
    """Exact WBRC-T42 zero-correction structural predicate."""
    normalized = _nonnegative_integer_matrix(matrix)
    if not critical_graph_shaped(normalized):
        raise ValueError("zero-correction law requires a critical-graph-shaped matrix")
    return all(sum(row) in (0, 1) for row in normalized)


def critical_log_threshold_analysis(
    matrix: Sequence[Sequence[int]],
    threshold: RationalInput,
) -> FiniteRecurrentMassAnalysis:
    """Analyze ``K/R`` exactly; stable iff ``Gamma_crit < LN(R)``."""
    normalized = _nonnegative_integer_matrix(matrix)
    r = _positive_fraction("threshold", threshold)
    scaled = tuple(tuple(Fraction(value, 1) / r for value in row) for row in normalized)
    return finite_recurrent_mass_analysis(scaled)


def critical_log_less_than_rational(
    matrix: Sequence[Sequence[int]],
    threshold: RationalInput,
) -> bool:
    """Return the exact rational-threshold comparison ``Gamma_crit < LN(R)``."""
    return critical_log_threshold_analysis(matrix, threshold).stable


def critical_log_bounds(selector: CriticalRootSelector) -> tuple[LnExpr, LnExpr]:
    """Return BRC-LN lower/upper expressions for ``Gamma_crit=-ln(z_c)``.

    For an exact rational root the two expressions are identical.  For an
    irrational selector ``a<z_c<b`` the returned pair is
    ``(LN(1/b), LN(1/a))``.
    """
    if not selector.verify_interval():
        raise ValueError("invalid critical root selector")
    lower_argument = Fraction(1, 1) / selector.upper
    upper_argument = Fraction(1, 1) / selector.lower
    lower_expr = ln(division(lower_argument.numerator, lower_argument.denominator))
    upper_expr = ln(division(upper_argument.numerator, upper_argument.denominator))
    return lower_expr, upper_expr


def critical_log_correction_from_branches(
    state_count: int,
    branches: Sequence[ExplicitBranch],
) -> tuple[CriticalDegeneracyAnalysis, CriticalLogCorrectionState]:
    """Full explicit-branch route to ``K`` and the exact log-correction state."""
    analysis = critical_degeneracy_analysis(state_count, branches)
    return analysis, critical_log_correction_state(analysis.critical_matrix)
