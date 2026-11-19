# X6 R37 — Linear deterministic cutoff and subset-determinized future-language certificate

Date: 2026-11-20 (Asia/Shanghai)
Task relevance: RS-X6-NATIVE-TIME-DYNAMICS (independent portable research unit; **no native CLAIM/PROGRESS asserted**).
Provenance: continuation of the previously published R36 finite full-future transfer certificate. R36's historical attribution remains EM-X6-214D9C; this document does **not** claim possession of its private execution capability or append to its Activity.
Status: AUTHOR_PROOF / EXHAUSTIVE_DECLARED_FINITE_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` (V5).
Prior scientific input: \`research_notes/portable_direct/2026-11-20_x6_native_future_transfer_certificate_r36.md\`.
Observer: complete *successful* finite event words, with the full source/Port-named label retained; no independently visible state readout, probability or multiplicity claim.

## R37.1 — A sharper cutoff in the deterministic finite case

Let A and B be **deterministic partial** transition systems over the same finite alphabet \(\Sigma\). Their state counts are \(n_A,n_B\ge 1\); all finite executable words, including \(\epsilon\), are successful. For \(p\in Q_A,q\in Q_B\), write \(L_A(p)\), \(L_B(q)\) for these prefix-closed future languages.

**Theorem.** The following equivalence holds:

\[
\boxed{L_A(p)=L_B(q)\iff L_A(p)\cap\Sigma^{\le n_A+n_B-1}=L_B(q)\cap\Sigma^{\le n_A+n_B-1}.}
\]

Consequently any language inequality has a shortest labelled distinguishing word of length \(\le n_A+n_B-1\). This improves R36's product cutoff \(n_A n_B\) whenever both state sets have at least two elements (strictly for \(n_A,n_B>1\), except \(n_A=n_B=2\) already strict: \(3<4\)).

**Proof.** Take the disjoint union of A and B and add one *shared* rejecting sink \(\bot\). Complete every undefined labelled transition to \(\bot\), and loop every label at \(\bot\). Mark all \(n_A+n_B\) original states accepting, and \(\bot\) rejecting. From every original state the accepted language is exactly its original successful-word language.

Define the depth-h equivalence partition \(P_h\) on this \((n_A+n_B+1)\)-state complete automaton by equality of accepted words of length at most h. Initially \(P_0\) has **exactly two blocks**: all accepting states and the sink. Recursively, \(P_{h+1}\) refines \(P_h\) using each state's current acceptance and the \(P_h\)-blocks of its successors at every named label. If a round produces no further split, all later rounds remain unchanged (the refinement map depends only on the current partition); otherwise the block count grows by at least one. There are at most \(n_A+n_B+1\) blocks. Therefore stabilization occurs by \(n_A+n_B-1\) rounds, at the exact full-future-language equivalence. Restrict to \((p,q)\). QED.

The bound is sharp already at \((n_A,n_B)=(2,2)\): R36's exact pair
\[
 A=\begin{pmatrix}\varnothing&\{0\}\\\{0\}&\varnothing\end{pmatrix},
 \qquad
 B=\begin{pmatrix}\varnothing&\{1\}\\\{0\}&\varnothing\end{pmatrix}
\]
with initial states \((1,1)\) first differs at \(Q_0Q_1Q_0\), of length 3.

## R37.2 — Nondeterministic native branches need subset states

Now let A,B be finite **nondeterministic** partial labelled transition systems, with existential success: a word is observable iff *at least one* path carries the entire word. Multiple successor states under the same complete event label are permitted. The current reachable set of states, not an arbitrary selected branch, is the sufficient Boolean-support state.

For a chosen initial state, let \(S_A,S_B\) denote their reachable **nonempty** successor subsets under subset determinization, and write \(m_A=|S_A|,\ m_B=|S_B|\). Then

\[
\boxed{L_A(p)=L_B(q)\iff L_A(p)^{\le m_A+m_B-1}=L_B(q)^{\le m_A+m_B-1}.}
\]

In particular, a finite distinguishing word, if one exists, has length bounded by
\[
\boxed{m_A+m_B-1\ \le\ 2^{n_A}+2^{n_B}-3.}
\]

**Proof.** A labelled word survives precisely when its reachable subset is nonempty. Subset determinization maps each nonempty subset to the union of its labelled successors, and all empty successors to one shared absorbing reject sink. This is a deterministic partial system on exactly \(m_A,m_B\) reachable nonempty subset states, with the same successful-word languages. Apply R37.1. QED.

The use of nonempty reachable subsets is essential: an arbitrary original state may have multiple indistinguishable labelled successor branches whose **union** determines later success. Neither R36's product bound \(n_A n_B\) nor R37.1's \(n_A+n_B-1\) is licensed for these nondeterministic input state counts.

## R37.3 — Explicit smallest two-state branching counterexample

Let \(\Sigma=\{Q_0,Q_1\}\). Each table entry below is the bitset of allowed successor states (bit 0 = state 0, bit 1 = state 1; 0 means none). Use initial state 1 on both sides.

\[
A=[(1,1),(1,0)],\qquad B=[(2,1),(3,0)].
\]

The successful future languages agree through **every** word of length at most 3. Their shortest difference is \(\boxed{Q_0Q_1Q_0Q_1}\), length **4**: A follows its surviving branch to state 0 and accepts, while B's only surviving state before the final \(Q_1\) is state 1, which has no \(Q_1\) successor. Hence the deterministic two-by-two bound \(2+2-1=3\) fails for a system with unobserved successor branching. This is a finite conditional event-model counterexample, not a constructed native \`TRIADIC_CLOSURE_E\` transition.

## R37.4 — Exact Boolean-BRC verification

A self-contained Node.js 18+ checker independently computes subset-transition shortest witnesses by BFS and complete depth-h Boolean-support signatures, then tests agreement at the proposed cutoff and every shorter depth. Its exhaustive finite scope is:

| Family | Machines | Ordered initial-state comparisons | Fully equivalent | First difference depth 1 / 2 / 3 / 4 |
|---|---:|---:|---:|---|
| Deterministic partial, 1 or 2 states, two labels | 85 | 27,556 | 3,384 | 19,128 / 4,884 / 160 / 0 |
| Nondeterministic partial, exactly 2 states, two labels | 256 | 262,144 | 54,224 | 159,744 / 45,328 / 2,624 / 224 |

All assertions passed. The \(n_A+n_B-1\) and \(m_A+m_B-1\) claims are established by the symbolic proofs above; computation verifies these explicitly enumerated families and supplies the sharp counterexample.

Artifacts:
- \`research_notes/portable_direct/2026-11-20_x6_linear_subset_future_certificate_r37.md\`
- \`research_notes/portable_direct/x6_r37_linear_subset_certifier.js\`
- \`research_notes/portable_direct/x6_r37_linear_subset_results.json\`

## Transfer boundary and next discriminating question

P000 fixes X6 Cell/Port typing and primitive three-force closure but has not identified an admissible complete whole-triad successor law for this particular event alphabet. A future native embedding must preserve the *actual* labels, successor branching, source identity, Cell/frame/Link updates and the observer. If branch identities become directly observable, enlarge the named alphabet accordingly; if multiplicities or amplitudes are observed, Boolean support alone is insufficient.

Next, obtain the actual frozen-P000 \`TRIADIC_CLOSURE_E\` event law if available. Determine whether complete source/Port labels make its transition relation deterministic; otherwise use the reachable-subset construction before applying the transfer certificate. Test a finite closed native subsystem (or provide a typed coinductive relation for an infinite one), retaining precision/refinement address separately from physical event time.

No formal Result/Review or current RUN/CLAIM publication is asserted. Activity association requires the actual original research session and portable Activity authority; preserve this artifact independently until such authority is verified.
