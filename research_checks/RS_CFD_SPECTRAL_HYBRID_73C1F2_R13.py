#!/usr/bin/env python3
"""Exact finite-cost checker for CFD guarded sparse/FFT routing R13.

This checker proves only algebraic equivalence for a declared additive finite-cost
model and checks frozen 2026-09-16 native-host summary numbers. It is not a PDE,
performance-portability, or causal speedup proof.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 40

OBSERVED = [
    {"n":16,"case":"shear","dense_ms":"113.296","hybrid_ms":"25.563","sparse_calls":49,"fft_calls":0},
    {"n":16,"case":"taylor_green","dense_ms":"113.177","hybrid_ms":"108.148","sparse_calls":3,"fft_calls":46},
    {"n":16,"case":"random32","dense_ms":"111.922","hybrid_ms":"112.125","sparse_calls":1,"fft_calls":48},
    {"n":16,"case":"edge","dense_ms":"112.976","hybrid_ms":"25.675","sparse_calls":49,"fft_calls":0},
    {"n":32,"case":"shear","dense_ms":"366.195","hybrid_ms":"64.608","sparse_calls":49,"fft_calls":0},
    {"n":32,"case":"taylor_green","dense_ms":"373.831","hybrid_ms":"349.573","sparse_calls":3,"fft_calls":46},
    {"n":32,"case":"random32","dense_ms":"365.820","hybrid_ms":"364.909","sparse_calls":1,"fft_calls":48},
    {"n":32,"case":"random256","dense_ms":"361.778","hybrid_ms":"360.303","sparse_calls":0,"fft_calls":49},
]


def dense_cost(N, D):
    return Fraction(N) * Fraction(D)


def hybrid_cost(N, D, S, G, A, k):
    """Homogeneous model: k dense fallbacks among N decisions."""
    return Fraction(A) + Fraction(N) * Fraction(G) + Fraction(N-k) * Fraction(S) + Fraction(k) * Fraction(D)


def wins_by_criterion(N, D, S, G, A, k):
    D, S, G, A = map(Fraction, (D, S, G, A))
    if D <= S:
        return False
    return Fraction(N) * G + A < Fraction(N-k) * (D-S)


def ceil_fraction(x):
    x = Fraction(x)
    return -((-x.numerator) // x.denominator)


def k_max_strict(N, D, S, G, A):
    """Largest integer fallback count k for which the homogeneous hybrid wins."""
    D, S, G, A = map(Fraction, (D, S, G, A))
    if D <= S:
        return -1
    r = Fraction(N) - (Fraction(N)*G + A)/(D-S)
    return max(-1, min(N, ceil_fraction(r)-1))


def exhaustive_equivalence():
    checks = 0
    for N in range(1, 7):
        for D in range(1, 8):
            for S in range(0, D+2):
                for gnum in range(0, 7):
                    G = Fraction(gnum, 3)
                    for A in (Fraction(0), Fraction(1,2), Fraction(2), Fraction(5,3)):
                        winners = []
                        for k in range(N+1):
                            direct = hybrid_cost(N,D,S,G,A,k) < dense_cost(N,D)
                            derived = wins_by_criterion(N,D,S,G,A,k)
                            assert direct == derived
                            if direct:
                                winners.append(k)
                            checks += 1
                        expected = max(winners) if winners else -1
                        assert k_max_strict(N,D,S,G,A) == expected
    return checks


def pathwise_identity(dense, sparse, sparse_mask, guards, delta_setup):
    """Verify D-H = sparse-opportunity savings - guard/setup overhead pathwise."""
    assert len(dense) == len(sparse) == len(sparse_mask) == len(guards)
    dense_total = sum(map(Fraction, dense))
    hybrid_total = Fraction(delta_setup)
    sparse_savings = Fraction(0)
    guard_total = sum(map(Fraction, guards))
    for d,s,use_sparse in zip(dense,sparse,sparse_mask):
        d,s = Fraction(d), Fraction(s)
        if use_sparse:
            hybrid_total += s
            sparse_savings += d-s
        else:
            hybrid_total += d
    hybrid_total += guard_total
    assert dense_total - hybrid_total == sparse_savings - guard_total - Fraction(delta_setup)
    return dense_total - hybrid_total


def pathwise_examples():
    # Heterogeneous costs: fallbacks cancel exactly under matched fallback cost.
    a = pathwise_identity([10,12,9,11],[2,3,4,5],[1,0,1,0],[1,1,1,1],2)
    assert a == Fraction(9)
    # All-fallback case has no sparse arithmetic opportunity. Any positive measured
    # aggregate delta in real data therefore cannot be attributed to sparse compute.
    b = pathwise_identity([10,12],[1,1],[0,0],[0,0],0)
    assert b == 0
    return 2


def observed_certificate():
    out=[]
    for row in OBSERVED:
        D=Decimal(row["dense_ms"]); H=Decimal(row["hybrid_ms"])
        margin=D-H
        calls=row["sparse_calls"]+row["fft_calls"]
        assert calls == 49
        rec=dict(row)
        rec["fallback_fraction"] = str(Decimal(row["fft_calls"])/Decimal(calls))
        rec["observed_total_margin_ms"] = str(margin)
        rec["observed_margin_fraction_of_dense"] = str(margin/D)
        rec["sparse_attribution_identifiable_from_aggregate_total"] = False
        if row["sparse_calls"] == 0:
            rec["exact_sparse_arithmetic_attribution_ms"] = "0"
            rec["interpretation"] = "ALL_FALLBACK_NEGATIVE_CONTROL: aggregate delta is non-sparse baseline/setup/timing effect"
        else:
            rec["exact_sparse_arithmetic_attribution_ms"] = None
            rec["interpretation"] = "TOTAL_MARGIN_ONLY: paired per-decision counterfactual costs are required for causal sparse attribution"
        out.append(rec)
    # Frozen all-fallback control: 0 sparse calls but a +1.475 ms aggregate median delta.
    ctrl=[r for r in out if r["n"]==32 and r["case"]=="random256"][0]
    assert ctrl["sparse_calls"] == 0 and ctrl["fft_calls"] == 49
    assert Decimal(ctrl["observed_total_margin_ms"]) == Decimal("1.475")
    assert ctrl["exact_sparse_arithmetic_attribution_ms"] == "0"
    return out


def main():
    eq = exhaustive_equivalence()
    ex = pathwise_examples()
    obs = observed_certificate()
    print("PASS")
    print(f"homogeneous_exact_checks={eq}")
    print(f"pathwise_identity_examples={ex}")
    for r in obs:
        print(r)

if __name__ == "__main__":
    main()
