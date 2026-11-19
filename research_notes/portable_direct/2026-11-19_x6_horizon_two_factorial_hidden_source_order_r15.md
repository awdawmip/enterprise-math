# X6 R15: factorial hidden source-order residual revealed in exactly two events

Date: 2026-11-19 Asia/Shanghai. **Author-side conditional theorem; verified finite Boolean-BRC examples; NOT_REVIEWED.** Parent research line \`RS-X6-NATIVE-TIME-DYNAMICS\`, publication \`TP2-91D4A7C2F63805BE21A3\`; frozen P000 scientific source \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This theorem uses the same **explicitly hypothetical** occupancy-only source-labelled signed X6 event semantics as R14, not an admitted native \`TRIADIC_CLOSURE_E\` Cell/Link/Port rule.

## Motivation

R14 proves the h-interaction-component state \`Sigma_h\` is exactly sufficient for full source/Port/direction-labelled future languages but prudently does **not** claim global minimum for n>=3. An exact witness now proves that the R14 signature can be substantially nonminimal at horizon 1 even when all twelve signed primitive moves are offered. More importantly, the same full observation can hide **factorially many** source-order configurations at horizon 1 and distinguish them all at horizon 2. This extends the earlier R12 finite-history delayed distinction to a new order-based family.

## Model, family and result

Let \`e_1,...,e_6\` be the six signed native coordinate directions within the X6 Cell torsor. Fix any positive integer \`k\`. Introduce \`k+2\` labelled sources:
- label \`0\` at position \`0*e_1\` (left endpoint);
- label \`k+1\` at position \`(k+1)*e_1\` (right endpoint);
- the labels \`1,...,k\` occupy the interior Cells \`e_1,2e_1,...,ke_1\` in an arbitrary permutation \`pi\`.

All other five signed components are **explicitly zero in this chosen relative chart**, rather than silently discarded dimensions. Every source can attempt any of twelve signed single-axis steps; an attempted move is permitted iff its target Cell is not occupied by any source. A typed Boolean-BRC word records the full ordered \`(source, signed-Port)\` sequence. Let \`L_h(pi)\` be every legal labelled word of length at most \`h\`, including the empty word.

**Theorem R15.1 (one-step collapse and two-step full recovery).** Across all \`k!\` permutations \`pi\`:
\`\`\`
|{ L_1(pi) : pi in S_k }| = 1,
|{ L_2(pi) : pi in S_k }| = k!.
\`\`\`
Consequently, on this explicitly fixed permutation fiber the extra source-order information necessary for lossless horizon-1 prediction is \`0\` bits, whereas preserving horizon-2 future language needs exactly
\`\`\`
b_2(k) = ceil(log_2(k!))
\`\`\`
bits. For \`k=1,2,3,4,5\` the classes at \`h=2\` are \`1,2,6,24,120\` and minimal fixed-length bits are \`0,1,3,5,7\`. This yields an unbounded factorial residual gap while the *observation horizon increases by just one*; the number of distinct source units is \`k+2\`, not a fixed constant. No unlabelled observer is substituted.

### Exact proof

**One-step.** Each of the \`k\` interior labels has **both** adjacent \`+e_1\` and \`-e_1\` target Cells occupied, irrespective of its place in the interior order. Every move of that label along any \`±e_2,...,±e_6\` is legal, since no source is off the \`e_1\` line. The left endpoint label 0 has \`+e_1\` blocked, \`-e_1\` legal, and all transverse moves legal. The right endpoint label \`k+1\` has \`-e_1\` blocked, \`+e_1\` legal, and all transverse moves legal. These complete one-letter legal/illegal patterns depend solely on each label's endpoint/interior *role* and not on \`pi\`. Thus every \`L_1(pi)\` is identical.

**Two-step.** Fix an interior label \`s\` and a candidate predecessor label \`t\` which is either the left endpoint 0 or another interior label. Consider the length-two typed event word
\`\`\`
w(s,t) = ((s,+e_2),(t,+e_1)).
\`\`\`
Its first move is always legal, moving \`s\` off the occupied \`e_1\` line and vacating \`s\`'s original Cell. The second move is legal **if and only if** \`t\` immediately precedes \`s\` in the original left-to-right interior chain. If so, \`t\` moves into exactly the newly vacated Cell; otherwise \`t\`'s \`+e_1\` target remains occupied by its own original right neighbor. The right endpoint is not a candidate predecessor of any interior source, so its always-free \`+e_1\` move is irrelevant.

Every permutation of the interior labels is uniquely determined by the predecessor relation of its interior labels with the fixed left endpoint 0. Any two distinct permutations differ in the predecessor of some interior label \`s\`; choose \`t\` to be that predecessor in the first permutation. Then \`w(s,t)\` is legal in the first and illegal in the second. Hence their \`L_2\` differ pairwise. Since the fiber has exactly \`k!\` configurations, the number of horizon-2 language classes is exactly \`k!\`; the fixed-length information bound follows. QED.

### Explicit smallest nontrivial witness

For \`k=2\`, the two full signed X6 configurations are
\`\`\`
P: [0, B, C, 3] at e1-coordinates [0,1,2,3]
Q: [0, C, B, 3] at e1-coordinates [0,1,2,3].
\`\`\`
Their complete one-event language is equal, although the R14 \`Sigma_1\` differs because the connected component stores different B/C positions. The two-event word \`((B,+e_2),(0,+e_1))\` is legal in P (the left endpoint enters B's vacated Cell) but illegal in Q (the left endpoint's immediate right neighbor is C and did not move). This proves by counterexample that **a future-safe sufficient state can be nonminimal** even under fully labelled signed-axis observation, while a one-step invisible order residual becomes distinguishable in two events.

## Exact verification

Companion files: \`x6_hidden_order_factorial_brc_verify.py\` and \`x6_hidden_order_factorial_brc_results.json\`; run \`python3 research_notes/portable_direct/x6_hidden_order_factorial_brc_verify.py\`.

A local Python checker enumerated *all* source-labelled, full twelve-direction legal event words of length \`0..2\` for **every** interior permutation at \`k=1..5\`, directly applies the six-component Cell vacancy guard, computes the actual language classes, and tests the constructive \`w(s,t)\` separator for every ordered pair of distinct permutations. Result: **PASS**; **792,022** cumulative legal-word observations across the two horizon computations and **14,864** directed permutation-pair witness checks. Those counts refer to repetitions across cases, not distinct physical words. The formula for all \`k\` is supported by the symbolic proof; no large-\`k\` enumeration is claimed.

The work concerns Boolean support of typed source-labelled conditional events. Neither it nor R14 asserts native three-force closure, actual Link incidence, native admissibility, signed amplitude/quantum prediction, or a calibrated time interval. The observed two-event distinction is in ordered *event count*, not a claim about physical duration.

## New precise research frontier

R14's interaction-component state is sufficient but not minimal at finite horizons: the smallest evidence is \`k=2,h=1\` above. The exact next problem is to characterize, for general source sets and horizon \`h\`, the quotient by equality of complete typed future languages, *rather than* treating component coordinates as necessarily minimal. For transfer to native Heartbeat World dynamics, first obtain a real \`TRIADIC_CLOSURE_E\` admitted multi-Cell Link/Port event and test whether the off-axis release-and-fill witness is a genuinely permitted future trace. Missing native permission cannot be filled by this occupancy-only conditional proof.

**Preserve prior sources:** R14 proof \`e1b9c6dd39754da27abf362793212cf93650b85e\`, R13 fixed-lane source and predecessor R11–R12. Exact author lineage remains on the existing Source Activity only to the extent authenticated; no formal Result/review or fresh CLAIM is inferred by this file.
