# Research Scheduling Protocol V2

Status: `ACTIVE / CURRENT ONLY`

Task definitions are immutable V2 publications. `research_control_dispatch.py` first resolves stale-owner recovery, then delegates fresh task selection to `tools/research_dispatch.py` or active-cohort lane selection to `tools/research_lane_dispatch.py`.

Issue #240 mutations require an authenticated, unedited GitHub server comment envelope from an authorized actor. `tools/research_runtime_reducer.py` is a pure reducer; it owns no task table and no mathematical authority.

Selection order is defined in `research_runtime_policy_v2.json`. Owner lease and conversation liveness are independent. A valid stale owner is adopted after durable-frontier verification; a second claim is not created.
