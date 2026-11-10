#!/usr/bin/env python3
"""Build and run certified selection experiments against twenty-six frozen controls."""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


SELECTION_PINS = {
    "selection_bench.cpp": "b1ffc89eadba94ab620276a600a65412b6d7b5716d661b384c3092c8e3c183c9",
    "selection_kernels.hpp": "323b790c1540ccc0d69cb2af2c3300ac172e2a7b062e134b01e08063d83566fc",
}

ADAPTIVE_PINS = {
    "adaptive_bench.cpp": "c98662a7ed38858c186dfd238c4b6b1d1bacdd51cff891ba7f5591c583d831a9",
    "adaptive_kernels.hpp": "6461477abf5cadd4b8c54429ba39c5da073bfb6ac0a194f21ee39fa01b81f25b",
    "run_experiment.py": "b9fc3c916db505a4731a8a9371bd2c05308c51c8d06ea05c8b0ef247c4043365",
}


def locate(explicit, parent, canonical, short, name, flag):
    choices = [explicit] if explicit is not None else [parent / canonical / name, parent / short / name]
    for p in choices:
        if p.is_file():
            return p.resolve()
    raise SystemExit(f"Provide {flag} pointing to the exact dependency")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module_from(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ["selection-source", "adaptive-source", "robust-source", "sampled-source", "base-source", "local-kernels"]:
        p.add_argument("--" + name, type=Path)
    p.add_argument("--cpu", type=int, default=0)
    p.add_argument("--sanitize", action="store_true")
    p.add_argument("--verify-only", action="store_true")
    p.add_argument("--build-only", action="store_true")
    p.add_argument("--skip-build", action="store_true")
    p.add_argument("--skip-verify", action="store_true")
    p.add_argument("--max-n", type=int, default=1_000_000)
    p.add_argument("--target-seconds", type=float, default=.012)
    p.add_argument("--subset", default="all")
    p.add_argument("--output", type=Path)
    p.add_argument("--receipt", type=Path)
    args = p.parse_args()
    root = Path(__file__).resolve().parent
    parent = root.parent
    selection = locate(args.selection_source, parent, "brc_residual_sort_selection_20261110_b0e94005",
                       "brc_selection_sort", "selection_bench.cpp", "--selection-source")
    adaptive = locate(args.adaptive_source, parent, "brc_residual_sort_adaptive_20261110_b0e94005",
                      "brc_adaptive_sort", "adaptive_bench.cpp", "--adaptive-source")
    robust = locate(args.robust_source, parent, "brc_residual_sort_robust_20261110_b0e94005",
                    "brc_robust_sort", "robust_bench.cpp", "--robust-source")
    sampled = locate(args.sampled_source, parent, "brc_residual_sort_sampled_20261108_b0e94005",
                     "brc_sampled_sort", "sampled_bench.cpp", "--sampled-source")
    base = locate(args.base_source, parent, "brc_residual_sort_expanded_20261107_b0e94005",
                  "brc_expanded_sort", "pure_bench.cpp", "--base-source")
    local = locate(args.local_kernels, parent, "brc_residual_sort_local_20261107_b0e94005",
                   "brc_local_sort", "local_kernels.hpp", "--local-kernels")
    checks = []
    for name, expected in SELECTION_PINS.items():
        source = selection.parent / name
        actual = sha256(source)
        if actual != expected:
            raise SystemExit(f"Frozen selection source differs: {source}")
        checks.append(dict(path=str(source), hash_kind="sha256", hash=actual, result="PASS"))
    for name, expected in ADAPTIVE_PINS.items():
        source = adaptive.parent / name
        actual = sha256(source)
        if actual != expected:
            raise SystemExit(f"Frozen adaptive source differs: {source}")
        checks.append(dict(path=str(source), hash_kind="sha256", hash=actual, result="PASS"))
    phase2 = module_from(adaptive.with_name("run_experiment.py"), "frozen_adaptive_runner")
    for name, expected in phase2.ROBUST_PINS.items():
        source = robust.parent / name
        actual = sha256(source)
        if actual != expected:
            raise SystemExit(f"Frozen robust source differs: {source}")
        checks.append(dict(path=str(source), hash_kind="sha256", hash=actual, result="PASS"))
    phase1 = module_from(robust.with_name("run_experiment.py"), "frozen_robust_runner")
    for source in [sampled, sampled.with_name("sampled_kernels.hpp"), sampled.with_name("flat_frequency.hpp"),
                   base, local, robust.parent / "vendor/pdqsort.h", robust.parent / "vendor/license.txt"]:
        kind, expected = phase1.PINS[source.name]
        actual = phase1.hash_file(source, kind)
        if actual != expected:
            raise SystemExit(f"Frozen dependency differs: {source}")
        checks.append(dict(path=str(source), hash_kind=kind, hash=actual, result="PASS"))
    cpus = sorted(os.sched_getaffinity(0))
    if args.cpu not in cpus:
        raise SystemExit("Selected CPU is outside process affinity")
    build = root / "build"
    build.mkdir(exist_ok=True)
    flavor = "sanitized" if args.sanitize else "optimized"
    binary = build / ("certified_bench_sanitized" if args.sanitize else "certified_bench")
    output = args.output or Path(f"results_{args.subset}.csv")
    output = output if output.is_absolute() else root / output
    receipt_file = args.receipt or Path(f"execution_{flavor}_{args.subset}.json")
    receipt_file = receipt_file if receipt_file.is_absolute() else root / receipt_file
    flags = ["-std=c++20", "-Wall", "-Wextra", "-march=native"]
    flags += (["-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
              if args.sanitize else ["-O3", "-DNDEBUG"])
    commands = []
    if not args.skip_build:
        commands += [
            [sys.executable, str(root / "prepare_frozen_include.py"),
             "--selection-source", str(selection), "--adaptive-source", str(adaptive), "--robust-source", str(robust),
             "--sampled-source", str(sampled), "--output-dir", str(build)],
            ["g++", *flags, f'-DBRC_BASE_SOURCE="{base}"', f'-DBRC_LOCAL_KERNELS="{local}"',
             f'-DBRC_SAMPLED_SOURCE="{build / "sampled_frozen_include.hpp"}"',
             f'-DBRC_ROBUST_SOURCE="{build / "robust_frozen_include.hpp"}"',
             f'-DBRC_ADAPTIVE_SOURCE="{build / "adaptive_frozen_include.hpp"}"',
             f'-DBRC_SELECTION_SOURCE="{build / "selection_frozen_include.hpp"}"',
             "-I", str(sampled.parent), "-I", str(robust.parent), "-I", str(adaptive.parent), "-I", str(selection.parent),
             str(root / "certified_bench.cpp"), "-o", str(binary)],
        ]
    if not args.build_only and not args.skip_verify:
        commands.append(["taskset", "-c", str(args.cpu), str(binary), "--verify"])
    if not args.build_only and not args.verify_only and not args.sanitize:
        commands.append(["taskset", "-c", str(args.cpu), str(binary), "--bench", str(output),
                         str(args.max_n), str(args.target_seconds), args.subset])
    env = dict(os.environ)
    if args.sanitize:
        env["ASAN_OPTIONS"] = "detect_leaks=0"
    receipt = {
        "os": platform.platform(), "selected_cpu": args.cpu, "cpu_affinity": cpus,
        "cpu": next((s.split(":", 1)[1].strip() for s in Path("/proc/cpuinfo").read_text().splitlines()
                     if s.startswith("model name")), "unknown"),
        "compiler": subprocess.check_output(["g++", "--version"], text=True).splitlines()[0],
        "dependency_checks": checks,
        "selection_scientific_commit": "6b096de75513160a579032ea11bc6cf8abd06008",
        "adaptive_scientific_commit": "1001e80fd510c8de6a9761dc20068e0e3c8c671d",
        "source_sha256": {s: sha256(root / s) for s in
                          ["certified_bench.cpp", "certified_kernels.hpp", "prepare_frozen_include.py", "run_experiment.py"]},
        "sanitizer_options": {"ASAN_OPTIONS": "detect_leaks=0"} if args.sanitize else {},
        "performance_subset": args.subset, "performance_output": str(output), "commands": [],
    }
    for argv in commands:
        step = dict(argv=argv, started_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
        start = time.perf_counter()
        run = subprocess.run(argv, cwd=root, env=env, capture_output=True, text=True)
        step.update(elapsed_seconds=time.perf_counter() - start, exit_code=run.returncode,
                    stdout=run.stdout, stderr=run.stderr)
        receipt["commands"].append(step)
        if binary.is_file():
            receipt["binary_sha256"] = sha256(binary)
        receipt_file.parent.mkdir(parents=True, exist_ok=True)
        receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps({"program": argv[0], "last_arguments": argv[-3:], "exit_code": run.returncode,
                          "seconds": round(step["elapsed_seconds"], 3)}), flush=True)
        if run.returncode:
            print(run.stderr, flush=True)
            raise SystemExit(run.returncode)
    receipt["result"] = "PASS"
    receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    print(str(receipt_file), flush=True)


if __name__ == "__main__":
    main()
