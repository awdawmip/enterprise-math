# EC49FLA — Exact small-distance two-key replacement theorem near the 84-prefix BRC witness

**Date:** 2026-11-12. **Status:** AUTHOR_EXACT_FINITE_COMPUTATION, selected independent Python checks; independent Driver admission pending. **Frozen science pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Proposition and result

Keep the complete frozen nine-state, 178,850-legal-word BRC model, its 24 (window, signature) demands, raw signed six-axis native microsteps and 94 distinct **complete** raw cache keys. The 84-prefix witness EC49FKX has

`K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.

For two distinct old keys `a,b in K*` and two distinct new keys `u,v in U\K*`, define a matched coordinate replacement distance

`d({a,b},{u,v})=min(||a-u||_1+||b-v||_1, ||a-v||_1+||b-u||_1)`.

Among all **two-key replacement sets with d<=3**, the exact full-observer coverage screen has 556 candidates: 423 cannot cover all 24 demand labels even when *every* candidate word using an allowed key is admitted, and 133 are feasible. Exact native signed-prefix trie subset dynamic programming on **all 133 feasible sets** yields minimum cost **90** (one set), with every other exact optimum at least 92. Thus

```
forall K=(K*\{a,b}) union {u,v}, d({a,b},{u,v})<=3:
  K feasible => C(K)>=90;
  all such K satisfy C(K)>84.
```

This is a **strict small-distance two-key local obstruction**: the original 84-prefix construction is better than every *distinct* two-key replacement at matched distance <=3. This extends EC49FKY's complete one-key swap theorem. The unrestricted seven-key minimum remains open, with the known explicit upper bound `C_min(7)<=84`.

The 90-minimum two-key set drops `(5,4,1),(6,4,1)` and adds `(5,5,1),(6,3,1)`, yielding native first roots 05,06,07, and exact global root costs 45+45+0=90.

## Complete enumeration checks

- All unrestricted two-key replacements from the 94-key universe: `C(7,2)*C(87,2)=78,561`; exactly **6,315** pass necessary 24-label coverage, split into 2,198 with 3 distinct signed first-step roots and 4,117 with 4 roots.
- For matched distance 2: 98 candidate pairs; 22 cover all demands; 76 fail coverage.
- For matched distance 3: 458 candidate pairs; 111 cover all demands; 347 fail coverage.
- For matched distance <=3: 556 candidate pairs; 133 exact fixed-seven-key optimizations. Deterministic ordering: `(distance, number_of_first_roots, dropped_pair, added_pair)`.

## Exact cost histogram, all 133 feasible d<=3 cases

| optimum | count | optimum | count | optimum | count |
|---:|---:|---:|---:|---:|---:|
|90|1|92|1|94|3|
|98|18|100|3|102|1|
|104|31|106|6|108|4|
|110|2|112|35|114|1|
|116|13|120|3|122|1|
|124|2|130|1|131|1|
|137|1|145|1|146|4|

See `COSTS_EC49FLA.json` for all 133 ordered costs, including exact minimum case index 6.

## Proof / algorithm

1. The retained EC49FGW frozen generator enumerates all 178,850 legal (observer, operation word) pairs. Each word yields exactly one of 24 labels, its complete signed raw cache key and the exact byte string of ordered signed X6 microsteps. Recomputing complete key-to-demand bitsets and every pair-of-two-key swaps establishes the coverage counts above by finite enumeration.
2. For every covered `K` with matched distance <=3, include **all** legal words whose complete key lies in `K`. Partition them by their first signed native byte; roots are disjoint for all nonempty prefixes.
3. Apply the same exact C++17 root-trie integer/subset solver published in EC49FKY: for each root compute its minimum prefix count for every demand subset via complete terminal and subtree DP; minimize the sum over every assignment of 24 labels to eligible roots. The min-sum is attained by combining root-local word families and is a lower bound for any admissible word family by assigning each covered label to one of its roots.
4. Run every one of the 133 sorted cases with the full candidate family. The original integer solver's 133 output lines yield the ordered array and cost histogram. Six independently written Python full-native-prefix trie checks reproduce cases 3,6,14,56,95,132, including the 90-minimum case and both 3- and 4-root strata.

**Reproduce:** execute `REPRO_EC49FLA.py` in this directory to generate `EC49FLA_CASE_INDEX.json` and `EC49FLA_CASES.txt`; compile the unchanged `../EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` using `g++ -O3 -std=c++17`; run it on the generated cases, compare all 133 costs with `COSTS_EC49FLA.json`; adapt the existing independent `VERIFY_SCAN_INDEPENDENT.py` to the corresponding exact index. All arithmetic is discrete integer arithmetic; original native signed prefixes and key identities are retained.

**Source provenance:** EC49FGW frozen generator `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`; EC49FKX explicit 84 witness; EC49FKY full first-root exact solver and independent Python reference. Scientific input remains frozen at the pin above.

**Unfinished next unit:** expand the certified distance shell to 4 (277 further *covered* instances), with bounded processing and exact retained checkpoint; then search farther two-key sets or change the entire seven-key structure for a valid <=83-prefix witness. A wider d<=4 computation was initiated locally but timed out, so its partial output is not included in the theorem.

**Control/identity:** Current EC49AS native task verification and dispatch were pending as of this author computation; no formal CLAIM, Result or independent Driver acceptance is asserted. P000 and ACTIVE worldview remain unchanged.
