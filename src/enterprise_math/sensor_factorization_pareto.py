"""CRT-equivalent sensor factorizations and channel/word-width Pareto frontiers.

Fix distinct prime precision factors p_1,...,p_k and let L be their product.
Any partition of the prime factors into groups B_1,...,B_g defines composite
sensor channels

    M_r = product_{p in B_r} p.

The M_r are pairwise coprime and their product/lcm is L, so CRT gives

    Z/LZ ~= product_r Z/M_r Z.

Hence every grouping carries exactly the same modular equality precision.  What
changes is implementation cost: number of channels, peak arithmetic word width,
and rounded aggregate storage width.

This module enumerates the finite factorization family for bounded prime sets,
computes exact resource metrics, and extracts the nondominated frontier under

    lower channel count  AND  lower/equal peak bit width.

It also exposes the fixed-channel balancing problem: for exactly g channels,
choose the factor grouping minimizing the largest composite modulus / residue
word width.  This is a multiplicative load-balancing problem (additive after
logs); the owner uses exhaustive enumeration only as a small-instance oracle.

Two universal lower bounds certify how far splitting can possibly help.  With
fused modulus L and g channels, peak width b must satisfy L<=2^(bg), while one
channel must still contain the largest atomic prime factor.  Therefore

    b >= max( ceil(log2(L)/g), bit_width(max prime) ).

When an exhaustive optimum meets this bound, no finer factor search can reduce
peak arithmetic width at that channel count.

CRT and set partitions are standard prior mathematics/CS.  The Enterprise Math
value is the explicit Stage131-style resource interpretation: one exact precision
law admits many semantically identical storage/parallel-width representations.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, prod
from typing import Sequence

from .local_law_modulus_design import joint_modulus


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def _prime_factors(values: Sequence[int]) -> tuple[int, ...]:
    primes = tuple(values)
    if not primes:
        raise ValueError("at least one prime precision factor is required")
    if len(set(primes)) != len(primes):
        raise ValueError("prime precision factors must be distinct")
    for value in primes:
        if isinstance(value, bool) or not isinstance(value, int) or not _is_prime(value):
            raise ValueError("precision factors must be distinct primes")
    return primes


def residue_bit_width(modulus: int) -> int:
    """Bits needed to store residues 0,...,M-1 exactly."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
        raise ValueError("modulus must exceed one")
    return (modulus - 1).bit_length()


def information_peak_width_lower_bound(
    fused_modulus: int,
    channel_count: int,
) -> int:
    """Least b allowed by L <= 2^(b*g), computed without floating logs."""
    if isinstance(fused_modulus, bool) or not isinstance(fused_modulus, int) or fused_modulus <= 1:
        raise ValueError("fused_modulus must exceed one")
    if isinstance(channel_count, bool) or not isinstance(channel_count, int) or channel_count < 1:
        raise ValueError("channel_count must be positive")
    bits = 1
    while (1 << (bits * channel_count)) < fused_modulus:
        bits += 1
    return bits


def atomic_peak_width_lower_bound(prime_factors: Sequence[int]) -> int:
    primes = _prime_factors(prime_factors)
    return residue_bit_width(max(primes))


def peak_width_lower_bound(
    prime_factors: Sequence[int],
    channel_count: int,
) -> int:
    primes = _prime_factors(prime_factors)
    if not 1 <= channel_count <= len(primes):
        raise ValueError("channel_count outside feasible range")
    fused = prod(primes)
    return max(
        information_peak_width_lower_bound(fused, channel_count),
        atomic_peak_width_lower_bound(primes),
    )


def set_partitions(values: Sequence[int]) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """All unlabeled set partitions in one deterministic canonical form."""
    items = tuple(values)
    if not items:
        return ((),)

    result: set[tuple[tuple[int, ...], ...]] = set()

    def rec(index: int, blocks: list[list[int]]) -> None:
        if index == len(items):
            canonical_blocks = tuple(
                sorted(
                    (tuple(sorted(block)) for block in blocks),
                    key=lambda block: (block[0], len(block), block),
                )
            )
            result.add(canonical_blocks)
            return
        value = items[index]
        for block_index in range(len(blocks)):
            nxt = [list(block) for block in blocks]
            nxt[block_index].append(value)
            rec(index + 1, nxt)
        rec(index + 1, [*blocks, [value]])

    rec(0, [])
    return tuple(sorted(result, key=lambda partition: (len(partition), partition)))


def grouping_moduli(
    prime_factors: Sequence[int],
    grouping: Sequence[Sequence[int]],
) -> tuple[int, ...]:
    primes = _prime_factors(prime_factors)
    groups = tuple(tuple(group) for group in grouping)
    if not groups or any(not group for group in groups):
        raise ValueError("grouping must contain nonempty groups")
    flattened = tuple(value for group in groups for value in group)
    if sorted(flattened) != sorted(primes):
        raise ValueError("grouping must partition the declared prime factors exactly")
    if len(set(flattened)) != len(flattened):
        raise ValueError("grouping repeats a prime factor")
    return tuple(prod(group) for group in groups)


def grouping_is_crt_exact(
    prime_factors: Sequence[int],
    grouping: Sequence[Sequence[int]],
) -> bool:
    primes = _prime_factors(prime_factors)
    moduli = grouping_moduli(primes, grouping)
    target = prod(primes)
    if prod(moduli) != target:
        raise AssertionError("grouped modulus product changed total arithmetic content")
    if joint_modulus(moduli) != target:
        raise AssertionError("grouped modulus lcm changed total arithmetic content")
    for index, left in enumerate(moduli):
        for right in moduli[index + 1 :]:
            if gcd(left, right) != 1:
                raise AssertionError("disjoint prime groups failed pairwise coprimality")
    return True


