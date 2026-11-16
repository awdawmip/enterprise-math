#!/usr/bin/env python3
"""Sharp absolute-noise count tomography; exact integer finite verifier.

Usage: python VERIFY_R5_ABSOLUTE_NOISE.py compact_stdout.json [EXACT_R5_ALL_101_BUDGETS.json]
"""
import hashlib
import itertools
import json
import sys

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
SHA = "a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
D = 1882951873548292168718745600000
D3 = 1744659037213380157479321600000
Q4 = (217, 218, 224, 305)

def table(path):
    raw = open(path, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA
    obj = json.loads(raw)
    assert obj["scientific_input"] == PIN
    assert obj["status"] == "PASS_R5_101_BUDGET_INTERACTION_HIERARCHY"
    N = {}
    for key, cs in obj["all_budget_coefficients"].items():
        a = [0] * 256
        for bitmask, value in cs.items():
            a[int(bitmask)] = int(value)
        for bit in range(8):
            h = 1 << bit
            for mask in range(256):
                if mask & h:
                    a[mask] += a[mask ^ h]
        assert all(v > 0 for v in a)
        N[int(key)] = a
    assert sorted(N) == list(range(214, 315))
    return N

def gap(N, k, b, c):
    return abs(N[k][b] - N[k][c])

def main():
    N = table(sys.argv[1])
    if len(sys.argv) > 2:
        expanded = json.load(open(sys.argv[2], encoding="utf8"))["counts_and_cohorts"]
        assert all(list(map(int, expanded[str(k)]["counts"])) == N[k] for k in N)
    pairs = list(itertools.combinations(range(256), 2))
    maxima = [(max(gap(N, k, b, c) for k in N), b, c) for b, c in pairs]
    assert min(v[0] for v in maxima) == D
    assert [[b,c] for d,b,c in maxima if d == D] == [[11+16*j,14+16*j] for j in range(8)]
    assert [k for k in N if gap(N,k,11,14) == D] == [217]
    four_margin = min(max(gap(N,k,b,c) for k in Q4) for b,c in pairs)
    assert four_margin == D
    assert all(gap(N,k,11,14) == gap(N,k,4,10) == 0 for k in N if k >= 222)
    forced_single_early = max(min(gap(N,k,11,14), gap(N,k,4,10))
                              for k in range(214,222))
    assert forced_single_early == 1752576979999614335377735680000
    six = (0,1,2,3,6,7)
    two = (4,5)
    sm = [sum(((i >> j) & 1) << bit for j,bit in enumerate(six)) for i in range(64)]
    tm = [sum(((i >> j) & 1) << bit for j,bit in enumerate(two)) for i in range(4)]
    spairs = list(itertools.combinations(sm,2))
    tpairs = list(itertools.combinations(tm,2))
    fg = {k:[gap(N,k,b,c) for b,c in spairs] for k in range(214,222)}
    mg = {k:[gap(N,k,b,c) for b,c in spairs] for k in range(223,292)}
    bestpair = max((min(max(a,b) for a,b in zip(fg[i],mg[j])),i,j)
                   for i in fg for j in mg)
    assert bestpair == (D3,217,290)
    late = max((min(gap(N,k,b,c) for b,c in tpairs),k) for k in range(294,314))
    assert late == (2653627577676347634246872444436480,305)
    out = {
        "status": "PASS_R5_ABSOLUTE_NOISE_FOUR_QUERIES_SHARP",
        "frozen_science_pin": PIN,
        "source_sha256": SHA,
        "budget_range": [214,314],
        "masks":256,
        "pair_budget_integer_checks":len(pairs)*len(N),
        "global_max_min_absolute_gap":str(D),
        "absolute_noise_threshold":str(D//2),
        "bottleneck_pairs":[[b,c] for d,b,c in maxima if d==D],
        "four_queries":Q4,
        "four_query_margin":str(four_margin),
        "best_fixed_three_margin":str(D3),
        "three_budget_example":[217,290,305],
        "one_early_query_pair_obstruction_gap":str(forced_single_early),
        "last_budget_best_margin":str(late[0]),
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
