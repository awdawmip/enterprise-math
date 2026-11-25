# T6 p13 q20 split(9,11): exact continuation c401..450

2026-11-25. Existing Driver EM-DVR-DEBB5E, own managed SID MCP-9b4714dc46b948afa4875a86c89c713c; own scientific continuation, NOT_REVIEWED. Reuse exact definitions and unchanged C++ source in [prior c301..400 record](https://github.com/awdawmip/enterprise-math/blob/f7f9693709f9ca2e89870561bd093b16e6786a40/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget301_400_four_residues.md). Both side budgets 2331, maximal p13 after high-valuation cancellation, q split 9+11, c=810-w(P), q0 mass <=c. Lower-prime denominators allowed: multiplying full reciprocal moment equality by 13^k makes 13-free denominators vanish modulo 13^k. Four necessary residues k=4,5,6,1, exact 61-bit disjoint encoding. No redo of completed c0..400; c401..500 prior interrupted run was not credited.

Executed unchanged C++17 reproduction code copied from the above immutable prior record (local /tmp/t6_q9.cpp), g++ -O3 -march=native -std=c++17 -pthread; /usr/bin/time -v /tmp/t6_q9 401 450. Exact output:

```
Q=9 full=8963595909 P=186647 H=63972
band=401..450 expected=675010922 P=15432
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 1 P=3776 profiles=164484647 filter=14733499 hits=0
group 2 P=3826 profiles=167727081 filter=15028830 hits=0
group 3 P=3871 profiles=170282562 filter=15249315 hits=0
group 0 P=3959 profiles=172516632 filter=15443738 hits=0
TOTAL 675010922 filter=60455382 hits=0
User 60.42s; system 0.48s; wall 25.02s; maximum RSS 951640 KiB; exit 0.
```

DP count equals exhaustive combined profile count; the four P index classes partition the full band; bitmap only filters, every survivor binary-searches the exact key. All 100750914 Q11 profiles in the exact target set. Thus complete c401..450 exclusion in the stated domain. Cumulative c0..450 1432278038 of 8963595909, remaining 7531317871. Next c451 onward; q20(10,10) open.

## Driver evidence reconciliation

Original dvr-20261125-1100-t6-current-read-v1 SUCCEEDED, observed 2026-11-25T03:05:24Z at Source db5103b44e0e7b13afdf1ff2cd142466714dbd5f: HANDOFF_READY/NEEDS_DISPATCH, no live claim in that snapshot, formal task frontier still names q14 p17 preflight and nonauthor review. Source science has advanced beyond this old task projection. In particular [prior four-adic q14 full-observer injection](https://github.com/awdawmip/enterprise-math/blob/88b60097898c597d2b950d8f1e132a91b8fd7b5d/research_notes/driver/2026-11-23_t6_p17_q14_split77_full_observer_four_adic_injection.md) and [p17 q12/q13 full-observer exclusions](https://github.com/awdawmip/enterprise-math/blob/6b886e4d07a22033ea48598c7a40c1fede34e92b/research_notes/driver/2026-11-24_t6_p17_q12_q13_full_observer_four_five_adic_exclusion.md) address the lower-prime gap flagged by [scope correction](https://github.com/awdawmip/enterprise-math/commit/bf085f15492b1725891caeaf29341e9944f42084). These are previous Driver contributions, not an independent formal review or a new q14 exclusion. The prior plan hash b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24 still needs exact source path/bytes and eligible independent reviewer; do not replay affine work merely because the task projection is stale. In the current read, direct JS DFS revalidated the frozen 1907 roster arrays against original blob 3fb721212af00096d12453035b1cef6e28b45587, with 809566 unordered disjoint pairs. Local six-residue computation reproduced 55347 unique complete order7 once-p17 profiles, first-three-residue injection for 67 v17=2 profiles; reuse previous stronger four-adic proof rather than claiming another new theorem. No new affine computation performed.

Original own registration and DA-2C461358FCCA215C8753 receipt read; own recovery shows managed session not closed or revoked, no pending own requests in recent returned list. The recovery metadata is not new write authority. Onhour r163 and backlog r483 independently read; preserve q11 research and DCMP11 original selection, no positively confirmed available researcher. Native Review, Result, task, parent completion increments all zero.
