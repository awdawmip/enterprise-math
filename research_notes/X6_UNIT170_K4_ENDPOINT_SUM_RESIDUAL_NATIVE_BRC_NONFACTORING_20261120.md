# X6 Unit170 — K4 endpoint-sum residual code does not determine the signed-X6 BRC comparison, even with L1 length and quadratic length

Date: 2026-11-20 (Asia/Hong_Kong). Mother task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`, immutable publication \`TP2-B4A441B23DA3159232C2\`, parent \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`. Source researcher \`EM-X6-FB6990\`, session \`MCP-082892eb480e45dea6d4b9fcc0491034\`, logical Research conversation \`chatgpt-research-onhour-enterprise-math-20260923\`. Status: **AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Exact source and typing

* Historical comparison: \`awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.
* True producer: \`src/enterprise_math/tetrahedral_endpoint_sum.py\` blob \`9f5098f7ba6995340406b39125b735cdba71fd4f\`; source lines 49–64 define signless K4 endpoint sum, three matching sums and star parity; 88–96 define the residual code; 114–165 define quotient equivalence and exact recovery via an integer vertex lift.
* True importer and executed historical consumer: \`tests/test_tetrahedral_endpoint_sum.py\` blob \`d5cf7d4fa1405eca8245baa143334e282ee8fb26\`, lines 4–20 import the producer, 24–29 check endpoint-sum identity, 36–61 check exact decomposition/parity, 63–72 check sampled quotient preservation. Its existing tests use these **derived K4 edge-lattice operations**, not a native-X6 BRC computation.
* Frozen native scientific source: \`59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` (six primitive signed coordinates; shortest-word count \`B(z)=||z||_1!/∏|z_i|!\`); P000 unchanged.
* The six labeled K4 **edge** entries are compared with the native \`Z^6\` endpoint formula only under an expressly selected bijection of the six labels. This is an algebraic type-check/reference comparison, not an assertion that the K4 carrier edges physically are the six native directions.

## Input objects and claim

Index \`E=Z^6\` in edge order \`(12,13,14,23,24,34)\`, \`V=Z^4\` in base-vertex order \`(1,2,3,4)\`. Let \`E_0={x:Σ_e x_e=0}\` and \`V_0={v:Σ_i v_i=0}\`. The frozen source's signless incidence map is

\[
\delta(v)=(v_1+v_2,v_1+v_3,v_1+v_4,v_2+v_3,v_2+v_4,v_3+v_4).
\]

For \`x=(a,b,c,d,e,f)\in E_0\`, its derived \`A_2 × C_2\` residual code is

\[
C(x)=(a+f,\ b+e,\ (a+b+c)\bmod 2).
\]

The existing source already identifies \`E_0/\delta(V_0)\` via this code and proves exact reconstruction with an additional zero-total vertex lift. **The quotient classification itself is not new here.**

Define three explicitly typed **native comparator** readouts for any six-component signed integer tuple \`x\`:

\[
L(x)=\sum_i|x_i|,\quad Q(x)=\sum_i x_i^2,\quad
B(x)=\frac{L(x)!}{\prod_i |x_i|!}.
\]

**New exact source-to-consumer nonfactorization proposition.** There is no function \`F\` on the triple \`(C(x),L(x),Q(x))\` satisfying \`B(x)=F(C(x),L(x),Q(x))\` for every \`x\in E_0\` under the stated axis-label comparison. In particular the K4 residual code alone does not determine native-X6 shortest ordered path multiplicity or squared spatial readout. Each zero-code fiber already contains an infinite sequence with unbounded \`L,Q,B\`.

## Complete algebraic proof and exact witness

For \`v\in V_0\` the sum of all six edge entries of \`\delta(v)\` is \`3Σ_i v_i=0\`. Each opposite-edge matching sum is \`Σ_i v_i=0\`. The first STAR sum is

\[
(v_1+v_2)+(v_1+v_3)+(v_1+v_4)=2v_1,
\]

hence is even. Therefore \`C(\delta(v))=(0,0,0)\`. Since the code is additive in its matching coordinates and the parity is additive modulo two, \`C(x+\delta(v))=C(x)\` for every \`x\in E_0\`. This is a source-defined gauge equivalence, not a physical displacement identification.

Now take two **exact input assignments**:

\[
\begin{aligned}
v_A&=(-3,0,0,3), &x_A=\delta(v_A)&=(-3,-3,0,0,3,3),\\
v_B&=(3,1,-2,-2), &x_B=\delta(v_B)&=(4,1,1,-1,-1,-4).
\end{aligned}
\]

Both have the **same residual code** \`C=(0,0,0)\`, the **same native-comparator shortest-event length** \`L=12\`, and the **same native-comparator quadratic length** \`Q=36\`. Nevertheless,

\[
\boxed{B(x_A)=\frac{12!}{(3!)^4}=369600,\qquad
B(x_B)=\frac{12!}{(4!)^2}=831600.}
\]

Their ratio is \`B(x_B)/B(x_A)=9/4\`. Therefore no factorization through \`(C,L,Q)\` exists. This is an unconditional mathematical counterexample for the **declared integer maps**; it neither changes P000 nor constitutes evidence that any existing production caller actually attempts such a factorization.

The zero-class family \`v_k=(k,-k,0,0)\`, \`k\ge0\`, yields

\[
x_k=(0,k,k,-k,-k,0),\ C(x_k)=0,\ 
L(x_k)=4k,\ Q(x_k)=4k^2,\ B(x_k)=\frac{(4k)!}{(k!)^4}.
\]

Its \`B\` values strictly increase: \`B(x_{k+1})/B(x_k)=\prod_{j=1}^4 (4k+j)/(k+1)^4>1\` for \`k\ge0\` (each numerator product is at least a ratio larger than 1; equivalently append four new labels to the existing balanced multinomial word). In particular \`B(x_k)\ge\binom{4k}{k}\to\infty\`. Hence one residual class has unbounded native-comparator count and no finite extra state alphabet can losslessly encode all its integer endpoints. An integer lift (or equally expressive unbounded information) is needed for full reconstruction.

Conversely, the **already existing** canonical decomposition supplies an exact safe repair: \`x=N(C(x))+\delta(v)\`, where the source's \`N\` is its normal form and the unique \`v\in V_0\` is recovered from the matching/parity-constrained difference. Retain \`(C,v)\` before applying any downstream native-comparator calculation. Source 124–165 and consumer 36–54 already preserve that lift; **no defect is asserted in this current call**.

## Independent integer executable certificate

Checker: \`research_checks/X6_UNIT170_K4_RESIDUAL_BRC_NONFACTORING_CHECK_20261120.py\` (actual SHA256 \`4299b9df0ed3329985e2710c72966b9df8055e789f59c8d425b1b298777ef896\`). Result: \`research_checks/X6_UNIT170_K4_RESIDUAL_BRC_NONFACTORING_RESULTS_20261120.json\` (actual SHA256 \`202e12b0c2c93c810d64ef4c1438a0400ef3f423d2a59fd734c265f2c5b9caf7\`).

Finite test enumerates all \`231\` zero-total vertex assignments \`v\in[-3,3]^4\`, all \`243\` zero-total edge input assignments \`x=(u_1,\dots,u_5,-Σu_i)\` with \`u_i\in[-1,1]\`, verifies **56,133** residual-invariance pairs, and checks **243** explicit unique canonical decompositions. It identifies **one** \`(C,L,Q)\` cell with multiple \`B\` values within **this declared bounded vertex sample**; the displayed witness matches it. Seven initial instances of the infinite family were exact-checked. All failed-condition counts: zero. Normal, \`python -O\` and \`python -OO\` emitted identical JSON bytes, using \`RuntimeError\` rather than disabled assertions. A finite search is not being promoted to a proof of universal minimal collision size; the universal nonfactorization and infinite family follow algebraically above. The original R063 benchmark, frozen module tests and any unrelated experiment were not rerun.

## Mother-objective disposition

This frozen historical **producer-to-actual-test-consumer** chain is certified **PRESERVE_DERIVED_K4_RESIDUAL_WITH_LIFT**. The residual code and torsion retain their existing genuine mathematics; no correct code is deleted. A downstream caller that tries to compute native signed X6 BRC from \`(C,L,Q)\` alone would have a provably invalid type transformation, witnessed above. No verified current producer/consumer observed here does this. This source does **not** establish LP011's alleged wrong native-axis argmax or LP019's alleged subtraction of positive N-BRC masses: exact offending \`commit:path:line\` for those allegations remains \`UNRESOLVED_PROVENANCE\`. Full 28-LP audit, old Units149–152 native semantic association and independent Driver review/Result remain open. Preserve Unit169 as prior authored frontier and its certified original Source PROGRESS; preserve the completed native R063 benchmark without replay.

Result scope: source-pinned derived carrier quotient plus conditional signed-six-axis BRC interface check. **AUTHOR_PROVED, FINITE_EXACT_EXECUTED; no independent review, no mathematical admission and no promotion of any K4 quotient to native X6 identity.**
