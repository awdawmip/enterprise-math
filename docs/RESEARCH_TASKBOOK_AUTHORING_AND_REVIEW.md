# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V4`
Effective: `2026-08-25`
Contract: `research_taskbook_contract.json`
Scheduler: `research_scheduler_v2.json`
Architecture: `research_architecture.json`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`

## Purpose

A taskbook is a **task-specific research contract**. It is not:

- a second copy of repository policy;
- runtime READY/DONE authority;
- a fixed conversation identity binding;
- a raw free-research candidate;
- a way to erase task origin/lineage;
- automatic evidence that a successful stage deserves another stage.

A good taskbook contains the mother question, frozen inputs/scope, deliverables/evidence, PASS/KILL/return criteria, origin, lineage, and any narrow temporary override.

Freeze:

`TASKBOOK_POLICY_PASS != SCHEDULER_READY`.

`TASKBOOK_FILE != RUNTIME_STATE_AUTHORITY`.

## 1. Who may author

Current allowed author roles:

- `RESEARCHER`;
- `RESEARCH_DRIVER`;
- `STEWARD`.

A FREE researcher may author a taskbook after its candidate has reached the audited intake-eligible maturity required by the candidate lifecycle.

Authorship does not grant dispatch authority. New taskbooks use:

`task_authority = SCHEDULER_REVIEW_REQUIRED`.

Legacy `DRIVER_APPROVED` taskbooks remain historical artifacts; the V2 migration may explicitly import still-live ones, but the new authoring tool never emits that authority.

## 2. Declare task origin

Every new taskbook declares `origin_kind`:

- `DIRECT_USER_DIRECTION`;
- `DRIVER_ROADMAP`;
- `FREE_AXIOM_CANDIDATE`;
- `FOUNDATION_QUESTION`;
- `REPLAY_OR_INTEGRATION`;
- `MAINTENANCE`.

If `origin_kind=FREE_AXIOM_CANDIDATE`, include the audited `origin_candidate_id` and `origin_candidate_state`. A raw candidate may not become a task by relabeling it `DRIVER_ROADMAP`.

If `origin_kind=FOUNDATION_QUESTION`, include `origin_foundation_question_id`.

## 3. Choose task lineage

Every new taskbook declares:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

A continuation requires:

- `parent_task_id`;
- `new_information_gap`;
- `why_parent_result_does_not_close_it`;
- `discriminating_outcomes`;
- `kill_condition`;
- `alternative_route_or_free_exploration_considered`;
- `why_new_stage_or_task_is_better_than_same_task_or_closure`.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

Stage 2+ is continuation semantics. Renaming does not reset lineage.

## 4. Generate

Driver-authored example:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --author-role RESEARCH_DRIVER \
  --origin-kind DRIVER_ROADMAP \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

Researcher-authored example:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --author-role RESEARCHER \
  --origin-kind DIRECT_USER_DIRECTION \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

FREE candidate-derived example:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --author-role RESEARCHER \
  --origin-kind FREE_AXIOM_CANDIDATE \
  --origin-candidate-id AX-... \
  --origin-candidate-state AUDITED_AXIOM_CANDIDATE \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

The generator starts at:

`DRAFT / POLICY_REVIEW_PENDING / NOT PUBLISHED / NOT DISPATCHABLE`.

It never assigns a fixed runtime Researcher-ID.

## 5. Write only task-local content

Include only what differs for the task:

- mother question;
- frozen inputs/assumptions/exclusions;
- exact mathematical/executable/formal outputs;
- task-local witnesses/discriminators;
- PASS/KILL/return criteria.

Do not paste generic scheduler, GitHub, identity, promotion, liveness, Working Truth or candidate-lifecycle policy into the body.

## 6. Policy review

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

Resolve findings, then:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

This sets:

`policy_review.review_state = PASS`

and changes a new `DRAFT` taskbook to file-level:

`base_state = PUBLISHED`.

This means **ready to publish into the scheduler**, not ready to execute.

Strict pre-publication audit:

```bash
python tools/research_taskbook.py audit research_tasks/<task>.md --publish
```

`--dispatch` remains a legacy alias for this strict taskbook audit only. Actual dispatch is exclusively a Scheduler V2 review transition.

## 7. Publish — task registration

After taskbook policy PASS, emit a V2 publication event:

```bash
python tools/research_scheduler.py emit-publish \
  --taskbook research_tasks/<task>.md \
  --publisher-role RESEARCHER \
  --publisher-id EM-... \
  --actor <actor>
```

Use `RESEARCH_DRIVER` or `STEWARD` as publisher role where applicable.

Append the emitted JSON to the configured runtime event log.

The task now exists in the scheduler as:

`PUBLISHED / NEEDS_REVIEW`.

At this point it is official and visible, but not claimable.

## 8. Driver dispatch review

An eligible Driver evaluates the published task and emits:

```bash
python tools/research_scheduler.py emit-review \
  --task-id RS-... \
  --review-stage DISPATCH \
  --verdict ACCEPT \
  --reviewer-id EM-DVR-... \
  --review-ref driver_reviews/... \
  --actor <actor>
```

Outcomes:

- `ACCEPT -> READY`;
- `CHANGES_REQUESTED -> PUBLISHED`;
- `REJECT -> REJECTED`.

If a Driver-ID published the task, that same Driver-ID cannot perform the accepting DISPATCH review.

A policy-review stamp and a scheduler Driver review are intentionally different objects.

## 9. Runtime execution identity

The reusable taskbook stays runtime-ID-free.

Scheduler `CLAIM` allocates/resolves Researcher-ID for the execution lease. Driver-mediated manual relay may preallocate Researcher-ID in the dispatch envelope. Driver review uses Driver-ID in scheduler review events.

Publication identity, execution identity, and review identity remain separately auditable.

## 10. Return and completion

The executor finishes with:

`RETURN -> RETURNED / NEEDS_REVIEW`.

A Driver then performs `REVIEW(stage=RETURN)`.

- `ACCEPT -> DONE`;
- `CHANGES_REQUESTED -> CHANGES_REQUESTED` and the repair becomes claimable.

The executor cannot make its own V2 task DONE.

## 11. Orphans

Lease expiry creates `ORPHANED`, never a silent HANDOFF_READY. An explicit orphan record may capture branch, last commit, source ref, previous identity, last progress and next action.

Recovery is a Driver action and preserves orphan history.

## 12. Temporary overrides

`policy_review.temporary_overrides` remains the only task-local mechanism for an intentional narrow policy difference. It cannot weaken theorem truth, safety, authorization, owner isolation, candidate maturity, origin/lineage, independent review, orphan persistence, or canonical-promotion rules.

## 13. Policy changes invalidate old stamps

`research_taskbook_policy.json` hashes the inherited policy inputs. When relevant policy changes, the digest changes.

Historical taskbooks remain provenance. A new PUBLISH/re-dispatch under current V2 policy requires current applicable review. An already-running execution is not retroactively erased; subsequent control-plane actions use current rules.

## Design separation

Repository policy answers: **How does Enterprise Math research operate?**

Candidate packet answers: **What was discovered before selection?**

Taskbook origin/lineage answers: **Why does this task exist?**

Taskbook body answers: **What exact question is proposed/executed?**

Scheduler PUBLISH answers: **Is this an official registered task?**

Driver DISPATCH review answers: **May it execute now?**

CLAIM answers: **Which researcher execution owns the lease?**

RETURN answers: **What result is submitted?**

Driver RETURN review answers: **Is the declared task workflow complete?**

Keeping these layers separate prevents provenance laundering, self-authorization, hidden tasks, stale identities and silent orphan loss.
