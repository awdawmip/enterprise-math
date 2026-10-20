"""Cube-root complexity split for the P017×P018 pronic Euclidean atlas.

Let M=k(k+1), 1<=n<=k, and write the two Euclidean quotients

    k = a n + b,
    b(b+1) = c n + t.

The two-quotient atlas proves that every fixed (a,c)-cell has integer n-width at
most

    1 + floor((B0-1)/a),

where B0 is the least positive integer satisfying

    a B0(B0+1) >= k-B0.

If a^3>=k then B0<=a (indeed a*a*(a+1)>=k-a), so every (a,c)-cell is a
singleton.  With

    A = least positive integer with A^3>=k,

all long cells therefore lie in the at most A-1 quotient strips a<A, while the
region a>=A contains only

    n <= floor(k/A) = O(k^(2/3))

factor states and all of its two-quotient cells are singleton.

There is also an exact modulus split on the long strips.  For a squarefree odd
divisor channel d coprime to n write

    g=gcd(d,a),   d=g e.

Then g|a, gcd(e,a)=1 and g<=a<A.  The channel

    r = Q_n(M) + 2 R_n(M) n^{-1} (mod d)

has the two CRT components

    r = 2 M n^{-1} - c                              (mod g),

    r = 2 a M (k-b)^{-1} - a(k+b+1) - c            (mod e).

Thus every obstruction to dividing by the fixed quotient a is confined to a
cube-root-size singular modulus g; the coprime modulus e carries the genuine
fixed-a Kloosterman inverse in k-b.

This is a finite complexity decomposition, not an exponential-sum bound or a
prime-gap theorem.
"""

from __future__ import annotations

from math import gcd

from .p018_pronic_two_quotient_atlas import (
    pronic_two_quotient_state,
    two_quotient_cell_width_ceiling,
    two_quotient_kloosterman_channel,
)


def integer_cube_root_ceiling(k: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    lo, hi = 1, k
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**3 >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


def cube_root_atlas_partition(k: int) -> dict[str, object]:
    """Partition n<=k into singleton-cell and long-strip quotient regimes."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    A = integer_cube_root_ceiling(k)
    singleton_region_ceiling = k // A
    singleton_states: list[int] = []
    long_strip_states: dict[int, list[int]] = {}

    for n in range(1, k + 1):
        a = k // n
        if a >= A:
            singleton_states.append(n)
            width = two_quotient_cell_width_ceiling(k, a)
            if int(width["integer_n_cell_width_ceiling"]) != 1:
                raise AssertionError("cube-root quotient regime did not force singleton cells")
        else:
            long_strip_states.setdefault(a, []).append(n)

    if singleton_states and max(singleton_states) > singleton_region_ceiling:
        raise AssertionError("singleton quotient regime escaped n<=floor(k/A)")
    if any(a >= A for a in long_strip_states):
        raise AssertionError("long-strip quotient escaped a<A")
    if len(long_strip_states) > A - 1:
        raise AssertionError("too many long quotient strips")

    return {
        "k": k,
        "cube_root_cutoff_A": A,
        "singleton_region_n_ceiling": singleton_region_ceiling,
        "singleton_region_state_count": len(singleton_states),
        "singleton_region_states": tuple(singleton_states),
        "long_strip_count": len(long_strip_states),
        "long_strips": tuple((a, tuple(values)) for a, values in sorted(long_strip_states.items())),
        "all_high_quotient_cells_singleton": True,
        "all_long_strips_have_small_quotient": True,
    }


def long_strip_modulus_split(k: int, n: int, d: int) -> dict[str, object]:
    """Split one long-strip channel into singular g|a and coprime e parts."""
    if isinstance(d, bool) or not isinstance(d, int) or d < 1 or d % 2 == 0:
        raise ValueError("d must be a positive odd integer")
    state = pronic_two_quotient_state(k, n)
    a = int(state["k_quotient_a"])
    if a < 1:
        raise ValueError("long-strip split is declared for 1<=n<=k")
    A = integer_cube_root_ceiling(k)
    if a >= A:
        raise ValueError("n is not in the long-strip regime a<A")
    if gcd(n, d) != 1:
        raise ValueError("channel requires gcd(n,d)=1")

    # The executable theorem assumes squarefree d only through gcd(g,e)=1.
    remaining = d
    prime = 3
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            if remaining % prime == 0:
                raise ValueError("d must be squarefree")
        prime += 2

    g = gcd(d, a)
    e = d // g
    if gcd(g, e) != 1 or gcd(e, a) != 1:
        raise AssertionError("squarefree modulus did not split into singular/coprime parts")
    if g > a or g >= A:
        raise AssertionError("singular modulus escaped the cube-root quotient scale")

    full = two_quotient_kloosterman_channel(k, n, d)
    M = int(state["center"])
    b = int(state["k_remainder_b"])
    c = int(state["small_pronic_quotient_c"])
    full_residue = int(full["euclidean_channel_residue"])

    if g == 1:
        singular_residue = 0
    else:
        inv_n_g = pow(n, -1, g)
        singular_residue = (2 * M * inv_n_g - c) % g
        if full_residue % g != singular_residue:
            raise AssertionError("singular quotient-prime channel formula failed")

    if e == 1:
        coprime_residue = 0
    else:
        inv_k_minus_b = pow(k - b, -1, e)
        coprime_residue = (
            2 * a * M * inv_k_minus_b
            - a * (k + b + 1)
            - c
        ) % e
        if full_residue % e != coprime_residue:
            raise AssertionError("coprime fixed-a Kloosterman channel formula failed")

    return {
        **state,
        "cube_root_cutoff_A": A,
        "d": d,
        "singular_modulus_g": g,
        "coprime_modulus_e": e,
        "full_channel_residue": full_residue,
        "singular_channel_residue": singular_residue,
        "coprime_channel_residue": coprime_residue,
        "singular_modulus_below_cube_root": True,
        "long_strip_modulus_split_exact": True,
    }
