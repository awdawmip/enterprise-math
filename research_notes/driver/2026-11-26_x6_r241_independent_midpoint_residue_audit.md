# X6 R241 — independent exact midpoint-residue audit

2026-11-26. RESEARCH_DRIVER independent implementation; preserves original R239–R242 author attribution. Frozen Port 10, 1935 directions, six BRC, positive (17t,B,22t,D), strict 3/2 near set plus legal optimum, 47 necessary supports and 49 active components. The auxiliary coefficient chart is not native spatial geometry. P000 and inherited necessary-wall/rank-three completeness premises unchanged.

Inputs:
- 0019f97b2d329305c963ddfd6ec8ea622bbd7e15:research_notes/portable_direct/2026-11-26_r2_x6_r241_reducible_root_midpoint_refinement.md (actual frozen data array and author comparison rows).
- 4bc3061af929f51a8dca388738fe3d3a6dc957d6:research_notes/portable_direct/2026-11-26_r2_x6_r240_factor_free_reducible_suffix_capacity.md (three coarse residual masks).
- 92b9c31df5b741322107e6fa70319d20d320ddfb:research_notes/portable_direct/2026-11-26_r2_x6_r242_reducible_quadratic_root_closure.md (author synthesis).

The prior Driver B-independent threshold census is a subfamily of the newer R242 author closure; do not repeat its 1345-mask unresolved relaxation as if it were the current strongest author frontier. This run independently tests the decisive R241 final residual stage, not the entire R239/R240 large coarse search. R242 as a whole remains conditional on those inherited coarse coverage results.

## Independent method

Read data from R241, retaining both split corrections. For each component (a,b) insert the positive projective midpoint m=a+b; preserve four oriented germs (a,m),(m,a),(m,b),(b,m). Normalize positive rays by primitive integer gcd. Assert both endpoints lie on their claimed support. Enumerate coefficient-space intersection rays via cross products of every pair of distinct endpoint rays; identify signs up to reversal. For each such v and each incident endpoint normal p_i, enumerate lexicographic perturbations v, v+epsilon*(+-cross(v,p_i)), and v+epsilon*(+-cross(v,p_i))+epsilon^2*(+-p_i). Use exact integer signs, retaining zeros. Evaluate each germ by its first nonzero endpoint sign. This is the inherited rank-three arrangement enumeration, implemented separately. Deduplicate unordered strict masks. Projection to the first and last fine germs on each component gives its original two germs. For each full fine mask group by the canonical projected mask; for target r and coarse factor u, its unique possible partner modulo complement is canon(u XOR r). Count each unordered pair once and expand its full Cartesian product. The resulting root masks exactly equal the 19 author masks. This step checks the three coarse factor multiplicities independently.

For a tagged remaining germ subset S, let c(S) count distinct supports (not components). A correct depth d linear suffix requires c(S)<=2^d-1. For the finite strict-germ relaxation c(S)<=d suffices by sequentially querying its supports. If c(S)=2^d-1 at least one complete label must disappear at the next query, which requires a query proportional to that support. Otherwise use the full finite linear bank. For each query (p,q), recurse on S&p and S&q; discard options exceeding child capacity, deduplicate identical child pairs, and test feasible options ordered by descending larger-side hardness as a tie-break only (actual sort ascending max child label count then min). Memoize exact true or false by (S,d). Check the larger root side first. Count using four-germ component occupancy with the two duplicate-label corrections; cross-check every bank mask against direct label intersection. This proof uses the inherited necessary-wall premise, not a claim that the finite relaxation is sufficient for the full output problem.

## Actual exact computation
- 99 rays, 196 germs, 13064 distinct unordered linear partitions, 2178 coarse full-mask groups.
- Coarse pairs (hex canonical masks), fine-group cardinalities:
  - 107b3c5c0047000000 / 33cf3313fffc5f307ffffff0: 1 x 3
  - 107b3c5c0045000000 / 33cf3313fffc5f307ffffff0: 5 x 3
  - 107b3c5c0047000000 / 33cf3313fffc7f307ffffff0: 1 x 1
- 19 exact fine roots, all 19 excluded; 1129673 exact query scans, 135 nontrivial recursive calls; no cutoff. Author R241 used 3179249 scans, 1455 calls; the order/memoization differs, not the logical scope. No disagreement.
- 26128 direct-vs-fast count comparisons (two masks per bank partition).

Exact excluded canonical root masks (each second branch is the 196-bit complement), with label counts:
```
f0ff0ff0f0f000fe010f000000f0f000fe0ffffffffff00 24 27
f0ff0ff0f0f000fe010f000060f0f000fe0ffffffffff00 25 27
f0ff0ff0f0f000fe010f000020f0f000fe0ffffffffff00 25 27
f0ff0ff0f0f000fe010f000000f0f000fe8ffffffffff00 25 27
f0ff0ff0f0f000fe010f000060f0f000fe8ffffffffff00 26 27
f0ff0ff0f0f000fe010f000020f0f000fe8ffffffffff00 26 27
f0ff0ff0f0f000fe070f000000f0f000fecffffffffff00 25 27
f0ff0ff0f0f000fe070f000060f0f000fecffffffffff00 26 27
f0ff0ff0f0f000fe070f000020f0f000fecffffffffff00 26 27
f0ff0ff0f0f000fe070f000000f0f000feeffffffffff00 25 27
f0ff0ff0f0f000fe070f000060f0f000feeffffffffff00 26 27
f0ff0ff0f0f000fe070f000020f0f000feeffffffffff00 26 27
f0ff0ff0f0f000fe070f000000f0f000fe8ffffffffff00 25 27
f0ff0ff0f0f000fe070f000060f0f000fe8ffffffffff00 26 27
f0ff0ff0f0f000fe070f000020f0f000fe8ffffffffff00 26 27
f0ff0ff0f0f000fe030f000000f0f000fe8ffffffffff00 25 27
f0ff0ff0f0f000fe030f000060f0f000fe8ffffffffff00 26 27
f0ff0ff0f0f000fe030f000020f0f000fe8ffffffffff00 26 27
f0ff0ff0f0f000fe010f0000e0f0f000fe0ffffffffff00 25 27
```

## Scope and next
This confirms the final refinement step of R242 independently. Under R238 and R239/R240 coarse coverage, every real reducible homogeneous quadratic at the sole nonlinear root is excluded, so the remaining root family is nonsingular indefinite. A first nonlinear query below linear ancestors is separate; unrestricted K6 in [1,2]. No Native Review, Result acceptance, formal Task completion or parent closure.
