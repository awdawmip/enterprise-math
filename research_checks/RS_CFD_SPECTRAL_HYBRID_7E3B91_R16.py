#!/usr/bin/env python3
"""Exact finite checker for R16 route-opportunity/payback certificate.

This is a finite cost-model verifier only. It does not run spectralDNS,
does not establish a CFD speedup, and does not change the frozen native
benchmark manifest.
"""
from fractions import Fraction


def direct_gain(N, L, m, D, S, G, A):
    """DenseTotal-HybridTotal for homogeneous matched-fallback model."""
    assert 0 <= m <= L <= N
    dense = N * D
    hybrid = m * S + (N - m) * D + L * G + A
    return dense - hybrid


def identity_gain(N, L, m, D, S, G, A):
    assert 0 <= m <= L <= N
    return m * (D - S) - L * G - A


def required_average_sparse_saving(H, m):
    if m <= 0:
        raise ValueError("m must be positive")
    return H / m


def cap_kills_positive_gain(M, U, H):
    """Sufficient kill gate when m<=M, sparse saving<=U, overhead>=H."""
    assert M >= 0 and U >= 0 and H >= 0
    return M * U <= H


def verify_exhaustive_homogeneous():
    count = 0
    for N in range(1, 9):
        for L in range(1, N + 1):
            for m in range(0, L + 1):
                for D2 in range(2, 9):
                    D = Fraction(D2, 2)
                    for S2 in range(0, D2):
                        S = Fraction(S2, 2)
                        for G2 in range(0, 5):
                            G = Fraction(G2, 2)
                            for A2 in range(0, 7):
                                A = Fraction(A2, 2)
                                g0 = direct_gain(N, L, m, D, S, G, A)
                                g1 = identity_gain(N, L, m, D, S, G, A)
                                assert g0 == g1
                                assert (g0 > 0) == (m * (D - S) > L * G + A)
                                if m:
                                    assert (g0 > 0) == (
                                        (D - S)
                                        > required_average_sparse_saving(L * G + A, m)
                                    )
                                count += 1
    return count


def verify_cap_gate():
    # Exact finite adversarial enumeration. Actual sparse count/saving is never
    # larger than the certified cap M/U. If the cap cannot repay H, positive
    # gain is impossible.
    count = 0
    for m in range(0, 7):
        for M in range(m, 7):
            for delta2 in range(0, 9):
                delta = Fraction(delta2, 2)
                for extra2 in range(0, 5):
                    U = delta + Fraction(extra2, 2)
                    for H2 in range(0, 25):
                        H = Fraction(H2, 2)
                        actual_gain_upper = m * delta - H
                        if cap_kills_positive_gain(M, U, H):
                            assert actual_gain_upper <= 0
                        count += 1
    return count


def r10_instantiations():
    # R10: N=20 calls; exact retained support is full by the end of RK4 step 1.
    # A conservative one-way dense latch therefore needs route guarding only on
    # the first L=4 RK4 RHS calls. Observed sparse counts were 2,2,1.
    N, L = 20, 4
    rows = []
    for seed, m in [(91001, 2), (91003, 2), (91007, 1)]:
        always_G = Fraction(N, m)
        latch_G = Fraction(L, m)
        setup_A = Fraction(1, m)
        rows.append(
            {
                "seed": seed,
                "N": N,
                "L": L,
                "m": m,
                "always_guard_required_avg": f"{always_G}*G + {setup_A}*A",
                "latched_required_avg": f"{latch_G}*G + {setup_A}*A",
                "guard_burden_reduction": f"{always_G-latch_G}*G",
            }
        )
    assert rows[0]["always_guard_required_avg"] == "10*G + 1/2*A"
    assert rows[0]["latched_required_avg"] == "2*G + 1/2*A"
    assert rows[2]["always_guard_required_avg"] == "20*G + 1*A"
    assert rows[2]["latched_required_avg"] == "4*G + 1*A"
    return rows


def main():
    n1 = verify_exhaustive_homogeneous()
    n2 = verify_cap_gate()
    rows = r10_instantiations()
    print(f"homogeneous_exact_cases={n1}")
    print(f"route_cap_exact_cases={n2}")
    for row in rows:
        print(row)
    print("R16 route-opportunity/payback verification: PASS")


if __name__ == "__main__":
    main()
