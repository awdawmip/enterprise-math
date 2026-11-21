#!/usr/bin/env python3
"""Check proposed memory-evaluation manifests.

This checks declared metadata and synthetic fixtures. It does NOT verify runtime
access controls, detect undeclared leaks, grade mathematics, benchmark models or
prove that a model has not previously seen public material.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

MODE_TRACKS = {
    "M0_CURRENT": {"TASK", "INFORMED", "FREE_A", "UPDATE_REPLAY"},
    "M1_LONG_CONTEXT": {"TASK", "INFORMED", "UPDATE_REPLAY"},
    "M2_FLAT_LEXICAL": {"TASK", "INFORMED", "UPDATE_REPLAY"},
    "M2_FREE_A_VIEW": {"FREE_A"},
    "M3_HYBRID": {"TASK", "INFORMED", "UPDATE_REPLAY"},
    "M4_TYPED_RELATIONS": {"TASK", "INFORMED", "UPDATE_REPLAY"},
    "M5_NOLLM_NATIVE": {"TASK", "INFORMED", "UPDATE_REPLAY"},
    "M6_TRAINED_HELPER": {"TASK", "INFORMED", "UPDATE_REPLAY"},
}
RESEARCH_PRINCIPALS = {"research", "retriever", "memory_builder", "trainer"}
FREE_BASELINE_KINDS = {"foundation", "current_governance"}
BASELINE_KINDS = FREE_BASELINE_KINDS | {"task_input"}
PRECISE_KINDS = {"precise_definition", "precise_condition", "precise_tool"}
EXPOSURE_EVENTS = {"read", "title_preview", "preview", "error_output", "tool_output", "source_exposure"}
SOURCE_ROLES = {"scientific", "governance"}
CLASSIFICATIONS = {"public", "restricted"}
REQUIRED = {
    "run_id", "mode_id", "track", "sample_id", "case_family_id", "split",
    "main_model_revision", "cutoff_at", "source_snapshot_id", "index_build_id",
    "resource_envelope_id", "artifact_classification", "sources", "events",
    "helper", "isolation", "attribution", "cost", "build", "split_manifest", "exposure_profile",
}
HEX_REVISION = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")


def utc_time(value: object, label: str, errors: list[str]) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timezone required")
        return parsed
    except (TypeError, ValueError):
        errors.append(f"{label}: timezone-aware timestamp required")
        return None


def validate_run(run: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(run, dict):
        return ["run must be an object"]
    missing = sorted(REQUIRED - run.keys())
    if missing:
        return [f"missing required fields: {', '.join(missing)}"]
    if run.get("schema") != "EM_MEMORY_RUN_CONTRACT_V1":
        errors.append("unknown run schema")
    if run.get("split") not in {"development", "heldout", "retrospective_public"}:
        errors.append("unknown evaluation split")
    mode, track = run["mode_id"], run["track"]
    if mode not in MODE_TRACKS:
        errors.append("unknown mode")
    elif track not in MODE_TRACKS[mode]:
        errors.append("mode is not eligible for this exposure track")
    cutoff = utc_time(run["cutoff_at"], "cutoff_at", errors)
    if run.get("synthetic"):
        if run.get("artifact_classification") != "PUBLIC_SYNTHETIC_DEVELOPMENT":
            errors.append("synthetic fixture must declare its public development classification")
        if run.get("split") != "development":
            errors.append("public synthetic fixtures must remain development cases")
        if run.get("claim_scope") != "CONTRACT_VALIDATION_ONLY":
            errors.append("synthetic fixture cannot claim model/benchmark performance")

    # The source list is the executor/build/train eligible pool, not evaluator
    # answers. Current governance is separate from replayed scientific knowledge.
    sources: dict[str, dict] = {}
    if not isinstance(run["sources"], list):
        return errors + ["sources must be an array"]
    for source in run["sources"]:
        if not isinstance(source, dict):
            errors.append("source must be an object")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            errors.append("source ID required")
            continue
        if source_id in sources:
            errors.append(f"duplicate source ID: {source_id}")
        sources[source_id] = source
        if not isinstance(source.get("identity"), str) or not source["identity"]:
            errors.append(f"{source_id}: source identity/locator required")
        if not HEX_REVISION.fullmatch(str(source.get("version", ""))):
            errors.append(f"{source_id}: immutable version digest required")
        if source.get("knowledge_role") not in SOURCE_ROLES:
            errors.append(f"{source_id}: explicit scientific/governance role required")
        if source.get("classification") not in CLASSIFICATIONS:
            errors.append(f"{source_id}: explicit classification required")
        if source.get("kind") in {"reference_answer", "grading_rubric", "source_label"}:
            errors.append(f"{source_id}: withheld evaluator material in eligible pool")
        if track == "FREE_A" and source.get("kind") not in FREE_BASELINE_KINDS | PRECISE_KINDS:
            errors.append(f"{source_id}: FREE_A eligible source pool contains nonpermitted result/catalog/task_input material")
        available = utc_time(source.get("available_at"), f"{source_id}.available_at", errors)
        if (source.get("knowledge_role") == "scientific"
                and cutoff and available and available > cutoff):
            errors.append(f"{source_id}: future scientific material crosses replay cutoff")

    exposure = run["exposure_profile"]
    if not isinstance(exposure, dict) or exposure.get("stage") != track:
        errors.append("exposure_profile must declare the same stage as track")
        exposure = {}
    for source_id in exposure.get("mandatory_source_ids", []):
        if source_id not in sources or sources[source_id].get("kind") not in BASELINE_KINDS:
            errors.append("mandatory baseline refers to an undeclared or nonbaseline source")

    split = run["split_manifest"]
    if not isinstance(split, dict):
        errors.append("split_manifest must be an object")
        split = {}
    train_families = set(split.get("train_family_ids", []))
    test_families = set(split.get("heldout_family_ids", []))
    if train_families & test_families:
        errors.append("training and heldout dependency families overlap")
    if run["split"] == "heldout" and run["case_family_id"] not in test_families:
        errors.append("heldout case lacks heldout family membership")

    helper = run["helper"]
    if not isinstance(helper, dict):
        errors.append("helper must be an object")
        helper = {}
    if set(helper.get("training_family_ids", [])) & test_families:
        errors.append("helper training contains heldout dependency family")
    if helper.get("trained_on_project_results") is True:
        trained_until = utc_time(helper.get("training_cutoff_at"), "helper.training_cutoff_at", errors)
        if cutoff and trained_until and trained_until > cutoff:
            errors.append("helper training crosses scientific replay cutoff")
    if track == "FREE_A":
        # This flag concerns the nonmandatory result set from which this run
        # claims relative blindness. It does not exclude knowledge already in
        # the authorized mandatory foundation, even if that foundation embeds
        # earlier results. Actual training exposure still needs external audit.
        if helper.get("trained_on_project_results") is not False:
            errors.append("FREE_A requires no result-trained recommender for the declared nonmandatory result set")
        if run.get("prior_result_exposure") != "NONE_IN_DECLARED_SCOPE":
            errors.append("FREE_A cannot certify unknown or prior result exposure")
        if not exposure.get("withheld_nonmandatory_result_set_id"):
            errors.append("FREE_A needs a declared relative-blindness result set")
    if mode == "M6_TRAINED_HELPER" and not helper.get("training_manifest_digest"):
        errors.append("trained helper needs an immutable training manifest digest")

    build = run["build"]
    if not isinstance(build, dict):
        errors.append("build must be an object")
        build = {}
    if run["split"] == "heldout":
        if build.get("saw_heldout_questions") is not False:
            errors.append("heldout question exposure during memory build is not excluded")
        if build.get("saw_answer_labels") is not False:
            errors.append("answer-label exposure during memory build is not excluded")
    for source_id in build.get("source_ids", []):
        if source_id not in sources:
            errors.append(f"build references undeclared source: {source_id}")
        elif track == "FREE_A" and sources[source_id].get("kind") not in FREE_BASELINE_KINDS | PRECISE_KINDS:
            errors.append("FREE_A memory build uses additional result/catalog/task_input material")
    if track == "FREE_A" and build.get("used_withheld_results_for_index_or_ranking") is not False:
        errors.append("FREE_A build/ranking exposure to withheld results is not excluded")

    isolation = run["isolation"]
    if not isinstance(isolation, dict):
        errors.append("isolation must be an object")
        isolation = {}
    if set(isolation.get("answer_store_readable_by", [])) & RESEARCH_PRINCIPALS:
        errors.append("research/build/train principal can read evaluator answers")
    if run["split"] == "heldout" and isolation.get("answer_store_readable_by") != ["evaluator"]:
        errors.append("heldout answer access must be explicitly evaluator-only")

    attribution = run["attribution"]
    if not isinstance(attribution, dict):
        errors.append("attribution must be an object")
        attribution = {}
    if mode == "M5_NOLLM_NATIVE":
        if attribution.get("entry_basis") != "surface_observation":
            errors.append("native Nollm entry was not selected from Surface observation")
        if attribution.get("fallback_source_ids") and attribution.get("label") == "native_only":
            errors.append("fallback evidence cannot be credited as native-only success")

    formed_questions: set[str] = set()
    selected_sources: dict[str, set[str]] = {}
    native_seen: set[str] = set()
    baseline_seen: set[str] = set()
    fallback_seen: set[str] = set()
    previous_time: datetime | None = None
    if not isinstance(run["events"], list):
        return errors + ["events must be an array"]
    for event in run["events"]:
        if not isinstance(event, dict):
            errors.append("event must be an object")
            continue
        event_time = utc_time(event.get("at"), "event.at", errors)
        if previous_time and event_time and event_time < previous_time:
            errors.append("events are not in chronological order")
        if event_time:
            previous_time = event_time
        event_type = event.get("type")
        source_fields = {"source_id", "source_ids"} & event.keys()
        if {"source", "sources", "payload_source_ids"} & event.keys():
            errors.append("unsupported source-bearing event field; use source_id/source_ids")
        if source_fields and event_type not in EXPOSURE_EVENTS | {"native_select"}:
            errors.append("unknown source-bearing event type")
        if event_type == "question_formed":
            question_id = event.get("question_id")
            if question_id:
                formed_questions.add(question_id)
            continue
        if event_type not in EXPOSURE_EVENTS | {"native_select"}:
            continue
        if not source_fields:
            errors.append("content exposure event must declare source_id/source_ids, even an empty list")
            continue
        source_ids = event.get("source_ids", [])
        if not isinstance(source_ids, list) or not all(isinstance(item, str) for item in source_ids):
            errors.append("event source_ids must be a list of source IDs")
            continue
        source_ids = list(source_ids)
        if "source_id" in event:
            if not isinstance(event["source_id"], str):
                errors.append("event source_id must be a source ID")
                continue
            source_ids.append(event["source_id"])
        recipients = event.get("exposed_to", "internal" if event_type == "native_select" else "research")
        recipients = [recipients] if isinstance(recipients, str) else recipients
        if not isinstance(recipients, list) or not all(isinstance(item, str) for item in recipients):
            errors.append("exposed_to must name declared principals")
            continue
        if set(recipients) - (RESEARCH_PRINCIPALS | {"evaluator", "internal"}):
            errors.append("unknown exposure principal")
        visible = bool(set(recipients) & RESEARCH_PRINCIPALS)
        if event_type == "native_select":
            selection_id = event.get("selection_id")
            if not isinstance(selection_id, str) or not selection_id:
                errors.append("native selection needs a selection_id")
            elif selection_id in selected_sources:
                errors.append("native selection_id is reused")
            else:
                selected_sources[selection_id] = set(source_ids)
        for source_id in source_ids:
            source = sources.get(source_id)
            if source is None:
                errors.append(f"exposure references undeclared source: {source_id}")
                continue
            kind = source.get("kind")
            if track == "FREE_A" and visible:
                if kind in FREE_BASELINE_KINDS:
                    pass
                elif kind in PRECISE_KINDS:
                    if event.get("question_id") not in formed_questions:
                        errors.append("FREE_A precise lookup precedes its formed question")
                    if event.get("relevance_declared") is not True:
                        errors.append("FREE_A precise lookup lacks a question/relevance relation")
                else:
                    errors.append("FREE_A exposure exposes result/catalog/recommendation material or task_input")
            if event_type == "native_select" or not visible:
                continue
            route = event.get("route", "unspecified")
            if route in {"native", "access_after_native"}:
                if source_id not in selected_sources.get(event.get("selection_id"), set()):
                    errors.append("native/Access source read lacks a preceding native selection")
                elif event_type == "read":
                    native_seen.add(source_id)
            elif route == "fallback":
                fallback_seen.add(source_id)
            elif route in {"direct", "baseline"}:
                if kind in BASELINE_KINDS and source_id in exposure.get("mandatory_source_ids", []):
                    if event_type == "read":
                        baseline_seen.add(source_id)
                elif mode == "M5_NOLLM_NATIVE":
                    # Direct source retrieval may be legitimate, but contributes
                    # extra evidence and cannot be credited to native navigation.
                    fallback_seen.add(source_id)
            elif mode == "M5_NOLLM_NATIVE" and source_ids:
                errors.append("native-mode source exposure has an unspecified/unknown retrieval route")

    if not set(attribution.get("native_source_ids", [])).issubset(native_seen):
        errors.append("native evidence attribution lacks corresponding native read event")
    if not set(attribution.get("fallback_source_ids", [])).issubset(fallback_seen):
        errors.append("fallback attribution lacks corresponding fallback read event")
    if fallback_seen - set(attribution.get("fallback_source_ids", [])):
        errors.append("fallback read event is missing from attribution")
    if fallback_seen and attribution.get("label") == "native_only":
        errors.append("observed fallback read cannot be credited as native-only success")
    for claim in run.get("returned_claims", []):
        source = sources.get(claim.get("source_id"), {})
        source_claim = source.get("claims", {}).get(claim.get("id"))
        if source_claim is None:
            errors.append("returned claim has no declared source claim metadata")
        elif claim.get("status") != source_claim.get("status"):
            errors.append("returned claim changes declared source status")
        elif claim.get("contract_digest") != source_claim.get("contract_digest"):
            errors.append("returned claim changes its declared condition contract")
        if (mode == "M5_NOLLM_NATIVE" and attribution.get("label") == "native_only"
                and claim.get("source_id") not in native_seen | baseline_seen):
            errors.append("native-only returned claim lacks native/Access or mandatory-baseline read support")
    for relation in run.get("relations", []):
        if relation.get("kind") in {"ANALOGY_CANDIDATE", "REUSE_IDENTIFIED"} and relation.get("asserted_proved_transfer"):
            errors.append("candidate relation is promoted to proved transfer")
    for export in run.get("exports", []):
        if export.get("classification") == "public":
            for source_id in export.get("contains_source_ids", []):
                if source_id not in sources or sources[source_id].get("classification") != "public":
                    errors.append("public export includes undeclared or restricted source content")
    # None/unknown costs are valid. Do not silently convert them to zero.
    if not isinstance(run["cost"], dict) or "measurement_status" not in run["cost"]:
        errors.append("cost needs measurement_status; unknown amounts must stay unknown")
    return errors


def source_signature(run: dict) -> str:
    """Compare the declared eligible source identities, not only snapshot names."""
    fields = ("id", "identity", "version", "kind", "knowledge_role", "classification", "available_at")
    rows = [{field: source.get(field) for field in fields}
            for source in run.get("sources", []) if isinstance(source, dict)]
    return json.dumps(sorted(rows, key=lambda item: json.dumps(item, sort_keys=True)), sort_keys=True)


def validate_comparison(bundle: object) -> list[str]:
    if not isinstance(bundle, dict) or not isinstance(bundle.get("runs"), list):
        return ["comparison must contain a runs array"]
    errors: list[str] = []
    groups: dict[str, list[dict]] = {}
    for run in bundle["runs"]:
        run_id = run.get("run_id", "<missing>") if isinstance(run, dict) else "<invalid-run>"
        for error in validate_run(run):
            errors.append(f"{run_id}: {error}")
        if isinstance(run, dict):
            groups.setdefault(str(run.get("sample_id")), []).append(run)
    intervention = bundle.get("intervention")
    if intervention in {"memory_only", "learned_helper"}:
        for sample_id, group in groups.items():
            for field in ("main_model_revision", "source_snapshot_id", "cutoff_at",
                          "resource_envelope_id", "track", "exposure_profile", "prior_result_exposure"):
                if len({json.dumps(run.get(field), sort_keys=True) for run in group}) > 1:
                    errors.append(f"{sample_id}: {intervention} comparison changes {field}")
            if len({source_signature(run) for run in group}) > 1:
                errors.append(f"{sample_id}: comparison changes actual eligible source identities/versions/roles/classifications")
            if intervention == "memory_only":
                if len({json.dumps(run.get("helper"), sort_keys=True) for run in group}) > 1:
                    errors.append(f"{sample_id}: memory_only comparison changes fixed helper configuration; use learned_helper")
            else:
                if any(not run.get("candidate_pool_id") for run in group):
                    errors.append(f"{sample_id}: learned_helper comparison needs a frozen candidate_pool_id")
                elif len({run["candidate_pool_id"] for run in group}) > 1:
                    errors.append(f"{sample_id}: learned_helper comparison changes candidate pool")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="A run contract or comparison JSON")
    parser.add_argument("--comparison", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    errors = validate_comparison(data) if args.comparison else validate_run(data)
    print(json.dumps({
        "passed": not errors,
        "scope": "DECLARED_CONTRACT_ONLY",
        "not_verified": ["runtime isolation", "undeclared leaks", "model prior exposure",
                         "mathematical correctness", "retrieval performance", "cost savings"],
        "errors": errors,
    }, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
