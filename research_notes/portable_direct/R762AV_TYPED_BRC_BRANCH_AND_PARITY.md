# R762AV — Path support versus typed positive-BRC multiplicity in the stable V29/V17 selector

Date: 2026-11-15 (Asia/Shanghai). Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. Author-side research continuation from R762AU. Current native session initiated \`MCP-8b844b9054c94d40aaed0131426d3935\` (registration/CLAIM may still be pending; historical \`EM-X6-3050F6\` is a prior contributor, not used as the current authenticated identity). Scientific premise: frozen P000 at \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This work is a CONDITIONAL finite selector + P000 signed-coordinate consequence, author-checked, NOT_REVIEWED.

## Precise question

R762AU (PR #2451) proved that eight microstep masks of the V29 cumulative PASS ledger have seven different eventual V25 maximizer relations, yet their union graph has one six-state odd V17 cycle and every external state enters it within three decisions for n>=16. Does this imply that the BRC population of histories stops growing? A mask-erased state-path observer and a branch/mask-provenance observer yield sharply different exact answers.

### Definition of the declared conditional selector

Use the same twenty states \`S\subset\{0,1,2,3,4,5\}\`, \`|S|=3\`, and the same four perfect matchings as R762AU: (01)(23)(45), (02)(14)(35), (03)(15)(24), (04)(13)(25). Their four-component parity code \`c(S)\` is zero unless a state selects exactly one endpoint per matched pair; otherwise it is the product of endpoint signs. Every state has nine Johnson neighbors \`T\` with \`|S\cap T|=2\`.

The count-positive V29 ledger starts with \`Rin=(0,0,0,10)\`, \`Rout=(2,4,3,0)\`; its nonzero entries are \`M01=n+e0\`, \`M12=n+e1\`, \`M20=n+e2\`, with \`m=e0+2e1+4e2\` in 0..7. Define \`u=(M-M^T)1+Rin-Rout\`, \`Omega=M-M^T\` and
\[
\Phi(n,m;S,T)=u\cdot c(T)+c(S)^T\Omega c(T).
\]
The successor relation \`F_m(S)\` consists of ALL neighbor maximizers, retaining ties. For positive rational \`rho>1\`, these are also the maximizers of the typed positive Weighted-BRC branch weight \`rho^\Phi\`.

We study the **declared broad scheduling language**: at every active-triad decision the scheduler may select any mask m from 0..7, and each tied winner is a separate branch. This language is an upper envelope of possible event orderings, not a claim that real native PASS masks can be independently reset at every decision.

Two distinct carriers are used:
* **Mask-erased path support:** an unlabeled word of actual visited triad states \`(S0,S1,...,Sk)\`, counted once, even if several mask choices realize an edge.
* **Typed positive BRC branch word:** \`(S0;(m1,S0,S1);...;(mk,S{k-1},Sk))\`, where m is retained at each step and tied successor branches remain distinct. Use the free noncommutative \`N\`-semiring on typed labeled transitions, with branch sum and ordered concatenation. All atomic branch coefficients are 1. This semiring is the explicit BRC carrier used for this theorem; no pre-existing native physics/BRC SDK execution is claimed.

## Theorem AV1 — sharp three-step absorption and finite support

For all integer n>=16, let \`U(S)=union_{m=0}^7 F_m(S)\`. Then U has exactly 27 distinct directed edges. Its sole directed recurrent component is the six-cycle
\[
C:\quad 012\to123\to234\to034\to035\to025\to012.
\]
Each cycle vertex has only its one displayed outgoing edge. The other 14 states form an acyclic graph with ten vertices of exit height 1, three of height 2, and exactly one (145) of height 3. Thus **every** state path, for **every** arbitrary mask schedule, reaches C in at most three decisions, and this bound is sharp.

For source 145, the six mask-erased length-three paths terminate at the six different vertices of C, each precisely once. No later decision branches at the triad-state level. Hence for all integers k>=3 the number of distinct mask-erased length-k triad paths starting at 145 is exactly **6**. Their endpoint-count vector in cycle order C rotates by one slot per step and has period 6. Across all twenty starting states the maximum at and after k=3 is 6, attained only at 145.

**Proof.** The verifier recomputes the exact integer V25 scores, all 20x8 maximizing sets, and prints the full union adjacency list. The exterior height partition is obtained by the well-founded recurrence \`h(s)=1+max_{t in U(s)}h(t)\`, with h=0 on C. The recurrence succeeds without an exterior cycle and gives heights 1:10, 2:3, 3:1. The three branches from 145 are
\`145→014→013→{012,034}\`,
\`145→135→235→{035,123}\`,
\`145→245→024→{025,234}\`.
Thus precisely six length-three state paths exist, one to each cycle vertex. Uniqueness of the outgoing cycle edge then gives the k>=3 bijection between length-k and length-(k+1) state paths.

## Theorem AV2 — positive-BRC mask multiplicity persists exponentially

Keep the mask as a **branch label**. The weighted adjacency coefficient \`A(S,T)\` is the number of masks m for which \`T in F_m(S)\`. Ties count separately. The 27 support edges carry total coefficient 172 (160 ordinary mask/source pairs plus 12 additional tied choices). Every cycle edge has coefficient **8**: all eight masks choose the same unique successor there.

For source 145, the exact labeled branch-mass vector at k=3, in C order, is
\[
(192,\ 16,\ 448,\ 48,\ 64,\ 112).
\]
Its total is **880**. All labeled paths have entered C by k=3; every subsequent step has exactly eight mask extensions. Therefore
\[
\boxed{B_k(145)=880\,8^{\,k-3}\quad\text{for every integer }k\ge3.}
\]
The vector rotates cyclically and is multiplied by 8 each step. Among the twenty initial states, the maximal k=3 labeled total is 880, again attained only at 145.

**Proof.** The active edges of 145 carry multiplicities \`145→014:3\`, \`145→135:1\`, \`145→245:7\`. Their unique second-step edges each have multiplicity 8. The third-step edge multiplicities are \`013→012:8\`, \`013→034:2\`, \`235→035:8\`, \`235→123:2\`, \`024→025:2\`, \`024→234:8\`. Ordered positive semiring multiplication yields the six displayed integer coefficients and sum 880. On C there are eight distinct mask labels on the unique successor per step. Branch-wise extension is therefore an 8-to-1 map at every later step, proving the formula for all k>=3. The verifier checks the complete 20-state table.

**Corollary (observer-safe BRC distinction).** Under this exact future language, replacing the typed mask-word carrier by triad-state paths is an information-losing quotient: \`6\` paths versus \`880\` labeled histories already at length 3. Support has zero asymptotic path-count entropy, while positive label multiplicity has per-step logarithmic growth \`log 8\`. There is no signed cancellation: counts are nonnegative integer branch coefficients, and the result is not a physical rate. Under the conditional V17 shared-axis transport, one six-step recurrent loop exchanges a pair of internal frame slots, so the full frame returns after two loop turns (12 decisions); the six-step triad endpoint return alone omits that residual.

## Theorem AV3 — three primitive signed X6 spatial steps cannot close a Cell loop

In the **frozen P000 full signed native spatial torsor** \`X6\` over \`Z^6\`, any primitive coordinate step changes one coordinate by +1 or -1. For every ordered triple of primitive spatial steps \`v1,v2,v3 in {±e_i:i=1,...,6}\`,
\[
v_1+v_2+v_3\ne0.
\]
**Proof.** The homomorphism \`p(z)=sum_i z_i mod 2\` changes by 1 after each signed primitive step. Three steps yield odd parity and cannot return to the original Cell. The verifier checks the entire 12^3=1728 finite domain as an independent exact certificate. This is a sharp obstruction to interpreting a P000 three-force closure as *exactly three successive signed unit Cell translations that spatially return*. It does not obstruct a genuine three-force **internal incidence/port relation** at one Cell, nor a separately typed composite longer path. In particular it explains why the V17 triad-context six-cycle and the V29 internal PASS loop must not be silently identified with a three-hop native Cell-center triangle.

## Verification, source boundary, next problem

Run \`node R762AV_TYPED_BRC_PATH_VERIFY.js\` (Node standard library only). It emits \`R762AV_TYPED_BRC_PATH_EVIDENCE.json\` as an exact JSON object. It independently reconstructs all 20 triads and their V25 exact integer maximizers, checks the 27-edge support, 172 branch coefficients, exterior DAG/height partition, full 20-state 3-step population table, 145 six-vector, and 1728 three-step spatial combinations. The one-step n=16 versus n=17 comparison is a consistency check; the *all n>=16* reduction relies on R762AU's published exact affine-dominance theorem (PR #2451) rather than finite extrapolation. Proof is author-checked and awaits independent review.

The immutable P000 target remains to construct a genuinely admitted \`TRIADIC_CLOSURE_E\` signed-force Cell/Link/Port transition, bind its scheduler to real V29 PASS/TRANSFER and V17 internal frame transport, and identify its V39 based-loop observer. If that native event uses phase masks as a fixed sequential microstep protocol, recompute the *legally admitted* branch-language growth rather than importing the 8-free-mask count as a physical model.

Sources:
- Frozen foundation: \`enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` and \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\`.
- Exact task: \`research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`, publication \`TP2-8B7E13C5904A2D6F1142\`.
- V29: \`research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md\`, blob \`6849ebd3fc776fb7da3b46627376490aba3dad99\`.
- V17: \`research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md\`, blob \`42b810a8f82c504833027da17884cc4fb2943e5b\`.
- R762AU: \`enterprise-math@f42064096ba3014a63a8d75bbe9f4b7dcdaff447:research_notes/portable_direct/R762AU_PARTIAL_PASS_BRC_NONROBUSTNESS.md\`, blob \`a729f1b333e83a53b585feeb9b751f674f5a4308\`.
- Related independent frontier: PR #2447 (ten exact V29 score probes), not re-proved here.
