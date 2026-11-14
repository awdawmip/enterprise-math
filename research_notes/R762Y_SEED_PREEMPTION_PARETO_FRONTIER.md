# R762Y — Sharp seed–interruption frontier for source-typed cyclic triad macroevents

Date: 2026-11-14 (Asia/Shanghai).
Evidence class: **AUTHOR-SIDE EXACT CONDITIONAL THEOREM / REPRODUCIBLE FINITE CHECK / NOT_REVIEWED / NOT_ADMITTED**.
Mother Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; immutable publication \`TP2-8B7E13C5904A2D6F1142\`; frozen scientific input \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
Author-side source identity: Researcher \`EM-X6-4CF999\`, Activity \`RA-057D26CD5FD545C32116EBE2\`; a historical role record is not a current claim. The current native continuation snapshot has a live claim held by another Researcher; this note does not take over that run.

## 1. Specific unresolved interface and reuse

P000 uses the native six-axis signed Cell torsor inside Heartbeat World (time separately typed). The primitive force balance has exactly three present quanta and requires \`TRIADIC_CLOSURE_E\`. The native force-event admission/update scheduler and V17/V39 transport are still not supplied by this statement.

R762W (PR #2354, immutable research commit \`2df9e89c0f7f98e5e57e3d8ac940047988c86b29\`) constructed a source-typed *candidate* X6 first-return hexagonal trace \`H(a,b,d)=(a,b,-a,d,-b,-d)\`. Its explicitly **separate conditional** V29 lift emits ordered PASS occurrences \`a->b, b->d, d->a\`. If successive macroevents must be atomic, consecutive, and phase-locked, the sharp initial-token minimum is \`min(k,3)\`; freely reordering the individual PASS multiset needs one token (R762U, PR #2347). R762X (PR #2355, commit \`fd9371a4c4175737f7af5bc8af2615e963477bea\`) proved a fixed-word prefix-seed law.

This note studies the **intermediate scheduling language**: each candidate macroevent's own three PASS operations retain their original source order, but operations of different macroevents may be interleaved. It asks for the exact resource–interruption tradeoff and a BRC-sufficient distinguishing observable. Neither interleaving nor token enabling is here asserted to be permitted by actual P000 primitive force-event physics.

## 2. Typed abstract execution language

For a finite directed cycle of \`q>=2\` distinct typed ports \`v_0,...,v_{q-1}\`, let \`e_i:v_i->v_{i+1 mod q}\`. The rooted macro \`C_r\` consists of the ordered \`q\` occurrences
\[
e_r,e_{r+1},\ldots,e_{r+q-1}\qquad(\text{indices mod }q).
\]
There are \`k>=1\` **individually labeled** macros \`C_{r_1},...,C_{r_k}\`. Even if roots coincide, labels and per-macro ordered provenance are retained. Define \`R={r_i:1<=i<=k}\` and \`d=|R|\`. Every occurrence consumes one nonnegative integer port token at its tail and deposits one at its head. Tokens are conserved and no tokens may be injected after time zero. A legal shuffle respects the within-macro occurrence order, but does **not** prescribe an ordering of first starts across different macros.

An **interruption/preemption** occurs when a scheduled macro is switched away from **before** its final occurrence has fired. Switching after a macro completes is free. A resumed macro can be interrupted more than once; those are distinct preemptions. All complete macroevents return to their own root, and after any uninterrupted macro **segment**, port-token changes consist of one transfer from the segment's first port to its last port. Count interruptions globally, independent of which indistinguishable token fires each occurrence.

For \`K\` initial tokens, let \`h_{\min}(K)\` be the minimum over all initial token distributions and admissible shuffles, using \`1<=K<=d\`. Let \`K_{\min}(h)\` be the minimum nonzero total seed permitting at most \`h>=0\` interruptions.

The P000-relevant instance has \`q=3\`, with \`v_0,v_1,v_2\` being three independently named, distinct-axis signed native ports associated with three nonzero force quanta. The arbitrary-\`q\` statement is **ordinary graph combinatorics**, not a claim of primitive stable \`q\`-force balance.

## 3. Theorem Y1 — exact seed–interruption Pareto frontier

For all \`q>=2\`, all nonempty lists of individually labeled cyclic macros and every \`1<=K<=d\`,
\[
\boxed{h_{\min}(K)=d-K.}
\]
Equivalently, for each interruption budget \`h>=0\`,
\[
\boxed{K_{\min}(h)=\max\{1,d-h\}.}
\]
Thus all integer pairs \`K>=1,h>=0\` with \`K+h>=d\` are feasible (allowing unused extra stock or interruption budget), and none with \`K+h<d\` is feasible.

**Necessity.** Split an actual execution into maximal consecutive segments belonging to the same labeled macro. An initial token can account for at most one initially occupied root; the stock vector with \`K\` tokens initially occupies no more than \`K\` roots. Consider the **first start** of a macro from any root \`r\` that had no initial token. Its enabling token must have arrived through an earlier positive-length macro segment. A segment ending in completion of its macro can deposit its last token only at that macro's own root, where a macro has already started; it cannot first enable a previously unused root. Therefore the first supply of \`r\` comes from a segment of a still-incomplete macro, which had to be interrupted before a macro rooted at \`r\` could start. Each interruption leaves the current segment at a single port, and can be charged to at most one distinct newly started root. Hence \`d <= K+h\`. With at least one nonempty macro, \`K>=1\`; these yield both lower bounds.

**Sufficiency.** Partition the \`d\` distinct roots into \`K\` nonempty groups, put one initial token at one chosen root \`r\` per group, and schedule groups independently. In a group, execute all macros rooted at \`r\` except one *carrier* completely. Begin that carrier's \`q\`-edge cycle. It visits every other root in the group exactly once before its final return. When it first visits another root \`s\`, pause it, execute **all** macros rooted at \`s\` consecutively and completely, and resume the carrier. Each inserted macro is a closed ordered cycle, so its execution returns the token to \`s\` and does not affect other port stocks. The carrier is interrupted once for each other distinct root in the group. This performs all prescribed labeled occurrences in their own order, with one token and exactly \`|group|-1\` interruptions. Summing over groups gives \`K\` tokens and \`d-K\` interruptions. This meets the lower bound, proving both formulas.

**Boundary cases.** A single macro or any number with the same root has \`d=1\`, hence one token and zero interruptions suffice. No macro is excluded by \`k>=1\`; if the empty event family is considered separately, its minimum stock is zero. Extra initial tokens cannot make the minimum interruption count negative.

## 4. Corollary Y2 — triadic cost is a scheduling-language residual

For the three named signed source ports of R762W, a set of \`k\` candidate macroevents whose distinct first sources number \`d\in\{1,2,3\}\` has:
\[
\begin{array}{c|ccc}
d & K_{\min}(0)&K_{\min}(1)&K_{\min}(2)\\\hline
1&1&1&1\\
2&2&1&1\\
3&3&2&1
\end{array}
\]
The phase-rotating \`k\`-round word used in W3 contains \`d=\min(k,3)\` distinct phase roots. Under this note's relaxed inter-macro shuffle, **one** seed is sufficient using exactly \`d-1\` interruptions, while every macro's internal \`a->b->d->a\` PASS order is preserved. The additional resource demanded by W3 is therefore attributable to its **atomic non-interleaving and prescribed macro phase chronology**. This note does not claim that the relaxed shuffle itself respects W3's prescribed chronology of macro first starts; that separate chronology would change the legal language and may increase the interruption requirement.

**Exact BRC observation fiber.** Every \`C_r\` contributes one each of the \`q\` directed PASS edge types. Therefore the complete terminal nonnegative PASS matrix is just \`k\` times the directed-cycle matrix, regardless of the multiset of roots. For \`q=3,k=3\`, the histories \`(a,a,a)\` and \`(a,b,d)\` have identical complete V29 terminal counts and zero net port imbalance, but have \`d=1\` and \`d=3\` respectively. They require, at zero preemption, \`1\` versus \`3\` initial tokens. Their full source-order histories and permitted shuffles differ. The one-integer carrier \`d\`, derived from the **retained named root set**, determines the entire tradeoff \`K_{\min}(h)\` for this precise future question. It is not a complete carrier for rooted X6 edge current, chronological phase-lock, V17/V39, or arbitrary future operations. Thus \`d\` is an **observer-sufficient repair coordinate** for the declared resource-preemption question, not permission to delete the provenance.

## 5. Independent finite exact verification

\`research_notes/R762Y_PREEMPTION_FRONTIER_VERIFY.py\` uses exact Python integer dynamic programming, enumerating every possible per-macro progress state, token allocation with a fixed total \`K\`, current port inventory, last active macro and all legal next occurrences. A switch from an incomplete macro costs one. Its independent optimal value is compared with \`d-K\` for **all** labeled phase words and \`1<=K<=d\` in these complete finite domains:

- \`q=2\`, \`1<=k<=4\`: 52 cases.
- \`q=3\`, \`1<=k<=4\`: 270 cases.
- \`q=4\`, \`1<=k<=3\`: 180 cases.

All **502** assertions passed; \`research_notes/R762Y_PREEMPTION_FRONTIER_EVIDENCE.json\` captures the deterministic output. These are crosschecks, not an extrapolation from finite ranges. Y1 is established for arbitrary finite \`q,k\` by the preceding constructive proof.

## 6. Provenance, native boundary, and next test

Sources: frozen scientific P000 pin \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`, current task publication \`TP2-8B7E13C5904A2D6F1142\`, R762U PR #2347, R762W PR #2354, R762X PR #2355. Keep full six-dimensional Cell/Link/Port and separately typed time, source/branch identities, individual PASS occurrences and the distinction between actual primitive force events and auxiliary V29 token transitions. No protected worldview modification.

**Next discriminating native question:** Determine whether any truly admitted \`TRIADIC_CLOSURE_E\` event permits inter-macro PASS interleaving; whether macro start chronology is fixed by the force update; and whether V17 active-frame and V39 based-loop transport detect the interleaving. Under a fixed phase order, compute the new legal shuffle frontier without silently importing Y1's no-first-start-order assumption. A legitimate native result requires an actual admission and update map; Y1 does not supply it.

Current status: durable author-side candidate theorem, NOT_REVIEWED, no formal Result or independent Driver disposition, and no CLAIM obtained by this note.
