#!/usr/bin/env python3
"""PREFIX-964E exact signed-residual difference-set sieve.
Auxiliary named-XOR necessary support; source signs are not thereby validated.
Run with Python >=3.9 in an empty writable directory.
"""
import json
from pathlib import Path

PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"

def signed_residuals(p):
    groups = {}
    for i in range(p):
        for j in range(p):
            for s in (-1, 1):
                value = (1 << i) - s * (1 << j)
                groups.setdefault(value, []).append((i, j, s))
    return groups

def fiber_count(delta, m, p):
    """Exact count of (a,b) in Q_p^2 satisfying 2a-mb=delta."""
    N = 1 << (p - 2)
    H = 2 * N
    diff = delta - (2 - m) * (H + 1)
    if diff % 2:
        return 0
    W = diff // 2
    if m % 2:
        z0 = W % 2
        step = 2
        r0 = (W + m * z0) // 2
        slope = m
    else:
        if W % 2:
            return 0
        z0 = 0
        step = 1
        r0 = W // 2
        slope = m // 2
    if z0 >= N:
        return 0
    qmax = (N - 1 - z0) // step
    if slope == 0:
        return qmax + 1 if 0 <= r0 < N else 0
    qmin = max(0, -(r0 // slope))
    qmax = min(qmax, (N - 1 - r0) // slope)
    return max(0, qmax - qmin + 1)

def spectrum(p):
    N = 1 << (p - 2)
    D = signed_residuals(p)
    E = {C - c for c in D for C in D}
    supports = [sum(fiber_count(delta, m, p) for delta in E) for m in range(7)]
    R = N // 2
    q = (R - 3) // 3
    coarse = [N*N//2, N*N, N*N, (11*N*N+4)//12,
              N*N//2, (N*N-(-1)**p)//5,
              0 if q < 0 else (q+1)*(R-2) - 3*q*(q+1)//2]
    return dict(p=p, N=N, signed_residual_values=len(D),
                difference_values=len(E), supports=supports, coarse=coarse,
                removed=[x-y for x,y in zip(coarse, supports)],
                pass_percent=[round(100*y/x, 8) if x else None for x,y in zip(coarse,supports)],
                min_difference=min(E), max_difference=max(E))

def brute(p):
    N = 1 << (p - 2)
    H = 2 * N
    D = signed_residuals(p)
    E = {C-c for c in D for C in D}
    counts = [0] * 7
    for r in range(N):
        a = H + 2*r + 1
        for z in range(N):
            b = H + 2*z + 1
            for m in range(7):
                counts[m] += (2*a - m*b) in E
    return counts

def check_gap_zero(p):
    H = 1 << (p-1)
    D = signed_residuals(p)
    E = {C-c for c in D for C in D}
    actual = [a for a in range(H+1, 2*H, 2) if 2*a in E]
    expected = [H + (1<<r) - 1 for r in range(1,p-1)]
    assert actual == expected, (p, actual, expected)

def main():
    results = []
    for p in range(4, 11):
        row = spectrum(p)
        direct = brute(p)
        assert row["supports"] == direct, (p, row["supports"], direct)
        assert row["supports"][0] == (p-2)*row["N"]
        check_gap_zero(p)
        row["verification"] = "full ordered-pair direct enumeration + exact fibers"
        results.append(row)
    for p in (11, 12, 16, 19, 25):
        check_gap_zero(p)
    row = spectrum(19)
    assert row["supports"][0] == 17*131072
    row["verification"] = "distinct-difference exact integer fiber sum; direct gap-zero enumeration"
    results.append(row)
    output = {
        "schema": "PREFIX964E_R6_EXACT_RESIDUAL_DIFFERENCE_SUPPORT_V1",
        "frozen_science_pin": PIN,
        "status": "AUTHOR_COMPUTED_NOT_REVIEWED",
        "dictionary": "D_p={2^i-s*2^j:0<=i,j<p,s in {-1,+1}}",
        "difference_set": "D_p-D_p",
        "count_relation": "delta=(2-m)*(H+1)+4r-2mz",
        "evidence": results,
        "methods": {
            "small_widths": "p=4..10 independent ordered-pair brute vs O(1) fiber sum",
            "gap_zero": "p=4..12,16,19,25 direct first-modulus membership check",
            "p19": "deduplicated exact differences and bounded linear fibers",
            "claim_scope": "necessary support only; no original XOR signs or source multiplicity inferred"
        }
    }
    Path("PREFIX964E_R6_EXACT_RESULTS.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(row, indent=2))

if __name__ == "__main__":
    main()
