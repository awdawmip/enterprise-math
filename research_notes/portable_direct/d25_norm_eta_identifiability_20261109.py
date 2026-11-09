#!/usr/bin/env python3
"""D25 signed rank-one normalization audit, exact modular integers only.
This is a portable author-side diagnostic, NOT a native H0/B0 computation.
"""
from collections import Counter
from math import gcd


def exhaustive_norm_fibers(p: int) -> None:
    m = p * p
    counts = Counter((a*a - 2*b*b) % m for a in range(m) for b in range(m))
    units = [v for v in range(m) if v % p]
    nonzero_multiples = [v for v in range(p, m, p)]
    assert pow(2, (p-1)//2, p) == p-1  # inert quadratic algebra
    assert len(units) == p*(p-1)
    assert all(counts[v] == p*(p+1) for v in units)
    assert all(counts[v] == 0 for v in nonzero_multiples)
    assert counts[0] == p*p
    assert sum(counts.values()) == m*m
    print(f"p={p}; total={m*m}; unit norm outputs={len(units)}; "
          f"unit fiber size={p*(p+1)}; norm=0 fiber={p*p}")


def target_373() -> None:
    p = 373
    m = p*p
    a, b = 92060, 21788  # PREVIOUSLY author-computed ordinary Hesse candidate
    norm = (a*a-2*b*b) % m
    assert norm == 122102 and norm % p == 131
    assert pow(2, (p-1)//2, p) == p-1
    assert pow(131, (p-1)//2, p) == p-1  # non-square: scalar-conjugacy obstruction
    eta0, eta1 = 89901, 6579
    eta_norm = (eta0*eta0 - 2*eta1*eta1) % m
    assert eta_norm == 18818 and norm * eta_norm % m == 1
    assert (a*eta0+2*b*eta1) % m == 1
    assert (a*eta1+b*eta0) % m == 0
    matrix = ((a % p, (-2*b) % p), (b % p, (-a) % p))
    determinant = (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]) % p
    assert matrix == ((302, 65), (154, 71)) and determinant == 242
    print("p=373; m=139129; ordinary source candidate=92060+21788*T; "
          "norm=122102; norm mod373=131; Legendre=-1")
    print("norm-one normalizer eta=(89901+6579*T), norm(eta)=18818; "
          "eta*a=1 mod139129; normalized norm=1")
    print(f"sigma-semilinear matrix mod373={matrix}; det={determinant}")

if __name__ == '__main__':
    for p in (13, 19):
        exhaustive_norm_fibers(p)
    target_373()
    print("PASS: exact exhaustive norm-fiber and source-normalization checks")
