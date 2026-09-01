#!/usr/bin/env python3
"""Deterministic checks for the reflection-complete finite typed-module obstruction."""
from __future__ import annotations

from itertools import product
from math import gcd

def rank_mod(A, r):
    if not A:
        return 0
    M = [[x % r for x in row] for row in A]
    m, n = len(M), len(M[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((i for i in range(rank, m) if M[i][col] % r), None)
        if pivot is None:
            col += 1
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        inv = pow(M[rank][col], -1, r)
        M[rank] = [(inv*x) % r for x in M[rank]]
        for i in range(m):
            if i != rank and M[i][col] % r:
                c = M[i][col] % r
                M[i] = [(a - c*b) % r for a,b in zip(M[i], M[rank])]
        rank += 1
        col += 1
    return rank

def mat_vec(A, x, N):
    return tuple(sum(a*b for a,b in zip(row, x)) % N for row in A)

def image_set(A, N):
    n = len(A[0]) if A else 0
    return {mat_vec(A, x, N) for x in product(range(N), repeat=n)}

def quotient_cardinality(A, N):
    m = len(A)
    return (N ** m) // len(image_set(A, N))

def support_scalar_from_cardinality(card, N):
    return gcd(card, N)

def support_product_from_hidden_dims(A, p, q):
    m = len(A)
    dp = m - rank_mod(A, p)
    dq = m - rank_mod(A, q)
    s = 1
    if dp > 0:
        s *= p
    if dq > 0:
        s *= q
    return s, dp, dq

def recover_from_eval(A, N):
    """Reconstruct a total public linear-map evaluator by standard-basis probing."""
    n = len(A[0])
    cols = []
    for j in range(n):
        e = tuple(1 if i == j else 0 for i in range(n))
        cols.append(mat_vec(A, e, N))
    m = len(A)
    return [[cols[j][i] for j in range(n)] for i in range(m)]

def quotient_class_count_by_equality(A, N):
    """Count quotient classes using only ambient enumeration and the total equality oracle."""
    m = len(A)
    im = image_set(A, N)
    ambient = list(product(range(N), repeat=m))
    unseen = set(ambient)
    classes = 0
    while unseen:
        x = next(iter(unseen))
        cls = {
            y for y in unseen
            if tuple((y[i] - x[i]) % N for i in range(m)) in im
        }
        unseen.difference_update(cls)
        classes += 1
    return classes

def main():
    semiprimes = [(2,3),(2,5),(3,5),(3,7)]
    alphabet = range(5)
    matrix_cases = 0
    support_checks = 0
    one_sided = 0
    eval_recon_checks = 0
    equality_count_checks = 0
    relation_enumeration_checks = 0
    witness_relation_count = 0

    for p, q in semiprimes:
        N = p*q
        for entries in product(alphabet, repeat=4):
            A = [list(entries[:2]), list(entries[2:])]
            matrix_cases += 1
            card = quotient_cardinality(A, N)
            scalar = support_scalar_from_cardinality(card, N)
            expected, dp, dq = support_product_from_hidden_dims(A, p, q)
            assert scalar == expected, (N, A, card, scalar, expected, dp, dq)
            support_checks += 1
            if (dp > 0) ^ (dq > 0):
                one_sided += 1
                assert scalar in (p, q)
                assert 1 < scalar < N
            recovered = recover_from_eval(A, N)
            assert recovered == [[x % N for x in row] for row in A]
            eval_recon_checks += 1

    # Exact parent non-vacuity witness, now treated through a genuinely lazy quotient interface.
    N = 15
    p, q = 3, 5
    A = [[1,1],[1,4]]
    assert all(gcd(N, x) == 1 for row in A for x in row)
    card = quotient_cardinality(A, N)
    assert card == 3
    assert quotient_class_count_by_equality(A, N) == 3
    equality_count_checks += 1
    scalar = gcd(N, card)
    expected, dp, dq = support_product_from_hidden_dims(A, p, q)
    assert (dp, dq) == (1,0)
    assert scalar == expected == 3

    # Construct the generic "all extensional elements as generators" relation compiler
    # for the witness quotient, using only ambient enumeration + quotient equality.
    im = image_set(A, N)
    ambient = list(product(range(N), repeat=2))
    classes = []
    unseen = set(ambient)
    while unseen:
        x = min(unseen)
        cls = {y for y in unseen if tuple((y[i]-x[i]) % N for i in range(2)) in im}
        classes.append(min(cls))
        unseen.difference_update(cls)
    assert len(classes) == 3
    index = {}
    for i, rep in enumerate(classes):
        for y in ambient:
            if tuple((y[j]-rep[j]) % N for j in range(2)) in im:
                index[y] = i
    zero_class = index[(0,0)]
    rels = []
    for coeffs in product(range(N), repeat=len(classes)):
        acc = (0,0)
        for a, rep in zip(coeffs, classes):
            acc = tuple((acc[j] + a*rep[j]) % N for j in range(2))
        if index[acc] == zero_class:
            rels.append(coeffs)
    witness_relation_count = len(rels)
    assert witness_relation_count == (N ** len(classes)) // len(classes)
    assert (N ** len(classes)) // witness_relation_count == len(classes)
    relation_enumeration_checks += 1

    # Zero, full-support, and opposite one-sided 1x1 controls.
    controls = [
        (15, 3, 5, [[1]], 1),
        (15, 3, 5, [[0]], 15),
        (15, 3, 5, [[3]], 3),
        (15, 3, 5, [[5]], 5),
    ]
    for N,p,q,A,expected_card in controls:
        card = quotient_cardinality(A,N)
        assert card == expected_card
        scalar = gcd(N,card)
        expected, dp, dq = support_product_from_hidden_dims(A,p,q)
        assert scalar == expected
        support_checks += 1

    print(
        "PASS REFLECTION_COMPLETE_TYPED_MODULE_SCALARIZATION "
        f"matrix_cases={matrix_cases} support_checks={support_checks} "
        f"one_sided={one_sided} eval_reconstruction={eval_recon_checks} "
        f"equality_class_counts={equality_count_checks} "
        f"relation_enumeration={relation_enumeration_checks} "
        f"witness_relations={witness_relation_count} "
        "witness=N15_A[[1,1],[1,4]]_card3_gcd3"
    )

if __name__ == "__main__":
    main()
