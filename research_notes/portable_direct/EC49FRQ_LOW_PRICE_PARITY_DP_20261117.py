#!/usr/bin/env python3
"""EC49FRQ: unrestricted named-BRC parity Bellman checker and witness replay.

Put this script beside EC49FQI_NATIVE_DATA.py in code/, with frozen source/
files and inherited evidence/ files from the EC49FRQ self-contained archive.
The SHA256-pinned original 141-state / 228-action response array is preserved.
Identical same-price response partitions are coalesced, never root/terminal.
"""
from functools import cache
from pathlib import Path
import json
import hashlib
import time

from EC49FQI_NATIVE_DATA import V, weights, cost_pair, PIN, MASTER, CSV

ROOT = Path(__file__).resolve().parent.parent
assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert hashlib.sha256((ROOT / "source/frozen_original_master.txt").read_bytes()).hexdigest() == MASTER
assert hashlib.sha256((ROOT / "source/EC49FPG_PROFILE.csv").read_bytes()).hexdigest() == CSV
assert len(V) == 228 and len(weights) == 141 and sum(weights) == 310
FULL = (1 << 141) - 1
INF = 10**60

unique = {}
for q, vector in enumerate(V):
    fibers = {}
    for i, label in enumerate(vector):
        fibers[label] = fibers.get(label, 0) | (1 << i)
    parts = tuple(fibers.values())
    signature = tuple(sorted(parts))
    if signature in unique:
        assert (unique[signature][0] < 144) == (q < 144)
    else:
        unique[signature] = (q, parts)
ACTIONS = list(unique.values())
assert len(ACTIONS) == 209


def solve(x, alpha, beta):
    """Integer minimization of alpha*U_x+beta*M_x by U_x parity."""
    w = [alpha + beta * m for m in weights]

    @cache
    def mass(s):
        z = 0
        while s:
            b = s & -s
            s ^= b
            z += w[b.bit_length() - 1]
        return z

    @cache
    def optimum(s):
        if s.bit_count() == 1:
            return (0, INF)
        out = [INF, INF]
        for q, partition in ACTIONS:
            child = [s & t for t in partition if s & t]
            if len(child) < 2:
                continue
            c = x if q >= 144 else 1
            even, odd = 0, INF
            for sub in child:
                if sub.bit_count() == 1:
                    continue
                e, o = optimum(sub)
                even, odd = min(even + e, odd + o), min(even + o, odd + e)
            offset = c * mass(s)
            shift = (c * s.bit_count()) & 1
            for p in (0, 1):
                out[p] = min(out[p], offset + (even if p == shift else odd))
        return tuple(out)

    def reconstruct(s, parity):
        if s.bit_count() == 1:
            assert parity == 0
            return {"leaf": s.bit_length() - 1}
        target_cost = optimum(s)[parity]
        for q, partition in ACTIONS:
            children = [s & t for t in partition if s & t]
            if len(children) < 2:
                continue
            c = x if q >= 144 else 1
            dp = {0: (0, [])}
            for sub in children:
                opts = [(0, 0)] if sub.bit_count() == 1 else [
                    (p, v) for p, v in enumerate(optimum(sub)) if v < INF
                ]
                new = {}
                for k, (v, path) in dp.items():
                    for p, z in opts:
                        kp = k ^ p
                        cost = v + z
                        if kp not in new or cost < new[kp][0]:
                            new[kp] = (cost, path + [p])
                dp = new
            child_parity = parity ^ ((c * s.bit_count()) & 1)
            if child_parity in dp and (
                c * mass(s) + dp[child_parity][0] == target_cost
            ):
                tree = {"q": q, "children": {}}
                for sub, sub_par in zip(children, dp[child_parity][1]):
                    i = (sub & -sub).bit_length() - 1
                    lab = str(V[q][i])
                    assert lab not in tree["children"]
                    tree["children"][lab] = reconstruct(sub, sub_par)
                return tree
        raise AssertionError("unreconstructible Bellman optimum")

    start = time.monotonic()
    values = optimum(FULL)
    trees = []
    for p, value in enumerate(values):
        tree = reconstruct(FULL, p)
        c = cost_pair(tree)
        u = c["U_T"] + x * c["U_R"]
        m = c["M_T"] + x * c["M_R"]
        assert u % 2 == p and alpha * u + beta * m == value
        trees.append({
            "parity": p, "objective": value, "counts": c, "tree": tree
        })
    return {
        "x": x, "alpha": alpha, "beta": beta,
        "parity_optima": list(values),
        "memoized_subsets": optimum.cache_info().currsize,
        "elapsed_sec": round(time.monotonic() - start, 3),
        "witnesses": trees
    }


if __name__ == "__main__":
    expect = {
        (1, 24, 1): (7861, 7886),
        (1, 19, 2): (7080, 7099),
        (2, 49, 1): (15561, 15561),  # optional regression
    }
    results = []
    for args, expected in expect.items():
        item = solve(*args)
        assert tuple(item["parity_optima"]) == expected
        assert item["memoized_subsets"] == 12922
        results.append(item)
        print("PASS", args, expected, flush=True)

    trees = {
        "A": ("x1-1_l0-1.json", 32, (6, 290, 6, 751)),
        "B": ("x1-1_l155-1847.json", 140, (5, 293, 5, 704)),
        "C": ("x1-1_l1-1.json", 16, (5, 295, 5, 685)),
    }
    for label, (file, first, target) in trees.items():
        native = json.loads((ROOT / "evidence" / file).read_text())
        t = native["all_optimal_first_trees"][str(first)]
        c = cost_pair(t)
        assert tuple(c[k] for k in ("U_R", "U_T", "M_R", "M_T")) == target
        print("FULL REPLAY", label, target, flush=True)

    old = json.loads((ROOT / "evidence/EC49FRP_NATIVE_PARITY_BELLMAN_CERTIFICATE.json").read_text())
    assert (old["opt_even"], old["opt_odd"]) == (7290, 7311)
    assert old["source_master_sha256"] == MASTER
    out = ROOT / "evidence/EC49FRQ_NATIVE_LOW_PRICE_PARITY_CERTIFICATE.json"
    out.write_text(json.dumps({
        "schema": "EC49FRQ_NATIVE_LOW_PRICE_PARITY_V1",
        "scientific_pin": PIN, "source_sha256": [MASTER, CSV],
        "num_named_states": 141, "num_original_named_actions": 228,
        "unique_same_price_partitions": len(ACTIONS),
        "results": results, "inherited_x3_parity": [7290, 7311],
        "status": "AUTHOR_EXACT_FINITE_CHECKED_NOT_REVIEWED"
    }, indent=2, sort_keys=True) + "\n")
    print("PASS CERTIFICATE", out, flush=True)
