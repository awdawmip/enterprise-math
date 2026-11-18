# S23/AV exact capacity plateaux 269–300: contiguous continuation through 300

Date: 2026-11-09 Asia/Shanghai. Status: **32 new finite exact-rational endpoint coverage certificates**, author-side; independently reviewable. Freeze: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Scoped result

Continue the precise auxiliary statistical-observer definitions and rigorous proof dependencies in `research_notes/brc_s23_av_plateaux221_268_20261109_research1/PROOF.md` at immutable commit `33bbdc28e9b397d5e0fdaaea0f34ebf486b784c1`.

Write `r=log(7)/log(10/7)`, `epsilon=79r-431`, `d=2074774-380295r`, `a_i=floor(i*d/epsilon)`; `V_i=380295*i+79*a_i`, `K_i=2074774*i+431*a_i`, `H_i=V_i+510`, and `M_i=K_i+V_i-V_(i-1)-1`.

**For every integer 269<=i<=300 and all integer V_(i-1)+511<=h<=V_i+510, the frozen auxiliary S23/AV capacity is N(h)=M_i.**

The new terminal endpoint is `H_300=114,102,835`, `N(H_300)=622,887,919`. Together with previous verified i=201..268, this now certifies a contiguous range from `h=76,068,754` through `h=114,102,835`. The contribution from i=221..300 relative to the previous index-220 end is **30,427,313 consecutive integer horizons**, `83,675,523<=h<=114,102,835`, across 80 new endpoint certificates.

## Finite proof and validation

The lower bound at `h=V_(i-1)+511` follows from the previously proved all-index scaled-gap first-entry theorem in `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md`, immutable `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`.

For each new index separately, the **same** existing rigorous `check(i)` was locally executed using its 3,983-character source-equivalent Python `Fraction` port. Its exact source is `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py` at Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`. The predecessor's finite critical-cell partition soundness argument covers integer (v,j,v+j) cells, all embedded narrow-gap directions, translated prefixes within budget, top-510 rows and both exterior cells. For each of the new 32 endpoints the checker returned a complete certificate; none returned `UNCOVERED` or `MIXED_SIGN`.

The 269..300 checks yielded exactly **1,256,627 feasible critical cells**, up to 43,635 cells at index 300, and up to 92 narrow direction classes. The strict 45-term rational logarithm and witness bounds were asserted during each invocation. Both failed-late long-running attempts were transparently bounded: 221..268 and 269..297 finished before execution-time limits, and 298..300 were subsequently executed in a separate short call. The union of completed rows is contiguous 221..300 and each row is preserved in the two Source notes. No untested index is inferred.

The auxiliary two-point iid likelihood observer preserves its original labels, neutral padding and joint-count semantics. Native P000 Heartbeat/X6 and six-source/ten-label bridges remain separately typed. The result remains author-side until independent review; formal task CLAIM and math admission are separate.

## Reproduce / next

Run `python VERIFY_269_300.py` on this same PR branch; it loads the exact predecessor source file and checks all 32 endpoints and statistics. Actual local execution rows are normalized in `RUN_EVIDENCE.txt`, and they were additionally checked against the strict integer `alpha` bounds for every i.

Next exact unit: test i=301+, retaining an exact first uncovered critical cell if any; seek a uniform-i theorem for translated-witness coverage and total bit-complexity estimates instead of indefinite per-endpoint proof.
