"""Synthetic routing regressions; no claim, identity or scientific verdict issued."""
import copy
import hashlib
import json
from datetime import datetime, timezone
from unittest import mock

import pytest

from control_plane import research_continuation as continuation


TYPED = "PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER"


def test_released_predecessor_routes_to_existing_typed_preparation():
    state = {"dispatch_state": "NEEDS_DISPATCH", "claim_id": None,
             "last_claim_id": "prior-claim", "last_claim_comment_id": 101}
    original = copy.deepcopy(state)
    route = continuation._route(state)
    assert route["action"] == TYPED
    assert route["preparation"] == {
        "operation": "continuation_prepare", "expected_previous_claim_id": "prior-claim",
        "expected_previous_comment_id": 101, "verified_frontier_required": True,
        "use_current_own_session": True, "ordinary_prepare_allowed": False,
        "preparation_grants_claim": False,
    }
    assert not route["execution_authorized"] and not route["requires_predecessor_contact"]
    assert state == original


def test_task_without_predecessor_keeps_fresh_prepare_route():
    route = continuation._route({"dispatch_state": "NEEDS_DISPATCH", "claim_id": None})
    assert route["action"] == "REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION"
    assert "preparation" not in route and not route["execution_authorized"]


@pytest.mark.parametrize("extra, action, role", [
    ({"dispatch_state": "LEASED", "claim_id": "live"}, "VERIFY_LIVENESS_THEN_PREPARE_EXPLICIT_TAKEOVER", "RESEARCHER"),
    ({"dispatch_state": "COMPLETE"}, "CONSUME_COMPLETED_RECORDS", "NONE"),
    ({"execution_lane_id": "lane"}, "SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED", "CONTROL_PLANE_MAINTENANCE"),
    ({"dispatch_state": "AWAITING_REVIEW"}, "ACTIVATE_NEW_DRIVER_AND_REVIEW_FROZEN_RESULT", "RESEARCH_DRIVER"),
])
def test_routing_change_does_not_replace_live_review_lane_or_completion_scope(extra, action, role):
    state = {"dispatch_state": "NEEDS_DISPATCH", "last_claim_id": "prior", "last_claim_comment_id": 7, **extra}
    route = continuation._route(state)
    assert (route["action"], route["required_role"]) == (action, role)
    assert "preparation" not in route and not route["execution_authorized"]


def test_governance_recovery_still_requires_driver_authority():
    route = continuation._route({"dispatch_state": "NEEDS_DISPATCH", "kind": "GOVERNANCE", "last_claim_id": "prior", "last_claim_comment_id": 7})
    assert route["action"] == TYPED and route["required_role"] == "RESEARCH_DRIVER"
    assert route["requires_current_role_authorization"] and not route["execution_authorized"]


def test_packet_includes_predecessor_cas_and_original_source_verified_inputs(tmp_path):
    from tools import research_dispatch, research_task_records, research_result_records, research_taskbook
    source = "a" * 40
    (tmp_path / "EM_SNAPSHOT_READY.json").write_text(json.dumps({"sha": source}))
    taskbook = "research_tasks/synthetic.md"
    publication = {"task_id": "RS-TEST", "publication_id": "TP2-TEST", "taskbook_path": taskbook}
    bodies = {
        taskbook: research_taskbook.render_taskbook({"task_id": "RS-TEST"}, "Synthetic control fixture only."),
        "research_task_records/RS-TEST/TP2-TEST.json": json.dumps(publication),
    }
    blobs = {}
    for path, text in bodies.items():
        p = tmp_path / path
        p.parent.mkdir(parents=True, exist_ok=True)
        raw = text.encode()
        p.write_bytes(raw)
        blobs[path] = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    (tmp_path / "EM_SOURCE_BLOBS.json").write_text(json.dumps({"schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1", "source_commit": source, "blobs": blobs}))
    runtime = {"task_id": "RS-TEST", "state": "HANDOFF_READY", "dispatch_state": "NEEDS_DISPATCH",
               "claim_id": None, "last_claim_id": "old", "last_claim_comment_id": 101}
    with mock.patch.object(continuation, "_definition", return_value={"task_id": "RS-TEST", "publication_id": "TP2-TEST", "base_state": "READY"}), \
         mock.patch.object(research_task_records, "current_records", return_value={"RS-TEST": publication}), \
         mock.patch.object(research_dispatch, "reduce_definition", return_value=runtime), \
         mock.patch.object(research_result_records, "task_result_state", return_value=None):
        packet = continuation.continuation_packet("RS-TEST", root=tmp_path, events=[], now=datetime(2026, 11, 9, tzinfo=timezone.utc), source_commit=source)
    assert packet["route"]["action"] == TYPED
    assert packet["route"]["preparation"]["expected_previous_comment_id"] == 101
    assert {a["path"] for a in packet["source_artifacts"]} == set(bodies)
    assert all(a["source_commit"] == source for a in packet["source_artifacts"])
    assert packet["frontier_template"]["completed_units"] == []
    assert not packet["execution_authorized"]
