#!/usr/bin/env python3
"""Build and run the adaptive extension against its frozen twenty controls."""
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


ROBUST_PINS = {
    "robust_bench.cpp": "d1f9d696ad8f02efad7d79adfca55087dac0a060e4ec4977cb3bc1c597256d26",
    "robust_kernels.hpp": "46b6ad5f0a7791c733cb8920ee34a01adfade778035c13c14a7390516c8eea68",
    "run_experiment.py": "e1f401dfde343216ad15cf73f5341e67a8dabeb522fdc703a4df1133d4a526e6",
}


def locate(explicit, choices, label):
    for p in ([explicit] if explicit is not None else choices):
        if p.is_file():
            return p.resolve()
    raise SystemExit(f"Provide {label} pointing to the frozen dependency")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--robust-source", type=Path)
    p.add_argument("--sampled-source", type=Path)
    p.add_argument("--base-source", type=Path)
    p.add_argument("--local-kernels", type=Path)
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
    robust = locate(args.robust_source, [
        root.parent / "brc_residual_sort_robust_20261110_b0e94005/robust_bench.cpp",
        root.parent / "brc_robust_sort/robust_bench.cpp"], "--robust-source")
    checks = []
    for name, expected in ROBUST_PINS.items():
        source = robust.parent / name
        actual = sha256(source)
        if actual != expected:
            raise SystemExit(f"Frozen robust source mismatch: {source}")
        checks.append(dict(path=str(source), hash_kind="sha256", hash=actual, result="PASS"))
    spec = importlib.util.spec_from_file_location("frozen_robust_runner", robust.with_name("run_experiment.py"))
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    sampled = locate(args.sampled_source, [
        root.parent / "brc_residual_sort_sampled_20261108_b0e94005/sampled_bench.cpp",
        root.parent / "brc_sampled_sort/sampled_bench.cpp"], "--sampled-source")
    base = locate(args.base_source, [
        root.parent / "brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp",
        root.parent / "brc_expanded_sort/pure_bench.cpp"], "--base-source")
    local = locate(args.local_kernels, [
        root.parent / "brc_residual_sort_local_20261107_b0e94005/local_kernels.hpp",
        root.parent / "brc_local_sort/local_kernels.hpp"], "--local-kernels")
    for source in [sampled, sampled.with_name("sampled_kernels.hpp"), sampled.with_name("flat_frequency.hpp"),
                   base, local, robust.parent / "vendor/pdqsort.h", robust.parent / "vendor/license.txt"]:
        kind, expected = old.PINS[source.name]
        actual = old.hash_file(source, kind)
        if actual != expected:
            raise SystemExit(f"Frozen dependency mismatch: {source}")
        checks.append(dict(path=str(source), hash_kind=kind, hash=actual, result="PASS"))
    cpus = sorted(os.sched_getaffinity(0))
    if args.cpu not in cpus:
        raise SystemExit("Selected CPU is outside the process affinity")
    build = root / "build"
    build.mkdir(exist_ok=True)
    binary = build / ("adaptive_bench_sanitized" if args.sanitize else "adaptive_bench")
    flavor = "sanitized" if args.sanitize else "optimized"
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
             "--robust-source", str(robust), "--sampled-source", str(sampled), "--output-dir", str(build)],
            ["g++", *flags, f'-DBRC_BASE_SOURCE="{base}"', f'-DBRC_LOCAL_KERNELS="{local}"',
             f'-DBRC_SAMPLED_SOURCE="{build / "sampled_frozen_include.hpp"}"',
             f'-DBRC_ROBUST_SOURCE="{build / "robust_frozen_include.hpp"}"',
             "-I", str(sampled.parent), "-I", str(robust.parent),
             str(root / "adaptive_bench.cpp"), "-o", str(binary)],
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
        "robust_scientific_commit": "085ff2fb544cd2bfc85beb75cfd72ed15f6a0569",
        "source_sha256": {s: sha256(root / s) for s in
                          ["adaptive_bench.cpp", "adaptive_kernels.hpp", "prepare_frozen_include.py", "run_experiment.py"]},
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
