"""Administrative freeze and connector payloads; never import or rerun science.

No default action. Use status while preparing; run prepare only after all actual
reviews and continuation notes are complete. Existing packages are immutable.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
PLAN_NAME = "PLANNED_PUBLICATION_FILES.json"
LOCK_NAME = ".adjacent_trace_publication_prepare.lock"
SEAL_NAME = "LOCAL_FREEZE_RECEIPT.json"


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def git_blob(value):
    return hashlib.sha1(b"blob " + str(len(value)).encode("ascii") + b"\0" + value).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def relative_name(name):
    require(isinstance(name, str) and name and "\\" not in name,
            "Use a nonempty forward-slash relative path")
    path = PurePosixPath(name)
    require(not path.is_absolute() and all(x not in ("", ".", "..") for x in name.split("/")),
            "Unsafe relative path: " + name)
    require(":" not in name and "\0" not in name, "Unsafe path character")
    return name


def under(root, name):
    relative_name(name)
    target = root.joinpath(*PurePosixPath(name).parts)
    require(target.resolve().is_relative_to(root.resolve()), "Path escapes package root: " + name)
    # Immutable snapshots must not depend on symlinks or junctions.
    cursor = target
    while cursor != root:
        require(not cursor.is_symlink(), "Symlink input/output is not accepted: " + str(cursor))
        if hasattr(cursor, "is_junction"):
            require(not cursor.is_junction(), "Junction input/output is not accepted: " + str(cursor))
        cursor = cursor.parent
    return target


def new_write(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def load_plan():
    raw = (HERE / PLAN_NAME).read_bytes()
    plan = json.loads(raw)
    require(plan["schema"] == "ADJACENT_TRACE_PUBLICATION_PLAN_V1", "Wrong plan schema")
    require(plan["status"] == "PLANNED_NOT_FROZEN", "Do not mutate a prior frozen plan")
    names = plan["required_files"]
    require(isinstance(names, list) and len(names) == len(set(names)), "Duplicate input path")
    require(PLAN_NAME in names and Path(__file__).name in names, "Publish plan and packager source")
    for name in names:
        relative_name(name)
        require(PurePosixPath(name).suffix in (".py", ".md", ".json"),
                "Only explicit UTF-8 project records belong in required_files: " + name)
        require("__pycache__" not in PurePosixPath(name).parts, "Do not publish compiled files")
    prefix = plan["remote_prefix"]
    require(isinstance(prefix, str) and prefix.endswith("/"), "Remote prefix must end in /")
    relative_name(prefix[:-1])
    require(re.fullmatch(r"[0-9a-f]{40}", plan["prior_science_commit"]) is not None,
            "Prior checkpoint must be an exact commit")
    relative_name(plan["publication_directory"])
    relative_name(plan["manifest_path"])
    require(plan["manifest_path"] not in names, "Manifest must not recursively include itself")
    require(isinstance(plan["chunk_characters"], int) and
            4 <= plan["chunk_characters"] <= 80000 and plan["chunk_characters"] % 4 == 0,
            "Chunk size must be base64-aligned and at most 80000 characters")
    for key in ("compressed_path", "summary_path", "started_path", "source_path", "plan_path",
                "reader_path", "record_review_path"):
        relative_name(plan["science"][key])
    for key in ("summary_path", "started_path", "source_path", "plan_path",
                "reader_path", "record_review_path"):
        require(plan["science"][key] in names, "Missing required scientific binding " + key)
    if plan["publication_ready"]:
        final_markdown = {name for name in names if name.endswith(".md") and name != plan["science"]["plan_path"]}
        require(set(plan["reviewed_symbolic_and_report_pins"]) == final_markdown,
                "Every final proof, review and continuation text needs its exact frozen pin")
    return plan, raw


def check_unfrozen(plan):
    final = under(HERE, plan["publication_directory"])
    require(not os.path.lexists(final), "Frozen publication directory already exists: " + str(final))
    require(not os.path.lexists(HERE / LOCK_NAME), "A prepare lock exists; inspect the original attempt")
    legacy = under(HERE, plan["manifest_path"])
    require(not os.path.lexists(legacy), "A legacy frozen manifest already exists: " + str(legacy))
    parent = under(HERE, plan["science"]["compressed_path"]).parent
    pattern = Path(plan["science"]["compressed_path"]).name + ".part*.b64"
    require(not list(parent.glob(pattern)), "Legacy base64 chunks already exist; do not overwrite")
    return final


def collect(plan, plan_raw):
    """Read all inputs and check bindings before creating any output or lock."""
    require(plan["publication_ready"] and not plan["pending_finalization"],
            "Publication list is still a draft; finish the declared finalization before prepare")
    final = check_unfrozen(plan)
    names = list(plan["required_files"])
    science = plan["science"]
    needed = names + [science["compressed_path"]]
    missing = [name for name in needed if not under(HERE, name).is_file()]
    require(not missing, "Missing required inputs: " + ", ".join(missing))
    for name in science["failure_paths"]:
        require(not os.path.lexists(under(HERE, name)), "Scientific failure artifact exists: " + name)
    source_bytes = {name: under(HERE, name).read_bytes() for name in names}
    require(source_bytes[PLAN_NAME] == plan_raw, "Plan changed during input collection")
    for name, raw in source_bytes.items():
        raw.decode("utf-8")
        require(bool(raw), "Empty required input: " + name)
    compressed = under(HERE, science["compressed_path"]).read_bytes()
    raw = gzip.decompress(compressed)
    summary = json.loads(source_bytes[science["summary_path"]])
    started = json.loads(source_bytes[science["started_path"]])
    results = json.loads(raw)
    require(summary["status"] == science["expected_status"] and
            results["status"] == science["expected_status"], "Execution does not have declared finite PASS status")
    for label, value in (("raw", raw), ("gzip", compressed)):
        require(summary[label + "_bytes"] == len(value) and
                summary[label + "_sha256"] == sha256(value), "Summary " + label + " bytes/hash mismatch")
    for label, name in (("source_sha256", science["source_path"]),
                        ("plan_sha256", science["plan_path"])):
        digest = sha256(source_bytes[name])
        require(summary[label] == started[label] == results["binding"][label] == digest,
                "Frozen execution binding differs from supplied " + name)
    # Reading JSON fields is administrative verification, not a scientific replay.
    require(summary["schema"] == results["schema"] == started["schema"], "Execution schema mismatch")
    require(len(summary["cases"]) == len(results["cases"]), "Summary/raw case count mismatch")
    require(results["binding"]["guard_sha256"] == started["guard_sha256"] and
            results["binding"]["expected_guard_record_sha256"] == started["expected_guard_record_sha256"],
            "Raw/STARTED guard binding mismatch")
    review = json.loads(source_bytes[science["record_review_path"]])
    require(review["status"] == science["expected_record_review_status"], "Record reader has not passed")
    for label in ("free_dependencies", "elliptic_dependencies", "local_dependencies", "old_dependencies"):
        require(results["binding"][label] == started[label] == review["binding"][label],
                "Execution/review dependency-map disagreement: " + label)
    require(started == {k:v for k,v in results["binding"].items() if k != "reused_interfaces"},
            "Complete STARTED binding mismatch")
    require(review["binding"] == results["binding"], "Complete review/raw binding mismatch")
    for name, expected in results["binding"]["local_dependencies"].items():
        require(name in source_bytes and sha256(source_bytes[name]) == expected,
                "Local executed proof omitted or changed: " + name)
    # Exact earlier readbacks bind published proof/source bytes; local prior
    # dependencies keep their narrower local binding, never an invented readback.
    archives = {}
    for label, archive in plan["external_source_archives"].items():
        archives[label] = json.loads(under(HERE.parent, archive).read_bytes())

    def observed_bytes(pin):
        require(re.fullmatch(r"[0-9a-f]{40}", pin["commit"]) is not None,
                "External ref is not an immutable commit")
        matches = [o for o in archives[pin["archive"]]
                   if o.get("arguments", {}).get("path") == pin["path"]
                   and o.get("arguments", {}).get("ref") == pin["commit"]]
        require(len(matches) == 1, "Missing or ambiguous actual external readback: " + pin["path"])
        observed = matches[0]
        answer = observed["result"]["structuredContent"]
        value = answer["content"].encode("utf-8")
        require(observed["tool_name"] == "github_fetch_file" and observed["observation_id"] and
                observed["arguments"]["repository_full_name"] == "awdawmip/enterprise-math" and
                not observed["result"].get("isError") and answer["encoding"] == "utf-8" and
                sha256(value) == pin["sha256"] and git_blob(value) == answer["sha"] and
                answer["display_url"] == "https://github.com/awdawmip/enterprise-math/blob/" + pin["commit"] + "/" + pin["path"],
                "External actual bytes/URL mismatch: " + pin["path"])
        return value

    external = plan["external_dependency_sources"]
    baseline_spec = plan["saved_baseline_evidence"]
    for group in ("free_dependencies", "elliptic_dependencies"):
        expected_names = set(results["binding"][group])
        if group == "free_dependencies":
            expected_names.remove(baseline_spec["dependency_name"])
        require(set(external[group]) == expected_names,
                "Unaccounted prior dependency: " + group)
        for name, pin in external[group].items():
            require(pin["sha256"] == results["binding"][group][name], "External dependency pin mismatch: " + name)
            observed_bytes(pin)
    old_local = plan["external_local_dependency_sources"]
    require(set(old_local) == set(results["binding"]["old_dependencies"]), "Unaccounted local prior dependency")
    for name, pin in old_local.items():
        require(pin["sha256"] == results["binding"]["old_dependencies"][name] and
                sha256(under(HERE.parent, pin["local_path"]).read_bytes()) == pin["sha256"],
                "Previously bound local interface changed: " + name)

    # Reconstruct the already-published old gzip from its actual immutable
    # manifest/chunk readbacks. This is data decoding, not baseline execution.
    old_manifest = json.loads(observed_bytes(baseline_spec["manifest_source"]))
    old_evidence = old_manifest["compressed_evidence"]
    chunk_specs = baseline_spec["chunk_sources_in_order"]
    require([p["relative_path"] for p in chunk_specs] == old_evidence["base64_chunks_in_order"],
            "Prior baseline chunk order mismatch")
    old_entries = {e["path"]:e for e in old_manifest["files"]}
    old_chunks = []
    for pin in chunk_specs:
        value = observed_bytes(pin)
        entry = old_entries[pin["relative_path"]]
        require(len(value) == entry["bytes"] and sha256(value) == entry["sha256"] and
                git_blob(value) == entry["git_blob_sha1"], "Prior baseline chunk manifest mismatch")
        old_chunks.append(value.strip())
    old_gzip = base64.b64decode(b"".join(old_chunks), validate=True)
    old_raw = gzip.decompress(old_gzip)
    require(sha256(old_gzip) == results["binding"]["free_dependencies"][baseline_spec["dependency_name"]],
            "Prior baseline gzip differs from actual execution binding")
    baseline = summary["saved_baseline_comparison"]
    require(results["saved_baseline_comparison"] == baseline, "Raw/summary baseline comparison mismatch")
    for label, value in (("raw", old_raw), ("gzip", old_gzip)):
        summary_label = "compressed" if label == "gzip" else label
        require(len(value) == old_evidence[label+"_bytes"] == baseline[summary_label+"_bytes"] and
                sha256(value) == old_evidence[label+"_sha256"] == baseline[summary_label+"_sha256"],
                "Published baseline evidence mismatch: " + label)
    require(baseline["new_scientific_execution_of_old_program"] is False and
            baseline["equal_output_end_to_end_ratio_claimed"] is False and
            baseline["unpaired_case_index"] == 3 and
            [m["case_index"] for m in baseline["matched"]] == [0,1,2] and
            all(m["common_outputs_equal"] for m in baseline["matched"]),
            "Saved baseline comparison scope differs from the frozen contract")
    for name, expected in plan["reviewed_symbolic_and_report_pins"].items():
        require(name in source_bytes and sha256(source_bytes[name]) == expected,
                "Reviewed final text changed: " + name)
    tool = json.loads(source_bytes["ACTUAL_EXECUTION_TOOL_RESULT.json"])
    require(tool["tool_name"] == "exec_command" and tool["arguments"] and
            tool["result"]["chunk_id"] == science["actual_tool_chunk_id"] and
            tool["result"]["exit_code"] == 0 and json.loads(tool["result"]["output"]) == summary,
            "Actual one-run tool receipt mismatch")
    require(review["actual_tool_chunk_id"] == science["actual_tool_chunk_id"] and
            review["actual_tool_receipt_sha256"] == sha256(source_bytes["ACTUAL_EXECUTION_TOOL_RESULT.json"]),
            "Saved-record review actual tool receipt mismatch")
    require(review["category_totals"] == summary["category_totals"], "Seven-category costs differ")
    require(review["reader_sha256"] == sha256(source_bytes[science["reader_path"]]) and
            review["summary_sha256"] == sha256(source_bytes[science["summary_path"]]),
            "Record review reader/summary binding mismatch")
    for label in ("raw_bytes", "raw_sha256", "gzip_bytes", "gzip_sha256"):
        require(review[label] == summary[label], "Record review evidence mismatch: " + label)
    for label in ("source", "plan"):
        require(review["source_pins"][label] == summary[label + "_sha256"],
                "Record review source binding mismatch: " + label)
    for label, value in summary["total_cost"].items():
        require(review["total_cost"][label] == value, "Record review cost mismatch: " + label)
    return final, source_bytes, compressed, raw, summary, started


def prepare():
    plan, plan_raw = load_plan()
    final, inputs, compressed, raw, summary, started = collect(plan, plan_raw)
    encoded = base64.b64encode(compressed).decode("ascii")
    chunks = {}
    step = plan["chunk_characters"]
    for index, offset in enumerate(range(0, len(encoded), step)):
        name = plan["science"]["compressed_path"] + ".part" + str(index) + ".b64"
        require(name not in inputs, "Chunk/source path collision")
        chunks[name] = (encoded[offset:offset + step] + "\n").encode("ascii")
    files = dict(inputs)
    files.update(chunks)
    manifest = {
        "schema": "ADJACENT_TRACE_EVIDENCE_MANIFEST_V1",
        "status": "FROZEN_LOCAL_BYTES_PUBLICATION_RECEIPT_SEPARATE",
        "scope": "Administrative immutable byte packaging; no scientific replay or remote publication",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "prior_science_commit": plan["prior_science_commit"],
        "remote_prefix": plan["remote_prefix"],
        "manifest_path": plan["manifest_path"],
        "files": [{"path": name, "bytes": len(value), "sha256": sha256(value),
                   "git_blob_sha1": git_blob(value)} for name, value in files.items()],
        "compressed_evidence": {
            "path": plan["science"]["compressed_path"],
            "gzip_bytes": len(compressed), "gzip_sha256": sha256(compressed),
            "raw_bytes": len(raw), "raw_sha256": sha256(raw),
            "base64_chunks_in_order": list(chunks),
        },
        "science_binding": {
            "status": summary["status"], "source_sha256": summary["source_sha256"],
            "plan_sha256": summary["plan_sha256"], "guard_sha256": started["guard_sha256"],
            "expected_guard_record_sha256": started["expected_guard_record_sha256"],
            "free_dependencies": started["free_dependencies"],
            "elliptic_dependencies": started["elliptic_dependencies"],
            "local_dependencies": started["local_dependencies"],
            "external_dependency_sources": plan["external_dependency_sources"],
            "saved_baseline_evidence": plan["saved_baseline_evidence"],
            "external_local_dependency_sources": plan["external_local_dependency_sources"],
            "external_prior_package_dependencies": started["old_dependencies"],
        },
        "excluded_external_material": plan["excluded"],
    }
    manifest_bytes = encode(manifest)
    # All mandatory input reads, JSON checks and output-byte calculations succeeded.
    lock = HERE / LOCK_NAME
    with lock.open("xb") as stream:
        stream.write(encode({"pid": os.getpid(), "target": str(final),
                             "manifest_sha256": sha256(manifest_bytes),
                             "state": "PREPARE_STARTED"}))
        stream.flush()
        os.fsync(stream.fileno())
    stage = None
    committed = False
    try:
        # Concurrent conforming runs stop at the exclusive lock. Windows rename
        # also refuses a pre-existing final directory; never merge or overwrite it.
        require(not os.path.lexists(final), "Publication appeared before staging")
        stage = Path(tempfile.mkdtemp(prefix=".adjacent-trace-publication-stage-", dir=HERE))
        for name, value in files.items():
            new_write(under(stage / "files", name), value)
        new_write(under(stage, plan["manifest_path"]), manifest_bytes)
        new_write(stage / SEAL_NAME, encode({
            "schema": "ADJACENT_TRACE_LOCAL_FREEZE_RECEIPT_V1",
            "manifest_path": plan["manifest_path"],
            "manifest_sha256": sha256(manifest_bytes),
            "manifest_git_blob_sha1": git_blob(manifest_bytes),
            "file_count_with_manifest": len(files) + 1,
        }))
        for name, value in inputs.items():
            require(under(HERE, name).read_bytes() == value, "Input changed while staging: " + name)
        require(under(HERE, plan["science"]["compressed_path"]).read_bytes() == compressed,
                "Compressed execution evidence changed while staging")
        for name, value in files.items():
            require(under(stage / "files", name).read_bytes() == value, "Staging readback mismatch: " + name)
        require(not os.path.lexists(final), "Publication appeared before final rename")
        os.rename(stage, final)
        committed = True
    except BaseException:
        # Preserve an incomplete administrative attempt for inspection. Never
        # erase or recreate scientific STARTED/evidence and never rerun science.
        print(json.dumps({"status": "ADMIN_PREPARE_FAILED",
                          "staging_directory": str(stage) if stage else None,
                          "lock": str(lock), "scientific_rerun_performed": False}), file=sys.stderr)
        raise
    finally:
        if committed:
            lock.unlink()
    print(json.dumps({"status": "FROZEN_LOCAL_BYTES", "directory": str(final),
                      "manifest": str(final / plan["manifest_path"]),
                      "manifest_sha256": sha256(manifest_bytes),
                      "file_count_with_manifest": len(files) + 1,
                      "science_rerun_performed": False, "remote_write_performed": False}))


def payloads():
    # The saved plan is inside the frozen package. Do not trust a mutable current
    # plan to select a different manifest or publication prefix after freeze.
    plan, _ = load_plan()
    final = under(HERE, plan["publication_directory"])
    seal = json.loads((final / SEAL_NAME).read_bytes())
    manifest_bytes = under(final, seal["manifest_path"]).read_bytes()
    require(sha256(manifest_bytes) == seal["manifest_sha256"] and
            git_blob(manifest_bytes) == seal["manifest_git_blob_sha1"], "Frozen manifest seal mismatch")
    manifest = json.loads(manifest_bytes)
    require(manifest["schema"] == "ADJACENT_TRACE_EVIDENCE_MANIFEST_V1", "Wrong manifest schema")
    entries = manifest["files"]
    require(len({entry["path"] for entry in entries}) == len(entries), "Duplicate frozen file")
    values = {}
    for entry in entries:
        name = entry["path"]
        value = under(final / "files", name).read_bytes()
        require(len(value) == entry["bytes"] and sha256(value) == entry["sha256"] and
                git_blob(value) == entry["git_blob_sha1"], "Frozen snapshot mismatch: " + name)
        value.decode("utf-8")
        values[name] = value
    frozen_plan = json.loads(values[PLAN_NAME])
    require(frozen_plan["publication_directory"] == plan["publication_directory"] and
            manifest["remote_prefix"] == frozen_plan["remote_prefix"] and
            manifest["manifest_path"] == frozen_plan["manifest_path"], "Frozen plan/manifest disagreement")
    evidence = manifest["compressed_evidence"]
    encoded = b"".join(values[name].strip() for name in evidence["base64_chunks_in_order"])
    compressed = base64.b64decode(encoded, validate=True)
    raw = gzip.decompress(compressed)
    for label, value in (("raw", raw), ("gzip", compressed)):
        require(len(value) == evidence[label + "_bytes"] and
                sha256(value) == evidence[label + "_sha256"], "Reconstructed " + label + " mismatch")
    require(len(entries) + 1 == seal["file_count_with_manifest"], "Frozen file count mismatch")
    prefix = manifest["remote_prefix"]
    values[manifest["manifest_path"]] = manifest_bytes
    # Root uses these exact path/content fields with the authorized GitHub connector.
    print(json.dumps([{"path": prefix + name, "content": value.decode("utf-8"),
                       "git_blob_sha1": git_blob(value)}
                      for name, value in values.items()], ensure_ascii=False))


def status():
    plan, _ = load_plan()
    names = plan["required_files"] + [plan["science"]["compressed_path"]]
    print(json.dumps({
        "status": "READ_ONLY_PLANNED_INPUT_INVENTORY",
        "existing": [name for name in names if under(HERE, name).is_file()],
        "missing": [name for name in names if not under(HERE, name).is_file()],
        "publication_exists": os.path.lexists(under(HERE, plan["publication_directory"])),
        "prepare_lock_exists": os.path.lexists(HERE / LOCK_NAME),
        "publication_ready": plan["publication_ready"],
        "pending_finalization": plan["pending_finalization"],
        "new_chunks_or_manifest_created": False,
        "review_pass_inferred": False,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("status", "prepare", "payloads"))
    arguments = parser.parse_args()
    {"status": status, "prepare": prepare, "payloads": payloads}[arguments.command]()

