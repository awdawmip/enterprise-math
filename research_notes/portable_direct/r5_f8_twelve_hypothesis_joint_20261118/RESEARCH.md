# R5 fifth noise chamber: a twelve-hypothesis joint minimax certificate

Date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Scientific setting and immutable provenance

This is a derived *scalar integer-center observer* of the Enterprise Math R5 model, not an identification of full native P000/X6 joint paths. Frozen scientific code/semantic pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Source: the 101-by-256 exact integer table `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, retained in the already preserved R5 portable reproduction packs; its supplied bytes were checked before calculating. Original exact small-hypothesis Bellman verifier: `research_notes/portable_direct/r5_fifth_chamber_f8_five_state_one_exchange_20261117/VERIFY_EXACT_SMALL_MINIMAX.cpp` at immutable commit `8acd30cbf9312afde72d0da39cbf57107c14ad48`.

Let `C_f(H;tau)` be the optimal worst-case sum of physical query costs k in {214,...,314} for identifying h in the *named* finite hypothesis set H, normal real response error at most tau/2 around exact center N_h(k), and at most f arbitrary unmarked corruptions. Write
`L=25845652773852463277015040000`,
`U=58182461585441404127941754880`, and
`H0={18,24,82,34,17}`.

## New exact restricted-population theorem

For the **twelve** actual named hypotheses

`H12=(18,24,82,34,17,0,1,2,3,144,208,255)`,

and for **every real** noise diameter tau with `L <= tau < U`,

```
C_8(H12;tau) = 8335.
```

A reusable explicit choice of physical query budgets sufficient for a worst-case 8335 strategy throughout the interval is
`K9={214,215,216,217,221,222,223,295,296}`.
This statement is specific to the twelve-hypothesis scalar observer; the complete 256-hypothesis optimum retains the proven bound `8335 <= C_8^*(tau) <= 8343`.

## Proof

1. Previous independently saved restricted Bellman evidence establishes `C_8(H0;L)=8335` with all 101 budgets. Hypothesis-set monotonicity and noise-diameter monotonicity imply `C_8(H12;tau)>=8335` throughout the stated interval.
2. At the **integer** threshold `tau=U-1=58182461585441404127941754879`, build all real-response maximal compatibility supports for all 101 original budgets from the exact integer centers. Each support is the set of named hypotheses whose centers lie in an interval of width tau; a maximal support can be found by anchoring the interval at an observed distinct center. Dropping subset-dominated supports and retaining the cheapest cost for each identical maximal-support family is exact for the worst-case adaptive identification game.
3. This produces ten distinct cheapest support families. One is the full-support query `k=291`, whose only answer keeps every live lie counter unchanged, so it has no finite-game value. The other nine families have cheapest physical costs `K9` above.
4. Represent the live state by twelve unsigned four-bit mismatch counters `e_i in {0,...,9}`, with 9 the eliminated sentinel. An answer support A updates each active counter by `e_i <- min(9,e_i + 1[i not in A])`. Terminal iff at most one counter is <=8. On useful responses, the sum of active counters strictly increases, so Bellman recursion on the finite acyclic state graph is exact. The recurrence is
`V(e)=min_k(k+max_A V(T_{k,A}(e)))`, with looping actions excluded and V=0 at terminal states.
5. The actually executed C++17 integer Bellman minimax returned `V(0)=8335` at `tau=U-1`, using all ten families; it visited **9,769,571** memoized states. Thus there is a 8335-cost adaptive strategy on H12 at U-1 using only K9. For any smaller real tau, possible answer supports are subsets of those available at U-1 (integer centers, integer width ceiling accounted for), so the same strategy provides an upper bound of 8335 throughout `[L,U)`. Combine with step 1.
6. As an independent endpoint consistency calculation, at `tau=L` the same exact solver returned `V(0)=8335`, 5,193,976 memoized states, and ten cheapest support families.

The theorem is a genuine seven-additional-hypothesis **joint** certificate (five plus seven), not an extrapolation from the earlier one-mask or seven-mask stars. The exact root equality uses a finite exhaustive solver over this stated 12-state instance, with no floating point.

## Additional exact nested certificates

The same executable returned 8335 at U-1 for the nested H8, H9, H10 and H11 populations, respectively:
- H8 = H0 + (0,144,208): 1,206,404 states;
- H9 = H8 + (1): 5,020,198 states;
- H10 = H9 + (255): 4,805,671 states;
- H11 = H10 + (2): 6,398,337 states.

All are likewise 8335 throughout the interval by the same H0-lower/endpoint-upper sandwich. The five-, six-, and seven-hypothesis older results remain independently cited, not recomputed.

## Verification, source paths, and next

Results: `RESULTS.json`; action generator and full recomputation contract: `RECOMPUTE_TWELVE.py`. Input bytes are expected to be supplied from the existing portable research packages and checked against the pinned SHA256; the exact C++17 source is pinned at the immutable GitHub commit above. The independent full256 f=8 feasibility attempt at budget 8335 did not reach a result within the bounded execution window; it is **not** evidence for feasibility or impossibility. The completed finite twelve-state calculations are preserved separately.

Next: search for a different 12+ population whose optimal eight-error budget exceeds 8335, or solve the full256 f=8 game exactly. Verify any proposed action-pruning/classification against all 101 original physical budgets. Preserve P000 residual/source semantics and exact R5 frozen input.

Formal Task CLAIM/Result/Review are not asserted by this author-side portable scientific preservation.