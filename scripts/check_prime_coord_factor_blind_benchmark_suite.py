#!/usr/bin/env python3
"""PCF2 sealed factor-blind benchmark suite.

Private factor generation/verifier lives in this process. Candidate execution is
delegated to a separate worker process that receives only N, an independent
public seed, candidate id, and frozen public parameters.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

SCHEMA = "PCF2_SEALED_BENCHMARK_V1"
MANIFEST_VERSION = "PCF2_PARAMETERS_V1"
CORPUS_SEED = 0x5A17C0DE
PUBLIC_SEEDS = tuple(range(0, 64))
CANDIDATES = ("prime_fusion_public_polynomial_gcd_probe", "prime_fusion_public_sixth_power_gcd_probe")
BASELINES = ("trial_division", "fermat", "pollard_rho", "pollard_p_minus_1")
FORBIDDEN_PUBLIC_TOKENS = {
    "p", "q", "factor", "factors", "factorization", "hidden_factor",
    "idempotent", "m_pq", "root_mod_p", "root_mod_q", "phase_p", "phase_q",
    "factor_coordinate", "factor_label",
}
FORBIDDEN_CONTROL_TOKENS = {
    "adaptive", "postselect", "postselection", "answer_dependent", "on_failure_seed",
    "factor_derived", "hidden",
}

PARAMETER_MANIFEST = {
    "schema": MANIFEST_VERSION,
    "public_seeds": list(PUBLIC_SEEDS),
    "candidate_parameters": {
        "prime_fusion_public_polynomial_gcd_probe": {"polynomials": ["x^2+1", "x^2+x+1"]},
        "prime_fusion_public_sixth_power_gcd_probe": {"polynomials": ["x^6-1", "x^6+1"]},
    },
    "baseline_parameters": {
        "trial_division": {"odd_step": 2},
        "fermat": {"max_steps": 4096},
        "pollard_rho": {"seeds": [2, 3, 5, 7, 11], "max_steps_per_seed": 4096},
        "pollard_p_minus_1": {"bases": [2, 3, 5, 7], "B1": 256},
    },
    "cost_model": {
        "candidate": "count modular multiplications/exponentiation calls/gcd calls; memory_bits=live_integer_slots*bit_length(N)",
        "baseline": "algorithm-specific exact loop counters plus gcd/modexp counts; no wall-clock claims",
    },
}

@dataclass(frozen=True)
class PublicCase:
    case_id: str
    n: int
    family: str
    bit_length: int
    band: str

@dataclass(frozen=True)
class PrivateCase:
    public: PublicCase
    factors: tuple[int, ...]

@dataclass
class AlgoResult:
    algorithm: str
    success: bool
    factor: int | None
    ops: int
    gcd_calls: int
    seeds_used: int
    memory_bits: int
    failure_class: str | None
    extra: dict[str, Any]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n: int) -> int:
    n = max(2, n)
    if n == 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n


def prev_prime(n: int) -> int:
    n = max(2, n)
    if n == 2:
        return 2
    if n % 2 == 0:
        n -= 1
    while n >= 2 and not is_prime(n):
        n -= 2
    if n < 2:
        raise ValueError("no prime")
    return n


def factor_small(n: int) -> tuple[int, ...]:
    """Private verifier-only exact factorization for the bounded benchmark corpus."""
    out: list[int] = []
    x = n
    d = 2
    while d * d <= x:
        while x % d == 0:
            out.append(d)
            x //= d
        d = 3 if d == 2 else d + 2
    if x > 1:
        out.append(x)
    return tuple(out)


def band_name(bits: int) -> str:
    if bits <= 12:
        return "B05_12"
    if bits <= 16:
        return "B13_16"
    if bits <= 20:
        return "B17_20"
    return "B21_PLUS"


def _add_case(out: list[PrivateCase], seen: set[int], case_id: str, n: int, family: str, factors: tuple[int, ...]) -> None:
    if n in seen or n <= 3 or len(factors) < 2:
        return
    assert math.prod(factors) == n
    seen.add(n)
    pub = PublicCase(case_id=case_id, n=n, family=family, bit_length=n.bit_length(), band=band_name(n.bit_length()))
    out.append(PrivateCase(pub, tuple(sorted(factors))))


def build_corpus() -> list[PrivateCase]:
    """Deterministic private generator; candidate worker never receives factors."""
    rng = random.Random(CORPUS_SEED)
    out: list[PrivateCase] = []
    seen: set[int] = set()
    case_i = 0

    for bits in (10, 12, 14, 16, 18, 20):
        half = bits // 2
        for k in range(4):
            base = (1 << (half - 1)) + rng.randrange(1, max(3, 1 << max(1, half - 2)))
            p = next_prime(base)
            q = next_prime(p + 2 + 2 * k)
            if p == q:
                q = next_prime(q + 2)
            n = p * q
            case_i += 1
            _add_case(out, seen, f"C{case_i:04d}", n, "balanced_semiprime", (p, q))

        for k in range(3):
            pb = max(3, bits // 4)
            qb = max(4, bits - pb)
            p = next_prime((1 << (pb - 1)) + 2 * k + 1)
            q = next_prime((1 << (qb - 1)) + rng.randrange(1, 1 << max(1, qb - 3)))
            if p == q:
                q = next_prime(q + 2)
            n = p * q
            case_i += 1
            _add_case(out, seen, f"C{case_i:04d}", n, "unbalanced_semiprime", (p, q))

        for k in range(3):
            center = (1 << (half - 1)) + rng.randrange(5, max(7, 1 << max(2, half - 2)))
            p = next_prime(center)
            q = next_prime(p + 2)
            n = p * q
            case_i += 1
            _add_case(out, seen, f"C{case_i:04d}", n, "near_twin_semiprime", (p, q))

        p = next_prime((1 << max(2, bits // 3 - 1)) + 1)
        e = 2
        while (p ** (e + 1)).bit_length() <= bits:
            e += 1
        e = max(2, e)
        n = p ** e
        case_i += 1
        _add_case(out, seen, f"C{case_i:04d}", n, "prime_power", tuple([p] * e))

        p = next_prime((1 << max(2, bits // 5 - 1)) + 1)
        q = next_prime(p + 4)
        r = next_prime((1 << max(3, bits // 2 - 1)) + rng.randrange(1, 8))
        n = p * q * r
        case_i += 1
        _add_case(out, seen, f"C{case_i:04d}", n, "multi_prime", (p, q, r))

    for n in (561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341):
        case_i += 1
        _add_case(out, seen, f"C{case_i:04d}", n, "carmichael", factor_small(n))

    for n in (2047, 3277, 4033, 4681, 8321, 15841, 29341, 42799, 49141, 52633):
        if _is_strong_pseudoprime_base2(n):
            case_i += 1
            _add_case(out, seen, f"C{case_i:04d}", n, "strong_pseudoprime_base2", factor_small(n))

    collision_ns: list[int] = []
    for s in PUBLIC_SEEDS:
        if s < 2:
            continue
        vals = (s*s + 1, s*s + s + 1, s**6 - 1, s**6 + 1)
        for v in vals:
            if v <= 3:
                continue
            fac = factor_small(abs(v))
            if len(fac) >= 2 and abs(v) % 2 == 1 and abs(v).bit_length() <= 22:
                collision_ns.append(abs(v))
        if len(set(collision_ns)) >= 12:
            break
    for n in sorted(set(collision_ns))[:12]:
        case_i += 1
        _add_case(out, seen, f"C{case_i:04d}", n, "coordinate_collision", factor_small(n))

    required = {
        "balanced_semiprime", "unbalanced_semiprime", "near_twin_semiprime",
        "prime_power", "multi_prime", "carmichael", "strong_pseudoprime_base2",
        "coordinate_collision",
    }
    got = {c.public.family for c in out}
    assert required <= got, (required - got)
    return out


def _is_strong_pseudoprime_base2(n: int) -> bool:
    if n < 3 or n % 2 == 0 or is_prime(n):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    x = pow(2, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
    return False


def verify_nontrivial_divisor(n: int, d: int | None) -> bool:
    return d is not None and 1 < d < n and n % d == 0


def run_worker_batch(worker: Path, requests: list[dict[str, Any]]) -> list[dict[str, Any]]:
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0"}
    payload = "".join(json.dumps(req, sort_keys=True) + "\n" for req in requests)
    proc = subprocess.run(
        [sys.executable, str(worker), "--worker"],
        input=payload,
        text=True,
        capture_output=True,
        check=False,
        env=env,
        timeout=10,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"worker failed rc={proc.returncode}: {proc.stderr.strip()} / {proc.stdout.strip()}")
    outs = [json.loads(line) for line in proc.stdout.splitlines() if line.strip()]
    if len(outs) != len(requests):
        raise RuntimeError(f"worker response count mismatch: {len(outs)} != {len(requests)}")
    assert all(out["schema"] == "PCF2_CANDIDATE_RESPONSE_V1" for out in outs)
    return outs


def benchmark_candidate(worker: Path, candidate_id: str, public: PublicCase) -> AlgoResult:
    params = PARAMETER_MANIFEST["candidate_parameters"][candidate_id]
    requests = [
        {
            "schema": "PCF2_CANDIDATE_REQUEST_V1",
            "candidate_id": candidate_id,
            "n": public.n,
            "seed": seed,
            "public_parameters": params,
        }
        for seed in PUBLIC_SEEDS
    ]
    responses = run_worker_batch(worker, requests)
    outcomes = []
    total_ops = 0
    total_gcd = 0
    peak_mem = 0
    factor = None
    earliest = None
    saw_sync = False
    for idx, (seed, r) in enumerate(zip(PUBLIC_SEEDS, responses), start=1):
        total_ops += int(r["ops"])
        total_gcd += int(r["gcd_calls"])
        peak_mem = max(peak_mem, int(r["memory_bits"]))
        for d in r["gcd_outputs"]:
            d = int(d)
            if d == public.n:
                saw_sync = True
            if factor is None and verify_nontrivial_divisor(public.n, d):
                factor = d
                earliest = idx
        outcomes.append((seed, tuple(int(x) for x in r["gcd_outputs"])))
    if factor is not None:
        failure = None
    elif saw_sync:
        failure = "SYNCHRONIZED_OR_TRIVIAL_ONLY"
    else:
        failure = "NO_NONTRIVIAL_GCD_IN_PUBLIC_SEED_BUDGET"
    return AlgoResult(
        algorithm=candidate_id,
        success=factor is not None,
        factor=factor,
        ops=total_ops,
        gcd_calls=total_gcd,
        seeds_used=earliest or len(PUBLIC_SEEDS),
        memory_bits=peak_mem,
        failure_class=failure,
        extra={"seed_budget": len(PUBLIC_SEEDS)},
    )


def baseline_trial_division(n: int) -> AlgoResult:
    bits = n.bit_length()
    ops = 0
    if n % 2 == 0:
        return AlgoResult("trial_division", True, 2, 1, 0, 0, 3*bits, None, {})
    d = 3
    while d * d <= n:
        ops += 1
        if n % d == 0:
            return AlgoResult("trial_division", True, d, ops, 0, 0, 3*bits, None, {})
        d += 2
    return AlgoResult("trial_division", False, None, ops, 0, 0, 3*bits, "NO_FACTOR_BELOW_SQRT", {})


def baseline_fermat(n: int) -> AlgoResult:
    bits = n.bit_length()
    max_steps = PARAMETER_MANIFEST["baseline_parameters"]["fermat"]["max_steps"]
    if n % 2 == 0:
        return AlgoResult("fermat", True, 2, 1, 0, 0, 5*bits, None, {"steps": 0})
    a = math.isqrt(n)
    if a*a < n:
        a += 1
    steps = 0
    while steps <= max_steps:
        b2 = a*a - n
        b = math.isqrt(b2)
        if b*b == b2:
            d = math.gcd(a-b, n)
            if verify_nontrivial_divisor(n, d):
                return AlgoResult("fermat", True, d, steps+1, 1, 0, 5*bits, None, {"steps": steps})
        a += 1
        steps += 1
    return AlgoResult("fermat", False, None, steps, 0, 0, 5*bits, "STEP_BUDGET_EXHAUSTED", {"steps": steps})


def baseline_pollard_rho(n: int) -> AlgoResult:
    bits = n.bit_length()
    pars = PARAMETER_MANIFEST["baseline_parameters"]["pollard_rho"]
    if n % 2 == 0:
        return AlgoResult("pollard_rho", True, 2, 1, 0, 1, 8*bits, None, {})
    ops = gcd_calls = 0
    for attempt, seed in enumerate(pars["seeds"], start=1):
        x = seed % n
        y = x
        c = (seed * seed + 1) % n
        for step in range(pars["max_steps_per_seed"]):
            x = (x*x + c) % n
            y = (y*y + c) % n
            y = (y*y + c) % n
            ops += 3
            d = math.gcd(abs(x-y), n)
            gcd_calls += 1
            if 1 < d < n:
                return AlgoResult("pollard_rho", True, d, ops, gcd_calls, attempt, 8*bits, None, {"seed": seed, "steps": step+1})
            if d == n:
                break
    return AlgoResult("pollard_rho", False, None, ops, gcd_calls, len(pars["seeds"]), 8*bits, "SEED_BUDGET_EXHAUSTED", {})


def baseline_pollard_pm1(n: int) -> AlgoResult:
    bits = n.bit_length()
    pars = PARAMETER_MANIFEST["baseline_parameters"]["pollard_p_minus_1"]
    ops = gcd_calls = 0
    for attempt, base in enumerate(pars["bases"], start=1):
        a = base % n
        for j in range(2, pars["B1"] + 1):
            a = pow(a, j, n)
            ops += 1
        d = math.gcd(a - 1, n)
        gcd_calls += 1
        if verify_nontrivial_divisor(n, d):
            return AlgoResult("pollard_p_minus_1", True, d, ops, gcd_calls, attempt, 5*bits, None, {"base": base, "B1": pars["B1"]})
    return AlgoResult("pollard_p_minus_1", False, None, ops, gcd_calls, len(pars["bases"]), 5*bits, "B1_BASE_BUDGET_EXHAUSTED", {"B1": pars["B1"]})


def run_baseline(name: str, n: int) -> AlgoResult:
    if name == "trial_division":
        return baseline_trial_division(n)
    if name == "fermat":
        return baseline_fermat(n)
    if name == "pollard_rho":
        return baseline_pollard_rho(n)
    if name == "pollard_p_minus_1":
        return baseline_pollard_pm1(n)
    raise KeyError(name)


def leakage_tests(worker: Path) -> dict[str, Any]:
    base = {
        "schema": "PCF2_CANDIDATE_REQUEST_V1",
        "candidate_id": CANDIDATES[0],
        "n": 77,
        "seed": 2,
        "public_parameters": PARAMETER_MANIFEST["candidate_parameters"][CANDIDATES[0]],
    }
    attacks = [
        {**base, "factors": [7, 11]},
        {**base, "p": 7},
        {**base, "q": 11},
        {**base, "public_parameters": {"factorization": [7, 11]}},
        {**base, "public_parameters": {"nested": {"phase_p": 3}}},
        {**base, "public_parameters": {"adaptive": True}},
    ]
    rejected = 0
    for payload in attacks:
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0"}
        proc = subprocess.run(
            [sys.executable, str(worker), "--worker"],
            input=json.dumps(payload, sort_keys=True) + "\n",
            text=True,
            capture_output=True,
            check=False,
            env=env,
            timeout=10,
        )
        if proc.returncode != 0:
            rejected += 1
    assert rejected == len(attacks), (rejected, len(attacks))

    payload = base
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0"}
    a = subprocess.run([sys.executable, str(worker), "--worker"], input=json.dumps(payload, sort_keys=True)+"\n",
                       text=True, capture_output=True, check=True, env=env, timeout=10).stdout
    b = subprocess.run([sys.executable, str(worker), "--worker"], input=json.dumps(payload, sort_keys=True)+"\n",
                       text=True, capture_output=True, check=True, env=env, timeout=10).stdout
    assert a == b
    return {"deliberate_attacks": len(attacks), "rejected": rejected, "deterministic_replay": True}


def summarize(rows: list[dict[str, Any]], corpus: list[PrivateCase]) -> dict[str, Any]:
    algs = sorted({r["algorithm"] for r in rows})
    families = sorted({c.public.family for c in corpus})
    summary: dict[str, Any] = {}
    for alg in algs:
        rr = [r for r in rows if r["algorithm"] == alg]
        succ = [r for r in rr if r["success"]]
        fam = {}
        for f in families:
            x = [r for r in rr if r["family"] == f]
            fam[f] = {
                "cases": len(x),
                "successes": sum(bool(r["success"]) for r in x),
                "failures": len(x) - sum(bool(r["success"]) for r in x),
            }
        total_ops = sum(int(r["ops"]) for r in rr)
        total_pre = sum(int(r.get("preprocessing_ops", 0)) for r in rr)
        success_seed_total = sum(int(r["seeds_used"]) for r in succ)
        summary[alg] = {
            "cases": len(rr),
            "successes": len(succ),
            "success_rate_num": len(succ),
            "success_rate_den": len(rr),
            "total_ops": total_ops,
            "total_preprocessing_ops": total_pre,
            "amortized_ops_per_success": {"numerator": total_ops + total_pre, "denominator": len(succ)},
            "successful_seed_amplification": {"numerator": success_seed_total, "denominator": len(succ)},
            "total_gcd_calls": sum(int(r["gcd_calls"]) for r in rr),
            "max_memory_bits": max((int(r["memory_bits"]) for r in rr), default=0),
            "failure_classes": dict(sorted(Counter(r["failure_class"] for r in rr if r["failure_class"]).items())),
            "by_family": fam,
        }
    return summary


def benchmark_candidates_all(worker: Path, corpus: list[PrivateCase]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for candidate_id in CANDIDATES:
        params = PARAMETER_MANIFEST["candidate_parameters"][candidate_id]
        requests: list[dict[str, Any]] = []
        for case in corpus:
            for seed in PUBLIC_SEEDS:
                requests.append({
                    "schema": "PCF2_CANDIDATE_REQUEST_V1",
                    "candidate_id": candidate_id,
                    "n": case.public.n,
                    "seed": seed,
                    "public_parameters": params,
                })
        responses = run_worker_batch(worker, requests)
        pos = 0
        for case in corpus:
            pub = case.public
            chunk = responses[pos:pos+len(PUBLIC_SEEDS)]
            pos += len(PUBLIC_SEEDS)
            total_ops = sum(int(r["ops"]) for r in chunk)
            total_gcd = sum(int(r["gcd_calls"]) for r in chunk)
            peak_mem = max(int(r["memory_bits"]) for r in chunk)
            factor = None
            earliest = None
            saw_sync = False
            for idx, r in enumerate(chunk, start=1):
                for d0 in r["gcd_outputs"]:
                    d = int(d0)
                    if d == pub.n:
                        saw_sync = True
                    if factor is None and verify_nontrivial_divisor(pub.n, d):
                        factor = d
                        earliest = idx
            if factor is not None:
                failure = None
            elif saw_sync:
                failure = "SYNCHRONIZED_OR_TRIVIAL_ONLY"
            else:
                failure = "NO_NONTRIVIAL_GCD_IN_PUBLIC_SEED_BUDGET"
            result = AlgoResult(
                algorithm=candidate_id,
                success=factor is not None,
                factor=factor,
                ops=total_ops,
                gcd_calls=total_gcd,
                seeds_used=earliest or len(PUBLIC_SEEDS),
                memory_bits=peak_mem,
                failure_class=failure,
                extra={"seed_budget": len(PUBLIC_SEEDS)},
            )
            row = asdict(result)
            row.update({"case_id": pub.case_id, "n": pub.n, "family": pub.family, "bit_length": pub.bit_length, "band": pub.band, "kind": "enterprise_candidate", "preprocessing_ops": 0})
            rows.append(row)
        assert pos == len(responses)
    return rows


def build_replay(worker: Path) -> dict[str, Any]:
    corpus = build_corpus()
    public_corpus = [asdict(c.public) for c in corpus]
    private_digest = hashlib.sha256(
        json.dumps(
            [{"case_id": c.public.case_id, "n": c.public.n, "factors": c.factors} for c in corpus],
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()
    public_digest = hashlib.sha256(
        json.dumps(public_corpus, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    manifest_digest = hashlib.sha256(
        json.dumps(PARAMETER_MANIFEST, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    leak = leakage_tests(worker)
    rows: list[dict[str, Any]] = benchmark_candidates_all(worker, corpus)
    for case in corpus:
        pub = case.public
        for base in BASELINES:
            res = run_baseline(base, pub.n)
            assert (not res.success) or verify_nontrivial_divisor(pub.n, res.factor)
            row = asdict(res)
            row.update({"case_id": pub.case_id, "n": pub.n, "family": pub.family, "bit_length": pub.bit_length, "band": pub.band, "kind": "classical_baseline", "preprocessing_ops": 0})
            rows.append(row)

    success_count = sum(bool(r["success"]) for r in rows)
    for r in rows:
        if r["success"]:
            assert verify_nontrivial_divisor(int(r["n"]), int(r["factor"]))

    required_families = sorted({c.public.family for c in corpus})
    bands = sorted({c.public.band for c in corpus})
    report = {
        "schema": SCHEMA,
        "verdict": "BENCHMARK_FROZEN_AND_SEALED",
        "parameter_manifest": PARAMETER_MANIFEST,
        "parameter_manifest_sha256": manifest_digest,
        "corpus": {
            "cases": len(corpus),
            "families": required_families,
            "bands": bands,
            "public_sha256": public_digest,
            "private_verifier_sha256": private_digest,
            "private_factors_serialized_to_worker": False,
        },
        "leakage_tests": leak,
        "verification": {
            "rows": len(rows),
            "successful_splits": success_count,
            "all_successes_exactly_divide_n": True,
            "worker_top_level_schema_exact": True,
        },
        "summary": summarize(rows, corpus),
        "public_corpus": public_corpus,
        "rows": rows,
    }
    return report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--worker", default=str(Path(__file__).with_name("check_prime_coord_factor_blind_benchmark_suite_independent.py")))
    ap.add_argument("--out", default="")
    ap.add_argument("--compact", action="store_true")
    args = ap.parse_args()
    report = build_replay(Path(args.worker))
    text = json.dumps(report, sort_keys=True, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    print(json.dumps({
        "schema": report["schema"],
        "verdict": report["verdict"],
        "cases": report["corpus"]["cases"],
        "families": report["corpus"]["families"],
        "bands": report["corpus"]["bands"],
        "rows": report["verification"]["rows"],
        "successful_splits": report["verification"]["successful_splits"],
        "leakage_rejected": report["leakage_tests"]["rejected"],
        "summary": {
            k: {
                "successes": v["successes"],
                "cases": v["cases"],
                "total_ops": v["total_ops"],
                "failure_classes": v["failure_classes"],
            } for k, v in report["summary"].items()
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
