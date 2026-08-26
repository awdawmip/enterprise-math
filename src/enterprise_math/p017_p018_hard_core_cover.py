"""Small-core vertex-cover reduction for the P017/P018 hard-core bridge.

For every residual hard-core core pair ``a,b`` one has ``a*b < k``. Put

    h = isqrt(k-1).

Then at least one core is at most ``h``. Thus the odd cores in ``[3,h]`` form
a vertex cover of the abstract hard-core core graph. Moreover, any two distinct
odd small cores ``d,e <= h`` satisfy ``d*e <= h^2 <= k-1 < k``. The P018 #148
odd-small-product theorem therefore gives disjoint two-basin candidate channels
for every two different small-core cells.

Consequently all cross-cell root-channel reuse is eliminated exactly. The only
remaining multiplicity question is within one fixed small-core cell, where the
P017 #150/L053 parity spacing by ``2*d*e`` becomes the relevant next constraint.

This module records only the bridge consequence; P018 retains ownership of the
general candidate-root separation theorem.
"""

from __future__ import annotations

from math import isqrt

from .p017_p018_hard_core_bridge import base_root_index


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def small_core_cutoff(k: int) -> int:
    _require_int("k", k)
    if k < 2:
        raise ValueError("k must be at least 2")
    return isqrt(k - 1)


def hard_core_small_endpoint(k: int, a: int, b: int) -> dict[str, int]:
    """Return the canonical smaller endpoint and certify it lies below sqrt(k)."""
    for name, value in (("k", k), ("a", a), ("b", b)):
        _require_int(name, value)
    if not (a >= 3 and b >= 3 and a % 2 == 1 and b % 2 == 1 and a * b < k):
        raise ValueError("require odd cores a,b>=3 with a*b<k")
    cutoff = small_core_cutoff(k)
    endpoint = min(a, b)
    if endpoint > cutoff:
        raise AssertionError("hard-core edge escaped the small-core vertex cover")
    return {
        "k": k,
        "a": a,
        "b": b,
        "cutoff": cutoff,
        "small_endpoint": endpoint,
    }


def small_core_candidate_channel(k: int, core: int) -> tuple[int, int]:
    """Return the canonical two-root candidate channel for one odd small core."""
    _require_int("core", core)
    cutoff = small_core_cutoff(k)
    if not (3 <= core <= cutoff and core % 2 == 1):
        raise ValueError("core must be an odd small core in [3,isqrt(k-1)]")
    root = base_root_index(k, core)
    return root, root + 1


def disjoint_small_core_channels(k: int, d: int, e: int) -> dict[str, object]:
    """Certify pairwise disjoint candidate channels on the small-core cover."""
    _require_int("d", d)
    _require_int("e", e)
    cutoff = small_core_cutoff(k)
    if not (3 <= d < e <= cutoff and d % 2 == 1 and e % 2 == 1):
        raise ValueError("require distinct odd small cores 3<=d<e<=isqrt(k-1)")
    if d * e >= k:
        raise AssertionError("small-core cutoff failed to imply d*e<k")
    left = small_core_candidate_channel(k, d)
    right = small_core_candidate_channel(k, e)
    if left[0] < right[0] + 2:
        raise AssertionError("P018 odd-small-product candidate separation failed")
    if set(left).intersection(right):
        raise AssertionError("distinct small-core channels overlap")
    return {
        "k": k,
        "d": d,
        "e": e,
        "cutoff": cutoff,
        "d_channel": left,
        "e_channel": right,
        "base_root_gap": left[0] - right[0],
    }


def small_core_channel_cover(k: int) -> dict[str, object]:
    """Return all odd small-core cells and verify global pairwise channel separation."""
    cutoff = small_core_cutoff(k)
    cores = tuple(range(3, cutoff + 1, 2))
    channels = {core: small_core_candidate_channel(k, core) for core in cores}
    for i, d in enumerate(cores):
        for e in cores[i + 1 :]:
            disjoint_small_core_channels(k, d, e)
    return {
        "k": k,
        "cutoff": cutoff,
        "cores": cores,
        "channels": channels,
        "cell_count": len(cores),
    }
