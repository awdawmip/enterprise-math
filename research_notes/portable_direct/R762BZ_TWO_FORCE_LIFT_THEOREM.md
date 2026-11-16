# R762BZ — Signed-X6 apparent two-force triadic lift: equivariant no-go and exact BRC repair

Date: 2026-11-16 (Asia/Shanghai). Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142.
Status: AUTHOR-PROVED exact conditional combinatorics; independent review NOT_REVIEWED. Native TRIADIC_CLOSURE_E event licensing is OPEN.

## Frozen premises and the declared candidate interface

Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. P000 fixes six signed native spatial axes, a separate time dimension, PERP_E/120-degree orthogonality, and the requirement that apparent two-force balance receive a triadic lift. It does not prescribe a unique Cell/Port/Link event predicate. Current ACTIVE worldview retains a 3D research slice of the 6D X6 Cell torsor and provenance-sensitive residuals.

This theorem extends the explicitly CONDITIONAL three named signed-Port model of R762BY, Draft PR #2544@91356f8b05c2682ca1bf454d9ea5fae686b7ee95, and V17 active-frame replacement semantics; V1R distinguishes the signed internal Cell fiber from its spatial address. All proofs below concern this defined candidate relation, not an independently licensed native physical event.

Fix one X6 Cell anchor x, a positive force quantum q, and directed named Links p0→p1→p2→p0. The full state has distinct native axis labels (a,b,d) in A={1,2,3,4,5,6} and signs (s0,s1,s2) in {±1}^3. The three named Port/force slots have fixed identity. There are (6·5·4)·2^3 = 960 full signed frames F=(a,b,d;s0,s1,s2) at fixed x,q.

Define the apparent two-Port observation pi(F)=(a,b;s0,s1), retaining the declared existence and orientation of the hidden third Port and Link cycle. There are 6·5·2^2=120 such observations. For each observation, the hidden d belongs to A\{a,b}, a four-element set, and the hidden s2 is ±1. The exact fiber contains 8 full frames.

Future availability interface: Port p0 is eligible for the declared R762BY/V17 axis replacement; a proposed target y in A\{a,b} is legal iff y differs from hidden d. Define L_y(F)=1[y≠d]. These are *conditional graph* legal-target queries. Optionally add a direct third-sign observation S(F)=1[s2=+1]. No Euclidean force summation or physical calibration enters the model.

## Theorem A — exact lift and covariance obstruction

1. For each pi-fiber there are exactly 4 hidden-axis labels times 2 hidden signs. An exact full-frame repair therefore needs ceil(log2 8)=3 fixed-length bits, attained by an index of the four unused axis labels and a sign bit. If the declared future reads only legal-target responses L_y, hidden signs are equivalent, and the exact repair needs 2 bits for four classes.

2. There is NO deterministic S6-axis-relabel-equivariant third-axis completion d(a,b) in A\{a,b}; the same holds when it additionally takes visible signs but no new source label. Proof: fixing (a,b), its pointwise stabilizer S4 fixes the visible arguments and acts transitively on the other 4 axis labels. An equivariant output would be fixed by the entire stabilizer, and no unused label is. This argument is entirely finite and applies to each signed observed pair.

3. Any S6-covariant positive probability distribution on the four hidden-axis completions is uniform. On the eight signed completions S6 alone allows separate total weights for the two hidden-sign sectors, but each sector must be uniform over the four axis labels. If independent hidden signed-axis gauge reversal is also part of the *declared* observer symmetry, it exchanges the two sign sectors and forces all eight probabilities to be 1/8. The covariance is an assumption about the observer interface; positive weights are BRC selection weights, not signed physical amplitudes.

## Theorem B — a single legal-target query detects the lost joint source

Given two full frames with the same observed pair and distinct hidden labels d and d', query target y=d. It is illegal for the first frame (L_d=0) and legal for the second (L_d=1). Thus the two-force projection is not operation-safe for a future containing all such legal-target queries. The four legal-target response vectors have exactly one zero each, at the hidden d, and are pairwise distinct. The quotient by these observations has exactly 4 classes. Hidden sign variants have identical legal-target responses; when the future additionally queries S they become 8 classes.

This is a precise BRC / joint-relation observer-loss witness. The third Port is hidden by a two-force effective readout, not deleted from the primitive triad. The 2-bit statement is scoped to the specified future language; a full provenance-sensitive history may require additional state.

## Theorem C — sharp binary-query cost

An atomic query may test one L_y at a time. Recovering the hidden d takes exactly 3 worst-case adaptive queries, and exactly 3 nonadaptive queries, although its storage index is only 2 bits. Proof: after any two distinct queries answered true, at least two of the four originally possible hidden labels remain, so the adaptive worst-case lower bound is 3. Any fixed two queries also leave their two unqueried labels identical. Query any three different candidate axes: the one false answer identifies d, or three true answers identify the fourth. This attains both bounds.

If one additional atomic query S reports the hidden sign, the exact (d,s2) requires 4 worst-case adaptive and 4 nonadaptive queries: the sign bit is independent of the target-legality answers, and the three-membership-query lower bound survives within either sign sector; one S plus the previous three-query construction attains it.

| Future observer | Hidden equivalence classes | Fixed repair bits | Adaptive worst-case atomic queries | Nonadaptive atomic queries |
|---|---:|---:|---:|---:|
| L_y for visible Port replacement | 4 | 2 | 3 | 3 |
| L_y plus third-Port sign S | 8 | 3 | 4 | 4 |

## Exact verification

Companion R762BZ_TWO_FORCE_LIFT_VERIFY.js performs independent exact enumeration of 960 full frames, 120 distinct pi-fibers, 720 S6 axis permutations, 2,764,800 legal-target covariance checks, S4 stabilizer transitivity, hidden-branch distinguishing witnesses, and complete adaptive/nonadaptive query optimizations on 4- and 8-state fibers. Evidence is captured in R762BZ_TWO_FORCE_LIFT_EVIDENCE.json. A separately written Python 3 finite enumerator obtained matching totals for every stated result. The group-theoretic proofs cover the declared finite alphabet without extrapolation.

## Relation to prior work, limits and next question

R762BQ–BT optimize directed-Link observations of a previously specified 8-state partition fiber. Here the observable is the availability of an upcoming native-axis replacement after hiding one Port; the 4-state signature and S4 selector obstruction are a different question. The R762BY k-gated model supplies a concrete prospective transition alphabet but has not established the actual licensed TRIADIC_CLOSURE_E event predicate or the authoritative V17/V29/V39 physical transducer. V27 and V36 construct conditional PF-10/network active-triad dynamics, not that native licensing rule.

Next: read the task-pinned signed Cell/Port/Link event sources and implement the actually licensed predicate P(F,event). Restrict the 8-completion Boolean observation matrix to native-allowed actions, then recompute its exact BRC fiber partition, covariant selectors and shortest distinguishers. Preserve Cell anchor, sign, Link, provenance and event order for any future query that actually depends on them. Independent Driver review remains NOT_REVIEWED; no P000 or Foundation promotion is proposed.
