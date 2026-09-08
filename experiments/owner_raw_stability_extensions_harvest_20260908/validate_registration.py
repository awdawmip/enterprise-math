"""Mathematical L4 transport driver with the source registration check preserved.

The validate() function is copied verbatim. The main adapter runs the bounded
registration/API, fresh compression-review replay and selected static checks.
Original source evidence is never overwritten; the replay copy writes to TEMP.
"""

from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import importlib
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys
import time


SHARD = "research_method_inventory_addenda/20260908_owner_raw_stability_extensions.json"
PREFIX = "experiments/owner_positive_support_compression_20260908/"
COMPRESS = "candidate.x6.positive_support_raw_compression_certificate"
EQUALITY = "result.x6.two_positive_equality_rectangle"
MASS = "result.x6.three_positive_raw_mass_boundary"
PAPER_EQUALITY = "research_notes/OWNER_TWO_POSITIVE_EQUALITY_CLASSIFICATION_REVIEW_20260908.md"
PAPER_MASS = "research_notes/OWNER_THREE_POSITIVE_RAW_STABILITY_PROBE_20260908.md"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_pinned(root, pins):
    data = {path: (root / path).read_bytes() for path in pins}
    require({path: digest(value) for path, value in data.items()} == pins, "source pin mismatch")
    return data


