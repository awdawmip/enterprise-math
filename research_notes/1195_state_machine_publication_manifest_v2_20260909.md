# #1195 reconciled state-machine publication manifest

Status: `CURRENT / RECONCILED AGAINST ALL DURABLE #1195 COMMENTS THROUGH CP34`
Parent objective: `EM-PI-POWER-SPECTRAL-SELECTOR`
Publisher: `EM-FREE-8C31A2`
Base handoff: `research_notes/1195_research_handoff_index_20260909.md`
Post-CP16 delta: `research_notes/1195_research_handoff_postcp16_20260909.md`

## Current claimable heads

### A. Rank-5 pi-free q-selector arithmetic descent

- Task: `RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD`
- Current publication: `TP2-C107B5EB1A53099EECB1`
- Generation: `2`
- Supersedes: `TP2-AED4C763FDB7C4C2A688`
- Record: `research_task_records/RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD/TP2-C107B5EB1A53099EECB1.json`
- Taskbook: `research_tasks/1195_RANK5_SELECTOR_GALOIS_CLASSFIELD_GEN2_20260909.md`
- Pinned taskbook blob: `sha1:08b98a11b55bf7632ca1cc774fac4307f6ac1117`
- State: `ACTIVE / claimable=true / P2 / MEDIUM / taskbook-unassigned`
- Frontier: prove or kill algebraicity/Galois transport of the two CP19 pi-free projective q-ratios at a proved modular/CM rank-5 specialization.

### B. Projected middle-selector relative p-adic depth

- Task: `RS-1195-RANK-SPINE-PADIC-BRIDGE`
- Current publication: `TP2-5805E8EDC14073894F86`
- Generation: `2`
- Supersedes: `TP2-F80964DD3AFA26525AE8`
- Record: `research_task_records/RS-1195-RANK-SPINE-PADIC-BRIDGE/TP2-5805E8EDC14073894F86.json`
- Taskbook: `research_tasks/1195_RANK_SPINE_PADIC_BRIDGE_GEN2_20260909.md`
- Pinned taskbook blob: `sha1:24d316090831da55009a80ad31f4c289a52f80c6`
- State: `ACTIVE / claimable=true / P2 / MEDIUM / taskbook-unassigned`
- Frontier: after the middle filtration supplies the leading `p^c`, prove or kill the additional relative `p^(c+1)` depth for the projected middle selector, first at `c=2`, then pressure-test `c=3`.

## Closed stale publication

### Exact finite selector interval/height certificate

- Task: `RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT`
- Terminal publication: `TP2-C7375AAF8C87B4980193`
- Generation: `2`
- Supersedes stale open generation: `TP2-1F53456CF4C21AC62FB6`
- Record: `research_task_records/RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT/TP2-C7375AAF8C87B4980193.json`
- Taskbook: `research_tasks/1195_SELECTOR_INTERVAL_HEIGHT_CERT_CLOSED_20260909.md`
- Pinned taskbook blob: `sha1:aa517444153369a8b7c1cace24d222dc460fafb9`
- State: `CLOSED / claimable=false`
- Durable completion evidence: Issue #1195 comment `5540958862`, exact rational interval certificate.

## Current-head reasoning

The immutable-record reducer treats a publication named by a later `supersedes_publication_id` as non-head. It also excludes terminal states `PARKED`, `SUPERSEDED`, and `CLOSED` from current claimable heads. Therefore:

- the rank-5 task has exactly one current active head: `TP2-C107B5EB1A53099EECB1`;
- the p-adic task has exactly one current active head: `TP2-5805E8EDC14073894F86`;
- the interval task has no active head because its generation-2 terminal record supersedes generation 1.

All three generation-2 records were read back remotely and their `taskbook_blob_sha1` values match the pinned taskbook blobs above.

## New-researcher intake

Do not start from Issue #1195 chronologically. Read the base handoff, then the post-CP16 reconciliation handoff, then the selected current taskbook. The taskbook lists only the checkpoint comments needed for its exact frontier. Completed units are dependencies to consume, not work to replay.