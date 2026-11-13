# R762L — Exact classification of S6-covariant signed triadic admission and the hidden-polarity observer obstruction

**Research date:** 2026-11-13 (Asia/Shanghai). **Status:** author-side exact proof and finite exhaustive verification; not independently reviewed. **Parent:** \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. **Frozen scientific input:** \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Reuse R762K (#2297) without recasting candidate support as a native physical force event.

## Definitions and precise hypothesis

Choose one Cell \`c\` of the signed X6 affine spatial torsor. A signed primitive port is \`(i,epsilon)\` for \`i in {0,...,5}\`, \`epsilon in {+1,-1}\`, denoting \`c -> c + epsilon*e_i\`. Let \`T\` be the 160 unordered sets of three ports on **distinct** axes. Let \`T_hat\` contain both cyclic orientations of each set, hence 320 elements. The already established S6 axis-name-permutation skeleton acts on axis indices and preserves port signs. It is only a finite skeleton, not a declaration of the full native rotation group.

Study boolean candidate admission laws \`A:T_hat -> {0,1}\` with the *specific* input restriction that admission depends solely on the signed three-port support and its cyclic orientation, and with the invariance condition \`A(sigma*x)=A(x)\` for every \`sigma in S6\`. No Cell field, timed source history, phase, context, signed amplitude, or native event-update state is an input. This is an explicit finite candidate-law class, **not** an assertion that P000 admits any such law or that a 3-armed Cell star is a spatial closed walk.

For \`x\`, let \`k(x)\` be the number of negative signed ports. An unordered visible pair \`v\` has two distinct axes; let \`r(v)\` denote its negative count in \`{0,1,2}\`. A labeled hidden arm and a cyclic orientation remain distinguishable candidates, with unit positive N-BRC incidence weight.

## Theorem 1: Exactly sixteen covariant candidate laws

**Claim.** Every such \`S6\`-invariant boolean law has the unique form
\[
A(T,\chi)=a_{k(T)},\qquad(a_0,a_1,a_2,a_3)\in\{0,1\}^{4}.
\]
Consequently there are exactly \(\boxed{16}\) such candidate admission laws.

**Proof.** By orbit–stabilizer, the \`S6\`-orbits on unsigned-orientation-free signed triples are exactly the four negative-sign-count classes \`k=0,1,2,3\`; their sizes are respectively 20,60,60,20. For each triple the pigeonhole principle selects two distinct same-sign ports. The S6 transposition exchanging precisely their axis indices fixes the unordered signed support and flips the cyclic orientation. Thus the two orientations of each fixed support belong to the same S6 orbit. Hence the oriented 320-element domain has just four S6 orbits, of sizes 40,120,120,40. An invariant boolean function is constant on each orbit, with one independent bit per orbit. Conversely, any four-bit choice defines an invariant function. QED.

In particular an invariant candidate law cannot admit only one of two opposite cyclic orientations for the *same* signed support without supplying an additional source/phase/field datum or breaking the stated S6 symmetry.

## Theorem 2: Exact fiber law of the visible two-port observer

For a fixed visible unordered signed pair \`v\`, consider oriented admitted incidences \`(T,chi,h)\` with \`T\{h}=v\`. Four unused axes times two possible signs times two orientations give 16 potential incidence branches. Define \`B_r^+\` and \`B_r^-\` as counts distinguished by positive or negative **hidden-port sign**. Then for every visible pair with \`r\` negative signs,
\[
\boxed{B_r^+=8a_r,\quad B_r^-=8a_{r+1},\quad B_r=8(a_r+a_{r+1}).}
\]
There are 15,30,15 visible pairs of negative counts 0,1,2, respectively. Each formula is exact for all 16 candidate laws.

**Proof.** For each of the four remaining axes, a positive hidden port yields signed triple count \`r\` and two orientations, hence \`4*2*a_r=8a_r\` branches. A negative hidden port yields signed triple count \`r+1\` and likewise \`8a_{r+1}\`. The groups are disjoint and exhaust the 16 candidates. QED.

## Theorem 3: Sharp ambiguity of total-count-only inference

Let \`F(a)=(B_0,B_1,B_2)\`, the three total candidate branch-count readouts without hidden-port polarity. Exactly 15 distinct \`F\` values occur among the 16 admission laws. The sole collision is
\[
\boxed{a=(1,0,1,0),\quad a'=(0,1,0,1),\quad F(a)=F(a')=(8,8,8).}
\]
These two laws admit *disjoint* families of signed triad supports (even and odd negative-port parity).

**Proof.** Let \`b_r=B_r/8\`; the three equations \`a_r+a_{r+1}=b_r\` recursively determine \`a_1=b_0-a_0\`, \`a_2=b_1-b_0+a_0\`, \`a_3=b_2-b_1+b_0-a_0\`. Every fiber has at most two solutions, indexed by the initial bit \`a_0\`. If both \`a_0=0\` and \`a_0=1\` are legal binary solutions, comparing successive terms forces the alternating pair \`(0,1,0,1)\` and \`(1,0,1,0)\`, with \`b_0=b_1=b_2=1\`. They do indeed collide. Thus there is one double fiber, all other 14 signatures singleton. QED.

The refined observer \`(B_r^+,B_r^-)_{r=0}^2\` uniquely determines all four bits. For the unique ambiguous total-count fiber a **single hidden-polarity bit** distinguishes its two laws (e.g. \`B_0^+\` for visible \`(+E_1,+E_2)\`, which is 8 in the even law and 0 in the odd law). This is a sharp observer repair **only for law recovery under the stated candidate model**. It does not encode the 16 incident branches, full force history, event ordering, V29/V39 state, or native causality.

## Verification and foundations

The companion Python standard-library checker enumerates 160 signed supports, 320 oriented supports, 60 visible pairs, all 720 axis permutations, verifies the four orbit classes and every support's chirality-flipping stabilizer, checks all 16 predicates against each of the 60 visible pairs, and confirms 15 total signatures, the unique even/odd collision, and 16 refined signatures. This finite exhaustive verification is independent corroboration of the constructive proofs, not a claim about a native physical admission predicate.

P000 maintains six native spatial dimensions and a separate time dimension; pairwise Enterprise orthogonality is 120°; stable primitive nonzero events require triadic closure \`TRIADIC_CLOSURE_E\`. We have not asserted that all distinct-axis signed triples actually satisfy this event. Under the mandatory joint-observer-preservation contract, aggregating positive N-BRC branch mass must preserve hidden signs, labeled branches and source relations when a future observer needs them. Positive branch counts do not represent signed force cancellation. All conclusions above are at the candidate signed-cell-port-incidence level.

**Sources:** \`p000_reality_foundation.json\` and \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\`, \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` at frozen Source \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`; canonical Task publication \`TP2-8B7E13C5904A2D6F1142\` and pinned taskbook \`e01d91db2ad6e45fbfbb8360837cbf78a2bc5e11:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`; preceding candidate note R762K Draft PR #2297.

## Next discriminating scientific question

Introduce a concrete \`TRIADIC_CLOSURE_E\` incidence predicate on one signed Cell/Link/Port star and a source-typed post-event transition. Prove or disprove covariance under \`S6\`, determine whether the same event remains admissible when repeated, and compute its actual V29 PASS/TRANSFER and V39 frame consequences. If it depends on source order, hidden polarity or phase, provide the smallest additional typed state and recompute the admitted (rather than candidate) two-port fibers. A further exact problem: classify three-arm-to-two-arm observer laws in the presence of one retained source-cycle label; this may split the chirality orbit and should be checked before using R762L on physical events.
