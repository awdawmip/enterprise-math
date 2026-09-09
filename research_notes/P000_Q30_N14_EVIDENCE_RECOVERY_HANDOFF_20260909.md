# P000 Q30 n=14 evidence recovery handoff — 2026-09-09

Status: `EVIDENCE RECOVERY HANDOFF / NOT MATHEMATICAL ACCEPTANCE`

Task to claim: `RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE`

## Why this handoff exists

Current main retains the original Q30 publication `research_task_records/RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N14-COLLISION-FRONTIER/TP2-8969646E7FF5FB8A9F5D.json`, but no result record exists for that original task. Do not reconstruct Q30 from conversation history and do not restart the n=14 census before testing the persisted evidence below.

## Immutable prior research entrypoint

Old research head: `b90378c332e0dbf80aad0c09d363047abb2ee2f3`

Primary certificate:
`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_RETURN_PROFILE_1WL_N14_EXACT_KERNEL_ORBIT_CERTIFICATE_V2.json`

Dedicated r=14 replay supplement:
`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_SUPPLEMENT_V1.json`

Dedicated r=14 executable checker:
`research_checks/P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_CHECK_20260905.py`

Sector compact shards at the same commit:

- `P000_Q30_N14_KERNELS_R2_V1.json`
- `P000_Q30_N14_KERNELS_R4_V1.json`
- `P000_Q30_N14_KERNELS_R6_V1.json`
- `P000_Q30_N14_KERNELS_R8_V1.json`
- `P000_Q30_N14_KERNELS_R10_V1.json`
- `P000_Q30_N14_KERNELS_R12_V1.json`

r=14 persisted replacement material includes:

- `P000_Q30_N14_KERNELS_R14_P1_V1.json`
- `P000_Q30_N14_KERNELS_R14_P2_V1.json`
- `P000_Q30_N14_KERNELS_R14_RECON_P1_V1.json` through `P000_Q30_N14_KERNELS_R14_RECON_P5_V1.json`
- `P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_SUPPLEMENT_V1.json`

Also consume `P000_Q30_N14_ORBIT_COVER_CHECKPOINT_V1.json`.

## Exact claim carried by the old certificate

Frozen observable:
`FROZEN_Q22_Q25_Q27_Q28_Q29_PRIMITIVE_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_UNCHANGED`.

Claimed terminal classification:
`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N14`.

| r | representatives | normalized connected | exact stable packets | kernel types |
|---:|---:|---:|---:|---:|
| 2 | 43 | 12,414,124,800 | 43 | 2 |
| 4 | 931 | 38,690,265,600 | 931 | 5 |
| 6 | 6,879 | 120,607,023,600 | 6,879 | 17 |
| 8 | 19,587 | 393,165,964,800 | 19,587 | 59 |
| 10 | 21,434 | 1,358,543,793,600 | 21,434 | 197 |
| 12 | 7,589 | 4,991,840,330,400 | 7,589 | 478 |
| 14 | 509 | 19,491,385,914,000 | 509 | 509 |
| **total** | **56,972** | **26,406,647,416,800** | **56,972** | **1,267** |

Claimed collision fibers: `0`. The certificate records PASS for each persistent compact sector verifier, PASS for the full direct representative verifier, and `cross_sector_equal_packets = 0`. Treat these as evidence to replay, not as acceptance by this handoff.

## Provenance caveat that must not be hidden

The V2 certificate's `kernel_shards` list still names `P000_Q30_N14_KERNELS_R14_V1.json`. That monolithic file is absent at the final old head. Later r=14 reconstruction/shard material and the direct replay checker were added instead. The recovery must show exactly how those later files supersede the stale citation and still cover all 509 r=14 objects.

## Prior execution identities

The old certificate records:

- researcher: `EM-P000Q30N14-536310`
- claim: `chatgpt-p000q30n14-20260904-2106-536310`
- execution record id: `ER-DB89BAA8E483449E2E00`

A later 2026-09-06 recovery attempt claimed the original Q30 task as:

- researcher: `EM-P000Q30-BCC31E`
- claim: `CLAIM-P000Q30-20260906T1328Z-CHATGPT-01`
- branch: `research/p000-phil-q30-return-profile-1wl-n14-em-p000q30-bcc31e`

That later claim did not produce a result record on main. It is continuity provenance only.

## Current recovery package available for comparison

A subsequent recovery package is available in open PR `#1366` and is useful continuity evidence for this gate. It is **not** mathematical acceptance and is not a substitute for the gate's own replay.

- PR: `#1366` — `research: recover completed P000 Q30 n=14 collision frontier`
- branch: `research/p000-phil-q30-return-profile-1wl-n14-em-p000q30-d67de2`
- researcher: `EM-P000Q30-D67DE2`
- claim: `CLAIM-P000Q30-20260907T0800Z-CHATGPT-02`
- execution: `ER-9EF9871C713F5C79FA92`
- result: `RR-23FD8C3BE3A3F95C2D4B`
- result path on that branch: `research_result_records/RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N14-COLLISION-FRONTIER/RR-23FD8C3BE3A3F95C2D4B.json`
- return path on that branch: `research_returns/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER_RETURN_20260907.md`

That recovery result reports `SUCCESS` at the same bounded terminal state and independently rechecks all seven persisted sector sums/global totals while marking the legacy monolithic r=14 pointer `SUPERSEDED`. Consume it as an additional reproducibility/provenance cross-check; the current gate still owns the decision whether the evidence is recoverable under current policy.

## Observer/BRC boundary

Preserve every primitive-return-profile initial color, every ordinary 1-WL neighbor-multiset refinement branch, and the full anonymous stable packet. Use hashes only as integrity digests. Kernel/orbit coordinates establish exhaustive enumeration; they are not graph identity and not a stronger observer.

## Stop boundary

Do not work on `n=15` inside this recovery task. Return either an exact validated recovery of Q30 n=14 or the first reproducible mismatch/provenance gap.
