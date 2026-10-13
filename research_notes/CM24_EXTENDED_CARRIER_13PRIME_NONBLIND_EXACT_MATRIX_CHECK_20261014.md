# CM24 enlarged formal carriers: exact finite-field matrix cross-check

Status: **UNREVIEWED / NOT_ADMITTED / NONCANONICAL_EVIDENCE_ONLY**.
Date: 2026-10-14 (Asia/Taipei).
Provenance: this ChatGPT execution independently programmed finite-field checks after reading existing Source. **NONBLIND / SOURCE-AWARE**; no clean-independent-context assertion, native Driver session, DA, CLAIM, review disposition, or native Result freeze. This does not impersonate existing Driver `EM-DVR-FBF223` or any CM24 author.
Source under test: `awdawmip/enterprise-math@6152f02ed6420b243e812f39b55f013ffc502ce4:research_notes/CM24_EXTENDED_CARRIER_BN0_SOURCE_SURJECTIVITY_DIRECTION_20261013_FBF223.md`. The earlier Source proofs and fixed CM24 endpoint definitions remain independent obligations.
Control pins: `awdawmip/chatgpt-global-knowledge@675546aaf3e9128fe45f1fb6783757e707dc4ec1`, global P000 V4, historical fixed EM P000 `@4e318b1a978a4c4e26817752354cdd3e63ebee87`. Existing active-worldview constraints are unchanged.

## Exact executable mathematical scope

For primes `p = 6m+1` with `13 <= p <= 127`, `N=3m`, let
`q(x)=x(x-3)^2/4`, `(MF)_n = -[x^(N+n)]q'(x)F(q(x))`,
`1 <= n < N`. Work in **formal polynomials** over `F_p`,
`F(z)=sum(j=0..p-2) f_j z^j` and `B(z)=sum(b=0..p-2)b_b z^b`.
For the unchanged `D*`, compute `F_j=A_j b_(j+1)-D_j b_j`,
`A_j=(j+1)(j+3/2)`, `D_j=(j+2/3)(j+5/6)`, with
`b_(p-1)=0`. The test removes the column `b_N` to impose
`B_N=0`. No functional-polynomial quotient is taken.

The independent coefficient implementation uses
`q'(x)q(x)^j=3*x^j*(x-1)*(x-3)^(2j+1)/4^(j+1)`.
Writing `r=N+n-j` and `h_k=binom(2j+1,k)*(-3)^(2j+1-k)`,
where `h_k=0` outside `0<=k<=2j+1`, the matrix entry is
`M[n,j] = -3*4^(-j-1)*(h_(r-1)-h_r) (mod p)`.
The second matrix is `(M D*)[n,b] = -D_b M[n,b] + A_(b-1) M[n,b-1]`
(with the `b=0` predecessor zero), omitting `b=N`.
All divisions are modular inverses and all ranks use exact modular
Gaussian elimination.

It also checks **every** `s=1..m-1`, `j=0..p-2` against:
`Gamma_s(M z^j) = -9*4^(s-1)*1[j=p-s-1]`,
where `Gamma_s(y) = sum(k=0..2s) binom(2s,k)*(-3)^(2s-k)*y_(N-s-k)`.

## Executed outputs

| p | m | N | rank old M (degree < N) | rank enlarged M | rank M D* with B_N=0 | failed Gamma identities |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 6 | 4 | 5 | 5 | 0 |
| 19 | 3 | 9 | 6 | 8 | 8 | 0 |
| 31 | 5 | 15 | 10 | 14 | 14 | 0 |
| 37 | 6 | 18 | 12 | 17 | 17 | 0 |
| 43 | 7 | 21 | 14 | 20 | 20 | 0 |
| 61 | 10 | 30 | 20 | 29 | 29 | 0 |
| 67 | 11 | 33 | 22 | 32 | 32 | 0 |
| 73 | 12 | 36 | 24 | 35 | 35 | 0 |
| 79 | 13 | 39 | 26 | 38 | 38 | 0 |
| 97 | 16 | 48 | 32 | 47 | 47 | 0 |
| 103 | 17 | 51 | 34 | 50 | 50 | 0 |
| 109 | 18 | 54 | 36 | 53 | 53 | 0 |
| 127 | 21 | 63 | 42 | 62 | 62 | 0 |

