#!/usr/bin/env python3
"""Apply the physical legacy-control isolation after the V2 task cutover.

This is a one-shot repository migration.  It preserves the exact pre-cutover
bytes on archive/legacy-control-plane-pre-v2-20260902, rewires live runtime code
to immutable V2 task publications, removes legacy task/config writers from main,
and replaces prompt-level avoidance rules with a small current-only router.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_BRANCH = "archive/legacy-control-plane-pre-v2-20260902"
ARCHIVE_SHA = "ce629e24e5af59128e25af87075c6622413684e0"

LEGACY_PATHS = [
    "research_scheduler.json",
    "tools/research_scheduler.py",
    "research_task_registry.json",
    "tools/research_task_registry.py",
    "research_task_publication_contract.json",
    "tools/check_task_registry_cutover.py",
    "docs/RESEARCH_SCHEDULER.md",
    "docs/RESEARCH_TASK_PUBLICATION_PROTOCOL_V1.md",
    "docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md",
]
ONE_SHOT_PATHS = [
    "control_plane/audit_legacy_control_migration.py",
    "control_plane/audit_legacy_runtime_states.py",
    "control_plane/materialize_legacy_tasks_v2.py",
    "control_plane/run_legacy_task_migration_safe.py",
    ".github/workflows/legacy-control-migration-audit.yml",
    ".github/workflows/materialize-legacy-tasks-v2.yml",
]
STALE_TESTS = [
    "tests/test_research_task_registry_cli_surface_unittest.py",
    "tests/test_research_task_registry_unittest.py",
    "tests/test_task_registry_cutover_unittest.py",
    "tests/test_research_task_publication_contract_unittest.py",
    "tests/test_research_scheduler.py",
]


class CutoverError(ValueError):
    pass


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load(rel: str) -> dict[str, Any]:
    value = json.loads(read(rel))
    if not isinstance(value, dict):
        raise CutoverError(f"{rel}: JSON object required")
    return value


def dump(rel: str, value: dict[str, Any]) -> None:
    write(rel, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def require_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise CutoverError(f"{label}: required span not found")
    return text.replace(old, new)


def replace_region(text: str, start: str, end: str, replacement: str, label: str) -> str:
    left = text.find(start)
    if left < 0:
        raise CutoverError(f"{label}: start marker missing")
    right = text.find(end, left)
    if right < 0:
        raise CutoverError(f"{label}: end marker missing")
    return text[:left] + replacement + text[right:]


def derive_runtime_reducer() -> None:
    source = read("tools/research_scheduler.py")
    start = source.index("class SchedulerError")
    end = source.index("\ndef effective_states(", start)
    core = source[start:end].replace("SchedulerError", "RuntimeReducerError")
    header = '''#!/usr/bin/env python3
"""Pure V2 runtime event reducer.

