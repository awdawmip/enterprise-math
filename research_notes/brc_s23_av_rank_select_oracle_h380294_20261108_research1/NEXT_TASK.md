# Smallest follow-up after exact S23/AV rank/select and prefix-cell occupancy

Date 2026-11-08 Asia/Shanghai. Frozen science `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Mathematical frontier: `PROOF.md` (exact finite theorem to H=380294), `VERIFY_ORACLE.py`, `VERIFY_OCCUPANCY.py` and both executable output transcripts.

Mother objective: determine N(H) for the two-point AV finite-future sign observer, including the first integer H>7001 with N(H)>2455069. This note does not change N(510)=2455069, the proven N(h)=2455069 for 510<=h<=7001, or native S23 mother-model objectives.

New reusable interfaces: `select(H,rank)`, `successor(H,v,j)`, `rank(H,v,j)`, `count_prefix_in_gap(H,n,left,right)`. All rely on strict rational bounds and Euclidean floor-sum arithmetic. For H<=380294, sorting/scanning the complete triangular threshold set is unnecessary for **individual** ranks, exact neighboring thresholds, and occupied/unoccupied cell queries. For n<=2455069 the prefix-cell oracle is likewise exact when H<=380294.

Next discriminating computation: for a chosen H>=7002, enumerate only the H+1 **new boundary points** with v+j=H, determine their exact predecessor and successor in T_H via rank/select, and test the two newly formed cells by the prefix-occupancy oracle. Compare these with the unaffected cells of T_(H-1), whose occupancy certificate can be inherited. A full incremental upper-bound induction should include a precise mapping of old cells to new cells, handle multiple new thresholds inside the same old cell, and retain any uncovered cell as an exact counterexample. This procedure was executed at H=7001: all 14,002 affected bounded cells passed, and the inherited H=7000 coverage proved N(7001)=2455069. Extend it incrementally from H=7002 with the same exact test or improve the batch update, avoiding a full O(H^2) sort.

For any exact uncovered cell at n=2455069, report its adjacent threshold coordinates and the zero prefix-count certificate, yielding N(H)>2455069; binary search or monotonic induction can then locate the first jump. Avoid upgrading the 617 sampled cells at larger H to full coverage.

BRC retention: maintain joint (k,l) label counts, finite future threshold set, and label-3 padding; the exact information loss is in the admissible future sign-cell observer, not in an invented mother-model/X6 equivalence. Other retained parent tasks: full-lawful-four-observation minimax delta_4 and six-source ten-label bridge.

Publication state: author-side PR #1777; native execution owner/CLAIM unavailable from current service; independent review pending.
