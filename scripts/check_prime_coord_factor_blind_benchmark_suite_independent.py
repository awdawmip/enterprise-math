#!/usr/bin/env python3
"""PCF2 sealed candidate worker and independent interface checker.

This process accepts exactly (N, independent seed, candidate id, public parameters).
It contains no corpus factor ledger and no verifier-side factor inputs.
"""
from __future__ import annotations

import json
import math
import sys
from types import MappingProxyType
from typing import Any

ALLOWED_TOP_KEYS = frozenset({"schema", "candidate_id", "n", "seed", "public_parameters"})
FORBIDDEN_PUBLIC_TOKENS = frozenset({
    "p", "q", "factor", "factors", "factorization", "hidden_factor",
    "idempotent", "m_pq", "root_mod_p", "root_mod_q", "phase_p", "phase_q",
    "factor_coordinate", "factor_label",
})
FORBIDDEN_CONTROL_TOKENS = frozenset({
    "adaptive", "postselect", "postselection", "answer_dependent", "on_failure_seed",
    "factor_derived", "hidden",
})
CANDIDATES = frozenset({
    "prime_fusion_public_polynomial_gcd_probe",
    "prime_fusion_public_sixth_power_gcd_probe",
})


def _validate_public(obj: Any, path: str = "public_parameters") -> Any:
    if isinstance(obj, dict):
        clean = {}
        for k, v in obj.items():
            if not isinstance(k, str):
                raise ValueError("public parameter keys must be strings")
            norm = k.strip().lower()
            if norm in FORBIDDEN_PUBLIC_TOKENS or norm in FORBIDDEN_CONTROL_TOKENS:
                raise ValueError(f"forbidden public field: {path}.{k}")
            if "factor" in norm or norm.startswith("phase_") or norm.startswith("root_mod_") or norm == "m_pq":
                raise ValueError(f"factor-derived public field: {path}.{k}")
            clean[k] = _validate_public(v, f"{path}.{k}")
        return MappingProxyType(clean)
    if isinstance(obj, list):
        return tuple(_validate_public(v, path) for v in obj)
    if isinstance(obj, (str, int, bool)) or obj is None:
        return obj
    raise ValueError("unsupported public parameter type")


def _poly_probe(n: int, seed: int) -> tuple[list[int], int, int, int]:
    x = seed % n
    vals = ((x*x + 1) % n, (x*x + x + 1) % n)
    gcds = [math.gcd(n, v) for v in vals]
    return gcds, 3, 2, 5 * n.bit_length()


def _sixth_probe(n: int, seed: int) -> tuple[list[int], int, int, int]:
    x = seed % n
    x2 = (x*x) % n
    x3 = (x2*x) % n
    x6 = (x3*x3) % n
    vals = ((x6 - 1) % n, (x6 + 1) % n)
    gcds = [math.gcd(n, v) for v in vals]
    return gcds, 3, 2, 6 * n.bit_length()


def run(req: dict[str, Any]) -> dict[str, Any]:
    if set(req) != ALLOWED_TOP_KEYS:
        raise ValueError("candidate request has forbidden or missing top-level fields")
    if req.get("schema") != "PCF2_CANDIDATE_REQUEST_V1":
        raise ValueError("bad request schema")
    candidate_id = req["candidate_id"]
    if candidate_id not in CANDIDATES:
        raise ValueError("unknown candidate")
    n = req["n"]
    seed = req["seed"]
    if not isinstance(n, int) or not isinstance(seed, int) or n <= 1 or seed < 0:
        raise ValueError("invalid N/seed")
    public_parameters = _validate_public(req["public_parameters"])
    _ = public_parameters
    if candidate_id == "prime_fusion_public_polynomial_gcd_probe":
        gcds, ops, gcd_calls, memory_bits = _poly_probe(n, seed)
    else:
        gcds, ops, gcd_calls, memory_bits = _sixth_probe(n, seed)
    return {
        "schema": "PCF2_CANDIDATE_RESPONSE_V1",
        "candidate_id": candidate_id,
        "n": n,
        "seed": seed,
        "gcd_outputs": gcds,
        "ops": ops,
        "gcd_calls": gcd_calls,
        "memory_bits": memory_bits,
    }


