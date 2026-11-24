#!/usr/bin/env python3
"""Replay selected research branches into a separate output directory."""
from pathlib import Path
import argparse
import importlib.metadata
import importlib.util
import json
import shutil
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent
BRANCHES = {
    "crossing_tree": {
        "script": "verify_crossing_tree.py",
        "certificate": "crossing_tree_certificate.json",
        "copy_inputs": ["fixed_inputs.json"],
    },
    "directed_arithmetic": {
        "script": "certify_local_arithmetic.py",
        "certificate": "local_arithmetic_certificate.json",
        "prior_files": [
            "dependencies/certify_fast_harmonic_energy.py",
            "prefix_compute/fixed_matched_family.json",
            "inputs/rh_triangle_certificate_20261122/dyadic_triangle_certificate.json",
        ],
        "source_inputs": ["fixed_triangle_geometry.json"],
    },
    "matching_transfer": {
        "script": "certify_matching_kernel.py",
        "certificate": "matching_kernel_certificate.json",
        "prior_files": [
            "dependencies/certify_fast_harmonic_energy.py",
            "prefix_compute/certify_paired_prefix.py",
            "prefix_compute/fixed_matched_family.json",
            "prefix_compute/fixed_node_positions.json",
            "prefix_compute/paired_prefix_certificate.json",
            "inputs/rh_partial_frontier_20261122/sparse_sample_observations.json",
        ],
    },
    "matching_order": {
        "script": "certify_matching_order.py",
        "certificate": "matching_order_certificate.json",
        "copy_inputs": [],
        "requires_sympy": True,
    },
    "harmonic_windows": {
        "script": "verify_harmonic_windows.py",
        "certificate": "harmonic_window_certificate.json",
        "copy_inputs": [],
    },
}


def plan_for(name, prior, output):
    spec = BRANCHES[name]
    source = ROOT / name
    destination = output / name
    script = source / spec["script"]
    required = [script]
    required += [source / p for p in spec.get("copy_inputs", [])]
    required += [source / p for p in spec.get("source_inputs", [])]
    required += [prior / p for p in spec.get("prior_files", [])]
    missing = [str(p) for p in required if not p.is_file()]
    if missing:
        raise ValueError("Missing input files for " + name + ":\n" + "\n".join(missing))

    copied = "copy_inputs" in spec
    executable_script = destination / spec["script"] if copied else script
    command = [sys.executable, "-B", str(executable_script)]
    certificate = destination / spec["certificate"]
    if name == "directed_arithmetic":
        command += [
            "--harmonic-module", str(prior / spec["prior_files"][0]),
            "--family", str(prior / spec["prior_files"][1]),
            "--geometry", str(source / "fixed_triangle_geometry.json"),
            "--comparison", str(prior / spec["prior_files"][2]),
            "--output", str(certificate),
        ]
    elif name == "matching_transfer":
        command += ["--prior", str(prior), "--output", str(certificate)]

    return {"branch": name, "source": str(source), "output": str(destination),
            "command": command, "copy_script_and_inputs": copied,
            "copy_inputs": spec.get("copy_inputs", []),
            "certificate": str(certificate),
            "required_files": list(map(str, required))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", nargs="+", choices=["all", *BRANCHES], default=["all"],
                        help="one or more branches; default: all")
    parser.add_argument("--prior", type=Path,
                        default=ROOT / "prior/riemann_cumulative_haar_20261123",
                        help="complete previous package; needed by directed_arithmetic and matching_transfer")
    parser.add_argument("--output", type=Path, required=True,
                        help="separate output directory, for example /tmp/riemann-replay")
    parser.add_argument("--check", action="store_true",
                        help="validate arguments, dependencies and input paths; do not execute calculations")
    args = parser.parse_args()
    if "all" in args.branch and len(args.branch) != 1:
        parser.error("Use --branch all by itself, or name individual branches.")
    names = list(BRANCHES) if args.branch == ["all"] else list(dict.fromkeys(args.branch))
    prior = args.prior.expanduser().resolve()
    output = args.output.expanduser().resolve()
    # These scripts write certificates beside their own copied file, or to an
    # explicit output path. Keep that destination separate from published inputs.
    if output == ROOT or ROOT in output.parents or output == prior or prior in output.parents:
        parser.error("--output must be outside the current and previous source-package directories.")
    versions = {"python": sys.version.split()[0]}
    if any(BRANCHES[name].get("requires_sympy") for name in names):
        if importlib.util.find_spec("sympy") is None:
            parser.error("matching_order requires SymPy in this Python environment.")
        versions["sympy"] = importlib.metadata.version("sympy")
    try:
        plans = [plan_for(name, prior, output) for name in names]
    except ValueError as exc:
        parser.error(str(exc))
    if args.check:
        print(json.dumps({"status": "PATHS_AND_DEPENDENCIES_CHECKED_NO_CALCULATIONS",
                          "versions": versions, "plans": plans}, indent=2))
        return

    output.mkdir(parents=True, exist_ok=True)
    report = {"status": "RUNNING", "versions": versions,
              "prior": str(prior), "source": str(ROOT), "branches": []}
    report_path = output / "replay_run.json"
    for plan in plans:
        destination = Path(plan["output"])
        destination.mkdir(parents=True, exist_ok=True)
        if plan["copy_script_and_inputs"]:
            source = Path(plan["source"])
            for filename in [BRANCHES[plan["branch"]]["script"], *plan["copy_inputs"]]:
                shutil.copy2(source / filename, destination / filename)
        print("Running " + plan["branch"], flush=True)
        started = time.perf_counter()
        result = subprocess.run(plan["command"], cwd=destination,
                                capture_output=True, text=True)
        (destination / "stdout.txt").write_text(result.stdout)
        (destination / "stderr.txt").write_text(result.stderr)
        row = {"branch": plan["branch"], "command": plan["command"],
               "exit_code": result.returncode,
               "seconds": time.perf_counter() - started,
               "certificate": plan["certificate"],
               "certificate_present": Path(plan["certificate"]).is_file()}
        report["branches"].append(row)
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip(), file=sys.stderr)
        if result.returncode != 0 or not row["certificate_present"]:
            report["status"] = "FAILED"
            report_path.write_text(json.dumps(report, indent=2) + "\n")
            raise SystemExit(result.returncode or 1)
    report["status"] = "ALL_SELECTED_BRANCHES_COMPLETED"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print("Saved replay outputs to " + str(output))


if __name__ == "__main__":
    main()
