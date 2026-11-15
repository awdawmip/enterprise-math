# Driver independent source audit: R6 PREFIX-801 incremental Hall slack

Date: 2026-11-15.
Reviewer/derivation of this audit: RESEARCH_DRIVER EM-DVR-DEBB5E.
Source author: R6 independent portable research (retain the actual source/session author record; this Driver is not the theorem author).
Status: mathematical identity and finite-evidence consistency reviewed from immutable GitHub files; a Source note only, not an authenticated Native Result review/disposition or Task completion.

## Exact sources and boundaries

- Research note: `research_notes/portable_direct/2026-11-15_r6_prefix801_incremental_hall_slack_certificate.md`, published at commit `39ee7b864f6fd3582a9f013fd4d2355e5b98a156`; corrected display rendered at commit `959d4efe21613154167f5ed5d613f863b8a1ecdf`.
- Python 3 reference implementation: `research_notes/portable_direct/PREFIX801_R6_INCREMENTAL_HALL_CHECK.py`, immutable source commit `d2dbf89cdce9435330f80141c5aabbd18dc52455`.
- Author-run JSON: `research_notes/portable_direct/PREFIX801_R6_INCREMENTAL_HALL_RESULTS.json`, immutable source commit `da5ada83e00c1830dff641fc1a78de4d1402a221`.

The scientific object is a **finite source-labeled bounded integer bipartite flow/count fiber**. It is an auxiliary joint-observer model; no implicit projection to native X6 cell, event or time semantics is introduced.

## Exact independent derivation of the update

Let F be fixed edges, with integer values t_{ij}. With residual row/column margins R_i,S_j and capacity sums C_{Aj} over currently unfixed edges, define

    sigma_A = sum_j min(S_j,C_{Aj}) - sum_{i in A}R_i.

Fix an unfixed edge e=(p,q) of capacity k to an allowed integer t, and let d_A=1_{p in A}. Directly from these definitions,

    S'_j=S_j-t*1_{j=q},
    C'_{Aj}=C_{Aj}-d_A*k*1_{j=q},
    D'_A=D_A-d_A*t.

Therefore exactly, for every row subset A,

    sigma'_A-sigma_A
       =min(S_q-t,C_{Aq}-d_A*k)-min(S_q,C_{Aq})+d_A*t. (1)

No step in this subtraction needs a nonnegativity hypothesis. Subsequent feasibility still separately requires nonnegative residual margins and the full set of Hall inequalities. Notice that even when p is not in A, its assignment can affect sigma_A through the shared column q; dropping the S_q change would be incorrect. The author's formula retains that term.

The reference class `IncrementalHall.push` applies (1) for each nonempty row mask, then updates R_p,S_q, storing each integer delta; `pop` reverses those exact changes. The `hall_recompute` reference reconstructs the same margins/capacity sums directly. Thus, for a fixed chord-variable order and the same branch predicate, the inductive exact-state invariant supports the same pruned branch tree. The claim `O(2^b)` arithmetic per push/pop is supported by the explicit loop over 2^b-1 masks, given maintained C and D; the initialization remains O(bc2^b).

## Independent consistency cross-check of declared finite families

The capacity-pattern count is

    3^(2*3) + 2^(3*3) + 1 = 729+512+1 = 1242.

Every bounded integral source table contributes exactly one margin fiber. Summed *across all capacity patterns*, the number of source tables is therefore

    (1+2+3)^(2*3) + (1+2)^(3*3) + 2^(2*4)
     = 6^6 + 3^9 + 2^8
     = 46656 + 19683 + 256 = 66595.             (2)

These calculations reproduce independently the `capacities=1242` and `tables=66595` source JSON totals, without trusting the implementation's output. The reported 57395 distinct pattern/margin fibers, 194900 visits, 62390 prunes, 5738 histogram spot-checks, and paired process timing 2.213928s vs 1.686127s are read from the author's preserved run record. They were **not** independently re-executed in this review. Equality of complete sorted source tables, if the reported `assert` run is reproduced, would imply equality of every deterministic histogram over those tables; the script explicitly checks only a sampled subset of histograms.

## Review finding and next discriminating evidence

Theorem 801.1's incremental Hall-slack update is an exact integer identity, and the implementation's `push`/`pop` transitions statically implement it. The independent combinatorial sum (2) verifies two of the complete regression totals. This supports mathematical reuse **at exactly the finite source-count model and theorem scope**, with the provenance and source-hash pins above.

An authenticated Native Result disposition would require the exact current frozen RR/ER evidence, current active Driver DA and its independence/byte-CAS review gates. The original test's timings are environment-specific measurements, not complexity guarantees. The important next technical experiment is a truly independent full-program execution and nontrivial b>=4 sparse/dense comparison once an eligible R6 owner wishes to promote this auxiliary method.

P000 and joint/composite observer directions are retained. No source author is replaced and no new CLAIM, Result acceptance, formal Task DONE or native-X6 lifting is asserted.
