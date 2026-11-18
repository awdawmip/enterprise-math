# S23/AV: exact capacity plateaux 221–268 (author-side certificate)

Date: 2026-11-09 Asia/Shanghai. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: **48 finite index checks passed; independent mathematical review pending**.

## Claim and exact scope

In the frozen two-point auxiliary iid experiment, one-step laws on labels (1,3,4) are `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)`. Retain joint counts (#1,#4), with neutral label-3 padding. Let `N(h)` be the least padded prefix length whose attainable likelihood ratios hit every open threshold cell induced by `T_h={10^j/7^s:0<=j<=s<=h}`, including exterior cells.

Define `r=ln 7/ln(10/7)`, `epsilon=79r-431`, `d=2074774-380295r`, `alpha=d/epsilon`,
`a_i=floor(i alpha)`, `V_i=380295i+79a_i`, `K_i=2074774i+431a_i`, `H_i=V_i+510`,
`M_i=K_i+V_i-V_(i-1)-1`.

**For every integer 221 <= i <= 268 and every integer V_(i-1)+511 <= h <= V_i+510,**
`N(h)=M_i`.

The previous certificate's endpoint is `H_220=83,675,522`. This run extends exact capacity through `H_268=101,931,894`, adding **18,256,372 consecutive integer horizons**, namely `83,675,523 <= h <= 101,931,894`. The last candidate/equated capacity is `M_268=556,486,962`; the first is `M_221=458,961,026`.

## Proof dependencies and exact finite certificate

The *lower bound* is the all-index first-entry law for a scaled base threshold gap `J_t=(10^431/7^(510+t),1/7^t)`, proved in `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at immutable commit `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`. At `t=V_(i-1)+1` that theorem gives `N(510+t)>=M_i`, for any integer i>=2.

For *upper bounds*, the exact checker `check(i)` of `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py` (blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`) encodes a full partition of integer left endpoints into critical (v,j,v+j) cells and proves that every cell has a translated prefix witness of length <=M_i. Its correctness argument, rigorous log enclosures, narrow-displacement completeness, top-510-row and exterior-cell constructions are in the predecessor `PLATEAUX20_200.md` and `research_notes/brc_s23_av_plateaux201_220_20261108_research1/PROOF.md` at `696f253de86bf781dda922080a65f49076d2018b`.

The source-equivalent local port of `check(i)` was executed for each i=221..268: all 48 returned finite certificates, no `MIXED_SIGN`, `UNCOVERED`, exact-bound or log enclosure assertion failed. Across the 48 indices, there were **1,394,515 feasible critical cells**, up to 34,798 at i=268, and up to 82 embedded narrow direction classes. See `RUN_EVIDENCE.txt` for per-index H, M, narrow class count, beta bound and critical-cell count. The computed candidate endpoints were independently checked using the *strict* integer bounds for `alpha` (no float floors). Nesting of `T_h` and monotonicity of `N(h)` propagates the proven lower and upper endpoint equalities across each integer interval.

## Reproduction and finite-validation boundary

Run `python VERIFY_221_268.py` from this directory on the same PR branch; it loads the pinned upstream source file from its same-repository relative path and calls `check(i)` for all 48 endpoints. The original local verification used a complete 3,983-character source-equivalent copy rather than the import, and the attached normalized stdout preserves the actual complete rows. The longer attempted run through i=300 was interrupted after i=268; **no result is claimed for 269..300**.

The quantified conclusion is a finite author-side mathematical proof under the inherited checker soundness theorem. This S23/AV auxiliary statistical observer is not yet a verified lawful native six-source/ten-label observation bridge; P000 native X6 ontology and the frozen inputs are unchanged. Researcher identity/active Owner/CLAIM and independent mathematical review retain separate authority.

## Next smallest executable unit

Continue from i=269 with the same exact checker, preserving the first uncovered cell (v, j, v+j) or the first ambiguous bound if any; otherwise grow a new nonduplicating contiguous capacity certificate. For a stronger structural result, replace the finite endpoint-by-endpoint coverage proof with an all-index uniform witness theorem, accounting for narrow-direction growth and exact-bit cost. See `VERIFY_221_268.py` and `RUN_EVIDENCE.txt`.
