# R681｜V17 有序槽位在原子 PASS 事件时间中的独立 BRC 残差

Date: 2026-11-10 Asia/Shanghai. Mother task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW, publication TP2-47D65B35A7D48082EFBB. Frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Continuing author-side R680@151d820a1c776fe4b1401ab0a23b1d0867c13883 (PR #1921); independent Driver review has not been established. Model-internal finite exact claim; no physical calibration or P000 modification.

## 1. Model

At one chosen X6 Cell, distinguish native six-axis spatial directions from four internal V29 port/field labels 0,1,2,3 and from three V17 ordered slots. In the V23 model let S be one of the 20 three-subsets of six activity labels 0..5. Two S,T are neighbors iff they share exactly two labels, giving 9 possible successors per S. The four V23 codes c(S) are obtained from matchings
(01,23,45), (02,14,35), (03,15,24), (04,13,25), each with values -1,0,+1 according to one-from-each-pair parity.

Retain R680's precise deterministic score for the six R679 initial biases u0:
Psi(S,T) = 7*(u.c(T) + c(S)^T (M-M^T)c(T)) + w.c(T), w=(-1,1,-2,-1).
The three internal nonnegative PASS events are A=(0->1), B=(1->2), C=(2->0), each performed at most once; order is a specified positive BRC branch, not a claimed spontaneous event law. Each PASS increases M_ab by one and changes u by e_a-e_b, so three PASSs together restore u0. R680 verified that Psi has a unique maximizer over all nine neighbors at every tested prefix.

Unlike a sorted triad S, an ordered V17 slot frame F=(f0,f1,f2) assigns each activity label to a persistent slot position. Put S=sort(F). A legal S->T loses exactly one label x and gains exactly one label y. Define the exact inherited-slot update: F'_i=y when F_i=x, otherwise F'_i=F_i. The two shared activity labels keep their slot positions. This is an explicit observer-compatible V17 slot-carry operation in the declared local model.

## 2. Theorem A: a future-sufficient exact state

Fix an initial bias u0 and a starting triad S0 (with initial frame sorted). With at most one of each A,B,C, the pair (M,F) is sufficient for the entire future language and ordered-frame observations. Indeed M directly identifies which PASSs have already occurred. From M and fixed u0 recover
u=u0+sum_ab M_ab(e_a-e_b), Omega=M-M^T; obtain S=sort(F). Given a legal next event e, update M, compute the unique maximizing T under Psi, and apply the inherited-slot update to F. This map depends only on (M,F,e). Induction proves future sufficiency for any legal word.

If the observer includes the current complete (M,F), histories have the same observations under every common legal future iff their current (M,F) agree. Equality suffices by the transition argument; inequality fails already at future word length zero. Therefore, **for each fixed (u0,S0) separately**, the minimal number of future states under that declared observer is the number of reachable distinct (M,F) pairs. Under the coarser observer (M,S) and future unordered-triad outputs, the same argument yields distinct (M,S) pairs. No claim is made about a shared machine combining different initial inputs or stronger V39/rotation observables.

## 3. Theorem B: a shortest exact frame-loss witness within the tested domain

Take u0=(3,2,4,-10) and S0=145 with F0=(1,4,5). Applying all six orders of the three PASSs produces:

| PASS word | Final unordered S | Final ordered F |
|---|---|---|
| ABC | 124 | (1,2,4) |
| ACB | 015 | **(1,0,5)** |
| BAC | 345 | (3,4,5) |
| BCA | 015 | **(0,1,5)** |
| CAB | 345 | (5,4,3) |
| CBA | 345 | (5,4,3) |

Every final full V29 PASS ledger M, u and Omega is identical, because each event occurs once. ACB and BCA have the same unordered current triad 015 but distinct ordered slot frames. The common future legal V17 triad move 015->012 takes their frames to (1,0,2) and (0,1,2), respectively. Thus the difference survives a subsequent operation, not merely a naming convention.

The exhaustive checker found no such equal-ledger equal-triad different-frame collision after zero, one or two PASS events over the specified six biases and twenty starts. The displayed length-three witness is thus minimum **in this enumerated restricted model**.

## 4. Theorem C: finite exact state census and positive BRC branching

For each fixed (u0,S0), all legal non-repeating PASS words have lengths 0,1,2,3, with counts 1+3+6+6=16. There are 6*20=120 independent initial contexts and hence 1920 context-labeled histories.

The independent exact state-machine census obtains, after quotienting within each fixed context:

| Observer | Sum of minimal reachable state counts over 120 separate machines |
|---|---:|
| Raw event words | 1920 |
| (M, unordered S) | 1141 |
| (M, ordered F) | **1143** |

Histograms of minimum counts per context:
- (M,S): {8:59,9:14,10:10,11:10,12:21,13:3,14:3}.
- (M,F): {8:59,9:14,10:10,11:10,12:21,13:2,14:3,15:1}.

The only context with distinct frames on the same (M,S) fiber is u0=(3,2,4,-10), S0=145, after all three PASS events. It contains three unordered-word pairs with equal (M,S) but distinct F. These produce exactly two additional distinguishable states under the ordered-frame observer.

Give each of the six complete labeled event words positive BRC mass one. Their unordered output histogram is {124:1,015:2,345:3}. Their ordered-frame histogram is {124:1,105:1,015:1,345:1,543:2}. The coarse unordered histogram conserves total positive mass 6 but discards the allocation needed for ordered-slot predictions. This is a genuine typed structural residual, not signed amplitude cancellation, numerical noise or a fourth spatial axis.

## 5. Proof and verification boundary

The transition sufficiency/minimality theorem is a direct induction and observational distinguishability argument. The exact numerical state counts, minimal collision length and output fiber weights come from complete integer enumeration of all 120*16 histories, with explicit V23 codes, V27 scores, V29 PASS ledgers, inherited V17 frames and no floating-point operations. See R681_VERIFY.py, R681_EVIDENCE.json and R681_HANDOFF.md. Local checker finished R681_V17_ORDERED_FRAME_BRC_FIBER_EXACT_PASS.

This work makes no assertion that an autonomous PASS/TRANSFER scheduler was derived from the native X6 local permission graph, that full R675 rotation covariance was established for this augmented state, or that V39 current j has been coupled. Its finite observer scope is explicit; it is author-side research, not formally accepted Result/Review.

## 6. Next discriminating unit

Derive a source-backed autonomous local event selector on an X6 port-licensed network and couple the V39 loop-current j. Test whether (M,F,j,scheduler) admits a smaller future-sufficient quotient while respecting the verified slot and positive BRC branch weights, local conservation and typed rotational covariance. Preserve the frozen R462 science and independently verified author/Driver provenance.

Sources: P000 (p000_reality_foundation.json), Heartbeat World native X6 contract, R674 V29/V17 double-loop proof@7e85d3b0fe3543e28c91894c174090102babb6db, R679@fab76ba01a87745b098ab57a0219d958707bdbb9, R680@151d820a1c776fe4b1401ab0a23b1d0867c13883; current MATH_RESEARCH_POLICY and PORTABLE_RESEARCH_PROTOCOL.

## 7. Native/BRC-only arithmetic boundary

The calculations in this note are an exact finite **formal combinatorial model**: integer event scores, nonnegative V29 count updates, labeled ordered V17 slots, and six formal positive branch weights. We use the typed positive-branch bookkeeping law “one unit mass for each distinct label word; sum masses only when applying a declared observer.” No native-to-BRC physical correspondence, heartbeat propagation, phase evolution, cancellation amplitude or new executable BRC-kernel run is claimed. The source constraints `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md` and `research_constraints/heartbeat_brc_only.json` require an actual verified typed BRC interface before these formal counts may be used for native physical residual attribution. The latter remains `NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION` if ever proposed. The finite model-internal slot-frame witness and its exact mathematical proof have the narrower declared meaning given above.
