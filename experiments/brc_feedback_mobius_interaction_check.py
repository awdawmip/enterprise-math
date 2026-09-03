#!/usr/bin/env python3
"""Exact all-orders feedback interaction checks for stable BRC event kernels."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

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


def subset_zeta_table(kernel: Matrix) -> dict[int, Q]:
    n = len(kernel)
    zeta = {0: Q(1)}
    for mask in range(1, 1 << n):
        p = principal(kernel, mask)
        det = determinant(sub(eye(len(p)), p))
        assert det > 0
        zeta[mask] = 1 / det
    return zeta


def mobius_interactions(zeta: dict[int, Q], n: int) -> dict[int, Q]:
    out: dict[int, Q] = {}
    for mask in range(1, 1 << n):
        factor = Q(1)
        submask = mask
        while True:
            parity = (mask.bit_count() - submask.bit_count()) & 1
            if parity:
                factor /= zeta[submask]
            else:
                factor *= zeta[submask]
            if submask == 0:
                break
            submask = (submask - 1) & mask
        out[mask] = factor
    return out


def support_has_closed_walk_cover(kernel: Matrix, mask: int) -> bool:
    idx = indices(mask, len(kernel))
    if len(idx) == 1:
        i = idx[0]
        return kernel[i][i] > 0
    allowed = set(idx)
    for source in idx:
        reached = {source}
        changed = True
        while changed:
            changed = False
            for i in tuple(reached):
                for j in idx:
                    if j not in reached and kernel[i][j] > 0:
                        reached.add(j)
                        changed = True
        if reached != allowed:
            return False
    return True


def all_submasks(mask: int):
    submask = mask
    while True:
        yield submask
        if submask == 0:
            break
        submask = (submask - 1) & mask


def check_kernel(kernel: Matrix) -> tuple[int, int, int]:
    n = len(kernel)
    stable, _ = stable_star(kernel)
    assert stable
    zeta = subset_zeta_table(kernel)
    interactions = mobius_interactions(zeta, n)

    positive_interactions = 0
    for mask, factor in interactions.items():
        assert factor >= 1
        expected_positive = support_has_closed_walk_cover(kernel, mask)
        assert (factor > 1) == expected_positive
        positive_interactions += int(factor > 1)

    # Exact reconstruction: Z(A)=prod_{nonempty T subseteq A} J_T.
    for mask in range(1 << n):
        rebuilt = Q(1)
        for submask in all_submasks(mask):
            if submask:
                rebuilt *= interactions[submask]
        assert rebuilt == zeta[mask]

    # Conditional marginal factor equals product of interactions enabled when e arrives.
    marginal_checks = 0
    for e in range(n):
        bit = 1 << e
        others = ((1 << n) - 1) ^ bit
        a = others
        while True:
            marginal = zeta[a | bit] / zeta[a]
            rebuilt = Q(1)
            for t in all_submasks(a | bit):
                if t and (t & bit):
                    rebuilt *= interactions[t]
            assert marginal == rebuilt
            a = (a - 1) & others if a else -1
            marginal_checks += 1
            if a == -1:
                break

    # Supermodularity/increasing marginal risk: A subset B, e notin B.
    supermod_checks = 0
    for e in range(n):
        bit = 1 << e
        other_vertices = [i for i in range(n) if i != e]
        # state 0=neither, 1=B only, 2=A and B.
        for states in product(range(3), repeat=len(other_vertices)):
            a = 0
            b = 0
            for vertex, state in zip(other_vertices, states):
                if state == 2:
                    a |= 1 << vertex
                    b |= 1 << vertex
                elif state == 1:
                    b |= 1 << vertex
            marginal_a = zeta[a | bit] / zeta[a]
            marginal_b = zeta[b | bit] / zeta[b]
            assert marginal_a <= marginal_b

            # Normalized conditional self-return x=delta*kappa = 1-1/M.
            x_a = 1 - 1 / marginal_a
            x_b = 1 - 1 / marginal_b
            assert Q(0) <= x_a <= x_b < 1
            # Critical multiplier 1/x can only shrink; x=0 means infinity.
            if x_a > 0:
                assert 1 / x_b <= 1 / x_a
            supermod_checks += 1

    # Pair closed formula and strictness criterion.
    pair_checks = 0
    for e in range(n):
        for f in range(e + 1, n):
            emask, fmask = 1 << e, 1 << f
            pair = emask | fmask
            a = kernel[e][e]
            b = kernel[e][f]
            c = kernel[f][e]
            d = kernel[f][f]
            det_pair = (1 - a) * (1 - d) - b * c
            expected = ((1 - a) * (1 - d)) / det_pair
            assert interactions[pair] == expected
            assert (expected > 1) == (b * c > 0)

            # Interaction = conditional marginal amplification.
            base_f_marginal = zeta[fmask]
            conditioned_f_marginal = zeta[pair] / zeta[emask]
            assert interactions[pair] == conditioned_f_marginal / base_f_marginal
            pair_checks += 1

    # Disjoint group interaction equals product of all crossing J_T.
    for a in range(1, 1 << n):
        for b in range(1, 1 << n):
            if a & b:
                continue
            union = a | b
            group_factor = zeta[union] / (zeta[a] * zeta[b])
            crossing = Q(1)
            for t in all_submasks(union):
                if t and (t & a) and (t & b):
                    crossing *= interactions[t]
            assert group_factor == crossing >= 1
            # Same factor is B's conditional risk amplification after A.
            conditional_b = zeta[union] / zeta[a]
            direct_b = zeta[b]
            assert group_factor == conditional_b / direct_b

    return positive_interactions, marginal_checks, supermod_checks + pair_checks


def check_exhaustive_three_event_kernels() -> None:
    values = [Q(0), Q(1, 10), Q(1, 5)]
    kernels = 0
    positive_interactions = 0
    marginal_checks = 0
    inequality_checks = 0
    for entries in product(values, repeat=9):
        kernel = [list(entries[:3]), list(entries[3:6]), list(entries[6:])]
        # Every row sum is <=3/5, so every sampled kernel is stable.
        assert stable_star(kernel)[0]
        p, m, s = check_kernel(kernel)
        positive_interactions += p
        marginal_checks += m
        inequality_checks += s
        kernels += 1
    assert kernels == 3**9 == 19683
    print(f"3x3 kernels={kernels}")
    print(f"positive interaction instances={positive_interactions}")
    print(f"marginal reconstructions={marginal_checks}")
    print(f"supermod/pair inequalities={inequality_checks}")


def check_pure_third_order_event_cycle() -> None:
    x = y = z = Q(1, 2)
    kernel = [
        [Q(0), x, Q(0)],
        [Q(0), Q(0), y],
        [z, Q(0), Q(0)],
    ]
    zeta = subset_zeta_table(kernel)
    interactions = mobius_interactions(zeta, 3)
    for mask in [1, 2, 4, 3, 5, 6]:
        assert zeta[mask] == 1
        assert interactions[mask] == 1
    assert determinant(sub(eye(3), kernel)) == 1 - x * y * z == Q(7, 8)
    assert zeta[7] == interactions[7] == Q(8, 7)


def full_feedback_kernel(star: Matrix, events: list[tuple[int, int, Q]]) -> Matrix:
    return [
        [star[r[1]][s[0]] * s[2] for s in events]
        for r in events
    ]


def check_six_state_dag_realization() -> None:
    background = [[Q(0) for _ in range(6)] for _ in range(6)]
    u = v = w = Q(1, 2)
    background[1][2] = u
    background[3][4] = v
    background[5][0] = w
    stable, star = stable_star(background)
    assert stable and star is not None
    events = [(0, 1, Q(1)), (2, 3, Q(1)), (4, 5, Q(1))]
    kernel = full_feedback_kernel(star, events)
    assert kernel == [
        [Q(0), u, Q(0)],
        [Q(0), Q(0), v],
        [w, Q(0), Q(0)],
    ]
    zeta = subset_zeta_table(kernel)
    interactions = mobius_interactions(zeta, 3)
    assert all(interactions[mask] == 1 for mask in [1, 2, 4, 3, 5, 6])
    assert interactions[7] == Q(8, 7)


def main() -> int:
    check_exhaustive_three_event_kernels()
    check_pure_third_order_event_cycle()
    check_six_state_dag_realization()
    print("BRC feedback Mobius interaction checker: PASS")
    print("pure_third_order_synergy=PASS")
    print("six_state_DAG_realization=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
