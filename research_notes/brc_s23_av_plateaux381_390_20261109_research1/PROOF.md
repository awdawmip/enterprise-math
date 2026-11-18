# S23/AV auxiliary capacity: exact finite plateau certificates 381–390

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE_FINITE_EXACT_CERTIFICATE; independent review pending. Scientific inputs unchanged: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Exact problem and assertion

For the frozen two-point iid auxiliary likelihood observer on labels (1,3,4), one-step laws are `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)`. Preserve joint counts of labels 1 and 4, with label 3 as neutral padding. Let `T_h={10^j/7^s:0<=j<=s<=h}`; `N(h)` is the smallest common padded prefix length with an attainable score in every open cell of the threshold partition, including exterior cells.

Put `r=ln(7)/ln(10/7)`, `epsilon=79r-431`, `d=2074774-380295r`, `alpha=d/epsilon`, `a_i=floor(i alpha)`, `a_0=0`; `V_i=380295i+79a_i`, `K_i=2074774i+431a_i`, `H_i=V_i+510`, `M_i=K_i+V_i-V_(i-1)-1`.

**New finite-range conclusion (conditional on the inherited soundness of the existing exact critical-cell checker and first-entry lower-bound lemma): for every integer `381<=i<=390` and every integer `V_(i-1)+511<=h<=V_i+510`, `N(h)=M_i`.**

The contiguous new horizon range is `144530149<=h<=148333572` (3,803,424 integers). At the last endpoint, `N(148333572)=809640501`. Previous endpoint: `H_380=144530148`, `M_380=788890175`.

## Proof and witness structure

The prior all-index scaled-gap first-entry theorem, `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at immutable commit `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`, gives `N(V_(i-1)+511)>=M_i` for each integer `i>=2`.

For every `i=381,...,390`, the **unchanged** critical-cell checker `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py`, Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`, completed `check(i)` with a non-null tuple (10 actual complete rows). The checker uses strict 45-term rational logarithm bounds, checks the unique `floor(i alpha)` bracket, enumerates every embeddable positive threshold displacement narrower than `epsilon`, and verifies that translated prefix witnesses cover each feasible integer critical cell. Its partition predicates are constant on each feasible cell (see prior `PLATEAUX20_200.md` for the completeness proof); it additionally checks top 510 rows and both exterior cells. This yields `N(H_i)<=M_i` at each tested endpoint.

The completed 10 calls covered **721,366 feasible critical cells**, with no uncovered cell, no mixed-sign blocker, and no failed exact rational comparison. Maximal critical-cell count per endpoint: 73,831; maximal narrow direction count: 120. The first failed/unverified next endpoint is **not** established; indices 391 onward were not completed in this attempt.

Monotonicity of `N(h)`, the lower bound at the first point of each interval, and the upper bound at the last point imply equality on every stated interval. Adjacent intervals join exactly because the next lower endpoint is `H_i+1`.

## Execution evidence / provenance

The original script was fetched from GitHub PR #1777 at commit `8b141c30615ec08c00c9452fa80da662e939e24a`, recreated byte-for-byte in local execution (Git blob checked equal to `261d7e22da0e62d667009cb50acfe77ac4e35c3f`), and imported by `VERIFY_381_400.py` for actual sequential execution. The 381–400 batch was interrupted by the execution time limit after exactly indices 381–390 had emitted complete successful rows. All ten completed rows are preserved verbatim in `RUN_EVIDENCE.csv`; later indices are deliberately absent. A separate exact rational arithmetic row audit confirmed `H_i`, `M_i` and the strict alpha-floor witnesses for the ten rows: `PASS_COMPLETED_ROWS_381_TO_390`. The published `VERIFY_381_390.py` is the focused reproducible wrapper using the same pinned checker; its `--start 381 --end 381` run completed separately with `PASS_SEGMENT 381 381`.

Evidence strength: author-side exact finite computations plus existing published sufficiency theorem and lower-bound proof, not an independently reviewed or formally admitted statement. The auxiliary joint-count observer is a typed external statistical representation; lawful passage to the full six-source ten-label model and native X6/Heartbeat observables remains a distinct mapping obligation.

## Next unit

Complete the exact checker at `i=391` and expand in short bounded segments. In parallel derive a uniform (rather than endpoint-by-endpoint) covering invariant for the narrow-gap displacement families and investigate the lawful six-source observation bridge. Preserve the first exact uncovered cell or failed inequality if the next checker fails.