Task definitions come from immutable V2 publication records.  This module only
reduces already-authenticated Issue #240 events and derives stable execution
identity.  It owns no task table, legacy baseline, publication authority, or
mathematical status.
"""
from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import re
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "research_runtime_policy_v2.json"
HARD_BLOCK_FIELDS = ("missing_object", "owner", "necessity", "unblock_condition")
RESEARCHER_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\\d{3}[A-Z]?)\\b")
LANE_RE = re.compile(r"[^A-Z0-9]+")
EVENT_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"
POLICY_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RUNTIME_POLICY_V2"

'''
    footer = '''

def validate_policy(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if policy.get("schema") != POLICY_SCHEMA:
        errors.append("unexpected V2 runtime-policy schema")
    if policy.get("status") != "ACTIVE_CANONICAL":
        errors.append("V2 runtime policy must be ACTIVE_CANONICAL")
    if policy.get("task_definition_source") != "IMMUTABLE_V2_TASK_PUBLICATIONS":
        errors.append("runtime policy task source must be immutable V2 publications")
    if policy.get("event_schema") != EVENT_SCHEMA:
        errors.append("runtime policy event schema mismatch")
    lease = policy.get("default_claim_lease_minutes")
    if type(lease) is not int or lease <= 0:
        errors.append("default_claim_lease_minutes must be positive integer")
    selection = policy.get("selection_policy")
    if not isinstance(selection, dict):
        errors.append("selection_policy must be an object")
    else:
        for field in ("state_order", "priority_order", "leverage_order"):
            value = selection.get(field)
            if not isinstance(value, list) or not value or any(not isinstance(x, str) for x in value):
                errors.append(f"selection_policy.{field} must be a nonempty string list")
    if policy.get("legacy_task_definition_source") is not None:
        errors.append("legacy task-definition source must be null after cutover")
    return errors


def load_policy(root: pathlib.Path = ROOT) -> dict[str, Any]:
    policy = load_json(root / "research_runtime_policy_v2.json")
    errors = validate_policy(policy)
    if errors:
        raise RuntimeReducerError("invalid V2 runtime policy: " + "; ".join(errors))
    return policy


def select_state(
    states: Iterable[dict[str, Any]],
    policy: dict[str, Any],
    *,
    kind: str = "RESEARCH",
) -> dict[str, Any] | None:
    selection = policy["selection_policy"]
    state_rank = {name: index for index, name in enumerate(selection["state_order"])}
    priority_rank = {name: index for index, name in enumerate(selection["priority_order"])}
    leverage_rank = {name: index for index, name in enumerate(selection["leverage_order"])}
    candidates = [
        value for value in states
        if value.get("dispatch_state") == "NEEDS_DISPATCH"
        and (kind == "ANY" or value.get("kind") == kind)
    ]
    if not candidates:
        return None

    def key(value: dict[str, Any]) -> tuple[Any, ...]:
        try:
            last = parse_time(str(value.get("last_progress_at") or ""))
        except Exception:
            last = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (
            state_rank.get(value.get("state"), len(state_rank)),
            priority_rank.get(value.get("priority"), len(priority_rank)),
            leverage_rank.get(value.get("leverage"), len(leverage_rank)),
            last,
            value.get("task_id", ""),
        )

    return min(candidates, key=key)
'''
    write("tools/research_runtime_reducer.py", header + core + footer)


def write_runtime_policy() -> None:
    dump(
        "research_runtime_policy_v2.json",
        {
            "schema": "ENTERPRISE_MATH_RESEARCH_RUNTIME_POLICY_V2",
            "status": "ACTIVE_CANONICAL",
            "effective": "2026-09-02",
            "task_definition_source": "IMMUTABLE_V2_TASK_PUBLICATIONS",
            "task_record_store": "research_task_records/<task-id>/<publication-id>.json",
            "event_schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
            "runtime_issue": 240,
            "event_authentication": "GITHUB_SERVER_COMMENT_ENVELOPE_REQUIRED",
            "default_claim_lease_minutes": 120,
            "selection_policy": {
                "state_order": ["HANDOFF_READY", "READY"],
                "priority_order": ["P0", "P1", "P2", "P3"],
                "leverage_order": ["FOUNDATION", "VERY_HIGH", "HIGH", "MEDIUM", "LOW"],
            },
            "completion_rule": "TERMINAL_EVENT_PLUS_DURABLE_PROGRESS_REF",
            "legacy_task_definition_source": None,
            "legacy_runtime_on_main": False,
            "mathematical_truth_authority": False,
            "working_truth_authority": False,
            "foundation_authority": False,
        },
    )


def patch_dispatch() -> None:
    rel = "tools/research_dispatch.py"
    text = read(rel)
    text = re.sub(
        r'\A#!/usr/bin/env python3\n""".*?"""\n',
        '#!/usr/bin/env python3\n"""Canonical immutable-V2 Enterprise Math dispatch view.\n\nTask definitions come only from current immutable V2 publication records. Issue\n#240 events are accepted only through authenticated GitHub comment envelopes and\nare reduced by tools/research_runtime_reducer.py.  No task table or legacy\ndefinition fallback is present on main.\n"""\n',
        text,
        count=1,
        flags=re.S,
    )
    text = text.replace("from tools import research_scheduler", "from tools import research_runtime_reducer")
    text = text.replace("import research_scheduler  # type: ignore", "import research_runtime_reducer  # type: ignore")
    text = text.replace('LEGACY = ROOT / "research_scheduler.json"\nOWNERS = ROOT / "branch_governance_overrides.json"\n', 'RUNTIME_POLICY = ROOT / "research_runtime_policy_v2.json"\n')
    text = text.replace("research_scheduler.", "research_runtime_reducer.")

    merged = '''def merged_definitions(root: Path = ROOT) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for task_id, record in research_task_records.current_records(root).items():
        by_id[task_id] = registered_definition(record, root)
    return [by_id[key] for key in sorted(by_id)]


'''
    text = replace_region(text, "def merged_definitions(", "def _is_registered(", merged, rel + ":merged")

    auth = '''def _event_authentication_filter(
    task: dict[str, Any], events: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fail closed unless a live event carries an authorized server envelope."""
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if event.get("task_id") != task.get("task_id"):
            accepted.append(event)
            continue
        meta = event.get(GITHUB_META_KEY)
        if not isinstance(meta, dict) or meta.get("server_authenticated") is not True:
            rejected.append({
                "index": index,
                "reason": "runtime event requires server-authenticated GitHub Issue #240 comment envelope",
            })
            continue
        if meta.get("issue_number") != 240 or type(meta.get("comment_id")) is not int:
            rejected.append({"index": index, "reason": "GitHub event envelope issue/comment identity is invalid"})
            continue
        if meta.get("control_authorized") is not True:
            rejected.append({
                "index": index,
                "reason": "GitHub event author is authenticated but not authorized for control-plane mutation",
            })
            continue
        if meta.get("edited") is True:
            rejected.append({
                "index": index,
                "reason": "edited runtime event is not authority; append a correction event",
            })
            continue
        accepted.append(event)
    return accepted, rejected


'''
    text = replace_region(text, "def _event_authentication_filter(", "def _inline_claim_envelope(", auth, rel + ":auth")

    summary = '''def _authentication_summary(task: dict[str, Any], events: list[dict[str, Any]]) -> dict[str, Any]:
    matching = [event for event in events if event.get("task_id") == task.get("task_id")]
    server = [event for event in matching if isinstance(event.get(GITHUB_META_KEY), dict)]
    if server:
        latest = max(server, key=lambda event: event[GITHUB_META_KEY].get("comment_id", -1))
        meta = latest[GITHUB_META_KEY]
        return {
            "event_authentication": "GITHUB_SERVER_COMMENT_ENVELOPE",
            "last_server_comment_id": meta.get("comment_id"),
            "last_server_author_login": meta.get("author_login"),
        }
    return {
        "event_authentication": "UNAUTHENTICATED_EVENT_REJECTED" if matching else "NO_RUNTIME_EVENT",
        "last_server_comment_id": None,
        "last_server_author_login": None,
    }


'''
    text = replace_region(text, "def _authentication_summary(", "def reduce_definition(", summary, rel + ":summary")
    text = require_replace(
        text,
        '    legacy = load_json(root / "research_scheduler.json")\n    policy = legacy["selection_policy"]\n',
        '    policy = research_runtime_reducer.load_policy(root)["selection_policy"]\n',
        rel + ":selection-policy",
    )

    validation = '''def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        policy = research_runtime_reducer.load_policy(root)
        errors.extend(research_runtime_reducer.validate_policy(policy))
    except Exception as exc:
        errors.append(f"V2 runtime policy failure: {exc}")
    try:
        control_authorization_policy(root)
    except Exception as exc:
        errors.append(f"control-event authorization policy failure: {exc}")
    try:
        definitions = merged_definitions(root)
    except Exception as exc:
        errors.append(f"V2 dispatch definition failure: {exc}")
        return errors
    ids = [item.get("task_id") for item in definitions]
    if len(ids) != len(set(ids)):
        errors.append("canonical V2 dispatch view contains duplicate task IDs")
    for item in definitions:
        if item.get("registration_source") not in {
            "IMMUTABLE_TASK_RECORD",
            "TASK_DEFINITION_FAULT_QUARANTINE",
        }:
            errors.append(f"{item.get('task_id')}: non-V2 task definition entered live dispatch")
    return errors


'''
    text = replace_region(text, "def validate(", "def _decode_event_input(", validation, rel + ":validate")
    text = require_replace(
        text,
        "    return research_runtime_reducer.load_events(path)\n",
        '    raise DispatchError("runtime input must be raw authenticated Issue #240 comment objects")\n',
        rel + ":bare-events",
    )
    text = text.replace("canonical registered-plus-legacy dispatch", "canonical immutable-V2 dispatch")
    text = text.replace("merged task definition(s)", "V2 task definition(s)")
    write(rel, text)


