"""Bound the repair alphabet traded for the final odd proof-order quantum.

Let m_* be the least positive odd Bonferroni order at which every canonical
defect token is globally single-use under P017 CG12.  If m_*>1, put

    m = m_*-2.

The order-m token prefix uses m+1 transverse primes; order m_* uses exactly two
more, say u,v.  Minimality gives

    P_m < k <= P_m*u*v.

Write

    C_m = floor((k-1)/P_m)+1,
    E_m = C_m-1.

Since P_m*u*v>=k,

    E_m = floor((k-1)/P_m) < u*v,

so

    C_m <= u*v.

The exact signed-fiber theorem sharpens each individual CG12 token fiber to
`C_D` or `C_D-1`, and the quotient-remainder construction provides a minimal
exact incidence-repair alphabet of its actual fiber size F_D.  Hence every
penultimate-order token admits exact repair with at most

    F_D <= C_m <= u*v

symbols.  Raising proof order by one odd quantum makes the token family
single-use and removes that repair coordinate entirely.

Thus the last proof-order quantum can always be exchanged for a finite bounded
repair alphabet; the prime-pair scale factor u*v is an exact universal ceiling,
not an entropy approximation.

This is a P017/P018/P007 bridge specialization.  It does not assert that the
repair alphabet is always sharp, and it does not prove prime existence.
"""

from __future__ import annotations

from .p017_p018_token_reuse_precision import (
    defect_token_reuse_capacity,
    least_global_single_use_odd_order,
)
from .p017_p018_transverse_primorial import transverse_odd_prime_prefix


def final_quantum_repair_tradeoff(k: int) -> dict[str, object]:
    """Return the penultimate repair ceiling and final prime-pair scale factor."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")

    terminal = least_global_single_use_odd_order(k)
    terminal_order = int(terminal["least_global_single_use_odd_order"])
    if terminal_order == 1:
        return {
            "k": k,
            "terminal_order": 1,
            "penultimate_order": None,
            "already_single_use_at_first_odd_order": True,
            "repair_symbol_ceiling": 1,
            "final_pair_scale_factor": None,
        }

    penultimate_order = terminal_order - 2
    penultimate = defect_token_reuse_capacity(k, penultimate_order)
    terminal_capacity = defect_token_reuse_capacity(k, terminal_order)
    if not bool(penultimate["defect_tokens_possible"]):
        raise AssertionError("penultimate token family disappeared before the terminal order")
    if bool(penultimate["all_order_m_tokens_single_use"]):
        raise AssertionError("terminal order was not minimal")
    if not bool(terminal_capacity["all_order_m_tokens_single_use"]):
        raise AssertionError("terminal token order is not single-use")

    current_count = penultimate_order + 1
    terminal_count = terminal_order + 1
    primes = transverse_odd_prime_prefix(k, terminal_count)
    if len(primes) < terminal_count:
        # Terminality by exhaustion rather than by a complete next pair.
        return {
            "k": k,
            "terminal_order": terminal_order,
            "penultimate_order": penultimate_order,
            "terminal_by_prime_family_exhaustion": True,
            "penultimate_universal_capacity": int(penultimate["universal_signed_reuse_capacity"]),
            "repair_symbol_ceiling": int(penultimate["universal_signed_reuse_capacity"]),
            "final_prime_pair": tuple(primes[current_count:]),
            "final_pair_scale_factor": None,
        }

    pair = (int(primes[current_count]), int(primes[current_count + 1]))
    scale = pair[0] * pair[1]
    capacity = int(penultimate["universal_signed_reuse_capacity"])
    excess = max(0, capacity - 1)
    if excess >= scale:
        raise AssertionError("penultimate reuse excess did not fit below final pair scale")
    if capacity > scale:
        raise AssertionError("penultimate repair alphabet exceeded final pair scale")

    return {
        "k": k,
        "transverse_primorial_depth": int(terminal["transverse_primorial_depth"]),
        "penultimate_order": penultimate_order,
        "terminal_order": terminal_order,
        "penultimate_universal_capacity": capacity,
        "penultimate_extra_reuse": excess,
        "final_prime_pair": pair,
        "final_pair_scale_factor": scale,
        "repair_symbol_ceiling": capacity,
        "repair_symbol_ceiling_bounded_by_final_pair_scale": True,
        "terminal_repair_symbol_count": 1,
        "terminal_repair_is_trivial": True,
        "proof_order_quantum": 2,
    }
