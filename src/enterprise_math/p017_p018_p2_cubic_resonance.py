"""Cubic resonance at the minimal P2 roughness cutoff.

The minimal product cutoff forcing every square-interval rough survivor to have
Omega<=2 is

    z = floor((k^2+2k)^(1/3)).

One might hope to feed the resulting semiprime tail into the existing P018
cubic-high channel injectivity theorem.  The scales lock in the opposite way.

For a rough semiprime n=p*q in the interval, p>=z+1, hence

    q <= (k^2+2k)/(z+1) < (z+1)^2,

so its base square-root channel index satisfies

    j_q=floor(sqrt(q)) <= z.

The P018 cubic candidate horizon is

    H_c(k)=floor((2k^2-1)^(1/3))+1.

For k>=3, k^2+2k < 2k^2-1, so z<=H_c(k)-1.  Therefore the entire two-point
candidate channel

    {j_q,j_q+1}

lies at or below H_c(k).  None of the minimal-P2 quotient channels reaches the
cubic-high injective regime.

This is an exact negative boundary: the cubic factor cutoff that first reduces
Omega to two simultaneously pushes the complementary quotient root into the
P018 cubic ambiguity zone.  Existing cubic-high uniqueness can localize other
P017 hard-core channels, but it cannot by itself terminate this P2 tail.
"""

from __future__ import annotations

from math import isqrt

from .p017_p018_buchstab_cutoff_ladder import (
    prime_or_semiprime_cutoff_decomposition,
    square_interval_upper,
)
from .p017_p018_cubic_high_channel import cubic_candidate_horizon


def p2_cubic_resonance(k: int) -> dict[str, object]:
    """Verify every minimal-P2 semiprime quotient channel is cubic-low."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")

    data = prime_or_semiprime_cutoff_decomposition(k)
    z = int(data["cubic_root_cutoff"])
    upper = square_interval_upper(k)
    horizon = cubic_candidate_horizon(k)

    if not upper < 2 * k * k - 1:
        raise AssertionError("k>=3 failed U_k<2k^2-1")
    if z > horizon - 1:
        raise AssertionError("P2 cutoff escaped below-horizon cubic ordering")

    rows: list[tuple[int, int, int, tuple[int, int]]] = []
    for p, q, value, _offset in data["semiprime_edges"]:
        if p < z + 1:
            raise AssertionError("P2 semiprime factor did not exceed the cutoff")
        if not q * (z + 1) <= upper:
            raise AssertionError("cofactor quotient bound failed")
        if not q < (z + 1) ** 2:
            raise AssertionError("cofactor failed the cubic self-dual square bound")
        root = isqrt(q)
        channel = (root, root + 1)
        if root > z:
            raise AssertionError("cofactor root escaped the cubic cutoff")
        if channel[1] > horizon:
            raise AssertionError("P2 quotient candidate channel entered cubic-high range")
        rows.append((p, q, root, channel))

    return {
        "k": k,
        "p2_cutoff": z,
        "cubic_candidate_horizon": horizon,
        "cutoff_below_horizon": z <= horizon - 1,
        "semiprime_channel_rows": tuple(rows),
        "all_p2_channels_cubic_low": True,
        "route_status": "CUBIC_RESONANCE_NEGATIVE_BOUNDARY",
    }
