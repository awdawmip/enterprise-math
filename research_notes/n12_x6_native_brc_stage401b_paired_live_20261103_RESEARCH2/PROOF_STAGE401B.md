# Stage401-B: exact future quotient for live synchronized BRC paths

Date 2026-11-03. Author-side complete proof plus exact verification; UNREVIEWED / NOT_ADMITTED. Parent Stage400-B at a6a7fb82c079ea00f6e87922872f9170687cc869, Draft PR #1736. Frozen scientific inputs: EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Normative rules read separately from main. No new P000/worldview assertion.

## Model

Let A={+E1,-E1,...,+E6,-E6} be all twelve signed native X6 primitive-axis directions. Two aligned, source-tagged histories P=(p1,...,pm),Q=(q1,...,qm) form W=((p1,q1),...,(pm,qm)) over B=A×A, with |B|=144. The synchronization index is not an extra spatial dimension. The current observer includes each source's length m, all six displacement coordinates relative to a Cell, full directed neighbor histogram J_P,J_Q, all twenty triple-coordinate readouts, and the cross-source *live* equality count K(W)=sum_i 1[p_i=q_i]. It can also include fixed-direction native BRC endpoint count N_m(z), fixed positive rational BRC endpoint masses, and separately nonzero per-direction multiplicative signed trace. Such endpoint observables are determined by length/endpoints and source parameters; signed trace is determined by direction multiplicities and does not represent positive mass.

Future language consists of PAIRED_APPEND(x) for arbitrary x=(a,b)∈B; and PAIRED_CANCEL deleting the last two aligned paired positions, enabled iff m>=2 and W_(m-1)=inverse(W_m), where inverse(a,b)=(-a,-b). Cumulative cancellations <=C, arbitrary finite append count. Observe operation enabledness, both source marginals, and K anew after *each* operation. No asynchronous or independent-source CANCEL, order-dependent branch mass, physical heartbeat trajectory, or unproved native Cell-address conversion is assumed.

Let pred(W) delete the last paired position, with pred(empty)=empty. Let G_0(W)=last(W), or EMPTY when W is empty. Define recursively, for c>=1,

G_c(W)=(G_(c-1)(W), G_(c-1)(pred(W)), Z_c(W)),

Z_c(W)=G_(c-1)(pred²(W)) iff the two final paired labels are inverse; otherwise Z_c(W)=ABSENT, a separate marker from EMPTY.

## Theorem 401.1 — exact minimal live-paired memory

For any nonnegative integer C, and any two finite W,V in the *same present complete-observation fiber*, they are indistinguishable under every common finite sequence of allowed future actions with <=C paired CANCEL operations (including intermediate observations/enabledness) if and only if G_C(W)=G_C(V). Therefore for any fixed observation fiber F, its exact minimum number of additional deterministic memory classes is

q_C(F)=#{G_C(W): W∈F},

and when F is finite its fixed-length binary cost is ceil(log2(q_C(F))). This applies over all 144 paired labels and arbitrary finite path lengths, not only the verification alphabet.

**Sufficiency proof.** PAIRED_APPEND(x) updates each marginal endpoint by its signed native step and its directed neighbor histogram by precisely the edge (last_source,x_source); live K increases by 1[x_P=x_Q]. G_c contains the last paired letter, so these are known. Further, G_c(Wx) is computed from G_c(W) and x by induction on c: its first component is the lower-order append update on G_(c-1)(W), its second is G_(c-1)(W), and (only if the newly appended pair is inverse to the previous last pair) the third is G_(c-1)(pred(W)). Those components are already in G_c(W). For enabled PAIRED_CANCEL, G_c contains the two last paired labels and, if m>=3, the third-last paired label. Those determine the removal of the final two source-directed edges and two native spatial displacements, plus live K decrement by the two deleted equality indicators. The exact post-operation G_(c-1)(pred²(W)) is its third component; the remaining cancel budget is c-1. BRC endpoint and nonzero multiplicative per-direction signed trace values follow from the updated sufficient marginal data. Induction on the entire future action sequence establishes the claimed congruence.

**Necessity proof.** Induct on C. For C=0, if last paired labels differ, appending one common paired label creates different directed marginal edges in at least one source; this distinguishes under the current complete observation. For C>0, suppose G_C differ. If first components G_(C-1)(W) differ, induction distinguishes with <=C-1 cancels. Otherwise the last paired letters are identical. If second components G_(C-1)(pred(W)) differ, append the inverse of the shared last paired letter, then CANCEL, in both histories: this deletes appended and original last pairs and leaves pred(W), pred(V) with C-1 cancel budget, distinguishable by induction. If third components differ, either exactly one has an enabled immediate CANCEL (distinguished by enabledness), or both have it enabled: direct CANCEL leaves pred²(W),pred²(V) with distinct G_(C-1), distinguished by induction. The three cases exhaust G_C differences and produce finite distinguishing action sequences. QED.

This sharpness is specific to paired CANCEL. Earlier single-source S_C signatures remain sufficient under this paired language but are not necessarily minimal. It does not alter Stage400's independently allowed source actions/frozen K analysis.

## Theorem 401.2 — strict C=1 compression and exact C=2 separation

Let A=+E1, B=-E1, D=+E3, and take P=(A,A,B,A,B), P'=(A,B,A,A,B), Q=(D,D,D,D,D). Both paired histories (P,Q),(P',Q) have precisely the same current observable: each P has endpoint +E1, multiplicities three A and two B, directed histogram A→A:1, A→B:2, B→A:1; Q identical with endpoint 5E3; K=0. All twenty three-coordinate readouts, any nonzero per-direction multiplicative trace, and fixed-source positive/unweighted BRC endpoint readings agree. Using the full twelve-direction integer BRC recurrence gives N_5(+E1)=1660 and N_5(5E3)=1.

The *independent-source* S_1(P), S_1(P') differ because both end in inverse pair A,B but have third-from-last letter B versus A. However the last two **paired** letters are not inverse (Q ends D,D), hence G_1(P,Q)=G_1(P',Q). They require **one joint class** rather than two source-product classes on this two-history subfiber when C=1. For C=2 the same histories are distinguishable: APPEND(A,-D), CANCEL; APPEND(B,-D), CANCEL. Each CANCEL is enabled in both histories and removes one original paired final position. The resulting P histories are (A,A,B) versus (A,B,A), which have different directed neighbor histograms (A→A,A→B versus A→B,B→A); Q ends (D,D,D). Thus G_2 differs. No extrapolation to physically measured processes is made.

## Reproduction and next question

The attached Node JavaScript verifier uses exact BigInt for the full 12-native-step BRC recurrence, plus an independently built finite **future-behavior tree** with live K and both APPEND/CANCEL actions. It compares G_c equivalence and independently generated future semantics for c=0,1,2, all paired words of length <=4, and two four-letter subalphabets: shared ±E1/±E1 and disjoint ±E1/±E3. It explores up to three paired APPENDs and two cancels and checks both directions of equivalence on each tested current fiber; stdout is stored beside the source. A second Python standard-library verifier (executed twice locally with identical stdout) additionally explored all words through length five with at most two future appends and checked the explicit witness. Infinite-length assertions follow the mathematical induction, not finite sampling.

Next Stage402-B: extend Stage400's exact coupled-source edge-count transfer to compute class multiplicities D_C(K,g) of joint G_C signatures without full word-pair enumeration, particularly C=2 and nonzero K. Account for J formation, 288 counters and exact integer output bit costs; compare with independent source S_C products. Preserve immutable scientific pins and no-CLAIM/NOT_ADMITTED boundaries.