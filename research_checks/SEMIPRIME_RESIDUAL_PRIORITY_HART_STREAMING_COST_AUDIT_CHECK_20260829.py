#!/usr/bin/env python3
"""Reproduce the frozen unseen holdout for RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT.

Standard-library only.  The scheduling algorithms receive only N and the public K window.
Verifier p/q labels are loaded only after all factor-blind case metrics have been recomputed,
and are used solely to check N=p*q and the declared evaluation stratum metadata.
"""
from __future__ import annotations

import inspect
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT"
PUBLIC = ART / "frozen_holdout_public_cases_20260829.json"
LABELS = ART / "frozen_holdout_verifier_labels_20260829.json"

QR_MOD = 6720
B = 32
WINDOWS = (4, 16, 64, 256, 1024)
K_CAP = 65536

qr = bytearray(QR_MOD)
for a in range(QR_MOD):
    qr[(a * a) % QR_MOD] = 1


def ceil_cuberoot(n: int) -> int:
    lo, hi = 0, 1
    while hi * hi * hi < n:
        hi <<= 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid * mid >= n:
            hi = mid
        else:
            lo = mid
    return hi


def precompute_factor_blind(N: int, K: int):
    """Return Hart-M4 residual states; inputs are deliberately only public N,K."""
    arr = []
    for k in range(1, K + 1):
        m = 4 * k * N
        r = math.isqrt(m)
        x = r if r * r == m else r + 1
        e = x * x - m
        ok = bool(qr[e % QR_MOD])
        hit = False
        gcd_ops = 0
        if ok:
            y = math.isqrt(e)
            if y * y == e:
                g = math.gcd(x - y, N)
                gcd_ops += 1
                if 1 < g < N:
                    hit = True
                else:
                    g = math.gcd(x + y, N)
                    gcd_ops += 1
                    if 1 < g < N:
                        hit = True
        arr.append((e, x, ok, hit, gcd_ops))
    return arr


def empty_counts():
    return {"gen": 0, "mod": 0, "sq": 0, "gcd": 0, "enqueue": 0, "bucket_scan": 0, "chunks": 0}


def sim_hart_m4_asc(arr):
    c = empty_counts()
    for k, (e, x, ok, hit, gops) in enumerate(arr, 1):
        c["gen"] += 1
        c["mod"] += 1
        if not ok:
            continue
        c["sq"] += 1
        y = math.isqrt(e)
        if y * y == e:
            c["gcd"] += gops
        if hit:
            return k, c
    return None, c


