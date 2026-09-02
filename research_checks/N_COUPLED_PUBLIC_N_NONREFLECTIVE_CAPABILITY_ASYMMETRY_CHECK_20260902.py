#!/usr/bin/env python3
"""Deterministic finite checks for the G_trace-lin negative boundary.

The symbolic theorem is proved in the research return.  This checker verifies:
- the maximal-minor CRT-support identity over a bounded exact matrix envelope;
- direct-sum and tensor presentation compilers on finite samples;
- the N=15 sequential linear-use witness;
- that the frozen pre-readout handle vocabulary contains no extensional reflection primitive.
"""
from __future__ import annotations

from itertools import combinations, product
from math import gcd

FORBIDDEN = {
    "COPY_HANDLE",
    "REPLAY_HANDLE",
    "HANDLE_EQUALITY",
    "ENUMERATE_ELEMENTS",
    "MEMBERSHIP_QUERY",
    "QUOTIENT_EQUALITY_QUERY",
    "STANDARD_BASIS_PROBE",
    "ARBITRARY_ELEMENT_EVALUATION",
    "CARDINALITY_QUERY",
    "PRESENTATION_QUERY",
}
PRE_READOUT = {
    "NEW_FREE(r)",
    "ATTACH_RELATION(H,v)",
    "DIRECT_SUM(H1,H2)",
    "TENSOR(H1,H2)",
}


def det_int(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    total = 0
    for j, a in enumerate(matrix[0]):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        total += ((-1) ** j) * a * det_int(minor)
    return total


def rank_mod(matrix: list[list[int]], p: int) -> int:
    if not matrix:
        return 0
    a = [[x % p for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(rows):
            if i == rank or a[i][col] % p == 0:
                continue
            factor = a[i][col] % p
            a[i] = [(a[i][j] - factor * a[rank][j]) % p for j in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def delta_maximal_minors(matrix: list[list[int]]) -> int:
    rows = len(matrix)
    if rows == 0:
        return 1
    cols = len(matrix[0]) if rows else 0
    if cols < rows:
        return 0
    delta = 0
    for chosen in combinations(range(cols), rows):
        square = [[matrix[i][j] for j in chosen] for i in range(rows)]
        delta = gcd(delta, abs(det_int(square)))
    return delta


def support_scalar(matrix: list[list[int]], n: int) -> int:
    return gcd(n, delta_maximal_minors(matrix))


def hidden_support_product(matrix: list[list[int]], p: int, q: int) -> int:
    rows = len(matrix)
    p_on = rows - rank_mod(matrix, p) > 0
    q_on = rows - rank_mod(matrix, q) > 0
    return (p if p_on else 1) * (q if q_on else 1)


def block_diag(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    ra = len(a)
    ca = len(a[0]) if ra else 0
    rb = len(b)
    cb = len(b[0]) if rb else 0
    out = [[0] * (ca + cb) for _ in range(ra + rb)]
    for i in range(ra):
        for j in range(ca):
            out[i][j] = a[i][j]
    for i in range(rb):
        for j in range(cb):
            out[ra + i][ca + j] = b[i][j]
    return out


def eye(n: int) -> list[list[int]]:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def kron(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    ra = len(a)
    ca = len(a[0]) if ra else 0
    rb = len(b)
    cb = len(b[0]) if rb else 0
    if ra == 0 or rb == 0:
        return []
    return [
        [a[i // rb][j // cb] * b[i % rb][j % cb] for j in range(ca * cb)]
        for i in range(ra * rb)
    ]


def hcat(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    assert len(a) == len(b)
    return [a[i] + b[i] for i in range(len(a))]


def tensor_presentation(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    r = len(a)
    u = len(b)
    return hcat(kron(a, eye(u)), kron(eye(r), b))


def check_support_identity() -> tuple[int, int]:
    semiprimes = [(2, 3), (2, 5), (3, 5), (3, 7), (5, 7)]
    shapes = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3)]
    matrix_cases = 0
    one_sided = 0
    for p, q in semiprimes:
        n = p * q
        for rows, cols in shapes:
            for values in product(range(3), repeat=rows * cols):
                matrix = [list(values[i * cols : (i + 1) * cols]) for i in range(rows)]
                got = support_scalar(matrix, n)
                expected = hidden_support_product(matrix, p, q)
                assert got == expected, (p, q, matrix, got, expected)
                p_on = rows - rank_mod(matrix, p) > 0
                q_on = rows - rank_mod(matrix, q) > 0
                one_sided += int(p_on ^ q_on)
                matrix_cases += 1
    return matrix_cases, one_sided


def check_composition() -> tuple[int, int]:
    samples = [
        [[1]],
        [[0]],
        [[1, 1]],
        [[1], [1]],
        [[1, 1], [1, 4]],
        [[1, 0], [0, 1]],
        [[2, 1], [1, 2]],
    ]
    tensor_checks = 0
    direct_sum_checks = 0
    for p in (2, 3, 5, 7):
        for a in samples:
            for b in samples:
                r = len(a)
                u = len(b)
                tensor = tensor_presentation(a, b)
                dim_a = r - rank_mod(a, p)
                dim_b = u - rank_mod(b, p)
                dim_tensor = r * u - rank_mod(tensor, p)
                assert dim_tensor == dim_a * dim_b
                tensor_checks += 1

                summed = block_diag(a, b)
                dim_sum = r + u - rank_mod(summed, p)
                assert dim_sum == dim_a + dim_b
                direct_sum_checks += 1
    return tensor_checks, direct_sum_checks


def check_sequential_witness() -> None:
    n = 15
    # NEW_FREE(2) has the 2x0 presentation. Two linear-use ATTACH_RELATION
    # calls add the public relation columns (1,1)^T and (1,4)^T.
    compiled = [[1, 1], [1, 4]]
    assert all(gcd(n, x) == 1 for row in compiled for x in row)
    assert delta_maximal_minors(compiled) == 3
    assert support_scalar(compiled, n) == 3
    assert 2 - rank_mod(compiled, 3) == 1
    assert 2 - rank_mod(compiled, 5) == 0


def main() -> int:
    assert not (PRE_READOUT & FORBIDDEN)
    matrix_cases, one_sided = check_support_identity()
    tensor_checks, direct_sum_checks = check_composition()
    check_sequential_witness()
    print(
        "PASS G_TRACE_LIN_INTENSIONAL_PRESENTATION_SCALARIZATION "
        f"matrix_cases={matrix_cases} one_sided={one_sided} "
        f"tensor_checks={tensor_checks} direct_sum_checks={direct_sum_checks} "
        "witness=N15_two_linear_ATTACH_Delta3_gcd3 forbidden_reflection_ops=10"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