def patch_runtime_guard() -> None:
    rel = "control_plane/research_runtime_guard_core.py"
    text = read(rel)
    text = text.replace("from tools import research_scheduler", "from tools import research_runtime_reducer")
    text = text.replace("import research_scheduler  # type: ignore", "import research_runtime_reducer  # type: ignore")
    text = text.replace("research_scheduler.", "research_runtime_reducer.")
    text = replace_region(text, "def legacy_task_ids(", "def _execution_scope(", "", rel + ":legacy-id-loader")
    start = '    if scope is not None:\n        raise RuntimeAuthorizationError(\n            "execution cohorts require an immutable registered task"\n        )\n'
    left = text.find(start)
    if left < 0:
        raise CutoverError(rel + ": legacy registration branch start missing")
    right = text.find("\n\ndef _registered_definition(", left)
    if right < 0:
        raise CutoverError(rel + ": legacy registration branch end missing")
    replacement = '''    if scope is not None:
        raise RuntimeAuthorizationError("execution cohorts require an immutable registered task")
    raise RuntimeAuthorizationError(
        f"task {task_id!r} has no current immutable V2 publication"
    )
'''
    text = text[:left] + replacement + text[right:]
    write(rel, text)

    wrapper = read("tools/research_runtime_guard.py").replace(
        "_core.research_scheduler.", "_core.research_runtime_reducer."
    )
    write("tools/research_runtime_guard.py", wrapper)

    runtime = read("tools/research_runtime.py")
    runtime = runtime.replace('    "LEGACY_BASELINE_REGISTERED",\n', "")
    old = '''    if registration_state != "LEGACY_BASELINE_REGISTERED":
        if not isinstance(registry_key, str) or not registry_key.strip():
            raise RuntimeStateError("registered task requires nonempty task_registration.registry_key")
        if registry_key != task_id:
            raise RuntimeStateError("task_registration.registry_key must equal task.task_id")
    if registration_state == "LEGACY_BASELINE_REGISTERED" and registration.get("fresh_redispatch") is True:
        raise RuntimeStateError("legacy baseline cannot authorize fresh redispatch; migrate to explicit registry record")
'''
    new = '''    if not isinstance(registry_key, str) or not registry_key.strip():
        raise RuntimeStateError("registered task requires nonempty task_registration.registry_key")
    if registry_key != task_id:
        raise RuntimeStateError("task_registration.registry_key must equal task.task_id")
'''
    runtime = require_replace(runtime, old, new, "tools/research_runtime.py:registration")
    write("tools/research_runtime.py", runtime)


def patch_publication_fault_isolation() -> None:
    rel = "control_plane/research_publication_fault_isolation.py"
    text = read(rel)
    start = "        def merged_definitions(local_root: Path = research_dispatch.ROOT) -> list[dict[str, Any]]:\n"
    left = text.find(start)
    if left < 0:
        raise CutoverError(rel + ": merged definition patch start missing")
    right = text.find("\n        research_dispatch.merged_definitions = merged_definitions", left)
    if right < 0:
        raise CutoverError(rel + ": merged definition patch end missing")
    replacement = '''        def merged_definitions(local_root: Path = research_dispatch.ROOT) -> list[dict[str, Any]]:
            by_id: dict[str, dict[str, Any]] = {}
            for task_id, record in isolated_current_records(local_root).items():
                try:
                    by_id[task_id] = research_dispatch.registered_definition(record, local_root)
                except Exception as exc:
                    by_id[task_id] = definition_fault(task_id, record, exc, None)
            for task_id, row in validated_quarantines(local_root).items():
                by_id[task_id] = blocked_definition(task_id, row, by_id.get(task_id))
            return [by_id[key] for key in sorted(by_id)]
'''
    write(rel, text[:left] + replacement + text[right:])


