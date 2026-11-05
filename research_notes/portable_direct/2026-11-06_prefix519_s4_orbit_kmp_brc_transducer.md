# PREFIX-519 — Exact S4-orbit KMP–BRC transducer and a minimal frame-change collision

Date: 2026-11-06 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Connection: independent author-side continuation of `RS-X6-NATIVE-ROTATION-DYNAMICS`; no authenticated CLAIM/RA is asserted in this publication. Frozen scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Previous frontier: PREFIX-515 through PREFIX-518, especially `research_notes/portable_direct/2026-11-05_prefix518_four_star_switch_covariant_brc_lift.md` at `a51bb9bf8071f90d95e0e0ffa956dde8f27901fa`.

## Research question and precise symbolic carrier

PREFIX-518 constructs a four-STAR common-pivot *candidate* switch relation and an S4 action on the six signed native axes. Which finite observer can compute the KMP/source output after **any** of these 24 atlas relabelings, and continue by concatenation without replaying all primitive steps?

Take the signed-X6 alphabet `Sigma={+L_i,-L_i : 1<=i<=6}` as primitive Cell-to-Cell steps in one chosen relative chart. The four STAR names `A,B,C,D` are K4 vertices with edge labels `L1=AB,L2=CD,L3=AC,L4=BD,L5=BC,L6=AD`. The 24 permutations of the vertices induce faithful signed-axis permutations `R_h` (sign unchanged).

Use the **declared extension** of the existing PREFIX-515 five-axis color observer: `+L1 -> 0 (a)`, `-L1 -> 4 (A)`, `+L2 -> 1 (b)`, `-L2 -> 2 (B)`, both signs of `L3 -> 3 (c/C)`, and both signs of `L4,L5,L6 -> 4` (filler). This is an observer convention for testing KMP transport; the sixth-axis filler is an explicit choice, not a new native axiom. Source letters are B for either sign of L2, C for either sign of L3, and N otherwise. The gates are the three-color patterns `aab=(0,0,1)` and `aba=(0,1,0)` with a four-state prefix/suffix KMP machine `Q={0,1,2,3}` (including its full-match state).

For gate g and atlas permutation h, let `F_{h,g}(w):Q->Q` be the complete KMP state-transition map from arbitrary initial state when reading the colors of `R_h(w)`. Let `B_{h,g}(w)=F_{h,g}(rev(w))`; let `f_h(w),ell_h(w)` be the first/last source among B/C in that relabeled word (or N). Define the **orbit transducer**

`K(w)=[ (F_{h,aab},B_{h,aab},F_{h,aba},B_{h,aba},f_h,ell_h) : h in S4 ]`.

The full observer `Xi(w)=(n,y,p,A,K(w))` additionally retains exact signed displacement `y in Z^6`, six-axis BRC pair count `p_i=(N_i-|y_i|)/2`, and the 15-coordinate antisymmetric area `A=sum_{r<t}s_r wedge s_t`. Native branch labels/ordered midpoint history remain available in the original source when indexed history questions are posed.

## Theorem 1 — finite exact concatenation and atlas covariance

For **every** finite signed native word u,v, each gate g, and each h in S4, the observer Xi(uv) can be computed from Xi(u),Xi(v) without scanning either word. Write `F^h_u=F_{h,g}(u)`, `B^h_u=B_{h,g}(u)`. Then

`F^h_{uv}=F^h_v o F^h_u`, `B^h_{uv}=B^h_u o B^h_v`.

`f_h(uv)=first_non_N(f_h(u),f_h(v))` and `ell_h(uv)=first_non_N(ell_h(v),ell_h(u))`.

The BRC fields obey `y(uv)=y(u)+y(v)` and

`p_i(uv)=p_i(u)+p_i(v)+(|y_i(u)|+|y_i(v)|-|y_i(u)+y_i(v)|)/2`.

Area obeys `A(uv)=A(u)+A(v)+y(u) wedge y(v)`. Formal step-order reversal swaps F/B and first/last (while changing the sign of A and retaining y,p). For any atlas permutation k acting on the signed native word, the complete orbit is equivariant:

`F_{h,g}(R_k w)=F_{h o k,g}(w)` and likewise for `B`, `f`, `ell`.

