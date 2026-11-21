# X6 native time — Unit233: P000 S6-realizable OUTER-C12 symmetry and sharp holonomy classes

Date: 2026-11-21 13:00 Asia/Hong_Kong. Task: \`RS-X6-NATIVE-TIME-DYNAMICS\`, publication \`TP2-91D4A7C2F63805BE21A3\`. Author lineage: \`EM-X6-FB6990\`, Source session \`MCP-082892eb480e45dea6d4b9fcc0491034\`, Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**. Conditional mathematics on the frozen restricted OUTER-C12 Cell graph; not a declared physical precision-fiber update.

## Scientific pins and the question actually resolved

- \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` (ACTIVE_LOCKED P000 V5): six native signed spatial axes, a **positive-axis permutation S6 rotation skeleton**, and nonspatial time.
- Same frozen commit: \`research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md\`, §§3–10: a 12-Cell primitive-step OUTER loop inside one selected STAR slice.
- Same frozen commit: \`research_notes/VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md\`: relative static principal-root selection \`Sigma(A(k,epsilon))=3 epsilon\` from oriented six-step arcs; not a physical fiber transfer rule.
- User-protected \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\` and current ACTIVE residual-fidelity worldview: preserve Link, orientation, branch, provenance and future-relevant joint observers.
- Unit232 pinned source \`awdawmip/enterprise-math@a5e42e421d375628f12c64deeb5f67e733d7b3f3:research_notes/X6_TIME_OUTER_C12_MACROSHIFT_REFLECTION_HOLONOMY_OBSTRUCTION_20261121_1200.md\`: the two imposed graph symmetries imply \`H=6(a-theta(a))\`. This unit checks which of those graph automorphisms actually belong to the P000 **S6 positive-axis-permutation skeleton**, rather than treating graph automorphisms as physical rotations.

This is a source-scope correction of the model-selection question, not repetition of the Unit232 conditional theorem.

## Exact native Cell and symmetry model

Within a centered selected three-axis slice of the **six-dimensional** X6 spatial torsor, write the six signed radius-one relative Cell vectors as
\`a_0=e1, a_1=e2, a_2=e3, a_3=-e1, a_4=-e2, a_5=-e3\`.
Set \`v_(2r)=a_r\`, \`v_(2r+1)=a_r+a_(r+1)\` for \`r in Z/6Z\`. The 12 \`v_q\` are distinct and each \`v_q -> v_(q+1)\` is exactly one signed native-axis step. The three omitted X6 components are zero *because membership in this selected slice is explicitly imposed*, not because the full world is three-dimensional. Absolute Cell locations require the pivot anchor; these are relative signed chart vectors, not final six-field nonnegative public addresses.

Let \`C={v_0,...,v_11}\`. Consider **only** the previously frozen P000 skeleton \`S6\` acting by positive-axis coordinate permutation \`e_i -> e_(p(i))\`; sign reversal is not silently declared a member of that skeleton. Its setwise stabilizer is \`Stab_S6(C)\`.

### Theorem 1: exact S6 cycle stabilizer

\`Stab_S6(C) = ( {id,(1 3)} on active axes {1,2,3} ) × S_{ {4,5,6} }\`, a subgroup of order **12**. On the twelve vertices, the induced image has exactly two elements:
\`id: q -> q\`; and \`T: q -> (4-q) mod 12\`, the second being orientation-reversing. There is **no nonidentity orientation-preserving C12 phase shift induced by the P000 S6 skeleton** on this chosen OUTER loop.

**Proof.** The six radius-one vertices are precisely \`{±e1,±e2,±e3}\`; positive-axis permutations preserve both radius and sign. Stabilizing these vertices forces preservation of the active three-axis subset, while the remaining axes may be freely permuted (factor S3). Adjacency among the radius-one vertices through the OUTER intermediate Cells comprises the unordered pairs \`{a_r,a_(r+1)}\`. Of these, the only two cross-sign pairs are \`{e3,-e1}\` and \`{-e3,e1}\`. A positive-axis permutation preserving the loop must preserve or exchange these two pairs. Thus its action on the active axes is either identity or \`e1 <-> e3\` with \`e2\` fixed; both do preserve every loop edge. The swap sends \`a_r -> a_(2-r)\` and hence sends \`v_q -> v_(4-q)\`. The full count is \`2·3!=12\`. The identity action on active axes fixes all twelve vertices, whereas the swap reverses their orientation. QED.

The shift \`R:q->q+2\` used as an additional hypothesis in Unit232 sends \`e3\` to \`-e1\`; it is a **signed-coordinate permutation graph automorphism** on the restricted loop, but is not in the positive-axis-permutation \`S6\` skeleton. Likewise the specific Unit232 reflection \`q->-q\` is a signed-permutation graph automorphism, not an S6 positive-axis permutation on this selected loop. They remain valid model transformations when explicitly hypothesized, but are not automatically imposed by P000's S6 skeleton.

### Theorem 2: sharp attainable holonomy under only the S6-realizable reflection

Let \`A\` be any abelian additive fiber, and \`theta:A->A\` any involutive additive automorphism. For a reversible additive update on each directed OUTER Link \`e_q:v_q->v_(q+1)\`, write its fiber increment \`w_q in A\`, with reverse traversal \`-w_q\`. **Hypothesize** that the physically proposed fiber update is covariant under the one nontrivial S6-induced loop reflection \`T\`, acting on the fiber by \`theta\`.

Because \`T(e_q)\` reverses the Link indexed by \`3-q\`, covariance is exactly
\`theta(w_q)=-w_(3-q)\` (indices modulo 12).
The involution \`q->3-q\` has **six disjoint two-edge orbits**, none fixed. Choose one representative from each pair and write its increment \`a_i\`. Its partner must have increment \`-theta(a_i)\`. Therefore
\`H=sum_q w_q = sum_(i=1)^6 (a_i-theta(a_i))\`.
The **exact attainable subgroup** of complete clockwise loop holonomies is
\`H in Im(id-theta)\`.
Conversely every \`h=a-theta(a)\` is realized by putting \`a\` and \`-theta(a)\` on one reflection edge-pair and zero on all other pairs, proving sharpness. Also \`theta(H)=-H\`.

For comparison, the strictly *stronger* simultaneous graph-macroshift hypothesis in Unit232 makes every even Link carry the same \`a\` and every odd Link carry \`-theta(a)\`, hence shrinks the exact subgroup to \`6 Im(id-theta)\`. The factor six is caused by that **additional dynamical covariance hypothesis**, not by the P000 S6 spatial permutation skeleton alone.

### Concrete finite precision consequences and witness

For \`A=C_(6·2^m)\` and \`m>=1\`:
- With \`theta=id\`, \`Im(id-theta)={0}\`, so \`H=0\`.
- With \`theta=-id\`, \`Im(id-theta)=2A\`, exactly the even residues. In particular \`H=[6]\` is allowed at every precision level. At C24 there are exactly **12** such holonomy values (compared with **2** values under Unit232's additional macroshift).

A reversible witness at every level is \`w_5=w_10=3\`, all other \`w_q=0\`. These two edges are paired by \`q->3-q\`; the reflection uses \`theta=-id\`, so the field is covariant. The full positive circuit has \`H=6\`, the negative circuit has \`H=-6\`, and the two particular clockwise half-circuits from \`q=0\` have increments \`3\` and \`3\`. It **fails** the extra \`w_(q+2)=w_q\` macroshift condition. This is a precise conditional repair of the over-restrictive symmetry assumption, *not* evidence that the physical X6 fiber actually evolves according to these weights.

## Reproducible calculation and BRC observer lease

The exact Python checker \`research_checks/X6_TIME_S6_OUTER_REFLECTION_HOLONOMY_CHECK_20261121_1300.py\` enumerates all **720** positive-axis permutations, verifies the twelve stabilizers and their identity/reflection action on all twelve native Cell vertices, and verifies **4,846** finite modular covariance/congruence assertions across C6/C12/C24/C48/C96 and \`theta=±id\`, without mismatches. It also verifies twelve primitive signed-axis Links, six reflection edge-pairs and the \`w5=w10=3\` witness. The general image theorem is proved symbolically above, independent of the finite tests.

Population: one actual previously proved OUTER native Cell loop in the selected STAR slice, retaining full X6 slice embedding, each primitive signed Link, orientation, ordered provenance and the independent hypothetical fiber. Operator horizon: \`S6\` positive-axis spatial permutations **that preserve this particular loop**, Link reversal, and explicitly hypothesized fiber reflection. Readout: clockwise/anticlockwise fiber holonomy if an independent physical fiber readout exists. Endpoint-only, fixed static relative root \`Sigma\`, and C12 phase projections are strictly different observers. No physical fiber update law, source-specific \`theta\`, observed holonomy or independence-admitted Result has been supplied.

## Next original mother-objective action

Use the frozen task pins and actual Cell/Link/Port sources to determine whether a *physical* fiber and \`theta\` action are specified. For a supported native update, calculate clockwise/anticlockwise holonomies at the same Cell and compare C12/C24 observable readouts; test any actual macroshift symmetry rather than importing signed graph automorphisms as P000 rotations. Keep the separate R063 six-file native benchmark unchanged and pending its original task/support owner. Unit233 is a reusable sharp restriction/repair for evaluating such a proposed rule, not completion of the native physical time law.
