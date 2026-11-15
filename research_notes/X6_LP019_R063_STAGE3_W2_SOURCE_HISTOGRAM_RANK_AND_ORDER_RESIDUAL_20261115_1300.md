# X6 LP019 — R063 Stage3 W2 来源直方图秩与有序来源残差（2026-11-15 13:00 HKT）

**Parent:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2`, own Researcher `EM-X6-FB6990`; P000 V5 and native signed Cell-torsor scientific baseline fixed at `59538f585d037d09ef687b28715c4bc1a3f9fe03`. **Status:** AUTHOR-PROVED / EXACT FINITE INTEGER CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Problem and exact source

This is the *smallest source/observer factorization subproblem* left by the W2 investigation: does the original Stage3 source-conditioned **formal witness histogram** preserve which ordered source pair generated a target word? The prior #31 result concerned Boolean support and minimum source covers. This result concerns **all integer coefficients** and the complete kernel of a linear observer.

Read the actual frozen R063 Stage3 source `awdawmip/enterprise-math@69b7a90328bdb72852d47b338dedd7b276740ac9:scripts/r063_stage3_validate_pairwise_interaction_process.py` (Git blob `4fca0c160acaa2b5d257d9bc1aefe82e1e3f4636`), especially `interaction_cells`, `residual_sets`, `linext_word_counts`, `relation_weights` at original lines 26–57. The existing executed W2 baseline is `research_checks/X6_LP019_R063_STAGE3_W2_MINIMAL_SOURCE_COVER_CHECK_20261115_1200.py` at `df3fdfd9c2a2c8d7caed370fafa0c15933b067e1` (Git blob `429494cee9124334a81b9d59b405f549f40b7904`).

Take source word set (W=\{\mathtt{iij},\mathtt{iji},\mathtt{jii}\}) and target words (V=\{w:\#i(w)=3,\#j(w)=4\}), so `|W|=3`, `|V|=35`. For each *ordered* pair ((p,q)\in W^2), define (H_{pq}(w)\in\mathbb N) to be the exact integer coefficient returned by `relation_weights(p,q)`, with zero on absent words. The linear observer on nonnegative integer source-pair counts (n\in\mathbb N^{9}) is (T(n)=\sum_{p,q}n_{pq}H_{pq}\in\mathbb N^{35}).

The formula is scoped to this frozen Stage3 **positive two-generator chart**: a named native three-axis slice may embed target endpoint as (3e_a+4e_b+0e_c) (other native coordinates explicitly zero). `H` counts derived **formal process witnesses**, not natural signed-X6 N-BRC shortest paths, nor original Stage0 C3/C4 benchmark outcomes.

## Exact theorem: rank six and complete three-dimensional order kernel

1. The Stage3 histograms satisfy (H_{pq}=H_{qp}) for every (p,q\in W).
2. Of the six histograms (H_{pp}) and (H_{pq}) with (p<q) (lexicographic word order), **all six are linearly independent over** (\mathbb Q). Consequently the (9\times35) integer matrix (H) has rank **6** and kernel dimension **3**.
3. Using row ordering `(iij,iij), (iij,iji), (iij,jii), (iji,iji), (iji,jii), (jii,jii)`, and target column ordering `iiijjjj, iijijjj, ijijijj, jiijijj, jiijjij, jjijiji`, the exact (6\times6) witness minor is

```text
[36,30,8,0,0,0]
[ 0, 2,5,2,4,0]
[ 0, 0,0,2,1,0]
[ 0, 0,4,0,0,4]
[ 0, 0,0,0,2,5]
[ 0, 0,0,0,0,8]
det = -9216
```

Its nonzero determinant proves independence. The kernel basis, in the nine-pair row-major ordering, is exactly
(e_{\mathtt{iij,iji}}-e_{\mathtt{iji,iij}},\ e_{\mathtt{iij,jii}}-e_{\mathtt{jii,iij}},\ e_{\mathtt{iji,jii}}-e_{\mathtt{jii,iji}}).

**Proof of equality by transpose.** The Stage3 interaction rectangle for ((p,q)) consists of ((r,s,\mathrm{phase}(p_r,q_s))). Interchange (p,q) and transpose ((r,s)\mapsto(s,r)). Phase uses the sum of the two `j` indicators modulo four and therefore is unchanged. The opposite-phase residue group sizes and all survivor subsets correspond bijectively. The product partial order ((r,s)\le(u,v)) is invariant under transposition, and labels in every linear extension remain unchanged. Thus the entire coefficient histograms agree, including multiplicities. This is stronger than equality of Boolean support. The displayed determinant supplies the independent six-row lower bound; three transpose differences supply the entire kernel.

For arbitrary (n,m\in\mathbb N^9), **(T(n)=T(m)) if and only if** their three diagonal source coefficients match and their three unordered off-diagonal pair sums (n_{pq}+n_{qp}) match. Thus unordered source counts are an exact sufficient carrier for the declared Stage3 word-histogram observer, while the three order differences remain necessary for a future observer that distinguishes first/second source roles.

**Explicit observer collision:** one input unit on `(iij,iji)` and one on `(iji,iij)` produce the identical whole 35-coordinate histogram. The source-first-word observer returns different values; therefore the histogram quotient cannot safely replace the ordered source state for that future operation without retaining order residuals.

## Exact executed checks and scope

Independent Python stdlib integer calculation (finite residue subsets, topological linearizations, rational Gaussian rank and Bareiss determinant) returned `PASS_X6_R063_STAGE3_W2_SOURCE_HISTOGRAM_RANK6`, exit 0. Tested all nine source pairs and 35 target words, exact equality of three transposed pairs, row totals `[102,54,26,54,52,54,26,54,102]`, six-row rank, determinant `-9216`, three kernel vectors, aggregate formal witnesses `524`, and union support `31` versus 35 native two-letter shortest words. No floats or approximations are involved.

This certificate is **one W2 coefficient-level source-preservation criterion**; it neither identifies an historical LP019 positive-natural-BRC signed subtraction error nor performs the original pinned R063 Stage0 `--N 2500 --regression-max-r 512` 17-gate benchmark. Existing [same-object runner intake #2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains OPEN/unassigned; the prior host safety-denied mutation is not retried.

## Continuation

**Mother target:** historical six-axis plane retyping and the 28-LP source/consumer ledger under the frozen P000 V5 and historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3` comparison pin.

