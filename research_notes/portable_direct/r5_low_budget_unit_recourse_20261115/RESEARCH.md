# R5: universal one-center recovery for cuts 27 and 25 at lower budgets

**Date:** 2026-11-15. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Science pin:** \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.

The object is the previously frozen 954-event **derived 1D integer-coordinate, indexed-center radius-2 observer**. Event indices are retained. A closure at one of 28 separated length-three coordinate gaps shortens that gap to two. This theorem concerns center-set optimization in that observer, with the P000/native-X6 provenance and richer path/source observers retained separately.

## Statement

For B any subset of the 28 gap indices omitting i, let
\[
\rho_B(S)=\min_{T\in\operatorname{Opt}_B(K)}|S\setminus T|,\quad
R_i(K)=\max_{B\subseteq I\setminus\{i\}}\;\max_{S\in\operatorname{Opt}_{B\cup\{i\}}(K)}\rho_B(S).
\]
The \`min_T\` occurs **inside** the \`max_S\`. Each set contains exactly K indexed centers. For all the actual 28-bit backgrounds,
\[
\boxed{R_{27}(K)=1\quad(214\le K\le291)},\qquad
\boxed{R_{25}(K)=1\quad(223\le K\le291).}
\]
In fact, every newly feasible optimal center set can be repaired without altering any other selected center by the replacements **479→480** for cut 27, or **438→439** for cut 25, whenever it is not already old-optimal. The respective cut starts at event indices 482 and 441.

These are exact special-case results for the frozen instance. At K=214–221 the effective other cuts 3,8,9,10 remain to be analyzed for recourse; the theorem makes no assertion about their maximum replacement distances.

## Reduction to the tested backgrounds

Prior R5 global optimizer-family support theorem (Draft PR #2427 at \`ccd014a53eebefc7516da4b1442162749d5c1c0d\`) proves that \`Opt_B(K)\` depends only on
- \`E(K)={3,8,9,10,27}\` at K=214–221;
- \`E(K)={27}\` at K=222;
- \`E(K)={25,27}\` at K=223–291.

It follows that every possible 28-cut background is represented exactly by the matching restriction to E(K), even though the coordinate arrays of those backgrounds can differ. This is a **family-level equality**, not a claim of native state equality. Exhaust all 16 cut-27 transitions in the first band at each of 8 budgets, the sole cut-27 transition at K=222, and both cut-25 and cut-27 transitions for both backgrounds at each of the 69 budgets K=223–291: **405 exact directed family transitions**.

## Certified finite proof: global optimum paths and complete local repairs

For a fixed closure mask, take vertices 0,...,953 representing center event indices in increasing order. An edge i→j (i<j) is permitted if all intervening events lie within distance two of their nearer endpoint, and carries the exact sum of these intervening minimum distances. At the endpoints add the first-/last-center prefix/suffix coverage and costs. Every feasible K-center subset gives one increasing path with K vertices, and every such path gives one feasible subset with exactly its total nearest-center distance cost. Because all event gaps are at most 3, feasible successive centers in this frozen integer instance are separated in coordinate by at most 7; the verifier constructs precisely those edges.

Compute shortest-path forward tables \`C[t][j]\`, backward tables \`D[t][j]\`, and the global optimum \`J(K)\`. An edge on a global shortest K-center path is selected only if its prefix, edge, suffix and center count attain \`J(K)\`. For a target cut starting at event index i, enumerate every optimal-path center subword P inside \`[i-9,i+9]\`; a predecessor within seven preceding indices and the first succeeding vertex ensure no optimum path is omitted. This is finite exhaustive enumeration of *local patterns occurring on global optimum paths*, rather than sampling center configurations.

Take the event window \`W=[i-6,i+7]\`. All center indices outside \`[i-9,i+9]\` are more than two coordinate units from W, since successive integer event indices differ by at least one. Thus P computes the exact feasible distances and sum on W. Outside W, both the one-gap closure and any replacement of a center \`p\in[i-4,i+5]\` by \`q\in[i-4,i+5]\` leave the minimum-distance vector unchanged: event coordinates on the same side of the changed gap undergo only a rigid translation; an event outside W is more than two away from all changed centers or opposite-side centers across the gap. Therefore, if the old-coordinate local feasible maximum distance and local cost agree with the new-coordinate local values after such a replacement, the full old-coordinate center set is feasible and has exactly the same global cost \`J(K)\`, hence belongs to the old optimal family.

The attached original standard-library Python verifier exhausts each such optimal-path P. It tests first whether the same centers are old-optimal. Otherwise it searches every admissible one-center exchange, verifying the two local exact integer quantities. **All 22,389 local patterns, over 405 transitions, are certified as unchanged or one-exchange repairable**, with a strict one-exchange pattern in every tested transition. All one-exchange witnesses use only the replacements above.

Every pattern arises on some globally optimal new-center path, so the strict witnesses establish \`R_i(K)\ge1\`; the local repair lemma and exhaustive coverage establish \`R_i(K)\le1\`. The equality follows with the required nested quantifier order.

## Execution evidence and reproducibility

\`VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py\` is the executed source, self-contained (Python standard library). Run:

\`\`\`bash
python VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py > EXACT_R5_LOW_BUDGET_UNIT_RECOURSE.json
\`\`\`

Observed: \`PASS_EXACT_R5_LOW_BUDGET_ONE_SWAP\`; **405 transitions** (267 for bit 27, 138 for bit 25); **22,389** complete local-pattern checks. Full deterministic stdout JSON: **107,384 bytes**, SHA-256 \`a5688e231fcd3e5954925823deb7b333bcadace5fb2eb92ad0bcc0049ae73a7b\`. In addition, a separate independent full-path sampler rebuilt exact globally optimal K-center sequences and checked entire 954-event distance vectors for 56 full-path instances: \`PASS_R5_FULL_PATH_RANDOM_CROSSCHECK 56\`. That sampler is a consistency check rather than the exhaustive proof.

The output is reproducible from the committed verifier. Frozen scientific input and the previous support theorem are cited as premises. Independent mathematical peer review remains \`NOT_REVIEWED\`; no formal task result, CLAIM, or privileged RA checkpoint is claimed by this author-side branch.

## Remaining research

Calculate exact worst necessary replacements for bits 3,8,9,10 at K=214–221 (their local optimal center path structures can require nonlocal repairs); examine the low-budget boundary K<214 under its own feasibility/cost conditions. Compare this exact derived-index observer with any richer X6/BRC provenance observer only after an explicit preservation mapping.