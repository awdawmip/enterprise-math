#!/usr/bin/env python3
"""Exact critical-degeneracy log-correction/root-selector checker.

The selected state is an integer polynomial plus either an exact positive
rational root or a Sturm-certified rational interval containing the smallest
positive irrational root.  No floating eigensolver/root solver is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product

Q = Fraction
Poly = tuple[Fraction, ...]  # ascending powers


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def p_add(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return trim(tuple((left[i] if i < len(left) else Q(0)) + (right[i] if i < len(right) else Q(0)) for i in range(n)))


def p_mul(left: Poly, right: Poly) -> Poly:
    out = [Q(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def p_scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * value for value in poly))


def p_eval(poly: Poly, x: Fraction) -> Fraction:
    result = Q(0)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def p_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def p_divmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    numerator = trim(numerator)
    denominator = trim(denominator)
    if denominator == (Q(0),):
        raise ZeroDivisionError
    if len(numerator) < len(denominator):
        return (Q(0),), numerator
    quotient = [Q(0) for _ in range(len(numerator) - len(denominator) + 1)]
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and any(remainder):
        degree = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[degree] += factor
        for j, value in enumerate(denominator):
            remainder[degree + j] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return trim(tuple(quotient)), trim(tuple(remainder))


def p_monic(poly: Poly) -> Poly:
    poly = trim(poly)
    if poly == (Q(0),):
        return poly
    return p_scale(poly, Q(1) / poly[-1])


def p_gcd(left: Poly, right: Poly) -> Poly:
    left, right = trim(left), trim(right)
    while right != (Q(0),):
        _, remainder = p_divmod(left, right)
        left, right = right, remainder
    return p_monic(left)


def p_div_exact(poly: Poly, factor: Poly) -> Poly:
    quotient, remainder = p_divmod(poly, factor)
    assert remainder == (Q(0),)
    return quotient


def divisors(value: int) -> tuple[int, ...]:
    value = abs(value)
    if value == 0:
        return ()
    result = []
    for candidate in range(1, int(value**0.5) + 1):
        if value % candidate == 0:
            result.append(candidate)
            if candidate * candidate != value:
                result.append(value // candidate)
    return tuple(sorted(result))


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
    return -1 if inversions % 2 else 1


def criticality_polynomial(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    n = len(matrix)
    assert n and all(len(row) == n for row in matrix)
    total: Poly = (Q(0),)
    for perm in permutations(range(n)):
        term: Poly = (Q(permutation_sign(perm)),)
        alive = True
        for i, j in enumerate(perm):
            if i == j:
                factor = (Q(1), Q(-matrix[i][i]))
            elif matrix[i][j]:
                factor = (Q(0), Q(-matrix[i][j]))
            else:
                alive = False
                break
            term = p_mul(term, factor)
        if alive:
            total = p_add(total, term)
    total = trim(total)
    assert all(value.denominator == 1 for value in total)
    assert total[0] == 1
    return tuple(value.numerator for value in total)


def rational_root_deflation(poly_int: tuple[int, ...]) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    poly: Poly = tuple(Q(value) for value in poly_int)
    if len(poly) <= 1:
        return (), poly
    leading = poly_int[-1]
    roots: list[Fraction] = []
    for denominator in divisors(leading):
        root = Q(1, denominator)
        while len(poly) > 1 and p_eval(poly, root) == 0:
            roots.append(root)
            poly = p_div_exact(poly, (-root, Q(1)))
    return tuple(sorted(roots)), trim(poly)


def sturm_sequence(poly: Poly) -> tuple[Poly, ...]:
    poly = trim(poly)
    derivative = p_derivative(poly)
    gcd = p_gcd(poly, derivative)
    squarefree = p_div_exact(poly, gcd) if len(gcd) > 1 else poly
    squarefree = trim(squarefree)
    if len(squarefree) <= 1:
        return (squarefree,)
    sequence = [squarefree, p_derivative(squarefree)]
    while sequence[-1] != (Q(0),):
        _, remainder = p_divmod(sequence[-2], sequence[-1])
        if remainder == (Q(0),):
            break
        next_poly = p_scale(remainder, Q(-1))
        # Positive rescaling only; preserve Sturm signs.
        scale = abs(next_poly[-1])
        if scale:
            next_poly = p_scale(next_poly, Q(1) / scale)
        sequence.append(next_poly)
    return tuple(sequence)


def variations(sequence: tuple[Poly, ...], x: Fraction) -> int:
    signs: list[int] = []
    for poly in sequence:
        value = p_eval(poly, x)
        if value > 0:
            signs.append(1)
        elif value < 0:
            signs.append(-1)
    return sum(signs[i] != signs[i - 1] for i in range(1, len(signs)))


def root_count(sequence: tuple[Poly, ...], left: Fraction, right: Fraction) -> int:
    assert left < right
    return variations(sequence, left) - variations(sequence, right)


@dataclass(frozen=True)
class RootSelector:
    polynomial: tuple[int, ...]
    exact_root: Fraction | None
    lower: Fraction
    upper: Fraction

    @property
    def is_rational(self) -> bool:
        return self.exact_root is not None


def isolate_smallest_irrational(poly: Poly) -> tuple[Fraction, Fraction] | None:
    if len(poly) <= 1:
        return None
    sequence = sturm_sequence(poly)
    total = root_count(sequence, Q(0), Q(1))
    if total <= 0:
        return None
    left, right = Q(0), Q(1)
    for _ in range(512):
        count = root_count(sequence, left, right)
        if count == 1 and right - left <= Q(1, 4096):
            assert root_count(sequence, Q(0), left) == 0
            return left, right
        midpoint = (left + right) / 2
        # Rational roots were completely deflated, so midpoint cannot be a root.
        assert p_eval(poly, midpoint) != 0
        if root_count(sequence, left, midpoint) > 0:
            right = midpoint
        else:
            left = midpoint
    raise AssertionError("irrational root isolation did not converge")


def smallest_positive_selector(poly_int: tuple[int, ...]) -> RootSelector:
    rational_roots, irrational_factor = rational_root_deflation(poly_int)
    rational_candidates = tuple(root for root in rational_roots if Q(0) < root <= 1)
    rational_min = min(rational_candidates, default=None)
    irrational_interval = isolate_smallest_irrational(irrational_factor)

    if rational_min is None and irrational_interval is None:
        raise ValueError("no positive root in (0,1]")
    if irrational_interval is None:
        assert rational_min is not None
        return RootSelector(poly_int, rational_min, rational_min, rational_min)
    if rational_min is None:
        return RootSelector(poly_int, None, *irrational_interval)

    left, right = irrational_interval
    sequence = sturm_sequence(irrational_factor)
    while left < rational_min < right:
        midpoint = (left + right) / 2
        assert p_eval(irrational_factor, midpoint) != 0
        if root_count(sequence, left, midpoint) > 0:
            right = midpoint
        else:
            left = midpoint
    if right <= rational_min:
        return RootSelector(poly_int, None, left, right)
    return RootSelector(poly_int, rational_min, rational_min, rational_min)


def reachability(matrix: tuple[tuple[int, ...], ...]) -> list[list[bool]]:
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


def critical_graph_shaped(matrix: tuple[tuple[int, ...], ...]) -> bool:
    if not any(value for row in matrix for value in row):
        return False
    reach = reachability(matrix)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value and not reach[j][i]:
                return False
    return True


def zero_correction_structure(matrix: tuple[tuple[int, ...], ...]) -> bool:
    assert critical_graph_shaped(matrix)
    # Since every positive edge lies in an SCC/cycle, row sum one on each
    # nonzero row is equivalent to every recurrent SCC being a unit cycle.
    return all(sum(row) in (0, 1) for row in matrix)


def validate_selector(matrix: tuple[tuple[int, ...], ...]) -> int:
    poly = criticality_polynomial(matrix)
    selector = smallest_positive_selector(poly)
    checks = 0
    assert selector.polynomial == poly
    if selector.is_rational:
        assert selector.exact_root is not None
        assert p_eval(tuple(Q(value) for value in poly), selector.exact_root) == 0
        assert Q(0) < selector.exact_root <= 1
        checks += 2
    else:
        rational_roots, irrational_factor = rational_root_deflation(poly)
        sequence = sturm_sequence(irrational_factor)
        assert Q(0) <= selector.lower < selector.upper <= 1
        assert root_count(sequence, selector.lower, selector.upper) == 1
        assert root_count(sequence, Q(0), selector.lower) == 0
        assert p_eval(irrational_factor, selector.lower) != 0
        assert p_eval(irrational_factor, selector.upper) != 0
        assert all(root >= selector.upper for root in rational_roots if root > 0)
        checks += 5

    zero = zero_correction_structure(matrix)
    if zero:
        assert selector.is_rational and selector.exact_root == 1
    else:
        if selector.is_rational:
            assert selector.exact_root is not None and selector.exact_root < 1
        else:
            assert selector.upper < 1
    checks += 1
    return checks


def exhaustive() -> tuple[int, int]:
    samples = 0
    checks = 0
    for n in (2, 3):
        for values in product((0, 1, 2), repeat=n * n):
            matrix = tuple(tuple(values[n * i + j] for j in range(n)) for i in range(n))
            if not critical_graph_shaped(matrix):
                continue
            samples += 1
            checks += validate_selector(matrix)
    return samples, checks


def special_examples() -> int:
    checks = 0

    # Unit 3-cycle: zero correction and exact root z=1.
    unit_cycle = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
    assert criticality_polynomial(unit_cycle) == (1, 0, 0, -1)
    selector = smallest_positive_selector(criticality_polynomial(unit_cycle))
    assert selector.exact_root == 1
    checks += 2

    # Degeneracy cycle: p=1-24 z^3, irrational root selector, correction ln(24)/3.
    deg_cycle = ((0, 2, 0), (0, 0, 3), (4, 0, 0))
    assert criticality_polynomial(deg_cycle) == (1, 0, 0, -24)
    selector = smallest_positive_selector(criticality_polynomial(deg_cycle))
    assert not selector.is_rational and selector.upper < 1
    checks += 2

    # Branching critical graph: rho=2, exact z_c=1/2.
    branching = ((1, 1), (1, 1))
    assert criticality_polynomial(branching) == (1, -2)
    selector = smallest_positive_selector(criticality_polynomial(branching))
    assert selector.exact_root == Q(1, 2)
    checks += 2

    # Golden ratio correction: p=1-z-z^2 and rational Sturm bracket.
    golden = ((1, 1), (1, 0))
    assert criticality_polynomial(golden) == (1, -1, -1)
    selector = smallest_positive_selector(criticality_polynomial(golden))
    assert not selector.is_rational
    assert Q(3, 5) < selector.lower < selector.upper < Q(5, 8)
    checks += 3

    # Rational correction maps to the current rational LN input 1/z_c.
    from enterprise_math.brc_logarithm import ln
    from enterprise_math.exact_arithmetic import division

    expr = ln(division(selector=1, denominator=1)) if False else ln(division(2, 1))
    assert expr.argument.numerator == 2 and expr.argument.denominator == 1
    checks += 1

    return checks


def main() -> int:
    samples, checks = exhaustive()
    special = special_examples()
    assert samples > 1000
    print("BRC critical-degeneracy log-correction selector checker: PASS")
    print(f"critical_graph_matrices={samples}")
    print(f"exact_selector_checks={checks}")
    print(f"special_checks={special}")
    print("irrational_golden_selector=PASS")
    print("zero_correction_structure=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