Under R_k, the six y/p coordinates permute and A is transported by the induced exterior-square action. The 24 atlas labels are closed under `h o k`, so the claimed operations descend exactly to Xi. For fixed two gates and fixed S4, combining the finite transition maps takes a constant number of state-map lookups (24*2*4-scale), plus the established six-axis BRC and area updates. Integer bit sizes of n,y,p,A still depend on path length; this is **constant transition-operation count**, not constant bit-cost.

**Proof.** A word induces a deterministic function Q->Q; concatenation is function composition. The reversed concatenation identity `rev(uv)=rev(v)rev(u)` supplies the reverse formula. Source selectors follow earliest/latest non-N occurrence. The pair-count and antisymmetric area formulas follow by partitioning primitive counts and ordered pairs across the concatenation boundary, as already established in PREFIX-515/516. Finally, `R_h(R_k(w))=R_{h o k}(w)` letter by letter, including the corresponding source tags, establishing covariance. The group is closed; all fields are exact. These identities are valid for arbitrary finite lengths.

## Theorem 2 — shortest frame-change information-loss witness for the fixed-chart observer

Take `w1=dD=(+L4,-L4)` and `w2=Dd=(-L4,+L4)`. Both have `n=2`, `y=(0,0,0,0,0,0)`, `p=(0,0,0,1,0,0)` and all 15 area coordinates zero. In the original PREFIX-515 fixed-color observer every letter has filler color 4 and source N, so **the entire** `(n,y,p,A,F_g,B_g,f,ell)` agrees for the two words for both gates.

Consider the K4 vertex permutation `(A,B,C,D) -> (D,A,C,B)`, represented by `[3,0,2,1]`. It sends `L4=BD` to `L1=AB`. The transformed words are colored `aA` and `Aa`, respectively. From initial KMP state 0, `aA` ends in state 0, while `Aa` ends in state 1 for **both** `aab` and `aba`. Thus no exact operator on the original fixed-chart `Gamma^A` alone can implement every S4 atlas recoloring: equal inputs would require different outputs.

This is a **minimum-length collision among arbitrary native signed words**, because at length zero there is one word and at length one the signed displacement y uniquely identifies the primitive letter. The orbit observer repairs this specific descent failure by recording both complete transition functions in every relabeling.

For an additional two-distinct-axis witness with `p=0`, the palindromic words `deed` and `edde` have identical original y,p,A and fixed-color KMP functions, but the same permutation maps L4 to L1 and L5 to L3, producing color words `acca` and `caac`. Their terminal KMP states are 1 and 0. This independently shows an area observer is not enough to reconstruct arbitrary frame-sensitive word matching.

## Executed finite certificate and scope

Run `node research_notes/portable_direct/prefix519_s4_kmp_brc_certificate.js`. This executable uses exact signed native axis vectors, integer BRC cancellation counts, wedge areas and direct four-state KMP transition tables. The actual execution reports `ALL_CHECKS_PASS`: 1,885 signed words of lengths 0 through 3; 353,712 transition-composition checks; 90,480 reversal checks; 180,864 S4 covariance checks on 157 words of lengths 0 through 2; 7,369 BRC/area split checks; and both explicit collisions. The accompanying JSON is the captured stdout from that execution. Finite enumeration validates the implementation; Theorems 1–2 follow from the algebraic arguments and explicit words.

The KMP orbit is a constructed finite observer for atlas relabeling, reversal and concatenation. It may be combined with the PREFIX-518 phase/frame itinerary and the PREFIX-517 ordered branch string when the requested observation includes indexed intermediate Cells. It does not select a physical STAR-switch motion.

## Next unit (PREFIX-520)

Build the chart-dependent, switch-by-switch color transducer for the actual 48 directed phase states / six labeled local moves of the PREFIX-518 *candidate* switch relation. Determine whether the whole 24-frame orbit can be quotiented on this restricted language by proving a future-operation-safe fiber factorization, or exhibit the shortest restricted-language counterexample. Compare retained state size and O(1) transition composition against the full provenance carrier; preserve the frozen native physical-rotation mother question.

Sources: frozen `p000_reality_foundation.json` and `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` at `f42f2906d77f24085c123f3ccfe9667d41caa96d`; current `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`; PREFIX-515 through PREFIX-518. Gateway task-state/identity read was attempted on 2026-11-06 and returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`, so current native owner/CLAIM and RA registration are not asserted here.
