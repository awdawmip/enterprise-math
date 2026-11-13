# R715 — Exact source-query complexity after the BRC X6 pair-degree ledger

Status: author-side mathematical research / independent Driver review pending.
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`.
Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (unchanged).
Previous verified frontier: R714, Draft PR #2067, author commit `0208b28dfec535f6538ae8cc59938bf67bf262e5`.

## Model and three query interfaces

Let `V={0,...,5}`, `T=C(V,3)` (20 labeled triple identities), `E=C(V,2)` (15 pair identities). Full Boolean source state is `H⊆T`. Define the exact unsigned BRC pair-degree ledger
`D(H)_e = Σ_{t∈H} 1[e⊂t]`, equivalently `D=Ah` for the 15×20 pair/triple incidence matrix A.
A source membership query at a specified triple t returns `1[t∈H]`. D is already supplied (its acquisition cost is separate).

* Arbitrary auxiliary code: a bit string selected given H and D.
* Fixed-address query: select the same source-identity subset S for every H and D, obtain `h|S`.
* Adaptive query: select the next triple address as a deterministic function of D and previous membership answers, minimizing worst-case depth on each D-fiber.

Source-identity inquiries are different operations from updating a previously admitted signed triple event.

## Theorem R715.1 — exact five/four query separation

For the complete `2^20` Boolean state family with the full 15-coordinate pair-degree ledger known:

1. The largest degree fiber has size 12, so unrestricted fixed-length auxiliary recovery needs exactly 4 bits.
2. The minimum *universal fixed-address* membership query set has **5 triples**. Exactly **5,184** of the `C(20,5)=15,504` sets of five triples reconstruct every H; no set of four does.
3. The minimum *adaptive worst-case* membership query depth is **4**. Exact depth for fibers of cardinality k is `1→0, 2→1, 3→2, 4→2, 5→3, 6→3, 7→4, 12→4`. In particular, the twenty 7-state fibers need four membership queries, one more than the information lower bound of three.

One universal fixed set is `S={012,013,014,023,024}`. Remove those five columns from A. The remaining 15×15 integer submatrix has Bareiss determinant **+96** in lexicographic row/remaining-column order; knowing D and the five observed Boolean bits therefore uniquely determines all remaining triple bits by an exact rational linear solve.

## Exhaustive finite proof and audit

Assign pair indices 0..14 in lexicographic order. A triple t has integer weight `w_t=Σ_{e⊂t}5^{index(e)}`. The base-5 integer `L(H)=Σ_{t∈H}w_t` encodes all 15 exact degree digits without carry because an edge lies in at most four triples. Visit every one of the `2^20` H via binary reflected Gray order and update L by adding/subtracting the unique changed triple weight. Group H by L to obtain exactly **995,085** fibers:

| Fiber size | Number |
|---:|---:|
| 1 | 950,564 |
| 2 | 37,650 |
| 3 | 5,340 |
| 4 | 1,080 |
| 5 | 360 |
| 6 | 70 |
| 7 | 20 |
| 12 | 1 |

All non-singleton fibers contain **65,286** unordered colliding pairs (H,H'). Their nonzero symmetric-difference support masks H△H' form exactly **31** distinct masks: 15 masks of size 8, 15 masks of size 12, and the full 20-bit mask once. Under inclusion they have exactly **30** minimal masks (the 15 size-8 and 15 size-12 masks), matching the supports of R714's Pasch and 6↔6 trade classes.

A fixed S can recover H iff `S∩(H△H') ≠ ∅` for every colliding pair. This is equivalent to hitting those 30 minimal masks; exhaustive inspection of all sets with 0,1,2,3,4,5 queried triples yields successful counts **[0,0,0,0,0,5184]**. The displayed 5-set independently has an invertible 15-column complement with determinant +96.

For the adaptive case, define `F(U,d)` for a nonempty subset U of a known fiber: `F(U,d)` holds iff a binary decision tree of depth at most d identifies each state. Base `|U|≤1`; if `|U|>2^d`, return false. Otherwise try each triple index j and partition U by that membership bit; return true iff both parts are nonempty and satisfy `F(part,d−1)`. This recurrence is necessary and sufficient by induction on d. Execute it on all **44,521** nonsingleton fibers. Optimal-depth counts are `(size,depth,count): (2,1,37650),(3,2,5340),(4,2,1080),(5,3,360),(6,3,70),(7,4,20),(12,4,1)`. The unique 12-state fiber gives the universal lower bound of 4 queries; the recurrence constructs a tree of depth ≤4 for every fiber.

The attached standard-library Python verifier implements these exact enumerations, the depth recurrence and the Bareiss determinant. It emits `R715_BRC_TRIAD_MEMBERSHIP_QUERY_EXACT_PASS`; full machine-readable evidence is in the adjacent JSON file.

## BRC / native scope

This result supplies an exact source-observer design choice: 4 arbitrary side bits, 4 adaptive membership queries, or 5 universally fixed identity queries given pair-degree D. The operation/observer contract above is static Boolean source recovery, not a proof of dynamical sufficiency when event legality reads particular triple identities. In P000 native X6, the signed Cell/Link/Port state and V29 PASS/TRANSFER and V39 signed loop j are an additional admissibility and conservation layer.

**Next scientific unit:** at the task's frozen input, extract the actual native-legal family `H_native(c,state,time,source)`; compute the restricted pair-degree fibers and optimal membership trees; test both halves of a Pasch and a six-to-six witness for native realizability, actual legal membership-sensitive events, rotation covariance, BRC provenance and the typed `TRIADIC_CLOSURE_E` update. Keep author evidence, formal CLAIM, result freeze and independent Driver acceptance distinct.
