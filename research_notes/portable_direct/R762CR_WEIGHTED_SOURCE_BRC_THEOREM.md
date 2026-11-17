# R762CR — 来源通道重数引发 K4 一步观察失效：无限反例、八步上界与精确 N-BRC 检验

Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, \`TP2-8B7E13C5904A2D6F1142\`. Date: 2026-11-17. Status: AUTHOR_DERIVED_AND_EXACT_CHECKED; independent review NOT_REVIEWED.

**Frozen scientific inputs:** P000 V5 @ \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`, published taskbook @ \`e3f42efac29a2da2d95be391f3231a664e2fade0\`. Uses R762CQ, PR #2606 @ \`ed55f51caa843d79cdbf027e0b18778bfaed10f6\`. Active worldview retains six native X6 axes, a separate time dimension, a three-dimensional slice of six-dimensional space, 120° native \`PERP_E\`, signed Port/Cell/Link, and provenance-safe observer distinctions. K4 is a **six-label combinatorial carrier**, not a change of primitive spatial dimension.

## Model and observer

Label six native axes by K4 edges \`01,02,03,12,13,23\`. The ten conditional states are unordered partitions \`A|A^c\` with \`|A|=3\`. Four are F (star/face) and six P (path/path). Partition labels into arbitrary source-equality classes \`C_j\`. One candidate event exchanges \`x in A\` and \`y in A^c\` only when \`x,y in C_j\`. Associate **w_j distinct positive unit microbranches** to such an exchange, with integer \`w_j >= 1\`. Each microbranch retains its source, exchanged labels and ordered time step. Positively recoalesce only upon the declared F/P terminal observer.

Writing \`F_t(s)\` and \`P_t(s)\` for exact N-BRC paths of length \`t\` ending in F/P,
\[
F_{t+1}(s)=\sum_{e:s\to u}F_t(u),\quad P_{t+1}(s)=\sum_{e:s\to u}P_t(u),
\]
where every one of the \`w_j\` unit branches is separately counted. Define \`O_h(s)=((F_t(s),P_t(s)))_{t=0}^h\`. This is the explicit-positive-branch Weighted-BRC reduction \`(C,W,M)\` with unit per-branch mass; **it is not a signed-force cancellation calculation or native event-license claim**.

## Theorem A — infinite family invalidating one-step sufficiency

Take source tags \`001112\`: \`C0={01,02}\`, \`C1={03,12,13}\`, \`C2={23}\`. States
\[
s=\{01,03,12\}|\{02,13,23\},\qquad u=\{02,03,13\}|\{01,12,23\}
\]
are both P. Put source multiplicities \`(a,b,c)\`. Exact branch enumeration yields:

| state | F1 | P1 | F2 | P2 |
|---|---:|---:|---:|---:|
| s | 2b | a | 2b² | a² + 4ab + 2b² |
| u | a | 2b | 2ab | a² + 2ab + 4b² |

For every positive integers \`b,c\`, set \`a=2b\`. Both states have \`O1=((0,1),(2b,2b))\`, whereas their F/P counts at time two differ by \`(F2(u)-F2(s), P2(u)-P2(s))=(2b²,-2b²)\`. The smallest shown instance \`(a,b,c)=(2,1,1)\` has \`O1=(0,1,2,2)\` for each and \`(F2,P2)(s)=(2,14)\`, \`(F2,P2)(u)=(4,12)\`. The positive N-BRC microbranches are sufficient for the witness. Therefore the R762CQ one-step full-future theorem applies to **unit source multiplicities** and does not hold for arbitrary positive source weights.

Proof: enumerate each allowed crossed pair and its independently named \`w_j\` unit branches. First-step counts give the middle two columns. Compose each named first step with each named second step; positive integer recoalescence gives the final columns. Direct substitution completes the infinite-family proof. The verifier independently enumerates the unaggregated unit copies for the witness.

## Theorem B — all positive weights admit a universal eight-step exact certificate

For *every* source partition and *all* positive integer weights, \`O8(s)=O8(u)\` **if and only if** \`O_h(s)=O_h(u)\` for every integer \`h >= 0\`.

Proof: the declared BRC successor-summation map \`L\` acts linearly on the ten-dimensional rational space of state readouts. Put \`V_h=span_Q(F_0,P_0,LF_0,LP_0,...,L^h F_0,L^h P_0)\`. Since F/P form two nonempty disjoint indicator functions, \`dim V0=2\`. If \`V_(h+1)=V_h\`, it is L-invariant, so all future readouts already lie inside. Otherwise dimension increases at least one each step and cannot exceed 10; by \`h=8\` it has stabilized or fills the whole space. Equality of two state evaluations on \`V8\` thus implies all-future equality. Reverse implication is immediate. Knowing F/P type, the smallest full-future quotient has at most 4 F and 6 P states; **three extra bits always suffice** to restore a named state, hence also all declared future F/P readouts. This is finite combinatorial BRC linearity, not classical continuous physical propagation.

## Theorem C — complete weighted finite-range census

Each of the 203 set partitions of six labels has a unique restricted-growth representative. Enumerating all positive source weights \`w_j in {1,2,3}\` gives exactly \`sum_r S(6,r)*3^r=12351\` complete configurations. Exhaustive exact integer BRC branch counts through time eight, with Theorem B, produce:

| Minimum necessary future depth | Configurations |
|---|---:|
| 0 | 735 |
| 1 | 11,544 |
| **2** | **72** |
| 3–8 | 0 |

The 72 one-step failures occur in 24 partition patterns; each affected O1 fiber splits into at most two full-future classes, so **one additional repair bit after O1** suffices for these. The distribution of the number of full-future classes is \`2:735,3:1674,4:1758,5:4752,6:648,7:1440,10:1344\`. The optimal fixed extra bits after the currently known F/P type distribute as \`0:735,1:1950,2:7674,3:1992\`. Setting all weights to 1 recovers R762CQ exactly: \`2:3,3:30,4:62,5:36,6:24,7:48\`.

Completeness: the attached runnable JS verifier constructs every partition, each source weight tuple, the 10 named states, all matched crossed exchanges, every positive branch count, all 0..8 signatures, and tests the weighted source-occupation conservation formula \`d_w(k)=sum_j w_j k_j(n_j-k_j)\`. Witness paths are also checked by a separate explicit two-step expansion. All integer counts at depth eight are below the JS safe-integer limit for this finite weight range. Source code and JSON preserve all 203 per-partition summaries. This result is exact for the stated finite domain; the infinite-parameter claim is Theorem B and the explicit family in Theorem A.

## Next scientific frontier

The task's harder native question remains the **actual licensed** \`TRIADIC_CLOSURE_E\` signed Cell/Link/Port dynamics and V17/V29/V39 event transport, with the source/path/area residuals from R762CH and R762CK. Given the actual license predicate, filter the named candidate event branches and recompute the observer-safe BRC quotient; seek the shortest legal signed Port suffix that distinguishes a collapsed pair. On the weighted candidate itself, determine whether \`O2\` suffices for *all* positive integer weights (here proven only for weights 1..3) or produce a weight counterexample.

**Sources:** frozen taskbook/P000 stated above; \`definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json\`, \`definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md\` and \`src/enterprise_math/brc_weighted.py\` on canonical main; R762CQ @ \`ed55f51c\`. Exact reproduction: \`node R762CR_WEIGHTED_SOURCE_BRC_VERIFY.js > R762CR_WEIGHTED_SOURCE_BRC_EVIDENCE.json\`. Independent review NOT_REVIEWED.
