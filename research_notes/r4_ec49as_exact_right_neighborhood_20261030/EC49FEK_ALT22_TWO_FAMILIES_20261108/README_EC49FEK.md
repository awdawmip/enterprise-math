# EC49FEK — Two new 22-word BRC quota families exclude native-prefix cost ≤93

Date: **2026-11-08**. Status: **author-side finite exact calculation and lower-bound proof; independent Driver admission pending**. Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Prior EC49FEJ exact 94 theorem: `64b2b4a34e33c849e937dbf46df90a70c5d58ef2`, PR #1730. Original native signed-X6 primitives, full positive-BRC keys and nine-state DFA are preserved.

## New exact finite theorem

For each horizon H2..H9, require true ordered signed-X6 endpoint `+2E1`, original nine-state rank-nine observation clauses, and the specified **distinct words by observer signature**. A **high** horizon has 2 words with signatures `(16,32)`; a **low** horizon has 4 words with signatures `(1,2,4,8)`. Across 22 total words, allow at most five complete positive BRC keys `(x,y,z)`, freely mixed within each horizon. Native cost is the union of distinct nonempty ordered signed-X6 step prefixes.

For **each** of these two alternate quota families, every legal full system has native cost **at least 94 edges**.

| Family | High horizons | Low horizons | Inventories (complete product) | Quota-feasible | Lower-bound ≥94 | Infeasible |
|---|---|---|---:|---:|---:|---:|
| F8 | H3,H4,H6,H8,H9 | H2,H5,H7 | 2,304 | 2,304 | 2,304 | 0 |
| F5 | H3,H4,H5,H6,H9 | H2,H7,H8 | 768 | 432 | 432 | 336 |

Thus these **3,072 new inventories** contribute 2,736 feasible cases ruled out for the ≤93 target and 336 infeasible cases. This is a lower-bound exclusion in the two stated models, not proof either family attains 94. Every feasible inventory has an explicit lexicographic complete 22-word witness. The least *lexicographic witness* costs are **106** (F8) and **171** (F5), not certified optimum costs.

Together with EC49FEJ's distinct H3,H4,H6,H7,H9 family of 1,728 inventories (exact optimum 94), the three analysed 22-word families comprise **4,800** inventories, with **4,464 quota-feasible** and 336 infeasible. The remaining 12 possible high-horizon choices H4..H9 are not claimed resolved.

## Mandatory complete-key accounting

The native operator-count identity says that every word of high signature at horizon `h` has complete positive key satisfying `x+y=h+1`. Distinct high horizons require distinct full keys. At H2 the four compulsory low words `ce,ec,de,ed` all require key `(3,1,1)`. In a minimal 22-word regime with five high windows and ≤5 complete keys, H3 must therefore be high; otherwise H2 consumes a sixth key not supplied by the five later high horizons. H3 has its unique high key `(3,1,1)`.

The high-key family sizes are H4:2, H5:4, H6:6, H8:12, H9:16. F8 therefore has `2×6×12×16=2,304` possible complete inventories and F5 has `2×4×6×16=768`; these Cartesian products are exhaustive for the declared horizon pattern. Complete triples are retained throughout, not hashed or projected partial keys.

## Exact integer lower bound

The four H2/H3 early word variants each have **42** native-prefix edges; their union `U` has **54**. For every inventory `K`, give all prefixes in `U` free of cost. This deliberately relaxes the real early choice. For each of the **16** required later `(h, signature)` groups, enumerate **every** legal primitive word over any of the five complete keys.

At native step-depth `d`, retain a signature group only when *every* candidate word has at least `d` native steps. Every real system must cover each retained group by the native prefix of its chosen word. Remove groups already covered by free prefixes at that depth. For all remaining groups compute the **exact minimum number `m_d(K)`** of distinct depth-`d` prefixes needed, using integer bitmask set-cover DP. Depths are optimized independently, another lower-bound relaxation. Hence for every full valid system `W`:

```text
C_native(W) >= 42 + Σ_{d>=1} m_d(K).
```

The program stops a case when the partial integer lower bound first reaches **94**, which is sufficient to exclude ≤93 since all remaining terms are nonnegative. F8: **2,304/2,304** inventories reach ≥94. F5: **432/432** viable inventories reach ≥94; the other 336 fail a required signature-pool presence check. There is no floating point in the exhaustive cover computation.

## Actually executed audits and source

Author-side local execution completed four disjoint F8 partitions (indices `0:576`, `576:1152`, `1152:1728`, `1728:2304`) and all F5 indices `0:768`. All 3,072 records include the complete key inventory, computed partial-depth cover vector and stop depth or infeasibility status. Actual executed independent native witness audit: **2,736 complete 22-word systems**, checking **60,192 words** for original signed-X6 endpoint, positive BRC key, nine-state DFA signature and exact native-prefix union. An independently coded **SciPy/HiGHS binary MILP** solver matched the integer-DP counts on **152 selected depth-cover subproblems**. The MILP audit is corroboration; full case coverage is provided by the exact integer-DP loop.

A compact reproducible Python source file `EC49FEK_REPRODUCE.py` is adjacent. It consumes **unchanged EC49FEJ** pinned modules `EC49FEJ_SIEVE.py`, `EC49FEJ_CONSTRUCT.py` and `EC49FEJ_DEPTH_FILTER2.py` from the predecessor evidence archive (same PR). Run partitioned:

```bash
python EC49FEK_REPRODUCE.py F8 0 576
python EC49FEK_REPRODUCE.py F8 576 1152
python EC49FEK_REPRODUCE.py F8 1152 1728
python EC49FEK_REPRODUCE.py F8 1728 2304
python EC49FEK_REPRODUCE.py F5 0 768
```

The full executed author-side source, all raw 3,072 case records, independent checker and MILP samples are also packed as `EC49FEK_complete_evidence.tar.xz` with SHA-256 `f38e30e972710180093530a842543d35e4599bc12e192e63858f214c25fd3f61`. This archive is available as the original conversation attachment; this repository folder holds the readable theorem and reproducible algorithm. Exact reproduction of the predecessor module semantics and immutable pin is required; no missing-archive claim is a completed reproduction.

## Next EC49FEL

Inspect the remaining 12 possible five-high-window 22-word signature families, using time-bounded and restartable exact depth-cover partitions. The attempted third family H3,H4,H5,H7,H9 did not complete within this author run and has **no conclusion** here. When the depthwise lower bound remains below 94, solve a joint-prefix 0–1 optimization and validate any 93-edge explicit witness. The parent objective remains: **at most five complete BRC keys and at most 93 signed-native prefix edges**. Larger quota families can be explored as distinct research routes.

## Authority

Original science input is frozen; current normative policies, P000 and ACTIVE worldview were separately read. This work is **author-side**. The private Site-bound gateway currently reports `research_authority_granted=false`, and a task inventory read does not confer a live CLAIM. Source Result and independent Driver mathematical acceptance remain pending; no protected worldview or Foundation modification is requested.