def patch_machine_json() -> None:
    current = load("control_plane/current_control_authority.json")
    publication = current["task_publication"]
    for key in ("legacy_contract", "legacy_registry", "legacy_tool", "legacy_role"):
        publication.pop(key, None)
    publication["migration_manifest"] = "control_plane/legacy_control_migration_manifest.json"
    publication["physical_archive"] = {
        "branch": ARCHIVE_BRANCH,
        "source_commit": ARCHIVE_SHA,
        "runtime_on_main": False,
    }
    current["live_dispatch"]["runtime_policy"] = "research_runtime_policy_v2.json"
    current["live_dispatch"]["event_reducer"] = "tools/research_runtime_reducer.py"
    current["live_dispatch"]["task_definition_source"] = "IMMUTABLE_V2_TASK_PUBLICATIONS_ONLY"
    current["live_dispatch"]["legacy_definition_fallback"] = False
    current["precedence"].pop("stale_v1_pointer_semantics", None)
    current["precedence"]["legacy_control_files"] = "PHYSICALLY_ISOLATED_ON_ARCHIVE_BRANCH_NOT_PROMPT_HIDDEN"
    dump("control_plane/current_control_authority.json", current)

    contract = load("research_taskbook_contract.json")
    contract["task_publication_contract"] = "research_task_publication_contract_v2.json"
    contract.pop("task_registry", None)
    contract["task_record_store"] = "research_task_records/<task-id>/<publication-id>.json"
    contract["publication_tool"] = "tools/research_task_records.py"
    contract["publication_gate"] = "python tools/research_task_records.py publish --taskbook <path> --publisher-role <ROLE> --publisher-id <ID> --parent-objective-id <OBJ> --research-value <VALUE>"
    contract["registry_audit_gate"] = "python tools/research_task_records.py audit"
    contract["publication_contract"]["official_task_exists_only_after_registry_record"] = False
    contract["publication_contract"]["official_task_exists_only_after_immutable_record"] = True
    contract["publication_contract"]["scheduler_entry_alone_is_publication"] = False
    contract["publication_contract"]["publication_completion"] = "IMMUTABLE_TASK_RECORD_AUDIT_PASS"
    contract["runtime_lease_contract"].pop("scheduler_claim_lease_scope", None)
    contract["runtime_lease_contract"]["runtime_policy_claim_lease_scope"] = "OWNER_CLAIM"
    contract["rules"] = [row for row in contract.get("rules", []) if "Legacy taskbooks" not in row]
    contract["recommended_flow"] = [
        "prepare a taskbook with tools/research_task_records.py prepare or the approved equivalent",
        "edit only task-local content and complete any successor gate",
        "run optional structural lint with tools/research_taskbook.py audit",
        "publish one immutable V2 task record with publisher identity and research_value",
        "require tools/research_task_records.py audit PASS for the new transaction",
        "only then claim or dispatch the task",
        "after publication, return to the current parent objective",
    ]
    dump("research_taskbook_contract.json", contract)

    policy = load("research_taskbook_policy.json")
    policy["policy_inputs"] = [
        "research_task_publication_contract_v2.json" if row == "research_task_publication_contract.json" else row
        for row in policy.get("policy_inputs", [])
        if row not in {"research_task_registry.json", "research_scheduler.json runtime events"}
    ]
    policy["mutable_state_excluded_from_policy_digest"] = [
        "Issue #240 authenticated runtime events",
        "current immutable task-record selection overlays",
    ]
    policy["semantic_review_requirements"] = [
        row for row in policy.get("semantic_review_requirements", [])
        if "Legacy baseline tasks" not in row and "canonical research_task_registry.json" not in row
    ]
    policy["semantic_review_requirements"].insert(
        3,
        "Every newly published task requires one immutable V2 task-publication record; a taskbook, handoff, or runtime event alone is not publication.",
    )
    dump("research_taskbook_policy.json", policy)

    pub = load("research_task_publication_contract_v2.json")
    for key in ("v1_contract", "v1_shared_registry", "v1_publication_tool"):
        pub.pop(key, None)
    pub["legacy_cutover"] = {
        "status": "COMPLETE_PHYSICAL_ISOLATION",
        "manifest": "control_plane/legacy_control_migration_manifest.json",
        "archive_branch": ARCHIVE_BRANCH,
        "archive_source_commit": ARCHIVE_SHA,
        "legacy_runtime_on_main": False,
    }
    dump("research_task_publication_contract_v2.json", pub)

    common = load("research_common_surface.json")
    common["dispatch_scheduler"] = {
        "runtime_policy": "research_runtime_policy_v2.json",
        "task_definition_source": "research_task_records/<task-id>/<publication-id>.json",
        "runtime_issue": 240,
        "event_schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
        "event_reducer": "tools/research_runtime_reducer.py",
        "fresh_selector": "tools/research_dispatch.py",
        "control_router": "research_control_dispatch.py",
        "default_claim_semantics": "RENEWABLE_OWNER_LEASE",
        "auto_select_when_user_task_absent": True,
        "explicit_user_task_overrides": True,
        "handoff_required_for_unfinished_session": True,
        "expired_claim_returns_to_dispatch": True,
        "legacy_definition_fallback": False,
    }
    common["mandatory_preflight"] = [
        row for row in common.get("mandatory_preflight", [])
        if "research_scheduler.json" not in row
    ]
    common["mandatory_preflight"].insert(2, "current immutable V2 task publication and authenticated Issue #240 runtime events")
    dump("research_common_surface.json", common)

    runtime_machine = {
        "schema": "ENTERPRISE_MATH_RESEARCH_RUNTIME_STATE_MACHINE_V2",
        "status": "ACTIVE_CANONICAL",
        "effective": "2026-09-02",
        "classification": "CONTROL_FLOW_ONLY_NO_MATHEMATICAL_AUTHORITY",
        "task_definition_authority": "research_task_records/<task-id>/<publication-id>.json",
        "runtime_policy": "research_runtime_policy_v2.json",
        "event_reducer": "tools/research_runtime_reducer.py",
        "canonical_live_dispatch": "research_control_dispatch.py",
        "fresh_task_selector": "tools/research_dispatch.py",
        "fresh_lane_selector": "tools/research_lane_dispatch.py",
        "executable_runtime": "tools/research_runtime_guard.py",
        "repository_tool_paths": [
            "tools/active_turn_liveness.py",
            "tools/research_cohort_runtime.py",
            "tools/research_dispatch.py",
            "tools/research_execution_records.py",
            "tools/research_lane_claims.py",
            "tools/research_lane_dispatch.py",
            "tools/research_result_records.py",
            "tools/research_runtime.py",
            "tools/research_runtime_guard.py",
            "tools/research_runtime_reducer.py",
            "tools/research_task_records.py",
        ],
        "state_chain": "PARENT_OBJECTIVE -> IMMUTABLE_TASK_PUBLICATION -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED",
        "owner_lease_is_session_liveness": False,
        "stale_valid_owner_action": "ADOPT_EXISTING_CLAIM",
        "legacy_runtime_on_main": False,
        "legacy_archive": {"branch": ARCHIVE_BRANCH, "source_commit": ARCHIVE_SHA},
        "invariants": [
            "UNPUBLISHED_TASK -> NO_READY_NO_CLAIM_NO_EXECUTION",
            "AUTHENTICATED_ISSUE_240_EVENT_ONLY -> RUNTIME_MUTATION",
            "OWNER_LEASE != SESSION_LIVENESS",
            "SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE",
            "PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED_FALSE",
        ],
    }
    dump("research_runtime_state_machine.json", runtime_machine)

    for rel in (
        "research_architecture.json",
        "research_role_policy.json",
        "research_axiom_candidate_state_machine.json",
        "foundation_backflow.json",
        "foundation_steward.json",
        "control_plane/control_semantic_migration_registry.json",
    ):
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace("research_task_publication_contract.json", "research_task_publication_contract_v2.json")
        text = text.replace("research_task_registry.json", "research_task_records/<task-id>/<publication-id>.json")
        text = text.replace("tools/research_task_registry.py", "tools/research_task_records.py")
        text = text.replace("research_scheduler.json", "research_runtime_policy_v2.json")
        text = text.replace("tools/research_scheduler.py", "tools/research_runtime_reducer.py")
        text = text.replace("tools/check_task_registry_cutover.py", "control_plane/check_legacy_control_isolation.py")
        json.loads(text)
        path.write_text(text, encoding="utf-8")


