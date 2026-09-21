#!/usr/bin/env python3
"""Verify the predeclared CFD A/B/C native-run manifest.

Stdlib-only. This is a design/manifest verifier, not a spectralDNS host run.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

ORDERS = ["ABC", "BCA", "CAB", "ACB", "CBA", "BAC"]

def sign_tail(n: int, k: int) -> Fraction:
    return sum((Fraction(math.comb(n, j), 2**n) for j in range(k, n + 1)), Fraction())

def threshold(n: int, alpha: Fraction) -> int:
    for k in range(n + 1):
        if sign_tail(n, k) <= alpha:
            return k
    raise AssertionError("no threshold")

def expected_cycles(seed: str):
    out = []
    for c in range(4):
        out.append(sorted(
            ORDERS,
            key=lambda order: hashlib.sha256(
                f"{seed}|cycle={c}|order={order}".encode("utf-8")
            ).hexdigest(),
        ))
    return out

def evaluate_run(m, rows, one_time_costs=None):
    """Fail-closed acceptance evaluator for completed native rows.

    `rows` must contain exactly 24 triplet dicts with A_total_ms/B_total_ms/
    C_total_ms, B_sparse_calls, C_sparse_calls, correctness_ok.
    Ties remain in n and count as non-success.
    """
    if len(rows) != 24:
        return {"accept": False, "reason": "expected exactly 24 scheduled triplets"}
    ids = [r["triplet"] for r in rows]
    if ids != list(range(1, 25)):
        return {"accept": False, "reason": "triplet IDs/order mismatch"}
    if not all(bool(r.get("correctness_ok")) for r in rows):
        return {"accept": False, "reason": "correctness gate failed"}
    if not all(int(r.get("B_sparse_calls", 0)) >= 1 for r in rows):
        return {"accept": False, "reason": "B failed sparse-route requirement"}
    if not all(int(r.get("C_sparse_calls", -1)) == 0 for r in rows):
        return {"accept": False, "reason": "C executed sparse route"}
    eps = float(m["ties_and_effect"]["directional_epsilon_ms"])
    ab = [float(r["A_total_ms"]) - float(r["B_total_ms"]) for r in rows]
    cb = [float(r["C_total_ms"]) - float(r["B_total_ms"]) for r in rows]
    ac = [float(r["A_total_ms"]) - float(r["C_total_ms"]) for r in rows]
    ab_pos = sum(x > eps for x in ab)
    cb_pos = sum(x > eps for x in cb)
    ac_pos = sum(x > eps for x in ac)
    req = int(m["statistics"]["confirmatory_positive_required"])
    veto = int(m["statistics"]["negative_control_positive_veto_at_or_above"])
    if ab_pos < req:
        return {"accept": False, "reason": "A-B sign gate failed", "AB_positive": ab_pos}
    if cb_pos < req:
        return {"accept": False, "reason": "C-B sign gate failed", "CB_positive": cb_pos}
    if ac_pos >= veto:
        return {"accept": False, "reason": "A-C negative-control veto", "AC_positive": ac_pos}
    oc = one_time_costs or {"A": 0.0, "B": 0.0, "C": 0.0}
    horizon = {
        arm: sum(float(r[f"{arm}_total_ms"]) for r in rows) + float(oc.get(arm, 0.0))
        for arm in "ABC"
    }
    if not (horizon["A"] > horizon["B"] and horizon["C"] > horizon["B"]):
        return {"accept": False, "reason": "fully charged horizon gate failed", "horizon_ms": horizon}
    return {
        "accept": True,
        "AB_positive": ab_pos,
        "CB_positive": cb_pos,
        "AC_positive": ac_pos,
        "horizon_ms": horizon,
    }

def verify_manifest(m):
    assert m["schema"] == "CFD_NATIVE_RUN_MANIFEST_V1"
    s = m["sampling"]
    assert s["scheduled_triplets"] == 24
    assert s["cycles"] == 4
    assert s["orders_per_cycle"] == 6
    exp = expected_cycles(s["seed_material"])
    assert s["cycle_orders"] == exp
    flat = [o for cycle in exp for o in cycle]
    assert [r["order"] for r in s["schedule"]] == flat
    assert [r["triplet"] for r in s["schedule"]] == list(range(1,25))
    assert [r["cycle"] for r in s["schedule"]] == [i for i in range(1,5) for _ in range(6)]
    for cycle in exp:
        assert sorted(cycle) == sorted(ORDERS)
        pos = {a: Counter() for a in "ABC"}
        pred = Counter()
        for o in cycle:
            for p,a in enumerate(o):
                pos[a][p] += 1
            for x,y in itertools.permutations("ABC",2):
                pred[(x,y)] += o.index(x) < o.index(y)
        assert all(pos[a][p] == 2 for a in "ABC" for p in range(3))
        assert all(pred[(x,y)] == 3 for x,y in itertools.permutations("ABC",2))
    pos = {a: Counter() for a in "ABC"}
    pred = Counter()
    for o in flat:
        for p,a in enumerate(o):
            pos[a][p] += 1
        for x,y in itertools.permutations("ABC",2):
            pred[(x,y)] += o.index(x) < o.index(y)
    assert all(pos[a][p] == 8 for a in "ABC" for p in range(3))
    assert all(pred[(x,y)] == 12 for x,y in itertools.permutations("ABC",2))

    assert m["ties_and_effect"]["directional_epsilon_ms"] == 0.0
    assert m["sampling"]["no_repeat_replacement"] is True
    assert threshold(24, Fraction(25,1000)) == 18
    assert sign_tail(24,18) == Fraction(190051,16777216)
    assert sign_tail(24,17) == Fraction(536155,16777216)
    assert threshold(24, Fraction(5,100)) == 17
    assert m["statistics"]["confirmatory_positive_required"] == 18
    assert m["statistics"]["negative_control_positive_veto_at_or_above"] == 17

    rows=[]
    for i in range(24):
        B=100.0
        A=101.0 if i < 18 else 99.0
        C=101.0 if i >= 6 else 99.0
        rows.append({
            "triplet":i+1, "A_total_ms":A, "B_total_ms":B, "C_total_ms":C,
            "B_sparse_calls":1, "C_sparse_calls":0, "correctness_ok":True,
        })
    good=evaluate_run(m, rows)
    assert good["accept"], good
    bad=[dict(r) for r in rows]
    bad[17]["A_total_ms"]=99.0
    assert not evaluate_run(m,bad)["accept"]
    bad=[dict(r) for r in rows]
    bad[0]["B_sparse_calls"]=0
    assert not evaluate_run(m,bad)["accept"]
    bad=[dict(r) for r in rows]
    bad[0]["C_sparse_calls"]=1
    assert not evaluate_run(m,bad)["accept"]
    bad=[dict(r) for r in rows]
    bad[0]["correctness_ok"]=False
    assert not evaluate_run(m,bad)["accept"]

    tie_rows=[dict(r) for r in rows]
    for i in range(7):
        tie_rows[i]["A_total_ms"]=tie_rows[i]["B_total_ms"]
    tie_result=evaluate_run(m,tie_rows)
    assert not tie_result["accept"] and tie_result.get("AB_positive", 0) <= 17

    return {
        "schema":"CFD_NATIVE_RUN_MANIFEST_VERIFICATION_V1",
        "manifest_schema":m["schema"],
        "order_sequence_sha256":hashlib.sha256("|".join(flat).encode("utf-8")).hexdigest(),
        "cycle_orders":exp,
        "global_position_counts":{a:{str(p):pos[a][p] for p in range(3)} for a in "ABC"},
        "global_pairwise_precedence_counts":{f"{x}>{y}":pred[(x,y)] for x,y in itertools.permutations("ABC",2)},
        "confirmatory_threshold_n24_alpha_0_025":18,
        "confirmatory_tail":str(sign_tail(24,18)),
        "negative_control_veto_threshold_n24_alpha_0_05":17,
        "negative_control_tail_at_veto":str(sign_tail(24,17)),
        "tie_policy_verified":"zero contrasts remain in fixed n=24 and count as non-success",
        "synthetic_fail_closed_tests":"PASS",
        "native_host_executed":False,
        "boundary":"Design/manifest verification only; no native performance acceptance."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--output")
    ns=ap.parse_args()
    m=json.loads(Path(ns.manifest).read_text(encoding="utf-8"))
    cert=verify_manifest(m)
    text=json.dumps(cert,indent=2,sort_keys=True)+"\n"
    if ns.output:
        Path(ns.output).write_text(text,encoding="utf-8")
    print(text,end="")

if __name__=="__main__":
    main()
