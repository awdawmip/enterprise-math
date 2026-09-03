#!/usr/bin/env python3
"""Exact checker for the unique-critical-cycle large-moment BRC asymptotic.

No floating eigenvalue is used.  The main verification expands characteristic
coefficients as finite integer combinations of rational exponential bases b^m
and checks the exact root-free critical-gap/equality pattern.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

Q = Fraction
EdgeMap = dict[tuple[int, int], tuple[Fraction, ...]]


def normalize_edges(n: int, raw: dict[tuple[int, int], tuple[Fraction, ...] | list[Fraction]]) -> EdgeMap:
    result: EdgeMap = {}
    for (u, v), weights in raw.items():
        assert 0 <= u < n and 0 <= v < n
        vals = tuple(Q(weight) for weight in weights)
        assert vals and all(weight > 0 for weight in vals)
        result[(u, v)] = vals
    return result


def dominant_cell(edges: EdgeMap, u: int, v: int) -> tuple[Fraction, int] | None:
    weights = edges.get((u, v), ())
    if not weights:
        return None
    maximum = max(weights)
    return maximum, sum(weight == maximum for weight in weights)


def canonical_rotation(cycle: tuple[int, ...]) -> tuple[int, ...]:
    if len(cycle) <= 1:
        return cycle
    rotations = [cycle[i:] + cycle[:i] for i in range(len(cycle))]
    return min(rotations)


def simple_cycles(n: int, edges: EdgeMap) -> tuple[tuple[int, ...], ...]:
    found: set[tuple[int, ...]] = set()
    for vertex in range(n):
        if (vertex, vertex) in edges:
            found.add((vertex,))
    for length in range(2, n + 1):
        for vertices in combinations(range(n), length):
            for order in permutations(vertices):
                if order != canonical_rotation(order):
                    continue
                if all((order[i], order[(i + 1) % length]) in edges for i in range(length)):
                    found.add(order)
    return tuple(sorted(found, key=lambda cycle: (len(cycle), cycle)))


def cycle_data(cycle: tuple[int, ...], edges: EdgeMap) -> tuple[Fraction, int]:
    product_weight = Q(1)
    degeneracy = 1
    for i, source in enumerate(cycle):
        target = cycle[(i + 1) % len(cycle)]
        cell = dominant_cell(edges, source, target)
        assert cell is not None
        weight, ties = cell
        product_weight *= weight
        degeneracy *= ties
    return product_weight, degeneracy


def compare_cycle_mean(left: tuple[int, ...], right: tuple[int, ...], edges: EdgeMap) -> int:
    q_left, _ = cycle_data(left, edges)
    q_right, _ = cycle_data(right, edges)
    lhs = q_left ** len(right)
    rhs = q_right ** len(left)
    return (lhs > rhs) - (lhs < rhs)


def critical_cycles(n: int, edges: EdgeMap) -> tuple[tuple[int, ...], ...]:
    cycles = simple_cycles(n, edges)
    if not cycles:
        return ()
    best = cycles[0]
    for cycle in cycles[1:]:
        if compare_cycle_mean(cycle, best, edges) > 0:
            best = cycle
    return tuple(cycle for cycle in cycles if compare_cycle_mean(cycle, best, edges) == 0)


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
    return -1 if inversions % 2 else 1


def characteristic_exponential_coefficients(n: int, edges: EdgeMap) -> dict[int, dict[Fraction, int]]:
    """Return lambda-degree -> {rational base b: integer coeff c} for sum c*b^m."""
    output: dict[int, dict[Fraction, int]] = {}
    for perm in permutations(range(n)):
        terms: dict[tuple[int, Fraction], int] = {(0, Q(1)): permutation_sign(perm)}
        alive = True
        for source in range(n):
            target = perm[source]
            factors: list[tuple[int, Fraction, int]] = []
            if source == target:
                factors.append((1, Q(1), 1))  # lambda choice
                factors.extend((0, weight, -1) for weight in edges.get((source, source), ()))
            else:
                factors.extend((0, weight, -1) for weight in edges.get((source, target), ()))
                if not factors:
                    alive = False
                    break
            next_terms: dict[tuple[int, Fraction], int] = {}
            for (degree, base), coeff in terms.items():
                for add_degree, factor_base, factor_coeff in factors:
                    key = (degree + add_degree, base * factor_base)
                    next_terms[key] = next_terms.get(key, 0) + coeff * factor_coeff
            terms = {key: coeff for key, coeff in next_terms.items() if coeff}
        if not alive:
            continue
        for (degree, base), coeff in terms.items():
            bucket = output.setdefault(degree, {})
            bucket[base] = bucket.get(base, 0) + coeff
    return {
        degree: {base: coeff for base, coeff in bases.items() if coeff}
        for degree, bases in output.items()
        if any(bases.values())
    }


def evaluate_characteristic(exp_coeffs: dict[int, dict[Fraction, int]], moment_order: int, lam: Fraction) -> Fraction:
    return sum(
        sum(Q(coeff) * (base**moment_order) for base, coeff in bases.items()) * (lam**degree)
        for degree, bases in exp_coeffs.items()
    )


def moment_matrix(n: int, edges: EdgeMap, m: int) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(sum((weight**m for weight in edges.get((i, j), ())), Q(0)) for j in range(n))
        for i in range(n)
    )


def determinant(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Q(1)
    work = [list(row) for row in matrix]
    result = Q(1)
    sign = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        result *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * result


def direct_char_value(matrix: tuple[tuple[Fraction, ...], ...], lam: Fraction) -> Fraction:
    n = len(matrix)
    return determinant(
        tuple(
            tuple((lam if i == j else Q(0)) - matrix[i][j] for j in range(n))
            for i in range(n)
        )
    )


def verify_unique_critical_sample(n: int, edges: EdgeMap) -> int:
    critical = critical_cycles(n, edges)
    if len(critical) != 1:
        return 0
    star = critical[0]
    r = len(star)
    q_star, d_star = cycle_data(star, edges)

    cycles = simple_cycles(n, edges)
    for cycle in cycles:
        if cycle == star:
            continue
        q_cycle, _ = cycle_data(cycle, edges)
        assert q_cycle**r < q_star ** len(cycle)

    exp_coeffs = characteristic_exponential_coefficients(n, edges)
    assert exp_coeffs[n] == {Q(1): 1}
    equality_terms: list[tuple[int, Fraction, int]] = []
    checked = 0
    for degree, bases in exp_coeffs.items():
        k = n - degree
        if k == 0:
            continue
        for base, coeff in bases.items():
            assert coeff
            lhs = base**r
            rhs = q_star**k
            assert lhs <= rhs
            if lhs == rhs:
                equality_terms.append((k, base, coeff))
            checked += 1
    assert equality_terms == [(r, q_star, -d_star)]

    # Exponential dictionaries exactly reproduce the ordinary characteristic
    # polynomial after moment specialization.
    for m in (0, 1, 2, 3, 5):
        matrix = moment_matrix(n, edges, m)
        for lam in (Q(0), Q(1, 7), Q(2, 3), Q(3, 2)):
            assert evaluate_characteristic(exp_coeffs, m, lam) == direct_char_value(matrix, lam)
            checked += 1
    return checked


def structured_exhaustion() -> tuple[int, int]:
    unique_samples = 0
    checks = 0

    # Two-state explicit multigraphs with parallel dominant alternatives.
    catalog = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog, repeat=len(cells2)):
        raw = {cell: weights for cell, weights in zip(cells2, assignment) if weights}
        edges = normalize_edges(2, raw)
        result = verify_unique_critical_sample(2, edges)
        if result:
            unique_samples += 1
            checks += result

    # Three-state support/weight exhaustion.  Single branches are enough here;
    # parallel-degeneracy behavior is already exercised above and below.
    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=len(cells3)):
        raw = {cell: weights for cell, weights in zip(cells3, assignment) if weights}
        edges = normalize_edges(3, raw)
        result = verify_unique_critical_sample(3, edges)
        if result:
            unique_samples += 1
            checks += result

    return unique_samples, checks


def exact_perron_brackets() -> int:
    checks = 0

    examples = [
        (
            2,
            normalize_edges(
                2,
                {
                    (0, 1): (Q(1, 2), Q(1, 2), Q(1, 4)),
                    (1, 0): (Q(1, 2), Q(1, 2), Q(1, 5)),
                    (0, 0): (Q(1, 5),),
                    (1, 1): (Q(1, 6),),
                },
            ),
            Q(1, 2),
            Q(2),  # D^(1/r) = sqrt(4)
        ),
        (
            3,
            normalize_edges(
                3,
                {
                    (0, 1): (Q(1, 2), Q(1, 2), Q(1, 4)),
                    (1, 2): (Q(1, 2), Q(1, 2)),
                    (2, 0): (Q(1, 2), Q(1, 2), Q(1, 5)),
                    (0, 0): (Q(1, 6),),
                    (1, 1): (Q(1, 7),),
                    (2, 2): (Q(1, 8),),
                },
            ),
            Q(1, 2),
            Q(2),  # D^(1/r) = cube-root(8)
        ),
    ]

    for n, edges, mu, target in examples:
        critical = critical_cycles(n, edges)
        assert len(critical) == 1
        exp_coeffs = characteristic_exponential_coefficients(n, edges)
        for m in range(4, 13):
            scale = mu**m
            lower = scale * (target - Q(1, 10))
            upper = scale * (target + Q(1, 10))
            p_lower = evaluate_characteristic(exp_coeffs, m, lower)
            p_upper = evaluate_characteristic(exp_coeffs, m, upper)
            # For these irreducible examples the largest positive root is simple;
            # exact signs bracket it inside a 0.2*mu^m window around the limit.
            assert p_lower < 0 < p_upper
            checks += 2
    return checks


def multiple_critical_counterexample() -> None:
    # Two equally critical self-loop state cycles, but different degeneracies.
    edges = normalize_edges(
        2,
        {
            (0, 0): (Q(1, 2),),
            (1, 1): (Q(1, 2), Q(1, 2), Q(1, 2)),
        },
    )
    critical = critical_cycles(2, edges)
    assert set(critical) == {(0,), (1,)}
    for m in range(1, 8):
        matrix = moment_matrix(2, edges, m)
        scale = Q(1, 2) ** m
        # Exact spectral radius is the larger diagonal entry: normalized value 3,
        # not the D=1 correction of the first critical loop.
        assert matrix[0][0] / scale == 1
        assert matrix[1][1] / scale == 3


def main() -> int:
    unique_samples, coefficient_checks = structured_exhaustion()
    bracket_checks = exact_perron_brackets()
    multiple_critical_counterexample()

    assert unique_samples > 1000
    print("BRC unique-critical-cycle moment asymptotic checker: PASS")
    print(f"unique_critical_samples={unique_samples}")
    print(f"exact_coefficient_checks={coefficient_checks}")
    print(f"exact_perron_bracket_checks={bracket_checks}")
    print("multiple_critical_boundary=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
