#!/usr/bin/env python3
"""Exact regression for RS-SEED6-DECORATED-CARRIER-PAIR-STRATIFIED-GROWTH.

Finite factorization is used only to build/check small valuation profiles.
The mathematical claims in the return are symbolic; this script is a regression
certificate, not a factor-recovery benchmark.
"""

from __future__ import annotations

from functools import reduce
from itertools import combinations
from math import gcd


def gcd_all(values):
    vals = [abs(v) for v in values if v]
    return reduce(gcd, vals, 0)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    q = 2
    while q * q <= n:
        if n % q == 0:
            return False
        q += 1
    return True


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def fresh_primes(ab: int, count: int = 2) -> list[int]:
    out = []
    n = 2
    while len(out) < count:
        if is_prime(n) and ab % n:
            out.append(n)
        n += 1
    return out


def valuation_profile(a: int, b: int) -> list[tuple[int, int, int]]:
    fa, fb = factor(a), factor(b)
    return [(p, fa.get(p, 0), fb.get(p, 0))
            for p in sorted(set(fa) | set(fb))]


def stratum(a: int, b: int) -> str:
    if a == b:
        return "EQUALITY"
    fa, fb = factor(a), factor(b)
    if gcd(a, b) > 1:
        return "OVERLAP_DISTINCT"
    if len(fa) == len(fb) == 1:
        (_, ea), = fa.items()
        (_, eb), = fb.items()
        if ea == eb == 1:
            return "DISTINCT_PRIME_PAIR"
        return "COPRIME_PRIME_POWER_THICK"
    return "COPRIME_MULTISUPPORT"


def triangle_matrix_from_profile(a: int, b: int, r: int) -> list[list[int]]:
    cols = [(alpha + beta, alpha, beta)
            for _, alpha, beta in valuation_profile(a, b)]
    cols.append((0, 1, 1))
    return [list(row) for row in zip(*cols)]


def direct_triangle_matrix(a: int, b: int, r: int) -> tuple[list[int], list[list[int]]]:
    nums = [a * b, a * r, b * r]
    primes = sorted(set(factor(a * b)) | {r})
    matrix = []
    for n in nums:
        fn = factor(n)
        matrix.append([fn.get(p, 0) for p in primes])
    return primes, matrix


def normalized_profile_matrix(a: int, b: int, r: int) -> tuple[list[int], list[list[int]]]:
    prof = valuation_profile(a, b)
    cols_by_prime = {p: (alpha + beta, alpha, beta)
                     for p, alpha, beta in prof}
    cols_by_prime[r] = (0, 1, 1)
    primes = sorted(cols_by_prime)
    return primes, [[cols_by_prime[p][row] for p in primes] for row in range(3)]


def det2(c1, c2, i, j):
    return c1[i] * c2[j] - c1[j] * c2[i]


def det3(c1, c2, c3):
    return (
        c1[0] * (c2[1] * c3[2] - c3[1] * c2[2])
        - c2[0] * (c1[1] * c3[2] - c3[1] * c1[2])
        + c3[0] * (c1[1] * c2[2] - c2[1] * c1[2])
    )


