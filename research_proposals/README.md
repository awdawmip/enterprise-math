# Enterprise Math research proposal queue

This directory is the lightweight pre-task queue for side branches discovered by researchers.

A proposal is **not** a taskbook. It is not `READY`, not claimable, not canonical, and does not change the roadmap. Only a Research Driver explicitly activated by the user in the current conversation may approve a proposal and create an official taskbook under `research_tasks/`.

Researchers remain free to explore and document mathematics. Proposal governance limits scheduling authority only; it must not interrupt proof search, experiments, computation, Lean work, or normal handoff.

## Capture rule

Do not create one Markdown file per idea. At a semantic checkpoint or handoff, consolidate worthwhile branches into one compact JSON bundle:

```json
{
  "schema": "ENTERPRISE_MATH_PROPOSAL_BUNDLE_V1",
  "parent_task_id": "RS-...",
  "created_by_role": "RESEARCHER",
  "at": "2026-08-10T19:21:00+08:00",
  "candidates": [
    {
      "proposal_id": "...",
      "title": "...",
      "research_question": "...",
      "why_now": "...",
      "expected_leverage": "HIGH",
      "evidence_refs": ["..."]
    }
  ]
}
```

One bundle may contain several candidate branches. Related candidates should be grouped rather than emitted as separate files.

If a repository write path is unavailable, keep the candidates in a compact `proposal_candidates` section of the ordinary handoff. Do not stop productive research merely to create proposal artifacts.

## Driver review

The Driver may batch-review the queue and decide `APPROVE`, `MERGE`, `PARK`, or `REJECT`. Approval is materialized by creating a Driver-authorized taskbook; proposal files themselves never become dispatchable tasks.

Role authority is defined by `research_role_policy.json`.
