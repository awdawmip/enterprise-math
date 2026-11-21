"""Exact finite models inspired by Alpoge's 2026-11-20 RH announcement.

This is our standalone method-harvest calculation, not a replay of the RH proof.
Only Python integer arithmetic is used. Run: python3 verify_finite_models.py
"""

from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
import json


def rank_mod(matrix, q):
    rows = [list(row) for row in matrix]
    pivot = 0
    for col in range(len(rows[0])):
        j = next((j for j in range(pivot, len(rows)) if rows[j][col] % q), None)
        if j is None:
            continue
        rows[pivot], rows[j] = rows[j], rows[pivot]
        inv = pow(rows[pivot][col] % q, -1, q)
        rows[pivot] = [(a * inv) % q for a in rows[pivot]]
        for j in range(len(rows)):
            if j != pivot:
                c = rows[j][col]
                rows[j] = [(a - c * b) % q for a, b in zip(rows[j], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def bilinear_counts(matrix, modulus):
    r, s = len(matrix), len(matrix[0])
    counts = [0] * modulus
    for a in product(range(modulus), repeat=r):
        coefficients = [sum(a[i] * matrix[i][j] for i in range(r)) for j in range(s)]
        for b in product(range(modulus), repeat=s):
            counts[sum(x * y for x, y in zip(coefficients, b)) % modulus] += 1
    return counts


def predicted_field_counts(matrix, q):
    k = len(matrix) + len(matrix[0])
    d = rank_mod(matrix, q)
    correction = q ** (k - d - 1)
    return [q ** (k - 1) + (q - 1) * correction] + [q ** (k - 1) - correction] * (q - 1)


def path_counts(modulus, length, allowed=None):
    allowed = tuple(range(modulus) if allowed is None else allowed)
    state = Counter({(u, 0): 1 for u in allowed})
    for _ in range(1, length):
        nxt = Counter()
        for (u, phase), count in state.items():
            for v in allowed:
                nxt[v, (phase + u * v) % modulus] += count
        state = nxt
    counts = [0] * modulus
    for (_, phase), count in state.items():
        counts[phase] += count
    return counts


def direct_path_counts(modulus, length, allowed):
    counts = [0] * modulus
    for x in product(allowed, repeat=length):
        phase = sum(a * b for a, b in zip(x, x[1:])) % modulus
        counts[phase] += 1
    return counts


def smith_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    first = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
    determinant = a * d - b * c
    if first == 0:
        return []
    if determinant == 0:
        return [first]
    return [first, abs(determinant) // first]


def smith_character_sum(matrix, modulus, h):
    ds = smith_2x2(matrix)
    result = modulus ** (4 - len(ds))
    for d in ds:
        result *= gcd(h * d, modulus)
    return result


def kernel_character_sum(matrix, modulus, h):
    count = sum(
        all(h * sum(a[i] * matrix[i][j] for i in range(2)) % modulus == 0 for j in range(2))
        for a in product(range(modulus), repeat=2)
    )
    return modulus ** 2 * count


def main():
    matrices_checked = 0
    assignments_checked = 0
    for q in (2, 3, 5):
        for entries in product(range(q), repeat=4):
            matrix = [entries[:2], entries[2:]]
            assert bilinear_counts(matrix, q) == predicted_field_counts(matrix, q)
            matrices_checked += 1
            assignments_checked += q ** 4

    path_cases = 0
    for q in (2, 3, 5, 7, 11):
        for k in range(2, 13):
            counts = path_counts(q, k)
            d = k // 2
            correction = q ** (k - d - 1)
            assert counts == [q ** (k - 1) + (q - 1) * correction] + [q ** (k - 1) - correction] * (q - 1)
            assert sum(counts) == q ** k
            path_cases += 1

    subset_cases = 0
    for mask in range(1 << 5):
        allowed = tuple(i for i in range(5) if (mask >> i) & 1)
        for k in range(1, 6):
            assert path_counts(5, k, allowed) == direct_path_counts(5, k, allowed)
            subset_cases += 1

    composite_cases = 0
    example_matrices = [
        [[0, 0], [0, 0]], [[1, 0], [1, 1]], [[1, 1], [1, 1]],
        [[2, 0], [0, 3]], [[2, 2], [2, 2]], [[2, 1], [4, 5]],
    ]
    for modulus in (4, 6, 8, 9, 10, 12):
        for matrix in example_matrices:
            sums = [smith_character_sum(matrix, modulus, h) for h in range(modulus)]
            assert sums == [kernel_character_sum(matrix, modulus, h) for h in range(modulus)]
            counts = bilinear_counts(matrix, modulus)
            assert sum(sums) == modulus * counts[0]
            composite_cases += 1

    path = [[1, 0], [1, 1]]
    cycle = [[1, 1], [1, 1]]
    comparison = []
    for name, matrix in (("four_vertex_path", path), ("four_cycle", cycle)):
        counts = bilinear_counts(matrix, 5)
        comparison.append({"model": name, "matrix": matrix, "rank_mod_5": rank_mod(matrix, 5),
                           "counts_by_phase": counts, "zero_phase_count": counts[0],
                           "residual_5N_minus_625": 5 * counts[0] - 625})

    subset_comparison = [{"allowed": list(a), "length": 3, "counts_by_phase": path_counts(5, 3, a)}
                         for a in ((0, 1), (1, 2))]
    report = {
        "status": "EXACT_FINITE_CHECKS_PASS",
        "arithmetic": "Python arbitrary-precision integers only; no floating-point inference",
        "scope": "finite toy models independently expanded from the announcement; not the RH proof",
        "all_2x2_field_matrices_checked": matrices_checked,
        "field_assignments_checked": assignments_checked,
        "path_cases_checked": path_cases,
        "all_subset_path_cases_checked": subset_cases,
        "composite_modulus_cases_checked": composite_cases,
        "path_cycle_comparison": comparison,
        "same_size_subset_comparison": subset_comparison,
    }
    output = Path(__file__).with_name("finite_model_results.json")
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
