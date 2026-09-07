#!/usr/bin/env python3
"""Replay only the two frozen owner tools in an isolated copy of this checkout.

This is a mathematical L4 candidate receipt, not a mainline admission or a
formal Result/Driver review. No original consumer evidence is overwritten.
The public source and historical shell baseline Git objects must be available
locally. No fetching, source repair, arithmetic implementation, or broad test
suite is performed here.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
SHARD = "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json"
NOTE = "research_notes/OWNER_NATIVE_TOOLS_L4_INTEGRATION_20260908.md"
SELF = "experiments/owner_native_tools_l4_20260908/validate_integration.py"
SHELL = "experiments/owner_shell_length_20260907"
ONE = "experiments/owner_one_positive_stability_20260908"
SHELL_REVIEW = SHELL + "/brc_runtime_independent_20260908"
ONE_REVIEW = ONE + "/independent_review_20260908"
POLICY_PATHS = [
    SHELL + "/shell_length.py",
    SHELL + "/validate_brc_runtime.py",
    SHELL_REVIEW + "/review.py",
    ONE + "/check_one_positive_stability.py",
    ONE_REVIEW + "/review.py",
    SELF,
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def literal_mapping(path, name):
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError("missing literal mapping: " + name)


def frozen_map(paths):
    return {relative: digest(ROOT.joinpath(relative).read_bytes()) for relative in sorted(paths)}


def verify_inputs(shard):
    provenance = shard["provenance"]
    expected = provenance["selected_method_ids"]
    methods = shard["methods"]
    require(len(expected) == 2 and len(set(expected)) == 2, "two distinct selected method IDs required")
    require([method["method_id"] for method in methods] == expected, "selected method set/order drift")
    require(shard["availability"]["available_selected_method_ids"] == expected, "availability scope drift")
    require(provenance["integration_channel"] == "MATHEMATICAL_L4", "wrong integration channel")
    source = provenance["published_source_commit"]
    require(git("rev-parse", source + "^{tree}").decode().strip() == provenance["source_tree"],
            "public source tree mismatch; obtain the exact public object if absent")
    original_bytes = git("show", source + ":" + provenance["source_shard_path"])
    require(digest(original_bytes) == provenance["source_shard_sha256"], "public source shard drift")
    original_methods = json.loads(original_bytes)["methods"]
    selected = [method for method in original_methods if method["method_id"] in expected]
    require(methods == selected, "selected method objects differ from immutable source")
    pins = provenance["frozen_source_files_sha256"]
    require(len(pins) == 20 and frozen_map(pins) == pins, "twenty frozen source files drifted")
    for relative, expected_hash in pins.items():
        require(digest(git("show", source + ":" + relative)) == expected_hash,
                "copied file differs from immutable source: " + relative)
    refs = set()
    for method in methods:
        refs.update(method["source_refs"] + method["validation_refs"])
        for relative, expected_hash in method["source_sha256"].items():
            require(pins.get(relative) == expected_hash, "method source pin not in frozen closure: " + relative)
    require(refs <= set(pins), "method references leave the declared closure")
    native = literal_mapping(ROOT.joinpath(ONE, "check_one_positive_stability.py"), "SOURCE_SHA256")
    require(frozen_map(native) == native, "one-positive twelve-source dependency drift")
    shell_evidence = read_json(ROOT.joinpath(SHELL, "validate_brc_runtime.json"))
    shell_native = shell_evidence["source_dependencies"]
    require(frozen_map(shell_native) == shell_native, "shell native dependencies drifted")
    baseline = provenance["legacy_shell_review_baseline_commit"]
    require(git("rev-parse", baseline + "^{tree}").decode().strip()
            == provenance["legacy_shell_review_baseline_tree"], "historical baseline object/tree mismatch")
    return pins, native, shell_native, sorted(refs)


API_CHECK = r'''
import importlib, inspect, json, sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root.joinpath("tools")))
import enterprise_toolbox as toolbox
shard = json.loads(root.joinpath("research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json").read_text(encoding="utf-8"))
inventory = toolbox.load_method_inventory()
expected = shard["provenance"]["selected_method_ids"]
assert len(expected) == 2 and {m["method_id"] for m in shard["methods"]} == set(expected)
rows = []
for method in shard["methods"]:
    selected = [m for m in inventory["methods"] if m["method_id"] == method["method_id"]]
    assert selected == [method], "loaded method absent, duplicated or changed"
    hits = toolbox.method_suggestions(method["triggers"][0], inventory=inventory)
    assert method["method_id"] in {m["method_id"] for m in hits}, "preferred query misses selected method"
    module_path = next(root.joinpath(p) for p in method["source_refs"] if p.endswith(".py"))
    sys.path.insert(0, str(module_path.parent))
    module = importlib.import_module(module_path.stem)
    assert Path(module.__file__).resolve() == module_path.resolve()
    apis = {}
    for name in method["api"]:
        value = getattr(module, name)
        assert callable(value), name
        apis[name] = str(inspect.signature(value))
    rows.append({"method_id": method["method_id"], "loaded_exactly_once": True,
                 "query": method["triggers"][0], "query_hit": True,
                 "api_signatures": apis})
print(json.dumps({"status": "PASS_TWO_SELECTED_METHODS", "methods": rows,
                  "global_inventory_count_is_not_an_assertion": True}, ensure_ascii=False))
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-commit", help="explicit current-main base for this replay; defaults to the recorded preparation base")
    parser.add_argument("--receipt", type=Path, default=ROOT.joinpath("experiments/owner_native_tools_l4_20260908/receipt.json"))
    args = parser.parse_args()
    require(__debug__, "consumer assertions require normal Python, not -O")
    shard = read_json(ROOT.joinpath(SHARD))
    pins, native, shell_native, refs = verify_inputs(shard)
    base = args.base_commit or shard["provenance"]["observed_main_commit"]
    subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", base, "HEAD"], check=True)
    head = git("rev-parse", "HEAD").decode().strip()
    base_tree = git("rev-parse", base + "^{tree}").decode().strip()
    # The canonical package __init__ imports historical modules. Preserve its
    # actual package and type identity; do not construct a private replacement.
    package_paths = git("ls-files", "-z", "--", "src").decode().split("\0")
    package_paths = [path for path in package_paths if path]
    input_paths = set(pins) | set(native) | set(shell_native) | set(package_paths)
    input_paths.update([SHARD, SELF, NOTE, "tools/enterprise_toolbox.py",
                        "enterprise_toolbox_registry.json", "research_method_inventory.json"])
    input_paths.update(str(path.relative_to(ROOT)).replace("\\", "/")
                       for path in ROOT.joinpath("research_method_inventory_addenda").glob("*.json"))
    require(args.receipt.resolve() not in {ROOT.joinpath(path).resolve() for path in input_paths},
            "receipt output must not overwrite an input or frozen source artifact")
    owned = set(pins) | {SHARD, SELF, NOTE, "experiments/owner_native_tools_l4_20260908/receipt.json"}
    tracked_changes = set(git("diff", "--name-only", "HEAD").decode().splitlines())
    require(tracked_changes <= owned, "unrelated tracked changes are outside this candidate replay")
    before = frozen_map(input_paths)
    temporary = Path(tempfile.mkdtemp(prefix="owner-native-tools-l4-20260908-"))
    replay = temporary.joinpath("candidate")
    replay.mkdir()
    for relative in sorted(input_paths):
        target = replay.joinpath(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT.joinpath(relative), target)
    require({relative: digest(replay.joinpath(relative).read_bytes()) for relative in before} == before,
            "isolated copy differs from candidate")
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONUTF8"] = "1"
    environment["GIT_DIR"] = git("rev-parse", "--absolute-git-dir").decode().strip()
    environment["GIT_WORK_TREE"] = str(replay)
    commands = []

    def run(label, arguments):
        argv = [sys.executable, "-X", "utf8", "-B", *arguments]
        start = time.perf_counter_ns()
        result = subprocess.run(argv, cwd=replay, env=environment, capture_output=True, timeout=180)
        log = temporary.joinpath(label + ".log")
        log.write_bytes(result.stdout + result.stderr)
        item = {"label": label, "argv": argv, "cwd": str(replay), "exit_code": result.returncode,
                "elapsed_nanoseconds": time.perf_counter_ns() - start,
                "log_path": str(log), "log_sha256": digest(log.read_bytes())}
        commands.append(item)
        require(result.returncode == 0, label + " failed; see " + str(log))
        return result.stdout

    receipt = {"schema": "OWNER_NATIVE_TOOLS_LOCAL_L4_REPLAY_V1", "status": "STARTED",
               "channel": "MATHEMATICAL_L4", "created_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version.split()[0], "actual_checkout_head": head,
               "replay_base_commit": base, "replay_base_tree": base_tree,
               "published_source_commit": shard["provenance"]["published_source_commit"],
               "source_tree": shard["provenance"]["source_tree"],
               "selected_method_ids": shard["provenance"]["selected_method_ids"],
               "selected_ref_count": len(refs), "selected_api_count": sum(len(m["api"]) for m in shard["methods"]),
               "original_source_sha256": pins, "one_positive_source_sha256": native,
               "shell_native_source_sha256": shell_native,
               "candidate_input_sha256": before, "temporary_evidence_directory": str(temporary),
               "commands": commands, "final_main_admission": "NOT_PERFORMED",
               "formal_result_review_or_foundation_mutation": False,
               "historical_git_access": "Read-only Git show/rev-parse through this checkout's shared object store; no fetching or history mutation.",
               "scope": "Two unchanged source methods on the explicitly recorded base; current-main changes require a new actual combination assessment.",
               "arithmetic_limit": "Selected static gates and finite runtime observations do not establish transitive arithmetic migration. Legacy noninteger probes and canonical package initialization remain explicitly typed historical dependencies."}
    try:
        receipt["loader_and_api"] = json.loads(run("two-entry-loader-api", ["-c", API_CHECK, str(replay)]))
        run("static-v2-selected-six", ["tools/check_exact_arithmetic_policy.py", *POLICY_PATHS])
        run("shell-consumer", [SHELL + "/validate_brc_runtime.py"])
        shell_run = read_json(replay.joinpath(SHELL, "validate_brc_runtime.json"))
        require(replay.joinpath(SHELL, "validate_brc_runtime.json").read_bytes()
                == ROOT.joinpath(SHELL, "validate_brc_runtime.json").read_bytes(), "shell stored evidence replay differs")
        receipt["shell_consumer"] = {"selected_cases": shell_run["selected_case_count"],
                                     "verified_traces": shell_run["trace_count_verified"],
                                     "original_json_byte_equal": True}
        run("shell-independent", [SHELL_REVIEW + "/review.py", str(replay)])
        run("one-positive-consumer", [ONE + "/check_one_positive_stability.py"])
        run("one-positive-independent", [ONE_REVIEW + "/review.py", str(replay)])
        receipt["replayed_artifacts"] = {}
        for relative in [SHELL + "/validate_brc_runtime.json", SHELL_REVIEW + "/review.json",
                         ONE + "/certificate.json", ONE_REVIEW + "/review.json"]:
            data = replay.joinpath(relative).read_bytes()
            receipt["replayed_artifacts"][relative] = {"path": str(replay.joinpath(relative)),
                                                       "sha256": digest(data), "status": json.loads(data).get("status")}
        receipt["status"] = "PASS_LOCAL_TWO_TOOL_L4_CANDIDATE_REPLAY"
    except Exception as error:
        receipt["status"] = "FAIL_LOCAL_CANDIDATE_REPLAY"
        receipt["error"] = str(error)
        raise
    finally:
        after = frozen_map(input_paths)
        receipt["all_candidate_input_bytes_unchanged"] = after == before
        receipt["all_twenty_original_files_unchanged"] = frozen_map(pins) == pins
        receipt["checkout_head_unchanged"] = git("rev-parse", "HEAD").decode().strip() == head
        if (after != before or not receipt["checkout_head_unchanged"]
                or not receipt["all_twenty_original_files_unchanged"]):
            receipt["status"] = "FAIL_CANDIDATE_CHANGED_DURING_REPLAY"
        receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_bytes(json_bytes(receipt))
    require(receipt["status"] == "PASS_LOCAL_TWO_TOOL_L4_CANDIDATE_REPLAY", receipt["status"])
    print(json.dumps({"status": receipt["status"], "base": base, "methods": len(shard["methods"]),
                      "source_files": len(pins), "api_count": receipt["selected_api_count"],
                      "receipt": str(args.receipt), "receipt_sha256": digest(args.receipt.read_bytes()),
                      "temporary_evidence_directory": str(temporary)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