**Preserved non-repeat frontier:** 31 Source-confirmed prior units; W2 support minimum cover #31 and original frozen Stage3 source retained; source coefficients vs natural N-BRC distinguished; don't replay completed tests, old denied writings, or the Stage0 substitute.

**Remaining evidence:** locate actual LP011 signed native argmax and LP019 natural positive N-BRC incorrect callsite, close 28-LP consumers, independent Driver REQUEST_REVISION, and receive the original unchanged R063 Stage0 17-gate / 512-case runner evidence under #2416.

**Next exact action:** inspect a new named current/frozen consumer that imports `relation_weights` or discards `(p,q)` source ordering. If it relies on ordered provenance after histogram aggregation, test the explicit pair-swap collision and correct that actual consumer; otherwise preserve typed historical Stage3 without claiming a defect. Track original Native Source semantic PROGRESS separately from GitHub publication.

## Actual frozen Stage3 3-tensor consumer: stronger no-factorization witness

The original same frozen source separately defines `tensor3_signature(p,q,r)` (line 61), and calls it in the associativity corpus (lines 111–115), with **ordered port indices** `(i,j,k)` and phase `(j(p[i])+j(q[j])+j(r[k])) mod 4`. The rank-six observer collision above has a directly source-defined downstream witness, not merely a hypothetical future operation.

Set `p=iij`, `q=iji`, and fixed third source `r=ij`. The pair `(p,q)` and swapped pair `(q,p)` have identical all-35-word Stage3 coefficient histograms, but their actual ordered 3-tensor signatures each have 18 labeled cells and differ at **12** entries. The first differing exact entry is `(0,1,0,1)` versus `(0,1,0,0)`. The appended independent checker computes this from the original tensor formula with integer-only arithmetic and checks the exact 12-cell difference.

Thus no function of only the pair histogram can reproduce this **existing frozen Stage3 ordered tensor consumer** on both inputs. An interface promising the full tensor must retain the three source-order residual directions or the original named ordered pairs. The original Stage3 code itself computes the tensor from the uncollapsed sources and is not identified as a bug. This is a concrete information-preservation boundary for LP019 and the joint-relation observer contract, not a statement about signed cancellation of positive natural N-BRC or a new full-X6 tensor operator.
