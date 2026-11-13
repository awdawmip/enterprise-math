# R676｜V27—R675 类型化接口的四种等变桥、严格选择协变及对称平局残差

Date: 2026-11-10 (Asia/Shanghai)  
Status: AUTHOR-SIDE SYMBOLIC PROOF + FINITE INTEGER CHECK; DRIVER UNREVIEWED  
Parent Task: `RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW`  
Frozen science: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f (unchanged).  
Predecessors: R674@7e85d3b0fe3543e28c91894c174090102babb6db; R675@7beceb012a43d6c7c0ad005d8793bc96f4a38383.

## 1. Precise question and interfaces

R675 provides an order-two typed transformation of the seven-Cell double-loop model: spatial-axis cycle exchange, a V29 port relabeling `sigma=(0 2)`, a V17 active-label relabeling `g=(0 1)`, and S3 frame conjugation. These are different types of labels. V27 defines a four-field active-triad selector using the V23 code `c_H(S)` and an exact skew passage contrast, with score

`Phi_{H,u,Omega}(S,T) = u^T c_H(T) + c_H(S)^T Omega c_H(T)`.

Here `S,T` are allowed adjacent active triads, `H=(H_0,...,H_3)` is an *ordered set of four field sources*, `u=I-O` is a four-coordinate ingress/egress bias, and `Omega=M-M^T` is a skew four-coordinate passage contrast. V23's field-coordinate labels, V17 active-label names, V29 port names and native X6 axis names are distinct interfaces. In this note the V27 field-source relabeling is explicitly **chosen** as `tau=(0 1)`, and a proposed typed port-to-field bridge `beta` is analyzed. This is a new, stated coupling choice, not a hidden consequence of V27 or V29.

The observations are (i) exact allowed-neighbor score comparisons, (ii) argmax *set* and, where unique, the selected next triad, and (iii) the complete labeled two-loop event provenance and S3 holonomy. Time remains a separate ordered event parameter. The finite X6 graph remains embedded in the six native axes, not a plane.

## 2. Four exactly admissible port-to-field bridges

Let `P=F={0,1,2,3}` be two **typed copies** of a four-element set. The R675 V29 port action is `sigma_P=(0 2)`; choose `tau_F=(0 1)` for V27 field-source coordinate transport. An equivariant bijective interface `beta:P->F` must satisfy

`beta o sigma_P = tau_F o beta.`  (1)

**Theorem R676-A.** Exactly four bijections satisfy (1). Writing the tuple `(beta(0),beta(1),beta(2),beta(3))`, they are

`(0,2,1,3), (0,3,1,2), (1,2,0,3), (1,3,0,2).`

**Proof.** The unique nontrivial two-cycle of `sigma_P` is `{0,2}`; that of `tau_F` is `{0,1}`. The intertwining identity sends the first orbit to the second, with two orientation choices, while bijectively mapping the two fixed points `{1,3}` to `{2,3}`, with two choices. Hence there are `2!*2!=4` bridges, precisely the displayed tuples. Conversely each satisfies (1) pointwise. The identity interface fails: for the port basis vector `e_0`, `id(sigma_P e_0)=e_2` but `tau_F(id e_0)=e_1`. QED.

This is an interface classification for the declared pair of transpositions. It uses no claim that the physical four-field sources must be identified bijectively with four V29 ports.

## 3. Exact transport of the V23 code and V27 score

For a permutation `g` of six active-axis labels and any ordered source family `H=(H_i)`, write `(gH_i)(gS)=H_i(S)` (ordinary transported field evaluation). Choose an independent field-source name permutation `tau_F` and define

`H'_{tau_F(i)}=gH_i`.

Let `T_tau` be its four-coordinate permutation matrix. Then directly from the definition,

`c_{H'}(gS)=T_tau c_H(S)`.  (2)

This is the correctly typed use of V23's covariance: **the ordered sources are transported**. A fixed reference code `H` need not satisfy (2) after acting on `S` alone.

Transport the count data by

`I'=T_tau I,quad O'=T_tau O,quad M'=T_tau M T_tau^T`.

Consequently `u'=T_tau u`, `Omega'=T_tau Omega T_tau^T`; all entries of `I',O',M'` remain nonnegative integers. Using (2), permutation matrices' exact orthogonality gives

`Phi_{H',u',Omega'}(gS,gT)=Phi_{H,u,Omega}(S,T)`.  (3)

**Theorem R676-B (argmax covariance).** Assume the allowed neighboring-triad relation is transported by `g`. Then its maximizing-neighbor *set* transforms exactly by `g`. If a winner is unique, the deterministic selector obeys

`f_{H',u',Omega'}(gS)=g f_{H,u,Omega}(S).`  (4)

**Proof.** Equation (3) is equality of every corresponding candidate score. Since the neighbor sets are bijective under the assumed transport, both the maximum and all ties are preserved. A singleton maximum maps to a singleton maximum. QED.

