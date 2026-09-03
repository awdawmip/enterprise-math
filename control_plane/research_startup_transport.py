"""Non-semantic startup transport for Enterprise Math research execution.

This transport carries no task, theorem, review, publication, Working Truth,
Foundation, or canonical authority. It only prevents repository discovery from
becoming a task-start prerequisite: AGENTS.md is obeyed when already injected by
the host, but researchers must not remotely search/fetch it merely to begin an
already-authorized exact task.
"""
from __future__ import annotations

import copy
from typing import Any, Mapping

STARTUP_TRANSPORT = {
    "schema": "ENTERPRISE_MATH_RESEARCH_STARTUP_TRANSPORT_V1",
    "agents_md": "INJECTED_CONTEXT_ONLY_DO_NOT_REMOTE_SEARCH_OR_FETCH_FOR_TASK_START",
    "if_agents_context_unavailable": "PROCEED_FROM_CANONICAL_DISPATCH_TARGET_AND_EXACT_TASKBOOK",
    "hot_start": [
        "EXACT_DISPATCH_TARGET",
        "EXACT_TASK_PUBLICATION_AND_TASKBOOK",
        "FIRST_REQUIRED_DEPENDENCY",
        "SUBSTANTIVE_RESEARCH",
    ],
    "remote_control_reads": "TRIGGERED_ONLY",
    "taskbook_policy_digest_impact": "NONE_CONTROL_TRANSPORT_ONLY",
}


def attach(value: Mapping[str, Any]) -> dict[str, Any]:
    out = dict(value)
    out["startup_transport"] = copy.deepcopy(STARTUP_TRANSPORT)
    return out
