# HODGE H0L — Return Materialization Recovery

Date: `2026-08-23`
Status: `ACTIVE / DRIVER-ISSUED RECOVERY / NO_NEW_MATHEMATICS`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0L-RETURN-MATERIALIZATION-RECOVERY`
Owner branch to repair: `research/hodge-h0l-coniveau-support-collapse`
Recovery branch: `research/hodge-h0l-return-materialization-recovery`
Original taskbook: `research_tasks/HODGE_STAGE_H0L_CONIVEAU_SUPPORT_DOWNWARD_COLLAPSE_20260822.md`
Original taskbook source: `e74eeb9966f0adb7deb74408b74336c2aa20c542`

## 0. Driver finding

The researcher reports H0L complete, but the connected GitHub audit finds:

- original owner branch is still identical to original taskbook source (`ahead=0`, `behind=0`);
- no other branch matching `h0l` exists;
- repository code search finds no `HODGE_H0L_*` result artifacts;
- commit search finds no H0L return commit;
- PR search finds no H0L return;
- global-knowledge history contains only the H0L dispatch, not a completion return.

Freeze temporary control-plane status:

`H0L_RETURN_NOT_MATERIALIZED_REMOTE`.

This is **not** a mathematical failure and does **not** authorize recomputation, reinterpretation, or a successor research stage.

## 1. Single hard objective

`H0L_COMPLETED_RETURN_MATERIALIZED_ON_CANONICAL_OWNER_BRANCH_WITHOUT_NEW_MATHEMATICS`

The recovery actor must locate the already-completed local H0L work and publish exactly that return to:

`research/hodge-h0l-coniveau-support-collapse`

with the original taskbook source as the frozen base.

## 2. Forbidden

- no new theorem search;
- no change of scientific conclusion;
- no tuning of support grammar, bounds, baselines, or attribution after seeing the completed result;
- no opening H0M/H1;
- no rewriting H0L to improve outcome;
- no reading new downstream work in order to alter H0L;
- no replacing missing artifacts with a newly reconstructed answer unless the original completed payload is genuinely unrecoverable.

## 3. Required materialization

Publish the completed H0L result/checker artifacts required by the original taskbook, preserving their original semantics and researcher identity. At minimum the materialized return must make it possible for Driver to audit:

1. degree-2p algebraicity/coniveau equivalence typing;
2. full rational `H^4` control including `V_nonHdg,Q`;
3. Phase-A anti-leakage compliance;
4. support grammar and support certificates;
5. downward-collapse candidate(s);
6. fair source baseline sandwich;
7. attribution certificates;
8. R3/H1 classification;
9. deterministic checker output;
10. semantic checkpoint and manifest/digests.

If the completed payload used different filenames, retain them rather than renaming solely to satisfy this list, but provide a manifest mapping.

## 4. Integrity checks

Before push, verify:

- diff from `e74eeb9966f0adb7deb74408b74336c2aa20c542` contains only H0L return/checker artifacts and any strictly necessary return metadata;
- no historical taskbook/result modification;
- no control-plane policy mutation;
- no H0K result mutation;
- no protected worldview mutation;
- checker command/result and semantic digest are recorded.

If the completed return cannot be recovered, freeze instead:

`H0L_COMPLETED_PAYLOAD_UNRECOVERABLE`

with a precise inventory of what is missing. Do not silently regenerate a different research result.

## 5. Stop condition

Once the completed payload is pushed to the canonical owner branch, stop. Driver will perform the mathematical acceptance audit in a separate turn.