def patch_prompts_and_docs() -> None:
    agents = read("AGENTS.md").replace("old-route index", "archive index")
    start = "### Unified task publication / orphan prevention\n"
    end = "## 3. Identity and mandatory final footer\n"
    replacement = '''### Current task publication and runtime

Current task authority is deliberately small:

- immutable task publication: `research_task_records/<task-id>/<publication-id>.json`;
- publication contract/tool: `research_task_publication_contract_v2.json` and `tools/research_task_records.py`;
- runtime policy/reducer: `research_runtime_policy_v2.json` and `tools/research_runtime_reducer.py`;
- live routing: `research_control_dispatch.py`, `tools/research_dispatch.py`, and `tools/research_runtime_guard.py`;
- authenticated coordination: GitHub Issue #240 server comment envelopes.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`OFFICIAL_NEW_TASK -> IMMUTABLE_V2_TASK_PUBLICATION_RECORD`.

`UNPUBLISHED_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

`OWNER_LEASE != SESSION_LIVENESS`.

Publication is a capture subflow and grants no mathematical truth, Working Truth, Foundation status, canonical promotion, or Driver authority. A stale session adopts the existing winning claim only after durable-frontier verification; it never creates a second claim.

The pre-V2 control surface is physically absent from `main`. Its exact bytes and task lineage are preserved by `control_plane/legacy_control_migration_manifest.json` on `archive/legacy-control-plane-pre-v2-20260902`; normal execution does not need avoidance instructions for those files.

'''
    agents = replace_region(agents, start, end, replacement, "AGENTS current task section")
    agents = agents.replace(
        "verify it is immutably registered or covered by an already-owned legacy continuation;",
        "verify its current immutable V2 publication and claimability;",
    )
    agents = agents.replace(
        "Scheduler `claim_lease_minutes` / `lease_until` is owner lease only. It does not prove conversation liveness.",
        "Runtime-policy `claim_lease_minutes` / `lease_until` is owner lease only. It does not prove conversation liveness.",
    )
    write("AGENTS.md", agents)

    runtime_doc = '''# Enterprise Math Runtime State Machine

Status: `ACTIVE / CANONICAL / V2`

The live runtime is current-only. Task definitions come from immutable V2 task-publication records, runtime ordering comes from `research_runtime_policy_v2.json`, and authenticated Issue #240 comments are reduced by `tools/research_runtime_reducer.py`.

## Live chain

`PARENT_OBJECTIVE -> IMMUTABLE_TASK_PUBLICATION -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`

Canonical tools:

- `research_control_dispatch.py` — recovery-aware top-level router;
- `tools/research_dispatch.py` — fresh task selector;
- `tools/research_lane_dispatch.py` — active-cohort lane selector;
- `tools/research_runtime_reducer.py` — pure authenticated-event reducer;
- `tools/research_runtime_guard.py` — repository-backed execution/adoption/final guard;
- `tools/research_task_records.py` — immutable task publication;
- `tools/research_execution_records.py` and `tools/research_result_records.py` — durable execution/result records;
- `tools/active_turn_liveness.py` — session-liveness primitive.

## Invariants

`UNPUBLISHED_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

`AUTHENTICATED_ISSUE_240_EVENT_ONLY -> RUNTIME_MUTATION`.

`OWNER_LEASE != SESSION_LIVENESS`.

`SESSION_STALE + OWNER_LEASE_ACTIVE -> ADOPT_EXISTING_CLAIM_AFTER_DURABLE_FRONTIER_VERIFICATION`.

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

The archived pre-V2 state is provenance, not a runtime fallback. Exact source bytes are pinned in `control_plane/legacy_control_migration_manifest.json` and preserved on `archive/legacy-control-plane-pre-v2-20260902`.
'''
    write("docs/RESEARCH_RUNTIME_STATE_MACHINE.md", runtime_doc)

    publication_doc = '''# CANONICAL TASK PUBLICATION / V2

Status: `ACTIVE / CURRENT ONLY`

An official task exists only after one immutable publication record is written under `research_task_records/<task-id>/<publication-id>.json` and pins the exact taskbook blob.

Canonical surfaces:

- `research_task_publication_contract_v2.json`;
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`;
- `tools/research_task_records.py`;
- `research_control_dispatch.py`.

Typical flow:

```text
python tools/research_task_records.py prepare ...
python tools/research_taskbook.py audit research_tasks/<TASK>.md
python tools/research_task_records.py publish ...
python tools/research_task_records.py audit
```

Publication requires publisher identity, `parent_objective_id`, `research_value`, lineage/origin review, exact taskbook blob, and a conflict-safe immutable record write. It creates no execution claim and grants no mathematical truth, Working Truth, Foundation status, canonical promotion, or Driver authority.

After publication, fresh execution uses one authenticated Issue #240 CLAIM envelope and routes through `research_control_dispatch.py`. CI is a backstop, not publication authorization, and does not keep a chat turn alive.

The completed pre-V2 task migration is recorded in `control_plane/legacy_control_migration_manifest.json`; old publication surfaces are not present on `main`.
'''
    write("docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md", publication_doc)

    scheduling_en = '''# Research Scheduling Protocol V2

Status: `ACTIVE / CURRENT ONLY`

Task definitions are immutable V2 publications. `research_control_dispatch.py` first resolves stale-owner recovery, then delegates fresh task selection to `tools/research_dispatch.py` or active-cohort lane selection to `tools/research_lane_dispatch.py`.

Issue #240 mutations require an authenticated, unedited GitHub server comment envelope from an authorized actor. `tools/research_runtime_reducer.py` is a pure reducer; it owns no task table and no mathematical authority.

Selection order is defined in `research_runtime_policy_v2.json`. Owner lease and conversation liveness are independent. A valid stale owner is adopted after durable-frontier verification; a second claim is not created.
'''
    scheduling_zh = '''# 研究调度协议 V2

状态：`ACTIVE / CURRENT ONLY`

任务定义只来自不可变的 V2 发布记录。`research_control_dispatch.py` 先处理陈旧会话下的既有 owner 恢复，再把全新任务选择交给 `tools/research_dispatch.py`，把并行 cohort lane 选择交给 `tools/research_lane_dispatch.py`。

Issue #240 的运行态变更必须来自经服务器认证、未编辑且属于授权操作者的 GitHub 评论封装。`tools/research_runtime_reducer.py` 只是纯 reducer，不持有任务表，也没有数学权威。

选择顺序由 `research_runtime_policy_v2.json` 定义。owner lease 与会话存活相互独立；陈旧会话在核验 durable frontier 后接管原 claim，不创建第二个 claim。
'''
    write("docs/RESEARCH_SCHEDULING_PROTOCOL.en.md", scheduling_en)
    write("docs/RESEARCH_SCHEDULING_PROTOCOL.zh-CN.md", scheduling_zh)

    substitutions = {
        "research_task_publication_contract.json": "research_task_publication_contract_v2.json",
        "research_task_registry.json": "research_task_records/<task-id>/<publication-id>.json",
        "tools/research_task_registry.py": "tools/research_task_records.py",
        "research_scheduler.json": "research_runtime_policy_v2.json",
        "tools/research_scheduler.py": "tools/research_runtime_reducer.py",
        "tools/check_task_registry_cutover.py": "control_plane/check_legacy_control_isolation.py",
    }
    for rel in (
        "docs/RESEARCH_ARCHITECTURE.md",
        "docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md",
        "docs/FOUNDATION_STEWARD_CONTROL_PLANE_ADDENDUM.md",
        "docs/RESEARCH_COMMON_SURFACE.en.md",
        "docs/RESEARCH_COMMON_SURFACE.zh-CN.md",
        "research_roles/EM_FREE_RESEARCHER_ROLE.md",
        "definitions/RESEARCH_DRIVER_FOR_AI.md",
        "definitions/RESEARCH_DRIVER_FOR_AI.zh-CN.md",
    ):
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in substitutions.items():
            text = text.replace(old, new)
        text = text.replace("V1 compatibility/read-only audit surfaces", "historical migration provenance")
        text = text.replace("V1 compatibility/read-only surfaces", "historical migration provenance")
        text = text.replace("V1 read-only compatibility/audit surfaces", "historical migration provenance")
        text = text.replace("V1 compatibility/audit surfaces", "historical migration provenance")
        text = text.replace("frozen legacy scheduler baseline", "immutable V2 task-publication surface")
        path.write_text(text, encoding="utf-8")


