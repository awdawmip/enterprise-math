#!/usr/bin/env python3
"""Exact checker for RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY.

Pure-stdlib replay of the finite A3 carrier, signed-permutation frame action,
shell penetration model, alignment stabilizers, radial double-coset defects,
and A2 slice orientation witness.

When the Enterprise Math package is importable, the checker also cross-checks
the finite action through T7 `finite_symmetry`; the standalone proof checks do
not depend on that optional import.
"""
from __future__ import annotations

from itertools import permutations, product
from math import comb


Perm = tuple[int, int, int, int]
Vec = tuple[int, int, int, int]

G: tuple[Perm, ...] = tuple(permutations(range(4)))
E: Perm = (0, 1, 2, 3)
SWAP12: Perm = (1, 0, 2, 3)
SWAP23: Perm = (0, 2, 1, 3)


def parity(p: Perm) -> int:
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
    return 1 if inv % 2 == 0 else -1


def compose(p: Perm, q: Perm) -> Perm:
    """p after q."""
    return tuple(p[q[i]] for i in range(4))


def inverse(p: Perm) -> Perm:
    out = [0] * 4
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)  # type: ignore[return-value]


def r_act(p: Perm, x: Vec) -> Vec:
    """R_p = sgn(p) P_p, with (P_p x)_{p(i)}=x_i."""
    y = [0] * 4
    for i, value in enumerate(x):
        y[p[i]] = value
    s = parity(p)
    return tuple(s * value for value in y)  # type: ignore[return-value]


def radius(x: Vec) -> int:
    return max(abs(value) for value in x)


def ball(n: int) -> tuple[Vec, ...]:
    out: list[Vec] = []
    for x1, x2, x3 in product(range(-n, n + 1), repeat=3):
        x4 = -(x1 + x2 + x3)
        x = (x1, x2, x3, x4)
        if abs(x4) <= n:
            out.append(x)
    return tuple(sorted(out))


def ball_formula(n: int) -> int:
    return comb(4 * n + 3, 3) - 4 * comb(2 * n + 2, 3)


def shell(n: int) -> tuple[Vec, ...]:
    prev = set(ball(n - 1)) if n else set()
    return tuple(x for x in ball(n) if x not in prev)


def anchor(n: int) -> Vec:
    return (n, -n, 0, 0)


def rigid_anchor_2(n: int) -> Vec:
    return (n, 0, -n, 0)


def unreachable_anchor(n: int) -> Vec:
    return (n, n, -n, -n)


def stabilizer(x: Vec) -> tuple[Perm, ...]:
    return tuple(g for g in G if r_act(g, x) == x)


def orbit(x: Vec) -> frozenset[Vec]:
    return frozenset(r_act(g, x) for g in G)


