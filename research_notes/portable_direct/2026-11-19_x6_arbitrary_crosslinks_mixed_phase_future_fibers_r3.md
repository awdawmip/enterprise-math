# X6 native-time cut observers IV — arbitrary crosslinks, mixed local periods, and future-safe source repair

Date: 2026-11-19 (Asia/Shanghai). Scope: **author-side exact mathematical result in a conditional finite event-poset model**. Research line: RS-X6-NATIVE-TIME-DYNAMICS, immutable publication TP2-91D4A7C2F63805BE21A3. Frozen scientific foundation: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. P000 retains six native spatial axes, separate event time and primitive TRIADIC_CLOSURE_E. No new native Cell/Link/Port event is admitted by this poset theorem. Independent mathematical review is pending.

## Prior source and genuine extension

Reuse, without recalculation: the independent-chain / C12 winding study at f115d6abf67f4dd41fe8a4d89367a0b1d1caa55f; the one-link study at c8a44eeb585f83be41a161f1492caae07f8066f6; the 2026-11-17 opposing two-link exact proof at 6e2ad6bc4da4b76a27fbe59c767ba787e5f1d104; and the 2026-11-19 one-link phase-fiber theorem at cfa0c2903602f8edaa99fe200270b296039e4083. The guarded triadic-resource-conflict witness at 98d4d694933fa159276c20caa6970d68d5e3a55b shows why a precedence-only model needs separate native admission and resource-compatibility checks.

The extension here covers **arbitrarily many two-chain causal crosslinks, including links of both orientations**, **different exact local return periods** and **minimal memory for source-labelled future-language preservation**. It resolves the former "several links may create holes" possibility: the legal two-chain k-cut count support is always contiguous for an acyclic precedence relation.

## Conditional labelled-BRC carrier and axioms

Take two distinguishable local source-event chains A_1<...<A_a and B_1<...<B_b, a,b positive integers. Let E_AB contain (r,s) meaning A_r<B_s, and let E_BA contain (u,v) meaning B_u<A_v. Include chain relations and assume this finite graph is acyclic. A legal prefix ideal is specified by local counts i,j with k=i+j. Declared fully decorated local phase readouts have **exact periods p_A,p_B**, independently of the hypothetical crosslink. Time k is an event count, not a physical interval.

The typed Boolean-support BRC carrier is a set of labelled branch words in the alphabet {A,B}; its source/branch provenance and order are retained before projection. An allowed operation appends A or B only when the resulting prefix is a legal ideal. For Boolean reachability and these append operations, the count-support map from words to (i,j) is exact and commutes with updating support, since the guard depends only on counts. This is observer-scoped, and does not discard multiplicity or signed amplitude for another observer. We then examine the nontrivial second projection (i,j) -> (k,i mod p_A,j mod p_B) rather than presuming it is future-safe.

## Theorem I: exact interval support for any finite crosslink set

For k=0,...,a+b define

    L(k) = max(0, k-b, max_{(r,s) in E_AB} min(r,k-s+1))
    U(k) = min(a, k, min_{(u,v) in E_BA} max(v-1,k-u))
    W(k) = U(k)-L(k)+1.

An empty inner maximum/minimum contributes no bound. The exact set of reachable k-cut ideals is

    I_k = {(i,k-i) : L(k)<=i<=U(k)}.

With acyclicity, L(k)<=U(k) and W(k)>=1 for every k. The exact ideal-count polynomial is C(x)=Σ_{k=0}^{a+b}W(k)x^k, and C(1)=Σ_k W(k).

**Proof.** The original chain bounds are max(0,k-b)<=i<=min(a,k). A_r<B_s requires (j<s OR i>=r). Since j=k-i, this is i>=min(r,k-s+1). B_u<A_v requires (i<v OR j>=u), which is i<=max(v-1,k-u). Intersecting all these one-sided constraints gives exactly the stated interval. Conversely they describe all order ideals in the two-chain-generated poset. Every ideal of a finite acyclic poset is a prefix of a linear extension; a linear extension has an ideal at every k. Therefore there are no missing ranks or internal holes. QED.

This replaces arbitrary edge-wise inclusion-exclusion by an upper and lower envelope. A cycle is outside the theorem: counted prefix candidates need not extend to any full event history.

## Theorem II: heterogeneous periods are joined by LCM

Put P=lcm(p_A,p_B). Two cuts at the same rank k have equal total count and both equal complete local phases iff their A-counts differ by a multiple of P. For an observable phase pair compatible with k, let q be its uniquely determined A-count residue modulo P. Then the exact fiber cardinality is

    F(k,q) = floor((U(k)-q)/P) - floor((L(k)-1-q)/P).