def write_isolation_checker() -> None:
    checker = f'''#!/usr/bin/env python3
"""Fail closed if the pre-V2 control surface re-enters main."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_BRANCH = {ARCHIVE_BRANCH!r}
ARCHIVE_SHA = {ARCHIVE_SHA!r}
LEGACY_PATHS = {LEGACY_PATHS!r}
FORBIDDEN_NAMES = (
    "research_scheduler.json",
    "tools/research_scheduler.py",
    "research_task_registry.json",
    "tools/research_task_registry.py",
    "research_task_publication_contract.json",
    "tools/check_task_registry_cutover.py",
)
ACTIVE_PROMPTS = (
    "AGENTS.md",
    "docs/RESEARCH_RUNTIME_STATE_MACHINE.md",
    "docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md",
    "docs/RESEARCH_SCHEDULING_PROTOCOL.en.md",
    "docs/RESEARCH_SCHEDULING_PROTOCOL.zh-CN.md",
    "docs/RESEARCH_ARCHITECTURE.md",
    "docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md",
    "research_roles/EM_FREE_RESEARCHER_ROLE.md",
)


def check() -> list[str]:
    errors: list[str] = []
    for rel in LEGACY_PATHS:
        if (ROOT / rel).exists():
            errors.append(f"legacy control path remains on main: {{rel}}")
    manifest_path = ROOT / "control_plane/legacy_control_migration_manifest.json"
    if not manifest_path.is_file():
        errors.append("migration manifest missing")
        return errors
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "COMPLETE":
        errors.append("migration manifest is not COMPLETE")
    source = manifest.get("source") or {{}}
    if source.get("archive_branch") != ARCHIVE_BRANCH or source.get("commit") != ARCHIVE_SHA:
        errors.append("migration manifest archive pin mismatch")
    rows = manifest.get("tasks")
    if not isinstance(rows, list) or len(rows) != 27:
        errors.append("migration manifest must preserve exactly 27 legacy task identities")
    elif len({{row.get("task_id") for row in rows if isinstance(row, dict)}}) != 27:
        errors.append("migration manifest task identities are duplicated or incomplete")
    authority = manifest.get("authority") or {{}}
    for flag in (
        "mathematical_truth_granted",
        "working_truth_granted",
        "foundation_authority_granted",
        "canonical_promotion_granted",
        "execution_claim_created",
    ):
        if authority.get(flag) is not False:
            errors.append(f"migration manifest illegally grants {{flag}}")
    policy = json.loads((ROOT / "research_runtime_policy_v2.json").read_text(encoding="utf-8"))
    if policy.get("legacy_task_definition_source") is not None or policy.get("legacy_runtime_on_main") is not False:
        errors.append("V2 runtime policy still exposes a legacy definition fallback")
    dispatch = (ROOT / "tools/research_dispatch.py").read_text(encoding="utf-8")
    if "FROZEN_LEGACY_BASELINE" in dispatch or "LEGACY_BARE_EVENT_REPLAY" in dispatch:
        errors.append("live dispatch still contains legacy fallback semantics")
    if "raw authenticated Issue #240 comment objects" not in dispatch:
        errors.append("live dispatch does not fail closed on bare runtime events")
    guard = (ROOT / "control_plane/research_runtime_guard_core.py").read_text(encoding="utf-8")
    if "legacy_task_ids" in guard or "LEGACY_BASELINE_REGISTERED" in guard:
        errors.append("runtime guard still authorizes legacy registration")
    for rel in ACTIVE_PROMPTS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for name in FORBIDDEN_NAMES:
            if name in text:
                errors.append(f"active prompt {{rel}} still names isolated file {{name}}")
        if re.search(r"(?i)do not read|must not read|不要读|不得读取|禁止读取", text):
            errors.append(f"active prompt {{rel}} still relies on file-avoidance instructions")
    return errors


def main() -> int:
    errors = check()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: 27 task identities migrated; pre-V2 control files are physically isolated and live prompts are current-only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''
    write("control_plane/check_legacy_control_isolation.py", checker)


def patch_checks_and_tests() -> None:
    common = read("tools/check_research_common_surface.py")
    common = common.replace('surfaces.get("legacy_scheduler_reducer")', 'surfaces.get("runtime_event_reducer")')
    common = common.replace('"tools/research_scheduler.py"', '"tools/research_runtime_reducer.py"')
    common = common.replace('"research_scheduler.json"', '"research_runtime_policy_v2.json"')
    write("tools/check_research_common_surface.py", common)

    authority = read("control_plane/check_current_control_authority.py")
    old = '''    legacy_tool = read("tools/research_task_registry.py")
    require("Read-only V1 task-registry compatibility surface" in legacy_tool, "V1 registry tool not explicitly read-only")
    require('for name in ("new", "publish", "select")' in legacy_tool, "V1 registry write/select commands are not all fail-closed")
    require("_forbid(command)" in legacy_tool, "V1 registry commands do not route through fail-closed guard")

