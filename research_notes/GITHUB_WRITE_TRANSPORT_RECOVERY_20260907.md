# GitHub write transport recovery — 2026-09-07

Status: CONTROL_PLANE_ONLY / CURRENT WRITE-ROUTE RUNBOOK
Scope: preserve and upload an already-authorized frozen bundle; no new mathematics, research-role authority or review disposition.

## Current route

The current explicit user instruction permits the assistant to choose direct commits/updates to the intended ref or branch → PR → merge. Earlier main-only/no-PR restrictions from an older conversation do not govern this write-route choice. Use [the current GitHub interaction budget](../docs/GITHUB_INTERACTION_BUDGET.md#21-current-write-route-choice) and the actions actually advertised by the active connection. Existing owner/claim, task-publication, immutable-record, test and mathematical-admission contracts remain unchanged. A global-knowledge staging branch is still noncanonical until the accepted content reaches canonical main.

A frozen upload remains the same bundle when its transport changes. Keep each package's task/bundle identifier, source ref, file paths, exact bytes and hashes. A repeated round label alone is not a bundle identifier. Do not combine different packages' manifests or replay completed mathematics to repair an upload.

## Recovery sequence for an older conversation

1. **Recover the frozen payload.** Record the exact repository, bundle/task identifier, source commit or local frontier, target paths, byte lengths, UTF-8/binary representation, SHA-256 hashes and known remote checkpoint. Reuse the original bytes, including line endings. Keep separate manifests for separate packages. If bytes are unavailable, identify the missing artifact; do not regenerate a mathematical result merely to reconstruct an upload.
2. **Resolve the current write capability.** Use the current advertised connector action names and schemas. Supply the repository owner/name and explicit target branch/ref; do not reuse a cached endpoint or assume a similarly named action has the old parameters. Rebase the cached write plan to the current route without changing the research scope or frozen payload.
3. **Choose one available route.** For a direct update, read the target file/head and use its expected identity/CAS where supported. For a branch route, create or reuse the intended branch from an explicitly read base SHA, upload the bundle, then use an authorized PR/merge when needed. File-write, multi-file commit, or Git blob/tree/commit actions are alternatives when they preserve the same bytes, target and transaction requirements. Keep an atomic multi-file unit atomic; an equivalent action must not split it into partial authority-bearing updates.
4. **Handle one failed request precisely.** Retain the action name, repository, ref, status/error, timestamp and available request/correlation identifier. Do not log credentials. A `create_blob`/`Resource not found` failure does not prove all writes, all connections, or that endpoint globally are unavailable. If the advertised capability or target binding differs, correct that concrete mismatch; otherwise try a currently available equivalent authorized write action once instead of looping on the unchanged request. Inspect the target for a possible prior success before retrying an uncertain write.
5. **Read back the committed result.** Record the returned commit SHA. Read every intended path from that immutable commit and compare exact bytes/hashes with the frozen manifest. A blob SHA alone does not mean a branch/file was updated. When using PR/merge, also verify that the intended target ref contains the verified payload after merge. Report only the actions and paths actually verified.
6. **Resume the original objective.** Keep the verified remote checkpoint and continue from the original unfinished unit. A successful probe is transport evidence, not a new Result, Driver review or mathematical admission. If the old connection still fails and no equivalent write is callable, retain the ready-to-upload bundle and the single unresolved transport diagnosis; do not change account/plugin permissions or restart research as a substitute.

## Fixed successful probe evidence

The owner supplied the following successful tool results from the current conversation. This runbook preserves that evidence; it does not claim to have repaired the older conversation's binding.

| Object/action | Verified identity or outcome |
|---|---|
| Repository | `awdawmip/enterprise-math`; metadata reported default branch `main`, not archived, and push permission on the current connection |
| `create_branch` | `maintenance/em-github-write-recovery-20260907`, based on exact main commit `fbb1b7a58c7530070ea9b14de829fe447950372f` |
| `create_file` | UTF-8 `research_notes/GITHUB_WRITE_TRANSPORT_RECOVERY_20260907.md`; commit `d1fb64cd2d9daf9768ed79a1614e0f33b849b892` |
| Exact-commit readback | Owner read the full original probe file from that exact commit and verified its content |
| Original probe bytes | 1,481 UTF-8 bytes / 1,475 characters; SHA-256 `6518cf6c213a193b47af3afd65f8ff00bef452612e0f25596224b0eab01724c1` |
| Original Git blob | `4933b241a0eaa572fb9c73d3bf1196b829eaf4b1` |
| Current advertised `github_create_blob` | The same frozen probe text succeeded against the same repository and returned the exact original blob above; the existing object was reused, with no new file or commit |

The original file and its probe wording remain available at [the immutable probe commit](https://github.com/awdawmip/enterprise-math/blob/d1fb64cd2d9daf9768ed79a1614e0f33b849b892/research_notes/GITHUB_WRITE_TRANSPORT_RECOVERY_20260907.md). Its recorded owner was `EM-DVR-01E1D9 / CONTROL_PLANE`, with `Global-Knowledge-Sync: main@314275a / GLOBAL_KNOWLEDGE_V1`. Those identify the original probe, not a new role activation by the editor of this runbook.

The local documentation editor independently matched the original committed Git blob, byte length and SHA-256 before replacing this note with the runbook. The hashes above describe the original probe at `d1fb64cd…`, not the expanded current note.

## Diagnosis boundary

The older conversation reported `Resource not found` during branch creation or upload while reads succeeded. Its raw request/correlation identifier and exact connection/action mapping have not been obtained; its endpoint root cause remains unlocated. The successful current `create_branch`, `create_file` and `create_blob` calls establish those operations for this current connection, not automatic recovery of every older conversation.

At the owner's inspected Enterprise Math `2dd4c296f713f6bb3b2e509ba65104dc4a2a8ce0` workflow snapshot, no branch-deletion or PR-prohibition workflow was identified. The separately identified global-knowledge branch-enforcement workflow belongs to `awdawmip/chatgpt-global-knowledge`; the owner disabled it and read workflow `352137881` as `disabled_manually` at 2026-09-07 14:56 UTC. [Global knowledge PR #51](https://github.com/awdawmip/chatgpt-global-knowledge/pull/51) then removed the workflow and replaced the current branch/PR prohibition with optional publication routes. Its merged commit `7d3390037d828a58af68dc68bc236a907bc42fa2` has the exact independently reviewed tree `9e95343d11d3ea137b5ba6e8a6bb47f0282fe606`; both online checks passed. This completed a real branch → upload → PR → merge path in that repository. That separate repository's workflow does not explain an Enterprise Math `create_blob` 404. Do not turn either observation into an unverified permission or endpoint diagnosis.

The owner ran the shipped global-knowledge sync with `-BeforeWrite` at 2026-09-07 15:09:30 UTC and read canonical `982a4404689e7abdc2b060967474880c321afdf7`. This snapshot contains the merged policy and the subsequent generated-index refresh; the new write-route rules were read from its canonical entrypoints. This runbook changes the current GitHub write/recovery route; existing research authority and admission requirements continue to apply.

Global-Knowledge-Sync: main@982a440 / GLOBAL_KNOWLEDGE_V1
