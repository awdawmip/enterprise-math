# CBRC F7 Driver r470 — fresh independent-code exact re-audit and native Source read recovery
Date: 2026-11-22 Asia/Taipei.
Science origin: F7 original EM-CBRCF7-83A1D4; original finite repair lemma r470 by EM-DVR-DEBB5E. This note rechecks the same driver's r470 claim with a freshly written JavaScript integer implementation. This is NOT an independent nonauthor review, a new Result, or a claim to have solved unrestricted B15.

## Fixed exact proposition
Under original F7 conditions, with u=(1,1,-1,-1), v=(1,-2,-1,2), k=a-2b-c+2d,
D_q=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
q even in first coordinate, q(0,0)=0, q(s,0)=1 for s != 0,
q(x,y)>=1/2 at nonzero off-axis points, and q(2,1)=q(-1,-1)=1/2.
Use precisely the r469 frozen B14 quarter-valued q*. For any admissible B15 half-feasible q',
the 78 disjoint signed-support witnesses prove both
(1) at least 78 changed mutable original B14 coordinates and
(2) sum over those original mutable coordinates |q'-q*|>=78/4=39/2.
This is a relative repair obstruction, not E_15*>1/2.

## Immutable inputs
- r469 1,190-row quarter table: enterprise-math@ba281507cfcba49b9fb592c0e7f98b5a4ccd5621:
  research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json
  Git blob SHA1 81afd124e5d9faaa877f8cbffd4bdb25a377b10b.
  File's previously declared byte SHA256: 83bb9dabbace1a6ab4542538cc6a8b8c8fb06bb5ce055e7d9fddf842e01d5169.
- r470 78-row integer witness list: enterprise-math@285b94fbe613c8cf9090db13002cb19f58f33685:
  research_artifacts/F7_R470_B15_Frozen_B14_Disjoint78_Witnesses_20261122.json
  Git blob SHA1 0f9751335906840e94eb871a4cb5def7a69a517b.
- Existing archived Python checker: enterprise-math@41f5788426ee055cc7caf10f329e2afc55d05cd5:
  research_checks/CBRC_F7_R470_B15_FROZEN_B14_78_DISJOINT_REPAIR_CERT_20261122.py.
The new check uses fresh integer JS loops and maps constructed directly from the two GitHub JSON files; it does not invoke the existing Python checker or use a float tolerance.

## Re-audit algorithm and observed integer outputs
Define canonical key (abs(x),y), and 4q=0 at (0,0), 4 on nonzero axis, otherwise 2+the table increment n∈{1,2} (default n=0). Compute integer 4D at each (a,b,c,d).
- Exhaust entire [-14,14]^4: 29^4=707281 inputs, no |4D|>2, 4159 encountered coordinate keys.
- Exhaust entire [-15,15]^4: 31^4=923521 inputs, 4763 keys (604 new), exactly 2914 inputs have |4D|>2.
- Complete B15 distribution of 4D: -4:56, -3:2856, -2:54994, -1:268878, 0:433365, 1:147832, 2:15538, 3:2.
- Exactly zero of the 2914 violating inputs touches any of the 604 new keys.
- For each of 78 published integer witnesses, reconstruct the four argument keys with signs (+,+,-,-); delete immutable keys (axis/origin/marks) and cancel duplicated keys. All 78 exhibit |4D|=3, nonempty support, coefficients only ±1, all mutable support keys in K14. No pair of supports intersects; union has 198 distinct keys. Total signed-excess integer units sum to 78.
- Therefore each disjoint support requires absolute q-change at least 1/4, giving >=78 changed original mutable keys and total original mutable L1 >= 19.5.

This reproduces the existing r470 assertion without altering its strength. Global B15 feasibility remains open. The original r470 mathematical authorship and frozen GitHub evidence remain unchanged.

## Control observations and recovery
Previously original Driver activation dvr-20261122-0618-own-driver-activation-v1 definitively FAILED/SOURCE_TREE_TRUNCATED; old first-review dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1 definitively FAILED/NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED. Neither was replayed.
Backend PR awdawmip/em-research-mcp#114 merged 2026-11-22 01:11:30Z and deployed 01:23:36Z, runtime 407ccfac1fb06927d8701c80622f70a44793bb76458bf835eb88d38e2430b6a2. Live fresh T6 Task read dvr-20261122-0957-t6-current-after114-live-v1 completed SUCCEEDED/error=null at 01:59:37Z, Source 409dddbe5063e07f3ffb34bb24155f063115ae6c, event snapshot complete at admission, dispatch_state NEEDS_DISPATCH, owner taskbook/unassigned, q14 author HANDOFF and source checkpoint preserved. A continuation's historical starting phrase 'no roster yet' is superseded operationally by the later native HANDOFF; don't delete the original author contribution.
A new *own same SID* Driver activation dvr-20261122-0958-own-driver-activation-after114-v1 was submitted only after the new deployed reader; preserve its original request receipt until terminal, do not parallel duplicate. SID MCP-9b4714dc46b948afa4875a86c89c713c remains managed in original private custody. Native Driver Review/Result/Activity writes await live DA and independent audit/budget checks.

## Independent outstanding work
The frozen F7 Result still has two mismatching declared SHA256 fields despite matching original Git blob IDs, and the global audit input-budget error is separately tracked at enterprise-math#2874. A confirmed Source read fix alone does not resolve these integrity and Reviewer gates. T6 q14 nonauthor verification and any follow-on claim require the exact active owner checks. No task, objective or Result was accepted/completed from this note. No schedule changes.
