#!/usr/bin/env python3
"""R5 sharp adaptive absolute-error query complexity: exact finite certificate.

Usage: python VERIFY_R5_ADAPTIVE_ABSOLUTE_COMPLEXITY.py compact_stdout.json
"""
import hashlib
import itertools
import json
import sys

SOURCE_SHA256 = "a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
SCIENCE_PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
D3 = 1744659037213380157479321600000
D4 = 1882951873548292168718745600000
TRIPLE = (217, 290, 305)
QUAD = (217, 218, 224, 305)
E = range(214, 222)
M = range(223, 292)
L = range(293, 315)

def recover(path):
    raw = open(path, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA256
    obj = json.loads(raw)
    assert obj["scientific_input"] == SCIENCE_PIN
    assert obj["status"] == "PASS_R5_101_BUDGET_INTERACTION_HIERARCHY"
    N = {}
    for k, cs in obj["all_budget_coefficients"].items():
        a = [0] * 256
        for mask, value in cs.items():
            a[int(mask)] = int(value)
        for bit in range(8):
            h = 1 << bit
            for b in range(256):
                if b & h:
                    a[b] += a[b ^ h]
        assert min(a) > 0
        N[int(k)] = a
    assert sorted(N) == list(range(214, 315))
    return N

def gap(N, k, b, c):
    return abs(N[k][b] - N[k][c])

def margin(N, budgets):
    return min(max(gap(N, k, b, c) for k in budgets)
               for b, c in itertools.combinations(range(256), 2))

def main(path):
    N = recover(path)
    fiber = range(16)
    fiber_pairs = list(itertools.combinations(fiber, 2))
    assert all(len({N[k][b] for b in fiber}) == 1 for k in N if k not in E)
    windows = {"early": (E, 0), "middle": (M, 6), "late": (L, 4)}
    for name, (window, bit) in windows.items():
        assert all(N[k][b] == N[k][b ^ (1 << bit)]
                   for k in N if k not in window for b in range(256)), name
        assert any(gap(N, k, 0, 1 << bit) > 0 for k in window)

    witnesses = {}
    for k in E:
        d, b, c = min((gap(N, k, b, c), b, c) for b, c in fiber_pairs)
        witnesses[str(k)] = {"pair": [b,c], "gap": str(d)}
    assert max(int(v["gap"]) for v in witnesses.values()) == D3
    assert witnesses["217"] == {"pair":[4,10], "gap":str(D3)}

    d3 = margin(N, TRIPLE)
    d4 = margin(N, QUAD)
    global_margin = margin(N, N)
    assert (d3, d4, global_margin) == (D3, D4, D4)
    assert [k for k in N if gap(N, k, 11, 14) == D4] == [217]

    print(json.dumps({
        "status": "PASS_R5_SHARP_ADAPTIVE_ABSOLUTE_THREE_FOUR_QUERY_COMPLEXITY",
        "frozen_science_pin": SCIENCE_PIN,
        "source_sha256": SOURCE_SHA256,
        "budget_range": [214,314],
        "masks": 256,
        "early_only_fiber_size": 16,
        "fiber_constancy_outside_early_budgets": 93,
        "early_min_pair_gaps": witnesses,
        "private_switch_window_bits": {"early":0,"middle":6,"late":4},
        "full_state_pair_count": 32640,
        "pair_budget_checks": 32640 * 101,
        "three_query_fixed_witness": list(TRIPLE),
        "sharp_adaptive_three_query_gap": str(d3),
        "four_query_fixed_witness": list(QUAD),
        "sharp_four_query_gap": str(d4),
        "unlimited_query_gap": str(global_margin),
        "sharp_noise_thresholds": {"three":str(D3)+"/2", "four":str(D4)+"/2"}
    }, indent=2))
if __name__ == "__main__":
    main(sys.argv[1])
