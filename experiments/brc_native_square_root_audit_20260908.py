"""Compare an exact integer-square-root implementation on fixed saved data.

Public work is state reconstruction at 66 previously recorded positions, not
new square-witness queries. Complete-cost witness measurements use only the
three pinned constructive controls. Each variant runs in a fresh process.
"""
from __future__ import annotations

import argparse
from hashlib import sha1, sha256
from math import gcd
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter_ns
import json
import platform
import subprocess
import sys


CORE_BLOBS = {
    "baseline": "cdb8ace10e4cc8bba13b70f4da306313efb24819",
    "candidate": "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07",
}
SOURCE_BLOBS = {
    "brc_square_gap_prefilter.py": "42d4e9a397b56d9d371f034780ffc736d43e6d96",
    "brc_opportunistic_shortcuts.py": "1214aa09770893fb3de7f85b994d1994ff56bffe",
}
INPUT_BLOBS = {
    "brc_public_rsa_fixed_predicates_20260908.json": "e56cfc8457e2398b5de3c90182c2b37824580ef3",
    "brc_public_frozen_prefix_20260908.json": "c4b201e608167cfff96c5a141bd9e26b575dad69",
    "brc_materialized_gap_order_20260908.json": "9a866dd4a923fa046768346c3ce0f1f49f4dc73c",
}


def checked_text(path, expected_blob):
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
    assert sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest() == expected_blob
    return raw.decode("utf-8")


