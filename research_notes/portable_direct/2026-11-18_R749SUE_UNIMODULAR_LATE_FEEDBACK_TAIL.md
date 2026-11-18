# R749SUE — Unimodular late-resolution tails of the two-Port BRC feedback quotient

Date: 2026-11-18 (Asia/Shanghai). Research status: AUTHOR_EXACT_NOT_REVIEWED. Independent portable continuation of R749SUD (source commit `fff3ca187002507fa702fd6e0d293feae8533a7c`). Frozen scientific baseline: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; WBRC-T30–T32 and P000 remain unchanged. This is a typed auxiliary positive-rational recurrent Port result, not an assertion of a physical native X6 event.

## Exact setting

Use the R749SUD two-labeled-Port model, integer resolution `K>M>=1`, four ordered nonnegative rational Port-star entries, and resettable tests adding edge `j/K` for `j=1,...,M`. `N(2,K,M)` is the count of realizable four-Port binary signatures. The preceding exact theorem establishes
```
N_inf(M) = (2M+1)(2M^2+2M+1) + (M^4-E_M)/2,
E_M = M^2 + 2 sum_{h=2}^M phi(h) floor(M/h)^2,
```
and a positive-bin four-tuple `(u,v,a,d) in [1,M]^4` with `ad>uv` is realized exactly when
```
K(ad-uv) > max(u,v) ad .
```
The strict inequality is essential: equality of the feedback stability threshold is unstable. Theorem B of R749SUD gives first saturation `K_*(1)=2`, `K_*(2)=5`, `K_*(M)=M(M-1)^2+1` for `M>=3`.

## Theorem 1. Exact unimodular representation of the late unsaturated tail

For every integer `M>=1` and `K>M` with `2K>M^3`:
```
D_M(K):=N_inf(M)-N(2,K,M)
      = #{(a,d,u,v) in [1,M]^4:
           ad-uv=1 and K<=max(u,v)*ad }.
```
Thus every signature still missing in this late regime corresponds to a **positive unimodular integer matrix**, with determinant `ad-uv=1`.

**Proof.** From R749SUD, all missing signatures are exactly the strictly positive product differences `delta=ad-uv>=1` for which `K delta<=max(u,v)ad`. If `delta>=2`, then `max(u,v)ad/delta<=M^3/2<K`. Therefore `delta=1` is necessary and sufficient for a missing signature under `2K>M^3`. No change of the underlying BRC physical or observation model is made. QED.

This is an exact finite-dimensional arithmetic classification, not a statistical identification of matrix states. The original four-star feasibility theorem supplies the independent realizability correspondence.

## Theorem 2. Exact total population of positive determinant-one classes

Let
```
H_M=#{(a,d,u,v) in [1,M]^4 : ad-uv=1}.
```
Then for every integer `M>=1`,
```
H_M = 4 sum_{n=1}^M phi(n) - 2M - 2.
```
Consequently in the late regime `0<=D_M(K)<=H_M`, and, using the elementary summatory totient identity,
```
H_M = (12/pi^2) M^2 + O(M log M).
```
In particular, the late-resolution undecided classes are at most quadratic in the feedback budget `M`, against `N_inf(M)~M^4/2`.

**Proof.** At `M=1` the set is empty. For `M>=2`, partition newly admitted matrices according to which of the four entries first attains the maximum `M`. Two different entries cannot both equal `M`: if they share a row/column, their determinant is divisible by `M`, while if opposite entries are both `M`, the determinant-one equation is impossible with every other entry at most `M` (for `M>=2`).

If `a=M`, choose any `u` coprime to `M` in `1,...,M-1`; the congruence `uv=-1 mod M` determines a unique `v in [1,M-1]`, and `d=(uv+1)/M` is in `[1,M]`. This contributes `phi(M)` cases. The symmetric position `d=M` contributes `phi(M)` again.

If `u=M`, choose `a in [1,M-1]` coprime to `M`; the unique inverse `d in [1,M-1]` gives `v=(ad-1)/M`. The unique choice `a=d=1` has `v=0` and is excluded; hence `phi(M)-1` cases. Similarly `v=M` contributes `phi(M)-1`. Thus `H_M-H_{M-1}=4phi(M)-2`. Summing this recurrence from `H_1=0` proves the formula. The asymptotic follows from `sum_{n<=M}phi(n)=3M^2/pi^2+O(M log M)`, itself obtained by substituting `phi(n)=n sum_{d|n}mu(d)/d` and summing divisors. QED.

