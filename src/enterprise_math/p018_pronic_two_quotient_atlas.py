"""Two-quotient Euclidean atlas for the pronic center k(k+1).

Start from a factor n<=k and divide k by n:

    k = a n + b,                 0 <= b < n.

Then divide the small pronic remainder by the same n:

    b(b+1) = c n + t,           0 <= t < n.

The first pronic lift gives

    M=k(k+1)=n Q+t,
    Q=-a^2 n + a(2k+1)+c.

For an odd divisor channel d coprime to n, the Euclidean thin-strip child
residue is

    j = Q + 2t n^{-1} (mod d).

Using t=M-nQ this is simply

    j = 2M n^{-1}-Q (mod d),

and on a fixed two-quotient cell (a,c) it becomes the standard incomplete
Kloosterman phase

    j = a^2 n + 2M n^{-1} - a(2k+1)-c (mod d).

Thus the floor/remainder hybrid has disappeared inside one cell: the only
nonlinear arithmetic is n -> n^{-1} mod d.

The cells are also short.  In one fixed a-block put b=k-an and consider

    g_a(b)=a*b*(b+1)/(k-b).

Then c=floor(g_a(b)).  The function is strictly increasing and strictly convex
for 0<=b<k.  Let B0 be the least positive integer such that

    a*B0*(B0+1) >= k-B0,

i.e. g_a(B0)>=1.  Convexity implies that every real interval on which floor(g_a)
is constant has b-width < B0.  Since successive n in a fixed a-block change b
by exactly a, every (a,c)-cell contains at most

    1 + floor((B0-1)/a)

integer n-values.  Asymptotically B0~sqrt(k/a), so the cell-width ceiling is
O(1+sqrt(k/a^3)).  In particular, once a>=k^(1/3), every cell has bounded
integer width.

This is a finite quotient-coordinate theorem.  It does not assert an incomplete
Kloosterman estimate or a prime-gap theorem.
"""

from __future__ import annotations

from math import gcd

from .p018_pronic_euclidean_lift import pronic_euclidean_lift


def _cell_b_width_threshold(k: int, a: int) -> int:
    """Least B>=1 with a*B*(B+1)>=k-B, computed by integer arithmetic."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    if isinstance(a, bool) or not isinstance(a, int) or a < 1:
        raise ValueError("a must be positive")
    lo, hi = 1, k
    while lo < hi:
        mid = (lo + hi) // 2
        if a * mid * (mid + 1) >= k - mid:
            hi = mid
        else:
            lo = mid + 1
    return lo


def two_quotient_cell_width_ceiling(k: int, a: int) -> dict[str, int]:
    """Return the exact discrete width ceiling for every fixed (a,c) cell."""
    if a > k:
        raise ValueError("a must satisfy 1<=a<=k")
    B0 = _cell_b_width_threshold(k, a)
    n_ceiling = 1 + (B0 - 1) // a
    return {
        "k": k,
        "a": a,
        "b_width_threshold_B0": B0,
        "integer_n_cell_width_ceiling": n_ceiling,
    }


def pronic_two_quotient_state(k: int, n: int) -> dict[str, int | bool]:
    """Return (a,b,c,t,Q) and verify the linear quotient formula."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(n, bool) or not isinstance(n, int) or not (1 <= n <= k):
        raise ValueError("n must satisfy 1<=n<=k")
    data = pronic_euclidean_lift(k, n)
    a = int(data["k_quotient_a"])
    b = int(data["k_remainder_b"])
    c = int(data["small_pronic_quotient_c"])
    t = int(data["small_pronic_remainder_t"])
    Q = int(data["center_quotient_Q"])
    linear_Q = -a * a * n + a * (2 * k + 1) + c
    if Q != linear_Q:
        raise AssertionError("two-quotient cell did not linearize the pronic quotient")
    return {
        **data,
        "linearized_center_quotient": linear_Q,
        "two_quotient_state_exact": True,
    }


def two_quotient_kloosterman_channel(k: int, n: int, d: int) -> dict[str, int | bool]:
    """Return the exact An+B*n^{-1}+C channel residue on one (a,c) cell."""
    if isinstance(d, bool) or not isinstance(d, int) or d < 1 or d % 2 == 0:
        raise ValueError("d must be a positive odd integer")
    if gcd(n, d) != 1:
        raise ValueError("channel requires gcd(n,d)=1")
    data = pronic_two_quotient_state(k, n)
    M = int(data["center"])
    Q = int(data["center_quotient_Q"])
    t = int(data["center_remainder_R"])
    a = int(data["k_quotient_a"])
    c = int(data["small_pronic_quotient_c"])
    inv_n = pow(n, -1, d)

    euclidean_channel = (Q + 2 * t * inv_n) % d
    inverse_minus_quotient = (2 * M * inv_n - Q) % d
    kloosterman_channel = (
        a * a * n
        + 2 * M * inv_n
        - a * (2 * k + 1)
        - c
    ) % d
    if euclidean_channel != inverse_minus_quotient or euclidean_channel != kloosterman_channel:
        raise AssertionError("two-quotient Kloosterman channel identity failed")
    return {
        **data,
        "d": d,
        "inverse_n_mod_d": inv_n,
        "euclidean_channel_residue": euclidean_channel,
        "inverse_minus_quotient_residue": inverse_minus_quotient,
        "linear_inverse_kloosterman_residue": kloosterman_channel,
        "two_quotient_kloosterman_identity": True,
    }


def two_quotient_cells(k: int, a: int) -> dict[str, object]:
    """Enumerate bounded cells for regression and verify the universal width bound."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(a, bool) or not isinstance(a, int) or not (1 <= a <= k):
        raise ValueError("a must satisfy 1<=a<=k")
    groups: dict[int, list[int]] = {}
    for n in range(1, k + 1):
        q, _b = divmod(k, n)
        if q != a:
            continue
        state = pronic_two_quotient_state(k, n)
        c = int(state["small_pronic_quotient_c"])
        groups.setdefault(c, []).append(n)

    ceiling = two_quotient_cell_width_ceiling(k, a)
    max_width = max((len(values) for values in groups.values()), default=0)
    if max_width > int(ceiling["integer_n_cell_width_ceiling"]):
        raise AssertionError("observed two-quotient cell exceeded the convexity ceiling")
    for values in groups.values():
        if values != list(range(values[0], values[-1] + 1)):
            raise AssertionError("fixed (a,c) cell is not consecutive in n")
    return {
        **ceiling,
        "cells": tuple((c, tuple(values)) for c, values in sorted(groups.items())),
        "cell_count": len(groups),
        "observed_max_cell_width": max_width,
        "all_cells_within_ceiling": True,
    }
