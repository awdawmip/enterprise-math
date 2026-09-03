#!/usr/bin/env python3
"""Exact support/rational checks for BRC feedback circuit atoms."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
from math import inf

Matrix = list[list[Q]]


def eye(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def determinant(matrix: Matrix) -> Q:
    if not matrix:
        return Q(1)
    work = [row[:] for row in matrix]
    n = len(work)
    out = Q(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pv = work[col][col]
        out *= pv
        for row in range(col + 1, n):
            factor = work[row][col] / pv
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * out


def inverse(matrix: Matrix) -> Matrix | None:
    n = len(matrix)
    aug = [matrix[i][:] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [value / pv for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [aug[row][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def stable_star(matrix: Matrix) -> tuple[bool, Matrix | None]:
    star = inverse(sub(eye(len(matrix)), matrix))
    if star is None or any(value < 0 for row in star for value in row):
        return False, None
    return True, star


def indices(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if mask & (1 << i)]


def principal(matrix: Matrix, mask: int) -> Matrix:
    idx = indices(mask, len(matrix))
    return [[matrix[i][j] for j in idx] for i in idx]


def zeta_table(kernel: Matrix) -> dict[int, Q]:
    n = len(kernel)
    z = {0: Q(1)}
    for mask in range(1, 1 << n):
        p = principal(kernel, mask)
        d = determinant(sub(eye(len(p)), p))
        assert d > 0
        z[mask] = 1 / d
    return z


def interaction_table(zeta: dict[int, Q], n: int) -> dict[int, Q]:
    j: dict[int, Q] = {}
    for mask in range(1, 1 << n):
        value = Q(1)
        submask = mask
        while True:
            if (mask.bit_count() - submask.bit_count()) & 1:
                value /= zeta[submask]
            else:
                value *= zeta[submask]
            if submask == 0:
                break
            submask = (submask - 1) & mask
        j[mask] = value
    return j


def proper_nonempty_submasks(mask: int):
    submask = (mask - 1) & mask
    while submask:
        yield submask
        submask = (submask - 1) & mask


def is_primitive(mask: int, interactions: dict[int, Q]) -> bool:
    return interactions[mask] > 1 and all(
        interactions[submask] == 1
        for submask in proper_nonempty_submasks(mask)
    )


def directed_girth(matrix: Matrix) -> int | float:
    n = len(matrix)
    best = inf
    for i in range(n):
        if matrix[i][i] > 0:
            best = 1
    # shortest positive path distances
    dist = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if i != j and matrix[i][j] > 0:
                dist[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] > 0 and dist[j][i] < inf:
                best = min(best, 1 + dist[j][i])
    return best


def interaction_girth(interactions: dict[int, Q]) -> int | float:
    orders = [mask.bit_count() for mask, value in interactions.items() if value > 1]
    return min(orders) if orders else inf


def induced_is_directed_simple_cycle(kernel: Matrix, mask: int) -> bool:
    idx = indices(mask, len(kernel))
    if len(idx) == 1:
        return kernel[idx[0]][idx[0]] > 0
    allowed = set(idx)
    for i in idx:
        outdegree = sum(kernel[i][j] > 0 for j in idx)
        indegree = sum(kernel[j][i] > 0 for j in idx)
        if outdegree != 1 or indegree != 1:
            return False
    # 1-in/1-out can be disjoint cycles; require one component.
    reached = {idx[0]}
    current = idx[0]
    for _ in range(len(idx)):
        nxt = next(j for j in idx if kernel[current][j] > 0)
        reached.add(nxt)
        current = nxt
    return reached == allowed and current == idx[0]


def cycle_product(kernel: Matrix, mask: int) -> Q:
    idx = indices(mask, len(kernel))
    if len(idx) == 1:
        return kernel[idx[0]][idx[0]]
    assert induced_is_directed_simple_cycle(kernel, mask)
    start = idx[0]
    current = start
    value = Q(1)
    for _ in range(len(idx)):
        nxt = next(j for j in idx if kernel[current][j] > 0)
        value *= kernel[current][nxt]
        current = nxt
    assert current == start
    return value


def check_all_loopless_four_vertex_supports() -> None:
    n = 4
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    weight = Q(1, 10)
    graphs = 0
    primitive_atoms = 0
    girth_hist: dict[int | float, int] = {}

    for support_bits in range(1 << len(edges)):
        kernel = [[Q(0) for _ in range(n)] for _ in range(n)]
        for k, (i, j) in enumerate(edges):
            if support_bits & (1 << k):
                kernel[i][j] = weight
        # loopless row sum <=3/10, so every support is safely stable.
        assert stable_star(kernel)[0]
        zeta = zeta_table(kernel)
        interactions = interaction_table(zeta, n)
        g_dir = directed_girth(kernel)
        g_int = interaction_girth(interactions)
        assert g_int == g_dir
        girth_hist[g_int] = girth_hist.get(g_int, 0) + 1

        for mask in range(1, 1 << n):
            if not is_primitive(mask, interactions):
                continue
            primitive_atoms += 1
            assert induced_is_directed_simple_cycle(kernel, mask)
            q = cycle_product(kernel, mask)
            assert Q(0) < q < 1
            assert interactions[mask] == 1 / (1 - q)
            # All proper induced subsets have no interaction by definition.
            assert all(interactions[submask] == 1 for submask in proper_nonempty_submasks(mask))

        graphs += 1

    assert graphs == 2**12 == 4096
    print(f"loopless_4vertex_supports={graphs}")
    print(f"primitive_atoms={primitive_atoms}")
    print("girth_hist=" + ",".join(f"{key}:{value}" for key, value in sorted(girth_hist.items(), key=lambda kv: str(kv[0]))))


def valuation(value: Q, prime: int) -> int:
    numerator = value.numerator
    denominator = value.denominator
    out = 0
    while numerator % prime == 0:
        numerator //= prime
        out += 1
    while denominator % prime == 0:
        denominator //= prime
        out -= 1
    return out


def simple_cycle_kernel(weights: list[Q]) -> Matrix:
    n = len(weights)
    kernel = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i, w in enumerate(weights):
        kernel[i][(i + 1) % n] = w
    return kernel


def gauge_matrix(kernel: Matrix, potential: list[Q]) -> Matrix:
    return [
        [kernel[i][j] * potential[j] / potential[i] for j in range(len(kernel))]
        for i in range(len(kernel))
    ]


def check_nonuniform_circuit_atoms() -> None:
    examples = [
        [Q(2, 3), Q(1, 4)],
        [Q(2, 3), Q(3, 5), Q(1, 4)],
        [Q(2, 3), Q(3, 5), Q(5, 7), Q(1, 4)],
    ]
    potentials = [
        [Q(2), Q(3)],
        [Q(2), Q(3), Q(5)],
        [Q(2), Q(3), Q(5), Q(7)],
    ]
    for weights, h in zip(examples, potentials):
        kernel = simple_cycle_kernel(weights)
        assert stable_star(kernel)[0]
        interactions = interaction_table(zeta_table(kernel), len(kernel))
        full = (1 << len(kernel)) - 1
        assert is_primitive(full, interactions)
        q = Q(1)
        for weight in weights:
            q *= weight
        assert interactions[full] == 1 / (1 - q)
        assert interaction_girth(interactions) == len(kernel)

        gauged = gauge_matrix(kernel, h)
        q_g = cycle_product(gauged, full)
        assert q_g == q
        assert interaction_table(zeta_table(gauged), len(kernel))[full] == interactions[full]

        for prime in [2, 3, 5, 7]:
            assert valuation(q, prime) == sum(valuation(weight, prime) for weight in weights)


def has_directed_cycle_support(matrix: Matrix) -> bool:
    return directed_girth(matrix) < inf


def add_inserted_events(background: Matrix, active: set[int], events: list[tuple[int, int, Q]]) -> Matrix:
    out = [row[:] for row in background]
    for i in active:
        source, target, mass = events[i]
        out[source][target] += mass
    return out


def feedback_kernel(star: Matrix, events: list[tuple[int, int, Q]]) -> Matrix:
    return [[star[r[1]][s[0]] * s[2] for s in events] for r in events]


def check_pure_order_and_dag_realizations() -> None:
    cycle_weights = {
        2: [Q(1, 2), Q(1, 3)],
        3: [Q(1, 2), Q(1, 3), Q(1, 4)],
        4: [Q(1, 2), Q(1, 3), Q(1, 4), Q(1, 5)],
    }
    for r, weights in cycle_weights.items():
        kernel = simple_cycle_kernel(weights)
        interactions = interaction_table(zeta_table(kernel), r)
        full = (1 << r) - 1
        assert interaction_girth(interactions) == r
        assert interactions[full] > 1
        assert all(interactions[mask] == 1 for mask in range(1, full))

        # Full 2r-state DAG realization.
        n = 2 * r
        background = [[Q(0) for _ in range(n)] for _ in range(n)]
        events: list[tuple[int, int, Q]] = []
        for i in range(r):
            a_i = 2 * i
            b_i = 2 * i + 1
            a_next = 2 * ((i + 1) % r)
            background[b_i][a_next] = weights[i]
            events.append((a_i, b_i, Q(1)))
        assert not has_directed_cycle_support(background)
        stable, star = stable_star(background)
        assert stable and star is not None
        realized = feedback_kernel(star, events)
        assert realized == kernel

        # Every proper inserted subset leaves the full graph acyclic.
        for mask in range(1 << r):
            active = {i for i in range(r) if mask & (1 << i)}
            updated = add_inserted_events(background, active, events)
            if mask != full:
                assert not has_directed_cycle_support(updated)
                assert determinant(sub(eye(n), updated)) == 1
            else:
                assert has_directed_cycle_support(updated)
                q = cycle_product(kernel, full)
                assert determinant(sub(eye(n), updated)) == 1 - q


def check_self_loop_order_one() -> None:
    kernel = [[Q(1, 3), Q(1, 10)], [Q(0), Q(0)]]
    assert stable_star(kernel)[0]
    interactions = interaction_table(zeta_table(kernel), 2)
    assert interaction_girth(interactions) == directed_girth(kernel) == 1
    assert interactions[1] == Q(3, 2)


def main() -> int:
    check_all_loopless_four_vertex_supports()
    check_nonuniform_circuit_atoms()
    check_pure_order_and_dag_realizations()
    check_self_loop_order_one()
    print("BRC feedback circuit atoms checker: PASS")
    print("interaction_girth_equals_directed_girth=PASS")
    print("primitive_atom_closure=PASS")
    print("prime_valuation_holonomy=PASS")
    print("pure_order_DAG_realizations=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
