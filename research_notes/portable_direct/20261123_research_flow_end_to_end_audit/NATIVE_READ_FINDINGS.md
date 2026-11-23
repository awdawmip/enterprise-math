# Exact-task native-read overhead

Audit date: 2026-11-23. Read-only source inspection, no production heavy read or load test.

## Finding

The current backend's exact-task route uses the same broad native input/bootstrap path as global dispatch. Returning one task does not limit the input stores to that task. The shared event collector already reuses ready event bytes; this finding does not claim five full remote event downloads.

## Direct evidence in the deployed backend

Repository `awdawmip/em-research-mcp`, deployed application commit `b6c33838c05b8442b225a6c019773fb026e18607`.

1. `src/native_closure.py:22–35`: `AUTHORITY_ROOTS` includes Task, execution, Result, Review, Activity, session, objective, followup and parallel/historical stores.
2. `src/native_closure.py:105–134`: `initial_paths(tree, reviewed_python_blobs, operation)` explicitly treats operation as non-narrowing. It seeds every authority-root file, all taskbooks, root/control JSON and reviewed Python code. Only Activity `readbacks/*.json` descendants are excluded.
3. `src/control_transport.py:977–1001`: `_light_source_bundle` materializes those seeds and parses every selected JSON/Markdown document, recursively following control references. Verified cached blobs avoid repeated downloads but do not eliminate broad materialization and parsing.
4. `src/canonical_runner.py:244–261`: `_run_native` imports `research_control_dispatch` before the task-specific branch. It uses request-local `immutable_source_view` and `read_view`; both end with that subprocess/request.
5. `src/canonical_runner.py:439–449`: the exact-task branch calls `publications.current_records(root)`, selects the requested row, then `dispatch.reduce_definition`, and returns the taskbook with `execution_authorized=False`.

The read scope therefore already includes unrelated Activity and Result data before the native reducer asks for the selected task. This is actual deployed transport behavior; it is not inferred merely from timing.

Backend source blobs:
- canonical_runner.py: `b9c1c28fc60ea2fd2fdc5905dc95e5246bdf8260`
- native_closure.py: `62a1df16069e0f26ef22eae5fcb886bf226d958f`

## Relevant current Enterprise Math native implementation

Inspected at main `59e7d1e4c4717c0aaa6d5db1f016f62f1180c36d`. Deployment uses its configured reviewed source code package; this audit did not independently compare that complete runtime manifest to this main snapshot.

- `research_control_dispatch.py:38–53` imports and immediately installs the canonical bootstrap.
- `control_plane/research_control_bootstrap.py:213–264` installs publication, task-integrity, semantic, Result/Review, Driver-review, followup, handoff and parent-objective adapters.
- `control_plane/research_task_records_impl.py:97–112` reads `research_task_records/*/*.json`; `current_records` at 153–210 resolves all task heads. There is no task_id parameter on this API.
- Publication/integrity/followup wrappers add operational isolation around this global lookup, so simply indexing the returned dictionary does not reduce the read scope.
- `tools/research_dispatch_core.py:714–774` does reduce the selected task rather than global ranking, but invokes its Result state and cohort overlays.
- `tools/research_result_records.py:331–430` contains exact-task file reads for some authority checks, then delegates to the operational Result/Review/parallel/replacement machinery. A function named `task_result_state(task_id)` is not proof of a wholly task-scoped loader.
- `control_plane/research_read_view.py` caches raw/derived reads only within the immutable request context; it does not supply reuse across five separate exact-task subprocesses.

No existing fully task-scoped current-runtime projection API was found among these exact entry points.

## Lightweight scientific reading already works without this path

The existing `em_control_artifact` is sufficient for ordinary known-file reading:

- `src/control_jobs.py:825–837`: without a packet request, operation `artifact` calls `read_external_artifact` directly with exact path and supplied commit (or resolves current main once). It does not call the native task reducer, event collection, `_light_source_bundle`, or authority-root bootstrap.
- `src/control_transport.py:638–676`: that routine reads/verifies the one artifact, using its existing artifact cache when available. The maximum is 4 MiB and page size up to 24,000 characters.
- With a supplied packet request, lines 838–857 preserve that packet's path/commit restrictions. Known fully pinned artifacts go through `read_artifact`.
- `src/control_transport.py:592–637`: `read_artifact` verifies the exact immutable file and both hashes without materializing its repository tree.
- Tool registry confirms `em_control_artifact(request_id, path, source_commit?, packet_request_id?, start_char?, char_count?)` is exposed.

Thus ordinary informed research can read a known definition, theorem, report or frozen input through this existing artifact route, an exact notebook source, or the GitHub exact-file connector. A new native Task query is needed when its current operational state is the actual question. Frozen task/source restrictions still apply to scientific inputs, and a text read does not grant execution authority.

## Precise next backend change

Implement a canonical read-only exact-task projection whose dependency loaders operate on the requested task/publication and its actually linked evidence, retaining the full tree membership/omission guard and the existing demand loader. Use it for operation `task`. Keep actual write/claim/review authority checks fresh at their mutation boundaries.

This requires two coordinated narrow boundaries:

1. Source native entry: avoid the global-dispatch bootstrap's eager data validation for exact-task reads while retaining the selected task's publication forks, isolation, active ownership, Result/Review and dependency semantics.
2. Backend transport: seed that scoped reader with its required code/contracts and selected task records; let existing verified demand expansion supply additional exact dependencies. Unrelated Activity/Result/taskbook bytes should not enter solely because they share an authority root.

Shrinking `initial_paths` alone would not establish the improvement: the unchanged global readers would demand broad data again and may add repeated native restarts. Skipping bootstrap alone could remove current operational isolation. Neither change was made here.

A focused regression fixture should compare the scoped and existing canonical outputs for a selected task and its relevant isolation cases, while making unrelated Activity/Result content large or unreadable to show it is not consumed. Benchmark the native/source phases separately from queue/event collection. No predicted seconds or speedup are claimed before that measurement.

## Work performed

Source inspection and routing confirmation only. No new cache, registry, periodic audit, production identity/CLAIM, remote CI, mathematical replay, or runtime deployment.

