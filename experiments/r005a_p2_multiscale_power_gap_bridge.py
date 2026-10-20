#!/usr/bin/env python3
"""Exact arithmetic audit for the R005-A p=2 multiscale power/gap bridge.

External prime-gap tables are declared inputs and are not re-proved here.
The script checks the exact resource-overlap inequalities and endpoint.
"""

from __future__ import annotations

import json

G1 = 1724
X1 = 10**20
GA = 1132
XA = 43_841_547_845_541_059
GB = 916
XB = 1_686_994_940_955_803

LOWER_K = 640_503_066
K_MS = 2_794_976_585_489
K_PL = 2_263_762_760_542
OLD_CAMPBELL_K = 11_661_903_789


def icbrt(n: int) -> int:
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


def c3(k: int) -> int:
    return icbrt(k*k + 2*k)


def width_gate(k: int) -> bool:
    return G1 * c3(k) <= 2*k


def endpoint_gate(k: int) -> bool:
    return GB * k**3 < 2 * X1**2


def all_symbolic_overlap_gates(k: int) -> dict[str, bool]:
    return {
        "cube_root_core_inside_global_width_budget": G1 * c3(k) <= 2*k,
        # T1^(2/3) > L1, cubed exactly.
        "global_small_power_region_reaches_X1": G1**2 * k**4 < 4 * X1**3,
        # k/sqrt(XA) < sqrt(2k/G1).
        "global_small_to_tier_A_overlap": G1 * k < 2 * XA,
        # k/sqrt(XB) < sqrt(2k/GA).
        "tier_A_to_tier_B_overlap": GA * k < 2 * XB,
        # k^2/X1 < sqrt(2k/GB).
        "tier_B_to_global_e1_overlap": GB * k**3 < 2 * X1**2,
    }


def main() -> None:
    assert not width_gate(LOWER_K - 1)
    assert width_gate(LOWER_K)

    assert endpoint_gate(K_MS)
    assert not endpoint_gate(K_MS + 1)
    assert GB * K_MS**3 <= 2 * X1**2 - 1
    assert GB * (K_MS + 1)**3 >= 2 * X1**2

    gates = all_symbolic_overlap_gates(K_MS)
    assert all(gates.values())

    # Since every non-width overlap gate is monotone-safe downward in k,
    # checking the active upper endpoint plus the established width-gate start
    # freezes the whole large-tail certificate interval.
    assert all(all_symbolic_overlap_gates(k).values() for k in [LOWER_K, K_PL, K_MS])

    result = {
        "status": "R005-A P2 MULTISCALE POWER/GAP BRIDGE EXACT ARITHMETIC AUDIT / EXTERNAL GAP TABLE NOT REPROVED",
        "resources": {
            "global": {"G": G1, "X": X1},
            "tier_A": {"G": GA, "X": XA, "exponent": 2},
            "tier_B": {"G": GB, "X": XB, "exponent": 2},
        },
        "width_gate_first_k": LOWER_K,
        "multiscale_endpoint": K_MS,
        "previous_power_lift_endpoint": K_PL,
        "additional_indices_over_power_lift": K_MS - K_PL,
        "relative_increase_over_power_lift": (K_MS - K_PL) / K_PL,
        "factor_over_old_campbell_endpoint": K_MS / OLD_CAMPBELL_K,
        "endpoint_cube_root_core": c3(K_MS),
        "endpoint_margins": {
            "width": 2*K_MS - G1*c3(K_MS),
            "global_small_power": 4*X1**3 - G1**2*K_MS**4,
            "global_small_to_A": 2*XA - G1*K_MS,
            "A_to_B": 2*XB - GA*K_MS,
            "B_to_global_e1": 2*X1**2 - GB*K_MS**3,
            "next_k_B_to_global_e1_excess": GB*(K_MS+1)**3 - 2*X1**2,
        },
        "all_endpoint_overlap_gates_pass": True,
        "interpretation": (
            "The global 1724 tier covers small q via maximal higher powers and large q via e=1. "
            "The only middle band is bridged by e=2 tiers (1132,XA) and (916,XB). "
            "The active endpoint is the exact B-to-global overlap inequality 916*k^3 < 2*10^40."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
