# PREFIX-1029 — Exact finite Bernstein coupling, strict convex order and quantitative spectral-scale gap

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1028. Status: AUTHOR_EXACT_PROOF / EXACT_INTEGER_RATIONAL_CHECKED / NOT_REVIEWED.

## Frozen scientific scope

Keep the same scientific source pin `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` (P000 V5). The Stage46 **candidate** signed 12-direction BRC observer uses `W=J12-6I12`, native X6 Cell coordinates, incoming `-e1`, forbidden bidirectional Link `{0,e1}`, exactly one negative outgoing step, and coherent Cell–terminal-port–grade amplitude sums *before* square-mass observation. All statements below concern the resulting observer's derived contrast moments and finite exchangeable Bernstein representation. They do not replace a native BRC transition or infer a physical trajectory.

Let `a_m=Q^+_{m+4,1}-Q^+_{m+4,2}` for `m>=1`, with formal spectral extension `a_0=2412`. The exact three-shift `A6` identity of PREFIX-1016/1026/1028 defines all `a_m`. Write
`E_{m,k}=sum_{i=0}^k (-1)^i binom(k,i)36^{k-i}a_{m+i}`.
PREFIX-1028 exhaustively established `E_{m,k}>0` for all `m,k>=0, m+k<=1200` (721801 pairs), with an actual integer witness digest and finite consistency certificate.

For `1<=n<=1200` let
`p_{n,j}=binom(n,j) E_{j,n-j}/(2412*36^n)`, `0<=j<=n`, and define a probability law
`P_n= sum_{j=0}^n p_{n,j} delta_{36j/n}`.
Thus the positive spectral approximation of PREFIX-1028 is `sigma_n=2412*P_n`.

## Theorem 1 — exact finite-scale coupling and strict convex-order monotonicity

For all integers `1<=n<N<=1200` there is an explicit coupling `(Y_n,Y_N)` with marginal laws `P_n,P_N` and
`E[Y_n | Y_N]=Y_N`.
Consequently for every continuous convex `phi:[0,36]->R`,
`int phi dP_N <= int phi dP_n`.
The inequality is strict for **every strictly convex** `phi`, whenever `n<N`. In symbols `P_N <_cx P_n` (strict convex order).

**Proof.** PREFIX-1028's exact consistency defines a positive exchangeable distribution on binary strings of length `N`, with mass `p_{N,j}/binom(N,j)` on each string containing `j` ones. Its first `n` bits have the prescribed law `p_{n,m}`: iterate the adjacent deletion identity already proved there. Put `Y_n=(36/n)sum_{i=1}^n X_i`, `Y_N=(36/N)sum_{i=1}^N X_i`. Given the total number of ones, all placements are equally likely, so `E[sum_{i<=n}X_i | sum_{i<=N}X_i]=n*(sum_{i<=N}X_i)/N`. Thus the conditional expectation identity follows. Jensen proves convex order. Strictness follows because `p_{N,j}>0` at each interior `1<=j<=N-1`: for `n<N`, a hypergeometric subsample of any such `j` has nonzero conditional variance, hence conditional Jensen is strict for a strictly convex function. QED.

This is a finite-horizon statement for every pair of levels through 1200, not an unproved infinite exchangeable extension.

## Theorem 2 — exact mean, variance and L2/Wasserstein bounds

For every `1<=n<=1200`,
`E[Y_n]=a_1/a_0=2135/201`, and
`Var(Y_n)=1907744/40401 +(14897/67)/n`.

For `1<=n<N<=1200`, the above explicit coupling obeys
`E[(Y_n-Y_N)^2]=(14897/67)(1/n-1/N)`.

Accordingly the Wasserstein distances satisfy
`W_2(P_n,P_N)^2 <= (14897/67)(1/n-1/N)` and
`W_1(P_n,P_N) <= sqrt((14897/67)(1/n-1/N))`.
For a 1-Lipschitz test function `f`, the unnormalized measures satisfy
`|int f d(sigma_n)-int f d(sigma_N)| <= 2412 sqrt((14897/67)(1/n-1/N))`.

**Proof.** PREFIX-1028's exact factorial-moment identity at degrees `d=1,2` yields
`E[Y_n]=a_1/a_0` and
`E[Y_n^2]=a_2/a_0+(36a_1-a_2)/(a_0 n)`.
The three exact BRC-observer integers are `(a_0,a_1,a_2)=(2412,25620,386028)`. Hence `(36a_1-a_2)/a_0=536292/2412=14897/67`, and direct rational simplification gives the stated baseline variance. Theorem 1 makes the coupling orthogonal in `L^2`:
`E[(Y_n-Y_N)^2]=E[Y_n^2]-E[Y_N^2]`.
This proves the equality. Since Wasserstein distances are infima over all couplings, this particular coupling provides the stated upper bounds; Cauchy–Schwarz gives `W_1<=W_2` and the Lipschitz estimate. QED.

For `phi in C^2([0,36])` with `u<=phi''(y)<=v` over the interval, the same coupling and Taylor's integral remainder yield the **sharp curvature sandwich**
`(u/2)C(1/n-1/N) <= E[phi(Y_n)]-E[phi(Y_N)] <= (v/2)C(1/n-1/N)`,
where `C=14897/67`. Quadratic `phi` attains equality. In particular the approximate spectral measures become strictly less spread out in convex order as the exchangeable horizon grows, with a completely explicit finite-scale modulus.

## Independent exact BRC-observer check

A runnable exact-integer and Fraction companion recomputes `A6` from the published recurrence and `a_m` from the published three-shift formula, enumerates the full finite triangle at `N=240`, and recovers PREFIX-1026's independent baseline digest:
`ba12049d9510eabf3abef8326249de88d7edcfdf88f1d990d2539a51bae8afc8`
for `m>=1`. The extended `m>=0` digest is
`e1bd2ff6d0926241a991cd5b5bb3266abc146ad323103d34633fb4e6840b13a9`.
It checks positivity on all 29161 pairs; normalization, means and exact variances at `n=1,2,10,30,100,240`; and the deletion identity for the selected adjacent levels `n=2`. The `n=10,N=240` coupling variance gap is exactly `342631/16080`. The source and certificate are companion files in this directory.

The mathematical proof of Theorems 1–2 applies for all `N<=1200` based on the previously verified PREFIX-1028 triangle; this independent run covered `N<=240`. Neither is a claim of all-degree Hausdorff positivity, of an infinite exchangeable law, or of a new native BRC computation beyond the inherited coherent observer. Verification status: author derivation and exact finite check; independent mathematical review remains NOT_REVIEWED.

## New discriminating next step

The open positive-measure problem is whether `E_{m,k}>=0` for every `m,k>=0`, especially proportional simultaneous growth. A direct next unit is to derive a signed spectral density for PREFIX-1026's functional `nu` on regular interior subintervals, then prove its sign there or obtain an exact negative Bernstein witness. If global positivity is later established, the finite convex-order family extends consistently to every level and admits a genuine limiting mixing law; that consequence is currently conditional.

Historical provenance: `EM-DIRECT-FBEA5D`, `RA-3FB2D033BE6048D8712FF056`, original `MCP-45ad6d29cd534c1aad25595a72e3c532` (not evidence of current authenticated capability or formal owner). The mother problem `B_fix,odd(32) in {19,20}` stays open. No new CLAIM, PROGRESS, Result, Review or P000 change is asserted.
