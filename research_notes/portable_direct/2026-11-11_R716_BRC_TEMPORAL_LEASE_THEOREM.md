# R716 — Sharp temporal recovery radius for X6 BRC pair-degree ledger
Date: 2026-11-11. Research status: author-side proof and exact finite verifier; formal CLAIM/Driver review pending.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Input: R714 Draft PR #2067, R715 Draft PR #2071.

## Model
Six labeled native axes V={0,...,5}. Let T=C(V,3), |T|=20, E=C(V,2), |E|=15. A Boolean labeled triple carrier is H⊆T and its exact pair-degree BRC observer is D(H)_e=#{t∈H:e⊂t}, i.e. Ah where A is the 15×20 incidence matrix. This defines a candidate source-carrier interface and does not assert that every H is a physically realizable X6 Cell state.

Observer contract: previous full labeled source state H0 is known, later exact pair-degree D(H1) is measured, and |H0△H1|≤r. Determine when H1 is uniquely recoverable. A bound on the total number of actual toggles implies, but is stronger than, the symmetric-difference bound.

## Theorem R716.1 — distance eight and radius-three exact recovery
For every finite V, any distinct Boolean triple-source states H,H' with D(H)=D(H') satisfy |H△H'|≥8. Hence for any fixed full H0, the observation D restricted to its Hamming-radius-three ball is injective. For six axes the decoder enumerates Σ_{k=0}^3 C(20,k)=1,351 source states H0△S, |S|≤3, computes D of each and returns the unique matching candidate.

Proof. Let δ=1_H−1_H' ∈{-1,0,1}^T be nonzero with Aδ=0. Summing all pair equations counts each triple three times, so there are equally many positive and negative triples, say p=q. Select a positive triple abc. Its edges ab,ac,bc require at least three **distinct** negative triples; any negative triple different from abc includes at most one of these three edges. Therefore q≥3.

If p=q=3, the three negatives must have forms abx,acy,bcz with x,y,z outside {a,b,c} (they may coincide). The pairs ab,ac,bc are then exactly balanced by abc and those three negatives. Consequently, the other two positive triples may not contain any of the three pairs. The negatives contribute six cross-pair incidences, counted with multiplicity, joining {a,b,c} to outside axes. A triple with at most one of {a,b,c} contributes at most two such incidences; the two remaining positive triples contribute at most four, contradiction. Thus p=q≥4 and |H△H'|=p+q≥8.

If D(H1)=D(H1') and both H1,H1' lie within three flips of H0, the triangle inequality gives |H1△H1'|≤6, hence H1=H1'. QED.

## Theorem R716.2 — sharp radius four and six-axis collision census
Let A0={012,034,135,245} and B0={013,024,125,345}. These disjoint four-triple states have exactly the same pair-degree ledger and differ on eight labeled sources. Choose H0 as a midpoint: on their eight-source support, H0 differs from A0 in four positions and agrees with both endpoints outside the support. Then both states lie at Hamming distance four from H0 and D(A0)=D(B0). Thus radius three is universally optimal.

Six axes have 15 perfect matchings into three pairs. For each matching, the eight triples choosing one axis from each pair split into two complementary four-triple parity classes with equal pair-degrees. These give all 15 size-eight difference supports (verified by full exact collision enumeration).

For a given Pasch support, precisely C(8,4)=70 of the 2^8 local patterns of H0 are midpoints; 12 outside bits are unrestricted. A radius-four collision exists iff H0 is a midpoint on at least one such support: by the distance-eight bound, two radius-four endpoints with equal degree must differ in exactly eight positions, hence their difference support is one of the 15 Pasch supports.

Complete integer/bitset enumeration over 2^20=1,048,576 six-axis H0 states:
* Ambiguous radius-four initial states: **1,035,556**.
* Unambiguous radius-four initial states: **13,020**.
* Sum of midpoint-trade incidences over initial states: 15×70×2^12=**4,300,800**.
* Number of candidates at radii ≤3 and ≤4 respectively: **1,351** and **6,196**.
* Full ledger fiber census: **995,085** fibers, **65,286** unordered colliding source pairs, **31** difference supports of sizes 8 (15), 12 (15), 20 (1); minimum distance eight.

The exact fraction 1,035,556/1,048,576 is uniform counting on abstract Boolean masks, not a probability statement about native X6 physics. The general distance proof is valid for any finite number of axes; the finite census applies to six labeled axes.

## BRC use and next executable scientific unit
Carrier = labeled Boolean triples; observer = 15 exact integer pair degrees; repair = previously verified complete H0 plus a certified bound of ≤3 changed triple memberships across the observation interval. Within that scope full source identity can be reconstructed without the 4 arbitrary side bits, 4 adaptive or 5 fixed identity probes needed in the memoryless R715 interface. If the transition gives signed identities of toggled triples, H itself can instead be updated incrementally.

At the frozen Task input, derive true native legal H_native(c,Cell,Link/Port,t,source), including V29 PASS/TRANSFER, V39 loop current j, Cell identity and six-axis permutation covariance. Test whether a primitive event can alter no more than three Boolean triple memberships; if the bound is larger, test native reachability of the Pasch midpoint and retain labeled BRC provenance when needed. Confirm legality before using this candidate observer compression.

Evidence: R716_BRC_TEMPORAL_LEDGER_VERIFY.py, R716_BRC_TEMPORAL_LEDGER_RESULTS.json. Proof is author-side; independent Driver review and native semantic checkpoint are not part of this mathematical certificate.
