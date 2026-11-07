#!/usr/bin/env python3
"""Reproduce the local-residual experiment against its preceding source file."""
import argparse
import datetime
import json
import os
from pathlib import Path
import platform
import subprocess
import time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-source", type=Path)
    ap.add_argument("--max-n", type=int, default=1_000_000)
    ap.add_argument("--target-seconds", type=float, default=0.012)
    ap.add_argument("--cpu", type=int, default=0)
    ap.add_argument("--sanitize", action="store_true")
    ap.add_argument("--verify-only", action="store_true")
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    candidates = ([args.base_source] if args.base_source else [
        root.parent / "brc_residual_sort_expanded_20261107_b0e94005" / "pure_bench.cpp",
        root.parent / "brc_expanded_sort" / "pure_bench.cpp",
    ])
    base = next((p.resolve() for p in candidates if p.is_file()), None)
    if base is None:
        raise SystemExit("Provide --base-source pointing to the preceding pure_bench.cpp")
    affinity = sorted(os.sched_getaffinity(0))
    if args.cpu not in affinity:
        raise SystemExit("Requested CPU is outside this process's CPU affinity")
    cpu_names = [x.split(":", 1)[1].strip() for x in Path("/proc/cpuinfo").read_text().splitlines()
                 if x.startswith("model name")]
    suffix = "sanitized" if args.sanitize else "optimized"
    binary = f"local_bench_{suffix}"
    flags = ["-std=c++20", "-Wall", "-Wextra"]
    flags += (["-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
              if args.sanitize else ["-O3", "-DNDEBUG"])
    command_list = [["g++", *flags, f'-DBRC_BASE_SOURCE="{base}"',
                     "local_bench.cpp", "-o", binary],
                    ["taskset", "-c", str(args.cpu), f"./{binary}", "--verify"]]
    if not args.verify_only and not args.sanitize:
        command_list.append(["taskset", "-c", str(args.cpu), f"./{binary}",
                             "--bench", "local_results.csv", str(args.max_n),
                             str(args.target_seconds)])
    env = None
    if args.sanitize:
        # This executor cannot perform LeakSanitizer's /proc task enumeration.
        # AddressSanitizer and UndefinedBehaviorSanitizer are still active.
        env = dict(os.environ)
        env["ASAN_OPTIONS"] = "detect_leaks=0"
    receipt = {"os": platform.platform(), "cpu": cpu_names[0] if cpu_names else "unknown",
               "compiler": subprocess.check_output(["g++", "--version"], text=True).splitlines()[0],
               "cpu_affinity": affinity, "selected_cpu": args.cpu,
               "base_source": str(base),
               "expected_base_source_commit": "5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28",
               "expected_base_source_blob": "868723dc6b627b7230d4c54149d276537138b7aa",
               "sanitizer_options": {"ASAN_OPTIONS": "detect_leaks=0"} if args.sanitize else {},
               "commands": []}
    path = root / f"execution_{suffix}.json"
    for argv in command_list:
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        begin = time.perf_counter()
        p = subprocess.run(argv, cwd=root, text=True, capture_output=True, env=env)
        step = {"argv": argv, "started_at_utc": started,
                "elapsed_seconds": time.perf_counter() - begin, "exit_code": p.returncode,
                "stdout": p.stdout, "stderr": p.stderr}
        receipt["commands"].append(step)
        path.write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps({"command": argv, "exit_code": p.returncode,
                          "seconds": round(step["elapsed_seconds"], 3)}), flush=True)
        if p.returncode:
            print(p.stderr, flush=True)
            raise SystemExit(p.returncode)
    receipt["result"] = "PASS"
    path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(str(path), flush=True)


if __name__ == "__main__":
    main()
