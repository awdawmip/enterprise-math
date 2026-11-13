# R645 portable research handoff — sharp four-PASS minimal odd holonomy

Date: 2026-11-09 (Asia/Shanghai). Role: TASK_RESEARCH author-side, unreviewed/not admitted.
Mother task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW; publication TP2-47D65B35A7D48082EFBB. As-of native Source observation 2026-11-08T16:49:57Z: READY / NEEDS_DISPATCH, owner taskbook/unassigned, claim_id=null; no formal CLAIM granted.
GitHub connected identity: awdawmip, repo permission admin/push. Separate native Researcher-ID and RA must be stated from actual session receipt, not predecessor values; no previous session capability is inherited.

Freeze science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f unchanged. Reuse exactly V23 four-matching c(S), V27 signed score, V17 shared-slot transport, V29 source-defined PASS, source pin b62110008321d9147212cb89f2627ff613c2550d. Reference prior R644@d33317e4fbf70949f758db5b20ac4defe3b53892 (different exact target, five events including TRANSFER).

New result: in a single Cell, with zero nonnegative port ledger and NO transfers, four exact PASS events
0→1, 2→0, 2→3, 3→0
give M=[[0,1,0,0],[0,0,0,0],[1,0,0,1],[1,0,0,0]], Rin=Rout=0, u=(-1,-1,2,0), network Q=0. The V27 nine-neighbor unique-argmax selector from triad 012 follows 012→024→124→012 with score gaps 1,1,3 and odd inherited-slot holonomy (1,0,2).

Within this declared pure-PASS, one-Cell, strict-unique, V23/V27/V29 class, four events are optimal for an odd orbit from *any* starting active triad: exhaustive over all 12 off-diagonal PASS types, every multiset of n<=3 (1+12+78+364=455 multisets), all 20 initial triads, at most 20 steps per orbit, returns zero strict odd orbit. n=4 (1365 multisets) yields 60 strict odd orbits across all starts, including 2 immediately closed odd examples from 012. Self-loop PASS a→a does not change u or Omega and cannot improve minimum.

A **proposed**, not V29-native autonomous, selector-then-4-PASS packet scheduler yields M_n=(n+1)M and scales all winning score margins by n+1, preserving the odd three-cycle for all n≥0 with 151 exact packet checks. The scalar Q remains zero after each primitive event; full ledger grows. This is a strictly typed auxiliary observation, not established physical heartbeat/time or full X6 joint update.

Proof: R645_PROOF.zh-CN.md. Standard-library reproducer: R645_VERIFY.py. Finite enumeration and packet witness: R645_EVIDENCE.json, marker R645_V29_PASS_ONLY_FOUR_EVENT_ODD_HOLONOMY_EXACT_PASS. No new S6 axis or 2D native plane.

Next discriminating question: can a scheduler choose the next primitive PASS and next active triad from the *intermediate state after each single primitive event*, without an externally grouped 4-PASS packet, and be extended to multi-Cell TRANSFER while preserving V28 continuity, V30 order-dependence, full slot/path provenance and X6 Cell legality? Test with exhaustive eventwise score/transition combinations and explicit type constraints; a negative example should identify the smallest missing memory or selector context.

Activity and admission: author-side provenance only; Source identity/activity registration and Driver review are separate. GitHub branch persistence does not equal canonical main merge.