# Enterprise Math Governance Maintenance Liveness

Status: `ACTIVE / NARROW GOVERNANCE-MAINTENANCE OVERRIDE`
Effective: `2026-08-22`
Driver-ID: `EM-DVR-K7Q4N8`
Narrow authority over: `docs/GITHUB_INTERACTION_BUDGET.md` Section 8 **only for NO_NEW_MATHEMATICS governance maintenance**.

## Purpose

Prevent a stale or merely ready mathematical promotion candidate from becoming an indefinite repository-wide lock while preserving strict serialization of actual mathematical canonical promotion.

This protocol changes **promotion liveness**, not mathematical truth gates.

Freeze:

`READY_PR != PROMOTION_LANE_LEASE`.

`GOVERNANCE_MAINTENANCE != MATHEMATICAL_L4_PROMOTION`.

## 1. Mathematical L4 promotion lane

Mathematical/foundation-truth promotion remains serialized.

A PR being non-Draft or ready-for-review makes it a **candidate**. It does not by itself acquire an indefinite lane lease.

The mathematical L4 lane is occupied only during one bounded Driver promotion attempt:

`SELECT -> CURRENT_MAIN_SNAPSHOT -> CONFLICT_SNAPSHOT -> FROZEN_HEAD_VALIDATION -> FINAL_COMBINATION -> MERGE_OR_DEFER -> RELEASE`.

At most one such mathematical promotion attempt is active at a time.

The attempt ends on merge, explicit defer, conflict, failed gate, or inability to complete the bounded admission pass. There is no waiting/polling lock.

Therefore:

`READY_STATUS != ACTIVE_ATTEMPT`.

`STALE_OR_UNMERGEABLE_READY_PR != PERMANENT_LANE_LOCK`.

## 2. Governance-maintenance lane

A separate bounded governance-maintenance attempt may proceed while mathematical L4 candidates exist, including ready candidates, provided the payload satisfies every eligibility gate below.

Only one governance-maintenance merge attempt should be active at a time.

A governance attempt uses:

`SELECT -> CURRENT_MAIN_SNAPSHOT -> PATH/SEMANTIC_CONFLICT_AUDIT -> GOVERNANCE_REGRESSION -> EXPECTED_HEAD_MERGE_OR_DEFER -> RELEASE`.

It must not wait on or modify an unrelated mathematical L4 candidate.

## 3. Governance-maintenance eligibility

A payload is eligible only when all are true:

1. classification is `NO_NEW_MATHEMATICS`;
2. it does not introduce a new theorem, strengthen/weaken a theorem claim, change proof status, reinterpret evidence, or silently change theorem ownership;
3. it does not introduce a new native mathematical definition or change the semantic content of a frozen current definition;
4. pure authority-routing reconciliation is allowed only when it makes stale source/router/status text point to an already-frozen canonical definition and preserves exact provenance;
5. its changed-file set is explicitly audited against current `main` and any simultaneously relevant mathematical/governance payload;
6. any semantic/path overlap is either absent or explicitly resolved before merge;
7. relevant governance/static regression checks are present and pass to the strongest available extent; unavailable validation is disclosed rather than invented;
8. the final merge uses a fresh current-main snapshot and an atomic/expected-head guard when the merge surface supports one;
9. the payload does not use the governance lane to bypass required mathematical L4 gates.

If any theorem/native-definition/evidence-strength question is genuinely unresolved, classify the payload as mathematical/Foundation promotion instead of governance maintenance.

## 4. Authority reconciliation class

The following may qualify as governance maintenance when the no-new-mathematics proof is explicit:

- stale router/status repair;
- machine/human policy synchronization;
- role/scheduler/taskbook/identity/governance contract repair;
- historical/superseded status retyping;
- source authority reconciliation to an already-frozen later canonical definition;
- deterministic reference/lineage/bilingual metadata repair.

A file path named `definition` does not automatically make a change mathematical, and a governance label does not automatically make it non-mathematical. Classification follows the **semantic delta**.

## 5. Conflict with mathematical L4

Governance maintenance may proceed beside a ready mathematical L4 candidate only when it does not alter the mathematical candidate's theorem content, assumptions, proof artifacts, target source files, or required validation semantics.

If a governance change changes the rules under which the mathematical candidate must be admitted, the Driver must classify whether the L4 candidate needs revalidation under the new rule before its later merge. This does not make the governance repair wait indefinitely.

## 6. No persistent promotion locks

Do not persist statements such as:

`PR #X owns the lane until it merges`.

Persist only candidate/queue facts. At actual merge time, acquire the bounded attempt by current Driver action and release it in the same execution phase.

Driver Continuity may say that an L4 candidate exists, but must not treat readiness alone as an eternal lock.

## 7. Current-main and concurrency discipline

A governance merge is a concurrency-sensitive write. Immediately before merge:

- refresh `main` once;
- compare the frozen governance head against that observed main;
- audit newly appeared paths/semantic dependencies once;
- merge with the frozen expected head when supported;
- if the base moves again or a real conflict appears, defer rather than loop.

Never force-update `main` to make governance land.

## 8. Relationship to Research Architecture V2

This is the promotion-liveness component of `research_architecture.json`.

Research Architecture V2 continues to require:

- exploration/exploitation separation;
- candidate maturity before task/Foundation routing;
- task origin/lineage provenance;
- `PASS_IS_NOT_A_SUCCESSOR_TRIGGER`;
- exact claim status;
- gated mathematical canonical truth.

This file only prevents **control-plane starvation** from being mistaken for mathematical rigor.
