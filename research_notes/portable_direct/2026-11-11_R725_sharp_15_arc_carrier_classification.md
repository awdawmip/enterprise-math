# R725 — Exhaustive classification of sharp 15-arc X6/V17 CNB holonomy carriers

Date: 2026-11-11 (Asia/Shanghai).
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.
Native Researcher-ID: EM-X6-CE8BCF; activity RA-24E8F7A34C58EF4F084D3F82.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5).
Prior: R721b 15-arc construction and R723 global 15-arc minimum, immutable 5886f34e4d1c02f98c86b7dd9381286546790ddf.
Evidence status: author-side exhaustive finite proof, checked with exact integer/set code; independent review OPEN.

## Precise model and theorem

Work in the five accessible X6-axis labels {0,1,2,3,4}. The ten triads are the three-element subsets, and Ω consists of all 60 directed Johnson-neighbor arcs u>v with |u∩v|=2. Root is the triad 012 with initially ordered V17 slot frame 012. Every directed transition replaces the leaving axis with the entering axis *in its existing slot*. A positive rooted closed path v0=012,...,vm=012 obeys **cyclic nonbacktracking** (CNB): v_(i-1) != v_(i+1) for all cyclic indices, including the closing seam vm-1 != v1. For an allowed permission set E⊆Ω, H_m(E) is its set of final ordered root frames, a subset of S3={012,021,102,120,201,210}.

R723 establishes that any E with H_m(E)=S3 for every integer m>=4 has |E|>=15 and supplies a 15-arc witness.

**R725-A (complete classification):** Exactly **72** distinct labeled 15-arc sets E satisfy H_4(E)=H_5(E)=S3. Under the root-preserving axis-label group S3×S2 (permuting labels 012 and 34 independently), these form exactly **six** orbits of cardinality 12. Exactly **four** orbits satisfy H_m(E)=S3 for every integer m>=4; the other **two** fail first at m=6, realizing only {012,120,201} in their canonical representatives. Hence exactly **48** distinct labeled networks attain R723's global minimum for **all lengths**, forming **four** symmetry classes.

**R725-B (finite screen):** Within the exact domain |E|=15, H_m(E)=S3 for every m>=4 if and only if H_4(E)=H_5(E)=H_6(E)=S3. Checking m=4 and m=5 alone accepts 24 networks that fail at m=6.

## Exact exhaustive proof — all 15-arc candidates

For each length m=4,5 and each of six final frames h, enumerate **all** legal ordered positive rooted CNB paths in the unrestricted 60-arc graph. For each path record the set (60-bit union mask) of its directed permissions. Let C[m,h] be the complete set of distinct masks. By the literal path recursion, h belongs to H_m(E) exactly when at least one c∈C[m,h] is contained in E (bitwise c&E=c). This is an exact existence observer; the ordered path is generated before reducing its used-edge mask.

The six catalog cardinalities, in frame order 012,021,102,120,201,210, are:
- length 4: 12, 16, 16, 6, 6, 16
- length 5: 60, 40, 40, 66, 66, 40.

Beginning with empty permissions, choose an unsatisfied (m,h) condition and branch on **every** feasible path-mask witness; add its edges by bitwise union. Reject states exceeding 15 edges or missing a witness within the remaining budget. Memoization by the current selected mask is exact, because remaining budget is 15 minus its bit count. If all twelve obligations are witnessed, emit the selected mask.

**Completeness:** For any feasible E of cardinality 15, each currently unwitnessed group has at least one path mask contained in E. The exhaustive recursion includes that witness and can continue inside E. The cited R723 exact lower-bound proof shows no permission set of size <=14 can satisfy lengths 4 and 5 simultaneously. Thus every successful branch has exactly 15 bits, and its selected mask must equal E. Every and only feasible E is enumerated.

