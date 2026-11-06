# D25 — Unimodular p-adic Newton source codec and second-digit residual witnesses

2026-11-07 Asia/Hong_Kong. **AUTHOR-SIDE PROVED ALGEBRA / FINITE EXACT TESTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.** TASK_RESEARCH scheduled lane logical ID: `chatgpt-research-hourly-enterprise-math-20260923`. This is a BRC auxiliary arithmetic observer, not a native six-axis or H0/B0/Frobenius experiment.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Predecessor author-side proof: `20261107_hourly20_d25_newton_provenance_exact_split.md` (rational normal/carry split and mod-p reconstruction). New here: ALL p-adic precision, lossless determinant certificate, optimal sampling and second-digit witnesses.

## Source-labelled model

For prime `p=6m+1`, put `a=2m,b=3m,c=4m=p-1-2m` and work in `A=Z_(p)` or `A_s=Z/p^s Z`. Let

```
w_j = (6j+1)(-1/2)^j binom(b,j)
f_j(t) = w_j binom(t-a,j) binom(t,j),        0<=j<=b
N(t) = sum_{0<=j<=a} f_j(t)                 [NORMAL source]
R(t) = sum_{a<j<=b} f_j(t)                  [CARRY source]
F(t) = N(t)+R(t)
q(t) = product_{i=0}^{c} (t-i)
e_t = F(t) (mod p^s), 0<=t<=p-1.
```

All coefficients are p-integral because j! and 2 are units. The earlier exact polynomial theorem gives `R=q C`, `deg N=c`, `deg C=2m-1`. The source labels j and the two aggregated bands are retained. Observer scope is recovery of N, R and polynomial operations on these aggregates; it does not assert reconstruction of each individual j-labelled summand from the two aggregates.

## Theorem 1: p scalar samples uniquely reconstruct both bands at every p-adic precision

For ALL primes `p=6m+1` and integers `s>=1`, the evaluation map

```
Phi_s : A_s[t]_{<=c} (+) A_s[t]_{<=2m-1} -> A_s^p,
  (N,C) |-> (N(t)+q(t)C(t))_{t=0}^{p-1}
```

is an isomorphism of free rank-p modules. Its inverse preserves **every p-adic digit** of precision: both the evaluation matrix and inverse lie in `GL_p(Z_p)`, and, under the minimum-coordinate valuation of a vector, equal-precision coefficient differences map to equal-precision sample differences.

**Proof.** In `A[t]`, the ordered basis `1,t,...,t^c,q(t),tq(t),...,t^(2m-1)q(t)` is unitriangular relative to `1,t,...,t^(p-1)` because q is monic of degree c+1. Evaluation at `0,...,p-1` yields the Vandermonde determinant `prod_{0<=i<j<=p-1}(j-i)`, a p-adic unit since all integer differences lie in `1,...,p-1`. Thus the determinant is a unit in `A_s` for every s and the matrix and inverse preserve the p-adic unit ball. For vectors x,y, both directions are 1-Lipschitz, hence `min_i v_p(x_i-y_i)=min_j v_p(Phi_s(x)_j-Phi_s(y)_j)` whenever the valuations are read modulo the precision cap s. The actual source polynomials N,C lie in `A[t]`; division by the monic q preserves integrality. QED.

## Theorem 2: two disjoint Newton spectra, lossless jet operator

Let `D_r = sum_{t=0}^r (-1)^(r-t) binom(r,t) e_t`, reduced modulo `p^s` for `0<=r<=p-1`. Because R vanishes on `0,...,c` and N has degree at most c, the EXACT recovered bands are

```
N(t) = sum_{r=0}^{c}     D_r binom(t,r)  (mod p^s)
R(t) = sum_{r=c+1}^{p-1} D_r binom(t,r)  (mod p^s).
```

With `H_n=sum_{i=1}^n i^{-1}` in `A_s`, the source-separated first derivative at t=c is

```
N'(c) = sum_{r=1}^{c} D_r binom(c,r) (H_c-H_{c-r}),
R'(c) = sum_{r=c+1}^{p-1} D_r (-1)^(r-c-1) c! (r-c-1)! / r!,
F'(c) = N'(c)+R'(c)                                  (mod p^s).
```

