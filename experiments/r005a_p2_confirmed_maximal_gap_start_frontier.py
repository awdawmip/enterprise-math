#!/usr/bin/env python3
"""Exact arithmetic audit for the R005-A p=2 confirmed maximal-gap-start frontier.

External maximal-gap records are declared inputs and are not re-proved here.
The active global 1724 envelope is extended from 1e20 to the confirmed start
of the next larger maximal gap 1854.
"""

from __future__ import annotations

import json

G1 = 1724
P85 = 101_412_319_996_363_309_069
GA = 1132
XA = 43_841_547_845_541_059
GB = 916
XB = 1_686_994_940_955_803

LOWER_K = 640_503_066
K_OLD_MS = 2_794_976_585_489
K85 = 2_821_231_035_570
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


def gates(k: int) -> dict[str, bool]:
    return {
        "cube_root_width": G1*c3(k) <= 2*k,
        "global_small_power": G1**2 * k**4 < 4 * P85**3,
        "global_small_to_A": G1*k < 2*XA,
        "A_to_B": GA*k < 2*XB,
        "B_to_global_e1": GB*k**3 < 2*P85**2,
    }


def main() -> None:
    assert all(gates(LOWER_K).values())
    assert all(gates(K85).values())

    assert GB*K85**3 < 2*P85**2
    assert GB*(K85+1)**3 >= 2*P85**2

    result = {
        "status": "R005-A P2 CONFIRMED MAXIMAL-GAP-START FRONTIER EXACT ARITHMETIC AUDIT / EXTERNAL RECORD TABLE NOT REPROVED",
        "global_gap_envelope": G1,
        "global_frontier_next_larger_record_start": P85,
        "tier_A": {"G": GA, "X": XA, "e": 2},
        "tier_B": {"G": GB, "X": XB, "e": 2},
        "width_gate_first_k": LOWER_K,
        "previous_multiscale_endpoint": K_OLD_MS,
        "new_endpoint": K85,
        "additional_indices": K85-K_OLD_MS,
        "relative_increment": (K85-K_OLD_MS)/K_OLD_MS,
        "factor_over_old_campbell_endpoint": K85/OLD_CAMPBELL_K,
        "endpoint_cube_root_core": c3(K85),
        "endpoint_margins": {
            "width": 2*K85-G1*c3(K85),
            "global_small_power": 4*P85**3-G1**2*K85**4,
            "global_small_to_A": 2*XA-G1*K85,
            "A_to_B": 2*XB-GA*K85,
            "B_to_global_e1": 2*P85**2-GB*K85**3,
            "next_k_B_to_global_e1_excess": GB*(K85+1)**3-2*P85**2,
        },
        "interpretation": (
            "The confirmed next larger maximal gap 1854 starts at P85, so the "
            "1724 envelope remains valid for cofactor points x<P85. Substituting "
            "that exact frontier into the existing multiscale bridge moves the "
            "continuous cube-root-core forcing endpoint to k=2821231035570."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