13 primes; **10,956 exact Gamma equalities** checked with zero failures.
For every tested p, old-source rank is `2m`, enlarged-source rank is
`N-1`, and the full constrained composition `M D*` is also
surjective onto the `(N-1)` strict source coefficients. The last
result checks the stronger `B_N=0` assertion numerically; it is not
a proof for all eligible primes.

## Reproducer (Python 3; integer arithmetic only, no third-party packages)

```python
from math import comb

def primes_6m1(hi):
    return [p for p in range(13, hi + 1) if p % 6 == 1
            and all(p % d for d in range(2, int(p ** 0.5) + 1))]

def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def mr(p, n, j, N):
    r = N + n - j
    b1 = (binom(2*j+1, r-1) * pow(-3, 2*j+2-r, p)
          if 0 <= r-1 <= 2*j+1 else 0)
    b0 = (binom(2*j+1, r) * pow(-3, 2*j+1-r, p)
          if 0 <= r <= 2*j+1 else 0)
    return -3 * pow(4, -j-1, p) * (b1-b0) % p

def rankmod(M, p):
    a = [r[:] for r in M]
    k = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][j], -1, p)
        a[k] = [(x * inv) % p for x in a[k]]
        for i in range(k+1, len(a)):
            c = a[i][j]
            if c:
                a[i] = [(x - c*y) % p for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k

def test(p):
    m = (p-1)//6
    N = 3*m
    M = [[mr(p, n, j, N) for j in range(p-1)] for n in range(1, N)]
    half, third, sixth = (pow(d, -1, p) for d in (2, 3, 6))
    A = [(j+1)*(j+3*half) % p for j in range(p-1)]
    D = [(j+2*third)*(j+5*sixth) % p for j in range(p-1)]
    C = [[(-D[b]*M[i][b] + (A[b-1]*M[i][b-1] if b else 0)) % p
          for b in range(p-1) if b != N] for i in range(N-1)]
    failures = 0
    for s in range(1, m):
        for j in range(p-1):
            lhs = sum(binom(2*s,k)*pow(-3,2*s-k,p)*M[N-s-k-1][j]
                      for k in range(2*s+1)) % p
            rhs = (-9*pow(4,s-1,p)) % p if j == p-s-1 else 0
            failures += (lhs != rhs)
    return (p, m, N, rankmod([r[:N] for r in M],p),
            rankmod(M,p), rankmod(C,p), failures)

if __name__ == "__main__":
    for p in primes_6m1(127):
        print(*test(p))
        assert test(p)[3:] == (2*((p-1)//6), 3*((p-1)//6)-1,
                              3*((p-1)//6)-1, 0)
```

## Boundaries and handoff

These data support the **formal degree <= p-2** surjectivity/annihilator
claims for 13 specified primes only. They neither produce the fixed
original degree < N carrier, nor prove flat-gauge boundary/seed
compatibility, the CM24 target endpoint, a general algorithmic
speedup, physical transfer, or mother-goal closure.

The prior Source note itself discloses directed nonblind paper
checking; this test inherits Source awareness and is **not** an
independent native Driver reference pass. No official review,
reference, synthesis, follow-up, new Task, or Task state changes are
claimed here. The native Site-bound Driver identity gate remains
unavailable as observed in this execution; use an actually
authorized independent Driver and the current exact review set for
formal evaluation.

**Next finite scientific unit for the original owner/authorized
Driver:** derive and check a source-preserving flat-gauge boundary
and seed ledger for the enlarged carrier, including its full
half-prefix tail and class-19 top correction; compare against the
independently fixed `C/tau/F_CM`. A negative endpoint witness
must keep its exact coefficient provenance.

This file is neutral preservation of finite reproducible evidence,
not a substitute for any role-gated native transaction.