Two alternative exact search orders yielded identical sets of 72 masks:
| Strategy | Recursion calls | Distinct visited masks | Final sets |
|---|---:|---:|---:|
| Fewest feasible next witnesses | 19,447 | 19,223 | 72 |
| Reverse fixed (m,h) group order | 1,226,545 | 1,169,633 | 72 |

Both use arbitrary-precision integer bit operations and finite sets.

## Symmetry classification and infinite-length certificates

The 12 permutations in S3×S2 relabel all triads and arcs while preserving adjacency, root triad, CNB and the V17 slot-replacement rule. A permutation of root-axis labels changes the initial-frame gauge by a fixed slot permutation and therefore bijectively relabels the six final S3 outcomes; the property of **full S3 support** is invariant. The 72 networks partition into six disjoint orbits, each of size 12; the complete code checks equality of this orbit union with the candidate set and absence of a smaller stabilizer.

For each canonical orbit representative, propagate the finite typed sets D_t of states (previous triad, current triad, ordered slot frame, first neighbor after root). Every legal nonbacktracking successor defines D_(t+1)=F_E(D_t). A length-t state contributes to H_t only when the current triad is the root and the previous triad differs from the stored first neighbor. Exact equality D_t=D_(t+1) then implies **full typed-state constancy for all later t** by induction.

| Class | Canonical 60-bit mask (decimal) | Certificate | Verdict |
|---:|---:|---|---|
| 1 | 211733226574 | D_10=D_11, 270 states | Six states for all m>=4 |
| 2 | 423074469777 | D_9=D_10, 180 states | Six states for all m>=4 |
| 3 | 5363347296468 | D_9=D_10, 180 states | Six states for all m>=4 |
| 4 | 14021360160796 | D_10=D_11, 270 states | Six states for all m>=4 |
| 5 | 378233292275810 | m=6 support {012,120,201} | Fails at m=6 |
| 6 | 2287401872294258 | m=6 support {012,120,201} | Fails at m=6 |

For classes 1,4 every m=4,...,11 is directly verified and the complete 270-state D_10=D_11 equality proves all future lengths. For classes 2,3 every m=4,...,10 is verified and the complete 180-state D_9=D_10 equality closes all future lengths. Classes 5,6 have all six frames at m=4 and m=5, but only the three even root permutations at m=6. The original R721b witness falls in class 4. Because the group action preserves the all-length support property, exactly 4×12=48 of the 72 networks are full-length carriers.

This proves the finite-screen corollary: for every 15-arc E, passing the three tests m=4,5,6 selects precisely the four complete classes.

## Executable evidence

Run the adjacent program:
    python R725_15ARC_CLASSIFY_VERIFY.py > R725_15ARC_RESULTS.json

Expected marker: R725_15ARC_EXHAUSTIVE_CLASSIFICATION_PASS.
The JSON records all 12 path catalog sizes, two solver call counts, all six representative 15-arc lists and their mask IDs, the complete typed-set equalities or the failure length and resulting support, plus the R721b witness-class match. The enumeration domain is complete, finite and precisely stated. No floating-point numbers are used.

The theorem is for **Boolean existential final-frame support** of positive BRC/V17 paths in the rooted five-axis CNB permission model. Full branch multiplicity, provenance-sensitive future observations and actual V29 Link/Port inventory and event-time admissibility remain separate typed questions. Five accessible axes are a slice of P000's six-axis world. The fixed P000 triadic-balance premises are unchanged.

## Next scientific unit

Compare the four extremal classes under native V29 Link/Port event admissibility. Map each representative's 15 permissions into signed Cell-force incidences, positive port ledgers, one-event-per-participant temporal constraints and provenance. First compare class 2 (180 stable typed states) with the legacy class 4 (270 states). Determine the exact additional staging/permission cost of any unrealizable arc, then compute a native-constrained support and future-observer quotient. Preserve each branch's identity until that quotient is proved safe.

Review=UNREVIEWED; Native Result=not frozen; task publication and all ownership rules remain unchanged.