def independent_verify_report(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        report = json.load(fh)
    if report.get("schema") != "PCF2_SEALED_BENCHMARK_V1":
        raise ValueError("bad report schema")
    if report.get("verdict") != "BENCHMARK_FROZEN_AND_SEALED":
        raise ValueError("unexpected verdict")
    required_families = {
        "balanced_semiprime", "unbalanced_semiprime", "near_twin_semiprime",
        "prime_power", "multi_prime", "carmichael", "strong_pseudoprime_base2",
        "coordinate_collision",
    }
    got_families = set(report["corpus"]["families"])
    if not required_families <= got_families:
        raise ValueError("missing required family")
    if len(report["corpus"]["bands"]) < 3:
        raise ValueError("insufficient bit-length bands")
    if report["corpus"].get("private_factors_serialized_to_worker") is not False:
        raise ValueError("private factor serialization boundary failed")
    allowed_public_case_keys = {"case_id", "n", "family", "bit_length", "band"}
    for case in report["public_corpus"]:
        if set(case) != allowed_public_case_keys:
            raise ValueError("public corpus contains extra/leaky field")
        if not isinstance(case["n"], int) or case["n"] <= 1:
            raise ValueError("bad public N")
    algorithms = set()
    exact_successes = 0
    for row in report["rows"]:
        algorithms.add(row["algorithm"])
        n = int(row["n"])
        d = row["factor"]
        if row["success"]:
            if d is None:
                raise ValueError("success without factor")
            d = int(d)
            if not (1 < d < n and n % d == 0):
                raise ValueError("false split")
            exact_successes += 1
        elif d is not None:
            raise ValueError("failure row carries factor")
    required_algs = {
        "prime_fusion_public_polynomial_gcd_probe",
        "prime_fusion_public_sixth_power_gcd_probe",
        "trial_division", "fermat", "pollard_rho", "pollard_p_minus_1",
    }
    if algorithms != required_algs:
        raise ValueError("algorithm set mismatch")
    leak = report["leakage_tests"]
    if leak.get("rejected") != leak.get("deliberate_attacks") or leak.get("rejected", 0) < 6:
        raise ValueError("leakage rejection suite incomplete")
    if leak.get("deterministic_replay") is not True:
        raise ValueError("worker replay nondeterministic")
    recounted = {}
    for alg in sorted(required_algs):
        rr = [r for r in report["rows"] if r["algorithm"] == alg]
        successes = sum(bool(r["success"]) for r in rr)
        total_ops = sum(int(r["ops"]) for r in rr)
        total_pre = sum(int(r.get("preprocessing_ops", 0)) for r in rr)
        seed_total = sum(int(r["seeds_used"]) for r in rr if r["success"])
        recounted[alg] = {
            "cases": len(rr),
            "successes": successes,
            "total_ops": total_ops,
            "total_preprocessing_ops": total_pre,
            "successful_seed_total": seed_total,
        }
        summ = report["summary"][alg]
        if (
            recounted[alg]["cases"] != summ["cases"]
            or recounted[alg]["successes"] != summ["successes"]
            or recounted[alg]["total_ops"] != summ["total_ops"]
            or recounted[alg]["total_preprocessing_ops"] != summ["total_preprocessing_ops"]
            or summ["amortized_ops_per_success"] != {"numerator": total_ops + total_pre, "denominator": successes}
            or summ["successful_seed_amplification"] != {"numerator": seed_total, "denominator": successes}
        ):
            raise ValueError("aggregate mismatch")
    return {
        "schema": "PCF2_INDEPENDENT_REPORT_VERIFY_V1",
        "cases": report["corpus"]["cases"],
        "rows": len(report["rows"]),
        "exact_successes": exact_successes,
        "families": sorted(got_families),
        "bands": report["corpus"]["bands"],
        "leakage_rejected": leak["rejected"],
        "algorithms": sorted(algorithms),
        "recounted": recounted,
        "status": "PASS",
    }


def worker_main() -> None:
    saw = False
    for raw in sys.stdin:
        if not raw.strip():
            continue
        saw = True
        try:
            req = json.loads(raw)
            out = run(req)
        except Exception as exc:
            print(json.dumps({"schema": "PCF2_CANDIDATE_REJECTION_V1", "error": type(exc).__name__, "message": str(exc)}, sort_keys=True))
            raise SystemExit(2)
        print(json.dumps(out, sort_keys=True, separators=(",", ":")))
    if not saw:
        raise SystemExit("missing request")


def main() -> None:
    if sys.argv[1:] == ["--worker"]:
        worker_main()
        return
    if len(sys.argv) == 3 and sys.argv[1] == "--verify-report":
        print(json.dumps(independent_verify_report(sys.argv[2]), sort_keys=True))
        return
    raise SystemExit("usage: --worker | --verify-report PATH")


if __name__ == "__main__":
    main()