def validate(root):
    shard_bytes = (root / SHARD).read_bytes()
    shard = json.loads(shard_bytes)
    require(shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1", "schema")
    require(shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE", "candidate shard status")
    provenance = shard["provenance"]
    require(provenance["published_source_commit"] == "c0495fd71a557ed78eef7ab62a8b2bf08feee535", "published source")
    require(provenance["published_source_tree"] == "738656dd4d2c1f9a5d5f1175b151be7ed83f2772", "source tree")
    require(provenance["formal_driver_or_steward_acceptance"] is None
            and provenance["official_claim"] is None, "formal authority absent")
    require(provenance["foundation_mutation"] is False and provenance["new_global_tool_family"] is False,
            "no Foundation or family mutation")
    require(shard["availability"]["formal_acceptance_inferred_from_indexing"] is False, "index authority")
    rows = shard["methods"]
    require(len(rows) == 3 and {m["method_id"] for m in rows} == {COMPRESS, EQUALITY, MASS}, "three exact unique IDs")
    by_id = {row["method_id"]: row for row in rows}
    pins = {}
    for row in rows:
        require(row["family_id"] is None and row["formal_acceptance"] is None, "candidate has no formal family acceptance")
        require(row["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
                and row["owner_review_status"] == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT", "entry status")
        require(row["reuse_resolution"]["reuse_resolution_state"] == "EXTEND_EXISTING_TOOL", "reuse scope")
        scope = row["result_scope"]
        require(scope["post_jordan_positive_support"] is True and scope["same_anchor_labelled_signed_x6"] is True,
                "shared raw/Jordan contract")
        require(set(row["source_sha256"]) == set(row["source_refs"] + row["validation_refs"]), "exact source/evidence closure")
        for path, pin in row["source_sha256"].items():
            require(path not in pins or pins[path] == pin, "inconsistent shared pin")
            pins[path] = pin
    require(len(pins) == 9, "six-file consumer/review package and three papers")
    source_data = read_pinned(root, pins)
    comp = by_id[COMPRESS]
    require(comp["classification"] == "DOMAIN_OPERATOR" and comp["api"] == ["audit_compression"], "single public API")
    require(comp["api_binding"] == {"module_path": PREFIX + "check_positive_support_compression.py",
            "callable": "audit_compression", "signature": "(case_id, mu_atoms, nu_atoms, denominator=1)"}, "exact API binding")
    scope = comp["result_scope"]
    require(scope["generic_finite_positive_support"] is True and scope["raw_table_count_per_case"] == 20, "generic p/all20")
    for key in ("all_coordinate_subsets_executed", "carrier_enumerated", "carrier_bound_is_actual_support_count",
                "zero_ratio_defined", "arbitrary_low_level_pushforward_norm_guarantee", "recovers_microscopic_brc",
                "new_two_positive_sharp_bound_checker"):
        require(scope[key] is False, key)
    require(scope["p_zero_handled_separately"] is True and scope["retains_symbolic_div_mass_unit"] is True, "zero and DIV scope")
    for mid, paper in ((EQUALITY, PAPER_EQUALITY), (MASS, PAPER_MASS)):
        row = by_id[mid]
        require(row["classification"] == "RESULT_ONLY" and row["api"] == [] and "api_binding" not in row, "paper-only API")
        require(row["source_refs"] == row["validation_refs"] == [paper], "one actual paper source")
        require(row["result_scope"]["all_twenty_complete_raw_three_axis_norms"] is True, "all20 norm definition")
        require(row["result_scope"]["executable_theorem_certificate"] is False, "no executable paper proof")
    eq = by_id[EQUALITY]["result_scope"]
    require(eq["maximum_positive_support"] == 2 and eq["nonzero_required"] is True
            and eq["norm_equality_condition"] == "D=4*M" and eq["iff_original_coordinate_equal_weight_rectangle"] is True
            and eq["equal_total_mass_forced"] is True, "exact equality scope")
    require(all(eq[key] is False for key in ("unit_axis_spacing_required", "zero_difference_classified", "extends_to_p_ge_3")), "equality exclusions")
    mass = by_id[MASS]["result_scope"]
    require([mass[key] for key in ("example_positive_support", "example_total_support", "example_P", "example_N", "example_M", "example_D")]
            == [3, 7, 3, 4, 7, 26], "seven-point witness fields")
    require((mass["arbitrary_mass_lower_bound_numerator"], mass["arbitrary_mass_lower_bound_denominator"]) == (7, 26), "lower bound only")
    require(mass["equal_mass_bound_only_for_specified_symmetric_family"] is True
            and mass["equal_mass_family_equality"] == "c=0; 1/2<=b<=2/3; a=3-3*b; M=6; D=24", "restricted family equality")
    require(all(mass[key] is False for key in ("sharp_or_global_upper_bound_claimed", "all_equal_mass_p3_upper_bound_claimed",
                                             "arbitrary_mass_family_optimized")), "no global p3 upper bound")

    runtime = comp["runtime_dependency_manifest"]
    require(runtime == {"path": PREFIX + "certificate.json", "field": "source_sha256", "count": 14,
                        "all_transitive_arithmetic_compliance_claimed": False}, "runtime pin manifest scope")
    author = json.loads(source_data[runtime["path"]])
    runtime_pins = author[runtime["field"]]
    require(len(runtime_pins) == 14, "fourteen runtime dependencies")
    runtime_data = read_pinned(root, runtime_pins)
    independent = json.loads(source_data[PREFIX + "independent_review_20260908/review.json"])
    require(author["status"] == "PASS" and len(author["cases"]) == 18
            and sum(len(case["raw_tables"]) for case in author["cases"]) == 360, "historical author evidence")
    require(independent["status"] == "PASS_BOUNDED_CONSUMER_REVIEW_NO_FORMAL_ACCEPTANCE"
            and len(independent["independent_cases"]) == 5 and independent["independent_raw_tables"] == 100
            and len(independent["independent_rejections"]) == 3, "historical independent evidence")
    require(author["checker_sha256"] == pins[PREFIX + "check_positive_support_compression.py"]
            and independent["executed_script_sha256"] == pins[PREFIX + "independent_review_20260908/review.py"], "executed-source binding")

    prior_paths = provenance["protected_prior_shards"]
    require(prior_paths == ["research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json",
                           "research_method_inventory_addenda/20260908_owner_raw_stability_results.json"], "two prior shards")
    prior_bytes = {path: (root / path).read_bytes() for path in prior_paths}
    prior_objects = {path: json.loads(data)["methods"] for path, data in prior_bytes.items()}
    sys.path.insert(0, str(root / "tools"))
    import enterprise_toolbox as toolbox
    require(Path(toolbox.__file__).resolve() == (root / "tools/enterprise_toolbox.py").resolve(), "canonical loader")
    inventory = toolbox.load_method_inventory()
    query_checks = []
    for row in rows:
        require([m for m in inventory["methods"] if m["method_id"] == row["method_id"]] == [row], "unique exact loaded row")
        require(len(row["triggers"]) == 2 and row["triggers"][0].isascii()
                and any("\u4e00" <= char <= "\u9fff" for char in row["triggers"][1]), "English and Chinese triggers")
        for language, query in zip(("en", "zh-CN"), row["triggers"]):
            hits = toolbox.method_suggestions(query, inventory=inventory)
            require(row["method_id"] in {m["method_id"] for m in hits}, "query miss")
            query_checks.append({"method_id": row["method_id"], "language": language, "query": query, "hit": True})
    for objects in prior_objects.values():
        for row in objects:
            require([m for m in inventory["methods"] if m["method_id"] == row["method_id"]] == [row], "prior object changed")

    sys.path.insert(0, str(root / PREFIX))
    module = importlib.import_module("check_positive_support_compression")
    module_path = root / comp["api_binding"]["module_path"]
    require(Path(module.__file__).resolve() == module_path.resolve(), "canonical API module")
    api = getattr(module, "audit_compression")
    require(callable(api) and inspect.isfunction(api), "real callable API")
    require(Path(api.__code__.co_filename).resolve() == module_path.resolve(), "API code origin")
    require(str(inspect.signature(api)) == comp["api_binding"]["signature"], "exact callable signature")
    require(module.SOURCE_SHA256 == runtime_pins, "effective API runtime pins")
    # Inspection ends here: audit_compression, build_certificate and old consumers are never called.
    for path, data in {**source_data, **runtime_data, **prior_bytes, SHARD: shard_bytes}.items():
        require((root / path).read_bytes() == data, "input file changed during metadata validation")
    return {
        "schema": "OWNER_RAW_STABILITY_EXTENSIONS_REGISTRATION_VALIDATION_V1",
        "status": "PASS_THREE_CANDIDATE_REGISTRATIONS",
        "created_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0], "argv": sys.argv,
        "executed_script_sha256": digest(Path(__file__).read_bytes()), "shard_sha256": digest(shard_bytes),
        "published_evidence_source_commit": provenance["published_source_commit"],
        "canonical_loader_sha256": digest(Path(toolbox.__file__).read_bytes()),
        "method_ids_unique": [row["method_id"] for row in rows], "queries": query_checks,
        "source_sha256": pins, "source_files_unchanged": True, "runtime_dependency_sha256": runtime_pins,
        "runtime_dependency_count": len(runtime_pins), "runtime_dependencies_unchanged": True,
        "api_inspection": {"method_id": COMPRESS, "module_path": comp["api_binding"]["module_path"],
                           "callable": "audit_compression", "signature": str(inspect.signature(api)),
                           "exact_code_origin": True, "mathematical_api_invocations": 0},
        "protected_previous_shards": [{"path": path, "sha256_before_and_after": digest(data),
            "observed_method_count": len(prior_objects[path]), "all_objects_and_file_bytes_unchanged": True,
            "observed_count_is_not_a_permanent_main_assertion": True} for path, data in prior_bytes.items()],
        "historical_consumer_evidence_read_not_reexecuted": True,
        "mathematical_consumers_executed": False, "formal_acceptance_or_family_created": False,
        "registration_authoring_global_knowledge_sync": "main@eb09a0a / GLOBAL_KNOWLEDGE_V1",
    }


BASE = "0242e5ccbc6b134241f083e6204de2bd47393e78"
BASE_TREE = "1f3f3a5bc7c4a2b64c273a99bdac4bc1f8bfd926"
SELF = "experiments/owner_raw_stability_extensions_harvest_20260908/validate_registration.py"
RECEIPT = "experiments/owner_raw_stability_extensions_harvest_20260908/validation.json"
NOTE = "research_notes/OWNER_RAW_STABILITY_EXTENSIONS_L4_INTEGRATION_20260908.md"
OLD_L4 = "experiments/owner_native_tools_l4_20260908/validate_integration.py"
VALIDATE_BODY_SHA256 = "b45892f3ec1716583f529ea8a1379baa028ece469684514c24d464d90f6d3a13"
ORIGINAL_SOURCES = [PREFIX + p for p in (
    "check_positive_support_compression.py", "certificate.json", "README.md",
    "independent_review_20260908/review.py", "independent_review_20260908/review.json",
    "independent_review_20260908/REVIEW.md")] + [PAPER_EQUALITY, PAPER_MASS]
INPUTS = ORIGINAL_SOURCES + [SHARD, SELF, NOTE]


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def tree_entries(root, ref):
    result = {}
    for record in git(root, "ls-tree", "-r", "-z", ref).split(b"\0"):
        if record:
            metadata, path = record.split(b"\t", 1)
            mode, kind, blob = metadata.decode().split()
            result[path.decode("utf-8")] = {"mode": mode, "type": kind, "blob": blob}
    return result


def verify_checkout_bytes(root, entries):
    result = {}
    for path, entry in entries.items():
        require(entry["type"] == "blob", "unsupported non-blob checkout input: " + path)
        data = (root / path).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        require(actual == entry["blob"], "working bytes differ from committed blob: " + path)
        result[path] = {**entry, "sha256": digest(data), "bytes": len(data)}
    return result


def write_json(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--registration-only", action="store_true", help="metadata child phase; no consumer calls")
    parser.add_argument("--output", type=Path, help="fresh TEMP JSON for the metadata child phase")
    parser.add_argument("--evidence-dir", type=Path, help="new directory for logs and the independent replay copy")
    parser.add_argument("--global-read-sha", help="caller's actual current GLOBAL_KNOWLEDGE_V1 read snapshot")
    args = parser.parse_args()
    root = args.repo.resolve()
    require(__debug__, "normal Python assertions required")
    require(digest(inspect.getsource(validate).encode("utf-8")) == VALIDATE_BODY_SHA256,
            "the source validate() function body changed")
    if args.registration_only:
        require(args.output is not None and not args.output.exists(), "choose a new TEMP metadata output")
        report = validate(root)
        require([row["observed_method_count"] for row in report["protected_previous_shards"]] == [2, 2],
                "this main composition requires the preserved two-tools and two-results shards")
        report["main_execution"] = {"head": git(root, "rev-parse", "HEAD").decode().strip(),
            "tree": git(root, "rev-parse", "HEAD^{tree}").decode().strip(),
            "global_read_sha_supplied_by_caller": args.global_read_sha,
            "source_validate_function_sha256": VALIDATE_BODY_SHA256}
        write_json(args.output, report)
        print(json.dumps({"status": report["status"], "methods": 3, "queries": len(report["queries"]),
                          "runtime_pins": 14, "prior_method_counts": [2, 2]}))
        return
    require(args.evidence_dir is not None, "choose a fresh --evidence-dir")
    evidence = args.evidence_dir.resolve()
    require(not evidence.exists(), "evidence directory must be new")
    require(not evidence.is_relative_to(root), "execution evidence must be outside the committed checkout")
    evidence.mkdir(parents=True)
    head = git(root, "rev-parse", "HEAD").decode().strip()
    head_tree = git(root, "rev-parse", "HEAD^{tree}").decode().strip()
    baseline, current = tree_entries(root, BASE), tree_entries(root, head)
    require(git(root, "rev-parse", BASE + "^{tree}").decode().strip() == BASE_TREE, "base tree")
    require(all(current.get(path) == entry for path, entry in baseline.items()), "baseline entry changed")
    added = set(current) - set(baseline)
    require(added in (set(INPUTS), set(INPUTS + [RECEIPT])), "exact eleven inputs plus optional owned receipt required")
    committed_inputs = {path: entry for path, entry in current.items() if path != RECEIPT}
    before = verify_checkout_bytes(root, committed_inputs)
    environment = os.environ.copy()
    for key in ("PYTHONPATH", "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        environment.pop(key, None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONUTF8"] = "1"
    commands = []

    def run(label, arguments):
        argv = [sys.executable, "-B", "-X", "utf8", *arguments]
        started = time.perf_counter_ns()
        result = subprocess.run(argv, cwd=root, env=environment, capture_output=True, timeout=60, check=False)
        stdout_path, stderr_path = evidence / (label + ".stdout.log"), evidence / (label + ".stderr.log")
        stdout_path.write_bytes(result.stdout)
        stderr_path.write_bytes(result.stderr)
        commands.append({"label": label, "argv": argv, "cwd": str(root), "input_head": head,
            "input_tree": head_tree, "exit_code": result.returncode, "elapsed_ns": time.perf_counter_ns() - started,
            "stdout_path": str(stdout_path), "stdout_sha256": digest(result.stdout),
            "stderr_path": str(stderr_path), "stderr_sha256": digest(result.stderr)})
        require(result.returncode == 0, label + " failed: " + result.stderr.decode("utf-8", "replace"))
        return result.stdout

    receipt = {"schema": "OWNER_RAW_STABILITY_EXTENSIONS_MAIN_L4_EXECUTION_V1", "status": "STARTED",
        "channel": "MATHEMATICAL_L4", "scope": "NO_NEW_MATHEMATICS_SOURCE_TRANSPORT",
        "created_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0],
        "driver_argv": [sys.executable, "-B", "-X", "utf8", *sys.argv],
        "executed_script_sha256": digest(Path(__file__).read_bytes()),
        "actual_input_head": head, "actual_input_tree": head_tree, "base_commit": BASE, "base_tree": BASE_TREE,
        "published_source_commit": "f67c8d991cb8781f03285925a30cfefee743d3c9",
        "published_source_tree": "f1d40c9c6d5e7e7338d023caec1a1cb65a3fc592",
        "source_validate_function_sha256": VALIDATE_BODY_SHA256,
        "source_registration_script_sha256": "8c9de986eb9378cb4c76c8a69683788e2f81ad492edbcaa5a0d6e361902a9a95",
        "source_validate_function_body_preserved_verbatim": True,
        "main_execution_global_read_sha_supplied_by_caller": args.global_read_sha,
        "candidate_input_files": {path: before[path] for path in INPUTS},
        "temporary_evidence_directory": str(evidence), "commands": commands,
        "remote_actions_performed": False, "main_admission_performed": False,
        "formal_task_result_review_or_foundation_change": False,
        "historical_source_receipt_url": "https://github.com/awdawmip/enterprise-math/blob/f67c8d991cb8781f03285925a30cfefee743d3c9/experiments/owner_raw_stability_extensions_harvest_20260908/validation.json"}
    receipt["prior_failed_local_preparation_and_source_revision"] = {'prior_local_input_head': '6b35ff4546ed090ffbd0731f765f6fbbdc6f44c4', 'prior_local_input_tree': '0183bf57ab11847733883a51005121df2acfe4c0', 'prior_result': 'FAIL_LOCAL_L4_COMPOSITION', 'failed_execution_sha256': 'b99f20d78e5a18c9cbe15a0ef4691dffee3d3d70eeabcb57ed6fa10977161b4c', 'input_preservation_evidence_sha256': 'a3202375d50d5f6f22356d4595421cda8d01b881ccb9826d6e81096f28334b4e', 'exact_failure': "Five pathlib Path '/' expressions were rejected by the unchanged AST arithmetic policy; registration, old API and independent replay phases passed on that earlier input.", 'source_revision': 'Exactly five Path joins use equivalent joinpath calls; source independent receipt and note are freshly regenerated, and corresponding catalog pins updated.', 'revised_source_review_script_sha256': 'd49d91d6686b68790cbad7966d1db2421b4ef2533f5de9e6b5c18d2dee3258a9', 'revised_source_review_receipt_sha256': '2b69f5e837c8067bb266931e438b4207e394aff16f0f40c56d4d759dddeb844a', 'old_source_registration_receipt_url': 'https://github.com/awdawmip/enterprise-math/blob/ad2798bcc9d6f5b3c57bbd0fd292015f67390583/experiments/owner_raw_stability_extensions_harvest_20260908/validation.json', 'previous_failure_reclassified_as_pass': False, 'local_historical_evidence_is_not_a_runtime_dependency': True}
    try:
        registration_path = evidence / "registration.json"
        registration_args = [SELF, str(root), "--registration-only", "--output", str(registration_path)]
        if args.global_read_sha:
            registration_args += ["--global-read-sha", args.global_read_sha]
        run("registration-and-six-queries", registration_args)
        receipt["registration"] = json.loads(registration_path.read_bytes())
        receipt["registration_artifact"] = {"path": str(registration_path), "sha256": digest(registration_path.read_bytes())}
        old_source = (root / OLD_L4).read_text(encoding="utf-8")
        old_api = next(ast.literal_eval(node.value) for node in ast.parse(old_source).body
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "API_CHECK" for t in node.targets))
        old_output = json.loads(run("unchanged-old-l4-api-check", ["-c", old_api, str(root)]))
        require(old_output["status"] == "PASS_TWO_SELECTED_METHODS"
                and len(old_output["methods"]) == 2
                and sum(len(row["api_signatures"]) for row in old_output["methods"]) == 7, "old seven API compatibility")
        receipt["old_l4_api_check"] = {"source_path": OLD_L4, "source_sha256": digest((root / OLD_L4).read_bytes()),
            "original_api_check_string_sha256": digest(old_api.encode("utf-8")), "original_string_executed_unchanged": True,
            "result": old_output, "old_mathematical_consumers_executed": False}
        replay_dir = evidence / "independent-replay"
        replay_dir.mkdir()
        original_review = root / (PREFIX + "independent_review_20260908/review.py")
        replay_script = replay_dir / "review.py"
        replay_script.write_bytes(original_review.read_bytes())
        require(replay_script.read_bytes() == original_review.read_bytes(), "review copy bytes")
        run("fresh-compression-independent-review", [str(replay_script), str(root)])
        replay_path = replay_dir / "review.json"
        replay = json.loads(replay_path.read_bytes())
        require(replay["status"] == "PASS_BOUNDED_CONSUMER_REVIEW_NO_FORMAL_ACCEPTANCE"
                and len(replay["independent_cases"]) == 5 and replay["independent_raw_tables"] == 100,
                "independent replay summary")
        receipt["new_main_independent_replay"] = {"path": str(replay_path), "sha256": digest(replay_path.read_bytes()),
            "copied_script_sha256": digest(replay_script.read_bytes()), "original_main_review_json_overwritten": False,
            "author_default_replay_cases": 18, "author_default_raw_tables": 360,
            "independent_cases": replay["independent_cases"], "independent_rejections": replay["independent_rejections"],
            "independent_observed_calls_by_exact_code_object": replay["independent_observed_calls_by_exact_code_object"],
            "all_seventeen_protected_file_bytes_and_mtimes_unchanged": replay["all_seventeen_protected_file_bytes_and_mtimes_unchanged"]}
        run("selected-two-mathematical-python-arithmetic", ["tools/check_exact_arithmetic_policy.py",
            PREFIX + "check_positive_support_compression.py", PREFIX + "independent_review_20260908/review.py"])
        after = verify_checkout_bytes(root, committed_inputs)
        require(before == after and git(root, "rev-parse", "HEAD").decode().strip() == head, "input changed during execution")
        proof_path = evidence / "baseline-byte-proof.json"
        write_json(proof_path, {"base": BASE, "base_tree": BASE_TREE, "actual_input_head": head,
            "actual_input_tree": head_tree, "all_baseline_entries_and_actual_bytes_unchanged": True,
            "entry_count": len(baseline), "entries": {path: before[path] for path in baseline}})
        receipt["baseline_protection"] = {"entry_count": len(baseline), "mode_type_blob_and_actual_bytes_unchanged": True,
            "proof_path": str(proof_path), "proof_sha256": digest(proof_path.read_bytes())}
        receipt["all_eleven_input_files_and_current_head_unchanged"] = True
        receipt["arithmetic_scope"] = "Selected static files and finite observed runtime paths only; no import-time or unexecuted transitive compliance claim."
        receipt["status"] = "PASS_LOCAL_THREE_EXTENSION_MATHEMATICAL_L4_COMPOSITION"
    except Exception as error:
        receipt["status"] = "FAIL_LOCAL_L4_COMPOSITION"
        receipt["error"] = str(error)
        write_json(evidence / "failed-execution.json", receipt)
        raise
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    target = root / RECEIPT
    write_json(target, receipt)
    print(json.dumps({"status": receipt["status"], "input_head": head, "input_tree": head_tree,
        "baseline_entries_preserved": len(baseline), "commands": len(commands), "receipt": str(target),
        "receipt_sha256": digest(target.read_bytes())}))


if __name__ == "__main__":
    main()
