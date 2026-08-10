# Research taskbook operating rules

This directory is the append-only static input surface for scout-created Enterprise Math research tasks.

A research direction is ready for delegation only after a taskbook exists here with a valid `ENTERPRISE_MATH_TASK_V1` metadata block and `base_state: READY`. `tools/research_scheduler.py` discovers these Markdown taskbooks automatically and merges them with legacy tasks from `research_scheduler.json` at read time. Do not duplicate the same task into the central JSON.

## Sparse GitHub fast path

Creating a **new uniquely named taskbook** here is a narrow append-only control-plane fast path:

- when the user/scout has explicitly decided a direction is ready for delegation, create the new taskbook directly on current `main`;
- do not create a branch or PR merely to register that new task;
- do not write Issue #240 merely because the task was created;
- do not wait for or poll Actions after task registration;
- never use this fast path to modify theorem/code/canonical prose, rewrite an existing taskbook, alter completed-task history, or bypass owner/promotion rules.

If an existing taskbook needs a semantic rewrite, use the ordinary repository workflow or supersede it with a new uniquely named taskbook.

## Claim and research cadence

A researcher may claim a task through the existing Issue #240 mechanism. For scout taskbooks, prefer one `CLAIM` with `lease_minutes: 1440` so routine heartbeat traffic is unnecessary. If a claim is posted, follow the root scheduler race rule.

After claim, source-repository research remains `REMOTE_SILENT` between semantic checkpoints. Do not post routine `HEARTBEAT` or `PROGRESS` merely to prove activity. Use GLOBAL_KNOWLEDGE progress journaling for loss prevention when available. At a real session/ownership boundary, post at most one useful `HANDOFF` or `DONE` event when the write path is nonblocking.

A claim actor does not become the mother-theorem owner. Reusable results still route through existing owner/Relay/Foundation machinery before promotion.

## Metadata

Every taskbook must begin with:

```text
<!-- ENTERPRISE_MATH_TASK_V1
{ ... valid JSON task object ... }
-->
```

Use `owner: "taskbook/unassigned"` for a new cross-route task that has not yet acquired a canonical theorem owner. This value is a scheduler routing placeholder only.
