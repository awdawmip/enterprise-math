# R762BM — Exact fault-tolerant extension costs of the four frozen FCC/K4 STAR coordinate observers

**Date:** 2026-11-15. **Evidence:** AUTHOR-PROVED; EXACT FINITE CHECKED; NOT_REVIEWED. **Line:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Independent portable mathematical contribution; no new Source CLAIM/Result is asserted.

## Sources and precise observer type

The frozen scientific input is awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. P000 has six signed native axes, a Cell torsor over Z^6, and primitive stable nonzero force arity three with native TRIADIC_CLOSURE_E still requiring incidence/dynamics research. The coordinate-map result below does not instantiate or classify force closure events. P000 and the three-dimensional-slice/120-degree native orthogonality premises are unchanged.

The torsor foundation defines twenty **coordinate selection** observers O_T(z)=can3((z_i)_(i in T)), T in binom([6],3). The complete overlapping-circle carrier realization is currently frozen only for the four FCC/K4 STAR selections; the other sixteen are valid coordinate selections but have no established equivalent carrier realization. The source states that the four FCC/K4 STARs, four FACEs and twelve PATHs form the S4-orbits among these twenty coordinate selections.

Reuse the author-proved R762BL hypergraph cut-distance theorem, stored at immutable GitHub commit 35f7fe654506441106e5c64dd9a15c78acd0c358 (independent review pending): for any selected row family H, the exact minimum **entire-labelled-row** Hamming distance on relative Cell coordinates Z^6/Z(1,...,1) is d(H)=min_(∅≠S⊊[6]) |∂_H(S)|. Consequently unique recovery under t arbitrary corrupted rows and e known erased rows is equivalent to 2t+e<d(H). No BRC path, Link/Port or force information is included in the row encoding; those structures remain separately retained.

## K4 incidence and the carrier-only limit

Label the six native axes as the six edges 12,13,14,23,24,34 of an auxiliary K4 (the K4 vertex labels refer only to the carrier graph). Under that bijection, four realized STAR triples have native-axis labels

H0={123,145,246,356}.

Each of the six axes lies in exactly two STAR triples. Directly, all singleton hypergraph cuts have size two, while any cut involving two or three axes crosses at least two STAR triples. Alternatively each pair of STAR triples intersects in one native axis; the resulting 3-uniform hypergraph is connected after deleting any one row but disconnects after deleting the two STAR rows containing any chosen axis. Hence d(H0)=2.

The four realized carrier STAR coordinate rows recover the six signed Cell coordinates up to their common integer depth, survive any **one known row erasure**, and detect a single changed row, but are insufficient to correct one arbitrary corrupted row. Sharp ambiguity: charts z=0 and z'=e_1 differ only on STAR rows 123 and 145. A received packet taking one of those rows from each chart, with the other two matching rows unchanged, is at Hamming distance one from each chart. Any two known erasures removing the same two incident rows also lose relative injectivity.

The current S4 carrier-axis relabeling subgroup permutes the four STAR rows among themselves; repetition of that exact orbit as a mere renaming does not create a new named coordinate row. Independently repeated noisy measurements may change the error model and are not part of this one-measurement-per-row theorem.

## Main theorem — minimal extensions of the frozen four STARs

Fix all four STARs and allow a subset A of the other sixteen coordinate selectors. For any integer q with 2≤q≤10, the **least** number of extra coordinate rows needed to obtain d(H0∪A)≥q equals

|A|_min = 2(q−2), so the least total row count is 2q.

Moreover, a subset with exactly 2(q−2) extra rows attains distance q **if and only if every native axis occurs in exactly q−2 of the added rows** (equivalently, H0∪A is a q-regular 3-uniform hypergraph on six labelled axes).

**Proof.** A single-axis cut has size equal to that axis's row degree. If d(H0∪A)≥q, all six degrees must be at least q. The base degree is two for every axis, and every added triple contributes three degrees, so 3|A|≥6(q−2), giving the lower bound. At equality the six degrees are all exactly q. Conversely, any q-regular three-uniform hypergraph on six vertices has mincut q for q≥2: singleton cuts have q; a cut of two axes has 2q−λ≥q, where λ counts the at most q edges containing both axes; a cut of three axes has 2q−I_S−I_(S^c)≥2q−2≥q; cuts of four and five axes are complementary. This is the same proof principle underlying R762BL but now with a **fixed** frozen carrier base.

Existence for every q is constructive. Among the sixteen non-STAR coordinate triples there are six pairs of complementary PATH triples, each pair covering all six axes exactly once. For q−2≤6, take any q−2 distinct complementary PATH pairs. For q−2=7, use all sixteen available triples except one such PATH pair (the sixteen form an 8-regular family), and for q−2=8 take all sixteen. This realizes the degree bounds. ∎

