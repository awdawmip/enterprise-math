#!/usr/bin/env python3
"""Exact checker for global rational powered strict gauges and reducible obstructions."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

from enterprise_math.brc_critical_ratio_jet import powered_critical_gauge

Q = Fraction
Branch = tuple[int, int, Fraction]
RatMatrix = tuple[tuple[Fraction, ...], ...]


def normalize_branches(n: int, cells, assignment) -> tuple[Branch, ...]:
    return tuple(
        (u, v, q)
        for (u, v), weights in zip(cells, assignment)
        for q in weights
    )


def cells(branches: tuple[Branch, ...]):
    out: dict[tuple[int, int], list[Fraction]] = {}
    for u, v, q in branches:
        out.setdefault((u, v), []).append(q)
    return {cell: tuple(values) for cell, values in out.items()}


def simple_cycles(weight: RatMatrix) -> tuple[tuple[int, ...], ...]:
    n = len(weight)
    out: list[tuple[int, ...]] = []
    for length in range(1, n + 1):
        for subset in combinations(range(n), length):
            first = subset[0]
            for perm in permutations(subset):
                if perm[0] != first:
                    continue
                if all(weight[perm[i]][perm[(i + 1) % length]] > 0 for i in range(length)):
                    out.append(tuple(perm))
    return tuple(out)


def cycle_product(cycle: tuple[int, ...], weight: RatMatrix) -> Fraction:
    out = Q(1)
    for i, u in enumerate(cycle):
        out *= weight[u][cycle[(i + 1) % len(cycle)]]
    return out


def class_data(n: int, critical_components: tuple[tuple[int, ...], ...]):
    class_of: dict[int, int] = {}
    classes: list[tuple[int, ...]] = []
    for component in critical_components:
        idx = len(classes)
        classes.append(component)
        for vertex in component:
            class_of[vertex] = idx
    for vertex in range(n):
        if vertex not in class_of:
            idx = len(classes)
            classes.append((vertex,))
            class_of[vertex] = idx
    return tuple(classes), class_of


def max_simple_path_products(weight: RatMatrix) -> tuple[Fraction, ...]:
    n = len(weight)
    result: list[Fraction] = []
    for start in range(n):
        best = Q(1)

        def visit(current: int, seen: frozenset[int], value: Fraction) -> None:
            nonlocal best
            if value > best:
                best = value
            for target in range(n):
                edge = weight[current][target]
                if edge <= 0 or target in seen:
                    continue
                visit(target, seen | {target}, value * edge)

        visit(start, frozenset({start}), Q(1))
        result.append(best)
    return tuple(result)


def global_strict_gauge(n: int, branches: tuple[Branch, ...]):
    gauge = powered_critical_gauge(n, branches)
    analysis = gauge.analysis
    h0 = {v: Q(1) for v in range(n)}
    h0.update(gauge.potential_map)
    classes, class_of = class_data(n, gauge.components)
    m = len(classes)
    cell_map = cells(branches)
    critical_edges = set(analysis.critical_edges)

    quotient = [[Q(0) for _ in range(m)] for _ in range(m)]
    records: list[tuple[int, int, Fraction, bool]] = []
    for u, v, q in branches:
        dominant_critical = (
            (u, v) in critical_edges
            and q == max(cell_map[(u, v)])
        )
        raw = (q ** analysis.reference_cycle_length) * h0[v] / (
            analysis.reference_cycle_product * h0[u]
        )
        if dominant_critical:
            assert raw == 1 and class_of[u] == class_of[v]
        else:
            a, b = class_of[u], class_of[v]
            quotient[a][b] = max(quotient[a][b], raw)
        records.append((u, v, raw, dominant_critical))

    qmat = tuple(tuple(row) for row in quotient)
    cycles_q = simple_cycles(qmat)
    cycle_checks = 0
    for cycle in cycles_q:
        value = cycle_product(cycle, qmat)
        assert Q(0) < value < 1
        cycle_checks += 1

    if cycles_q:
        eps = min((Q(1) - cycle_product(cycle, qmat)) / (2 * len(cycle)) for cycle in cycles_q)
        c = Q(1) - eps
    else:
        c = Q(1, 2)
    assert Q(0) < c < 1

    scaled = tuple(tuple(value / c if value else Q(0) for value in row) for row in qmat)
    x = max_simple_path_products(scaled)
    edge_checks = 0
    for a in range(m):
        for b in range(m):
            if qmat[a][b]:
                assert qmat[a][b] * x[b] <= c * x[a] < x[a]
                edge_checks += 1

    h = {v: h0[v] * x[class_of[v]] for v in range(n)}
    final_records: list[tuple[int, int, Fraction, bool]] = []
    for u, v, _, dominant_critical in records:
        # recover q from original order below
        pass
    final_records = []
    for u, v, q in branches:
        dominant_critical = (
            (u, v) in critical_edges
            and q == max(cell_map[(u, v)])
        )
        lam = (q ** analysis.reference_cycle_length) * h[v] / (
            analysis.reference_cycle_product * h[u]
        )
        assert (lam == 1) == dominant_critical
        if not dominant_critical:
            assert Q(0) < lam <= c < 1
        final_records.append((u, v, lam, dominant_critical))

    return gauge, classes, class_of, h, tuple(final_records), c, cycle_checks, edge_checks


def moment_matrix(n: int, branches: tuple[Branch, ...], order: int):
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for u, v, q in branches:
        out[u][v] += q**order
    return tuple(tuple(row) for row in out)


def full_jet_check(n: int, branches: tuple[Branch, ...], gauge_data) -> int:
    gauge, _, _, h, records, _, _, _ = gauge_data
    r0 = gauge.analysis.reference_cycle_length
    q0 = gauge.analysis.reference_cycle_product
    levels = tuple(sorted({lam for _, _, lam, _ in records}, reverse=True))
    layers = []
    for level in levels:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, lam, _ in records:
            if lam == level:
                matrix[u][v] += 1
        layers.append(tuple(tuple(row) for row in matrix))
    assert layers[0] == gauge.analysis.critical_matrix
    checks = 1
    for s in range(4):
        Wm = moment_matrix(n, branches, r0 * s)
        transformed = tuple(
            tuple((h[j] / h[i]) ** s * Wm[i][j] / (q0**s) for j in range(n))
            for i in range(n)
        )
        expected = tuple(
            tuple(
                sum(((level**s) * layers[k][i][j] for k, level in enumerate(levels)), Q(0))
                for j in range(n)
            )
            for i in range(n)
        )
        assert transformed == expected
        checks += n * n
    return checks


def validate(n: int, branches: tuple[Branch, ...]):
    try:
        data = global_strict_gauge(n, branches)
    except ValueError:
        return None
    records = data[4]
    strict = sum(not flag for _, _, _, flag in records)
    branch_checks = 2 * len(records) + strict
    jet_checks = full_jet_check(n, branches, data)
    return branch_checks, jet_checks, data[6], data[7]


def exhaustive_regression():
    samples = branch_checks = jet_checks = cycle_checks = quotient_edge_checks = 0
    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog2, repeat=4):
        branches = normalize_branches(2, cells2, assignment)
        result = validate(2, branches)
        if result is None:
            continue
        samples += 1
        branch_checks += result[0]
        jet_checks += result[1]
        cycle_checks += result[2]
        quotient_edge_checks += result[3]

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=9):
        branches = normalize_branches(3, cells3, assignment)
        result = validate(3, branches)
        if result is None:
            continue
        samples += 1
        branch_checks += result[0]
        jet_checks += result[1]
        cycle_checks += result[2]
        quotient_edge_checks += result[3]
    return samples, branch_checks, jet_checks, cycle_checks, quotient_edge_checks


def class_gauge_and_puiseux_examples():
    checks = 0
    # Two tied unit critical classes with strict cross edges.
    a = b = Q(1, 4)
    # class gauge t=1/2 changes individual ratios but preserves closed product.
    ap = a * Q(1, 2)
    bp = b / Q(1, 2)
    assert ap != a and bp != b
    assert ap * bp == a * b == Q(1, 16)
    assert ap < 1 and bp < 1
    checks += 4

    # A_s=[[1,a^s],[b^s,1]] has rho=1+(ab)^(s/2).
    # Here ab=1/16 so even s gives a rational exact correction.
    for s in (2, 4, 6):
        root_shift = Q(1, 4) ** s
        x = (a * b) ** s
        assert root_shift * root_shift == x
        lam = Q(1) + root_shift
        char = (lam - 1) * (lam - 1) - x
        assert char == 0
        checks += 2

    # Unique winner k1=2,k2=1.  With x=(ab)^s, the Perron shift lies
    # strictly between x-x^2 and x, proving first excursion base ab.
    for s in range(1, 6):
        x = Q(1, 4) ** s
        lower = Q(2) + x - x * x
        upper = Q(2) + x
        def char_unique(lam: Fraction) -> Fraction:
            return (lam - 2) * (lam - 1) - x
        assert char_unique(lower) < 0 < char_unique(upper)
        checks += 2
    return checks


def main() -> int:
    samples, branch_checks, jet_checks, cycle_checks, quotient_edge_checks = exhaustive_regression()
    special = class_gauge_and_puiseux_examples()
    assert samples > 10000
    print("BRC global powered strict gauge reducible checker: PASS")
    print(f"recurrent_samples={samples}")
    print(f"branch_equality_strictness_checks={branch_checks}")
    print(f"exact_full_jet_checks={jet_checks}")
    print(f"quotient_cycle_strictness_checks={cycle_checks}")
    print(f"quotient_edge_potential_checks={quotient_edge_checks}")
    print(f"class_gauge_puiseux_unique_winner_checks={special}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