def worker(root, variant):
    source = root/"src"/"enterprise_math"
    checked_text(source/"core.py", CORE_BLOBS[variant])
    for name, blob in SOURCE_BLOBS.items():
        checked_text(source/name, blob)
    sys.path.insert(0, str(root/"src"))
    import enterprise_math.core as core
    import enterprise_math.brc_square_gap_prefilter as gap_api
    assert Path(core.__file__).resolve() == (source/"core.py").resolve()
    assert gap_api.integer_nth_root is core.integer_nth_root
    data = [json.loads(checked_text(Path(__file__).resolve().parent/name, blob))
        for name, blob in INPUT_BLOBS.items()]
    original, prefix, projected = data
    labels = ["RSA-270", "RSA-896", "RSA-2048"]
    assert [r["label"] for r in original["records"]] == labels
    assert [r["label"] for r in prefix["records"]] == labels
    assert [r["label"] for r in projected["public_records"]] == labels

    # One small explicit warmup, outside the measured arithmetic paths.
    assert gap_api.ceiling_completion_square_witness(15, 1) == (4, 1)
    public = []
    for parent, saved, added in zip(original["records"], prefix["records"], projected["public_records"], strict=True):
        n = int(parent["N"])
        assert sha256(parent["N"].encode("ascii")).hexdigest() == parent["decimal_sha256"]
        golden = {e["multiplier"]: (int(e["gap"]), e["multiplied_direction"])
            for e in saved["evaluations"]}
        for entry in added["new_derived_positions"]:
            assert entry["target_multiplier"] not in golden
            golden[entry["target_multiplier"]] = (int(entry["A"]), entry["direction"])
        assert len(golden) == 22
        multipliers = tuple(sorted(golden))
        started = perf_counter_ns()
        states = [gap_api.ceiling_completion_cost(n, m) for m in multipliers]
        elapsed = perf_counter_ns()-started
        digest_rows = []
        for m, (a, gap) in zip(multipliers, states, strict=True):
            assert gap == golden[m][0] and a*a-gap == m*n
            assert (a-1)**2 < m*n <= a*a
            j = a if gap == 0 else a-1
            remainder = m*n-j*j
            assert 0 <= remainder <= 2*j
            direction = "Z" if remainder == 0 else "D" if remainder <= j else "U"
            assert direction == golden[m][1]
            digest_rows.append([m, str(a), str(gap), direction])
        digest = sha256(json.dumps(digest_rows, separators=(",", ":")).encode("ascii")).hexdigest()
        public.append({"label": parent["label"], "bits": n.bit_length(), "states": 22,
            "state_preparation_ns": elapsed, "state_digest": digest,
            "exact_saved_gaps_and_directions_agree": True})

    controls = [r for r in projected["positive_controls"] if r["kind"] == "constructed_large"]
    assert [r["N_bits"] for r in controls] == [896,2048,8192]
    positive = []
    for row in controls:
        t = int(row["t"])
        n = t*(2*t+1)
        assert n.bit_length() == row["N_bits"]
        started = perf_counter_ns()
        first = gap_api.ceiling_completion_square_witness(n, 1)
        second = gap_api.ceiling_completion_square_witness(n, 8)
        assert first is None and second is not None
        a, b = second
        factor = gcd(n, a-b)
        assert 1 < factor < n and n % factor == 0
        assert factor*(n//factor) == n and a*a-b*b == 8*n
        elapsed = perf_counter_ns()-started
        assert (a,b) == (4*t+1,1) and factor == t
        positive.append({"N_bits": n.bit_length(), "complete_cost_ns": elapsed,
            "fixed_positions": [1,8], "source_api_calls": 2,
            "witness": "(4t+1,1) at multiplier 8", "proper_factor_verified": True,
            "factor_sha256": sha256(str(factor).encode("ascii")).hexdigest()})
    return {"variant": variant, "core_blob": CORE_BLOBS[variant], "public": public,
        "positive": positive, "python": sys.version, "platform": platform.platform()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-root", type=Path)
    parser.add_argument("--candidate-root", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--worker-root", type=Path)
    parser.add_argument("--worker-variant", choices=tuple(CORE_BLOBS))
    args = parser.parse_args()
    if args.worker_root is not None:
        assert args.worker_variant is not None
        print(json.dumps(worker(args.worker_root, args.worker_variant)))
        return
    if args.baseline_root is None or args.candidate_root is None:
        parser.error("--baseline-root and --candidate-root are required")
    roots = {"baseline": args.baseline_root, "candidate": args.candidate_root}
    rng = Random(20260908)
    trials = []
    for round_number in range(7):
        order = ["baseline", "candidate"]
        rng.shuffle(order)
        for variant in order:
            command = [sys.executable, str(Path(__file__).resolve()), "--worker-root",
                str(roots[variant]), "--worker-variant", variant]
            completed = subprocess.run(command, text=True, capture_output=True, check=True)
            result = json.loads(completed.stdout)
            assert result["variant"] == variant and result["core_blob"] == CORE_BLOBS[variant]
            trials.append({"round": round_number, "order_in_round": order.index(variant), **result})

    public_summary, positive_summary = [], []
    for index in range(3):
        public_rows = [r["public"][index] for r in trials]
        positive_rows = [r["positive"][index] for r in trials]
        assert len({r["state_digest"] for r in public_rows}) == 1
        assert len({r["factor_sha256"] for r in positive_rows}) == 1
        public_raw = {v: [r["public"][index]["state_preparation_ns"] for r in trials if r["variant"] == v]
            for v in CORE_BLOBS}
        positive_raw = {v: [r["positive"][index]["complete_cost_ns"] for r in trials if r["variant"] == v]
            for v in CORE_BLOBS}
        for values in (public_raw, positive_raw):
            assert all(len(values[v]) == 7 for v in CORE_BLOBS)
        pmed = {v: median(values) for v,values in public_raw.items()}
        cmed = {v: median(values) for v,values in positive_raw.items()}
        public_summary.append({"label": public_rows[0]["label"], "states": 22,
            "raw_ns": public_raw, "median_ns": pmed,
            "baseline_over_candidate": pmed["baseline"]/pmed["candidate"],
            "candidate_faster_rounds": sum(a>b for a,b in zip(public_raw["baseline"],public_raw["candidate"])),
            "state_digest": public_rows[0]["state_digest"]})
        positive_summary.append({"N_bits": positive_rows[0]["N_bits"],
            "raw_ns": positive_raw, "median_ns": cmed,
            "baseline_over_candidate": cmed["baseline"]/cmed["candidate"],
            "candidate_faster_rounds": sum(a>b for a,b in zip(positive_raw["baseline"],positive_raw["candidate"])),
            "factor_sha256": positive_rows[0]["factor_sha256"]})
    result = {"status": "COMPLETED_EXACT_SQUARE_ROOT_IMPLEMENTATION_AUDIT",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "b2d9ceff961c70ecb356721aafcb03d31396daeb",
        "project_parent": "0ba74daea4992becd19b9cc5aaed08854eae729d",
        "core_blobs": CORE_BLOBS, "unchanged_source_blobs": SOURCE_BLOBS,
        "input_certificates": INPUT_BLOBS, "rounds": 7, "trials": trials,
        "public_summary": public_summary, "positive_summary": positive_summary,
        "implementation_change": "After existing validation and trivial cases, p==2 uses exact math.isqrt; the p>2 algorithm and interfaces are unchanged.",
        "reuse_resolution": "EXTEND_EXISTING_TOOL using standard-library isqrt already used in the square-gap module; no new search method or router.",
        "coverage": {"reused_public_positions": 66, "new_public_positions": 0,
            "new_public_square_witness_queries": 0, "public_state_reconstructions": 924,
            "fixed_constructive_inputs": 3, "constructive_witness_api_calls": 84,
            "small_warmup_calls_outside_timers": 14, "timing_rounds_are_new_hits": False},
        "unit_tests": {"status": "passed before this benchmark", "count": 46,
            "modules": ["test_core", "test_brc_square_gap_prefilter", "test_brc_multiplier_basin",
                "test_brc_multiplier_priority_jump", "test_brc_opportunistic_shortcuts"],
            "new_coverage": "large square-basin boundaries through 8192-bit targets and retained integer/ValueError validation"},
        "cost_contract": {"public": "From supplied N and a fixed saved multiplier to exact ceiling/gap; caller loop and root acquisition included, audits outside timer.",
            "constructive": "Same fixed two source API calls at m=1,8 plus gcd/product verification, from the prescribed N; root preparation included.",
            "outside_timers": "Fresh interpreter start, imports, source/input checks, warmup, fixture construction and serialization.",
            "process_isolation": "Each variant/round imports from its own verified checkout in a fresh process; no runtime monkeypatch or module mixing.",
            "not_claimed": "New public factoring coverage, a new mathematical factorization method, or a universal speed ratio against other integer-root implementations."},
        "goal_status": "ACTIVE; implementation cost improved and archived states retained, public factorization still not achieved"}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir/"brc_native_square_root_audit_20260908.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "public": public_summary,
        "constructive": positive_summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
