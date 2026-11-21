# PREFIX-990 — Delayed positive-BRC histogram transfer without Markov history augmentation

Date: 2026-11-21 (Asia/Shanghai)
Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED
Research scope: independent portable continuation of PREFIX-989, auxiliary signed-source bit-flip observer, no native X6 update inferred.
Frozen scientific pin: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\` (P000 V5).
Relevant current typed interfaces: \`definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md\` (WBRC-T33/T36/T37), \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`; exact predecessor: \`research_notes/portable_direct/2026-11-21_r6_prefix989_weighted_history_refinement.md\`.
Historical author of PREFIX-989: EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056. This result preserves that provenance without asserting a new authenticated task CLAIM or Activity authority.

## Problem and exact observer

PREFIX-989 constructs a valid minimal state-by-state positive *named-word* Markov quotient on states \`(q,b,h)\`, where \`h\` is the previous selected port. Its explicit weight rule is \`g(h,a)=u_h\` with \`u_0=1\`, \`u_1=2,u_2=3,u_3=5,u_4=7,u_5=11\`. Two augmented states may have identical \`(q,b)\` and different next weights, so the previous-port coordinate cannot be erased by a plain state-by-state weighted quotient.

Question: for the separately typed **aggregate exact-weight histogram of all paths of each fixed length**, is that extra Markov state coordinate necessary? This is the positive finite BRC carrier \`N[Q_{>0}]\`, including multiplicity, all integer moments, and length. We require fixed start history \`h=0\` and do not discard source labels from the underlying graph.

## Theorem 990.1 — delayed-weight histogram identity

Let \`S\` be a finite partial deterministic labeled multigraph. Each edge \`a:s->t\` has a current port \`j(a)\`. The historical edge weight is
\[
g(h,a)=u_h v_a,\quad u_h,v_a\in\mathbb Q_{>0},
\]
where \`h=0\` initially and updates after edge \`a\` to \`j(a)\`; the next edge's availability and target depend only on the old graph state \`s\`, not on \`h\`. Let \`\mu\` be a finite vector of nonnegative integer starting multiplicities on old states. Work in \`\mathcal H=\mathbb N[\mathbb Q_{>0}^\times]\`, writing \`[r]\` for a single positive weight \`r\`. Define
\[
\mathcal T_{st}=\sum_{a:s\to t}[u_{j(a)}v_a],
\quad
d_v(s)=\sum_{a:s\to t}[v_a].
\]
Then the *complete exact positive-weight histogram* of legal \`n\`-step named paths from \`\mu\` is
\[
\boxed{\mathcal H_0=(\mu\mathbf 1)[1],\qquad
\mathcal H_n=[u_0]\,\mu\mathcal T^{\,n-1}d_v\quad(n\ge1).}
\]
All equal-weight multiplicities are exact. Its formal length-generating series is
\[
\sum_{n\ge0}z^n\mathcal H_n
=(\mu\mathbf1)[1]+z[u_0]\mu(I-z\mathcal T)^{-1}d_v.
\]
For each integer moment \`r>=0\`, specialize \`[w]\mapsto w^r\`:
\[
P_r(n)=u_0^r\,\mu(T_r)^{n-1}d_r,\quad
(T_r)_{st}=\sum_{a:s\to t}(u_{j(a)}v_a)^r,\quad
(d_r)_s=\sum_{a:s\to t}v_a^r.
\]
These are exact identities in finite positive-rational branch algebra, not assertions of analytic convergence at \`z=1\`.

**Proof.** For a fixed legal word \`a_1...a_n\` with ports \`j_1...j_n\`, the actual chronological weight is
\[
(u_0v_{a_1})(u_{j_1}v_{a_2})\cdots(u_{j_{n-1}}v_{a_n})
=u_0\Big(\prod_{t=1}^{n-1}u_{j_t}v_{a_t}\Big)v_{a_n}.
\]
The first \`n-1\` factors on the right are exactly the edge weights of \`\mathcal T\`; the final edge is counted by \`d_v\`. Sum in the positive histogram semiring, which recoalesces equal-weight alternatives without dropping multiplicity. \`n=0\` is the empty path of mass one. The formal geometric series and moment identities follow coefficientwise. QED.

**Specialization to PREFIX-989.** There \`v_a=1\`, \`u_0=1\`, hence \`d_v(s)=\deg^+(s)[1]\` and \`\mathcal H_n=\mu\mathcal T^{n-1}d\`. The old \`(q,b)\` graph suffices for every fixed-length positive mass histogram, although its states still fail the stronger conditional named-weight equivalence of PREFIX-989. This distinguishes *aggregate observer reduction with a terminal functional* from a state-by-state Markov weighted quotient. Neither the terminal functional nor the source label is silently erased.

## Theorem 990.2 — exact test for separable history/source weights

For a finite allowed relation \`E\subseteq H\times A\` with positive rational weights \`g(h,a)\`, positive factors \`u_h,v_a\` satisfying \`g(h,a)=u_hv_a\` on every allowed pair exist **if and only if** on every alternating cycle of the bipartite incidence graph,
\[
\prod_{i=1}^k g(h_i,a_i)
=\prod_{i=1}^k g(h_{i+1},a_i),\qquad h_{k+1}=h_1.
\]
Proof: necessity follows by cancellation of the factors around the cycle. For sufficiency, choose one vertex potential in each connected component, propagate rational potentials along a spanning tree, and use the cycle identities to ensure every non-tree edge agrees. Isolated vertices can be assigned arbitrary positive potentials. QED. A complete rectangular weight table has the equivalent rank-one / vanishing-all-2x2-minors test.

This test identifies when the delayed transfer can apply to a more general last-port/current-source rule without maintaining the full history automaton. Failure of factorization does not exclude alternative observer-specific reductions.

## Exact computations (PREFIX-989 historical port-weight instance)

Starting from all odd active-bit configurations at phase 0, with \`h=0\`, the checker projects PREFIX-989's augmented graph to \`(q,b)\`, verifies edge agreement across every historical \`h\`, and independently matches the complete augmented-graph mass at all lengths 0..24 and exact histograms at every length 0..13. All arithmetic is exact integer.

| Four-phase word | Reachable augmented states | Old reachable states | Weighted Nerode classes in PREFIX-989 | Active starts | N8 / Mass8 | N19 / Mass19 |
|---|---:|---:|---:|---:|---:|---:|
| (6,24,6,-3) | 96 | 64 | 89 | 16 | 96 / 276480 | 2016 / 1763596800000 |
| (6,24,8,40) | 188 | 120 | 163 | 32 | 84 / 1901600 | 0 / 0 |

First word's exact step-eight histogram: \`{1800:16, 2520:16, 2700:32, 3780:32}\`. Its step-thirteen histogram is \`{486000:64,680400:96,729000:128,1020600:192}\`. For 19-bit odd inputs, the spectator multiplier is \`2^14=16384\` for the first word and \`2^13=8192\` for the second; the first word's \`n=19\` mass becomes **28,894,769,971,200,000**, matching PREFIX-989.

Coverage: two explicit residue families, port-specific integer weights, all initial active states, exact forward/quotient comparison inherited from the PREFIX-989 checker. Theorems 990.1–990.2 are algebraic for the stated finite-rational domains. Theoretical state-count reduction concerns **the specified aggregate histogram observer**; it does not preserve independent conditional future weighted words, signed cancellation, or native Cell/Link/Port identity.

## Reproduction, status, and next problem

Checker: \`research_notes/portable_direct/PREFIX990_R6_DELAYED_HISTOGRAM_CHECK.py\` (uses the prior \`PREFIX989_R6_HISTORY_WEIGHTED_NERODE.py\` already at the same path). Exact output certificate: \`research_notes/portable_direct/PREFIX990_R6_EXACT_RESULTS.json\`. Full proof has been author checked and finite experiments reproduced; no independent mathematical Review or strict Activity audit.

Next: apply the cycle-factorization criterion to one actual Source-typed BRC transition/feedback weight law instead of the auxiliary chosen \`u_h\`. On failing factorization, determine whether the full histogram observer nevertheless has a smaller exact finite linear representation and retain a concrete defect/witness. The P000 X6 embedding and joint-observer-preservation bridge remain explicit later tasks; mother objective \`B_fix,odd(32) ∈ {19,20}\` stays open.
