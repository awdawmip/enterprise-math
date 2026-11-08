# EC49FEW — Universal pooled-complete-BRC-key duals exclude every H5-mixed 23-word branch

Date: 2026-11-09 (Asia/Shanghai). Status: **author-side exact finite certificate**, not an accepted Source Result or independent Driver review.

Frozen science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Research continuation: EC49FEU's exact type-B late mixed census, as read from `EC49FEU_STANDALONE_REPORT.json`; EC49FEV universal H4 technique, branch HEAD as remotely read `714a149dbf0840e28dca40b98ab0cdb9195fbbdc`. P000 and ACTIVE X6 worldview unchanged.

## Problem and theorem

The native path universe consists of **ordered signed six-axis microsteps** produced by the frozen six-operation alphabet `a,c,d,e,f,g`, with nine-state observer and native end displacement `(+2,0,0,0,0,0)`. Every operation word uses a complete, positive forward BRC key `K=(x,y,z)`. Choose at most five complete keys, possibly mixing keys among paths of one horizon. At H2 require four labels `(1,2,4,8)`, H3 two labels `(16,32)`, H5 mixed type-B triple `(1,8,16)`, and at exactly three other late horizons require two high labels `(16,32)`; the other late horizons require four low labels. There are **23 required (h,label) groups**, hence 23 paths. Count the union of all nonempty **ordered, signed microstep prefixes**, not final geometric cell positions and not unordered step multisets.

**Theorem (complete H5 type-B family, finite exact):** Every legal 23-path system meeting this pattern has `C_native >= 98`. The exact six high-horizon placements (four late high-bearing horizons, H3 always high) have the following conservatively verified bounds:

| Late high-bearing set | EC49FEU signature-feasible original full-five-key configurations | Universal pooled-key lower bound |
| --- | ---: | ---: |
| H4,H5,H6,H9 | 648 | **112** |
| H4,H5,H7,H9 | 828 | **108** |
| H4,H5,H8,H9 | 504 | **115** |
| H5,H6,H7,H9 | 4,160 | **98** |
| H5,H6,H8,H9 | 5,376 | **98** |
| H5,H7,H8,H9 | 4,296 | **99** |
| **Total** | **15,812** | **>=98** |

The other four possible late high sets (4567,4568,4578,5678) have zero signature-feasible configurations in the complete EC49FEU census. Thus all **34,344** original typed-B configurations are classified: 15,812 cost-excluded by exact dual certificates, 18,532 signature-infeasible. The original BRC involution `I=(c d)(f g)` and key map `J(x,y,z)=(y+2z,x-2z,z)` preserve signed-word prefix cost and map type B `(1,8,16)` to type C `(2,4,32)`; hence the same lower bounds apply to the corresponding 15,812 typed-C signature-feasible configurations. The type labels count branches, not disjoint underlying five-key sets. This H5-mixed result is separate from, and additional to, EC49FEV's H4-mixed theorem.

## Exact mathematical certificate

Let `S` be one of the six feasible late-high sets, `H = S union {3}`, and `K_h(A)` be the **complete finite set of positive full BRC keys** whose original observer emits all labels in `A` at horizon `h`. High label 16 forces `x+y=h+1` in the original grammar, and H3's high-pair key is uniquely `(3,1,1)`. Define the pooled eligible inventory

`K_pool(S) = {(3,1,1)} union K_5({16}) union union_(h in S\{5}) K_h({16,32}).`

Every original legal five-key inventory for this branch is a subset of `K_pool`. **We remove the five-key coupling** and allow every required group to choose freely from all pooled keys: this relaxes the original problem. Denote `W_g` all original signed operation words for label group `g` using any key in `K_pool`, and `P(w)` their set of nonempty native signed prefixes. Every required group chooses one word `w_g`.

For each branch, we provide nonnegative integer coefficients `T_(g,p)`, positive integer scale `Q=1,000,000`, and nonnegative integer `gamma_g` (23 components), such that

1. For every original signed native prefix `p`, `sum_g T_(g,p) <= Q`.
2. For every allowed original word `w` in group `g`, `sum_(p in P(w)) T_(g,p) >= gamma_g`.
3. `sum_g gamma_g` equals the branch's table lower bound multiplied by `Q`.

For every possible relaxed selection, exactly:

`Q * |union_g P(w_g)| >= sum_(p in union) sum_g T_(g,p) >= sum_g gamma_g`.

The first inequality uses per-prefix capacity, the second sums the mandatory **one-per-group** inequalities. Thus the certified integer bound applies to the *pooled* problem and therefore to the original at-most-five-key problem. No solver optimality assumption is used: each finite inequality is checked using exact Python integers after exhaustive original grammar enumeration.

## Actual execution and verification scope

The local `late_mixed_dual.py` uses SciPy/HiGHS only to find coefficients. `VERIFY_EC49FEW.py` independently reads the saved coefficients and verifies all 23 group inequalities, every candidate original signed operation word, its six-axis endpoint and positive full BRC key, every prefix capacity, and the exact integer conclusion. Its checker does not import NumPy/SciPy or trust LP solver success. All six certificates returned `EXACT_INTEGER_PASS` in `EC49FEW_VERIFICATION.jsonl`.

Verified per-branch original pooled-word counts: `78,413; 73,585; 48,455; 71,233; 46,935; 32,659` (351,280 total). Verified group/prefix indexed pairs: `467,882; 432,537; 268,920; 416,891; 258,947; 181,190` (2,026,367 total). Nonzero exact dual coefficients: `381,908; 348,181; 182,541; 353,657; 185,923; 111,410` (1,563,620 total). Counts are summed over separate pools and are not asserted unique across branches.

Run from the expanded archive's common directory:

`python3 VERIFY_EC49FEW.py UNIVERSAL_H5_4569.json UNIVERSAL_H5_4579.json UNIVERSAL_H5_4589.json UNIVERSAL_H5_5679.json UNIVERSAL_H5_5689.json UNIVERSAL_H5_5789.json`

The full evidence archive contains the six unrounded integer coefficient files, verifier, enumerator and original model files, JSON summary and actual output. The small repository synopsis alone is not a substitute for the full coefficients; retain the archive if extracting or cross-checking numerical certificates.

## Scientific interpretation and next question

Within the specified finite 23-word H5 mixed type-B/C family, 93 edges are excluded, **even with the relaxed larger pooled key inventory**. The mother objective remains a complete native X6 solution with at most five full BRC keys and `C_native <=93`; an existing 22-word example with 94 is still the better known bound. Next work: run pooled-key exact duals over H6/H7/H8 mixed placements from the unchanged EC49FEU census; retain potential survivors for original five-key-coupled optimization. Keep mother objective, independent Driver mathematical review and current Source task CLAIM state separate.

## Source and control state

Author-side activity: `EM-DIRECT-4FB3A8 / TASK_RESEARCH`, `RA-9854AC2E5AA8BFD1F95D7C37`, newly issued and Source-verified this turn. `execution_authorized=false`; no formal CLAIM or native Result is asserted. The attached archive and reproduced integer checks are research evidence, not an official Driver admission. Avoid changing original P000, ACTIVE worldview or the frozen science pin.