def sim_bucket(arr, W: int):
    c = empty_counts()
    n = len(arr)
    for start in range(0, n, W):
        end = min(start + W, n)
        buckets = [[] for _ in range(B)]
        c["chunks"] += 1
        for j in range(start, end):
            e, x, ok, hit, gops = arr[j]
            c["gen"] += 1
            c["mod"] += 1
            if ok:
                bi = min(B - 1, (B * e) // (2 * x - 1))
                buckets[bi].append((j + 1, e, hit, gops))
                c["enqueue"] += 1
        for bucket in buckets:
            c["bucket_scan"] += 1
            for k, e, hit, gops in bucket:
                c["sq"] += 1
                y = math.isqrt(e)
                if y * y == e:
                    c["gcd"] += gops
                if hit:
                    return k, c
    return None, c


def sim_threshold_t15(arr):
    """score < 1/2 first; then deferred k-order fallback restores finite-window completeness."""
    c = empty_counts()
    deferred = []
    for k, (e, x, ok, hit, gops) in enumerate(arr, 1):
        c["gen"] += 1
        c["mod"] += 1
        if not ok:
            continue
        bi = min(B - 1, (B * e) // (2 * x - 1))
        if bi <= 15:
            c["sq"] += 1
            y = math.isqrt(e)
            if y * y == e:
                c["gcd"] += gops
            if hit:
                return k, c, "phase1"
        else:
            deferred.append((k, e, hit, gops))
            c["enqueue"] += 1
    for k, e, hit, gops in deferred:
        c["sq"] += 1
        y = math.isqrt(e)
        if y * y == e:
            c["gcd"] += gops
        if hit:
            return k, c, "fallback"
    return None, c, "nohit"


def scalar_cost(c, sq_weight=0.5):
    return (
        c["gen"]
        + c["mod"] / 64.0
        + sq_weight * c["sq"]
        + c["gcd"]
        + c["enqueue"] / 64.0
        + c["bucket_scan"] / 128.0
    )


def main() -> int:
    public = json.loads(PUBLIC.read_text(encoding="utf-8"))["cases"]
    labels = {x["case_id"]: x for x in json.loads(LABELS.read_text(encoding="utf-8"))["labels"]}
    summary_expected = json.loads((ART / "summary_20260829.json").read_text(encoding="utf-8"))["frozen_unseen_holdout"]

    # Mechanical factor-blindness guard: deployment functions must not expose p/q arguments.
    forbidden = {"p", "q", "factor", "ratio", "stratum"}
    signature_failures = []
    for fn in (precompute_factor_blind, sim_hart_m4_asc, sim_bucket, sim_threshold_t15):
        params = set(inspect.signature(fn).parameters)
        if params & forbidden:
            signature_failures.append(fn.__name__)

    metric_failures = []
    label_failures = []
    ratios = {W: [] for W in WINDOWS}
    threshold_ratios = []
    threshold_phases = {"phase1": 0, "fallback": 0, "nohit": 0}
    hart_hits = 0

    for case in public:
        cid = case["case_id"]
        N = int(case["N"])
        Kfull = ceil_cuberoot(N)
        K = min(Kfull, K_CAP)
        if Kfull != case["K_full"] or K != case["K_test"] or (K < Kfull) != case["capped"]:
            metric_failures.append([cid, "K"])
            continue

        arr = precompute_factor_blind(N, K)
        hh, hc = sim_hart_m4_asc(arr)
        if hh is not None:
            hart_hits += 1

        got = {
            "hart_m4_asc_hit_k": hh,
            "hart_m4_asc": hc,
            "bucket": {},
        }
        for W in WINDOWS:
            bh, bc = sim_bucket(arr, W)
            got["bucket"][str(W)] = {"hit_k": bh, "ops": bc}
            ratios[W].append(scalar_cost(bc) / scalar_cost(hc))

        th, tc, phase = sim_threshold_t15(arr)
        got["threshold_t15"] = {"hit_k": th, "phase": phase, "ops": tc}
        threshold_phases[phase] += 1
        threshold_ratios.append(scalar_cost(tc) / scalar_cost(hc))

        # Verifier labels are consulted only here, after factor-blind execution.
        lab = labels[cid]
        p, q = int(lab["p"]), int(lab["q"])
        if p * q != N or not (1 < p < q) or p % 2 == 0 or q % 2 == 0:
            label_failures.append(cid)

    bucket_summary = {}
    for W in WINDOWS:
        rs = sorted(ratios[W])
        bucket_summary[str(W)] = {
            "median": (rs[(len(rs)-1)//2] + rs[len(rs)//2]) / 2,
            "mean": sum(rs) / len(rs),
            "wins": sum(x < 1 for x in rs),
            "min": min(rs),
            "max": max(rs),
        }
    tr = sorted(threshold_ratios)
    threshold_summary = {
        "median": (tr[(len(tr)-1)//2] + tr[len(tr)//2]) / 2,
        "mean": sum(tr) / len(tr),
        "wins": sum(x < 1 for x in tr),
        "min": min(tr),
        "max": max(tr),
        "phases": threshold_phases,
    }

    # Recomputed aggregate must agree with the separately frozen summary.
    if hart_hits != summary_expected["hart_window_hits"] or len(public) - hart_hits != summary_expected["hart_window_nohits"]:
        metric_failures.append(["aggregate", "hart_hit_count"])
    for W in WINDOWS:
        exp = summary_expected["bucket"][str(W)]
        got = bucket_summary[str(W)]
        for key in ("median", "mean", "min", "max"):
            if abs(got[key] - exp[key]) > 1e-9:
                metric_failures.append(["aggregate", f"bucket_{W}_{key}"])
        if got["wins"] != exp["wins"]:
            metric_failures.append(["aggregate", f"bucket_{W}_wins"])
    texp = summary_expected["threshold_t15"]
    for key in ("median", "mean", "min", "max"):
        if abs(threshold_summary[key] - texp[key]) > 1e-9:
            metric_failures.append(["aggregate", f"threshold_{key}"])
    if threshold_summary["wins"] != texp["wins"]:
        metric_failures.append(["aggregate", "threshold_wins"])
    if threshold_phases["phase1"] != texp["phase1_hits"] or threshold_phases["fallback"] != texp["fallback_hits"]:
        metric_failures.append(["aggregate", "threshold_phases"])

    status = "PASS" if not signature_failures and not metric_failures and not label_failures else "FAIL"
    print(json.dumps({
        "schema": "SSMFCOST_FROZEN_HOLDOUT_CHECK_V1",
        "status": status,
        "cases": len(public),
        "hart_hits": hart_hits,
        "hart_nohits": len(public) - hart_hits,
        "signature_failures": signature_failures,
        "metric_failures": metric_failures[:10],
        "label_failures": label_failures[:10],
        "bucket_cost_ratios": bucket_summary,
        "threshold_t15_cost_ratios": threshold_summary,
    }, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
