# R5 at K=214: exact witnesses for nonlocal optimizer recourse ≥3, 7, 7, 4

**Date:** 2026-11-15. **Evidence:** AUTHOR_PROVED_EXACT_WITNESS / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Frozen scientific input:** \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.

Model: the existing 954-event derived 1D radius-two event-index-center observer, 28 disjoint length-three intervals available for shortening to length two; this is a declared observer of Enterprise Math, not an asserted native X6 lossless quotient. Center budget \`K=214\`. Let \`Opt_B(K)\` be the full family of exactly K centers that cover all indexed events within 2 and minimize the integer nearest-center distance sum under closure mask B.

## Exact lower-bound theorem

For **B=∅**, let \`S_i\` be an explicitly constructed optimum under the singleton closure \`B={i}\`. Define
\[
\rho_i(S_i)=\min_{T\in\operatorname{Opt}_{\varnothing}(214)}|S_i\setminus T|.
\]
The attached deterministic code constructs 214-center sets \`S_i\` for i=3,8,9,10 and certifies the following **exact witness-specific** minimums:

| Closed cut index i (zero-based) | Gap starts at event | Exact \`rho_i(S_i)\` | Old-optimal maximum shared centers |
|---|---:|---:|---:|
| 3 | 46 | 3 | 211 |
| 8 | 110 | 7 | 207 |
| 9 | 116 | 7 | 207 |
| 10 | 123 | 4 | 210 |

The cut start indices in the table must be taken from the frozen reconstruction: \`cuts[3]=46\`, \`cuts[8]=110\`, \`cuts[9]=116\`, \`cuts[10]=123\`. The first column is the identity of the closure variable; center and event indices are distinct observers.

All cases have the same exact minimum total cost \`J_{\varnothing}(214)=J_{\{i\}}(214)=1064\`. Hence the original max-new/min-old directed recourse defined in the R5 research notes satisfies:

\[
\boxed{R_3(214)\ge3,\quad R_8(214)\ge7,\quad
 R_9(214)\ge7,\quad R_{10}(214)\ge4.}
\]

These inequalities are precise universal-lower-bound witnesses, **not** claims that the four worst-case maxima equal these numbers. They demonstrate that even when the optimum value is unchanged, the **nearest old optimum** can be much farther than one center replacement. For cut 8, a nearest-old-optimal witness changes centers at indices 271,274,278,282,286 in addition to near-cut changes, exposing distant optimizer coordination in a fully specified finite instance.

## Proof by an exact lexicographic shortest-path certificate

For a fixed new optimal indexed center set S, first enumerate the old admissible directed acyclic center path graph: a vertex is an indexed center, and each admissible increasing edge is scored by its exact integer nearest-center costs on the intermediate events. Add prefix and suffix costs and enforce the K-center budget. The existing \`VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py\` supplies independent frozen reconstruction, graph, and the original old/new exact min-cost forward/backward tables C,D,J.

To compute the **minimum over all old optimizers**, restrict an edge i→j at layer t to ones satisfying its exact min-cost prefix recurrence and full-path optimality identity. Among these globally old-optimal edges, calculate
\[
M_t(j)=\max_{i\to j\text{ admissible optimum}}
\bigl(M_{t-1}(i)+\mathbf1_{\{j\in S\}}\bigr).
\]
Initialize for all globally old-optimal first centers with \`1(j in S)\`, and maximize the final layer over globally optimum last centers. The recurrence visits every old-optimal K-center subset, so its terminal value \`M\` is **exactly** \(\max_{T\in Opt_\varnothing(214)}|S\cap T|\). Because |S|=|T|=214, the minimum required replacements are **exactly 214-M**. Backpointers reconstruct a maximizing old optimum T as an explicit second 214-center witness; the code independently checks the complete 954-event radius condition and cost for both S and T.

The new S comes from a deterministic random-seeded selection among *exactly globally optimal new-coordinate paths*, not from a heuristic objective optimizer. Sampling only locates four witnesses; the full old-optimum maximization, validity of each witness, and the resulting lower bounds are exact. A source file recreates **all 1,024** sampled new optima (256 for each of four cuts), selects the strongest witnessed minimum, and prints complete new and old optimizer lists with exchanged indices and sample histograms.

## Reproducibility and scope

Run \`python VERIFY_R5_K214_NONLOCAL_RECOURSE.py > EXACT_R5_K214_NONLOCAL_RECOURSE.json\` beside the previously published R5 path-DP source \`VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py\`. Standard-library Python; seed=20261115; samples per cut=256. Observed \`PASS_EXACT_R5_K214_NONLOCAL_RECOURSE\`; result lower-bound vector \`[3,7,7,4]\`.

Deterministic full output with all 214-center indexed witnesses: **24,394 bytes**, SHA-256 \`53072d874619a1eb6bede5e43d647d7d5c228f83371ea76b05eba03b5a81da82\`. The small \`K214_NONLOCAL_SUMMARY.json\` preserves observed maxima, full output digest, actual validation scope and follow-up questions. Independent mathematical review: \`NOT_REVIEWED\`.

## Next

Obtain exact upper bounds for R_i(214..221), first i=3,8,9,10, by combining all possible new optimal path choices with a full old-optimum nearest-neighbor DP. Preserve the nesting \`max_S min_T\`; a sampled lower-bound witness is not automatically the maximum. Analyze whether far-away replacement coordinates are genuinely forced in **every** nearest-old optimizer rather than only the concrete reconstructed T.