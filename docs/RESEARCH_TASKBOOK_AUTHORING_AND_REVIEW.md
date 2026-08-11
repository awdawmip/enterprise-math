# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS`

## Purpose

A taskbook is a task-specific research contract, not a second copy of repository operating policy and not a binding to one runtime conversation.

Researchers already load the repository execution rules. Therefore a taskbook should contain only:

- the mother question and task-local semantics;
- frozen inputs, assumptions, dependencies and exclusions;
- exact deliverables and evidence requirements;
- PASS / KILL / return criteria;
- any **intentional temporary override** of inherited repository policy.

The taskbook should not repeat generic GitHub, CI, identity, scheduler, ownership, promotion, liveness, or completion rules merely for emphasis.

## Canonical flow

### 1. Generate

Create new taskbooks through:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --kind RESEARCH \
  --priority P1 \
  --leverage HIGH \
  --lane R... \
  --output research_tasks/....md
```

The generator writes the required Driver/identity-policy metadata and a `policy_review` block stamped against the current policy set, initially as:

`PENDING_DRIVER_REVIEW`.

It deliberately creates only a task-local skeleton. It does **not** assign a fixed runtime Researcher-ID.

### 2. Write task-local content

Fill the taskbook with the actual mathematical/research problem.

Do **not** paste repository rules into the body. If the instruction would still be true for nearly every Enterprise Math task, it probably belongs in repository policy rather than in this taskbook.

### 3. Automatic conflict audit

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

The audit checks:

- required taskbook metadata;
- forbidden fixed runtime identity metadata;
- policy-sensitive directives that appear to alter GitHub/CI, scheduler, promotion, or similar inherited behavior;
- generic repository-policy restatement;
- temporary override schema;
- whether the taskbook policy stamp matches the current repository policy digest.

A machine pass does not replace Driver judgment. It prevents silent policy drift and catches known conflict classes before dispatch.

### 4. Declare temporary overrides only when genuinely needed

If a task must intentionally differ from inherited policy, record a narrow entry in:

`policy_review.temporary_overrides`.

Every override must contain:

- `conflict_id`;
- `scope`;
- `reason`;
- `replacement_behavior`;
- `expires_when`.

Example shape:

```json
{
  "conflict_id": "TB-REMOTE-RUNTIME",
  "scope": "one final validation after a complete proof candidate exists",
  "reason": "the repository-pinned compiler is unavailable locally",
  "replacement_behavior": "one batched remote validation; no iterative remote proof loop",
  "expires_when": "the validation result is captured or the task ends"
}
```

An override is not permission to weaken theorem truth, safety, authorization, owner isolation, or canonical promotion rules. It only replaces the named inherited behavior inside the declared scope and lifetime.

### 5. Driver approval stamp

After machine findings are resolved and any override has been reviewed:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

This records the current policy digest and sets:

`policy_review.review_state = PASS`.

### 6. Taskbook dispatch gate

Immediately before dispatch or re-dispatch:

```bash
python tools/research_taskbook.py audit research_tasks/<task>.md --dispatch
```

A taskbook is dispatchable only when this passes.

### 7. Bind runtime identity outside the taskbook

For a **Driver-mediated manual relay** into a new researcher conversation, taskbook PASS is not the last mechanical step. The Driver must preallocate the concrete runtime Researcher-ID in a separate dispatch envelope:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

Persist that Researcher-ID in:

- the `USER_RELAY_QUEUE` entry;
- the user-visible handoff prompt;
- the first researcher return/PR/commit metadata.

The receiving conversation starts with that ID already bound. Do not rely on the researcher remembering to invent or allocate an ID later.

This identity binding lives **outside** the taskbook because a taskbook may be reused by a later/new conversation. The same researcher conversation preserves its existing Researcher-ID on continuation; a new dispatch envelope normally gets a new one.

Scheduler CLAIMs and direct self-started research keep their own automatic bootstrap paths.

Driver conversations use `Driver-ID`; they do not consume the `Researcher-ID` visible label.

## Rule updates automatically invalidate old review stamps

`research_taskbook_policy.json` names the repository files that form the inherited taskbook policy set.

The tool computes a SHA-256 digest from the contents of that set.

Therefore:

1. a Driver reviews a taskbook against policy version `P`;
2. one inherited rule later changes;
3. the policy digest changes automatically;
4. the old taskbook stamp becomes stale;
5. `audit --dispatch` fails;
6. the Driver must review the still-live taskbook again and approve a new stamp.

The updated rule is therefore reflected in the taskbook by a new review digest, **without copying the rule text into the taskbook**.

Historical unstamped taskbooks may remain in the repository. They are not automatically rewritten. But they cannot be newly dispatched under the current process until reviewed and stamped.

## Policy-update procedure

When a repository execution rule covered by `research_taskbook_policy.json` changes:

1. change the canonical rule once;
2. do not manually copy the change into every taskbook;
3. run the taskbook audit on any still-live taskbook before its next dispatch;
4. re-review only the tasks that remain active/reusable;
5. update task-specific text only where the new rule creates an actual conflict or changes a temporary override;
6. if the task is being manually relayed by Driver, bind a runtime Researcher-ID in the relay envelope after the new taskbook PASS stamp.

The policy digest handles synchronization. Taskbook text changes only for semantic conflicts or explicit overrides.

## Design rule

The normal taskbook should be shorter after this protocol, not longer.

A good taskbook answers:

> What exactly is different about this task?

The repository policy answers:

> How does an Enterprise Math participant operate in general?

The dispatch envelope answers:

> Which concrete researcher conversation is executing this approved task now?

Keeping those three layers separate prevents contradictory duplicated rules, missing runtime identity, and stale taskbooks reopening previously closed operational loopholes.
