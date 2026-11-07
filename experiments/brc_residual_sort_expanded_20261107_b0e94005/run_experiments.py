#!/usr/bin/env python3
"""Build, validate, and time the two BRC expansion experiments sequentially.

The executables generate deterministic rotating input banks. Their timed regions
include input copies, local allocations, sorting, reconstruction, and release.
Run from any directory: python run_experiments.py [--max-n 1000000].
"""
import argparse
import datetime
import json
import os
import pathlib
import platform
import subprocess
import time


def run(argv, cwd, env=None):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    begin = time.perf_counter()
    result = subprocess.run(argv, cwd=cwd, text=True, capture_output=True, env=env)
    receipt = {
        "argv": argv,
        "started_at_utc": started,
        "elapsed_seconds": time.perf_counter() - begin,
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    print(json.dumps({"command": argv, "exit_code": result.returncode,
                      "seconds": round(receipt["elapsed_seconds"], 3)}), flush=True)
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=1_000_000)
    parser.add_argument("--cpu", type=int)
    parser.add_argument("--sanitize", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--only", choices=("record", "pure"))
    args = parser.parse_args()
    root = pathlib.Path(__file__).resolve().parent
    affinity = sorted(os.sched_getaffinity(0))
    cpu = affinity[0] if args.cpu is None else args.cpu
    if cpu not in affinity:
        raise ValueError("Selected CPU is outside the process affinity")
    cpu_names = [line.split(":", 1)[1].strip()
                 for line in pathlib.Path("/proc/cpuinfo").read_text().splitlines()
                 if line.startswith("model name")]
    receipt = {
        "os": platform.platform(),
        "python": platform.python_version(),
        "compiler": subprocess.check_output(["g++", "--version"], text=True).splitlines()[0],
        "cpu": cpu_names[0] if cpu_names else "unknown",
        "available_cpu_affinity": affinity,
        "benchmark_cpu": cpu,
        "max_n": args.max_n,
        "commands": [],
    }
    sanitizer_env = None
    if args.sanitize:
        # The hosted executor denies LeakSanitizer's /proc task enumeration.
        # AddressSanitizer and UndefinedBehaviorSanitizer remain enabled.
        sanitizer_env = dict(os.environ)
        sanitizer_env["ASAN_OPTIONS"] = "detect_leaks=0"
        receipt["sanitizer_options"] = {"ASAN_OPTIONS": "detect_leaks=0"}
    stem = args.only or "all"
    suffix = "sanitized" if args.sanitize else "optimized"
    output = root / f"execution_{stem}_{suffix}.json"
    for name in ((args.only,) if args.only else ("record", "pure")):
        binary = f"{name}_bench_{suffix}"
        flags = ["-std=c++20", "-Wall", "-Wextra"]
        flags += (["-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
                  if args.sanitize else ["-O3", "-DNDEBUG"])
        commands = [["g++", *flags, f"{name}_bench.cpp", "-o", binary],
                    ["taskset", "-c", str(cpu), f"./{binary}", "--verify"]]
        if not args.verify_only and not args.sanitize:
            commands.append(["taskset", "-c", str(cpu), f"./{binary}", "--bench",
                             f"{name}_results.csv", str(args.max_n)])
        for command in commands:
            result = run(command, root, sanitizer_env if args.sanitize else None)
            receipt["commands"].append(result)
            output.write_text(json.dumps(receipt, indent=2) + "\n")
            if result["exit_code"]:
                print(result["stderr"], flush=True)
                raise SystemExit(result["exit_code"])
    receipt["result"] = "PASS"
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(str(output), flush=True)


if __name__ == "__main__":
    main()
