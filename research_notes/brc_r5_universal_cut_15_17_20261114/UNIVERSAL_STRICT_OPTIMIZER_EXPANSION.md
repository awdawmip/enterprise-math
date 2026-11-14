# R5: two universally optimizer-active cost-inert gaps and one-edit recovery

Date: 2026-11-14. Scope: the frozen R5 **derived one-dimensional integer-event, radius-two, selected-event-center observer**. Scientific-input commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551. All gap and event indices are zero-based. Status: author-side exact finite proof with executable integer verification; independent mathematical review NOT_REVIEWED.

## Context and new theorem

The 954 event positions consist of integer coordinates x_0 < ... < x_953, with 28 length-three gaps indexed C={0,...,27}. For any B⊆C, let x^B be the coordinate sequence after shortening the gaps in B by one unit, with the original event indices retained. For a K-element set of center indices S, let d_B(t,S) denote the nearest-center distance from event t, and let Opt_B(K) consist of the radius-two feasible center-index subsets minimizing the sum of d_B(t,S).

Previous exact results in the R5 scientific branch establish that all B have the same optimal total cost J_B(K) for K≥214, and that gap indices 15 and 17 leave all J_B(K) unchanged. The present proof strengthens the set-valued consequence in the exact interval 293≤K≤314.

**Theorem (every intermediate background).** For i=15 or i=17, for EVERY subset B⊆C\{i} and EVERY integer K∈[293,314],

    Opt_B(K)  ⊊  Opt_{B∪{i}}(K).

There is a deterministically constructed S_i(K) in the difference and T_i(K)∈Opt_B(K) with exactly one removed and one added center:

    |S_i(K)\T_i(K)|=|T_i(K)\S_i(K)|=1.

The same S_i(K), T_i(K) work for every B excluding i, including backgrounds that close the other distinguished gap. Both optimal costs equal

    J_B(K)=J_{B∪{i}}(K)=1620-3K

(from 741 at K=293 to 678 at K=314).

The theorem covers 2^27=134,217,728 different backgrounds per distinguished gap using one universally valid pair of witnesses per budget. It is a strict optimizer-family inclusion statement and a **pointwise one-center swap certificate**. It is not a claim that the *minimum distance between the two families* is positive: since the older family is included, that latter minimum equals zero.

## Explicit local center conditions

The frozen gap i=15 lies immediately after event j=194; gap i=17 lies after event j=245. Every event step is at least one, and the unclosed gap from j to j+1 has length three.

For each of the 22 center budgets, construct an optimal size-K center set S from the **single-gap-closed** coordinates while enforcing

1. event j+1 is chosen as a center;
2. event indices j-2, j-1, j are not chosen;
3. event index j-3 is chosen.

The executable finite certificate finds such S with cost exactly 1620-3K, radius at most two, for all 44 (i,K) pairs. It additionally validates, by reconstructing all 954 coordinates, the exact center-index list and objective for every pair. In the original unclosed configuration, event j has no center within distance two: the three adjacent possible left indices are excluded, each earlier index is at least three positive event steps away, and each right index is separated by the unclosed length-three gap.

Define T by replacing selected center j-3 with center j-2. The program checks that the original unclosed configuration makes T radius-two feasible, with cost 1620-3K for all 44 cases. The swaps are:

| gap i | boundary event j | selected mandatory center in S | remove from S to form T | add to form T |
|---:|---:|---:|---:|---:|
| 15 | 194 | 195 | 191 | 192 |
| 17 | 245 | 246 | 242 | 243 |

## Proof for all other closure backgrounds

**Preservation lemma.** If S is radius-two feasible under a configuration B and a currently unclosed length-three gap is shortened to two, S remains feasible and its exact total nearest-center-distance cost stays unchanged. Indeed, before shortening, every event has a covering selected center on its own side of that gap (distance across the gap is at least three); distances to centers on the same side do not change. A newly available center across the shortened gap cannot lower a nearest distance below the formerly achieved distance: a crossing distance is at least two, while the previous nearest distance is at most two. Repeat this argument to close any collection of other gaps.

