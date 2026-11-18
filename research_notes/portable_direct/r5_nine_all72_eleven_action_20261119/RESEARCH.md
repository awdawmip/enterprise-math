# R5: complete 11-action nine-state signature stratum, 72 exact classes

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is independent portable research in the frozen integer-center scalar-observation game; no new formal CLAIM/RUN, driver review, or native-X6 identity assertion.

## Frozen source and predecessor

- Source science commit: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Reused immutable `EXACT_R5_ALL_101_BUDGETS.json`: 1,549,048 bytes; SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. This input is not duplicated in the repository artifact.
- Seven fixed named states: `H=(18,24,82,34,17,144,208)`. Additional unordered pair `x<y` outside H; canonical nine-slot order `(18,24,82,34,17,x,144,208,y)`. Each named slot retains an independent error counter.
- 101 physical query budgets `k=214,...,314` at cost `k`; integer response centers `N_h(k)`; correct response is any scalar within distance `tau/2` of its center; at most `f=8` arbitrary unmarked errors.
- Fifth noise interval: `L=25845652773852463277015040000 <= tau < U=58182461585441404127941754880`.
- Exact predecessor: historical 110 of 2,026 nine-state complete `U-1` support-signature classes, containing 15,203 of 30,876 unordered pairs; details `a1de7393dc8991e7729e682ce80f79cade7cb170` and `bfd1423c9d0c6e6f229a2802e9ffed5e8c6e2344`. The latter fixes NEW20 slot-hash provenance.

## New scoped finite theorem

Among the 1,916 previously unsolved signature classes, **exactly 72** have **11 distinct cheapest physical action families** at `tau=U-1` (the other 1,844 have 9 or 10). For every one of those 72 full classes, each represented unordered pair `{x,y}`, and every real `L <= tau < U`,

```
C_8(H union {x,y}; tau) = 8335.
```

The 72 classes contain **288 distinct pairs**. All 72 original integer Bellman root computations independently returned `8335`, with at most **1,912,889 memoized states** in any solve. Two response-support constructions agreed on **14,544** checks (72 representatives x 101 budgets x 2 noise endpoints). There were no failed, cutoff or timeout roots among the final 72 completed cases. The root cost `8335` of this nine-state family is not a new full-256 optimum claim.

**New cumulative coverage:** 182/2,026 signature classes and 15,491/30,876 unordered pairs (50.17%) now have historically reported exact cost 8335. Remaining 1,844 classes / 15,385 unordered pairs are not covered by this theorem. The established complete-256 interval bound remains `8335 <= C_8^* <= 8343`.

## Exact proof

For the nine integer centers of physical budget `k`, a correct-response support is a subset `S` of slots whose closed observation intervals have common intersection. Equivalently, `max_{i in S} N_i(k) - min_{i in S} N_i(k) <= tau`. It suffices to enumerate all maximal windows beginning at each distinct observed center; they contain every maximal correct-response support. The independent verifier also enumerates doubled-coordinate interval endpoints and intervening midpoints, retaining inclusion-maximal masks. Both constructions agree at `tau=L` and `tau=U-1` for all the reported representative/action pairs.

For each candidate pair, enumerate its **ordered nine-slot support family at each of the 101 physical budgets**. Two pairs belong to one `U-1` signature class exactly when their 101 ordered mask-family sequences coincide. The group classification enumerates all `C(249,2)=30,876` pairs; the original partition contains 2,026 classes and the prior 110 classes are subtracted by explicit IDs. Exactly 72 remaining classes have 11 distinct families when actions with identical family are replaced by the least-cost physical budget. At `U-1`, every pair in each class has the same Bellman state system and value as its representative: equivalence changes neither the nine named slots, available action costs, nor their transition masks.

At a counter vector `e_i in {0,...,9}` (9=excluded), for correct-response mask `S` define `T_S(e)_i=min(9,e_i+1[i not in S])` for live slots. The exact minimax recurrence is
```
V(e) = 0                                             if at most one live slot;
V(e) = min_k [ k + max_{S in supports(k)} V(T_S(e)) ] otherwise.
```
Positive-cost actions whose branch leaves the current state unchanged are safely removed **only in this unrestricted Bellman minimum**. Memoization over finite counter vectors then gives each recorded `C_8=8335`. The 8-state/five-state predecessor supplies `C_8(H; tau) >= 8335` for every `tau in [L,U)`. Inclusion of two additional named hypotheses cannot reduce worst-case value. Finally, enlarging the noise interval cannot improve minimax cost, so for `tau <= U-1` the nine-state value is at most its computed `U-1` cost 8335. For `U-1 <= tau < U`, all centers are integers and maximal support relations are unchanged. Thus lower and upper bounds coincide across the full real interval.

This conclusion **does not assume that the `U-1` equivalence partition remains identical at smaller noise diameters**; the monotonicity argument is what extends each class's cost.

## Reproduction and evidence

- `RESULTS_ALL72.csv`: all 72 canonical representatives, group IDs, multiplicities, exact cost, memo count, exact solver-stdin SHA-256 and original evidence batch `FULL` or `LOG`.
- `REPRODUCE_R5_ALL72.py`: reconstructs each exact solver input from the frozen table and validates its digest, maximal-support families and the supplied result table; optional `--solve` re-executes the exact C++ Bellman solver for all 72 cases.
- `EXACT_NINE_V2.cpp`: original integer Bellman implementation, with `12,000,000` memo limit, positive action cost, and strict named-slot error counters.
- Source execution transcripts: first 27 root results retained in the complete local JSON, middle 28 exact `DONE gid OK 8335 memo` lines preserved as observed stdout, final 17 full records saved immediately in JSONL. The CSV's `LOG` provenance marks the middle 28; reconstructed input SHA-256 and counts are corroborative, not fabricated original C++ stdout.
- Original execution used `g++ -O3 -std=c++17`; the full 72-root suite was completed in three bounded batches. Group IDs and class sizes are from the exact existing partition. Independent support comparisons cover all 72 x 101 x 2 cases; root solves were performed at `U-1`.

No source-state merging of different named hypotheses is used. This is an exact observation-equivalence quotient for the explicitly declared finite scalar game, preserving all joint response families and independent error counters; it does not discard native six-axis relational directions. Reusable BRC-type observer discipline is applied at the support/response-carrier boundary, but no new BRC native operation is claimed.

## Control and remaining work

The original R5 researcher provenance is `EM-DIRECT-4C3E47`, Activity `RA-F2257922D00B2FE4C4818DBD`. A new read-only owner query `r5-20261119-followup-owner-check-20261119-01` conclusively failed `SOURCE_TREE_BLOB_SIZE_INVALID`; its failure was preserved and not replayed. The last verified historic owner snapshots had no R5 active CLAIM; the current owner projection was not refreshed successfully. Independent portable-file publication uses the already authorized GitHub route, without claiming any current formal RUN.

**Next discriminating science:** analyze the remaining 1,844 nine-state classes (9 or 10 distinct action families) for strict lower-bound certificates over 8335, and independently investigate a complete-256 strategy with worst-case cost <= 8342. Reuse the present 72 certificates rather than repeating their root solves. Independent review: `NOT_REVIEWED`.
