# MCP live control code admission resolved

The earlier UPSTREAM_CODE_REVIEW_REQUIRED boundary recorded in OWNER_MCP_CODE_ADMISSION_PENDING_20260920.md is resolved for the three reviewed control-module changes. The user explicitly requested this service repair after the bounded research window had stopped. This was control maintenance; no research execution was resumed.

The MCP source update is awdawmip/em-research-mcp commit aed7e77b3194f54b45b205dcbed2ca88a2531dd6, with exact configuration blob1c8eba9e1d9d91e93070fa8278a02156a71f3f54 and draft PR3 against its existing deployed integration branch. Only the three reviewed Python pins and their source-reference metadata changed. All149 other pins, disabled claim writes, empty executor bindings and remaining configuration fields were preserved.37 adapter tests passed locally and37 on the host.

A separate release was activated at2026-09-19T23:50:52.938010Z, retaining the old release for rollback and keeping service PID755802 unchanged. Actual read-only MCP requests subsequently succeeded:
- RB task query, observed23:53:36Z, source91c39a76eaa69f9cb4221125619d75be53cac03b,834 authenticated server comments, state DONE / COMPLETE / ACCEPTED.
- Global dispatch, observed23:57:00Z, sourcea01dcabbaafb989a4853e9dfdbbf94842cb65f05,834 comments, valid JT2 persistent Driver route. formal_task_created=false; no CLAIM was created.

The current task inventory was independently reconstructed from a fully verified7,272-file main91c39a76 view and834 raw server envelopes:289 tasks, comprising103 NEEDS_DISPATCH,53 AWAITING_REVIEW,25 BLOCKED,20 DORMANT and88 COMPLETE (82 DONE plus6 SUPERSEDED). Incremental changes through3c0a14f3757a1c2d490b31e6bf8c904bd8c74730 add BRC research/source and activity records but do not alter the task/publication/result/review/runtime inputs. JT2 generation3 is ready, T6 is awaiting review, and the RB common-differential task is complete; their parent mathematical goals remain open.

Evidence and reproduction:
- https://github.com/awdawmip/em-research-mcp/blob/aed7e77b3194f54b45b205dcbed2ca88a2531dd6/docs/CONTROL_CODE_ADMISSION_20260920.md
- https://github.com/awdawmip/em-research-mcp/blob/aed7e77b3194f54b45b205dcbed2ca88a2531dd6/docs/evidence/control-code-admission-20260920.json
- https://github.com/awdawmip/em-research-mcp/pull/3
- Local full task inventory: D:/em/TEMP/task-inventory-20260920-0735/TASK_INVENTORY.md and tasks.csv.
- Local actual repair receipt: D:/em/TEMP/mcp-code-admission-fix-20260920/FINAL_REPAIR_RECEIPT.json.

This does not change the static pinned-bundle refresh policy, grant research/claim authority, admit arbitrary future control code, or retry the earlier platform-blocked MCP checkpoint-write command. It supersedes only the recorded live-control code-admission blocker.