'''
    new = '''    for isolated in (
        "research_scheduler.json",
        "tools/research_scheduler.py",
        "research_task_registry.json",
        "tools/research_task_registry.py",
        "research_task_publication_contract.json",
        "tools/check_task_registry_cutover.py",
    ):
        require(not (ROOT / isolated).exists(), f"isolated legacy path returned to main: {isolated}")
    require((ROOT / "control_plane/legacy_control_migration_manifest.json").is_file(), "legacy task migration manifest missing")
    require((ROOT / "research_runtime_policy_v2.json").is_file(), "V2 runtime policy missing")
    require((ROOT / "tools/research_runtime_reducer.py").is_file(), "V2 runtime reducer missing")

'''
    authority = require_replace(authority, old, new, "check_current_control_authority legacy block")
    authority = authority.replace(
        '    steward = read("docs/FOUNDATION_STEWARD_CONTROL_PLANE_ADDENDUM.md")\n',
        '    steward = read("docs/FOUNDATION_STEWARD_CONTROL_PLANE_ADDENDUM.md")\n',
    )
    write("control_plane/check_current_control_authority.py", authority)

    workflow = read(".github/workflows/reference-integrity.yml")
    workflow = workflow.replace(
        "      - name: Check legacy scheduler cutover is frozen\n        run: python tools/check_task_registry_cutover.py\n",
        "      - name: Check pre-V2 control files are physically isolated\n        run: python control_plane/check_legacy_control_isolation.py\n",
    )
    write(".github/workflows/reference-integrity.yml", workflow)

    identity = read("tests/test_research_identity.py")
    identity = identity.replace('scheduler = load_tool("research_scheduler", "tools/research_scheduler.py")', 'reducer = load_tool("research_runtime_reducer", "tools/research_runtime_reducer.py")')
    identity = identity.replace("scheduler.", "reducer.")
    identity = identity.replace("test_scheduler_claim_auto_allocates_identity", "test_runtime_claim_auto_allocates_identity")
    write("tests/test_research_identity.py", identity)

    runtime_test = read("tests/test_research_runtime_unittest.py")
    legacy_method = '''    def test_legacy_baseline_cannot_authorize_fresh_redispatch(self):
        state = make_state(task_registration={"state": "LEGACY_BASELINE_REGISTERED", "fresh_redispatch": True})
        with self.assertRaisesRegex(rt.RuntimeStateError, "fresh redispatch"):
            rt.pre_final_gate(state)

'''
    runtime_test = runtime_test.replace(legacy_method, '''    def test_non_v2_registration_cannot_execute(self):
        state = make_state(task_registration={"state": "LEGACY_BASELINE_REGISTERED"})
        with self.assertRaisesRegex(rt.RuntimeStateError, "not executable"):
            rt.pre_final_gate(state)

