# X6 Unit67 — Provenance repair: Viète reversal source under signed native X6

Date: 2026-11-16. Parent task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\` / \`TP2-B4A441B23DA3159232C2\`. Author-side source audit and exact counterexample; **UNREVIEWED / NOT_ADMITTED**.

## Located live consumer and source identity

Current-main \`research_notes/VIETE_NATIVE_TRACE_ORIENTATION_QUOTIENT_OBSTRUCTION_20260903.md\`, observed Git blob \`290fdafd1751b43e31245a666bc2ed04cec6fd20\`, retains a 2026-09-03 historical claim in language purporting to be *current native*: lines **35–41** assert canonical forward trace inverse differs from reverse trace for **every** nonzero segment, and lines **83–99** assert a reversal-asymmetric native gauge and cite unit-axis spectrum \`{1,sqrt(2)}\`. Line **124** further carries the historical asymmetry into the orientation/parity bridge. This is a concrete downstream theorem-facing consumer of the old R061 semantics, not merely a guessed caller.

Frozen active native baseline \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`, \`definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md\` lines 108–148, establishes \`d(P,Q)=q-p ∈ Z³\`, \`G(d)=Σd_i²=G(-d)\`, signed primitive steps \`±e_i\`. Current retyped \`definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md\` lines 12–49 already classifies asymmetric spectra as **relative/min-zero observer diagnostics**. Historical comparison pin: \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.

## Exact counterexample and all-displacement theorem

Choose any fixed native Cell \`P\` and \`Q=P+e_1\` in one signed three-axis slice. There is precisely one shortest primitive path word from P to Q, \`w=(+e_1)\`, and precisely one from Q to P, \`w'=(-e_1)\`. Defining path groupoid inverse as reverse *order and signs*, \`w^{-1}=(-e_1)=w'\`. Consequently the historical universal non-equality \`T(P→Q)^{-1} != T(Q→P)\` **is false if interpreted as a theorem about the current native shortest-path words**. Its old positive/min-zero decoded trace domain is retained without retroactively changing it.

For every signed displacement \`z∈Z³\`, let \`W(z)\` be the set of ordered shortest signed unit-axis step words with endpoint z. Inversion \`I(s_1,...,s_T)=(-s_T,...,-s_1)\` is an involution and bijects \`W(z)\` onto \`W(-z)\`. Hence \`|W(z)|=|W(-z)|=T!/(∏|z_i|!)\` with \`T=Σ|z_i|\`. The map preserves step-sign and path provenance *as a reversible bijection*; it does not identify different words or make an arbitrary Viète character automatically intertwine with inversion. A separately specified character \`χ\` still requires an actual factorization/intertwining proof.

The old unit-axis spectrum \`{1,sqrt(2)}\` is exact for the two **derived observer gauges**: for \`+e_1=(1,0,0)\`, \`can3(+e_1)=(1,0,0)\`, square 1; for \`-e_1=(-1,0,0)\`, \`can3(-e_1)=(0,1,1)\`, square 2. The native scalar squares are \`G(±e_1)=1\`. For \`z=(3,4,0)\`, native reversal preserves square 25 and shortest BRC 35; legacy min-zero re-decoding of \`-z\` yields \`(1,0,4)\` and square 17.

## Actual exact calculation

Companion \`research_checks/X6_UNIT67_SIGNED_PATH_INVERSION_CHECK_20261116.py\` enumerates all 125 signed triples with coordinates \`[-2,2]\`, including **1,957** ordered shortest native words, and checks that every word's inverse lands in the complete opposite-endpoint word set and double inversion returns the original word. **3,914** directed/inverse word observations; zero mismatches. Additionally checks \`±(3,4,0)\` (35 words each) and both min-zero observer counterexamples. Standard, \`python -O\`, and \`python -OO\` all give the same exact counts; failures raise exceptions independent of optimization flags. The scope is precisely the declared finite test. Universal inversion theorem is established by direct word bijection, not by extrapolating from that finite test.

## Repository action and scope

A dated top-of-file current-reader correction is added to the identified Viète note, preserving its original 2026-09-03 statements, author, historical hypothesis and #1158 orientation problem as source evidence. The correction retypes the original §§2/4/6 *native gauge and universal trace-inequality* language as historical R061 conventions, distinguishes current signed native path inversion and relative-observer asymmetry, and retains the unproved arbitrary-character bridge as an explicit further obligation.

This closes **one actual downstream old-semantic consumer** at LP008/LP011/LP012/LP013/LP019-adjacent type boundaries. It neither identifies an alleged LP011 erroneous native argmax caller nor an LP019 positive N-BRC subtraction caller. Independent Driver \`REQUEST_REVISION\` remains pending. No original R061–R063 benchmark or independent author's PR was changed; P000 and science pins remain fixed.

Status: **AUTHOR-PROVED / EXACT FINITE EXECUTED / THEOREM-FACING CURRENT-READER REPAIR / UNREVIEWED / NOT_ADMITTED**.
