# EC49FKZ — Complete two-full-cache-key replacement feasibility and exact selected native-prefix optima
Date: 2026-11-12. Research mode: AUTHOR_FINITE_EXACT_COMPUTATION; independent Driver review pending. Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Statement and complete finite coverage

Work in the original frozen nine-state BRC model: 178,850 legal operation words, 24 (window, signature) observation demands, 94 distinct **complete raw native cache keys**, and ordered signed six-axis native prefixes. The starting EC49FKX 84-prefix seven-key witness has
`K0={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.

For every exact two-key replacement `K=(K0\{a,b}) ∪ {c,d}` with distinct `a,b∈K0`, distinct `c,d∈U\K0`, enumerate all `C(7,2)*C(87,2)=78,561` candidate seven-key sets. For each complete raw key `k`, define `L(k)` to be the subset of the 24 demands realized by at least one frozen legal word of key `k`.

**Exact theorem (key-level feasibility):** Of 78,561 distinct two-key replacement sets, exactly **6,315** satisfy `∪_{k∈K} L(k)=D` (all 24 demands), and **72,246** cannot satisfy all 24 demands using any legal word restricted to that key set. This is necessary *and sufficient for demand coverability* under the model's independent per-demand word-selection semantics: a key-set covers each demand if and only if one allowed legal word can be independently selected for each demand. This theorem does not optimize the shared native prefix cost of the 6,315 coverable sets.

### Complete 21 dropped-pair counts (each has 3,741 additions)

| Two old keys removed | Coverable additions |
|---|---:|
| (2,1,1)+(3,0,1) | 0 |
| (2,1,1)+(3,1,1) | 0 |
| (2,1,1)+(4,2,1) | 0 |
| (2,1,1)+(5,3,1) | 0 |
| (2,1,1)+(5,4,1) | 0 |
| (2,1,1)+(6,4,1) | 0 |
| (3,0,1)+(3,1,1) | 0 |
| (3,0,1)+(4,2,1) | 0 |
| (3,0,1)+(5,3,1) | 0 |
| (3,0,1)+(5,4,1) | 0 |
| (3,0,1)+(6,4,1) | 0 |
| (3,1,1)+(4,2,1) | 0 |
| (3,1,1)+(5,3,1) | 1 |
| (3,1,1)+(5,4,1) | 1 |
| (3,1,1)+(6,4,1) | 0 |
| (4,2,1)+(5,3,1) | 255 |
| (4,2,1)+(5,4,1) | 259 |
| (4,2,1)+(6,4,1) | 45 |
| (5,3,1)+(5,4,1) | 3,741 |
| (5,3,1)+(6,4,1) | 1,185 |
| (5,4,1)+(6,4,1) | 828 |
| **Total** | **6,315** |

Independent exact check: the separate `VERIFY_GROUPED_MASK_EC49FKZ.py` groups all 87 outside keys by their restricted demand-support masks. For each missing-demand mask M, it computes the feasible unordered added-key count by `sum_{s<t, s|t=M} f(s)f(t)+sum_{s=M} C(f(s),2)`, an independent frequency-count formulation. All 21 counts and the 6,315 total match the direct pair enumeration (`EC49FKZ_INDEPENDENT_GROUPED_SUPPORT_PASS` on the local author-side run). Run the primary verifier first to regenerate its report JSON.

There are **13** zero-coverability dropped-pair classes. Every removal of (2,1,1) together with one other starting key is coverability-impossible under any pair of incoming keys.

## Additional exact original signed-prefix cost experiments

The original EC49FKY full ordered/signed six-axis trie solver was used without changes on **15** deterministically selected coverable two-key replacements (first two feasible additions per nonempty dropped-pair class plus the combination of two previously individually 84-optimal single swaps). Their exact minimum prefix costs, in the selection order recorded in `EXACT_SELECTED_RESULTS_EC49FKZ.txt`, are
`[102,100,114,124,114,116,121,110,112,112,141,108,137,104,90]`.
Thus none of these 15 has cost <=83. The double replacement combining the previously individually cost-84 swaps
`(5,4,1)→(6,3,1)` and `(6,4,1)→(5,5,1)`
has an **exact cost of 90**, despite each individual replacement preserving the 84 optimum. This is an interaction result, not a monotonicity theorem.

A separate **400-case exhaustive lexicographic prefix** of the 6,315 coverable double swaps was computed by the same exact C++ solver: all 400 costs are >=100 (smallest exactly 100). The 400 are indices 0 through 399 of the deterministic list ordered first by removed old-key pair and then by inserted new-key pair. The remaining 5,915 coverable sets have not been exactly optimized in this work. The attempted 0..800 batch was interrupted after 400 completed records; the complete 0..400 rerun succeeded.

Three selected cases (indices 0, 1 and 14) were separately checked by the established Python full native trie subset-DP with the independent word-to-prefix construction, yielding respectively 102, 100 and 90. All results are author-side computations and await independent mathematical audit.

## Exact prefix-cost algorithm

Partition all allowed native paths by literal first signed microstep. The distinct nonempty prefixes of different root tries are disjoint. In each trie compute a bottom-up integer demand-subset DP minimizing selected nonempty nodes; combine child demand masks by OR and costs additively, charging one unit for every selected nonempty prefix. Then enumerate every admissible assignment of all 24 requirements to their compatible root tries and minimize the sum. See the previously validated, unchanged `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` and `VERIFY_SCAN_INDEPENDENT.py` in this research branch. The present enumeration constructs key sets, not approximated coordinates; all signed native prefixes remain literal.

## Reproduction, provenance and next problem

The code/data files beside this note contain the exact per-dropped-pair counts, the 15 selected exact results, and the first 400 case results. Source generator: sibling `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py` (PIN verified), matching the earlier EC49FKY author-side 193-case scan. To reproduce, enumerate all legal words and raw keys; compute `L(k)`; iterate lexicographically over the 21*3741 replacements and check bitmask union, then apply the existing exact native-prefix solver for selected cases and any further coverable cases. Distinct seven-key set is the unit; no duplicate hidden orderings are counted.

**Next smallest unfinished unit:** classify or optimize the remaining 5,915 coverable two-key swaps, prioritizing the 3,741 cases obtained by removing (5,3,1) and (5,4,1), and seek a valid <=83 prefix witness or a tight lower-bound certificate. The present double-swap feasibility theorem can be reused to prune future all-seven-key searches. No formal EC49AS CLAIM/Result or independent Driver mathematical acceptance is asserted here. P000 and ACTIVE worldview remain unchanged.