def grouped_residue_code(
    value: int,
    moduli: Sequence[int],
) -> tuple[int, ...]:
    mods = tuple(moduli)
    if not mods:
        raise ValueError("at least one channel modulus is required")
    if any(isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1 for modulus in mods):
        raise ValueError("channel moduli must exceed one")
    return tuple(value % modulus for modulus in mods)


def grouped_code_equivalent_to_fused_modulus(
    prime_factors: Sequence[int],
    grouping: Sequence[Sequence[int]],
    left: int,
    right: int,
) -> bool:
    primes = _prime_factors(prime_factors)
    moduli = grouping_moduli(primes, grouping)
    fused = prod(primes)
    grouped_equal = grouped_residue_code(left, moduli) == grouped_residue_code(right, moduli)
    fused_equal = left % fused == right % fused
    if grouped_equal != fused_equal:
        raise AssertionError("grouped CRT code disagreed with fused modulus equality")
    return grouped_equal


@dataclass(frozen=True)
class SensorFactorizationPoint:
    prime_groups: tuple[tuple[int, ...], ...]
    channel_moduli: tuple[int, ...]
    fused_modulus: int
    channel_count: int
    peak_channel_modulus: int
    peak_bit_width: int
    total_rounded_bit_width: int
    peak_width_lower_bound: int

    @property
    def fully_fused(self) -> bool:
        return self.channel_count == 1

    @property
    def peak_width_optimality_gap(self) -> int:
        return self.peak_bit_width - self.peak_width_lower_bound

    @property
    def meets_peak_width_lower_bound(self) -> bool:
        return self.peak_width_optimality_gap == 0


def sensor_factorization_point(
    prime_factors: Sequence[int],
    grouping: Sequence[Sequence[int]],
) -> SensorFactorizationPoint:
    primes = _prime_factors(prime_factors)
    groups = tuple(tuple(group) for group in grouping)
    if not grouping_is_crt_exact(primes, groups):
        raise AssertionError("invalid CRT grouping")
    moduli = grouping_moduli(primes, groups)
    widths = tuple(residue_bit_width(modulus) for modulus in moduli)
    return SensorFactorizationPoint(
        prime_groups=groups,
        channel_moduli=moduli,
        fused_modulus=prod(primes),
        channel_count=len(moduli),
        peak_channel_modulus=max(moduli),
        peak_bit_width=max(widths),
        total_rounded_bit_width=sum(widths),
        peak_width_lower_bound=peak_width_lower_bound(primes, len(moduli)),
    )


def all_factorization_points(
    prime_factors: Sequence[int],
) -> tuple[SensorFactorizationPoint, ...]:
    primes = _prime_factors(prime_factors)
    return tuple(
        sensor_factorization_point(primes, grouping)
        for grouping in set_partitions(primes)
    )


def point_dominates(
    left: SensorFactorizationPoint,
    right: SensorFactorizationPoint,
) -> bool:
    """Lower channel count and lower peak width are both preferred."""
    weak = (
        left.channel_count <= right.channel_count
        and left.peak_bit_width <= right.peak_bit_width
    )
    strict = (
        left.channel_count < right.channel_count
        or left.peak_bit_width < right.peak_bit_width
    )
    return weak and strict


def factorization_pareto_frontier(
    prime_factors: Sequence[int],
) -> tuple[SensorFactorizationPoint, ...]:
    points = all_factorization_points(prime_factors)
    frontier = tuple(
        point
        for point in points
        if not any(
            point_dominates(other, point)
            for other in points
            if other != point
        )
    )
    return tuple(
        sorted(
            frontier,
            key=lambda point: (
                point.channel_count,
                point.peak_bit_width,
                point.peak_channel_modulus,
                point.channel_moduli,
            ),
        )
    )


def best_factorization_for_exact_channel_count(
    prime_factors: Sequence[int],
    channel_count: int,
) -> SensorFactorizationPoint:
    primes = _prime_factors(prime_factors)
    if isinstance(channel_count, bool) or not isinstance(channel_count, int):
        raise TypeError("channel_count must be an integer")
    if not 1 <= channel_count <= len(primes):
        raise ValueError("channel_count must lie between one and number of prime factors")
    candidates = tuple(
        point
        for point in all_factorization_points(primes)
        if point.channel_count == channel_count
    )
    return min(
        candidates,
        key=lambda point: (
            point.peak_bit_width,
            point.peak_channel_modulus,
            point.total_rounded_bit_width,
            point.channel_moduli,
        ),
    )


def best_factorization_by_channel_budget(
    prime_factors: Sequence[int],
    max_channels: int,
) -> SensorFactorizationPoint:
    primes = _prime_factors(prime_factors)
    if isinstance(max_channels, bool) or not isinstance(max_channels, int):
        raise TypeError("max_channels must be an integer")
    if not 1 <= max_channels <= len(primes):
        raise ValueError("max_channels outside feasible range")
    candidates = tuple(
        point
        for point in all_factorization_points(primes)
        if point.channel_count <= max_channels
    )
    return min(
        candidates,
        key=lambda point: (
            point.peak_bit_width,
            point.channel_count,
            point.peak_channel_modulus,
        ),
    )
