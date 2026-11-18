# R5 — Twenty-four further exact nine-state f=8 quotient classes (2026-11-19)

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Scoped to the pinned integer-center scalar observation game; portable standalone research, not formal Task CLAIM/RUN, independent Review, or native X6 state equivalence.

## Exact scientific premises and predecessor

- Science pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Original input: `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.
- Fixed seven named states: `H=(18,24,82,34,17,144,208)`. Additional pair `x<y` disjoint from H; independent ordered nine-slot counters `(18,24,82,34,17,x,144,208,y)`.
- There are 101 physical query budgets `k=214,...,314`, with cost k. Correct scalar observation y satisfies `|y-N_h(k)|<=tau/2`. Up to eight arbitrary unmarked errors.
- Fifth noise interval `L=25845652773852463277015040000 <= tau < U=58182461585441404127941754880`.
- Predecessor: 26 exact U-1 quotient classes/5,383 pairs, at `047036218649faaef1f72ad0d81d509268aab405`; 20 further classes/3,560 pairs at `37e03bc916c6a3d4afb5dae037c288589bc0022f`. Their 46 completed classes were excluded from this run.

## New finite theorem

For every unordered pair `x<y` in any of the **24 additional complete U-1 observation-signature classes** listed in `RESULTS_NEXT24.csv`, and every real `L<=tau<U`:

```
C_8(H union {x,y}; tau) = 8335.
```

These classes include 2,847 unordered pairs. Together with 46 predecessor classes, **70 of 2,026 classes and 11,790 of 30,876 pairs (38.19%)** now have exact f=8 certificates. **1,956 classes and 19,086 pairs** remain for this nine-state family. The full 256-state interval bound remains `8335 <= C_8^* <= 8343`.

## Exact proof and verification

For any action, the correct-response support masks are all maximal center-rooted windows of width tau on its nine integer centers; each starting center gives one candidate and every maximal nonempty window is so represented. Classes are equal iff their complete ordered 101-action maximal-support signatures are identical. Enumerating all 30,876 pairs and sorting groups by smallest representative gives exactly 2,026 U-1 classes. The 24 group IDs in the CSV are zero-based indices in this partition, selected among *unsolved* classes by descending class size then increasing group ID.

A separate doubled-observation-endpoint sweep checks that the window supports coincide with direct interval intersections for all 24 representatives and 101 actions: **2,424 exact integer crosschecks passed**.

Bellman recurrence on separate named counters `e_i in {0,...,9}` (9=eliminated):

```
V(e)=0 if at most one state survives;
V(e)=min_k { k + max_{maximal S} V(T_S(e)) } otherwise,
T_S(e)_i=min(9,e_i + 1[i not in S]) for live slots.
```

The cheapest physical budget represents each identical full support family. A positive-cost action with a no-progress branch is excluded from the unrestricted finite-cost minimization. `EXACT_NINE.cpp` uses exact integers and memoization. All **24** jobs returned `EXACT cost=8335`, exit code 0, with no 12-million-memo-state cutoffs; input SHA-256, actions, memo sizes and representatives are in the CSV. The independent previously certified eight-state subset of each nine-state problem has cost 8335 throughout [L,U), supplying the lower bound. The upper bound follows from the exact U-1 computation, integer-center response monotonicity and `tau<U`.

## Evidence and reproduction

The CSV contains all 24 group IDs, representatives, class multiplicities, Bellman costs, memo counts, retained action-family counts and SHA-256 of exact stdin input for each minimax run. Source implementation `EXACT_NINE.cpp` is provided in the same folder. The original pinned table is intentionally reused rather than duplicated. Complete author-side bundle also contains `partition.py`, `partition_2026.json`, `solve_more.py`, `results_next.json`, `VERIFY_R5_NINE_NEXT24.py`, and SHA-256 manifest.

Verification summary: `PASS_R5_NINE_NEXT24_CLASSES class_count=24 pairs=2847 cumulative_classes=70 cumulative_pairs=11790 support_crosschecks=2424`.

## Next discriminating problem

Search the remaining 1,956 classes using nine-state action-dominance or joint-interference invariants rather than brute-force class size alone. An exact nine-state U-1 value exceeding 8335 would improve the full-256 lower bound at that endpoint. An alternative path is a full-256 adaptive strategy of cost at most 8342. Keep observation-signature quotient separate from native X6 identity; independent mathematical Review remains NOT_REVIEWED.
