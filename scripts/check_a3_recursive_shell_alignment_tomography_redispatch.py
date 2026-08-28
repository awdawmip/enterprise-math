#!/usr/bin/env python3
r"""Exact redispatch checker for RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY.

This checker validates the finite S4/H instance of the universal radial-relation
coherence theorem proved in the redispatch return:
- double-coset support multiplication is associative;
- it is the exact relation image of pair-groupoid composition on H\G;
- single-valued composition fails for H={e,(12)};
- the full 7-class boolean table and integral orbital structure constants agree.
"""
from __future__ import annotations

import json
from itertools import permutations
from pathlib import Path

Perm = tuple[int, int, int, int]
G: tuple[Perm, ...] = tuple(permutations(range(4)))
E: Perm = (0, 1, 2, 3)
SWAP12: Perm = (1, 0, 2, 3)
H: tuple[Perm, ...] = (E, SWAP12)

EXPECTED_REPS: tuple[Perm, ...] = (
    (0, 1, 2, 3),
    (0, 1, 3, 2),
    (0, 2, 1, 3),
    (0, 2, 3, 1),
    (0, 3, 1, 2),
    (0, 3, 2, 1),
    (2, 3, 0, 1),
)

EXPECTED_SUPPORT_TABLE: tuple[tuple[tuple[int, ...], ...], ...] = (
    ((0,), (1,), (2,), (3,), (4,), (5,), (6,)),
    ((1,), (0,), (4,), (5,), (2,), (3,), (6,)),
    ((2,), (3,), (0, 2), (1, 3), (5, 6), (4, 6), (4, 5)),
    ((3,), (2,), (5, 6), (4, 6), (0, 2), (1, 3), (4, 5)),
    ((4,), (5,), (1, 4), (0, 5), (3, 6), (2, 6), (2, 3)),
    ((5,), (4,), (3, 6), (2, 6), (1, 4), (0, 5), (2, 3)),
    ((6,), (6,), (3, 5), (2, 4), (3, 5), (2, 4), (0, 1)),
)

EXPECTED_INVOLUTION = (0, 1, 2, 4, 3, 5, 6)
EXPECTED_VALENCIES = (1, 1, 2, 2, 2, 2, 2)


def compose(p: Perm, q: Perm) -> Perm:
    """p after q."""
    return tuple(p[q[i]] for i in range(4))


def inverse(p: Perm) -> Perm:
    out = [0] * 4
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)  # type: ignore[return-value]


def double_cosets() -> tuple[tuple[Perm, ...], ...]:
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
    assert seen == set(G)
    return tuple(out)


def left_coset(g: Perm) -> frozenset[Perm]:
    return frozenset(compose(h, g) for h in H)


def left_cosets() -> tuple[frozenset[Perm], ...]:
    out: list[frozenset[Perm]] = []
    for g in sorted(G):
        current = left_coset(g)
        if current not in out:
            out.append(current)
    return tuple(out)