''')
    runtime_test = runtime_test.replace('        self.assertEqual(contract["task_registry"], "research_task_registry.json")\n', '        self.assertEqual(contract["task_record_store"], "research_task_records/<task-id>/<publication-id>.json")\n')
    runtime_test = runtime_test.replace('        self.assertIn("research_task_publication_contract.json", policy["policy_inputs"])\n        self.assertNotIn("research_task_registry.json", policy["policy_inputs"])\n', '        self.assertIn("research_task_publication_contract_v2.json", policy["policy_inputs"])\n')
    runtime_test = runtime_test.replace('                "tools/check_task_registry_cutover.py",\n', '')
    runtime_test = runtime_test.replace('                "tools/research_task_registry.py",\n', '                "tools/research_runtime_reducer.py",\n')
    write("tests/test_research_runtime_unittest.py", runtime_test)

    role_test = read("tests/test_role_control_authority_unittest.py")
    role_test = role_test.replace('        self.assertEqual("READ_ONLY_COMPATIBILITY_AND_AUDIT_ONLY", data["task_publication"]["legacy_role"])\n', '        self.assertFalse(data["live_dispatch"]["legacy_definition_fallback"])\n')
    role_test = role_test.replace('        self.assertIn("V1 compatibility", text)\n', '        self.assertNotIn("research_task_registry.json", text)\n')
    role_test = role_test.replace('        self.assertIn("tools/research_task_registry.py` are V1 compatibility/read-only", text)\n', '        self.assertNotIn("tools/research_task_registry.py", text)\n')
    start = role_test.find("    def test_v1_registry_surface_fails_closed_for_write_commands(self):\n")
    if start >= 0:
        end = role_test.find("    def test_dispatch_contract_names_recovery_aware_top_level_entry", start)
        if end < 0:
            raise CutoverError("role-control test method boundary missing")
        role_test = role_test[:start] + '''    def test_legacy_control_files_are_physically_absent(self):
        for rel in (
            "research_scheduler.json",
            "tools/research_scheduler.py",
            "research_task_registry.json",
            "tools/research_task_registry.py",
            "research_task_publication_contract.json",
            "tools/check_task_registry_cutover.py",
        ):
            self.assertFalse((ROOT / rel).exists(), rel)
        manifest = self.load("control_plane/legacy_control_migration_manifest.json")
        self.assertEqual("COMPLETE", manifest["status"])
        self.assertEqual(27, manifest["counts"]["legacy_union"])

''' + role_test[end:]
    write("tests/test_role_control_authority_unittest.py", role_test)

    reducer_test = '''import unittest
from datetime import datetime, timezone

from tools import research_runtime_reducer as rr


def task(task_id="RS-T1", state="READY", priority="P1", leverage="HIGH"):
    return {
        "task_id": task_id,
        "base_state": state,
        "priority": priority,
        "leverage": leverage,
        "kind": "RESEARCH",
        "last_progress_at": "2026-09-01T00:00:00+00:00",
        "next_action": "continue",
    }


def event(kind, at, claim_id="c1", **extra):
    value = {
        "schema": rr.EVENT_SCHEMA,
        "event": kind,
        "task_id": "RS-T1",
        "claim_id": claim_id,
        "at": at,
    }
    value.update(extra)
    return value


class RuntimeReducerTests(unittest.TestCase):
    def now(self, value):
        return rr.parse_time(value)

    def test_policy_is_current_only(self):
        policy = rr.load_policy()
        self.assertEqual([], rr.validate_policy(policy))
        self.assertIsNone(policy["legacy_task_definition_source"])
        self.assertFalse(policy["legacy_runtime_on_main"])

    def test_second_claim_cannot_preempt_live_owner(self):
        state = rr.reduce_task(
            task(),
            [event("CLAIM", "2026-09-01T00:00:00+00:00"), event("CLAIM", "2026-09-01T00:01:00+00:00", claim_id="c2")],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:05:00+00:00"),
        )
        self.assertEqual("c1", state["claim_id"])
        self.assertEqual(1, len(state["ignored_events"]))

    def test_expired_claim_returns_to_handoff(self):
        state = rr.reduce_task(
            task(),
            [event("CLAIM", "2026-09-01T00:00:00+00:00", lease_minutes=30)],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:31:00+00:00"),
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_handoff_releases_identity(self):
        rid = rr.researcher_id_for_claim(task(), "c1")
        state = rr.reduce_task(
            task(),
            [
                event("CLAIM", "2026-09-01T00:00:00+00:00"),
                event("HANDOFF", "2026-09-01T00:10:00+00:00", researcher_id=rid, next_action="resume exact frontier"),
            ],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:11:00+00:00"),
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertIsNone(state["claim_id"])
        self.assertEqual(rid, state["last_researcher_id"])

    def test_selection_is_deterministic(self):
        policy = rr.load_policy()
        states = [
            {**task("RS-R", state="READY", priority="P0"), "state": "READY", "dispatch_state": "NEEDS_DISPATCH"},
            {**task("RS-H", state="HANDOFF_READY", priority="P2", leverage="LOW"), "state": "HANDOFF_READY", "dispatch_state": "NEEDS_DISPATCH"},
        ]
        self.assertEqual("RS-H", rr.select_state(states, policy)["task_id"])


if __name__ == "__main__":
    unittest.main()
'''
    write("tests/test_research_runtime_reducer.py", reducer_test)


def delete_old_paths() -> None:
    for rel in [*LEGACY_PATHS, *ONE_SHOT_PATHS, *STALE_TESTS]:
        path = ROOT / rel
        if path.exists():
            path.unlink()


def main() -> int:
    manifest = load("control_plane/legacy_control_migration_manifest.json")
    if manifest.get("status") != "COMPLETE" or manifest.get("counts", {}).get("legacy_union") != 27:
        raise CutoverError("legacy task migration is not complete")
    source = manifest.get("source") or {}
    if source.get("archive_branch") != ARCHIVE_BRANCH or source.get("commit") != ARCHIVE_SHA:
        raise CutoverError("migration manifest archive pin mismatch")

    derive_runtime_reducer()
    write_runtime_policy()
    patch_dispatch()
    patch_runtime_guard()
    patch_publication_fault_isolation()
    patch_machine_json()
    patch_prompts_and_docs()
    write_isolation_checker()
    patch_checks_and_tests()
    delete_old_paths()

    # The checker is imported only after all physical removals are complete.
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from control_plane import check_legacy_control_isolation
    errors = check_legacy_control_isolation.check()
    if errors:
        raise CutoverError("; ".join(errors))
    print("PASS: legacy control surface physically isolated and V2 runtime rewired")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CutoverError, OSError, json.JSONDecodeError) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
