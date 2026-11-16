# R5 — exact minimum budget-query complexity of the high-budget optimizer-family quotient

Date: 2026-11-16. Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Scope: 954 indexed events, derived one-dimensional integer radius-two nearest-center objective, original 28 independent closure bits, and budget queries 214 <= K <= 954. Research status: AUTHOR_PROVED (conditional on explicitly identified earlier exact input results), EXACT_FINITE_SUPPORT_CHECKED, NOT_REVIEWED. No native X6 projection or formal task/CLAIM admission is asserted.

## Sources inherited, not recomputed in this note

The earlier exact integer DP report \`research_notes/portable_direct/r5_global_optimizer_tomography_20261114/RESEARCH.md\` on this same R5 research branch gives the following complete *full-optimizer-family* effective closure supports:

| Budget K | E(K) |
|---|---|
| 214..221 | {3,8,9,10,27} |
| 222 | {27} |
| 223..291 | {25,27} |
| 292 | empty |
| 293..314 | {15,17} |
| 315..954 | empty |

For every original closure mask B among the 28 gap indices, the complete family \`Opt_B(K)\` and scalar \`N_B(K)=|Opt_B(K)|\` depend only on B restricted to E(K). That report additionally establishes by exact integer comparisons that the individual scalar maps \`B -> N_B(214)\`, \`B -> N_B(223)\` and \`B -> N_B(294)\` are injective on their respective 5-, 2- and 2-bit effective supports. It proves that the entire family for K>=214 identifies exactly the eight-bit quotient

    U = {3,8,9,10,15,17,25,27}.

The current work proves the optimal number of scalar observations needed to recover that quotient, including adaptive queries. Its proof depends on these inherited exact support and injectivity statements. It does not rerun the prior 954-event dynamic program.

## Theorem: three queries are necessary and sufficient, even with adaptivity

**Theorem.** Consider a deterministic protocol that, for an unknown 28-bit closure mask B, may request the exact scalar \`N_B(K)\` at integer budgets K in [214,954]. The next budget may depend arbitrarily on prior answers, and arbitrary exact postprocessing is allowed. Recovering the full eight-bit quotient B intersect U for every B requires at least three queries in the worst case. In fact every correct decision-tree leaf has depth >=3. Three nonadaptive queries suffice: K=214, 223 and 294.

**Proof.** Introduce three pairwise disjoint *private-bit blocks*:

    A={3,8,9,10},  C={25},  D={15,17}.

No permissible single budget query depends on bits from more than one of these private blocks. The only cross-window shared bit is 27, and K=222 observes only that bit.

Consider any putatively correct adaptive decision tree and any input B that terminates at depth at most two. Along that realized path, at most two of A,C,D have been queried. Choose one unqueried private block and flip one of its bits, obtaining B'. Both scalar answers on the realized path are unchanged because both budgets are independent of that bit. Since the protocol is deterministic, its adaptive second choice and terminal output are also unchanged. But B intersect U and B' intersect U are different. Moreover the inherited count-injectivity at the relevant representative budget (214 for A, 223 for C, 294 for D) certifies that the *complete high-budget observer* distinguishes them. Contradiction. Thus no correct leaf has depth below three.

Conversely the three scalar counts N_B(214), N_B(223), N_B(294) each uniquely decode their own E(K) bits by the inherited exact integer tables. Their union equals U, so the three queries recover the full quotient. QED.

This is a query-support obstruction, not merely a Shannon-bit counting argument: an individual exact count can encode several independent closure bits.

## Sharp two-query information bound

**Proposition.** A deterministic protocol allowed at most two (possibly adaptive) scalar budget queries produces no more than 128 distinct answer transcripts across all original masks. This maximum is attained nonadaptively by K=214 and K=294, which give 128 distinct signatures encoding exactly seven bits \`{3,8,9,10,15,17,27}\`. Under the uniform prior on all 2^28 closure masks, each signature has 2^21 original preimages and the observed Shannon entropy is exactly seven bits.

**Proof.** In the first query, a budget in the first active window (214..221) has at most 2^5 distinct answers, while every budget outside that window has at most 2^2. If the first query is in the first window, a second query in that same window still sees only the same five bits (at most 32 possible complete transcripts); a second query outside sees at most four answers conditional on the first response. Thus at most 32*4=128 transcripts. If the first query is outside the first window, it has at most four outcomes, and any second query has at most 32 outcomes; hence also at most 128 transcripts. The selected second budget is determined by the first answer and carries no independent information.

For the construction, E(214) and E(294) are disjoint, of sizes five and two. Their scalar readouts are separately injective on these supports, yielding 2^(5+2)=128 signatures. The other 21 original closure bits are free, giving 2^21 preimages per signature. QED.

## Complete necessary budget-window structure

A query sensitive to private bit 3 requires K in 214..221; a query sensitive to private bit 25 requires K in 223..291; one sensitive to private bit 15 requires K in 293..314. Therefore every nonadaptive *three-budget* decoder of the entire quotient must select exactly one budget from each of these three windows (up to ordering). There are

    8 * 69 * 22 = 12,144

structurally eligible unordered triples. This is a necessary support condition, not a claim that all 12,144 scalar triples are injective; the earlier exact DP certifies the specific triple (214,223,294).

Similarly a two-budget choice has maximal joint effective support size seven iff it selects one budget in 214..221 and one in 293..314; there are 8*22=176 such unordered pairs. The pair (214,294) is known to achieve the corresponding seven-bit scalar decoding optimum.

## Exact finite verification and independence boundary

Companion program \`VERIFY_R5_MINIMUM_BUDGET_QUERIES.js\` uses only finite integer sets and loops. It checks all 741 permissible budgets and 274,170 unordered budget pairs, confirms maximum one-budget support five and two-budget union seven, identifies the 176 maximizing pairs and the 12,144 structurally eligible triples. It also enumerates 256 eight-bit quotient assignments to check the support-map collision counts for representative queries. This is a verification of the combinatorial deduction from the inherited E(K) table; it is not a re-run of source-geometry DP or a new independent verification of the earlier scalar injectivity.

The recovered eight bits are information sufficient *for the declared derived high-budget optimizer-family observer*. Native Heartbeat/X6 joint relations, ordered paths, signed/provenance information and other future operations remain separately typed and are not erased by this observer-specific quotient.

## Next research question

Compute the count-map injectivity (or explicit collisions) for each of the 12,144 structurally eligible triples by a smaller exact method, ideally factoring the previously computed bandwise integer spectra rather than repeating full 954-event DP. Also derive the minimal number of budget observations when only a restricted interval of K is available, and the exact recourse/max-new-min-old distance for K=214..291. Preserve this three-query lower bound under the original frozen source and observer definitions.
