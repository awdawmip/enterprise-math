# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.3`

`AGENTS.md` is an execution router, **not** a theorem catalog, research roadmap, task queue, Foundation summary, or current-achievement preload.

Detailed policies live in the canonical files named below and are loaded only when their function is material.

## 1. Precedence and mode resolution

Current explicit user instruction controls the current task/role scope.

More-specific current role/mode contracts control over generic wording in this file.

Research modes:

- explicit `EM_FREE_RESEARCHER` -> `FREE_AXIOM_DISCOVERY`;
- explicit user task, Driver handoff, approved taskbook or actual scheduler dispatch -> `TASK_RESEARCH`;
- explicit Driver activation -> `RESEARCH_DRIVER`.

A missing user topic by itself does **not** auto-dispatch a generic researcher and does not make a generic researcher FREE.

Canonical mode/role authority:

- `research_architecture.json`;
- `research_role_policy.json`;
- `research_identity_state_machine.json`.

## 2. Identity before substantive work

Resolve or allocate the role identity before substantive research:

- researcher -> `Researcher-ID`;
- Driver -> `Driver-ID`.

Reuse the current conversation's valid identity when one already exists. Driver-mediated manual dispatch uses the preallocated Researcher-ID from the dispatch envelope. Scheduler/direct entry follows the identity state machine.

Identity registration is nonblocking; failure to update a directory is not a mathematical `HARD_BLOCK`.

Exact identity mechanics:

- `research_identity_state_machine.json`;
- `docs/RESEARCH_IDENTITY_PROTOCOL.md`.

## 3. FREE_AXIOM_DISCOVERY information boundary

FREE Phase A receives the **primitive substrate**, not the current-achievement catalog.

Canonical FREE substrate router:

`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`.

Before first candidate freeze:

- do not preload `definitions/00_CURRENT_NATIVE_FOUNDATION.md`;
- do not preload Common Surface/current-result catalogs, scheduler/task/route state, Relay/PR/recent-history context or Driver Continuity;
- do not inherit another branch's `WORKING_TRUTH`;
- do not use current success/failure vocabulary, available tools, implementation representations or file order to choose the question;
- do not supply a suggested-question or discovery-lens menu;
- use generic exclusion categories rather than enumerating salient forbidden current results.

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

FREE candidate provenance and Phase-B audit are governed by:

- `research_roles/EM_FREE_RESEARCHER_ROLE.md`;
- `research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md`;
- `research_axiom_candidate_state_machine.json`.

## 4. TASK_RESEARCH hot start

For an explicit selected task, use the smallest sufficient packet.

Normal source-read order:

1. this `AGENTS.md` router if not already loaded;
2. **the exact task entry** — taskbook/theorem/spec/code object;
3. **the first exact dependency actually required to begin**.

Then work.

Soft routine source-read budget before substantive work: `<= 3`.

The Common Surface is an ownership/tool/conflict **lookup**, not the automatic second read.

General current-result router:

`definitions/00_CURRENT_NATIVE_FOUNDATION.md`

is loaded only when the selected task actually needs current foundation/result routing.

## 5. Working Truth boundary

`WORKING_TRUTH` is a TASK execution discipline after an explicit Driver direction freeze or Driver-approved taskbook.

It is not a FREE Phase-A premise and not a raw-candidate status.

Once activated, pursue the frozen task direction decisively while preserving maximal proof/evidence audit rigor and exact external status.

It may be overturned only by:

- explicit user/Driver supersession;
- exact same-premise counterexample;
- formal contradiction;
- theorem-critical frozen checker/certificate failure.

Detailed Driver behavior:

`docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md`.

## 6. Evidence and semantic integrity

Never fabricate proof, computation, hashes, validation status, novelty, provenance or tool results.

Keep statuses exact. Conjectural, computed/executable-checked, proved, formal/Lean-checked and canonical-main are distinct.

Finite enumeration or successful software is not automatically a theorem proof.

Preserve exact negative results and counterexamples rather than editing definitions after the fact to hide them.

For foundation-facing inverse/recovery reasoning, load:

- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json`.

Before freezing a claim as native/intrinsic/base-world, load:

- `native_semantics_admissibility.json`.

These are **triggered** policies, not universal Phase-A FREE preloads.

## 7. Candidate -> task -> continuation provenance

Freeze:

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

A task opened from FREE discovery preserves audited candidate origin/ID/state.

Task lineage is semantic provenance and cannot be reset by renaming.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, and explicit consideration of closure/another owner/free exploration.

Exact taskbook contract/tooling:

- `research_taskbook_contract.json`;
- `research_taskbook_policy.json`;
- `docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md`;
- `tools/research_taskbook.py`.

## 8. Remote liveness

Core invariant:

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

Do not perform universal scheduler/Issue/PR/CI/repository-tree preflight.

Use remote systems when their function becomes material, and reuse immutable fetched blobs/SHAs within one execution phase.

Do not poll CI/review/status merely to wait for change.

Do not repeatedly reconcile against moving `main` without a concrete current action.

Only a complete mathematical/research `HARD_BLOCK` with:

- `missing_object`;
- `owner`;
- `necessity`;
- `unblock_condition`

may stop a research route. Tool/scheduler/CI availability is not such a block.

Detailed remote rules:

`docs/GITHUB_INTERACTION_BUDGET.md`.

## 9. Triggered control surfaces

Load only when relevant:

- branch/scope/promotion work -> owner-isolation protocol;
- actual scheduler dispatch/reconciliation -> scheduler protocol/state;
- Foundation feedback/verification -> Foundation Steward/backflow contracts;
- Driver portfolio decision -> Driver contract + continuity when needed;
- test diagnosis -> test-diagnostic liveness;
- Lean diagnosis -> Lean-diagnostic liveness;
- cross-owner theorem/tool lookup -> Common Surface;
- exact current math generation/current-result lookup -> current native foundation router.

Do not recursively traverse these surfaces merely because they exist.

## 10. Persistence and publication

L1/L2/L3 research is remote-silent between semantic checkpoints by default.

Publish when a coherent semantic checkpoint, handoff, loss-risk boundary, explicit user request or promotion payload exists.

One bounded owner generation normally uses one owner branch and at most one Draft PR.

Journal/continuity/promotion have distinct meanings:

- journal = what happened / provenance;
- Driver Continuity = pending routing state only;
- source task/result files = exact research content;
- source `main` = canonical truth only after the applicable gates.

## 11. Promotion liveness

Freeze:

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 promotion remains serialized as **one bounded active promotion attempt at a time**. Ready/non-Draft status is candidate status, not a permanent lock.

Strict `NO_NEW_MATHEMATICS` governance maintenance uses its own bounded attempt under:

`docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

Governance maintenance may not smuggle theorem/native-definition/evidence/ownership changes.

## 12. No hidden startup tax

Do not satisfy rigor by loading everything.

Correct pattern:

- FREE -> primitive substrate -> self-generated question -> candidate freeze -> Phase B expansion;
- TASK -> exact task -> first dependency -> work -> triggered expansion;
- Driver -> exact decision evidence -> route;
- Steward -> exact maintenance/verification evidence -> classify.

The existence of a policy, theorem catalog, tool, branch or current success is not itself a reason to load it.
