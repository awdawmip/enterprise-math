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
