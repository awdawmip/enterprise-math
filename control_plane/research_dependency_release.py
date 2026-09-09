"""Validate declared artifact dependencies from an applied typed release.

An authenticated UNBLOCK supplies the Driver's explicit obligation mapping.
Current publication, operational Result/DR and follow-up views verify its
bindings. This module interprets no requirement prose and creates no registry,
task, CLAIM, review or execution permission.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping

SCHEMA = "ENTERPRISE_MATH_ACCEPTED_REVIEW_DEPENDENCY_RELEASE_V1"
_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,191}$")
_SHA = re.compile(r"^sha256:[0-9a-f]{64}$")
_COMMIT = re.compile(r"^[0-9a-f]{40}$")


class DependencyReleaseError(ValueError):
    pass


def compact(proof: Mapping[str, Any]) -> dict[str, Any]:
    """Keep startup transport bounded; the full proof remains in the route."""
    raw = json.dumps(proof, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return {"schema": SCHEMA, "release_comment_id": proof["release_comment_id"],
            "release_body_sha256": proof["release_body_sha256"],
            "obligation_count": len(proof["obligations"]),
            "evidence_sha256": "sha256:" + hashlib.sha256(raw).hexdigest(),
            "execution_authorized": False}


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise DependencyReleaseError(message)


def _identifier(value: Any) -> bool:
    return isinstance(value, str) and bool(_ID.fullmatch(value))


def _file_digest(root: Path, relative: str) -> str:
    path = root.joinpath(relative).resolve()
    _require(path.is_relative_to(root.resolve()), "dependency record path escapes the source root")
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _publication(task_id: str, publication_id: str, records, root: Path):
    from tools import research_task_records

    row = records.get(task_id)
    _require(isinstance(row, dict) and row.get("publication_id") == publication_id
             and row.get("record_state") == "ACTIVE",
             "dependency release does not name the current operational publication")
    _require(research_task_records.taskbook_blob(root / row["taskbook_path"])
             == row.get("taskbook_blob_sha1"), "dependency publication taskbook bytes changed")
    return row


def _release_entries(event, dependency_ids):
    singular = {"review_obligation_task_id", "review_obligation_publication_id", "gate_evidence"}
    if "dependency_gate_evidence" in event:
        _require(not (singular & set(event)), "ambiguous singular and list dependency release")
        entries = event["dependency_gate_evidence"]
        _require(isinstance(entries, list) and bool(entries), "dependency release list is empty or malformed")
        _require(all(isinstance(row, dict) and set(row) == {
            "task_id", "publication_id", "gate_evidence", "review_ref"} for row in entries),
            "dependency release list requires exact typed obligation and evidence fields")
    else:
        _require(singular <= set(event) and len(dependency_ids) == 1,
                 "nonempty dependencies require a complete typed artifact release")
        entries = [{
            "task_id": event["review_obligation_task_id"],
            "publication_id": event["review_obligation_publication_id"],
            "gate_evidence": event["gate_evidence"],
            "review_ref": event.get("progress_ref"),
        }]
    ids = [row.get("task_id") for row in entries]
    _require(all(_identifier(value) for value in ids) and len(set(ids)) == len(ids)
             and set(ids) == set(dependency_ids),
             "typed release must cover every declared dependency exactly once")
    return {row["task_id"]: row for row in entries}


def _current_gate(entry, dependency, records, result_records, released_at, root: Path):
    import research_driver_followup
    from tools import research_result_records, research_runtime_reducer

    _require(_identifier(entry.get("publication_id")), "dependency publication ID is malformed")
    obligation = _publication(dependency["task_id"], entry["publication_id"], records, root)
    _require(research_runtime_reducer.parse_time(obligation["published_at"]) <= released_at,
             "dependency obligation was published after its release")

    gate = entry.get("gate_evidence")
    required = {"canonical_main", "result_id", "result_record_sha256", "review_id", "followup_id"}
    _require(isinstance(gate, dict) and required <= set(gate)
             and set(gate) <= required | {"accepted_strength"},
             "dependency gate evidence has missing or unsupported fields")
    _require(all(_identifier(gate[field]) for field in ("result_id", "review_id", "followup_id"))
             and isinstance(gate["result_record_sha256"], str)
             and bool(_SHA.fullmatch(gate["result_record_sha256"]))
             and isinstance(gate["canonical_main"], str)
             and bool(_COMMIT.fullmatch(gate["canonical_main"])),
             "dependency gate identifiers or digests are malformed")
    result = result_records.get(gate["result_id"])
    _require(isinstance(result, dict) and _identifier(result.get("task_id"))
             and _identifier(result.get("publication_id")),
             "dependency Result is absent from the current operational view")
    result_publication = _publication(result["task_id"], result["publication_id"], records, root)
    result_path = f"research_result_records/{result['task_id']}/{gate['result_id']}.json"
    _require(result.get("_record_path") == result_path,
             "dependency Result record path differs from its canonical identity")
    result_digest = _file_digest(root, result_path)
    _require(result_digest == gate["result_record_sha256"],
             "dependency raw Result bytes differ from the released digest")

    state = research_result_records.task_result_state(
        result["task_id"], root, result_publication["publication_id"])
    _require(isinstance(state, dict) and state.get("state") == "TERMINAL"
             and state.get("terminal") is True
             and (state.get("result") or {}).get("result_id") == gate["result_id"],
             "dependency Result no longer has current terminal review authority")
    review = state.get("review")
    review_path = f"research_result_reviews/{gate['result_id']}/{gate['review_id']}.json"
    _require(isinstance(review, dict) and review.get("review_id") == gate["review_id"]
             and review.get("review_authority_kind") == "IMMUTABLE_REVIEW"
             and review.get("disposition") == "ACCEPTED"
             and review.get("result_id") == gate["result_id"]
             and review.get("result_record_path") == result_path
             and review.get("result_record_sha256") == result_digest
             and review.get("task_id") == result["task_id"]
             and review.get("publication_id") == result["publication_id"]
             and review.get("_review_path") == review_path,
             "dependency release lacks the exact current accepted immutable Driver review")
    _require(research_runtime_reducer.parse_time(review["reviewed_at"]) <= released_at,
             "dependency review postdates the release")
    expected_ref = (
        f"https://github.com/awdawmip/enterprise-math/blob/{gate['canonical_main']}/{review_path}")
    _require(entry.get("review_ref") == expected_ref,
             "dependency release source link does not bind its exact review")

    followup = research_driver_followup.state_for_review(gate["review_id"], root)
    packet = followup.get("packet")
    _require(followup.get("ready") is True and isinstance(packet, dict)
             and packet.get("packet_id") == gate["followup_id"]
             and packet.get("review_id") == gate["review_id"]
             and packet.get("result_id") == gate["result_id"]
             and packet.get("review_disposition") == "ACCEPTED"
             and packet.get("source_result_record_sha256") == result_digest
             and packet.get("source_publication_id") == result["publication_id"]
             and packet.get("task_id") == result["task_id"],
             "dependency review follow-up is absent, unready, or differently bound")
    _require(research_runtime_reducer.parse_time(packet["created_at"]) <= released_at,
             "dependency follow-up postdates the release")
    followup_path = f"research_driver_followups/{gate['review_id']}/{gate['followup_id']}.json"
    return {
        "task_id": dependency["task_id"], "publication_id": obligation["publication_id"],
        "taskbook_blob_sha1": obligation["taskbook_blob_sha1"],
        "required_artifact": dependency["required_artifact"],
        "result_id": gate["result_id"], "result_record_path": result_path,
        "result_record_sha256": result_digest, "review_id": gate["review_id"],
        "review_record_path": review_path, "review_record_sha256": _file_digest(root, review_path),
        "followup_id": gate["followup_id"], "followup_record_path": followup_path,
        "followup_record_sha256": _file_digest(root, followup_path),
        "historical_source_ref": expected_ref,
    }


def resolve(definition: Mapping[str, Any], events: list[dict[str, Any]], *, now, root: Path):
    """Resolve all declared artifact obligations, without changing any state."""
    try:
        return _resolve(definition, events, now=now, root=root)
    except DependencyReleaseError:
        raise
    except Exception as exc:
        raise DependencyReleaseError(f"dependency release validation failed: {exc}") from exc


def _resolve(definition, events, *, now, root):
    import research_driver_authority
    from tools import research_dispatch, research_runtime_reducer, research_task_records, research_result_records

    dependencies = definition.get("dependencies")
    _require(isinstance(dependencies, list) and bool(dependencies)
             and all(isinstance(dep, dict) and set(dep) == {"task_id", "required_artifact"}
                     and _identifier(dep["task_id"]) and isinstance(dep["required_artifact"], str)
                     and bool(dep["required_artifact"].strip()) for dep in dependencies),
             "unsupported dependencies require a canonical satisfaction model")
    ids = [dep["task_id"] for dep in dependencies]
    _require(len(set(ids)) == len(ids), "duplicate dependency task IDs are ambiguous")
    records = research_task_records.current_records(root)
    publication = _publication(definition["task_id"], definition["publication_id"], records, root)
    # The installed canonical facade adds current parent/scope metadata that the
    # older single-record constructor does not expose. Consume that same facade.
    matching_definitions = [row for row in research_dispatch.merged_definitions(root)
                            if row.get("task_id") == definition["task_id"]]
    _require(len(matching_definitions) == 1, "dependency target has no unique canonical definition")
    canonical = matching_definitions[0]
    _require(all(canonical.get(key) == definition.get(key) for key in (
                 "task_id", "publication_id", "parent_objective_id", "dependencies", "base_state", "hard_block"))
             and canonical.get("publication_id") == publication["publication_id"],
             "dependency proof is not bound to the current task definition")

    authenticated, _ = research_dispatch._event_authentication_filter(canonical, events)
    filtered, _ = research_dispatch._filter_registered_events(canonical, authenticated, root)
    matching = [event for event in filtered if event.get("task_id") == canonical["task_id"]]
    replay = research_runtime_reducer.reduce_task(
        canonical, matching, default_lease_minutes=int(canonical.get("claim_lease_minutes") or 120), now=now)
    ignored = {row["index"] for row in replay["ignored_events"]}
    applied = [(index, event) for index, event in enumerate(matching) if index not in ignored]
    releases = [(index, event) for index, event in applied if event.get("event") == "UNBLOCK"]
    _require(bool(releases), "dependencies have no canonically applied UNBLOCK")
    release_index, release = releases[-1]
    _require(not any(index > release_index and event.get("event") in {"HARD_BLOCK", "DONE", "SUPERSEDE"}
                     for index, event in applied),
             "dependency release was followed by a new block or terminal transition")
    _require(release.get("publication_id") == publication["publication_id"]
             and release.get("schema") == research_dispatch.EVENT_SCHEMA,
             "dependency release is not explicitly bound to the current publication")
    meta = release.get(research_dispatch.GITHUB_META_KEY)
    _require(isinstance(meta, dict) and meta.get("edited") is False
             and meta.get("server_authenticated") is True and meta.get("control_authorized") is True
             and meta.get("issue_number") == 240 and type(meta.get("comment_id")) is int
             and isinstance(meta.get("body_sha256"), str)
             and bool(_SHA.fullmatch(meta["body_sha256"])),
             "dependency release lacks an authenticated unedited Issue 240 envelope")
    _require(sum(event.get(research_dispatch.GITHUB_META_KEY, {}).get("comment_id") == meta["comment_id"]
                 for event in matching) == 1, "duplicate dependency release envelope")
    released_at = research_runtime_reducer.parse_time(meta["created_at"])
    _require(released_at == research_runtime_reducer.parse_time(meta["updated_at"]) and released_at <= now
             and released_at >= research_runtime_reducer.parse_time(publication["published_at"]),
             "dependency release has an invalid publication/server clock")
    author = {"login": meta.get("author_login"), "user_id": meta.get("author_user_id"),
              "author_association": meta.get("author_association")}
    _require(research_driver_authority._server_author_allowed(author, root),
             "dependency release actor is not control-authorized")
    driver = release.get("driver_id")
    _require(isinstance(driver, str), "dependency release has no real Driver binding")
    authority = research_driver_authority.active_authority_at(driver, released_at.isoformat(), root)
    _require(authority is not None
             and authority["authority_record_id"] == release.get("driver_authority_record_id")
             and authority["source_comment_id"] == release.get("driver_authority_source_comment_id")
             and authority["source_comment_id"] < meta["comment_id"],
             "dependency release does not bind the Driver authority active when it was issued")

    entries = _release_entries(release, ids)
    result_records = research_result_records.result_map(root)
    obligations = [_current_gate(entries[dep["task_id"]], dep, records, result_records, released_at, root)
                   for dep in dependencies]
    return {
        "schema": SCHEMA, "task_id": canonical["task_id"], "publication_id": publication["publication_id"],
        "taskbook_blob_sha1": publication["taskbook_blob_sha1"],
        "release_comment_id": meta["comment_id"], "release_body_sha256": meta["body_sha256"],
        "release_created_at": released_at.isoformat(), "release_driver_id": driver,
        "release_driver_authority_record_id": authority["authority_record_id"],
        "obligations": obligations, "validated_at": now.isoformat(),
        "authority": "TYPED_DRIVER_RELEASE_AND_CURRENT_OPERATIONAL_ACCEPTED_REVIEW",
        "requirement_prose_interpreted": False, "execution_authorized": False,
        "claim_created": False, "parent_completion_granted": False,
    }
