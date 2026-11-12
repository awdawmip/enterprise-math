# R737 — Conditional P000 X6 triad-channel BRC lift, exact three-state repair and tenfold rotation obstruction

Date: 2026-11-12 (Asia/Shanghai). Author-side mathematical derivation and exact-integer checking; independent review pending.

Mother task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`. **Frozen scientific source:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`, especially \`p000_reality_foundation.json\`, \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\`, \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` and \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`. Derived, not admitted, BRC inputs: R735 at \`dedb2aee4c7a55ca6c68b53f823efdcb7921f9fd\` and R736 at \`d6f1856271183b353375b1c2a9b4db2dba1f6a25\`.

## 1. Typed Cell and force-triad construction

Let \`X\` be the native signed X6 spatial Cell torsor over \`Z^6\`. Choose a Cell \`C in X\` and an injective three-slot axis frame \`f:{0,1,2}->{1,...,6}\`. Give the Cell three explicitly sourced nonzero primitive force quanta
\[
Q_j=(\mathrm{Cell}=C,\ \mathrm{direction}=+E_{f(j)},\ \mathrm{quantum}=1,\ \mathrm{source\_slot}=j),\quad j=0,1,2.
\]
All three directions are signed native axes, and their distinct axes satisfy P000 pairwise \`PERP_E\` with native 120-degree right angle. We take the triple to be a **chosen canonical equal-quantum closed triad**, with the explicit typed incidence \`TRIADIC_CLOSURE_E(C;Q_0,Q_1,Q_2)\`. This is a *conditional instance of the P000 canonical triad type*, not an assertion that arbitrary three independently selected forces necessarily close. Slot permutations preserve the same three nonzero force tokens, their physical Cell, directions, quantum values and explicit closed incidence. The source-slot-to-axis attachment is part of the internal relational state.

Time is an ordinal of ordered channel events, not an elapsed physical heartbeat interval. These candidate updates change a Cell-attached *internal relation*, not the native Cell's spatial position. They neither introduce a primitive diagonal spatial step nor a primitive zero/two-force balance. This mathematical construction specifies one possible conditional channel model; deploying a lawful V29 PASS/TRANSFER event realization is a separate test.

## 2. Rooted BRC words and exact S6 covariance

Take the positive rooted cyclic-nonbacktracking three-step return generators verified in R735:

| Carrier | I (identity) | P | Q |
|---|---|---|---|
| A | \`012>014>013>012\` | \`012>023>013>012\` | \`012>023>123>012\` |
| B | \`012>123>124>012\` | \`012>023>013>012\` | \`012>123>013>012\` |

Here the three-digit words are V17 slot images, with carrier A's \`p=021, q=102\` and B's \`p=021, q=210\`; \`p\` and \`q\` are distinct transpositions of three slots. Write \`e\` for the identity and \`r=pq\` for a three-cycle. Each block \`I,P,Q\` permutes the ordered source/axis frame by *right composition* with \`e,p,q\`. Maintain full ordered BRC branch/arc provenance, not just letter counts.

For every finite word \`w\`, the resulting channel frame is
\[
 f_w=f_0\circ h(w),\qquad h(w)=g_1g_2\cdots g_n \in S_3 .
\]
In both carriers, root incoming and outgoing neighbors are disjoint (R735), hence concatenating any of the three rooted returns produces another legal cyclic-nonbacktracking return. For any rotation \`\sigma\in S_6\` acting by permutation of the six *positive-axis labels*, and for any update letter \`g\`,
\[
 U_g(\sigma\circ f)=\sigma\circ f\circ g=\sigma\circ U_g(f).
\]
This proves **exact S6-equivariance for this conditional local channel** at every word length. It preserves the unordered triad's Cell, force count, signed native directions up to rotation, and \`TRIADIC_CLOSURE_E\` incidence. S6 is the frozen finite axis-permutation rotation skeleton, not a proposed description of every native rotation.

## 3. Three-state online residual: constructive sufficiency and sharpness

Within the above three-return submonoid, R735 proves that either complete directed-arc counts \`N\` or its pooled four-port/two-PASS 12-counter observer \`Y\` determines generator counts \`(c,a,b)\` for \`(I,P,Q)\`. Set \`\epsilon=(a+b) mod 2\`. A single extra state \`k\in Z/3Z\` suffices to recover the exact final named holonomy:
\[
h=r^kp^\epsilon.
\]
Start \`(c,a,b,k)=(0,0,0,0)\`. On \`I\`: increment \`c\`, keep \`k\`. On \`P\`: increment \`a\`, keep \`k\`. On \`Q\`: increment \`b\`, compute new \`\epsilon'=(a+b) mod 2\`, then update
\[
k\leftarrow k+(-1)^{\epsilon'}\pmod 3.
\]
Proof: \`p^2=e\`, \`q=pr\`, \`prp=r^{-1}\`. Right multiplication of \`r^kp^\epsilon\` by \`p\` toggles the parity without changing \`k\`; right multiplication by \`q=pr\` changes the parity and contributes \`r^{(-1)^{\epsilon'}}\`. Induction proves the invariant for **every word**, not only a bounded test window.

The lower bound is attained at the four-block words \`PPQQ\`, \`PQPQ\`, \`QPQP\`: all have the same letter counts \`(0,2,2)\`, and hence the same complete \`N\`, \`Y\`, Cell and unordered force triad, but yield three different named slot/axis attachments.

| Carrier | PPQQ | PQPQ | QPQP |
|---|---|---|---|
| A | 012 (k=0) | 120 (k=2) | 201 (k=1) |
| B | 012 (k=0) | 201 (k=2) | 120 (k=1) |

Thus, for the declared final ordered-triad observer and with the full count ledger available, **exactly three** extra residual states are both necessary and sufficient. These are 12-step *abstract positive-BRC CNB histories*; they are not yet physical V29 execution traces.

## 4. New tenfold native-force decomposition and a rotation obstruction

At the same chosen Cell, consider six distinct positive unit force tokens directed along \`+E_1,...,+E_6\`. Assume each selected three-token equal-quantum triple is equipped with the explicitly admissible canonical \`TRIADIC_CLOSURE_E\` incidence. A structural division of these six tokens into two **unordered** closed triples corresponds to an unordered partition of \`{1,...,6}\` into two 3-subsets. There are exactly
\[
D_6={1\over2}{6\choose3}=10.
\]
S6 acts transitively on the ten partitions; the stabilizer of one is \`(S3 x S3) semidirect C2\`, of order \`3! 3! 2=72\`, and \`720/72=10\`.

**Theorem (no unmarked equivariant single-partition selector).** No deterministic selector from this unmarked six-force population to exactly one of the ten partitions can commute with all S6 axis permutations. The input is fixed as an unordered whole by every S6 element. An equivariant selector's output would therefore be a partition fixed by all rotations. But the action is transitive on ten distinct partitions, and has no global fixed partition. Contradiction.

A model can instead retain the ten positive BRC provenance branches, or specify a genuine symmetry-breaking mark/state that itself transforms equivariantly. To encode one of ten distinct chosen partitions in fixed-length binary requires at least \`ceil(log2 10)=4\` bits. This is a structural **decomposition/covariance theorem** under the stated canonical incidence assumptions; global dynamic stability of a six-force population is not asserted.

## 5. Triadic lift of a two-force observation

Define a coarse observation mapping a source-preserving triad \`(Q_0,Q_1,Q_2;TRIADIC_CLOSURE_E)\` to the visible ordered pair \`(Q_0,Q_1)\` and an **effective balance flag inherited from its hidden third-source incidence**. It has a canonical triadic witness in the full state. Its two visible quanta are not a new primitive two-force balance. For a future operation that can address the third slot, or select a decomposition in the six-force case, discarding the hidden incidence/branch fails observer safety.

This explicitly defines an observer and a repair; it does not assert every physical apparent two-force measurement admits this particular lift.

## 6. Verification, scope and next test

The Python-standard-library integer verifier \`R737_TRIAD_COVARIANT_SCHEDULER_VERIFY.py\` checks for each of A and B: nine generator seams and legal three-arc returns; all \`1+3+...+3^8=9841\` words against the exact \`r^kp^\epsilon\` invariant; all 720 S6 rotations against 81 length-four words (58,320 cases/carrier); three same-ledger/different-holonomy witnesses; all ten six-label triadic partitions, orbit size ten, stabilizer order 72 and absence of an S6-fixed partition. Its result is \`R737_TRIAD_COVARIANT_SCHEDULER_RESULTS.json\` with \`status=PASS\`. Infinite-length correctness follows from the displayed algebraic proofs; finite checks corroborate implementation.

The **next testable native step** is to take one selected closed Cell triad, instantiate each of the R735 three-arc returns as three **authorized V29 Link/Port/PASS/TRANSFER native events**, include Cell source/incidence and ordered time witnesses, and check the full ledger against both \`h(w)\` and \`k\`. A specific failed event realization narrows that scheduler, while the conditional channel construction and tenfold symmetry theorem remain at their declared scope. Full original Task hard-target coverage and independent mathematical review remain open.

**Status:** exact author-side conditional constructive special family and finite exact test; no official Source CLAIM/Result or independent mathematical admission is implied by this artifact.