Now fix i, K and the S constructed above. Every B∪{i} is obtained from the single-i closure by additionally closing other gaps. The preservation lemma keeps S feasible with objective 1620-3K. The pre-established universal K≥214 optimal-cost theorem makes this objective globally minimal, so S∈Opt_{B∪{i}}(K).

For every B not containing i, the gap immediately after event j remains length three. Distances from j to any selected event at index ≤j-3 remain at least three, since each event step remains at least one under any closures. No selected center has index j-2,j-1,j. All centers to the right of j are separated by the remaining length-three gap. Therefore d_B(j,S)≥3, proving S∉Opt_B(K).

The one-swap set T is feasible and optimal in the original unclosed instance by the 44 finite checks and the known cost J_empty(K). The preservation lemma keeps T with the same optimal cost in every B. Consequently T∈Opt_B(K), while the two sets differ by one replacement. This proves the theorem for all 2^27 backgrounds and 22 budgets, without enumerating all backgrounds.

For general cost-inert i the earlier lemma gives Opt_B(K)⊆Opt_{B∪{i}}(K). The new explicit S proves that this inclusion is strict for i=15 and 17 throughout the stated budget interval.

## Exact computational certificate and validation scope

The accompanying stand-alone verifier regenerates the immutable 954-point input from the frozen 15 integer weights and three rational event pools using Fraction. It uses a shortest-path dynamic program whose states are (center count, last chosen event index) and whose edges are permitted exactly when every intermediate event is covered by the neighboring centers, with edge cost equal to the sum of minimum distances. A mandatory-center index q is enforced by forbidding any path edge that skips q, and by bounding initial/final centers. Forbidden indices are excluded as states. Min-cost predecessor recovery produces all 44 complete center-index witnesses.

The script compares constrained and unconstrained minimum costs for each of the 44 cases, validates every full 954-event S/T pair directly, checks 150 independent tiny instances against brute-force combinations and tests 550 seeded closure backgrounds per distinguished cut (1100 total). Thus the computational claim covers 44 exact finite certificates and independent small-size checker controls; the quantified 2^27-background result follows from the proof above. No floating-point decisions are used.

The deterministic 954-bit witness masks for each K are recomputed by the script. Their SHA-256 digests (22 newline-separated, zero-padded, 240-character hexadecimal masks in increasing-K order) are in EXACT_R5_UNIVERSAL_CUT_15_17.json, for both new S and old T. Full masks are recoverable by the program; neither a private credential nor any external network input is needed.

## Provenance, interpretation and next research unit

The proof inherits the frozen data and high-budget optimal-cost sandwich theorem from R5 Draft PR #2379, especially research_notes/brc_r5_all_closure_jk_sandwich_20261114/RESEARCH.md, research_notes/brc_r5_exact_cost_spectrum_20261114/RESEARCH.md, and research_notes/brc_r5_cost_inert_optimizer_residual_20261114/INERT_GAP_OPTIMIZER_RESIDUAL.md. The present one-swap theorem and all-context witness extension are new within this author continuation.

The reduction is for a derived scalar/event-index observer. In the full native X6/P000 research program, relation/provenance and future operations remain separate evidence types.

**Open next questions:** (a) Do gaps 15 and 17 affect optimizer families outside K∈[293,314] in some intermediate closure backgrounds? (b) For each background and budget, compute the maximum or distribution of edit distance from newly admitted optimizers to the preclosure optimum family, rather than just this universal one-edit witness. (c) Derive a compact symbolic transfer-matrix classification of all 17 optimizer-relevant closure variables. Preserve the source's original 2,520-byte certificate and 8,192-prefix-query end-to-end experiment as an independent practical objective.

No formal R5 CLAIM, Result acceptance, independent reviewer finding or native BRC/X6 performance measurement is asserted by this note.
