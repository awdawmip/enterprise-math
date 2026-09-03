"""Non-semantic startup/rebase transport for Enterprise Math execution.

This transport carries no task, theorem, review, publication, Working Truth,
Foundation, or canonical mathematical authority. It only transports the current
control epoch and makes repository entry idempotently discard stale cached chat
workflow plans while preserving exact task/claim/durable-frontier authority.

AGENTS.md is obeyed when already injected by the host, but researchers must not
remotely search/fetch it merely to begin an already-authorized exact task.
"""
from __future__ import annotations

import copy
from typing import Any, Mapping

CONTROL_EPOCH = "EM-CONTROL-20260903-LEGACY-CONVERSATION-REBASE-1"

LEGACY_CONVERSATION_REBASE = {
    "mode": "ALWAYS_IDEMPOTENT_ON_CONTROL_ENTRY",
    "control_epoch": CONTROL_EPOCH,
    "cached_conversation_control_plan": "NONAUTHORITATIVE_REBASE_TO_CURRENT",
    "preserve": [
        "EXACT_TASK_AND_CURRENT_PUBLICATION_AUTHORITY",
        "WINNING_CLAIM_AND_OWNER_SCOPE",
        "HIGHEST_VERIFIED_DURABLE_FRONTIER",
        "FROZEN_SOURCE_AND_BLINDNESS_RESTRICTIONS",
        "THEOREM_STRENGTH_AND_TASK_LOCAL_SCOPE",
        "NO_SORRY_NO_ADMIT_NO_CUSTOM_AXIOM_AND_OTHER_FROZEN_CONSTRAINTS",
    ],
    "discard": [
        "PR_REQUIRED_FOR_START_PROGRESS_DURABILITY_OR_HANDOFF_UNLESS_EXACT_CURRENT_TASK_REQUIRES_IT",
        "CI_WAIT_OR_REPEATED_CI_MONITOR_AS_CONVERSATION_BARRIER_WHEN_PENDING_NONBLOCKING",
        "DRAFT_READY_TOGGLE_MERELY_TO_TRIGGER_VALIDATION",
        "REMOTE_SEARCH_OR_FETCH_AGENTS_MD_MERELY_FOR_TASK_START",
        "RESTART_VERIFIED_COMPLETE_WORK_BECAUSE_CONVERSATION_IS_OLD_RESUMED_OR_CONTEXT_IS_MISSING",
        "CACHED_PREVIOUS_CONTROL_ROUTE_WHEN_CURRENT_CANONICAL_DISPATCH_OR_RUNTIME_DISAGREES",
    ],
    "after_rebase": "RESUME_FROM_CURRENT_CANONICAL_DISPATCH_AND_HIGHEST_VERIFIED_DURABLE_FRONTIER",
    "pr_default": "OPTIONAL_DURABLE_OR_REVIEW_SURFACE_NOT_CONVERSATION_GATE",
    "ci_pending": "PENDING_NONBLOCKING_CONTINUE_PARENT_TASK",
    "repeated_ci_poll_without_state_change": "FORBIDDEN_NO_PROGRESS_ACTION",
    "taskbook_policy_digest_impact": "NONE_CONTROL_TRANSPORT_ONLY",
}

STARTUP_TRANSPORT = {
    "schema": "ENTERPRISE_MATH_RESEARCH_STARTUP_TRANSPORT_V2",
    "control_epoch": CONTROL_EPOCH,
    "conversation_rebase_required": True,
    "conversation_rebase": LEGACY_CONVERSATION_REBASE,
    "agents_md": "INJECTED_CONTEXT_ONLY_DO_NOT_REMOTE_SEARCH_OR_FETCH_FOR_TASK_START",
    "if_agents_context_unavailable": "PROCEED_FROM_CANONICAL_DISPATCH_TARGET_AND_EXACT_TASKBOOK",
    "hot_start": [
        "REBASE_CACHED_CONVERSATION_CONTROL_PLAN",
        "EXACT_DISPATCH_TARGET",
        "EXACT_TASK_PUBLICATION_AND_TASKBOOK",
        "FIRST_REQUIRED_DEPENDENCY",
        "SUBSTANTIVE_RESEARCH",
    ],
    "remote_control_reads": "TRIGGERED_ONLY",
    "taskbook_policy_digest_impact": "NONE_CONTROL_TRANSPORT_ONLY",
}


def attach(value: Mapping[str, Any]) -> dict[str, Any]:
    """Attach the current control epoch and idempotent rebase directive."""
    out = dict(value)
    out["startup_transport"] = copy.deepcopy(STARTUP_TRANSPORT)
    return out
