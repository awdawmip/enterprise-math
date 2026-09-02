#!/usr/bin/env python3
"""Exact checks for BRC rational holonomy parity / m-power thickness decomposition."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product

from enterprise_math import (
    brc_is_perfect_power,
    brc_root_integer_value,
    root,
)
from enterprise_math.brc_weighted_recurrent import finite_recurrent_mass_analysis

Q = Fraction
Edge = tuple[int, int, Fraction]


def factor_integer(n: int) -> dict[int, int]:
    if n <= 0:
        raise ValueError("positive integer required")
    result: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            result[p] = result.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


def valuations(q: Fraction) -> dict[int, int]:
    if q <= 0:
        raise ValueError("positive rational required")
    result = factor_integer(q.numerator)
    for p, exponent in factor_integer(q.denominator).items():
        result[p] = result.get(p, 0) - exponent
        if result[p] == 0:
            del result[p]
    return result


def reconstruct(data: dict[int, int]) -> Fraction:
    result = Q(1)
    for p, exponent in data.items():
        if exponent >= 0:
            result *= p**exponent
        else:
            result /= p ** (-exponent)
    return result


def m_power_decomposition(q: Fraction, m: int) -> tuple[int, Fraction]:
    if m < 2:
        raise ValueError("m must be >=2")
    residues: dict[int, int] = {}
    quotients: dict[int, int] = {}
    for p, exponent in valuations(q).items():
        quotient, residue = divmod(exponent, m)
        if residue:
            residues[p] = residue
        if quotient:
            quotients[p] = quotient
    skeleton = 1
    for p, residue in residues.items():
        skeleton *= p**residue
    thickness = reconstruct(quotients)
    return skeleton, thickness


def is_m_power_free(n: int, m: int) -> bool:
    return all(exponent < m for exponent in factor_integer(n).values())


def root_via_brc_of_power_ratio(q: Fraction, skeleton: int, m: int) -> Fraction:
    residual = q / skeleton
    numerator_expr = root(residual.numerator, m)
    denominator_expr = root(residual.denominator, m)
    exact_num, num_trace = brc_is_perfect_power(numerator_expr)
    exact_den, den_trace = brc_is_perfect_power(denominator_expr)
    assert exact_num and exact_den
    numerator, num_trace2 = brc_root_integer_value(numerator_expr)
    denominator, den_trace2 = brc_root_integer_value(denominator_expr)
    assert num_trace == num_trace2
    assert den_trace == den_trace2
    return Q(numerator, denominator)


def tree_normalizing_gauge(n: int, edges: list[Edge], tree: list[int]) -> list[Fraction]:
    if len(tree) != n - 1:
        raise ValueError("tree size mismatch")
    h: list[Fraction | None] = [None] * n
    h[0] = Q(1)
    remaining = set(tree)
    while remaining:
        progress = False
        for index in tuple(remaining):
            a, b, q = edges[index]
            if h[a] is not None and h[b] is None:
                h[b] = h[a] / q
                remaining.remove(index)
                progress = True
            elif h[b] is not None and h[a] is None:
                h[a] = q * h[b]
                remaining.remove(index)
                progress = True
            elif h[a] is not None and h[b] is not None:
                assert q * h[b] / h[a] == 1
                remaining.remove(index)
                progress = True
        if not progress:
            raise ValueError("tree does not connect all vertices")
    return [value for value in h if value is not None]


def tree_coordinates(n: int, edges: list[Edge], tree: list[int]) -> list[Fraction]:
    h = tree_normalizing_gauge(n, edges, tree)
    tree_set = set(tree)
    normalized = [q * h[b] / h[a] for a, b, q in edges]
    assert all(normalized[index] == 1 for index in tree)
    return [normalized[index] for index in range(len(edges)) if index not in tree_set]


def check_large_rational_m_decomposition() -> None:
    checked = 0
    for numerator in range(1, 61):
        for denominator in range(1, 61):
            q = Q(numerator, denominator)
            for m in range(2, 6):
                skeleton, thickness = m_power_decomposition(q, m)
                assert skeleton >= 1
                assert is_m_power_free(skeleton, m)
                assert q == skeleton * thickness**m
                assert root_via_brc_of_power_ratio(q, skeleton, m) == thickness

                qvals = valuations(q)
                svals = factor_integer(skeleton)
                tvals = valuations(thickness)
                primes = set(qvals) | set(svals) | set(tvals)
                for p in primes:
                    exponent = qvals.get(p, 0)
                    quotient, residue = divmod(exponent, m)
                    assert svals.get(p, 0) == residue
                    assert tvals.get(p, 0) == quotient
                checked += 1
    assert checked == 60 * 60 * 4
    print(f"rational m-power decompositions checked={checked}")


def check_squarefree_examples() -> None:
    examples = {
        Q(1, 2): (2, Q(1, 2)),
        Q(2): (2, Q(1)),
        Q(1, 8): (2, Q(1, 4)),
        Q(12, 5): (15, Q(2, 5)),
        Q(75, 28): (21, Q(5, 14)),
    }
    for q, expected in examples.items():
        skeleton, thickness = m_power_decomposition(q, 2)
        assert (skeleton, thickness) == expected
        assert q == skeleton * thickness**2
        assert is_m_power_free(skeleton, 2)


def check_tree_coordinate_complete_split() -> None:
    n = 4
    edges: list[Edge] = [
        (0, 1, Q(12, 5)),
        (2, 1, Q(7, 18)),
        (2, 3, Q(25, 14)),
        (3, 0, Q(9, 10)),
        (0, 2, Q(11, 6)),
        (1, 3, Q(5, 21)),
        (0, 1, Q(13, 8)),
    ]
    tree = [0, 1, 2]
    coordinates = tree_coordinates(n, edges, tree)
    assert len(coordinates) == 4

    pairs = [m_power_decomposition(q, 2) for q in coordinates]
    reconstructed = [Q(s) * r**2 for s, r in pairs]
    assert reconstructed == coordinates
    assert all(is_m_power_free(s, 2) for s, _ in pairs)

    # The squarefree tuple exactly packs all-prime parity in this fixed cycle basis.
    for coordinate, (skeleton, thickness) in zip(coordinates, pairs):
        qvals = valuations(coordinate)
        svals = factor_integer(skeleton)
        assert {p for p, e in qvals.items() if e % 2} == set(svals)
        assert coordinate / skeleton == thickness**2

    # A different tree gives another valid but generally different coordinate tuple.
    tree2 = [0, 1, 5]  # underlying edges 0-1,2-1,1-3
    coordinates2 = tree_coordinates(n, edges, tree2)
    pairs2 = [m_power_decomposition(q, 2) for q in coordinates2]
    assert len(coordinates2) == 4
    assert [s for s, _ in pairs2] != [s for s, _ in pairs]


def one_state_zeta(q: Fraction) -> Fraction | None:
    analysis = finite_recurrent_mass_analysis([[q]])
    if not analysis.stable or analysis.star is None:
        return None
    return analysis.star[0][0]


def check_parity_dynamic_negative_boundaries() -> None:
    stable = Q(1, 2)
    divergent = Q(2)
    s1, r1 = m_power_decomposition(stable, 2)
    s2, r2 = m_power_decomposition(divergent, 2)
    assert s1 == s2 == 2
    assert r1 == Q(1, 2) and r2 == 1
    assert finite_recurrent_mass_analysis([[stable]]).stable
    assert not finite_recurrent_mass_analysis([[divergent]]).stable

    stable2 = Q(1, 8)
    s3, r3 = m_power_decomposition(stable2, 2)
    assert s3 == s1 == 2
    assert r3 == Q(1, 4)
    z1 = one_state_zeta(stable)
    z2 = one_state_zeta(stable2)
    assert z1 == Q(2)
    assert z2 == Q(8, 7)
    assert z1 != z2


def check_fixed_skeleton_fibers() -> None:
    skeletons = [1, 2, 6, 30]
    roots = [Q(1, 6), Q(1, 2), Q(1), Q(3, 2), Q(5)]
    for skeleton in skeletons:
        assert is_m_power_free(skeleton, 2)
        seen: set[Fraction] = set()
        for r in roots:
            q = Q(skeleton) * r**2
            s2, r2 = m_power_decomposition(q, 2)
            assert s2 == skeleton
            assert r2 == r
            seen.add(q)
        assert len(seen) == len(roots)


def check_general_m_fibers() -> None:
    for m in [2, 3, 4, 5]:
        skeleton = 1
        # Use residues below m to create an m-power-free integer.
        for p, residue in [(2, 1), (3, m - 1), (5, min(2, m - 1))]:
            skeleton *= p**residue
        assert is_m_power_free(skeleton, m)
        for r in [Q(1, 3), Q(2, 5), Q(1), Q(7, 2)]:
            q = Q(skeleton) * r**m
            recovered_s, recovered_r = m_power_decomposition(q, m)
            assert recovered_s == skeleton
            assert recovered_r == r


def main() -> int:
    check_large_rational_m_decomposition()
    check_squarefree_examples()
    check_tree_coordinate_complete_split()
    check_parity_dynamic_negative_boundaries()
    check_fixed_skeleton_fibers()
    check_general_m_fibers()
    print("BRC holonomy parity/thickness exact checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
