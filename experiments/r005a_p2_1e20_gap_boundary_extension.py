#!/usr/bin/env python3
"""Exact arithmetic audit for the R005-A p=2 10^20 gap-frontier extension.

This script does NOT re-prove the external prime-gap computation. It freezes
and checks only the exact integer transport from the declared external input

    every real x < 10^20 has a prime in (x, x+1724]

to the R005 square-basin k frontier.
"""

from __future__ import annotations

from math import isqrt
import json

GAP = 1724
X_OLD = 68_000_000_000_000_000_000
X_NEW = 100_000_000_000_000_000_000
OLD_K = 11_661_903_789
NEW_K = 14_142_135_623
LOWER_K = 640_503_066


def integer_cuberoot(n: int) -> int:
    lo, hi = 0, 1
    while hi**3 <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def width_gate(k: int) -> bool:
    U = k*k + 2*k
    return GAP * integer_cuberoot(U) <= 2*k


def main() -> None:
    # Old and new cofactor ceilings convert exactly by k^2/2 < X.
    assert isqrt(2*X_OLD - 1) == OLD_K
    assert isqrt(2*X_NEW - 1) == NEW_K

    assert OLD_K*OLD_K < 2*X_OLD < (OLD_K+1)*(OLD_K+1)
    assert NEW_K*NEW_K < 2*X_NEW < (NEW_K+1)*(NEW_K+1)

    # Freeze the exact first k where the conservative cube-root width gate
    # reaches the constant gap envelope 1724.
    assert not width_gate(LOWER_K - 1)
    assert width_gate(LOWER_K)

    # Endpoint itself remains inside the exhaustive cofactor frontier.
    assert NEW_K*NEW_K < 2*X_NEW
    assert (NEW_K+1)*(NEW_K+1) > 2*X_NEW

    result = {
        "status": "R005-A P2 1E20 GAP-FRONTIER ARITHMETIC AUDIT / EXTERNAL GAP DATA NOT REPROVED",
        "external_gap_envelope": GAP,
        "external_old_x_frontier": X_OLD,
        "external_new_x_frontier": X_NEW,
        "constant_gap_width_gate_first_k": LOWER_K,
        "old_certified_k_endpoint": OLD_K,
        "new_certified_k_endpoint": NEW_K,
        "additional_k_indices": NEW_K - OLD_K,
        "relative_frontier_extension": (NEW_K - OLD_K) / OLD_K,
        "new_endpoint_square": NEW_K*NEW_K,
        "next_square": (NEW_K+1)*(NEW_K+1),
        "theorem_transport": (
            "Assuming the declared external finite input that all consecutive "
            "prime gaps with left endpoint below 1e20 are at most 1724, the "
            "existing R005 p=2 constant-gap core-forcing bridge extends the "
            "finite least-basis and tau<=1 classification through k=14142135623."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
