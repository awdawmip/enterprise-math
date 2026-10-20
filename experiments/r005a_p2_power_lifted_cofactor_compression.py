#!/usr/bin/env python3
"""Exact arithmetic audit for R005-A p=2 power-lifted cofactor compression.

The external premise is not re-proved here:
    every real x < 10^20 has a prime in (x, x+1724].

This verifier freezes the exact integer endpoint and the internal width/core
inequalities used by the symbolic proof.
"""

from __future__ import annotations

from math import isqrt
import json

G = 1724
X = 10**20
LOWER_K = 640_503_066
K_PL = 2_263_762_760_542
E1_ENDPOINT = 14_142_135_623
OLD_ENDPOINT = 11_661_903_789


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


def cube_core(k: int) -> int:
    return icbrt(k*k + 2*k)


def width_gate(k: int) -> bool:
    return G * cube_core(k) <= 2*k


def endpoint_gate(k: int) -> bool:
    return G * k**3 < 2 * X**2


def selected_power_lower_bound(q: int, k: int) -> tuple[int, bool]:
    """Finite sanity helper: largest q^e <= T=2k/G satisfies Q^2>=T.

    Uses the exact rational comparison G*Q^2 >= 2k rather than floating point.
    This helper is sampled only; the companion note gives the symbolic proof.
    """
    assert G*q <= 2*k
    Q = q
    while G * Q * q <= 2*k:
        Q *= q
    return Q, G * Q * Q >= 2*k


def main() -> None:
    assert not width_gate(LOWER_K - 1)
    assert width_gate(LOWER_K)

    assert endpoint_gate(K_PL)
    assert not endpoint_gate(K_PL + 1)

    # Exact strict-boundary formulation.
    assert G * K_PL**3 <= 2 * X**2 - 1
    assert G * (K_PL + 1)**3 >= 2 * X**2

    # At the endpoint the cube-root core is far inside the width budget.
    c3 = cube_core(K_PL)
    assert G * c3 <= 2 * K_PL

    # Deterministic samples across small, medium, and near-core q scales.
    # Primality is irrelevant to the power inequality itself; using integer
    # q values here pressure-tests the arithmetic lemma on a wider domain.
    samples = [2, 3, 5, 7, 11, 101, 1009, 50_000, 1_000_003, c3]
    power_rows = []
    for q in samples:
        if G*q > 2*K_PL:
            continue
        Q, ok = selected_power_lower_bound(q, K_PL)
        assert ok
        assert G*Q <= 2*K_PL
        # x=A/Q < X follows from Q^2 >= 2k/G and the endpoint gate.
        A = K_PL*K_PL
        assert A < X*Q
        power_rows.append({"q": q, "Q": Q})

    result = {
        "status": "R005-A P2 POWER-LIFTED COFACTOR COMPRESSION ARITHMETIC AUDIT / EXTERNAL GAP DATA NOT REPROVED",
        "gap_envelope_G": G,
        "external_cofactor_frontier_X": X,
        "width_gate_first_k": LOWER_K,
        "power_lifted_endpoint": K_PL,
        "endpoint_cuberoot_core": c3,
        "endpoint_width_margin": 2*K_PL - G*c3,
        "endpoint_cubic_margin": 2*X**2 - G*K_PL**3,
        "next_k_cubic_excess": G*(K_PL+1)**3 - 2*X**2,
        "previous_e1_endpoint": E1_ENDPOINT,
        "older_campbell_endpoint": OLD_ENDPOINT,
        "additional_indices_over_e1": K_PL - E1_ENDPOINT,
        "endpoint_factor_over_e1": K_PL / E1_ENDPOINT,
        "endpoint_factor_over_old": K_PL / OLD_ENDPOINT,
        "sampled_power_rows": power_rows,
        "symbolic_law": (
            "For q<=T=2k/G, the maximal q-power Q<=T satisfies Q>=sqrt(T). "
            "Thus x=k^2/Q<=sqrt(G/2)*k^(3/2). Combined with G*k^3<2*X^2, "
            "the external gap envelope forces every cube-root-core witness."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
