# R281 — Multi-output Port visibility and p-adic cancellation of positive feedback

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED**.
Science input remains pinned to \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Immediate frontier: R280, \`33fcdc666acd935b276e3b0f50789c2f3301193f\`.
Foundation: project P000, ACTIVE Heartbeat World and residual-fidelity / joint-relation constraints.
Typed scope: a finite, stable, nonnegative-rational **BRC labeled visible-Port** matrix with row sums < 1, named additive edges, and explicitly declared output Port pairs. The ambient P000 six-axis ontology is unchanged. Ordinary resolvent algebra is used only for this typed auxiliary Port subsystem; this note claims no unproved transfer from the R269 auxiliary source classes to native X6 evolution.

## 1. Multi-output theorem and minimal appearance degree

Let \`W in Q_>=0^(n x n)\` have strict row sums < 1 and set \`S=(I-W)^-1\`. Fix \`m\` distinct **named edit labels**, whose endpoints may coincide, \`e_i=(u_i,v_i)\`, and allowed nonnegative rational weights \`x_i\` for which \`W(x)=W+sum_i x_i e_(u_i)e_(v_i)^T\` remains stable. Declare a finite nonempty family \`O\` of readout pairs \`(a,b)\`. Their observations are \`F_ab(x)=[I-W(x)]^-1_(a,b)\`.

Construct one edit-transfer directed graph \`H\` on the \`m\` labels:
\`i -> j\` iff \`S_(v_i,u_j)>0\`.
For each declared \`(a,b)\`, define its starting labels \`I_ab={i:S_(a,u_i)>0}\` and ending labels \`T_ab={i:S_(v_i,b)>0}\`. Let \`dist(X,i)\` and \`dist(i,Y)\` denote minimum numbers of graph arcs from a vertex in \`X\` to \`i\` and from \`i\` to a vertex in \`Y\`, respectively; unreachable distances are infinite.

**Theorem R281-A.** In a neighborhood of zero, the exact expansion is
\`\`\`
F_ab(x) = S_ab + sum_(d>=1) sum_(i_1,...,i_d)
 S_(a,u_i1) [prod_(j=1 to d-1) S_(v_ij,u_i(j+1))]
 S_(v_id,b) x_i1...x_id.
\`\`\`
All displayed word weights are nonnegative rational. Therefore a label \`i\` affects the full rational function \`F_ab\` iff it lies on an initial-to-terminal path in \`H\`. Its *exact first total degree of appearance* is
\`\`\`
d_ab(i) = dist(I_ab,i) + 1 + dist(i,T_ab)
\`\`\`
with infinity for an absent path. The earliest appearance among the declared observers is
\`d_O(i)=min_((a,b) in O) d_ab(i)\`.
A label may be removed from this **declared multi-output observation interface** exactly when \`d_O(i)=infinity\`; in that case every declared \`F_ab\` is rational-function-independent of its edit coordinate for every admissible update vector. If relevant, \`d_O(i) <= 2m-1\`. The first nonconstant term among all outputs (if any) appears at degree at most \`m\`.

The two-way distance formula sharpens the individual-edge BFS statement of R280; the union across declared readouts gives a multi-output exact safe-deletion certificate. No information about an unlisted readout, Port provenance, signed/phase component, or external BRC operation is deleted.

**Proof.** The exact resolvent identity around \`x=0\` gives the word expansion. \`S=sum_{k>=0}W^k\` has nonnegative entries and its entry is positive exactly when there is a baseline directed path. Thus a word contributes positively precisely when it traces a path from \`I_ab\` to \`T_ab\` in \`H\`. An initial-terminal path containing \`i\` has minimum vertex count equal to the two shortest arc distances plus one: concatenate shortest portions, and conversely split any containing path at an occurrence of \`i\`. Because positive terms cannot cancel over the rationals, the corresponding monomial coefficient is positive; any smaller total degree has none. If the label occurs in no such path, all Taylor coefficients involving it vanish, hence the rational function is independent of that variable everywhere it is defined. In a finite graph of \`m\` vertices, either shortest portion can use at most \`m-1\` arcs, so \`d_ab(i) <= 2m-1\`. The shortest unrestricted initial-terminal path is simple, hence uses at most \`m\` vertices. Taking finite unions across outputs proves the result. QED.

**Explicit observer-scope witness.** With four Ports, baseline edges \`0->1=1/4\` and \`2->0=1/4\`, and edits \`A:1->2\`, \`B:3->3\`, readout \`(0,0)\` depends on A and not B, while readout \`(3,3)\` depends on B and not A. The singleton observation quotient for either one is therefore unsafe for the pair.

## 2. Prime-adic coefficient certificate (exact arithmetic, not a cancellation assumption)

For any prime \`p\`, a fixed output \`(a,b)\` and nonzero multi-index \`nu\`, let \`C_(ab,nu)\` be the coefficient of \`x^nu\` in the rational Taylor expansion. It is a **finite sum** over all edit-label words having multiplicities \`nu\`:
\`C_(ab,nu) = sum_(word has counts nu) t_word\`, with \`t_word >= 0\` rational.

**Theorem R281-B.** If at least one \`t_word\` is nonzero, let \`h=min_word v_p(t_word)\` over those nonzero words. Then
\`\`\`
v_p(C_(ab,nu)) >= h,
v_p(C_(ab,nu)) = h  iff
 sum_word (p^(-h) t_word mod p) != 0 in F_p.
\`\`\`
Every \`p^(-h)t_word\` in the residue test is \`p\`-integral. If the sum vanishes modulo \`p\`, the valuation is strictly greater and is obtained by exact rational addition or further digit checking. In particular, positive rational feedback does not imply **non-cancellation of modular leading residues**. Ordinary real visibility is structural; visibility at a declared mod-\`p^k\` readout also depends on valuations and residue sums.

**Proof.** Factor \`p^h\` from the finite rational sum and reduce the resulting \`p\`-integral terms modulo the maximal ideal \`p Z_(p)\`. The resulting sum is a unit exactly when its residue is nonzero. Positivity only guarantees the rational coefficient is nonzero; it does not guarantee its valuation equals the minimum term valuation. QED.

**Pure labeled-word cancellation witness.** On one Port with baseline \`W=0\` and 13 separately named editable self-loop edges,
\`F(x)=1/(1-sum_(i=1)^13 x_i)\`.
Every ordered word of length 13 containing each name exactly once contributes 1; the square-free monomial coefficient is \`13!=6227020800\`, with \`v_13(13!)=1\`, although every word has valuation zero. This example stays strictly stable for sufficiently small positive rational edits.

## 3. Two explicit mod-13 witnesses

**Positive baseline paths can lose their first mod-13 digit.** On Ports 0,1,2 take baseline \`W_(0,1)=1/16\`, \`W_(0,2)=7/8\`, \`W_(2,1)=6/7\`, other weights zero. All row sums are <1, and
\`\`\`
S_(0,1)=1/16 + (7/8)(6/7) = 1/16 + 12/16 = 13/16.
\`\`\`
The two positive baseline-path contributions are both 13-adic units, while their sum has \`v_13=1\`. For the named edit \`1->0\` of weight \`x\`, \`F_00(x)=1/(1-(13/16)x)\`. At \`x=1/4\`, the exact observation is \`64/51\`. This demonstrates a modular-leading-residue cancellation that an untyped Boolean reachability projection cannot predict.

**Real first visibility order need not equal mod-13 first visibility order.** On Ports 0,1,2,3 take sole baseline edge \`0->1=13/16\`; named edits are \`A:1->0\`, \`B:0->2\`, \`C:2->0\`, with weights \`x,y,z\`. The exact scalar response is
\`\`\`
F_00(x,y,z) = 1 / (1 - (13/16)x - yz).
\`\`\`
Over the positive rationals its first nonconstant coefficient is \`[x]F=13/16\`, so the structural degree is **1**. Over the 13-adic integers with \`16\` invertible, the reduced formal response is
\`\`\`
F_00(x,y,z) mod 13 = 1/(1-yz),
\`\`\`
whose first nonconstant term has degree **2**, coefficient \`[yz]F=1\`.
At \`x=y=z=1/16\`, strict row sums remain <1, the exact response is \`128/121\`, and its residue is 6 modulo 13. With only A added at \`x=1/16\`, the response is \`256/243\`, residue 1 modulo 13. Hence the 2-cycle is invisible to the first-order mod-13 test of A but changes the future mod-13 readout.

The statements above concern the indicated exact rational observer and the finite-resolution mod-13 comparison; no source/Port history is assumed equal merely from those residues.

## 4. Algorithm, verification and next unit

For fixed declared outputs, compute the exact rational Green matrix once, build \`H\`, and run directed and reverse BFS for each output. The resulting two-sided distances determine all first-appearance degrees and exact scoped irrelevance, without enumerating all edit words. For a requested finite multi-index coefficient, enumerate its finite labeled words and sum them exactly, then evaluate \`v_p\`; the simple residue-minimum criterion detects whether the lowest valuation survives. Integer/rational bit complexity, original-state construction costs and precision requirements belong to any subsequent end-to-end algorithmic claim.

The independent \`R281_multioutput_adic_checker.py\` uses only Python standard-library \`Fraction\` arithmetic and exact Gauss-Jordan inversion. Its reproducible report \`R281_verification.json\` records PASS for **1,036 ordered-word/output checks** through degree 5 in three multi-output model families, direct rational inverse checks, the two mod-13 witness values, and \`13!\` valuation. The universal theorems are proven algebraically above; the finite checks cover the specified examples only.

**Remaining question.** Characterize the least mod-\`p^k\` sufficient *multi-output* residual carrier for a specified edge-edit alphabet: whether coefficient residues through a computable finite depth suffice under bounded edit compositions, and which denominators/resonance depths must be stored for future unbounded edits. Investigate transfer of the resulting typed Port carrier to the R269 auxiliary source-label classes only after constructing an explicit provenance-preserving map.

This note is independent portable research. Native activity association, formal Task/CLAIM, Result and independent review require separate actual authorization and records.