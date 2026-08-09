"""Raw cofactor-window mass bound for the even-J terminal error shell.

At the product-adaptive terminal order with even J=J_perp(k), every reusable
full-block token A<=k-1 has a squarefree radical D containing exactly J
transverse odd primes and D<k.  The near-primorial replacement formula enumerates
all possible such radicals.

Before imposing exact p-adic exponents, anchor coprimality or least-prime
roughness, multiples of D in the open square basin correspond to the raw
cofactor window

    W_D(k) = [floor(k^2/D)+1, floor(k(k+2)/D)].

Its cardinality is

    w_D = floor(k(k+2)/D)-floor(k^2/D).

Since the numerator interval has length 2k,

    w_D <= ceil(2k/D).

Every exact reusable full-block incidence sits inside the corresponding
squarefree D window, so the total product-adaptive reusable error satisfies

    R_{m_*}(k) <= sum_{D in N_J(k)} w_D,

where N_J(k) is the terminal near-primorial radical shell.  A further soft
reciprocal bound is

    sum_D w_D <= sum_D ceil(2k/D)
                  <= 2k sum_D 1/D + |N_J(k)|.

This is a safe global resource bound.  It does not claim the raw window points
survive canonical least-support, p-adic, or anchor filters; those only reduce the
actual error.
"""

from __future__ import annotations

from math import gcd

from .p017_p018_near_primorial_shell import near_primorial_radical_candidates


def raw_square_basin_cofactor_window(k: int, divisor: int) -> dict[str, int]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(divisor, bool) or not isinstance(divisor, int) or divisor <= 0:
        raise ValueError("divisor must be a positive integer")
    q_min = (k * k) // divisor + 1
    q_max = (k * (k + 2)) // divisor
    size = max(0, q_max - q_min + 1)
    ceil_bound = (2 * k + divisor - 1) // divisor
    if size > ceil_bound:
        raise AssertionError("raw cofactor window exceeded ceil(2k/D)")
    return {
        "k": k,
        "divisor": divisor,
        "q_min": q_min,
        "q_max": q_max,
        "raw_window_size": size,
        "ceil_2k_over_D": ceil_bound,
    }


def near_primorial_raw_window_mass(k: int) -> dict[str, object]:
    """Sum the exact raw windows and reciprocal ceiling over terminal radicals."""
    shell = near_primorial_radical_candidates(k)
    rows: list[dict[str, int]] = []
    raw_mass = 0
    ceil_mass = 0

    # Rational reciprocal mass is retained exactly as numerator over the product
    # denominator by incremental common-denominator updates.
    reciprocal_num = 0
    reciprocal_den = 1
    for radical in shell["candidate_radicals"]:
        divisor = int(radical)
        data = raw_square_basin_cofactor_window(k, divisor)
        rows.append(data)
        raw_mass += int(data["raw_window_size"])
        ceil_mass += int(data["ceil_2k_over_D"])

        new_num = reciprocal_num * divisor + reciprocal_den
        new_den = reciprocal_den * divisor
        common = gcd(new_num, new_den)
        reciprocal_num = new_num // common
        reciprocal_den = new_den // common

    candidate_count = int(shell["candidate_count"])
    # ceil(x)<=x+1 gives the exact rational soft bound
    soft_num = 2 * k * reciprocal_num + candidate_count * reciprocal_den
    soft_den = reciprocal_den
    if raw_mass > ceil_mass:
        raise AssertionError("raw window mass exceeded sum of ceil bounds")
    if raw_mass * soft_den > soft_num:
        raise AssertionError("raw window mass exceeded reciprocal soft bound")

    return {
        **shell,
        "window_rows": tuple(rows),
        "raw_window_mass": raw_mass,
        "ceil_window_mass": ceil_mass,
        "reciprocal_shell_mass": (reciprocal_num, reciprocal_den),
        "reciprocal_soft_bound": (soft_num, soft_den),
        "actual_reusable_full_block_error_upper_bound": raw_mass,
    }
