#!/usr/bin/env python3
"""Exact checker for P000 P11 diagonal shared-leg Pythagorean fixed locus.

Standard-library only.  The bounded control b<=100000 was precommitted on
Issue #240 before inspection of the control outcome.  The census is regression
and falsification evidence only; the symbolic genus-one reduction is proved in
the accompanying Return.
"""
from __future__ import annotations

from collections import defaultdict
from functools import reduce
from math import gcd, isqrt

B_MAX = 100_000
HYP_MAX = 142_000  # > sqrt(2) * B_MAX

EXPECTED_BASE_TRIANGLES = 161_436
EXPECTED_SHARED_LEG_CANDIDATES = 700
EXPECTED_PARITY_VALID = 645

EXPECTED_PRIMITIVES = [
    (176, 57, 185, 105, 208, 56),
    (2720, 165, 2725, 1533, 2444, 2044),
    (3640, 270, 3650, 3128, 2346, 1254),
    (8640, 1475, 8765, 1547, 9996, 6996),
    (14640, 10679, 18121, 1785, 25256, 3536),
    (14760, 13570, 20050, 952, 28314, 714),
    (20592, 1015, 20617, 19065, 10168, 4448),
    (21222, 10600, 23722, 10528, 30030, 1410),
    (24050, 14280, 27970, 6072, 37846, 7654),
    (40200, 24662, 47162, 5712, 64610, 14450),
    (44200, 30690, 53810, 10808, 74106, 8106),
    (43885, 31680, 54125, 11557, 74676, 3924),
    (49728, 21571, 54205, 7755, 70876, 27068),
    (53650, 7992, 54242, 45080, 42042, 7242),
    (39770, 38640, 55450, 792, 78406, 806),
    (44642, 38640, 59042, 4080, 83182, 4402),
    (63280, 13662, 64738, 17360, 74958, 46482),
    (69930, 18352, 72298, 37720, 79818, 35178),
    (88560, 4631, 88681, 55335, 74984, 63104),
]


def build_hypotenuse_leg_map(max_h: int) -> dict[int, dict[int, int]]:
    """All nondegenerate integer right triangles with hypotenuse <= max_h.

    map[h][leg] = other_leg. Primitive Euclidean cores are unique; scaling
    supplies every integer right triangle.
    """
    out: dict[int, dict[int, int]] = defaultdict(dict)
    for m in range(2, isqrt(max_h) + 2):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a = m * m - n * n
            c = 2 * m * n
            h = m * m + n * n
            if h > max_h:
                continue
            for scale in range(1, max_h // h + 1):
                H = scale * h
                A = scale * a
                C = scale * c
                out[H][A] = C
                out[H][C] = A
    return out


def fixed_outer_roots(point: tuple[int, int, int, int, int, int]) -> list[int]:
    x, y, b, d, mu, nu = point
    p = x + y
    q = x - y
    assert p % 2 == d % 2
    assert b % 2 == d % 2
    assert q % 2 == d % 2
    assert mu % 2 == 0 and nu % 2 == 0

    roots: list[int] = []
    for delta in (p, b, q):
        roots.extend(((-d - delta) // 2, (-d + delta) // 2))
    roots.extend((-mu // 2, mu // 2, -nu // 2, nu // 2))
    for delta in (p, b, q):
        roots.extend(((d - delta) // 2, (d + delta) // 2))
    assert len(roots) == 16
    return roots


def root_gcd(point: tuple[int, int, int, int, int, int]) -> int:
    return reduce(gcd, (abs(v) for v in fixed_outer_roots(point)))


def verify_point(point: tuple[int, int, int, int, int, int]) -> None:
    x, y, b, d, mu, nu = point
    assert x > y > 0 and d > 0
    p, q = x + y, x - y

    assert x * x + y * y == b * b
    assert d * d + mu * mu == p * p
    assert d * d + nu * nu == q * q
    assert mu * mu - nu * nu == 4 * x * y

    assert p % 2 == q % 2 == b % 2 == d % 2
    assert mu % 2 == 0 and nu % 2 == 0

    assert d < q < b < p
    e = x * y // 2
    t_num = d * d - b * b
    assert (x * y) % 2 == 0 and t_num % 4 == 0
    t = t_num // 4
    assert 4 * (t - e) == -mu * mu
    assert 4 * (t + e) == -nu * nu
    assert t - e < t < t + e < 0

    roots = fixed_outer_roots(point)
    H = (-d, 0, d)
    T = (t - e, t, t + e)
    expected_cells = [
        (H[0], T[0]), (H[0], T[1]), (H[0], T[2]),
        (H[1], T[0]),                 (H[1], T[2]),
        (H[2], T[0]), (H[2], T[1]), (H[2], T[2]),
    ]
    pairs = [(roots[i], roots[i + 1]) for i in range(0, 16, 2)]
    for (r1, r2), (row_sum, col_prod) in zip(pairs, expected_cells):
        assert r1 + r2 == row_sum
        assert r1 * r2 == col_prod

    TT = mu + nu
    YY = 2 * TT * d
    assert TT != 0
    assert YY * YY == ((p + q) ** 2 - TT * TT) * (TT * TT - (p - q) ** 2)


def enumerate_control() -> tuple[list[tuple[tuple[int, ...], int]], int, int]:
    hyp_map = build_hypotenuse_leg_map(HYP_MAX)
    hits: list[tuple[tuple[int, ...], int]] = []
    base_count = 0
    shared_candidates = 0

    for m in range(2, isqrt(B_MAX) + 2):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a = m * m - n * n
            c = 2 * m * n
            h = m * m + n * n
            if h > B_MAX:
                continue
            for scale in range(1, B_MAX // h + 1):
                x = scale * max(a, c)
                y = scale * min(a, c)
                b = scale * h
                base_count += 1
                p, q = x + y, x - y

                common = set(hyp_map.get(p, ())).intersection(hyp_map.get(q, ()))
                for d in common:
                    if not (0 < d <= q):
                        continue
                    shared_candidates += 1
                    mu = hyp_map[p][d]
                    nu = hyp_map[q][d]

                    if (
                        (p - d) % 2
                        or (b - d) % 2
                        or (q - d) % 2
                        or mu % 2
                        or nu % 2
                    ):
                        continue

                    point = (x, y, b, d, mu, nu)
                    verify_point(point)
                    hits.append((point, root_gcd(point)))

    return hits, base_count, shared_candidates


def main() -> None:
    hits, base_count, shared_candidates = enumerate_control()
    primitives = sorted(
        (point for point, g in hits if g == 1),
        key=lambda point: (point[2], point),
    )

    assert base_count == EXPECTED_BASE_TRIANGLES, base_count
    assert shared_candidates == EXPECTED_SHARED_LEG_CANDIDATES, shared_candidates
    assert len(hits) == EXPECTED_PARITY_VALID, len(hits)
    assert primitives == EXPECTED_PRIMITIVES, primitives

    known = EXPECTED_PRIMITIVES[0]
    new = EXPECTED_PRIMITIVES[1]
    assert known == (176, 57, 185, 105, 208, 56)
    assert new == (2720, 165, 2725, 1533, 2444, 2044)
    assert root_gcd(known) == root_gcd(new) == 1
    assert new != known

    print(
        "PASS P000 P11 diagonal shared-leg control: "
        f"B={B_MAX} base_triangles={base_count} "
        f"shared_candidates={shared_candidates} parity_valid={len(hits)} "
        f"primitive_root_gcd_hits={len(primitives)} "
        "new_primitive=(2720,165,2725;1533,2444,2044)"
    )


if __name__ == "__main__":
    main()