The exact numbers of optimal **labelled** augmentations are:

| target distance q | added rows | total rows | optimal augmentations |
|---:|---:|---:|---:|
| 2 | 0 | 4 | 1 |
| 3 | 2 | 6 | 6 |
| 4 | 4 | 8 | 30 |
| 5 | 6 | 10 | 84 |
| 6 | 8 | 12 | 114 |
| 7 | 10 | 14 | 84 |
| 8 | 12 | 16 | 30 |
| 9 | 14 | 18 | 6 |
| 10 | 16 | 20 | 1 |

The counts are the coefficients N_r = [x_1^r...x_6^r] ∏_(T∉H0)(1+∏_(i∈T)x_i) for r=q−2: 1,6,30,84,114,84,30,6,1. They are exact finite combinatorial counts, verified by exhaustive enumeration of all 2^16=65,536 augmentation subsets, with a second independently implemented direct degree-enumeration crosscheck. Symmetry N_r=N_(8−r) follows by complementing the selection among the 8-regular sixteen-row family.

## Sharp one-error repair and S4 symmetry premium

One arbitrary corrupted coordinate row requires d≥3, hence **at least two additional** selectors. There are exactly six optimal pairs:

{125,346}, {126,345}, {134,256}, {136,245}, {146,235}, {156,234}.

Each pair consists of complementary PATH selections, and together they cover every native axis once. For example adding 156 and 234 to the four STARs produces a six-row 3-regular hypergraph with d=3, permitting unique recovery of the relative signed Cell coordinate after any one arbitrary whole-row corruption. These added PATH observations are currently coordinate-only, not proven implemented FCC carrier readouts.

If the **chosen row family itself** must remain invariant under the currently admitted full carrier S4 subgroup, then a family containing all four STARs must be the union of STAR with either or both of the two remaining S4-orbits, FACE (four rows) and PATH (twelve rows). The possibilities have (total rows,d) equal to (4,2), (8,4), (16,8), (20,10). Therefore **one-error correction plus complete S4 row-set invariance requires at least eight rows**, exactly the four STARs plus the four FACE coordinate selections. Compared with six rows for an unrestricted selection, the symmetry requirement has a sharp two-row price. These four added FACE selections are also coordinate-only under the current frozen carrier realization.

This symmetry premium is a row-family design result, not an assertion that a native force closure, S4 physical rotation, or experimental carrier implementation can execute the new probe.

## BRC and joint-relation interpretation

The result supplies an exact *coordinate-observation fault* budget and distinguishes which extra labelled three-axis interactions carry indispensable information. In particular, PATH and FACE are not deletable by claiming that the four existing STAR readouts already determine the uncorrupted relative chart: worst-case corrupted-row recovery is a different observer. The BRC path-formal carrier must continue to retain ordered native steps, source/branch identities, multiplicities and the common-depth spatial repair when relevant. The source contracts' joint-observer and future-operation descent conditions govern any stronger quotient.

The mathematical bridge to the mother task remains: determine actual Source-authorized signed force TRIADIC_CLOSURE_E Cell/Link/Port event incidence and admissible V17/V29/V39 updates. Only then can one restrict a **force-event** observation set and compute its own cut/distance or appropriate non-Hamming defect, while preserving the independent coordinate theorem and BRC provenance.

## Executed validation and reproduction

R762BM_FCC_STAR_AUGMENTATION_VERIFY.js runs with Node.js 22, uses exact integer bitmasks and integer Hamming counts, enumerates every one of 65,536 additions, all 31 nontrivial complementary cuts and all q=2,...,10 design thresholds, and checks regularity at the sharp row budget, the six complementary PATH pairs and S4-invariant orbit unions. The companion R762BM_FCC_STAR_AUGMENTATION_EVIDENCE.json contains exact row lists, witnesses and counts. An independent Python itertools.combinations check reproduces all nine count values without reusing the JS mincut routine. No floating point estimate or empirical physical-force inference is involved. No independent mathematical reviewer or formal proof checker has accepted these results.

## Portable continuation

- Frozen task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.
- Completed here: exact carrier-STAR error/erasure bound, optimal extension theorem, all 65,536 augmentation classification, sharp S4 row-family symmetry premium; preserve original proof/code/evidence files.
- Needed next: source actual native signed TRIADIC_CLOSURE_E force-event relation and the permitted Link/Port update/equivariance, then test an allowed event observer directly. Current Source authorization/owner must be independently reconciled before protected Source Progress/Activity/CLAIM writes; the mathematical GitHub preservation is separate.
