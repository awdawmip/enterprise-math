# R50 — automatic last-cell threshold and complete integer-bit cost

Frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34` remains fixed. R49 proved: for any fixed irrational theta, original consecutive history labels 0..m-1 and suffix H, all source-to-history crossings occupy the orbit sumset `[1,m+H-1]`. Once a Farey upper error v enters the last cut cell `v<=q*=1-max_{1<=s<=m+H-1}{s theta}`, every future upper-neighbor stage reuses the same complete labelled age vector. Frozen S23 enters at j=225 and needs only two source vectors for 78 stages.

**First proof unit:** Give a parameter-independent continued-fraction/Farey decision procedure to find the earliest future upper-neighbor stage with `v<=q*`. Handle equality at half-open cuts, insufficient H source coverage and the case where upper error is temporarily outside the threshold. Show an explicit non-S23 irrational example with an exact pre-threshold failure and an exact post-threshold transferred age vector.

**Second computation:** Use like-for-like bigint arithmetic costs for theta enclosure preparation/refinement, 353-cut proof, 516 unique difference floors, 389 initial source inspections, repeated stage decisions, event sorting, verification, full output, and generic atlas amortization across many source endpoints. Compare with frozen R32 and stagewise R48 in original input units. Maintain full owner provenance and actual task/claim/review state.

Acceptance: exact lemma and quantified scope, reproducible source, finite certificate, clear new observations, and formal shared authority handled separately from author-side saved work.
