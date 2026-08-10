"""R004 null-program history collision spectrum.

Binary finite exact reference tools. Joint/complete weight enumerators and
Hamming-scheme intersection counting are prior coding theory. This module
packages them for the P011/R004 bounded-program collision bridge.
"""
from __future__ import annotations
from itertools import combinations, product
from math import comb
from typing import Iterable, Sequence, Tuple


def bit_weight(x: int) -> int:
    return int(x).bit_count()


def code_from_basis(basis: Sequence[int]) -> frozenset[int]:
    code = {0}
    for b in basis:
        code |= {x ^ int(b) for x in tuple(code)}
    return frozenset(code)


def code_weight_enumerator(code: Iterable[int], length: int) -> Tuple[int, ...]:
    out = [0] * (length + 1)
    for c in code:
        w = bit_weight(c)
        if w > length:
            raise ValueError("codeword exceeds declared length")
        out[w] += 1
    return tuple(out)


def minimum_nonzero_weight(code: Iterable[int]) -> int | None:
    weights = [bit_weight(c) for c in code if c]
    return min(weights) if weights else None


def binary_ball_intersection(length: int, radius: int, center_weight: int) -> int:
    if not 0 <= center_weight <= length or not 0 <= radius <= length:
        raise ValueError("invalid arguments")
    total = 0
    for a in range(center_weight + 1):
        for b in range(length - center_weight + 1):
            if a + b <= radius and (center_weight - a) + b <= radius:
                total += comb(center_weight, a) * comb(length - center_weight, b)
    return total


def binary_three_ball_intersection(
    length: int, radius: int, weight_c: int, weight_d: int, weight_cd: int
) -> int:
    # Coordinate pattern counts for (c_j,d_j): 00,10,01,11.
    numerators = (
        2 * length - weight_c - weight_d - weight_cd,
        weight_c - weight_d + weight_cd,
        -weight_c + weight_d + weight_cd,
        weight_c + weight_d - weight_cd,
    )
    if any(v < 0 or v % 2 for v in numerators):
        return 0
    n00, n10, n01, n11 = (v // 2 for v in numerators)
    total = 0
    for a00 in range(n00 + 1):
        for a10 in range(n10 + 1):
            for a01 in range(n01 + 1):
                for a11 in range(n11 + 1):
                    dx = a00 + a10 + a01 + a11
                    dc = a00 + (n10 - a10) + a01 + (n11 - a11)
                    dd = a00 + a10 + (n01 - a01) + (n11 - a11)
                    if max(dx, dc, dd) <= radius:
                        total += (
                            comb(n00, a00)
                            * comb(n10, a10)
                            * comb(n01, a01)
                            * comb(n11, a11)
                        )
    return total


def short_program_multiplicities(code: Iterable[int], length: int, radius: int) -> Tuple[int, ...]:
    code = frozenset(code)
    if not code or 0 not in code:
        raise ValueError("code must contain zero")
    groups = {}
    for e in range(1 << length):
        if bit_weight(e) > radius:
            continue
        rep = min(e ^ c for c in code)
        groups[rep] = groups.get(rep, 0) + 1
    # Include empty cosets only implicitly: they do not affect W_k.
    return tuple(sorted(groups.values(), reverse=True))


def program_collision(code: Iterable[int], length: int, radius: int, order: int) -> int:
    if order < 1:
        raise ValueError("order must be positive")
    return sum(comb(m, order) for m in short_program_multiplicities(code, length, radius) if m >= order)


def pair_collision_from_weights(code: Iterable[int], length: int, radius: int) -> int:
    total = sum(
        binary_ball_intersection(length, radius, bit_weight(c))
        for c in code
        if c
    )
    if total % 2:
        raise AssertionError("ordered-pair count must be even")
    return total // 2


def triangle_profile(code: Iterable[int]) -> Tuple[Tuple[Tuple[int, int, int], int], ...]:
    code = tuple(c for c in code if c)
    counts = {}
    for c in code:
        for d in code:
            if c == d:
                continue
            key = (bit_weight(c), bit_weight(d), bit_weight(c ^ d))
            counts[key] = counts.get(key, 0) + 1
    return tuple(sorted(counts.items()))


def triple_collision_from_triangle_profile(code: Iterable[int], length: int, radius: int) -> int:
    total = 0
    for (wc, wd, wcd), multiplicity in triangle_profile(code):
        total += multiplicity * binary_three_ball_intersection(length, radius, wc, wd, wcd)
    if total % 6:
        raise AssertionError("ordered-triple count must be divisible by 6")
    return total // 6


def unique_short_programs(code: Iterable[int], radius: int) -> bool:
    dmin = minimum_nonzero_weight(code)
    return dmin is None or dmin > 2 * radius
