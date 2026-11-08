#!/usr/bin/env python3
"""Compile and reproduce the sampled residual-sorting experiment."""
import argparse
import datetime
import json
import os
from pathlib import Path
import platform
import subprocess
import time


def locate(explicit, choices, name):
    candidates = [explicit] if explicit else choices
    for p in candidates:
        if p.is_file():
            return p.resolve()
    raise SystemExit(f"Provide {name} pointing to the preceding source")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base-source", type=Path)
    p.add_argument("--local-kernels", type=Path)
    p.add_argument("--cpu", type=int, default=0)
    p.add_argument("--sanitize", action="store_true")
    p.add_argument("--verify-only", action="store_true")
    p.add_argument("--max-n", type=int, default=1_000_000)
    p.add_argument("--target-seconds", type=float, default=.012)
    p.add_argument("--subset", default="all")
    args = p.parse_args()
    root = Path(__file__).resolve().parent
    base = locate(args.base_source, [
        root.parent / "brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp",
        root.parent / "brc_expanded_sort/pure_bench.cpp"], "--base-source")
    local = locate(args.local_kernels, [
        root.parent / "brc_residual_sort_local_20261107_b0e94005/local_kernels.hpp",
        root.parent / "brc_local_sort/local_kernels.hpp"], "--local-kernels")
    cpus = sorted(os.sched_getaffinity(0))
    if args.cpu not in cpus:
        raise SystemExit("Selected CPU is outside this process's affinity")
    flags = ["-std=c++20", "-Wall", "-Wextra"]
    flags += (["-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
              if args.sanitize else ["-O3", "-DNDEBUG"])
    flavor = "sanitized" if args.sanitize else "optimized"
    binary = "sampled_bench_sanitized" if args.sanitize else "sampled_bench"
    commands = [
        ["g++", *flags, f'-DBRC_BASE_SOURCE="{base}"', f'-DBRC_LOCAL_KERNELS="{local}"',
         "sampled_bench.cpp", "-o", binary],
        ["taskset", "-c", str(args.cpu), "./" + binary, "--verify"],
    ]
    if not args.sanitize and not args.verify_only:
        commands.append(["taskset", "-c", str(args.cpu), "./" + binary, "--bench",
                         f"results_{args.subset}.csv", str(args.max_n),
                         str(args.target_seconds), args.subset])
    env = dict(os.environ)
    if args.sanitize:
        # Address/undefined checks are active. Leak checking is outside this run.
        env["ASAN_OPTIONS"] = "detect_leaks=0"
    receipt = {
        "os": platform.platform(), "selected_cpu": args.cpu, "cpu_affinity": cpus,
        "cpu": next((s.split(":", 1)[1].strip() for s in Path("/proc/cpuinfo").read_text().splitlines()
                     if s.startswith("model name")), "unknown"),
        "compiler": subprocess.check_output(["g++", "--version"], text=True).splitlines()[0],
        "base_source": str(base), "previous_local_kernels": str(local),
        "base_scientific_commit": "5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28",
        "local_scientific_commit": "4b66597bce400f6d19336058ac780e877188a769",
        "sanitizer_options": {"ASAN_OPTIONS": "detect_leaks=0"} if args.sanitize else {},
        "commands": [],
    }
    out = root / f"execution_{flavor}_{args.subset}.json"
    for argv in commands:
        step = {"argv": argv, "started_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        start = time.perf_counter()
        run = subprocess.run(argv, cwd=root, env=env, capture_output=True, text=True)
        step.update(elapsed_seconds=time.perf_counter() - start, exit_code=run.returncode,
                    stdout=run.stdout, stderr=run.stderr)
        receipt["commands"].append(step)
        out.write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps({"argv": argv, "exit_code": run.returncode,
                          "seconds": round(step["elapsed_seconds"], 3)}), flush=True)
        if run.returncode:
            print(run.stderr, flush=True)
            raise SystemExit(run.returncode)
    receipt["result"] = "PASS"
    out.write_text(json.dumps(receipt, indent=2) + "\n")
    print(str(out), flush=True)


if __name__ == "__main__":
    main()
