# Scheduler V2 Quickstart / 状态机 V2 快速入口

Canonical machine: `research_scheduler.json`  
Runtime log: Issue `#240`  
Reducer: `tools/research_scheduler.py`  
Event emitter: `tools/research_scheduler_event.py`

## Researcher / 研究员

- `领任务` -> `select` -> `CLAIM` -> work.
- Finish work with `SUBMIT`, never V2 `DONE`.
- Lease loss creates `ORPHANED`; resume with `ADOPT`, not ordinary `CLAIM`.

## FREE researcher / 自由研究员

FREE discovery itself stays outside automatic dispatch, but a FREE researcher may publish a concrete next task:

`publish-proposal -> REVIEW_PENDING`.

It cannot become `READY` until a different Driver reviews the publication and binds an approved immutable taskbook ref.

## Driver / 驾驶员

- `领审核` -> `select-review` -> `REVIEW_CLAIM`.
- Publication review: `APPROVE` or `REJECT`.
- Return review: `REVIEW` with an explicit verdict.
- A Driver cannot review a task they published or a return they executed.
- Use `MIGRATE` only for pre-V2 work already live at cutover.

## Orphan / 孤儿

Every unregistered taskbook is visible as an orphan. An orphan is not auto-dispatchable. Inspect its refs, then `ADOPT`, `SUPERSEDE`, or explicitly migrate/close it.

## Control checks / 控制检查

`python tools/research_scheduler.py validate`

`python tools/research_scheduler.py registry --events <exported-events.jsonl>`

The invariant to remember is:

`PUBLISH != READY`, `SUBMIT != DONE`, `ORPHANED != HANDOFF_READY`.
