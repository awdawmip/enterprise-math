# X6 Unit131 — exact stratum boundary: R063 two-axis charts versus full signed X6 G-shell

**2026-11-18; mother:** PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; **Task:** RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. **Research lane:** chatgpt-research-onhour-enterprise-math-20260923. **Status:** AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Verified source and scope

Retain P000 V5 and signed X6 at frozen scientific commit 59538f585d037d09ef687b28715c4bc1a3f9fe03. Original current R063 code experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py, blob 643b2bac659a445891dcb5588b647972977104e0, lines 136–149, defines positive ordered roots at *square* norm r² and path_fiber_size((a,b))=C(a+b,a). The actual current adapter research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py, blob db46dde5a962b93b65775bf2b4d8f52d5e3f83b9, embeds 15 named axis pairs and four sign choices, deducting 108 repeated signed axial chart incidences for r>0.

The following theorem extends the mathematical *typed chart union* to arbitrary integer squared norm N. It does not edit or recharacterize the old R063 benchmark's input domain. The general combinatorial parameter d>=2 is distinct from the frozen *native* six spatial axes d=6.

## Exact signed chart fiber theorem

Fix d>=2, N>=0. Let R_+(N) be all ordered nonnegative pairs (a,b) satisfying a²+b²=N. For each distinct named i<j, signs s,t in {−1,+1}, and (a,b) in R_+(N), form the signed native displacement z=s*a*e_i+t*b*e_j. Retain each six-field source label (i,j,s,t,a,b) separately from its image z. Let f_N(z) be the number of such labels, let C_d(N) count unique images, and let M_d(N) be their natural shortest-path BRC mass, where

\[
L(z)=\sum_k|z_k|,\quad B_{\min}(z)=\frac{L(z)!}{\prod_k|z_k|!},\quad
R(N)=|R_+(N)|,\quad H(N)=\sum_{(a,b)\in R_+(N)}\binom{a+b}{a}.
\]

For N>0 the fiber degree equals 1 on every support-two state and equals 2(d−1) on each nonzero axial state. Such axial states exist iff N is a positive square, and there are exactly 2d of them. Consequently

\[
\boxed{C_d(N)=4\binom d2R(N)-2d(2d-3)\mathbf1_{N=\square}},\qquad
\boxed{M_d(N)=4\binom d2H(N)-2d(2d-3)\mathbf1_{N=\square}}.
\]

For N=0 there is just the zero Cell: C_d(0)=M_d(0)=1, whereas label count and label-weight total are 4*C(d,2). In native signed X6, the positive-square correction is 108; for nonsquare positive N it is 0.

**Proof.** A displacement supported on two different nonzero axes uniquely specifies i,j, signs and magnitudes. A displacement ±r e_i instead allows (d−1) choices of unused second axis and 2 unused sign choices, hence exactly 2(d−1) source labels; all others occur once. The excess over one copy across 2d axial states is 2d[2(d−1)−1]=2d(2d−3). Each positive-root source has path count C(a+b,a)=B_min(z), and the axial BRC is 1. For N=0 every source produces the zero displacement with BRC 1. QED.

## Full native shell deficit and sharp first missing state

Let S_6(N)={z∈Z⁶: Σz_i²=N}. The signed two-axis chart union is *exactly* the subset of S_6(N) whose coordinate support is ≤2. Missing native endpoints and their N-BRC mass therefore come precisely from support≥3. At N=0,1,2 the chart union is complete. At N=3, all 160 native endpoints have three ±1 coordinates, each of BRC 6, so first missing mass is 960.

At G=25, independent exact arithmetic gives:

| Population | Endpoint count | N-BRC mass |
|---|---:|---:|
| 60 labeled pair/sign chart families, axial duplications retained | 240 | 4,320 |
| Unique signed X6 states in chart image, support ≤2 | 132 | 4,212 |
| Full six-axis signed native G=25 shell | 7,812 | 2,538,954,612 |
| Native states outside pair charts, support ≥3 | 7,680 | 2,538,950,400 |

This population is also distinct from the signed *three-axis* G=25 shell (30 endpoints, BRC 846) and the historical positive-sector subtotal (72).

## Actual reproducible check

- [Executed checker](../research_checks/X6_UNIT131_NORM_CHART_STRATIFIED_FIBERS_CHECK_20261118.py), immutable commit 65f71b16a055049e198ef3f9996e951977a4b337, blob 1e9c0d536d9d244ec946938d338089353f2aae7f.
- [Exact integer certificate](../research_checks/X6_UNIT131_NORM_CHART_STRATIFIED_FIBERS_RESULTS_20261118.json), immutable commit 62e6a7be2813e1a8c31652f66880b849f7dfbb57, blob 39f6a83884d08a7ee2dc562220a0b453ef10f14f.

The checker enumerates exact source fibers for d=2..8, N=0..200 (1,407 cases), and uses a separate native six-axis dynamic program for G=0..200. Its state is (G,L,count,mass); appending coordinate magnitude k inserts its k signed steps among L existing steps in C(L+k,k) ways and multiplies by 2 for k>0. Direct exhaustive signed six-axis enumeration at G=0..9 and G=25 checks that DP independently (the latter covers all 11^6 integer vectors in [−5,5]^6). Local CPython 3.13.5 subprocesses in normal, -O and -OO each exited 0 and emitted byte-identical 2,986-byte JSON, SHA256 26bcf516557f657af85a6b8e1c04b836e77be5c10d2f1231d7d74b02b46a3bd0. All mathematical checks are always-on.

The previously completed six-file, 512-case original R063/Helly benchmark was **not rerun** in this unit. Independent Driver review and Issue #2416 remain separate.

## Task-ledger disposition and frontier

PRESERVE_CARRIER / PRESERVE_PATH_BRC for R063 positive ordered roots and their word counts; PRESERVE_NATIVE for the *explicitly lifted* signed support≤2 images; SUPERSEDE any use of repeated labels as different native Cells, or of the two-axis image as the whole signed-six-axis shell. The current square-radius adapter already repairs the 108 axial duplication; this unit supplies a universal N stratification, N=0 correction and quantified full-shell deficit. Historical wrong-native LP011 argmax and natural-positive LP019 subtraction callers remain UNRESOLVED_PROVENANCE. Next: exact 28-LP source:line consumer ledger; locate those two alleged historical callers or return exact absence of reliable provenance; preserve independent Driver review. Original Native PROGRESS request onhour-20261118-1707-x6-own-units126-127-native-progress-v1 must be reconciled before overlapping same-run publication.
