"""Width/depth value spectrum of rooted-circuit premises in a binary AND tree.

A rooted-circuit premise P for a node is one-round if materialized as the circuit
rule P=>root, but under the local Horn basis the same premise may need several
rounds to derive the root.  Let d(P) be that base derivation depth.  Its direct
macro saves d(P)-1 rounds for the exact P->root query.

This module counts minimal premise sets jointly by

    (premise width, base derivation depth).

Let A_h(m,d) count minimal ways to make a height-h node available, allowing the
node itself as the direct seed (width1,depth0).  For an internal node, left/right
availability choices combine on disjoint subtrees:

    width = m_left + m_right
    depth = 1 + max(d_left,d_right).

The rooted-circuit spectrum P_h is the derived part only, excluding the direct
root seed.

A key closed consequence is that for any host height h>=d,

    # {root circuits with base depth <= d} = M_d,

where M_d is the rooted-circuit count of a standalone height-d tree.  Hence the
number with **exact** base depth d is M_d-M_(d-1), independent of the deeper host
tree.  Premise widths at exact depth d fill every integer from d+1 through 2^d.

This yields a materialization-opportunity spectrum: deeper circuits offer larger
per-query round savings but occur in explosively larger families and can have
wider premise sets.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

from .stage131_rooted_circuit_table_explosion import (
    rooted_circuit_count,
    rooted_circuit_width_polynomial,
)


Spectrum = dict[tuple[int, int], int]


def availability_width_depth_spectrum(height: int) -> Spectrum:
    """Count minimal availability sets by (width, derivation depth)."""
    if isinstance(height, bool) or not isinstance(height, int) or height < 0:
        raise ValueError("height must be a nonnegative integer")
    current: Spectrum = {(1, 0): 1}
    for _ in range(height):
        nxt: defaultdict[tuple[int, int], int] = defaultdict(int)
        nxt[(1, 0)] = 1  # direct seed of the current node
        for (left_width, left_depth), left_count in current.items():
            for (right_width, right_depth), right_count in current.items():
                key = (
                    left_width + right_width,
                    1 + max(left_depth, right_depth),
                )
                nxt[key] += left_count * right_count
        current = dict(nxt)
    return current


def rooted_circuit_width_depth_spectrum(height: int) -> Spectrum:
    """Count rooted-circuit premises by (width, base derivation depth)."""
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")
    child = availability_width_depth_spectrum(height - 1)
    result: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (left_width, left_depth), left_count in child.items():
        for (right_width, right_depth), right_count in child.items():
            key = (
                left_width + right_width,
                1 + max(left_depth, right_depth),
            )
            result[key] += left_count * right_count
    return dict(result)


def spectrum_total_count(spectrum: Spectrum) -> int:
    return sum(spectrum.values())


def spectrum_width_histogram(spectrum: Spectrum) -> dict[int, int]:
    result: defaultdict[int, int] = defaultdict(int)
    for (width, _depth), count in spectrum.items():
        result[width] += count
    return dict(result)


def spectrum_depth_histogram(spectrum: Spectrum) -> dict[int, int]:
    result: defaultdict[int, int] = defaultdict(int)
    for (_width, depth), count in spectrum.items():
        result[depth] += count
    return dict(result)


def rooted_circuit_depth_histogram(height: int) -> dict[int, int]:
    return spectrum_depth_histogram(rooted_circuit_width_depth_spectrum(height))


def rooted_circuit_count_through_base_depth(host_height: int, depth: int) -> int:
    h = int(host_height)
    d = int(depth)
    if h <= 0 or d <= 0 or d > h:
        raise ValueError("require 1<=depth<=host_height")
    spectrum = rooted_circuit_width_depth_spectrum(h)
    return sum(
        count
        for (_width, base_depth), count in spectrum.items()
        if base_depth <= d
    )


def rooted_circuit_exact_base_depth_count(host_height: int, depth: int) -> int:
    h = int(host_height)
    d = int(depth)
    if h <= 0 or d <= 0 or d > h:
        raise ValueError("require 1<=depth<=host_height")
    previous = 0 if d == 1 else rooted_circuit_count(d - 1)
    return rooted_circuit_count(d) - previous


def rooted_circuit_depth_count_closed(host_height: int) -> dict[int, int]:
    h = int(host_height)
    if h <= 0:
        raise ValueError("host_height must be positive")
    return {
        depth: rooted_circuit_exact_base_depth_count(h, depth)
        for depth in range(1, h + 1)
    }


def depth_cumulative_count_matches_closed(host_height: int) -> bool:
    h = int(host_height)
    if h <= 0:
        raise ValueError("host_height must be positive")
    for depth in range(1, h + 1):
        actual = rooted_circuit_count_through_base_depth(h, depth)
        expected = rooted_circuit_count(depth)
        if actual != expected:
            raise AssertionError("rooted-circuit depth cumulative count lost host-height invariance")
    return True


def widths_at_exact_base_depth(host_height: int, depth: int) -> tuple[int, ...]:
    h = int(host_height)
    d = int(depth)
    if h <= 0 or d <= 0 or d > h:
        raise ValueError("require 1<=depth<=host_height")
    spectrum = rooted_circuit_width_depth_spectrum(h)
    return tuple(
        sorted(
            width
            for (width, base_depth), count in spectrum.items()
            if base_depth == d and count > 0
        )
    )


def exact_depth_width_interval_closed(depth: int) -> tuple[int, int]:
    d = int(depth)
    if d <= 0:
        raise ValueError("depth must be positive")
    return d + 1, 1 << d


def depth_width_support_matches_closed(host_height: int) -> bool:
    h = int(host_height)
    if h <= 0:
        raise ValueError("host_height must be positive")
    for depth in range(1, h + 1):
        lower, upper = exact_depth_width_interval_closed(depth)
        actual = widths_at_exact_base_depth(h, depth)
        expected = tuple(range(lower, upper + 1))
        if actual != expected:
            raise AssertionError("exact-depth premise widths failed dense interval theorem")
    return True


def materialization_round_saving(base_depth: int) -> int:
    d = int(base_depth)
    if d <= 0:
        raise ValueError("base_depth must be positive")
    return d - 1


@dataclass(frozen=True)
class RootedCircuitDepthOpportunity:
    depth: int
    circuit_count: int
    cumulative_count: int
    min_premise_width: int
    max_premise_width: int
    one_round_saving: int
    share_of_all_root_circuits: Fraction


def rooted_circuit_depth_opportunities(host_height: int) -> tuple[RootedCircuitDepthOpportunity, ...]:
    h = int(host_height)
    if h <= 0:
        raise ValueError("host_height must be positive")
    total = rooted_circuit_count(h)
    cumulative = 0
    result = []
    for depth in range(1, h + 1):
        count = rooted_circuit_exact_base_depth_count(h, depth)
        cumulative += count
        min_width, max_width = exact_depth_width_interval_closed(depth)
        result.append(
            RootedCircuitDepthOpportunity(
                depth=depth,
                circuit_count=count,
                cumulative_count=cumulative,
                min_premise_width=min_width,
                max_premise_width=max_width,
                one_round_saving=materialization_round_saving(depth),
                share_of_all_root_circuits=Fraction(count, total),
            )
        )
    return tuple(result)


def spectrum_marginals_match_parent_width_polynomial(height: int) -> bool:
    h = int(height)
    if h <= 0:
        raise ValueError("height must be positive")
    spectrum = rooted_circuit_width_depth_spectrum(h)
    if spectrum_width_histogram(spectrum) != rooted_circuit_width_polynomial(h):
        raise AssertionError("width-depth spectrum failed parent width polynomial marginal")
    if spectrum_total_count(spectrum) != rooted_circuit_count(h):
        raise AssertionError("width-depth spectrum failed total circuit count")
    return True
