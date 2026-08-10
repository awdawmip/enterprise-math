"""Width/depth value spectrum of rooted-circuit premises in a binary AND tree.

A rooted-circuit premise P becomes a one-round rule if materialized as P=>root,
but under the local Horn basis it may require several synchronous rounds.  Let
``d(P)`` be that base derivation depth.  Materializing the exact circuit therefore
saves ``d(P)-1`` rounds for the P->root query.

We count circuits jointly by premise width and base derivation depth.

Let A_h(m,d) count minimal ways to make a height-h node available, allowing the
node itself as the direct seed (width1,depth0).  At an internal node:

* direct seed contributes (1,0);
* left/right availability choices combine as

      width = m_left + m_right,
      depth = 1 + max(d_left,d_right).

The rooted-circuit spectrum excludes only the direct root seed.

Closed consequences:

* for any host height h>=d,

      # {root circuits with base depth <= d} = M_d,

  where M_d is the rooted-circuit count of a standalone height-d tree;
* exact depth-d count is M_d-M_(d-1), with M_0=0;
* exact depth-d circuit widths occupy every integer from d+1 through 2^d.

Thus circuit depth is a materialization-value coordinate independent of the host
height once the host is deep enough.
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
    if isinstance(height, bool) or not isinstance(height, int) or height < 0:
        raise ValueError("height must be a nonnegative integer")
    current: Spectrum = {(1, 0): 1}
    for _ in range(height):
        nxt: defaultdict[tuple[int, int], int] = defaultdict(int)
        nxt[(1, 0)] = 1
        for (lw, ld), lc in current.items():
            for (rw, rd), rc in current.items():
                nxt[(lw + rw, 1 + max(ld, rd))] += lc * rc
        current = dict(nxt)
    return current


def rooted_circuit_width_depth_spectrum(height: int) -> Spectrum:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")
    child = availability_width_depth_spectrum(height - 1)
    result: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (lw, ld), lc in child.items():
        for (rw, rd), rc in child.items():
            result[(lw + rw, 1 + max(ld, rd))] += lc * rc
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
    return sum(count for (_width, base_depth), count in spectrum.items() if base_depth <= d)


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
    return {depth: rooted_circuit_exact_base_depth_count(h, depth) for depth in range(1, h + 1)}


def depth_cumulative_count_matches_closed(host_height: int) -> bool:
    h = int(host_height)
    if h <= 0:
        raise ValueError("host_height must be positive")
    for depth in range(1, h + 1):
        actual = rooted_circuit_count_through_base_depth(h, depth)
        expected = rooted_circuit_count(depth)
        if actual != expected:
            raise AssertionError("depth cumulative count lost host-height invariance")
    return True


def widths_at_exact_base_depth(host_height: int, depth: int) -> tuple[int, ...]:
    h = int(host_height)
    d = int(depth)
    if h <= 0 or d <= 0 or d > h:
        raise ValueError("require 1<=depth<=host_height")
    spectrum = rooted_circuit_width_depth_spectrum(h)
    return tuple(sorted(width for (width, base_depth), count in spectrum.items() if base_depth == d and count > 0))


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
        if widths_at_exact_base_depth(h, depth) != tuple(range(lower, upper + 1)):
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
        raise AssertionError("width-depth spectrum failed corrected parent width marginal")
    if spectrum_total_count(spectrum) != rooted_circuit_count(h):
        raise AssertionError("width-depth spectrum failed total circuit count")
    return True
