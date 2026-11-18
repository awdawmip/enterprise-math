# R5 K=214: forced nonlocal changes in every nearest-old optimum

Date: 2026-11-15. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Derived observer: the frozen 954-event 1D integer radius-two indexed-center model, K=214; this is not a native-X6 quotient claim. Frozen scientific input commit: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

## Statement and exact findings

Let `x` be the frozen original coordinates and `S_i` the **fixed, explicitly published 214-center optimal witness** in `EXACT_R5_K214_NONLOCAL_RECOURSE.json` (2026-11-15) for independently closing gap `i∈{3,8,9,10}`. Input file SHA-256: `53072d874619a1eb6bede5e43d647d7d5c228f83371ea76b05eba03b5a81da82`. Its original exact witness-specific nearest old distances are 3,7,7,4. Define

`C_i={T∈Opt_empty(214): |S_i∩T|=max_{U∈Opt_empty(214)}|S_i∩U|}`.

This run computes **all** members of `C_i`, not just a single backtracked old optimum. The following classifications are exact:

| gap i | closest old optimizers `|C_i|` | centers of `S_i` absent from **every** `T∈C_i` | centers absent from `S_i` present in **every** `T∈C_i` | optional incoming center (one of the pair) |
| --- | ---: | --- | --- | --- |
| 3 | 2 | 46,50,54 | 49,53 | 44 or 45 |
| 8 | 2 | 110,114,271,274,278,282,286 | 112,115,272,276,281,285 | 108 or 109 |
| 9 | 2 | 113,117,271,274,278,282,286 | 112,115,272,276,281,285 | 118 or 119 |
| 10 | 1 | 123,127,131,136 | 122,126,130,135 | none |

Every other center retained by `S_i` is present in every member of `C_i`. In particular, for **both i=8 and i=9**, the five far-away indices `271,274,278,282,286` of the new witness must be removed in every closest old optimum; this nonlocal part of the reconfiguration is mathematically forced, not a choice made by a particular traceback.

These are the fixed-witness results. They strengthen the previous `R_i(214)≥(3,7,7,4)` certificate; whether they equal the full `max_S min_T` worst-case values remains open.

## Exhaustive nearest-optimum path method

For increasing indexed-center paths `T=(j_1<...<j_K)`, precompute the old-coordinate directed acyclic graph: allowed edge `u→v` precisely when every intermediate event has nearest distance ≤2; its weight is the sum of old-coordinate distances of intermediate events to `{u,v}`. Prefix/suffix weights cover events before the first center and after the last center. Such a path represents each feasible K-center set once and its summed weights equal the entire nearest-center distance cost.

For a fixed `S`, attach bonus `b_j=1_{j∈S}` to a selected center `j`, and minimize the **lexicographically ordered exact-integer pair** `(cost,-sum b_j)`. This first selects exactly `Opt_empty(K)`, then among those maximizes the overlap with `S`. The result is `(1064,-M)`, where `M=K-rho_x(S;K)`.

Forward DP `F[t,j]` finds the best pair for prefixes with `t` centers ending at j; suffix DP `H[m,j]` finds the best pair from j to the final center, with `m` centers including j and the bonus for j excluded. Simultaneously count all paths achieving each pair, `A[t,j]` and `B[m,j]`, summing exact arbitrary-precision integers for ties. If `F[t,j]+H[K-t+1,j]` equals the global best pair, exactly `A[t,j]B[K-t+1,j]` globally nearest old optimizers contain j at rank t. Thus

`c(j)=sum_{t=1}^K 1_{F[t,j]+H[K-t+1,j]=best} A[t,j]B[K-t+1,j]`.

The unique path order implies each j appears in at most one rank. The total number `C` of nearest-old optimizers is the sum of tie counts at globally best terminal centers. Exact consequences: `c(j)=0` iff j occurs in none of them; `c(j)=C` iff j occurs in every one of them. The independent accounting identity `sum_j c(j)=K C` is verified for each witness.

## Reproduction and evidence scope

The actual local Python run reconstructed 954 events, extent 1065, 28 length-three cuts from the frozen subset-sum coefficients; read the prior immutable 24,394-byte witness JSON (SHA-256 above); and ran the pair-valued forward/backward count DP on each of the four witnesses. It returned `PASS_EXACT_R5_FORCED_COORDINATE_CLASSIFICATION`. The exact tie totals are `(2,2,2,1)` and the forced-coordinate sets match the table. Full newly generated JSON SHA-256: `f0fc5dae9566480df3337a55d620c92f4c4475797ca3969738e13738a27a313f`; the local reproducible script SHA-256: `16de8841fba77c3e4998c318e63f9337ae76c52815ea0db8b0ae69cb7723e3a7`.

Independently, 666 small randomly selected instances (n=3..8; all admissible K-center subsets exhaustively checked **within each instance**) matched the pair-DP's best distance, count of closest old optimizers, forced removals, always-retained centers and forced insertions. The set of selected small inputs was sampled; the verification within each such input was exhaustive. No floating-point arithmetic or approximate tie check was used.

Previously saved sources: `research_notes/portable_direct/r5_low_budget_unit_recourse_20261115/K214_NONLOCAL_LOWER_BOUNDS.md`, `VERIFY_R5_K214_NONLOCAL_RECOURSE.py`, `VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py`, Draft PR #2427. New executable, small-check program and full JSON evidence are retained in the handoff attachments; the committed `EXACT_R5_FORCED_COORDINATES_SUMMARY.json` records the result vector and full-output digest. Reproduce the complete input first with `python VERIFY_R5_K214_NONLOCAL_RECOURSE.py > EXACT_R5_K214_NONLOCAL_RECOURSE.json`; then run `python VERIFY_R5_FORCED_COORDINATES.py EXACT_R5_K214_NONLOCAL_RECOURSE.json > EXACT_R5_FORCED_COORDINATES.json`, and separately `python TEST_R5_LEX_MARGINALS.py`. Full source, cross-check, and summary are committed together; full 14,094-byte output remains available as the SHA-pinned conversation artifact. Independent review: `NOT_REVIEWED`.

## Next discriminating problem

Determine exact `R_i(K)=max_{B⊆I\{i}} max_{S∈Opt_{B∪{i}}(K)} min_{T∈Opt_B(K)}|S\T|` for i=3,8,9,10 and K=214..221 by a genuinely max-new/min-old algorithm. The existence of only 1–2 nearest old optima for **these fixed witnesses** should not be mistaken for a bound on all new optimizers or all closure backgrounds.
