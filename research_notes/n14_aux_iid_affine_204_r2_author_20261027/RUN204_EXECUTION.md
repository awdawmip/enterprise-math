# Stage204 actual local execution summary and scope

Executed on 2026-10-27: primary `python verify_stage204.py` with exact Fraction suffix observer recursion, 680-state Bellman policy and unmerged full ordered-history integer P/Q weighted DFS, and separate compact `python REPRO_STAGE204.py`. Both returned exact PASS; this PR stores the **actually locally executed** compact REPRO_STAGE204.py. Primary full executed source/log are in separately delivered local portable research archive; the PR reference source reproduces the complete theorem checks without that archive.

Primary stdout key exact lines:
```
z0 112590674732081049/819200000000000000
zs 43473243/32000000000
z1 113703589752881049/819200000000000000
alpha_left 1237525705766008115/3505953353861431296
alpha_right 1237582032550008115/3505953353861431296
delta_alpha 6875828125/427972821516288
V_left 2226587197356332573/219122084616339456
V_right 2225727754437932573/219122084616339456
DFS_NODES {'00': 92974, '01': 92974, '10': 84856, '11': 84856} 355660
STAGE204_AUTHOR_EXACT_FULL_REAL_PASS
STAGE204_REFERENCE_EXACT_PASS 355660 width 6875828125/427972821516288 slope 13101264/53665
```

Executed `python scan_stage205.py`, exact Fraction rational dual candidate:
```
STAGE205 K=L 16200/137 H 175689269891985199711/1876232849527406592 first_step 28063584/7352105 transition ((12, 3, 1), 'C', 'P') ties {'(12, 3, 1)': ('P', 'C'), '(14, 0, 0)': ('P', 'Q')} gaps 1238 69107093/19635830784
STAGE205_DUAL_SCAN_PASS
```

BRC method: positive weighted typed branch carrier and provenance preservation until the declared four-observer projection. No signed or phase cancellation or native X6 attribution. The native control owner read returned CONTROL_QUOTA and own service session start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. These author results have not been formally CLAIMed or independently reviewed.
