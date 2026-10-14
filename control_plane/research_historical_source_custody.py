"""One exact historical X6 custody packet; no canonical aliases or science rewrite."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from control_plane import research_historical_result_intake as h

TASK = "RS-X6-LEGACY-PLANE-RECONCILIATION"
PUBLICATION = "TP2-B4A441B23DA3159232C2"
RESULT = "RR-943A793DB1F7B8012A85"
EXECUTION = "ER-1508037CD774DEDA90E8"
ORIGINAL_SOURCE = "a0bfa8eace20b061f5b228c733acdc46221388d7"
PREFIX = f"research_artifacts/HISTORICAL_RESULT_CUSTODY/{TASK}/{ORIGINAL_SOURCE}"
UNKNOWN = "UNKNOWN_NO_RECOVERED_AUTHENTICATED_SERVER_ENVELOPES"
SUMMARY = "research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/recomputation_summary.json"
MAP_PIN = {"path": PREFIX + "/CUSTODY_MAP_V1.json",
           "sha256": "92cfe0e6dadb7bb52d6b25703e071bb0c4273503d39a84a62f89ad7955f96ad2",
           "git_blob_sha1": "2682c36453108b3deab251d061d3a861523ded7b"}
OBSERVATION = {"logical_path": SUMMARY,
               "raw_declared_sha256": "sha256:a40e89f66ffa42b684b918780994cdfd86b176eebdd3a71d87b89c815e975839",
               "actual_sha256": "21ac687263bc55283be5e50dcbab8dd3b6024900a323f941b3f703077cebf46f",
               "git_blob_sha1": "c6d42b50e75a9c05e93e922e88ddfd9f1e2eb14a",
               "basis": "MATCHING_ORIGINAL_PRIMARY_GIT_BLOB_AND_FULL_RAW_BYTES"}
ERRORS = ["unknown execution record", "invalid method_harvest", "invalid independence_status",
          "output digest drift: " + SUMMARY]
FALSE_FLAGS = ("execution_authentication_restored", "canonical_execution_alias_created",
               "hard_target_alias_created", "scientific_bytes_rewritten")


def map_pin(target: dict[str, Any]) -> dict[str, str]:
    """Closed opt-in; the map is also frozen inside the signed intake payload."""
    expected = {"schema": "ENTERPRISE_MATH_EXACT_SOURCE_CUSTODY_EVIDENCE_V1", "map_pin": MAP_PIN,
                "scientific_path_binding": "EXACT_NONCANONICAL_CUSTODY_MAP_ONLY",
                "secondary_digest_policy": "EXACT_SINGLE_PINNED_PRIMARY_BLOB_OBSERVATION",
                **{key: False for key in FALSE_FLAGS}}
    profile = target.get("historical_source_custody")
    h._keys(profile, frozenset(expected), "historical source custody profile")
    h._require(profile == expected and all(profile[key] is False for key in FALSE_FLAGS),
               "unsupported exact source custody profile")
    h._require("historical_execution_evidence" not in target, "custody cannot mix execution evidence profiles")
    h._require((target.get("task_id"), target.get("publication_id"), target.get("historical_result_id")) ==
               (TASK, PUBLICATION, RESULT), "custody profile is limited to the exact historical X6 target")
    h._require(target.get("authorizing_governance_task_id") == "RS-GOV-ORPHAN-CONTROL-RECOVERY-20261003",
               "custody target requires its original exact GOV scope")
    h._require(target.get("historical_authentication_status") == UNKNOWN,
               "custody cannot restore historical authentication")
    h._require(target.get("allowed_ordinary_audit_errors") == ERRORS,
               "custody permits only its exact historical diagnosis")
    return copy.deepcopy(MAP_PIN)


def _safe_logical(value: Any) -> str:
    h._require(isinstance(value, str) and bool(value) and "\\" not in value and "\0" not in value,
               "invalid custody logical path")
    path = Path(value)
    h._require(not path.is_absolute() and path.as_posix() == value and all(part not in (".", "..") for part in path.parts),
               "unsafe custody logical path")
    return value


def _read_pin(root: Path, row: dict[str, Any]) -> bytes:
    path = h._path(root, row["path"])
    h._require(path == root.resolve() / row["path"], "custody pin contains a symlink or escape")
    raw = path.read_bytes()
    h._require(hashlib.sha256(raw).hexdigest() == row["sha256"]
               and hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest() == row["git_blob_sha1"],
               "immutable custody evidence byte drift: " + row["path"])
    return raw


def _mapping(root: Path, value: dict[str, Any], old: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, bytes]]:
    """Validate closed structure after the complete map bytes have matched MAP_PIN."""
    expected_keys = {"schema", "original_source_commit", "task_id", "publication_id", "historical_result_id",
                     "custody_prefix", "entries", "secondary_digest_observations", "historical_authentication_status", *FALSE_FLAGS}
    h._keys(value, frozenset(expected_keys), "custody map")
    h._require(value["schema"] == "ENTERPRISE_MATH_EXACT_HISTORICAL_RESULT_SOURCE_CUSTODY_MAP_V1"
               and value["original_source_commit"] == ORIGINAL_SOURCE and value["custody_prefix"] == PREFIX
               and (value["task_id"], value["publication_id"], value["historical_result_id"]) == (TASK, PUBLICATION, RESULT),
               "custody map identity mismatch")
    h._require(value["historical_authentication_status"] == UNKNOWN and all(value[key] is False for key in FALSE_FLAGS),
               "custody map cannot restore authority or rewrite science")
    h._require(value["secondary_digest_observations"] == [OBSERVATION], "custody requires the single exact secondary digest observation")
    manifest = old.get("output_manifest")
    h._require(isinstance(manifest, list) and len(manifest) == 4, "custody requires the four original scientific outputs")
    logical_outputs = [_safe_logical(row.get("path")) for row in manifest]
    expected_paths = set(logical_outputs) | {f"research_result_records/{TASK}/{RESULT}.json", f"research_execution_records/{TASK}/{EXECUTION}.json"}
    h._require(len(logical_outputs) == len(set(logical_outputs)) and len(expected_paths) == 6,
               "custody original manifest duplicates or overlaps control records")
    entries = value["entries"]
    h._require(isinstance(entries, list) and len(entries) == 6, "custody requires exactly six mapping rows")
    indexed = {}
    frozen_bytes = {}
    for row in entries:
        h._keys(row, frozenset(("logical_path", "physical_path", "bytes", "sha256", "git_blob_sha1")), "custody map entry")
        logical = _safe_logical(row["logical_path"])
        h._require(logical not in indexed and logical in expected_paths, "custody map has duplicate or unexpected logical path")
        h._require(row["physical_path"] == PREFIX + "/originals/" + logical, "custody physical path differs from its exact logical mapping")
        physical = h._path(root, row["physical_path"])
        # Reject redirection even within the repository; custody must be actual
        # bytes at the immutable map's literal physical location.
        h._require(physical == root.resolve() / row["physical_path"], "custody physical path contains a symlink or escape")
        h._require(type(row["bytes"]) is int and row["bytes"] > 0, "custody byte length must be a positive integer")
        raw = _read_pin(root, {"path": row["physical_path"], "sha256": row["sha256"], "git_blob_sha1": row["git_blob_sha1"]})
        h._require(len(raw) == row["bytes"], "custody byte length drift")
        h._require(not (root / logical).exists(), "custody originals must remain outside canonical logical paths")
        indexed[logical] = row
        frozen_bytes[logical] = raw
    h._require(set(indexed) == expected_paths, "custody mapping does not cover the exact original packet")
    return indexed, frozen_bytes


class _OriginalBytes:
    def __init__(self, raw: bytes):
        self._raw = raw

    def exists(self) -> bool:
        return True

    def read_bytes(self) -> bytes:
        return self._raw


class _ScientificView:
    """Read-only path resolution solely for audit_result_record's four outputs.

    No filesystem enumeration, execution map or runtime discovery interface is
    exposed. The real root, never this view, is used for execution-map checks.
    """
    def __init__(self, raw: dict[str, bytes]):
        self._paths = {logical: _OriginalBytes(value) for logical, value in raw.items()}

    def __truediv__(self, logical: str) -> _OriginalBytes:
        h._require(logical in self._paths, "ordinary scientific audit requested an unmapped custody path")
        return self._paths[logical]


def science(root: Path, target: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    custody_pin = map_pin(target)
    map_raw = _read_pin(root, custody_pin)
    for key in ("result_pin", "execution_pin", "publication_pin", "taskbook_pin"):
        h._check_pin(root, target[key])
    old_raw = _read_pin(root, target["result_pin"])
    er_raw = _read_pin(root, target["execution_pin"])
    old = json.loads(old_raw)
    er = json.loads(er_raw)
    publication = json.loads(_read_pin(root, target["publication_pin"]))
    mapping = json.loads(map_raw)
    entries, original_bytes = _mapping(root, mapping, old)
    h._require(original_bytes[f"research_result_records/{TASK}/{RESULT}.json"] == old_raw
               and original_bytes[f"research_execution_records/{TASK}/{EXECUTION}.json"] == er_raw,
               "custody control bytes changed during validation")
    h._require(old.get("result_id") == RESULT and old.get("execution_record_id") == er.get("execution_record_id") == EXECUTION,
               "custody Result/execution identity mismatch")
    h._require(er.get("record_schema") == "ENTERPRISE_MATH_RESEARCH_EXECUTION_RECORD_V1", "wrong custody execution schema")
    for key in ("task_id", "publication_id"):
        h._require(old.get(key) == er.get(key) == publication.get(key) == target[key], "custody publication scope mismatch")
    for key in ("claim_id", "researcher_id", "execution_branch", "execution_branch_base", "taskbook_path", "taskbook_blob_sha1"):
        h._require(h._text(old.get(key)) and old[key] == er.get(key), "custody execution-linked field mismatch: " + key)
    h._require(old["taskbook_path"] == publication.get("taskbook_path") == target["taskbook_pin"]["path"], "custody Taskbook path mismatch")
    book = h.pin(root, target["taskbook_pin"]["path"])
    h._require(all(row["taskbook_blob_sha1"].removeprefix("sha1:") == book["git_blob_sha1"] for row in (old, er, publication)),
               "custody Taskbook byte mismatch")
    for field, logical in (("result_pin", f"research_result_records/{TASK}/{RESULT}.json"),
                           ("execution_pin", f"research_execution_records/{TASK}/{EXECUTION}.json")):
        row = entries[logical]
        h._require(target[field] == {"path": row["physical_path"], "sha256": row["sha256"], "git_blob_sha1": row["git_blob_sha1"]},
                   "custody control pin differs from mapped original")
    from control_plane import research_result_records_impl as impl
    h._require(EXECUTION not in impl.execution_map(root), "custody ER cannot enter the canonical execution map")
    outputs = []
    scientific_paths = {}
    for declared in old["output_manifest"]:
        h._keys(declared, frozenset(("path", "sha256", "git_blob_sha1")), "original custody manifest entry")
        logical = declared["path"]
        row = entries[logical]
        h._require(declared["git_blob_sha1"].removeprefix("sha1:") == row["git_blob_sha1"], "custody original primary blob mismatch")
        observation = None
        if logical == SUMMARY:
            h._require(declared["sha256"] == OBSERVATION["raw_declared_sha256"] and row["sha256"] == OBSERVATION["actual_sha256"]
                       and row["git_blob_sha1"] == OBSERVATION["git_blob_sha1"], "custody secondary digest observation changed")
            observation = copy.deepcopy(OBSERVATION)
        else:
            h._require(declared["sha256"].removeprefix("sha256:") == row["sha256"], "unapproved custody secondary digest mismatch")
        actual = {"path": row["physical_path"], "bytes": len(original_bytes[logical]),
                  "sha256": row["sha256"], "git_blob_sha1": row["git_blob_sha1"]}
        outputs.append({"schema": "ENTERPRISE_MATH_HISTORICAL_CUSTODY_OUTPUT_V1", **actual,
                        "logical_path": logical, "original_manifest_entry": copy.deepcopy(declared),
                        "secondary_digest_observation": observation})
        scientific_paths[logical] = original_bytes[logical]
    h._require(SUMMARY in scientific_paths and old.get("return_path") in scientific_paths, "custody return or summary absent from outputs")
    # This view cannot create a record-map alias. The ordinary audit receives
    # raw Result fields and no authenticated historical execution relation.
    failures = impl.audit_result_record(old, None, _ScientificView(scientific_paths))
    errors = {error.split(": ", 1)[-1] for error in failures}
    h._require(errors == set(ERRORS), "custody audit has an unapproved failure or changed diagnosis")
    return old, outputs