Consequently the maximum phase-fiber size and the optimal worst-case number of selector bits at k are

    M(k) = ceil(W(k)/P),
    b(k) = ceil(log_2 M(k))   (zero when M(k)=1).

A uniform fixed-length selector over the entire finite process requires B=max_k b(k) bits. All rank-cut phase observations are injective exactly when max_k W(k)<=P.

**Proof.** Equal A phase says p_A|(i-i'); equal B phase at fixed k says p_B|(i-i'); both hold iff P|(i-i'). A length-W integer interval has at most ceil(W/P) members in one congruence class, attained by some class; the floor difference counts each class exactly. The largest fiber requires exactly its binary index width, attainable by ordering its members. QED.

**Sharp one-link horizon.** With a=b=P (whether or not p_A=p_B), absent crosslinks the only distinct same-phase/same-k pair is (0,P) and (P,0) at k=P. Any single AB or BA crosslink forbids one of those two extremes, so it removes the entire ambiguity for this horizon. This extends the previous equal-period one-link result.

**Explicit longer-horizon counterexample.** p_A=3,p_B=4,P=12,a=24,b=12; add A_2<B_1. At k=24 both (12,12) and (24,0) are legal, with identical phase observation (24,0,0). One edge does not guarantee source recovery at longer horizons.

## Theorem III: these fibers are actual future-language distinctions

Let the future observer include the complete permitted **source-labelled** continuation language (words of A/B to finish the declared finite poset), and retain the premise that every ideal extends to a full serialization. If (i,j) and (i',j') are distinct ideals at the same k, their complete continuation-word languages are disjoint. Therefore every collision in Theorem II is an operationally relevant residual under this observer. The minimum number of extra bits needed to make the phase/count quotient *future-safe* is **exactly b(k)** (or B uniformly), not only a lower bound for instantaneous reconstruction.

**Proof.** Every complete continuation from (i,j) contains exactly a-i remaining A labels and b-j remaining B labels. Different ideals at the same k have i≠i', hence different remaining A counts. No labelled completion word can be shared. A future-safe quotient therefore must distinguish every element of each observation fiber. Conversely its fiber index recovers exact (i,j), after which every declared append guard and future language is computable. Theorem II supplies the optimal index size. QED.

**Explicit future witness.** With p_A=2,p_B=3,a=b=6 and no crosslinks, cuts (0,6) and (6,0) both read k=6, phases (0,0). Their unique complete labelled future words are AAAAAA and BBBBBB, respectively. The missing source bit is physically uncalibrated but exact in this typed event model.

## Finite executable checks and evidence

The accompanying standard-library checker x6_two_chain_multi_edge_phase_brc_verify.py implements the **actual source-labelled-branch / Boolean-support guarded append** and independently enumerates reachable labelled words and their supports; it verifies all k-bound envelopes and mixed-period phase fibers. Scope: all acyclic crosslink subsets for a,b in (1,1),(1,2),(2,1),(2,2),(2,3),(3,2); all acyclic subsets with at most two crosslinks for (3,3). Period pairs: (2,2),(2,3),(3,4),(4,5).

Observed PASS: **815 acyclic event posets, 4,933 rank supports**, of which 422 contain AB and BA links together; explicit mixed-direction 4x4 case; **72** oriented one-link choices at a=b=P=6; the future-language collision and the long-horizon C12 collision. Executed checker SHA256 c3e15ea922a6b158ed36f72e7aa787c4876fd6969c4ff506ab45f29e1c995e77. Output JSON SHA256 1c5e29a222a6446e7e9372229ce228ddaed222b3a207b37b150670e96381ce3c. The universal theorems are derived from proofs; finite checks do not extend their verified range by extrapolation. Calculation uses exact integers to implement the typed BRC source/branch-support operations; no pi/trigonometric, continuous wave or signed-amplitude computation.

Reproduce with:

    python3 x6_two_chain_multi_edge_phase_brc_verify.py > x6_two_chain_multi_edge_phase_brc_results.json

## Next live-native question and provenance separation

The 2026-11-18 source-triad alternative-exit model has exclusive resources: an event configuration may fail to be any order ideal of a precedence poset even though each individual source/port event is enabled. Before applying Theorems I–III to native X6, verify an admitted signed three-force TRIADIC_CLOSURE_E multi-Cell update, source/target link/port resource ledger, token and branch provenance, enabling/conflict semantics and future observer; then prove a correspondence between **actual reachable configurations** and a two-chain ideal carrier. If conflict survives, study a BRC carrier of guarded configurations rather than using the interval formula.

Scientific publication and its independent GitHub readbacks are distinct from Researcher/Activity linkage, native CLAIM/PROGRESS, Result and independent Review. Earlier author IDs, frozen pins and the existing unresolved cfa0 Activity attribution are preserved. No current live owner or native writing authority is inferred from this note.
