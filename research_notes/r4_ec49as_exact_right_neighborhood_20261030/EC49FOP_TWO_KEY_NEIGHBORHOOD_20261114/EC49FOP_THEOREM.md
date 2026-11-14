# EC49FOP — Exact radius-two native signed-prefix BRC observer census

Date: 2026-11-14. Status: AUTHOR_EXACT_FINITE_CHECK / NOT_REVIEWED.
Continues EC49FOO [PR #2411](https://github.com/awdawmip/enterprise-math/pull/2411), and EC49FON [PR #2406](https://github.com/awdawmip/enterprise-math/pull/2406).
Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Raw input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, `master_and_radius3_cases.txt`; 94 original inventory keys, 24 named demands, four named roots 03/05/06/07.

## Finite target, definition and finding

Freeze baseline seven inventory keys `(0,4,5,11,37,39,81)`, original case 32315. Select exactly two distinct outgoing keys from these seven and exactly two distinct incoming keys from the other 87 keys, without ordering the chosen pairs. There are exactly
```
C(7,2)*C(87,2) = 21*3741 = 78561
```
candidate substitutions. A candidate is retained if **every one** of the 24 named demand-to-root eligibility sets is unchanged, using actual frozen native signed-prefix key words; this leaves **341** cases, partitioned by outgoing pair:
`(5,81):1, (11,81):3, (37,39):7, (37,81):185, (39,81):145`.

For a root r and optional demand subset S, the cost `D(K,r,S)` is the exact native prefix-trie minimum node cover cost for root r's mandatory named demands together with S; it is computed by union-mask dynamic programming and exact superset closure (as in EC49FOO), preserving branch names and signed-prefix identities. The accessible rooted profile has **168** integer costs: 16+8+16+128 for roots 03,05,06,07. For every legal complete named allocation rho, the exact total cost is `C(K,rho)=sum_r D(K,r,S_r(rho))`. There are precisely `2*2*2*3*3*3*3=648` legal complete allocations.

**Finite proposition.** Among all 341 preserved-eligibility, exactly-two-key replacements of the stated baseline, each has at least one accessible rooted cost different from baseline and at least one legal complete allocation with total cost different from baseline. Thus there are **zero** native global nonzero all-assignment hub-cancellation gauges on this exact radius-two neighborhood.

The author program exhaustively verifies `341*168=57,288` rooted-profile comparisons and `341*648=220,968` legal complete-allocation comparisons. Of these, **204,300** complete-allocation totals change. **99** replacement pairs have at least one particular assignment where nonzero root deltas exactly cancel; total such assignment-specific cancellations = **4,728**. Those are real signed integer cost differences, not claims of global equality.

## Newly discriminating native witness

The unique retained substitution outgoing `{5,81}`, incoming `{1,10}`, results in signed-prefix keys `(0,4,1,11,37,39,10)`. Its rooted cost differences occur on 8 accessible coordinates for root 05 and 6 for root 06; roots 03 and 07 remain unchanged. Exactly **594/648** complete allocations change total cost, and **54** exhibit genuine nonzero-root exact compensation.

Independent reconstruction from the frozen raw source by a separate Python prefix-trie DP (without using the C++ output in its computation) verified all 168 root costs on both source and substituted inventories (336/336 exact C++ agreements), and all 648 allocations. An explicit compensated allocation is:
```
5->05, 7->07, 13->07, 15->03, 17->06, 19->03, 21->03
delta_root(03,05,06,07)=(0,+2,-2,0)
delta_total=0
```
This is a concrete two-key native compensation outside the earlier 51-case inventory; it is distinct from the one-key 37->62 witness in EC49FOO.

## Proof and reproducible finite coverage

A two-level loop enumerates each outgoing pair `i<j` of seven selected keys and each incoming pair `a<b` of the complementary 87; every unordered replacement set is visited once. It then compares all 24 exact named eligibility masks against the baseline. Each of the 341 passing cases enters the same native named signed-prefix trie DP; one root cost table is constructed over mandatory and optional label masks using exact integer operations. All 648 complete allocations are then exhaustively evaluated with the same frozen eligibility domains.

Because the filter is exact and the candidate-pair enumeration covers all combinations, the 341-way classification is an exact finite statement under the pinned input/operator. The implication equal accessible rooted profiles => equal terminal totals is algebraic. The reverse statement for this neighborhood is author-checked by zero observed exceptions.

The full native generator `VERIFY_EC49FOP_NEIGHBOR_EXTRACT.cpp` was run with C++17 `-O2`. The first execution produced the first 325 configurations before local resource termination; the remaining 16 were produced by the saved `VERIFY_EC49FOP_NEIGHBOR_RESUME.cpp` that executes the identical loop for indices >=325. The two outputs were assembled into **57,457 lines including header** and validated for unique (swap,root,mask) keys and exact 342 configurations including baseline. The classifier `VERIFY_EC49FOP_341.py` generated the full 341-row table and result JSON. The independent Python implementation reconfirmed the selected native witness.

The raw input, complete 57,456-root-cost data rows, exact classifier, independent reproduction, command outputs, 341-row result file and SHA256 manifest are preserved in the companion author evidence archive `EC49FOP_TWO_KEY_EVIDENCE_20261114.tar.xz`. The project GitHub submission stores the full proof and executable source/summary; if the large computed tables are not mirrored here, the archive is the additional data carrier. No floating point and no classical pi/trigonometric/matrix-expansion fallback was used.

## Status, owner scope and next discriminating unit

At `2026-11-14T11:35:01.916809+00:00`, exact control request `r4-ec49fon-current-task-20261114-1933-v1` confirmed RS-EC49AS has no canonical published-task directory (status `NO_CANONICAL_PUBLICATION_DIRECTORY`, execution_authorized=false; scientific_work_rejected=false). Historical researcher `EM-DIRECT-204C14` and Activity `RA-6893088D0A7347CE7F4D8720` are author attribution only; this independent portable work does not create CLAIM/Result/Review or alter protected task state.

Next: characterize a **specific** signed-prefix operator obstruction that excludes the 11-dimensional abstract hub kernel within one-/two-key fixed-domain neighborhoods, or expand to 3+ simultaneous substitutions and test whether an exact nonzero, all-allocation cost gauge appears while retaining the original full signed-prefix input and future observer scope.
