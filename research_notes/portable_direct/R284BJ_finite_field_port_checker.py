#!/usr/bin/env python3
"""R284BJ exact finite-field star-Port observer checks (stdlib only)."""
import hashlib
import itertools
import json
import math
import random


def is_prime_trial(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    divisor = 3
    while divisor * divisor <= x:
        if x % divisor == 0:
            return False
        divisor += 2
    return True


def next_prime_strict(bound):
    candidate = max(2, bound + 1)
    if candidate > 2 and candidate % 2 == 0:
        candidate += 1
    while not is_prime_trial(candidate):
        candidate += 2
    return candidate


def determinant_mod(matrix, p):
    """Gaussian elimination over F_p, accounting for row-swap sign."""
    rows = [list(row) for row in matrix]
    n = len(rows)
    result = 1
    for col in range(n):
        pivot_row = next(
            (i for i in range(col, n) if rows[i][col] % p != 0), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != col:
            rows[pivot_row], rows[col] = rows[col], rows[pivot_row]
            result = -result
        pivot = rows[col][col] % p
        result = result * pivot % p
        inverse = pow(pivot, -1, p)
        for row in range(col + 1, n):
            factor = rows[row][col] * inverse % p
            for j in range(col + 1, n):
                rows[row][j] = (rows[row][j] - factor * rows[col][j]) % p
            rows[row][col] = 0
    return result % p


def exact_fixture(n, H, delta, seed):
    N = H ** (n * n)
    pairs = N * (N - 1) // 2
    coefficient_guard = 2 * math.factorial(n) * (H + 2) ** n
    failure_guard = 4 * (n - 1) * (4 * delta + 1) * pairs
    p = next_prime_strict(max(coefficient_guard, failure_guard))
    rng = random.Random(seed)
    diagonals = [rng.randrange(p) for _ in range(n)]
    ports = [rng.randrange(p) for _ in range(n - 1)]
    residues = []
    for C in itertools.product(range(1, H + 1), repeat=n * n):
        matrix = [
            [
                (
                    (diagonals[i] if i == j else 0)
                    - C[i * n + j]
                    - (ports[j - 1] if i == 0 and j > 0 else 0)
                ) % p
                for j in range(n)
            ]
            for i in range(n)
        ]
        residues.append(determinant_mod(matrix, p))
    residues.sort()
    cyclic_gaps = [
        v - u for u, v in zip(residues, residues[1:])
    ] + [p + residues[0] - residues[-1]]
    min_gap = min(cyclic_gaps)
    assert len(residues) == N
    assert min_gap > 2 * delta
    payload = json.dumps(residues, separators=(",", ":")).encode("utf-8")
    return {
        "n": n,
        "H": H,
        "integer_noise_delta": delta,
        "seed": seed,
        "p": p,
        "field_bits": p.bit_length(),
        "cardinality_lower_bound_bits": (N - 1).bit_length(),
        "diagonal_controls": diagonals,
        "directed_star_controls": ports,
        "matrices_exhausted": N,
        "minimum_cyclic_residue_gap": min_gap,
        "necessary_gap_for_error_balls": 2 * delta + 1,
        "all_error_balls_disjoint": True,
        "sorted_residues_sha256": hashlib.sha256(payload).hexdigest(),
    }


if __name__ == "__main__":
    results = [
        exact_fixture(n=3, H=2, delta=3, seed=20261120),
        exact_fixture(n=4, H=2, delta=3, seed=20261120),
    ]
    print(json.dumps({
        "schema": "R284BJ_EXACT_MODULAR_PORT_CHECK_V1",
        "status": "PASS",
        "fixtures": results,
        "coverage_statement": (
            "Every C in {1,2}^{3x3} and {1,2}^{4x4}, "
            "for each listed fixed control tuple; exact modular arithmetic"
        ),
        "independent_review": "NOT_REVIEWED",
    }, indent=2, ensure_ascii=False))
