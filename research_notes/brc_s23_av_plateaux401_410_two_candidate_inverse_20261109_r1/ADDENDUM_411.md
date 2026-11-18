# Exact finite capacity addendum: plateau 411

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: **author-side exact finite certificate**, independently reviewable; no formal Task CLAIM implied.

Under the same frozen two-point S23/AV label-(1,3,4) auxiliary observation model and definitions in `PROOF.md`, the strict rational checker evaluated the entire finite critical-cell partition at index `i=411` and returned

```
CERTIFIED_PLATEAU 411 H 156320715 M 853215848 narrow 126 beta_bound 412 critical_cells 81910 witnesses_used 51
PASS_SEGMENT_411_411
```

Independent strict rational endpoint arithmetic gives `a_411=floor(411*alpha)=240`, `H_411=156320715`, `M_411=853215848` and previous endpoint `H_410=155940420`.

Consequently, conditional on the previously published soundness of the critical-cell reduction and global first-entry lower-bound theorem, the exact auxiliary capacity is

```
N(h)=853215848   for every integer 155940421<=h<=156320715.
```

The new interval comprises **380295 consecutive integer horizons**. This is a direct specialization of the same sufficiency-plus-lower-bound proof given in `PROOF.md`; the all-index two-candidate inverse lemma remains unchanged and now applies to an additional certified capacity interval. The original index-401–410 evidence and results are preserved.

Execution used the locally restored checker with exact published Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`. The one-index process completed. Reproduce in a repository checkout with `python research_notes/brc_s23_av_plateaux401_410_two_candidate_inverse_20261109_r1/VERIFY_411.py`; see `RUN_411.txt`.

Next: inspect index 412, and pursue a uniform witness covering invariant rather than relying entirely on incremental finite checks.