def smith_from_minors(matrix: list[list[int]]) -> tuple[int, tuple[int, int, int]]:
    cols = [tuple(matrix[i][j] for i in range(3))
            for j in range(len(matrix[0]))]
    d1 = gcd_all(x for row in matrix for x in row)
    minors2 = [
        det2(c1, c2, i, j)
        for c1, c2 in combinations(cols, 2)
        for i, j in combinations(range(3), 2)
    ]
    d2 = gcd_all(minors2)
    minors3 = [det3(*triple) for triple in combinations(cols, 3)]
    d3 = gcd_all(minors3)
    if d3:
        return 3, (d1, d2 // d1, d3 // d2)
    if d2:
        return 2, (d1, d2 // d1, 0)
    return 1, (d1, 0, 0)


def predicted_smith(a: int, b: int) -> tuple[int, tuple[int, int, int]]:
    vecs = [(alpha, beta) for _, alpha, beta in valuation_profile(a, b)]
    dets = [x1 * y2 - y1 * x2
            for (x1, y1), (x2, y2) in combinations(vecs, 2)]
    rho = 2 if any(dets) else 1
    h = gcd_all(
        [v for x, y in vecs for v in (x + y, x - y)] + dets
    )
    if rho == 1:
        return 2, (1, h, 0)
    D = gcd_all(dets)
    assert D > 0 and (2 * D) % h == 0
    return 3, (1, h, 2 * D // h)


def delta_T(a: int, b: int, r: int) -> int:
    x, y, z = a * b, a * r, b * r
    num = (gcd(x, y) * gcd(x, z) * gcd(y, z)) ** 2
    den = x * y * z
    assert num % den == 0
    return num // den


def common_excess(a: int, b: int) -> tuple[int, int, int]:
    d = gcd(a, b)
    A, B = a // d, b // d
    assert gcd(A, B) == 1
    return d, A, B


def pairing_states(a: int, b: int, p: int, q: int):
    return {
        tuple(sorted((a * b, p * q))),
        tuple(sorted((a * p, b * q))),
        tuple(sorted((a * q, b * p))),
    }


def check_pairing(a: int, b: int, p: int, q: int):
    assert p != q and gcd(p * q, a * b) == 1
    d = gcd(a, b)
    assert gcd(a * b, p * q) == 1
    assert gcd(a * p, b * q) == d
    assert gcd(a * q, b * p) == d

    ap, aq, bp, bq = a * p, a * q, b * p, b * q
    assert ap * bq == aq * bp
    assert gcd(ap, aq) == a
    assert gcd(bp, bq) == b
    assert gcd(ap, bp) == p * d
    assert gcd(aq, bq) == q * d
    assert gcd(ap, bq) == d
    assert gcd(aq, bp) == d
    expected_states = 2 if a == b else 3
    assert len(pairing_states(a, b, p, q)) == expected_states


def run():
    stratum_counts: dict[str, int] = {}
    checked = 0
    rank2 = rank3 = 0

    for a in range(2, 81):
        for b in range(2, 81):
            p, q = fresh_primes(a * b, 2)
            r = p

            d = gcd(a, b)
            x, y, z = a * b, a * r, b * r
            assert gcd(x, y) == a
            assert gcd(x, z) == b
            assert gcd(y, z) == r * d
            assert x * y // gcd(x, y) == a * b * r
            assert x * z // gcd(x, z) == a * b * r
            assert y * z // gcd(y, z) == a * b * r // d
            assert delta_T(a, b, r) == d * d

            dc, A, B = common_excess(a, b)
            assert (dc * A, dc * B) == (a, b)
            assert dc == d

            assert direct_triangle_matrix(a, b, r) == normalized_profile_matrix(a, b, r)
            matrix = triangle_matrix_from_profile(a, b, r)
            actual = smith_from_minors(matrix)
            predicted = predicted_smith(a, b)
            assert actual == predicted, (a, b, actual, predicted, valuation_profile(a, b))
            if actual[0] == 2:
                rank2 += 1
            else:
                rank3 += 1

            check_pairing(a, b, p, q)
            s = stratum(a, b)
            stratum_counts[s] = stratum_counts.get(s, 0) + 1
            checked += 1

    assert delta_T(2, 6, 5) == delta_T(6, 10, 7) == 4
    assert valuation_profile(2, 6) != valuation_profile(6, 10)

    assert gcd(2, 6) == gcd(4, 6) == 2
    assert stratum(2, 6) == stratum(4, 6) == "OVERLAP_DISTINCT"
    assert predicted_smith(2, 6) != predicted_smith(4, 6)

    assert 3 * 4 == 2 * 6 == 12
    assert stratum(3, 4) == "COPRIME_PRIME_POWER_THICK"
    assert stratum(2, 6) == "OVERLAP_DISTINCT"
    assert 4 * 9 == 2 * 18 == 6 * 6 == 36
    assert stratum(4, 9) == "COPRIME_PRIME_POWER_THICK"
    assert stratum(2, 18) == "OVERLAP_DISTINCT"
    assert stratum(6, 6) == "EQUALITY"

    assert predicted_smith(2, 3) == (3, (1, 1, 2))
    assert predicted_smith(4, 9) == (3, (1, 2, 4))
    assert predicted_smith(3, 4) == (3, (1, 1, 4))
    assert predicted_smith(2, 6) == (3, (1, 1, 2))
    assert predicted_smith(4, 6) == (3, (1, 1, 4))
    assert predicted_smith(4, 8) == (2, (1, 1, 0))
    assert predicted_smith(6, 6) == (2, (1, 2, 0))

    print("PASS: DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH exact regression")
    print(f"ordered_pairs_checked={checked}")
    print(f"rank2_triangle_lattices={rank2}")
    print(f"rank3_triangle_lattices={rank3}")
    print("stratum_counts=" + repr(dict(sorted(stratum_counts.items()))))
    print("delta_counterexamples=PASS")
    print("scalar_decomposition_ambiguity=PASS")
    print("pairing_cell_gcd_and_equality_collapse=PASS")
    print("general_snf_formula=PASS")


if __name__ == "__main__":
    run()
