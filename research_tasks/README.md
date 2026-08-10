# Enterprise Math research taskbooks

This directory contains executable research handoffs produced by the research-scout / Research Driver workflow.

A taskbook is both a human-readable Markdown brief and a static scheduler task through its leading `ENTERPRISE_MATH_TASK_V1` JSON block. The central `research_scheduler.json` remains the legacy owner/frontier registry; new Driver-approved taskbooks do not require a central JSON edit because `tools/research_scheduler.py` merges taskbooks into the effective state machine at read time.

Typical lifecycle:

```text
researcher executes assigned task
  -> may discover side branches without stopping research
  -> batch worthwhile branches into a compact proposal bundle at checkpoint/handoff
  -> Driver reviews proposal queue
  -> Driver may create one approved taskbook
  -> scheduler sees READY automatically
  -> researcher CLAIM (best effort; long lease)
  -> remote-silent research
  -> semantic checkpoint / HANDOFF / DONE
  -> reusable results route to real owners and canonical promotion
```

The taskbook itself is research input, not theorem truth.

## Role and task authority

Machine-readable authority is defined by `research_role_policy.json`.

Default session role is:

```text
RESEARCHER
```

A conversation becomes `RESEARCH_DRIVER` only after the user explicitly assigns Driver role in that current conversation (for example, `你现在是驾驶员`). Do not infer Driver authority from memory, another Project, repository state, or the fact that a useful new direction was discovered.

Researchers retain full scientific freedom: they may reason, prove, disprove, experiment, compute, formalize, write notes, write reports, and produce handoff artifacts. The restriction is on **scheduling authority**, not scientific exploration.

A new dispatchable taskbook must carry:

```json
{
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED"
}
```

Taskbooks that predate the role policy are grandfathered by stable task ID so ongoing work is not interrupted. A taskbook-like Markdown document created by a Researcher is ordinary research material and has **no scheduler authority**; it is not `READY` or claimable merely because it looks like a taskbook.

## Proposal capture without Markdown floods

Researchers do not need to stop work and create a separate task file for every promising branch. At a semantic checkpoint or handoff, related side branches may be batched into one compact `ENTERPRISE_MATH_PROPOSAL_BUNDLE_V1` JSON file under `research_proposals/`.

Proposal candidates are non-dispatchable and default to `PENDING_DRIVER_REVIEW`. The Driver may later `APPROVE`, `MERGE`, `PARK`, or `REJECT`; approval is materialized by creating a Driver-authorized taskbook here. Proposal files never become tasks by themselves.

If no proposal write path is available, include a compact `proposal_candidates` section in the ordinary handoff instead of generating standalone taskbook Markdown in chat. Role/proposal governance is never a `HARD_BLOCK`: continue the assigned research and defer routing paperwork to the next meaningful checkpoint.

## Context isolation

Every research task, including legacy scheduler tasks, inherits the non-weakenable context contract from `research_context_policy.json`:

```text
context_mode = TASK_ISOLATED
memory_policy = UNTRUSTED_HINT_ONLY
cross_task_import_policy = EXPLICIT_ONLY
```

This means a researcher starts from the selected taskbook, current repository rules, current canonical source required by that task, declared `source_refs` / dependencies, and task-local evidence. ChatGPT/Project/account memory, prior conversations, GLOBAL_KNOWLEDGE journal material, other taskbooks, other owner branches/PRs, and undeclared Relay results may suggest where to search, but they are not premises or evidence by themselves.

A cross-task result enters the current task only through an explicit `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY` import with a source reference, evidence/status class, and scope/assumptions. Remembering a result is not importing it.

Context quarantine is local research hygiene. It does not require a GitHub comment, heartbeat, new branch, or new PR, and failure of a memory-derived lead is never a `HARD_BLOCK`.
