#!/usr/bin/env python3
"""Reproduce the robust residual sorting experiment from pinned source files.

Dependencies are read from an existing checkout, never downloaded by this script.
Performance commands are serial; every command's real result is retained.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


PINS = {
    "sampled_bench.cpp": ("sha256", "596cf4add967669ec1feb02344f49ec448bd4c0b927ed9b791cc03d802b86468"),
    "sampled_kernels.hpp": ("sha256", "2890d16a360fa9c874dc8de1edec1508f9522602397fc2cb7fbe6e2da55cb192"),
    "flat_frequency.hpp": ("sha256", "3993c376b0160e87eee16acb7ca3e832fa2e7ac227320b909bb922f53f89350a"),
    "pure_bench.cpp": ("git_blob_sha1", "868723dc6b627b7230d4c54149d276537138b7aa"),
    "local_kernels.hpp": ("git_blob_sha1", "3c5a7302066f333a084101a3ab08b37f974660de"),
    "pdqsort.h": ("git_blob_sha1", "36360cd1d69d0bd6977d9ba2313b10612b889142"),
    "license.txt": ("git_blob_sha1", "41d496076f0e134ba66096cf89acee8e124afef5"),
}


def locate(explicit, choices, label):
    for path in ([explicit] if explicit is not None else choices):
        if path.is_file():
            return path.resolve()
    raise SystemExit(f"Provide {label} pointing to its frozen dependency")


def hash_file(path, kind="sha256"):
    data = path.read_bytes()
    if kind == "git_blob_sha1":
        return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-source", type=Path)
    parser.add_argument("--local-kernels", type=Path)
    parser.add_argument("--sampled-source", type=Path)
    parser.add_argument("--cpu", type=int, default=0)
    parser.add_argument("--sanitize", action="store_true")
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--skip-verify", action="store_true")
    parser.add_argument("--max-n", type=int, default=1_000_000)
    parser.add_argument("--target-seconds", type=float, default=.012)
    parser.add_argument("--subset", default="all")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    base = locate(args.base_source, [
        root.parent / "brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp",
        root.parent / "brc_expanded_sort/pure_bench.cpp"], "--base-source")
    local = locate(args.local_kernels, [
        root.parent / "brc_residual_sort_local_20261107_b0e94005/local_kernels.hpp",
        root.parent / "brc_local_sort/local_kernels.hpp"], "--local-kernels")
    sampled = locate(args.sampled_source, [
        root.parent / "brc_residual_sort_sampled_20261108_b0e94005/sampled_bench.cpp",
        root.parent / "brc_sampled_sort/sampled_bench.cpp"], "--sampled-source")
    dependencies = [base, local, sampled, sampled.with_name("sampled_kernels.hpp"),
                    sampled.with_name("flat_frequency.hpp"), root / "vendor/pdqsort.h",
                    root / "vendor/license.txt"]
    pin_checks = []
    for path in dependencies:
        kind, expected = PINS[path.name]
        actual = hash_file(path, kind)
        if actual != expected:
            raise SystemExit(f"Frozen dependency mismatch: {path.name}: {actual}")
        pin_checks.append(dict(path=str(path), hash_kind=kind, hash=actual, result="PASS"))
    cpus = sorted(os.sched_getaffinity(0))
    if args.cpu not in cpus:
        raise SystemExit("Selected CPU is outside this process's affinity")
    build = root / "build"
    build.mkdir(exist_ok=True)
    generated = build / "sampled_frozen_include.hpp"
    flavor = "sanitized" if args.sanitize else "optimized"
    binary = build / ("robust_bench_sanitized" if args.sanitize else "robust_bench")
    output = (args.output or Path(f"results_{args.subset}.csv"))
    output = output if output.is_absolute() else root / output
    receipt_path = args.receipt or Path(f"execution_{flavor}_{args.subset}.json")
    receipt_path = receipt_path if receipt_path.is_absolute() else root / receipt_path
    flags = ["-std=c++20", "-Wall", "-Wextra", "-march=native"]
    flags += (["-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
              if args.sanitize else ["-O3", "-DNDEBUG"])
    commands = []
    if not args.skip_build:
        commands += [
            [sys.executable, str(root / "prepare_frozen_include.py"), "--source", str(sampled),
             "--output", str(generated)],
            ["g++", *flags, f'-DBRC_BASE_SOURCE="{base}"', f'-DBRC_LOCAL_KERNELS="{local}"',
             f'-DBRC_SAMPLED_SOURCE="{generated}"', "-I", str(sampled.parent),
             str(root / "robust_bench.cpp"), "-o", str(binary)],
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
        "dependency_checks": pin_checks,
        "source_sha256": {p.name: hash_file(p) for p in
            [root / "robust_bench.cpp", root / "robust_kernels.hpp",
             root / "prepare_frozen_include.py", root / "run_experiment.py"]},
        "scientific_commits": {
            "expanded": "5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28",
            "local": "4b66597bce400f6d19336058ac780e877188a769",
            "sampled": "8bf6a677359b62d406eaa7258f5541431466315b",
            "pdqsort": "b1ef26a55cdb60d236a5cb199c4234c704f46726"},
        "sanitizer_options": {"ASAN_OPTIONS": "detect_leaks=0"} if args.sanitize else {},
        "performance_subset": args.subset, "performance_output": str(output),
        "commands": [],
    }
    for argv in commands:
        step = {"argv": argv, "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        start = time.perf_counter()
        run = subprocess.run(argv, cwd=root, env=env, capture_output=True, text=True)
        step.update(elapsed_seconds=time.perf_counter() - start, exit_code=run.returncode,
                    stdout=run.stdout, stderr=run.stderr)
        receipt["commands"].append(step)
        if binary.is_file():
            receipt["binary_sha256"] = hash_file(binary)
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps({"program": argv[0], "last_arguments": argv[-3:],
                          "exit_code": run.returncode,
                          "seconds": round(step["elapsed_seconds"], 3)}), flush=True)
        if run.returncode:
            print(run.stderr, flush=True)
            raise SystemExit(run.returncode)
    receipt["result"] = "PASS"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(str(receipt_path), flush=True)


if __name__ == "__main__":
    main()
