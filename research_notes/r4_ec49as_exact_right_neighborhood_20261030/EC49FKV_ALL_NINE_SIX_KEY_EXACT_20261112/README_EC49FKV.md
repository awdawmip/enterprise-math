# EC49FKV — Exact solver-free optimum for all nine residual six-cache-key BRC problems

Date: 2026-11-12. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Model: original nine-state BRC transitions, 24 precise observer labels, ordered signed-X6 native microsteps, full raw cache-key identity. Research status: author-side exact finite certificate, independent Driver review pending.

## Theorem and complete counts

For all nine residual six-key sets K0..K8 from EC49FKQ, the **exact** minimum number of distinct nonempty ordered signed-X6 prefixes is now independently certified with finite, integer-only **prefix-trie dynamic programming**. No MIP/HiGHS status or float tolerance is used to establish the new lower bounds.

| Six-key set | Legal words | Literal prefix nodes | Exact min | Root05 cost | Root06 cost | Root07 cost | Best nonempty root07 allocation |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 4366 | 19962 | **98** | 49 | 49 | 38 | 106 |
| 1 | 5578 | 26704 | **98** | 49 | 49 | 38 | 106 |
| 2 | 5578 | 26704 | **98** | 49 | 49 | 38 | 106 |
| 3 | 4366 | 19962 | **98** | 49 | 49 | 38 | 106 |
| 4 | 6828 | 42024 | **112** | 56 | 56 | 46 | 120 |
| 5 | 8170 | 46278 | **112** | 56 | 56 | 46 | 120 |
| 6 | 6142 | 39100 | **112** | 56 | 56 | 50 | 120 |
| 7 | 6828 | 42024 | **112** | 56 | 56 | 46 | 120 |
| 8 | 6142 | 39100 | **112** | 56 | 56 | 50 | 120 |

The previously published 24-path witnesses in EC49FKQ attain every displayed optimum; they were rechecked by its original independent BRC witness verifier in this run. This removes the MIP optimality-report dependency for *all nine*, including the previously open integer cases 1 and 2.

The other 1,995 of 2,004 possible six-key combinations were excluded in the earlier six-key cover classification. Combined with that existing classification, ≤6 full cache keys cannot attain 93 prefixes. The **seven-key** global mother problem `C_min(7) ?= 94` remains OPEN.

## Complete mathematical reduction

Enumerate precisely the 178,850 frozen legal (observation-label, operation-word) pairs. For a fixed six-key set, keep exactly the candidates with an allowed complete raw cache key. Expand each into its *ordered signed* microstep byte string and insert each into a native prefix trie, counting one for every distinct nonempty byte prefix.

For every residual K_i, the complete candidate trie has exactly three first signed microsteps, encoded by 05, 06, 07. Subtrees under these first-byte roots share **no nonempty prefixes**. Root05 can meet exactly a fixed 12-label set A; root06 exactly its disjoint 12-label complement B; and root07 can meet eight labels C contained in A∪B (four in each). All this is verified by actual enumeration of every legal candidate and its exact native byte prefixes.

For root r, define `g_r(D)` as the least count of its native prefixes required to satisfy *at least* the demanded label subset D. This is calculated exactly by an integer subset-mask DP on the **complete trie**: a terminal is either not selected or is selected (covering its observer mask); child costs add over disjoint child subtries and coverage masks combine by bitwise OR; every selected nonempty ancestor contributes +1; finally allow superset coverage by downward superset closure. This recurrence enumerates every finite selection of legal terminal words, and costs precisely the native prefix-union cardinality.

Every complete solution can assign a subset T of the eight labels to root07, the other required A labels to root05 and other B labels to root06. Conversely three selected local optimal covers for such a T concatenate into a valid global cover with additive costs. Thus exactly

```
C_min(K_i) = min_{T subset C} [g_05(A\T)+g_06(B\T)+g_07(T)].
```

There are only 2^8=256 allocation masks and local DP state spaces at most 2^12=4096. C++17 and an independently implemented Python checker both computed **all 9×256=2,304 allocation costs**, with exact entry-for-entry agreement. For each case the *unique* optimum is T=empty. Every nonempty T is at least 106 in cases0–3 and 120 in cases4–8. Hence the exact minima are 49+49=98, or 56+56=112.

## Exact BRC symmetry theorem

The operations admit an involution `c↔d, f↔g, a/e fixed` with nine-state relabeling `(0,1,3,2,5,4,7,6,8)`, signature relabeling `1↔4,2↔8,16↔32`, and raw-key transform
`(x,y,z) -> (y+2z,x-2z,z)`. The six literal signed microstep operation codewords are prefix-free and have the same pairwise LCP lengths before/after this involution. Therefore *all* concatenated BRC words preserve native prefix-union cardinalities. The full 178,850-word legal catalogue is mapped bijectively to itself. The resulting six-key-case orbits are `(0 3), (1 2), (4 7), (6 8), (5)`. A separate full-catalogue checker verifies the state, observation, raw-key and word assertions.

## Reproduction and evidence

Files in this directory:
- `MAKE_INSTANCE_ALL.py` reads the *original frozen* generator at adjacent `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`, emits each legal candidate as a demand number and *literal signed byte string*.
- `EXACT_SPLIT_DP.cpp` independently optimizes complete native prefix tries with exact integers; emits all 256 allocation costs for each set.
- `VERIFY_PYTHON_INDEPENDENT_ALL.py` regenerates the full frozen BRC catalogue and independently implements the subset-mask trie DP.
- `VERIFY_INVOLUTION.py` verifies the global BRC involution over all 178,850 legal words.
- `EXACT_REPORT_EC49FKV.json` contains all per-case cardinalities, exact results, root subproblem minima and checksums of all allocation vectors.
- FKQ's previously committed `MIP_WITNESS_i.json` and `VERIFY_EC49FKQ_WITNESSES.py` are the independently checked primal upper bounds.

To reproduce, execute `python3 MAKE_INSTANCE_ALL.py 0 > input0.txt` for all i=0..8; `g++ -O3 -std=c++17 EXACT_SPLIT_DP.cpp -o exact_split`; run `./exact_split < input0.txt` and similarly for other cases; then `python3 VERIFY_PYTHON_INDEPENDENT_ALL.py --write-costs` and `python3 VERIFY_INVOLUTION.py`. Compare all 256 C++ allocations to each Python case's allocation_costs array; every entry matched in the author's actual run. Both exact optimizers are non-floating and do not call an MIP solver.

## Source and scope

Frozen pin unchanged: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Predecessors: EC49FKQ, FK R, FKS, FKU within Draft PR #1730. True research session: `EM-DIRECT-483170 / TASK_RESEARCH`; Activity `RA-2267F5C9DF4148DEC7029CB7`. Native `EC49AS` task query returned `NO_CURRENT_IMMUTABLE_PUBLICATION`, while the fair dispatch selected unrelated `RS-X6-LEGACY-PLANE-RECONCILIATION`. No unrelated CLAIM or Result was asserted. This is a durable **author-side** mathematical theorem, pending independent Driver review. P000 and ACTIVE worldview remain unchanged.

Next discriminating research action: global **seven-cache-key 93-prefix** search/certification, using the verified native-root partition and exact full-key combination/observer coverage, with complete candidate-set and bound accounting.