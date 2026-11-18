# EC49FLD — Complete exact matched-distance-six two-key BRC shell

**Date:** 2026-11-12. **Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** AUTHOR_EXACT_FINITE_COMPUTATION; independent Driver mathematical review pending.

## Theorem

In the frozen nine-state signed-X6 BRC model, use the complete 178,850 legal labeled operation words, 24 exact observer demands and 94 full raw cache keys. The explicit 84-prefix EC49FKX witness has seven keys
`K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.
Delete two distinct keys `a,b` from K* and insert two distinct keys `u,v` outside K*. Matched L1 distance is
`d=min(||a-u||_1+||b-v||_1,||a-v||_1+||b-u||_1)`.

**Exact distance-six theorem.** Among all **3,755** two-key replacements with matched distance **6**, **676** can cover every demand and **3,079** fail the complete demand-coverage mask. For every one of the 676 coverable cases, exact optimization of distinct nonempty **ordered, signed six-axis native prefixes** yields minimum cost at least **92**. The minimum 92 occurs exactly once, at deterministic index **179**, deleting `(5,3,1),(5,4,1)` and inserting `(6,2,1),(7,2,1)`. The three 94-prefix cases are indices 228,269,293; two 96-prefix cases are 229,290. No distance-six candidate improves the existing 84-prefix construction.

Combining EC49FLB (all distance <=4) and EC49FLC (distance 5), **all 7,797** two-key replacements within matched distance <=6 are classified: **1,559** coverable and **6,238** noncoverable. The minimum coverable replacement cost is 84 at the unique previously identified distance-four key set. The unrestricted seven-key minimum retains the explicit upper bound `C_min(7)<=84` and is open.

## Complete enumeration and exact finite proof

`MAKE_EC49FLD.py` uses the unchanged frozen catalogue generator `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`. It reconstructs each lawful word's observer label, full raw cache key and literal ordered signed-X6 microstep bytes, enumerates each distinct pair of deleted/added keys exactly once, checks both bijective L1 matchings and filters by the full 24-label union mask. Feasible cases are deterministically sorted by `(first_signed_step_root_count, removed_pair, added_pair)`, including 299 cases with three roots and 377 with four roots.

For each key set, retain all lawful words whose *complete* raw key is in the seven-key set. Group paths by their first signed native microstep, build literal native prefix tries, and use exact integer min-plus DP over the demand-subset masks of all descendant paths. Each selected nonempty prefix incurs unit cost, and child demand subsets combine by bitwise union. Convert exact-mask to at-least-mask cost, then enumerate all assignments of 24 labels to eligible first-step roots and minimize the summed costs. Different first signed roots have disjoint nonempty prefixes. Every legal word cover induces such an assignment, and every DP assignment yields legal words, establishing exactness over the declared finite universe. Terminal displacement is never substituted for path identity.

The original EC49FKY C++17 exact solver `../EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` was compiled with `g++ -O3 -std=c++17` and executed on **all 676** cases: 0–298 in one completed run, 299–658 in completed 40-case disjoint batches, and 659–675 in completed one-case runs after an interrupted combined attempt. The interrupted batch contributes no duplicate results. `COSTS_EC49FLD.json` records all 676 optima in deterministic order; `EXACT_SUMMARY_EC49FLD.json` records the exact histogram and scope.

A separate Python standard-library native byte-prefix subset-DP checker `VERIFY_EC49FLD_INDEPENDENT.py` independently checked indices **0,179,228,269,293,299,458,675**; each matched the C++ integer optimum. Independent Python checks cover eight selected cases, while C++ covers all 676.

## Reproduction, evidence and next work

Run `python MAKE_EC49FLD.py` to generate `EC49FLD_CASE_INDEX.json` and `EC49FLD_CASES.txt`. Compile the unchanged EC49FKY C++ source and run its solver over the latter file, comparing its 676 ordered integer minima to `COSTS_EC49FLD.json`. Run `python VERIFY_EC49FLD_INDEPENDENT.py` for eight separate cross-checks. Full nontruncated execution logs and regenerated cases are in the independently packaged local evidence; generator, source, complete costs and exact evidence summary are preserved in GitHub.

**Next:** classify the distance-seven two-key shell, test longer-range/multikey alternatives and seek a lawful 83-prefix seven-key construction. Preserve native microstep order, sign, branch provenance, complete raw keys, 24 labels and the frozen science. Formal claim, Result and independent mathematical review require their own native authority.
