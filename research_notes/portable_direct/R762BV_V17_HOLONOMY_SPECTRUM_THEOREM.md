# R762BV — Exact V17 active-triad holonomy spectrum, shortest residuals and a finite certificate

Date: 2026-11-16 (Asia/Shanghai). Research task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Scientific status: AUTHOR-PROVED / EXACT INTEGER CHECK / NOT_REVIEWED.

## Sources, premises and provenance

Frozen scientific premise: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` and the corresponding P000 signed Cell and direction definitions. All six native axes and signed X6 Cell translations remain intact. The following is a precisely **conditional internal active-frame transport** model, drawn from the separately identified current source \`research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md\` (Git blob 42b810a8f82c504833027da17884cc4fb2943e5b). It neither identifies a Johnson-triad change with an admissible physical \`TRIADIC_CLOSURE_E\` event nor claims full spatial rotation dynamics.

Additional source and future-observer contexts: V29 \`X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md\` (blob 6849ebd3fc776fb7da3b46627376490aba3dad99); V39 \`X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md\` (blob 8151d0b6a4b65225b93d858bbc8a5d7037bf9cef); R762BU author-side joint X6 relative-coordinate repair PR #2532 at commit 324997fcf3bfb62a9b6fe1a88954a6ae28a4ac29. Their scientific claims retain their original scopes.

## Exact finite model

Let \(U=\{1,2,3,4,5,6\}\). An *active triad* is any three-element subset \(S\subset U\), twenty possibilities. An *ordered internal frame* is an ordered triple \(f=(a,b,c)\) with pairwise distinct members of U, 120 possibilities; its underlying triad is \(\underline f=\{a,b,c\}\). From \(f\), choose one of the three slots and one of the three labels absent from \(\underline f\), then replace that slot by the new label. These are the nine legal V17 canonical-replacement moves on the internal frame. They determine the 120-vertex, undirected, nine-regular arrangement graph \(A(6,3)\). Forgetting frame slots yields the 20-vertex Johnson graph \(J(6,3)\), also nine-regular.

Fix \(f_0=(1,2,3)\), \(S_0=\{1,2,3\}\). A based m-step triad loop is an ordered sequence of m allowed replacements whose final underlying triad is again \(S_0\). Its resulting frame is a unique element \(h\cdot f_0\), \(h\in S_3\). These are labelled BRC histories: different intermediate paths count separately even if the final frame agrees.

Write \(C_m\) for all based loops, \(I_m\) for loops with identity holonomy, \(T_m\) for loops with any *specified* transposition, \(R_m\) for loops with any *specified* 3-cycle, and \(S_m\) for their signed holonomy sum (even minus odd). We use \(0^0=1\) in the spectral formula at m=0.

## Theorem 1 — exact all-length labelled return spectrum

For every integer \(m\ge0\), the following formulas hold **exactly over integers**:

\[
C_m=\frac{9^m+5\,3^m+9(-1)^m+5(-3)^m}{20},
\]

\[
I_m=\frac{9^m+10\,6^m+15\,3^m+18\,2^m+9(-1)^m+20\,0^m+47(-3)^m}{120},
\]

\[
S_m=\frac{3^m+(-3)^m}{2},
\qquad
T_m=\frac{C_m-S_m}{6},
\qquad
R_m=\frac{C_m+S_m-2I_m}{4}.
\]

Hence \(C_m=I_m+3T_m+2R_m\), and each transposition or 3-cycle has the stated *per-element* count.

**Proof (finite exact linear-algebra certificate).** Let \(J\) be the symmetric 20-by-20 zero/one adjacency of the triad graph. It has integer diagonal traces for powers k=0,1,2,3 equal to \((20,0,180,720)\) and is annihilated by \((X-9)(X-3)(X+1)(X+3)\). Both facts are checked by enumerating the 20 triads and their nine neighbours, and using exact integer matrix-vector multiplication on each standard basis vector, not a floating eigensolver. Symmetry makes J diagonalizable. The distinct-root Vandermonde system for the four traces uniquely yields multiplicities \(1,5,9,5\). Transitivity on based triads gives \(C_m=\operatorname{tr}(J^m)/20\), the first identity.

Let \(A\) be the symmetric 120-by-120 adjacency of the frame graph. The same exact basis-vector certificate shows
\[
p(A)=0,\quad
p(X)=X(X+1)(X+3)(X-2)(X-3)(X-6)(X-9),
\]
with low-to-high coefficients \((0,972,216,-711,120,58,-16,1)\). Its traces for powers 0 through 6 are
\[
(120,0,1080,2160,24840,129600,1044360).
\]
The seven-root Vandermonde system yields multiplicities for roots \((9,6,3,2,-1,0,-3)\) respectively \((1,10,15,18,9,20,47)\). The full symmetric group on the six native labels acts transitively on all 120 ordered frames; therefore \(I_m=\operatorname{tr}(A^m)/120\).

For the sign observer, choose each triad's canonical ascending frame. Every adjacent triad pair induces the V17 ordered-frame transport, whose sign relative to the target ascending frame is \(\pm1\). Build the symmetric signed 20-by-20 matrix \(K\) with these weights. Exact basis-vector calculation gives \(K^2=9\,\mathrm{Id}_{20}\), \(\operatorname{tr}K=0\). Consequently its eigenvalues +3,-3 each occur ten times. Switching frame gauge conjugates K by a diagonal sign matrix and leaves closed-path signs invariant. Triad transitivity (with the same transport rule) gives \(S_m=\operatorname{tr}(K^m)/20\).

Finally the stabilizer of \(S_0\) acts on based loops and conjugates their holonomy by \(S_3\), so all three transpositions have equal counts and both 3-cycles have equal counts. Since the odd total is \((C_m-S_m)/2=3T_m\) and even total is \((C_m+S_m)/2=I_m+2R_m\), the remaining formulas follow. Every step uses finite exact matrices; the formulas hold for all m because the annihilation and diagonalization identities are universal. QED.

## Theorem 2 — shortest nontrivial residual and optimal horizon-specific storage

Under the above V17 nine-neighbour operation alphabet:
- At lengths m=0 or m=2 the only reachable based-loop holonomy is identity; at m=1 there are no based loops.
- At m=3 the reachable holonomy set has exactly four elements: identity and all three transpositions. Counts are 18 and 6 per transposition, respectively. Thus exact identification of the *holonomy-only* final state requires precisely 2 bits for fixed three-step based loops.
- At m=4 every element of S3 is reachable: identity 207 paths, each transposition 48, and each 3-cycle 9. At m=5 all six are also reachable; appending a two-step move out-and-back retains holonomy, proving all six are reachable at every length m≥4. Exactly 3 bits are therefore necessary and sufficient to identify final holonomy at every such fixed length. This is a six-state residual over internal relational history, not another X6 spatial coordinate.

**Proof.** A one-step return is impossible because each step changes one native axis label; a two-step based return necessarily retracts its sole changed label and retains frame slots, giving identity. Direct classification of the 36 oriented triangular loops gives 18 flat and 18 transpositions, six of each specified transposition, and no 3-cycles. This finite classification is independently recomputed by the companion verifier by direct three-step enumeration, separately from its spectral DP. The m=4,5 positive counts for every h follow from Theorem 1 (or exact 120-state DP), so each h occurs. Adding a reversible two-step hairpin at the beginning preserves the resulting frame, yielding all larger lengths by induction from 4 and 5. With N reachable distinguishable final states, a fixed-length binary holonomy index needs at least ceil(log2 N) bits, and indexing these exact states achieves the bound. QED.

Explicit four-switch 3-cycle witness (start and end same underlying triad):
\[
123\to124\to134\to234\to123.
\]
Slot transport sends the initial frame (1,2,3) to (2,3,1). Compare the four-switch backtrack loop \(123\to124\to123\to124\to123\), which has identity holonomy. They have identical base, terminal active triad, length and **even sign**, yet distinct full S3 states. This is the shortest even-parity BRC source-loss witness in the stated based-loop family.

## Finite computation / reproducibility

Companion \`R762BV_V17_HOLONOMY_SPECTRUM_VERIFY.js\` implements integer polynomial annihilation on **all 120 frame basis vectors**, the corresponding 20 triad and signed basis vectors, exact eigenvalue multiplicity trace checks, direct independent 36 three-step loop census and exact BigInt return DP for m=0..12. This is an exhaustive finite matrix identity certificate plus finite numeric crosschecks. The proof above extends the spectral formula to every m, independently of the finite DP cutoff. Companion \`R762BV_V17_HOLONOMY_SPECTRUM_EVIDENCE.json\` records exact integer outputs and coverage. The proof is author-origin and NOT_REVIEWED.

| m | all based | identity | each transposition | each 3-cycle |
|---:|---:|---:|---:|---:|
|0|1|1|0|0|
|1|0|0|0|0|
|2|9|9|0|0|
|3|36|18|6|0|
|4|369|207|48|9|
|5|2952|1080|492|198|
|6|26937|8703|4368|2565|
|8|2155617|502119|358176|289485|
|12|14121742545|2535253191|2353535184|2262941901|

## Relation to P000, R762BU and V29/V39

The active triad is a *typed internal frame*. Its transitions are not primitive signed spatial X6 translations \(\pm e_i\); R762BU's common-depth formula applies to the separate primitive Cell endpoint observer, not to this graph's 9-way choice count. V29 PASS/TRANSFER updates have their own nonnegative ledger and conservation scope, and V39's based-loop \((j,h)\) is the coarsest port for its declared joint current-plus-holonomy language. This result supplies an exact, constructive characterization of **h's** distribution and smallest witness lengths, which can be reused in V39/BRC without erasing j, source, event count or ordered history when subsequently queried.

**Unfinished native question:** Identify actual Source-approved \`TRIADIC_CLOSURE_E\` event admissibility, signed Cell/Link/Port conservation and V17/V29/V39 joint update permissions. If real native admissible transitions form a strict subgraph of J(6,3), build its exact frame transition operator and recompute the spectrum. Test whether any native event can realize the four-switch even/3-cycle witness, and certify precisely which BRC/source coordinates descend under the declared future language. This is the next valid mathematical input to independent Driver review.

Project publication: author-side GitHub scientific artifact under the declared Task, not formal Result/Review admission. Frozen P000 is unchanged.