## Theorem 3. Exactly two signatures remain one K-step before sharp saturation

For all integers `M>=2`:
```
N_inf(M)-N(2,K_*(M)-1,M)=2;
N_inf(M)-N(2,K_*(M),M)=0.
```
The second equality is the previously established sharp saturation theorem. The new first equality identifies the exact terminal jump as **two jointly-realizable response signatures**.

**Proof.** For `M>=4`, set `T=M(M-1)^2=K_*(M)-1` and `p=ad,q=uv,delta=p-q>0`. If `delta>=2`, the threshold `max(u,v)p/delta<=M^3/2<T`; hence such a candidate is already realized at `K=T`. For `delta=1`, the integer threshold is `max(u,v)p`. If `p<=(M-1)^2`, it is at most `T`, with equality only when `a=d=M-1`, `max(u,v)=M` and `uv=(M-1)^2-1=M(M-2)`. There are exactly two solutions `(u,v)=(M,M-2),(M-2,M)`. If `p>(M-1)^2`, at least one of `a,d` equals `M`, so `p` is `M(M-1)` or `M^2`. The greatest smaller product of two entries at most `M` is at most `(M-1)^2` in the first case, or `M(M-1)` in the second; thus `delta>=M-1` or `delta>=M` respectively, and the threshold is at most `M^2<T`. Therefore precisely those two threshold-equality tuples remain missing when `K=T`.

For `M=2` and `M=3` the finite positive-bin inequalities give respectively `D_2(4)=2` and `D_3(12)=2`, directly confirmed by enumerating `[1,M]^4`. The saturation theorem supplies the zero deficits at the next grid resolution. QED.

## Efficient exact enumeration and validation

The determinant-one condition also implies `gcd(a,u)=1`. For each coprime `(a,u)`, solve `a d =1 (mod u)`, with least positive solution `d_0`, and `v_0=(a d_0-1)/u`. Every positive solution is `d=d_0+t u, v=v_0+t a`, with integer `t` chosen to keep `1<=d,v<=M`. This is a reproducible integer algorithm with `O(M^2 log M+H_M)` elementary arithmetic using Euclid inverses and solution enumeration; apply `K<=max(u,v)ad` to count the late deficit. The supplied dependency-free JavaScript certificate instead uses simpler `O(M^3)` bounded loops to avoid reliance on an inverse implementation.

The certificate independently compares the old three-sum exact signature count with the new unit-determinant count in the late regime and checks `H_M=4sum phi-2M-2`, as well as the two-class terminal jump. Checked `M=1,...,32`; 154 grid/late-comparison cases, 32 totient identity cases and 31 terminal-step cases all PASS. Integer inputs remain safely below the JavaScript exact-integer limit in this declared finite test domain. The general theorems are established by the proofs above, not extrapolated from these checks.

Representative exact pairs:
| M | K | N_inf | Missing D_M(K) | H_M |
|---:|---:|---:|---:|---:|
| 10 | 501 | 9502 | 4 | 106 |
| 10 | 810 | 9502 | 2 | 106 |
| 10 | 811 | 9502 | 0 | 106 |
| 16 | 2049 | 50337 | 6 | 286 |
| 24 | 6913 | 223689 | 18 | 670 |
| 32 | 16385 | 659657 | 32 | 1230 |
| 32 | 30752 | 659657 | 2 | 1230 |
| 32 | 30753 | 659657 | 0 | 1230 |

## Evidence scope and next research

**Scope:** finite stable positive-rational two-Port Schur/BRC contexts with resettable feedback observations; native X6 six-axis Cell, causal time, triadic closure, resource and source-history licensing remain separate. **Review:** author exact proof and independent finite exact integer checks, no outside review or formal proof. **Novelty:** reuse of R749SUD's sharp grid count and classical unimodular/totient facts; the new specific late-deficit correspondence and terminal class jump are the increment.

The next discriminating question is to compute the exact deficit staircase for `K` between `M^3/2` and `K_*(M)`, using the positive unimodular matrices and their `max(u,v)ad` thresholds, then compare this feedback quotient with genuinely licensed Port contexts containing resource/time/source constraints.