V27's explicit witness is `M_{01}=M_{12}=M_{20}=1`, the other M entries zero, and `u=(-2,-4,-3,10)`. Its source reports a unique winner for all twenty triads with minimum winner/runner-up gap exactly 1. The transported witness under `tau_F=(0 1)` has `u'=(-4,-2,-3,10)` and permuted nonnegative counts, so equations (3)-(4) preserve **the same twenty unique-winner gaps** exactly. This conclusion reuses V27's reported exhaustive witness; this round independently checks the algebraic score identity over all `3^4*3^4=6561` signature pairs but does not rerun V27's 20-triad source generator.

The original numerical u is not invariant under `tau_F`: its first two entries are unequal. Therefore a proof of symmetry for this witness must transform the *bias context* together with sources and ports. The typed R675 map alone does not imply that a fixed-coefficient V27 selector respects it. Connecting (4) to the R675 two-loop autonomous update requires an explicitly selected `beta` and a source-to-Cell/edge dependency law transporting the scores.

## 4. Stabilizer obstruction and exact one-bit repair on a symmetric fork

Let an involution R act on states and on enabled labels, and let `E(RS)=R E(S)`. A deterministic selector f is equivariant if `f(RS)=R f(S)`.

**Theorem R676-C.** At any state `S_0=R S_0`, an equivariant deterministic selector requires an R-fixed element of `E(S_0)`. Conversely, for an arbitrary finite group action with nonempty equivariant enabled sets, a deterministic equivariant selector on all state orbits exists iff every state stabilizer fixes some enabled event.

**Proof.** For any stabilizer element g of S, equivariance gives `f(S)=f(gS)=g f(S)`. Conversely choose for each state orbit representative S a stabilizer-fixed enabled event e; define `f(gS)=ge`. If `gS=hS` then `h^{-1}g` fixes S and e, so f is well defined. QED.

If the R674 complete-block model additionally enables exactly `E(S_0)={A,B}` and R exchanges A,B at an R-fixed initial typed state, there is no equivariant deterministic single-event choice on that unaugmented state. A two-valued context `epsilon in {A,B}`, transformed by `epsilon->R epsilon`, repairs the fork: choose f(S,epsilon)=epsilon and retain epsilon under the block update. For this declared always-two-enabled block model the full deterministic update is equivariant under R675. Two distinct context states over the fixed base state are necessary and sufficient because the involution must exchange the two distinct chosen outputs. This is a **minimum binary symmetry-breaking context** for that fork, not a proof that V27's actual biased witness has a tie.

A positive rational branch law avoids selecting an unrecorded orientation. At the fixed two-choice fork, an equivariant probability kernel has uniquely `P(A)=P(B)=1/2`; more generally an invariant positive rational orbit-weight distribution is equivariant. Such a kernel preserves labeled branch provenance until the declared observer is applied.

## 5. Exact BRC-style two-step fiber

For the completed V29/V17 two-loop blocks, impose only the auxiliary rule that the second event must differ from the first. From a uniform symmetric first branch, the two histories `AB` and `BA` carry weights `1/2` each. Their complete V29 ledgers coincide but

`h(AB)=ab=(1,2,0),quad h(BA)=ba=(2,0,1)`.

The R675 frame action `h->c h c^{-1}`, `c=(1,0,2)`, exchanges these outputs. Thus the exact labeled positive-rational path histogram

`H=(1/2)[AB]+(1/2)[BA]`

is R-equivariant, while projection to the common additive V29 ledger has a two-element holonomy fiber. Its holonomy pushforward is the exact distribution `{ab:1/2,ba:1/2}`. These are finite typed combinatorial weights, not calibrated physical probabilities. This uses the BRC branch/provenance interface and demonstrates explicitly which information ledger-only compression erases.

## 6. Verification, limitations and next discriminating unit

`R676_VERIFY.py` checks the complete 24-permutation bridge search (exactly four solutions), the identity-bridge counterexample, nonnegative transported M, all 6561 V27 score identities over all four-coordinate ternary signature pairs, V27 witness bias transformation, exact S3 AB/BA holonomies and rational branch weights. All assertions passed under Python 3 standard-library integer and Fraction semantics; pass marker:
`R676_V27_TYPED_BRIDGE_SCORE_AND_SELECTOR_EXACT_PASS`.

Theorems A-C are symbolic for their declared domains. The 6561 tests cover all ternary four-tuples, including but not limited to the twenty V23 realizable codes; this finite verification does not by itself verify V27's claimed unique winners. No native heartbeat/residual or BRC-Shor numerical evolution was run; no pi/trigonometric or ordinary propagator is used. The documented branch histogram is an exact positive rational **combinatorial** BRC carrier under the specified loop-language scope. Research status: author checked, independent Driver review pending; no CLAIM/Result/Review authority asserted by this file.

**Next:** Construct the actual source-to-Cell incidence map `beta` (or prove the model needs a nonbijective field-source map), use local V29 event increments to generate `I-O`, then test (3) on the *actual* source-updated V27 selector at the eight-edge shared-Cell graph. Inspect whether a declared autonomous step produces a unique maximizer, an equivariant tie, or a symmetry-breaking context, and retain V39's `j` with `h` and the full ledger for future-language equivalence.

## Immutable sources

- V23 four-field active-triad code: `research_notes/X6_FOUR_FIELD_ACTIVE_TRIAD_CODE_V23_20260906.md` blob `67b94250e67d59c9581e17705d7c7214f939c35b`.
- V27 exact score, bias and unique-winner claim: `research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md` blob `c5a02e6727dfc1f70ae4594c3ee807d1760c0be9`.
- V29 event ledger: `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` blob `6849ebd3fc776fb7da3b46627376490aba3dad99`.
- V39 current plus S3 port: `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md` blob `8151d0b6a4b65225b93d858bbc8a5d7037bf9cef`.
- R675 source proof: `research_notes/r675_x6_typed_double_loop_covariance_20261110_emr3/R675_PROOF.zh-CN.md` @ `7beceb012a43d6c7c0ad005d8793bc96f4a38383`.
