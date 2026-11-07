"""Construct six prescribed 2048-bit semiprimes and time existing BRC queries.

Only synthetic cases from the fixed families below are generated. No external
modulus, key, ciphertext, factor-search budget, or public challenge is accepted.
Generation/primality proof and N-only query timing are separate stages.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import statistics
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter_ns


HERE = Path(__file__).resolve().parent
RUN = HERE/"semiprime-20260909"
GENERATION_FILE = RUN/"brc_proved_semiprime2048_20260909.json"
INPUT_FILE = RUN/"brc_proved_semiprime2048_inputs_20260909.json"
TIMING_FILE = RUN/"brc_proved_semiprime2048_timings_20260909.json"
CANONICAL = "3ad395d666b488e89f4e1cef56ec8fbdf9732a18"
PARENT = "48722250860b0727c4e4668a8caccb833ca10edb"
CORE_BLOB = "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07"
QUERY_BLOB = "e8ea67310094c517b5a882d5e2e1709be975c675"
WHEEL_SHA256 = "87d1493dc592b67451ffad48a2cbc85f3cdf3ddcd8ba2abf447c21ee5ef74030"
MAX_ODD_CANDIDATES = 2_000_000
SIEVE_LIMIT = 4096
BLOCK = 65536
PROCESSES, ROUNDS, REPEATS = 5, 21, 64
FAMILIES = (
    ("case_01", "D", 2, 1, 1),
    ("case_02", "D", 2, 1, 2),
    ("case_03", "U", 2, 1, 2),
    ("case_04", "U", 2, 1, 3),
    ("case_05", "D", 4, 3, 1),
    ("case_06", "U", 4, 3, 2),
)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def checked(path, expected):
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
    assert blob(raw) == expected, (str(path), blob(raw), expected)
    return raw


def write_json(path, document):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2, ensure_ascii=True)+"\n", encoding="utf-8")


def load_queries(enterprise_root):
    checked(enterprise_root/"src/enterprise_math/core.py", CORE_BLOB)
    path = HERE/"brc_residual_candidate_families_20260908.py"
    checked(path, QUERY_BLOB)
    sys.path.insert(0, str(enterprise_root/"src"))
    from enterprise_math.core import integer_nth_root
    spec = importlib.util.spec_from_file_location("frozen_residual_queries", path)
    query = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(query)
    query.ROOT = integer_nth_root
    return query


def small_sieve_primes():
    live = bytearray(b"\1")*(SIEVE_LIMIT+1)
    live[:2] = b"\0\0"
    for p in range(2, math.isqrt(SIEVE_LIMIT)+1):
        if live[p]:
            size = (SIEVE_LIMIT-p*p)//p+1
            live[p*p::p] = b"\0"*size
    return tuple(p for p in range(3, SIEVE_LIMIT+1, 2) if live[p])


def generate_case(family, primes, fmpz):
    label, state, a, b, c = family
    coefficient = a*a
    constant = 2*a*c + (b if state == "D" else -b)
    tag = f"BRC-PROVED-2048-V1:{label}:{state}:{a}:{b}:{c}".encode("ascii")
    offset = int.from_bytes(hashlib.sha256(tag).digest()[:12], "big")
    anchor = (3*(1 << 1024))//(4*a)
    p0 = (anchor+2*offset) | 1
    stats = {"odd_candidates_sieved": 0, "sieve_survivors_tested": 0,
             "p_probable_calls": 0, "q_probable_calls": 0, "proved_calls": 0,
             "probable_filter_ns": 0, "primality_proof_ns": 0, "sieve_ns": 0}
    started = perf_counter_ns()
    for first in range(0, MAX_ODD_CANDIDATES, BLOCK):
        count = min(BLOCK, MAX_ODD_CANDIDATES-first)
        start_p = p0+2*first
        start_q = coefficient*start_p+constant
        sieve_started = perf_counter_ns()
        live = bytearray(b"\1")*count
        for ell in primes:
            first_p = (-start_p*pow(2, -1, ell)) % ell
            first_q = (-start_q*pow(2*coefficient, -1, ell)) % ell
            if first_p < count:
                live[first_p::ell] = b"\0"*((count-1-first_p)//ell+1)
            if first_q < count and first_q != first_p:
                live[first_q::ell] = b"\0"*((count-1-first_q)//ell+1)
        stats["sieve_ns"] += perf_counter_ns()-sieve_started
        stats["odd_candidates_sieved"] += count
        for index, flag in enumerate(live):
            if not flag:
                continue
            p = start_p+2*index
            q = coefficient*p+constant
            stats["sieve_survivors_tested"] += 1
            stage = perf_counter_ns()
            stats["p_probable_calls"] += 1
            possible_p = fmpz(p).is_probable_prime()
            if possible_p:
                stats["q_probable_calls"] += 1
                possible_q = fmpz(q).is_probable_prime()
            else:
                possible_q = False
            stats["probable_filter_ns"] += perf_counter_ns()-stage
            if not (possible_p and possible_q):
                continue
            print(json.dumps({"event": "prove_pair", "id": label,
                "candidate_index": first+index, "p_bits": p.bit_length(),
                "q_bits": q.bit_length()}), flush=True)
            stage = perf_counter_ns()
            p_is_prime = int(fmpz(p).is_prime())
            p_proof_ns = perf_counter_ns()-stage
            stage = perf_counter_ns()
            q_is_prime = int(fmpz(q).is_prime())
            q_proof_ns = perf_counter_ns()-stage
            stats["proved_calls"] += 2
            stats["primality_proof_ns"] += p_proof_ns+q_proof_ns
            if p_is_prime != 1 or q_is_prime != 1:
                continue
            n = p*q
            j = math.isqrt(n)
            r, gap = n-j*j, (j+1)*(j+1)-n
            assert p != q and p*q == n and n.bit_length() == 2048
            assert p > c*c and p & 1 and q & 1
            if state == "D":
                assert j == a*p+c and r == b*p-c*c and 0 < r <= j
            else:
                assert j+1 == a*p+c and gap == b*p+c*c and j < r <= 2*j
            old_center = math.gcd(n, abs(j-r))
            stats["generation_wall_ns"] = perf_counter_ns()-started
            result = {"id": label, "state": state, "a": a, "b": b, "c": c,
                "p": str(p), "q": str(q), "N": str(n), "p_bits": p.bit_length(),
                "q_bits": q.bit_length(), "N_bits": n.bit_length(),
                "decimal_sha256": digest(str(n).encode("ascii")),
                "J": str(j), "R": str(r), "A": str(gap),
                "p0": str(p0), "accepted_odd_candidate_index": first+index,
                "prime_results": {"p_is_prime": p_is_prime, "q_is_prime": q_is_prime,
                    "p_proof_ns": p_proof_ns, "q_proof_ns": q_proof_ns,
                    "method": "python-flint fmpz.is_prime -> FLINT fmpz_is_prime(proved=1)",
                    "standalone_exported_primality_certificate": False},
                "old_center_gcd": str(old_center), "stats": stats}
            print(json.dumps({"event": "accepted_proved_semiprime", "id": label,
                "N_bits": n.bit_length(), "generation_seconds": stats["generation_wall_ns"]/1e9,
                "proof_seconds": (p_proof_ns+q_proof_ns)/1e9}), flush=True)
            return result
    raise RuntimeError(f"fixed construction budget exhausted for {label}; no extension")


def generate():
    sys.path.insert(0, str(RUN/"flint_runtime"))
    import flint
    from flint import fmpz
    assert flint.__version__ == "0.8.0" and flint.__FLINT_VERSION__ == "3.3.1"
    package = json.loads((RUN/"pip_install_report.json").read_text(encoding="utf-8"))
    download = package["install"][0]["download_info"]
    assert download["archive_info"]["hashes"]["sha256"] == WHEEL_SHA256
    if GENERATION_FILE.exists():
        result = json.loads(GENERATION_FILE.read_text(encoding="utf-8"))
        assert result["schema"] == "BRC_PROVED_SEMIPRIME2048_V1"
    else:
        result = {"schema": "BRC_PROVED_SEMIPRIME2048_V1", "canonical_sha": CANONICAL,
            "project_parent": PARENT, "created_at": datetime.now(timezone.utc).isoformat(),
            "activity_id": "RA-EM-HME-0CE4FD-SEMIPRIME-20260909",
            "generation_only": {"max_odd_candidates_per_family": MAX_ODD_CANDIDATES,
                "block_size": BLOCK, "small_sieve_limit": SIEVE_LIMIT,
                "note": "bounded synthetic prime-pair construction; no factor search on an external modulus"},
            "environment": {"python": platform.python_version(), "platform": platform.platform(),
                "python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__,
                "wheel": download},
            "primality_source": {
                "binding": "flintlib/python-flint@0.8.0:src/flint/types/fmpz.pyx",
                "binding_git_blob": "6f3cf67773055f152de6c85681bc5b355688dad2",
                "implementation": "flintlib/flint@v3.3.1:src/fmpz/is_prime.c",
                "implementation_git_blob": "fef98c14962cee953e7ff802918e943187649721",
                "contract": "is_prime calls proved=1; probable-prime screening alone never admits a sample",
                "proof_receipt": "rerunnable rigorous library result; no standalone proof certificate is exported"},
            "records": []}
    primes = small_sieve_primes()
    completed = {r["id"] for r in result["records"]}
    for family in FAMILIES:
        if family[0] in completed:
            continue
        result["records"].append(generate_case(family, primes, fmpz))
        write_json(GENERATION_FILE, result)
    assert len(result["records"]) == len(FAMILIES)
    inputs = {"schema": "BRC_SYNTHETIC_N_ONLY_INPUTS_V1",
        "provenance": "six generated cases; opaque ids and N only; no p, q, root, state or family parameters",
        "cases": [{"id": r["id"], "N": r["N"]} for r in result["records"]]}
    write_json(INPUT_FILE, inputs)
    print(json.dumps({"generation_complete": True, "cases": len(result["records"]),
        "all_N_bits": [r["N_bits"] for r in result["records"]],
        "total_generation_seconds": sum(r["stats"]["generation_wall_ns"] for r in result["records"])/1e9,
        "input_sha256": digest(INPUT_FILE.read_bytes())}), flush=True)


def worker(enterprise_root, worker_index):
    query = load_queries(enterprise_root)
    # The worker reads this N-only file. It never opens GENERATION_FILE.
    inputs = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    assert inputs["schema"] == "BRC_SYNTHETIC_N_ONLY_INPUTS_V1"
    assert [r["id"] for r in inputs["cases"]] == [f"case_0{i}" for i in range(1, 7)]
    records = []
    for case_index, row in enumerate(inputs["cases"]):
        assert set(row) == {"id", "N"}
        n = int(row["N"])
        assert n.bit_length() == 2048
        variants = {"complete_residual": lambda: query._complete(n),
                    "complete_root_gate": lambda: query._complete(n, gated=True)}
        names = tuple(variants)
        if (case_index+worker_index) & 1:
            names = names[::-1]
        first_ns, expected = {}, {}
        for name in names:
            start = perf_counter_ns()
            returned = variants[name]()
            first_ns[name] = perf_counter_ns()-start
            expected[name] = returned
            assert 1 < returned[0] < n and returned[0]*returned[1] == n
        raw = {name: [] for name in variants}
        for round_index in range(ROUNDS):
            order = names if round_index % 2 == 0 else names[::-1]
            for name in order:
                start = perf_counter_ns()
                for _ in range(REPEATS):
                    returned = variants[name]()
                raw[name].append(perf_counter_ns()-start)
                assert returned == expected[name]
        records.append({"id": row["id"], "first_call_ns": first_ns, "raw_batch_ns": raw,
            "returned": {name: {"factor": str(value[0]), "cofactor": str(value[1]),
                "c": value[2], "b": value[3], "N_divisions": value[4],
                "endpoint_remainders": value[5], "small_coefficient_divisions": value[6]}
                for name, value in expected.items()}})
    write_json(RUN/f"semiprime_worker_{worker_index}.json", {"worker_index": worker_index,
        "input_sha256": digest(INPUT_FILE.read_bytes()), "records": records})


def benchmark(enterprise_root):
    source = json.loads(GENERATION_FILE.read_text(encoding="utf-8"))
    assert len(source["records"]) == 6
    load_queries(enterprise_root)
    workers = []
    for index in range(PROCESSES):
        output = RUN/f"semiprime_worker_{index}.json"
        if output.exists():
            raise RuntimeError("timing worker output already exists; preserve previous run")
        command = [sys.executable, str(Path(__file__).resolve()), "--stage", "worker",
            "--enterprise-root", str(enterprise_root), "--worker-index", str(index)]
        started = perf_counter_ns()
        process = subprocess.run(command, capture_output=True, text=True)
        elapsed = perf_counter_ns()-started
        if process.returncode:
            raise RuntimeError(process.stdout+process.stderr)
        result = json.loads(output.read_text(encoding="utf-8"))
        result["process_wall_ns"] = elapsed
        workers.append(result)
    cases = []
    for row in source["records"]:
        expected = {int(row["p"]), int(row["q"])}
        samples = [next(r for r in w["records"] if r["id"] == row["id"]) for w in workers]
        stats = {}
        for name in ("complete_residual", "complete_root_gate"):
            for sample in samples:
                result = sample["returned"][name]
                assert {int(result["factor"]), int(result["cofactor"])} == expected
            batch_averages = [t/REPEATS for s in samples for t in s["raw_batch_ns"][name]]
            first_calls = [s["first_call_ns"][name] for s in samples]
            ordered = sorted(batch_averages)
            stats[name] = {"warm_median_ns": statistics.median(batch_averages),
                "warm_batch_mean_p95_ns": ordered[math.ceil(0.95*len(ordered))-1],
                "warm_batch_mean_min_ns": min(ordered), "warm_batch_mean_max_ns": max(ordered),
                "fresh_process_first_call_median_ns": statistics.median(first_calls),
                "fresh_process_first_call_min_ns": min(first_calls),
                "fresh_process_first_call_max_ns": max(first_calls)}
        cases.append({"id": row["id"], "state": row["state"], "a": row["a"],
            "b": row["b"], "c": row["c"], "N_bits": row["N_bits"],
            "p_bits": row["p_bits"], "q_bits": row["q_bits"],
            "verified_prime_pair": True, "verified_factor_recovery": True,
            "stats": stats})
    certificate = {"schema": "BRC_PROVED_SEMIPRIME2048_TIMING_V1",
        "canonical_sha": CANONICAL, "project_parent": PARENT,
        "source_blobs": {"core.py": CORE_BLOB, "residual_query_script": QUERY_BLOB},
        "generation_sha256": digest(GENERATION_FILE.read_bytes()),
        "N_only_inputs_sha256": digest(INPUT_FILE.read_bytes()),
        "cost_contract": {"fresh_processes": PROCESSES, "paired_rounds_per_process": ROUNDS,
            "repeats_per_batch": REPEATS, "input": "one Python integer N per query",
            "query_scope": "unchanged full fixed candidate packet, not an oracle-supplied c/b or assigned candidate",
            "included": ["native integer root", "R/A and D/U preparation", "fixed candidate enumeration",
                "parity and integer quotient gates", "optional endpoint remainder", "divmod and factor product verification"],
            "excluded": ["sample generation", "primality proof", "imports", "decimal text parsing",
                "source/input checks", "process startup", "JSON output"],
            "first_call_note": "one timed first query per case/variant in each fresh Python process; not a hardware-cold-cache guarantee",
            "p95_note": "95th percentile of batch averages, not individual-call latency",
            "timing_replays_are_independent_hits": False,
            "public_challenge_inputs": 0, "external_targets": 0},
        "cases": cases, "raw_workers": workers}
    write_json(TIMING_FILE, certificate)
    print(json.dumps({"benchmark_complete": True, "cases": cases,
        "worker_process_wall_ms": [w["process_wall_ns"]/1e6 for w in workers]}, ensure_ascii=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=("generate", "benchmark", "worker"), required=True)
    parser.add_argument("--enterprise-root", type=Path, default=HERE/"native-root-checkout")
    parser.add_argument("--worker-index", type=int, choices=range(PROCESSES), default=0)
    args = parser.parse_args()
    if args.stage == "generate":
        generate()
    elif args.stage == "worker":
        worker(args.enterprise_root, args.worker_index)
    else:
        benchmark(args.enterprise_root)
