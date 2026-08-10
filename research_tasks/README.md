# Enterprise Math research taskbooks

This directory contains executable research handoffs produced by the research-scout workflow.

A taskbook is both a human-readable Markdown brief and a static scheduler task through its leading `ENTERPRISE_MATH_TASK_V1` JSON block. The central `research_scheduler.json` remains the legacy owner/frontier registry; new scout tasks do not require a central JSON edit because `tools/research_scheduler.py` merges taskbooks into the effective state machine at read time.

Typical lifecycle:

```text
idea becomes research-worthy
  -> append one taskbook to research_tasks/
  -> scheduler sees READY automatically
  -> researcher CLAIM (best effort; long lease)
  -> remote-silent research
  -> semantic checkpoint / HANDOFF / DONE
  -> reusable results route to real owners and canonical promotion
```

The taskbook itself is research input, not theorem truth.

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