The second derivative kernel is the derivative of the single zero of `binom(t,r)` at `t=c`; every inverse in these formulas is a p-unit since r<p. No division by p or loss of precision occurs in source reconstruction or jet extraction. All identities hold over `Z_(p)` and then reduce to each `A_s`.

## Theorem 3: p scalar samples are optimal for the declared pair class

The unrestricted `(N,C)` module has `(c+1)+2m=p` independent coefficients over `F_p`. Any linear observer using fewer than p field samples has a nonzero kernel. An explicit p-1-sample ambiguity certificate is

```
G(t) = product_{i=0}^{p-2} (t-i), degree p-1.
G = N_G+q C_G  (Euclidean division by monic q).
```

Here `deg N_G<=c, deg C_G<=2m-1`. For t=0,...,p-2 the extra pair produces zero, but at t=p-1 it produces `(p-1)! = -1 (mod p)`, a unit. Thus p samples are necessary and sufficient for this unrestricted source-band observer, even at precision p^s. This is an optimality claim for that exact coefficient class, not for every constrained source family.

## Independent exact integer verification

Two Python-standard-library checkers, included beside this note, were executed:

1. `d25_padic_source_newton_20261107.py`: evaluates the original j-labelled finite sum at ALL p inputs modulo p^2 and p^3; reconstructs both aggregate polynomials by separated Newton coefficients; separately differentiates each labelled term and checks both recovered derivatives. Primes `7,13,19,31,37,61,73,109,229,373`, two precisions each: **20/20 PASS**, all scalar values and derivatives.
2. `d25_padic_tangent_scan_20261107.py`: a separate O(p)-per-prime modular recurrence for the original normal and carry derivatives, NOT a reuse of Newton samples. It inspected ALL 611 primes `7<=p<=10000, p=1 (mod6)` modulo p^2. In this finite range every total tangent is divisible by p and **none** is divisible by p^2. Cross-method comparison on the 20 full-sample instances: **20/20 PASS**.

For p=373, `N'(c)=62372, R'(c)=4768, F'(c)=67140=373*180 (mod 373^2)`; independent full-table reconstruction at p^3 gives `N'=7992725, R'=50786853, F'=6884461`. Examples of the observed second digit `(F'(c)/p) mod p`: p=13 ->12; p=19 ->18; p=109 ->40; p=229 ->68; p=373 ->180; p=5113 ->1216.

The Wieferich primes p=1093,3511 have `q_p(2)=0 (mod p)` but the auxiliary second digits equal **491** and **1678** respectively; these are exact counterexamples to an identity `F'(c)/p=K*q_p(2) (mod p)` with a single p-integral p-independent K at those points. No universal first-digit or second-digit theorem follows from the 611-prime scan.

## BRC meaning and continuation

The pre-compression carrier is the original integer j source, normal/carry label and valuations. The observer is the complete p-entry scalar table, the allowed future operations are polynomial arithmetic and derivatives modulo p^s, and the two-band reconstruction is exactly observer-safe under that declared scope. Full-table Newton computation is O(p^2) modular operations and O(p) working memory after the p original samples have been supplied; source sample generation is additional cost. This is not an algorithmic improvement over all arithmetic algorithms and not a native X6 transfer.

Next scientific unit: derive a source-labelled formula or exact counterexample for the second-digit correction `(F'(4m)/p) mod p` wherever the first digit vanishes. Seek the missing carry term beyond a Fermat-quotient-only expression. Any link to the frozen signed LIFT target requires an explicit observer map and the pinned original H0/B0/Frobenius experimental inputs. Mother target `Delta_p-R_p=0 (mod p)` for p=13,19 (mod24) remains OPEN.

## Native recovery

At 2026-11-07 ~04:24 Asia/Hong_Kong, Site phase `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; direct `em_status` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`. Old requests `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13` remain preserved without replay. Formal session, staging, current claim/run and Source checkpoint were not verified by this connection. Control support remains Enterprise Math #1558. Research here is portable author evidence, not a CLAIM, OPEN, formal checkpoint, Result or independent review.