def support_table(
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


def star_sets(
    table: tuple[tuple[tuple[int, ...], ...], ...],
    left: frozenset[int],
    right: frozenset[int],
) -> frozenset[int]:
    out: set[int] = set()
    for i in left:
        for j in right:
            out.update(table[i][j])
    return frozenset(out)


def defect_class(
    A: frozenset[Perm],
    B: frozenset[Perm],
    label: dict[Perm, int],
) -> int:
    values = {
        label[compose(a, inverse(b))]
        for a in A
        for b in B
    }
    assert len(values) == 1
    return next(iter(values))


def orbital_structure_constants(
    omega: tuple[frozenset[Perm], ...],
    rel: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    p: list[list[list[int]]] = [[[0] * 7 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        for j in range(7):
            for k in range(7):
                counts: list[int] = []
                for a in range(len(omega)):
                    for c in range(len(omega)):
                        if rel[a][c] != k:
                            continue
                        counts.append(
                            sum(
                                1
                                for b in range(len(omega))
                                if rel[a][b] == i and rel[b][c] == j
                            )
                        )
                assert counts and len(set(counts)) == 1
                p[i][j][k] = counts[0]
    return tuple(tuple(tuple(row) for row in plane) for plane in p)


def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    n = len(A)
    return [
        [sum(A[i][t] * B[t][j] for t in range(n)) for j in range(n)]
        for i in range(n)
    ]


def matrix_add_scaled(
    matrices: list[list[list[int]]], coeffs: tuple[int, ...]
) -> list[list[int]]:
    n = len(matrices[0])
    return [
        [
            sum(coeffs[k] * matrices[k][i][j] for k in range(len(matrices)))
            for j in range(n)
        ]
        for i in range(n)
    ]


def main() -> None:
    cosets = double_cosets()
    assert len(cosets) == 7
    assert tuple(c[0] for c in cosets) == EXPECTED_REPS
    assert tuple(len(c) for c in cosets) == (2, 2, 4, 4, 4, 4, 4)

    table = support_table(cosets)
    assert table == EXPECTED_SUPPORT_TABLE

    for i in range(7):
        assert table[0][i] == (i,)
        assert table[i][0] == (i,)
    for i in range(7):
        for j in range(7):
            for k in range(7):
                lhs = star_sets(table, frozenset(table[i][j]), frozenset({k}))
                rhs = star_sets(table, frozenset({i}), frozenset(table[j][k]))
                assert lhs == rhs

    inv_classes: list[int] = []
    for current in cosets:
        invset = {inverse(g) for g in current}
        inv_classes.append(
            next(i for i, other in enumerate(cosets) if set(other) == invset)
        )
    assert tuple(inv_classes) == EXPECTED_INVOLUTION
    for i in range(7):
        for j in range(7):
            lhs = {inv_classes[k] for k in table[i][j]}
            rhs = set(table[inv_classes[j]][inv_classes[i]])
            assert lhs == rhs

    omega = left_cosets()
    assert len(omega) == 12
    label = {g: i for i, current in enumerate(cosets) for g in current}
    rel = tuple(
        tuple(defect_class(A, B, label) for B in omega)
        for A in omega
    )
    valencies = tuple(sum(1 for x in rel[0] if x == i) for i in range(7))
    assert valencies == EXPECTED_VALENCIES

    realized = {(i, j): set() for i in range(7) for j in range(7)}
    triple_count = 0
    for a in range(12):
        for b in range(12):
            for c in range(12):
                i, j, k = rel[a][b], rel[b][c], rel[a][c]
                assert k in table[i][j]
                realized[(i, j)].add(k)
                triple_count += 1
    for i in range(7):
        for j in range(7):
            assert realized[(i, j)] == set(table[i][j])
    assert triple_count == 12 ** 3

    c22_endpoints = {
        rel[a][c]
        for a in range(12)
        for b in range(12)
        for c in range(12)
        if rel[a][b] == 2 and rel[b][c] == 2
    }
    assert c22_endpoints == {0, 2}
    c22_counts = {
        k: sum(
            1
            for a in range(12)
            for b in range(12)
            for c in range(12)
            if rel[a][b] == 2 and rel[b][c] == 2 and rel[a][c] == k
        )
        for k in (0, 2)
    }
    assert c22_counts == {0: 24, 2: 24}

    swap23: Perm = (0, 2, 1, 3)
    conjugate = compose(compose(swap23, SWAP12), inverse(swap23))
    assert conjugate not in H

    p = orbital_structure_constants(omega, rel)
    for i in range(7):
        for j in range(7):
            assert {k for k, value in enumerate(p[i][j]) if value} == set(table[i][j])

    adjacency = [
        [[1 if rel[a][b] == i else 0 for b in range(12)] for a in range(12)]
        for i in range(7)
    ]
    for i in range(7):
        for j in range(7):
            lhs = matrix_multiply(adjacency[i], adjacency[j])
            rhs = matrix_add_scaled(adjacency, p[i][j])
            assert lhs == rhs

    for i in range(7):
        for j in range(7):
            for k in range(7):
                left_coeff = [
                    sum(p[i][j][m] * p[m][k][ell] for m in range(7))
                    for ell in range(7)
                ]
                right_coeff = [
                    sum(p[j][k][m] * p[i][m][ell] for m in range(7))
                    for ell in range(7)
                ]
                assert left_coeff == right_coeff

    certificate = {
        "schema": "A3_RADIAL_RELATION_COHERENCE_CERTIFICATE_V1",
        "group": "S4",
        "stabilizer": ["e", "(12)"],
        "left_coset_object_count": 12,
        "double_coset_count": 7,
        "double_coset_sizes": [2, 2, 4, 4, 4, 4, 4],
        "representatives": ["e", "(34)", "(23)", "(234)", "(243)", "(24)", "(13)(24)"],
        "involution": list(EXPECTED_INVOLUTION),
        "valencies": list(EXPECTED_VALENCIES),
        "support_table": [[list(cell) for cell in row] for row in table],
        "structure_constants": [[list(coeffs) for coeffs in plane] for plane in p],
        "c2_c2_endpoint_triple_counts": {str(k): v for k, v in c22_counts.items()},
        "associativity_triples_checked": 7 ** 3,
        "pair_groupoid_triples_checked": triple_count,
        "weighted_associativity_triples_checked": 7 ** 3,
        "nonnormality_witness": "(23)(12)(23)=(13) notin H",
        "verdict": "PASS",
    }

    out_path = Path(__file__).resolve().parents[1] / (
        "research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_REDISPATCH/"
        "s4_h_orbital_certificate.json"
    )
    if out_path.parent.exists() and out_path.exists():
        existing = json.loads(out_path.read_text(encoding="utf-8"))
        assert existing == certificate

    print("A3_RADIAL_RELATION_COHERENCE_CHECK=PASS")
    print("DOUBLE_COSET_SUPPORT_ASSOCIATIVITY=343/343")
    print("PAIR_GROUPOID_TRIPLES=1728/1728")
    print("WEIGHTED_ORBITAL_ASSOCIATIVITY=343/343")
    print("C2*C2={C0,C2};ENDPOINT_TRIPLES=C0:24,C2:24")
    print("SINGLE_VALUED_DEFECT_COMPOSITION=REFUTED_FOR_NONNORMAL_H")
    print("EXACT_RELATIONAL_LIFT=PAIR_GROUPOID_ON_12_LEFT_COSETS")


if __name__ == "__main__":
    main()
