# X6 Unit183 — exact primitive trace lift and weighted observer-descent criterion

**Date:** 2026-11-20. **Parent:** \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`. **Task:** \`RS-X6-LEGACY-PLANE-RECONCILIATION\` / \`TP2-B4A441B23DA3159232C2\`. **Research lane:** \`chatgpt-research-onhour-enterprise-math-20260923\`, distinct from the maintenance lane. **Frozen science pin:** \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`; historical comparison pin \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / SOURCE_PUBLICATION_PENDING_READBACK / UNREVIEWED / NOT_ADMITTED. This unit concerns the signed native six-axis *coordinate-step submodel*. It does not claim that all P000 time, force, field, path decorations or physical dynamics descend.

## Consumed foundation and new question

The ACTIVE X6 Cell-torsor definition \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\`, sections 2–6, already freezes the full signed carrier \(\mathbb Z^6\), twelve primitive coordinate steps \(V=\{\pm e_i:1\le i\le 6\}\), relative map \(q(z)=\operatorname{can}_6(z)=z-\min(z)\mathbf1\), and one integer common-depth carry. The frozen \`research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md\` defines exact all-length native BRC endpoint counts. Unit182 proved the endpoint-fiber sum \(R_M(a)=\sum_h S_M(a+h\mathbf1)\) and the first observer-return leak at six steps. No part of those known results is re-originated here.

**New discriminator:** Is a complete time-ordered relative-coordinate trace sufficient to recover *which signed primitive events occurred*, despite not recovering the native absolute endpoint from one final relative snapshot? Which weighted primitive future kernels descend without retaining common depth?

## Theorem 1 — twelve marked native directions remain distinguishable in the relative trace

Let \(A=\{a\in\mathbb Z_{\ge0}^6:\min_i a_i=0\}\). For a primitive direction \(v\in V\), define
\[
  F_v(a)=\operatorname{can}_6(a+v),\quad
  c_v(a)=\min_i(a_i+v_i)\in\{-1,0,1\}.
\]
Then:

1. **All twelve successors are distinct at every relative state:** \(F_v(a)=F_w(a)\) implies \(v=w\) for \(v,w\in V\).
2. Every valid sequence of relative observations \(a_0,a_1,\dots,a_M\), with each \(a_{t+1}=F_{v_t}(a_t)\) for some primitive \(v_t\), uniquely determines the **entire ordered signed-axis word** \(v_0,\dots,v_{M-1}\), even without an initial native depth.
3. Given the single integer \(h_0\), the exact native signed spatial states are recovered by
\[
 h_{t+1}=h_t+c_{v_t}(a_t),\qquad z_t=a_t+h_t\mathbf1.
\]
Thus \((a_0,\ldots,a_M,h_0)\leftrightarrow(z_0,v_0,\ldots,v_{M-1})\) is bijective within this primitive-step model. Removing \(h_0\) leaves precisely a uniform diagonal-translation ambiguity, not a primitive-event ambiguity.
4. The carry is **not globally eliminable** for absolute spatial position: the six-step word \(+e_1,\ldots,+e_6\) returns to the same relative state but changes \(h\) by \(+1\). Similarly, the six negative directions change \(h\) by \(-1\). A nonzero carry on a closed relative word first becomes possible at length six.

**Proof.** If \(F_v(a)=F_w(a)\), then the full vectors \(a+v\) and \(a+w\) differ by some \(k\mathbf1\). Hence \(v-w=k\mathbf1\). Since \(v-w\) is supported on at most two of six coordinates, four coordinates of this difference vanish, so \(k=0\) and \(v=w\). The observer pair \((a_t,a_{t+1})\) therefore identifies exactly one \(v_t\). Decomposition \(z=a+h\mathbf1\) is unique, and
\[
a+h\mathbf1+v=\operatorname{can}_6(a+v)+(h+\min_i(a_i+v_i))\mathbf1.
\]
Induction proves the lift formula and bijection. Finally, the composite displacement of a relatively closed word is \(k\mathbf1\); if \(k\ne0\), its primitive length is at least \(6|k|\). The six positive (or negative) coordinate directions achieve the bound. This proof is for all integer states and all finite primitive-word lengths; it uses no finite-test extrapolation.

**Consequence for BRC.** A complete ordered relative trace retains the original primitive direction word, and hence its branch provenance within this declared coordinate graph. A *single terminal relative endpoint* does not retain native endpoint multiplicity (Unit182), nor does the relative trace alone fix a globally translated native anchor. Path/field/weight decorations beyond the primitive directions require their own preservation checks.

## Theorem 2 — exact strong lumpability criterion for weighted signed-coordinate transitions

For each full state \(z\in\mathbb Z^6\) and \(v\in V\), let \(w_v(z)\) be a nonnegative rational transition weight. The full-state one-step kernel sends \(z\) to \(z+v\) with weight \(w_v(z)\); it is a Markov kernel if \(\sum_{v\in V}w_v(z)=1\) for each \(z\).

A well-defined *memoryless weighted quotient kernel* on \(A\), valid for every native initial lift, exists **if and only if**
\[
  \boxed{\forall z\in\mathbb Z^6,\;\forall k\in\mathbb Z,\;\forall v\in V:
  \quad w_v(z+k\mathbf1)=w_v(z).}
\]
In that case, \(K_A(a,F_v(a))=w_v(a)\); the twelve target addresses are distinct, so no aggregation ambiguity arises at one step. Iterating this kernel and retaining the relative trace computes exact relative path masses. For any fixed initial native anchor, the full endpoint mass is recovered if the integer depth is propagated as in Theorem 1.

**Proof.** Sufficiency follows directly from \(q(z+v)=F_v(q(z))\) and weight invariance. Necessity follows because all twelve \(F_v(a)\) are different: the quotient transition mass to \(F_v(a)\) equals exactly \(w_v(a+h\mathbf1)\); independence of the chosen lift \(h\) forces the displayed equality for each \(v\).

Fixed positive rational primitive weights, as in the existing signed all-length Weighted-BRC kernel, satisfy the criterion. A spatially varying weight depending only on pairwise coordinate differences also satisfies it. A weight depending on native depth or the sign of an individual absolute component may fail.

**Explicit failure:** Let \(w_{+e_1}(z)=1\) when \(z_1>0\), \(w_{-e_1}(z)=1\) otherwise, and let the other ten weights vanish. States \(z=0\) and \(z'=\mathbf1\) have identical \(q(z)=q(z')=0\), but their next relative endpoints are \(F_{-e_1}(0)\) and \(F_{+e_1}(0)\), which are different. Hence no quotient-only memoryless Markov kernel describes this native operation. The precise repair for this operation is the missing depth (or a sufficient predicate derived from it); for **all** full native spatial positions the one integer depth is necessary and sufficient because each fiber is \(\{a+h\mathbf1:h\in\mathbb Z\}\).

## Finite exact execution and source boundary

A separate Node.js integer checker enumerated all **665** relative states in \(\{0,1,2\}^6\) with minimum zero, all **7,980** marked outgoing edges, and **23,940** full/native lift comparisons across initial depths \(-5,0,8\). It also enumerated all **45,242** primitive path-prefix traces of lengths 0–4 from two initial depths \(-2,3\), checking that successive relative observations uniquely recover each original event. Zero violations. An independent Python check confirmed that every one of the same 665 states has exactly 12 distinct outgoing relative successors. All tests use exact integers. Universal claims are proved above; the finite execution is diagnostic evidence only.

Artifact paths:
- \`research_checks/X6_UNIT183_RELATIVE_PRIMITIVE_TRACE_COCYCLE_CHECK_20261120.js\` (actual executed checker, Git blob/readback to be recorded);
- \`research_checks/X6_UNIT183_RELATIVE_PRIMITIVE_TRACE_COCYCLE_RESULTS_20261120.json\` (exact integer certificate).

**Provenance and scope:** \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` at the frozen science pin has verified Git blob \`b4d49a1bbcccad0521618c6d20f6dcfa242b420a\`, and \`research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md\` has blob \`aa005cd62c45d7f4105632257db9186b115c5b29\`. Unit182 consumed at \`17350b0bd567dfdafee44e1e19e5704c523a7c1c\`. The three-axis \`diagonal_quotient.py\` implementation was already fully audited by Unit178; it is not misrepresented as a six-axis native production operator. This unit is a **source-typed exact mathematical classification**, not an R063 native benchmark execution, accepted Result, P000 change, or independent review.

**Remaining obligations:** LP011/LP019 alleged historical offending \`commit:path:line\` remain unknown; original R063 benchmark was completed earlier with 17/17 acceptance and 512/512 regression and was not rerun; author Units175–182 plus this new unit require current same-lane authenticated Native PROGRESS; Units149–152 older association and independent Driver review remain separate. The original Researcher/SID/CLAIM/RUN references are historical provenance, never fresh write authority. Maintain the research/maintenance lane separation.

**Next scientific discriminant:** take one *actually sourced* state-dependent consumer and check the above diagonal-invariance condition on its entire declared future operation, not merely its final endpoint; if it fails, determine the smallest additional typed residual for that consumer.