def prefix_move(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    """Rotate exactly the outer `depth` shells, fix B_{n-depth} pointwise."""
    if not (0 <= depth <= n):
        raise ValueError("depth must lie in [0,n]")
    if radius(x) >= n - depth + 1:
        return r_act(g, x)
    return x


def double_cosets(H: tuple[Perm, ...]) -> tuple[tuple[Perm, ...], ...]:
    seen: set[Perm] = set()
    out: list[tuple[Perm, ...]] = []
    for g in sorted(G):
        if g in seen:
            continue
        current = {
            compose(compose(h_left, g), h_right)
            for h_left in H
            for h_right in H
        }
        seen.update(current)
        out.append(tuple(sorted(current)))
    return tuple(out)


def double_coset_product_table(
    cosets: tuple[tuple[Perm, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    label = {g: i for i, current in enumerate(cosets) for g in current}
    return tuple(
        tuple(
            tuple(sorted({label[compose(a, b)] for a in left for b in right}))
            for right in cosets
        )
        for left in cosets
    )


def det3(m: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def full_orientation_sign(g: Perm) -> int:
    basis = ((1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1))
    cols = []
    for b in basis:
        y = r_act(g, b)
        cols.append((y[0], y[0] + y[1], -y[3]))
    matrix = tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
    d = det3(matrix)  # type: ignore[arg-type]
    if d not in (-1, 1):
        raise AssertionError(f"unexpected full determinant {d}")
    return d


def slice_ball(n: int, zero_index: int = 3) -> tuple[Vec, ...]:
    return tuple(x for x in ball(n) if x[zero_index] == 0)


def restricted_orientation_sign_on_L4(g: Perm) -> int:
    b1 = (1, -1, 0, 0)
    b2 = (0, 1, -1, 0)
    v1, v2 = r_act(g, b1), r_act(g, b2)
    if v1[3] != 0 or v2[3] != 0:
        raise ValueError("g does not preserve L4")
    a1, b1c = v1[0], -v1[2]
    a2, b2c = v2[0], -v2[2]
    det = a1 * b2c - a2 * b1c
    if det not in (-1, 1):
        raise AssertionError(f"unexpected restricted determinant {det}")
    return det


def main() -> None:
    expected_balls = {0: 1, 1: 19, 2: 85, 3: 231}
    expected_shells = {1: 18, 2: 66, 3: 146}
    for n, expected in expected_balls.items():
        B = ball(n)
        assert len(B) == expected == ball_formula(n)
        assert all(sum(x) == 0 and radius(x) <= n for x in B)
        for g in G:
            assert {r_act(g, x) for x in B} == set(B)
    for n, expected in expected_shells.items():
        assert len(shell(n)) == expected == 16 * n * n + 2

    signatures = {tuple(r_act(g, x) for x in ball(1)) for g in G}
    assert len(signatures) == 24
    assert all(full_orientation_sign(g) == 1 for g in G)
    for p in G:
        for q in G:
            for x in ball(1):
                assert r_act(p, r_act(q, x)) == r_act(compose(p, q), x)

    t7_crosscheck = "SKIPPED_STANDALONE"
    try:
        from enterprise_math.finite_symmetry import (
            orbit as t7_orbit,
            stabilizer as t7_stabilizer,
            validate_finite_group_action,
        )
    except ModuleNotFoundError:
        pass
    else:
        B2 = ball(2)
        actions = {g: {x: r_act(g, x) for x in B2} for g in G}
        validate_finite_group_action(B2, actions)
        assert frozenset(t7_orbit(B2, actions, anchor(2))) == orbit(anchor(2))
        assert set(t7_stabilizer(B2, actions, anchor(2))) == set(stabilizer(anchor(2)))
        t7_crosscheck = "PASS"

    H = stabilizer(anchor(2))
    assert set(H) == {E, SWAP12}
    assert len(orbit(anchor(2))) == 12
    assert len(orbit(unreachable_anchor(2))) == 6
    assert orbit(anchor(2)).isdisjoint(orbit(unreachable_anchor(2)))
    H2 = set(stabilizer(rigid_anchor_2(2)))
    assert set(H) & H2 == {E}

    for n in (2, 3):
        for g in G:
            for x in ball(n - 1):
                assert prefix_move(n, 1, g, x) == x
    payload = (1, 0, -1, 0)
    moved_payload = prefix_move(2, 2, SWAP12, payload)
    assert moved_payload == (0, -1, 1, 0)
    assert moved_payload != payload
    assert prefix_move(2, 2, SWAP12, (0, 0, 0, 0)) == (0, 0, 0, 0)

    assert r_act(E, anchor(2)) == anchor(2)
    assert r_act(SWAP12, anchor(2)) == anchor(2)
    assert prefix_move(2, 1, E, payload) == prefix_move(2, 1, SWAP12, payload)
    raw_depth2 = {prefix_move(2, 2, h, payload) for h in H}
    assert raw_depth2 == {payload, moved_payload}

    cosets = double_cosets(H)
    assert [len(c) for c in cosets] == [2, 2, 4, 4, 4, 4, 4]
    expected_reps = [
        (0, 1, 2, 3),
        (0, 1, 3, 2),
        (0, 2, 1, 3),
        (0, 2, 3, 1),
        (0, 3, 1, 2),
        (0, 3, 2, 1),
        (2, 3, 0, 1),
    ]
    assert [c[0] for c in cosets] == expected_reps
    table = double_coset_product_table(cosets)
    assert table[2][2] == (0, 2)

    label = {g: i for i, current in enumerate(cosets) for g in current}
    g1, g2, g3 = E, SWAP23, E
    p1 = r_act(inverse(g1), anchor(1))
    p2 = r_act(inverse(g2), anchor(2))
    p3 = r_act(inverse(g3), anchor(3))
    assert p1 == anchor(1)
    assert p2 == (-2, 0, 2, 0)
    assert p3 == anchor(3)
    d12 = label[compose(g1, inverse(g2))]
    d23 = label[compose(g2, inverse(g3))]
    d13 = label[compose(g1, inverse(g3))]
    assert (d12, d23, d13) == (2, 2, 0)
    assert d13 in table[d12][d23] and table[d12][d23] == (0, 2)

    for n in (1, 2, 3):
        L = slice_ball(n, 3)
        assert len(L) == 1 + 3 * n * (n + 1)
        prev = set(slice_ball(n - 1, 3)) if n > 0 else set()
        assert len(set(L) - prev) == 6 * n
    assert all(r_act(SWAP12, x)[3] == 0 for x in slice_ball(3, 3))
    assert restricted_orientation_sign_on_L4(SWAP12) == -1

    print("A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_CHECK=PASS")
    print(f"T7_CROSSCHECK={t7_crosscheck}")
    print("BALL_COUNTS=1,19,85,231")
    print("SHELL_COUNTS=18,66,146")
    print("ANCHOR_ORBIT=12;ANCHOR_STABILIZER=2")
    print("UNREACHABLE_ORBIT=6")
    print("DEPTH1_SHIELDING=PASS;MIN_NONTRIVIAL_COUPLED_DEPTH=2")
    print("DOUBLE_COSET_COUNT=7;C2_TIMES_C2={C0,C2}")
    print("THREE_RADIUS_DEFECTS=C2,C2;ENDPOINT=C0")
    print("A2_SLICE_COUNTS=7,19,37;H_ORIENTATION_SIGN=-1")


if __name__ == "__main__":
    main()
