#!/usr/bin/env python3
"""Reproduce EC49FAA exact cutoff-78 certificates using existing frozen EXJ files.
Run from this directory within the research_notes/r4_ec49as_exact_right_neighborhood_20261030 tree.
Python standard library plus g++ (C++17); does not import a third-party solver.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXJ = ROOT / "EC49EXJ_H8_M4_S6_GLOBAL_EXACT"
EXY = ROOT / "EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS"
sys.path.insert(0, str(EXJ))
from SCREEN_H5_EC49EXJ import words, build_input

def schedule(row):
    a, b, c, d = row[2:6]
    groups = ((a, b), (c, d)) + tuple(
        (h,) for h in range(2, 9) if h not in (a, b, c, d))
    keys = [tuple(row[6 + 3 * i: 9 + 3 * i]) for i in range(5)]
    return tuple(sorted((h, keys[i], 4 if keys[i][0] + keys[i][1] - h - 1 >= 1 else 2)
                        for i, horizons in enumerate(groups) for h in horizons))

def main():
    lines = (EXY / "EC49EXY_DOUBLE_CANDIDATES.tsv").read_text().splitlines()
    rows = [tuple(map(int, line.split())) for line in lines
            if line and not line.startswith("#")]
    assert len(rows) == 12356 and all(len(row) == 21 for row in rows)
    ge78 = sum(row[0] >= 78 for row in rows)
    assert ge78 == 4282 and len(rows) - ge78 == 8074

    # Rank census uses the unchanged native word family (no cached count estimates).
    if "--full-rank-audit" in sys.argv:
        counts = {}
        def count_family(family):
            if family not in counts:
                counts[family] = len(words(*family))
            return counts[family]
        ranked = sorted(enumerate(rows), key=lambda ir:
            (sum(count_family((h, k, t)) for h, k, t in schedule(ir[1])),
             -ir[1][0], ir[0]))
        assert sum(row[0] < 78 for i, row in ranked[:200]) == 166
        assert [ranked[14][0], ranked[15][0]] == [0, 1492]

    report = json.loads((HERE / "EC49FAA_10_CASES.json").read_text())
    assert report["cutoff"] == 78 and len(report["cases"]) == 10
    with tempfile.TemporaryDirectory(prefix="ec49faa_") as tmp:
        exe = Path(tmp) / "exact_or_mask_dp"
        subprocess.run(["g++", "-O3", "-std=c++17",
                        str(EXJ / "EXACT_OR_MASK_DP.cpp"), "-o", str(exe)], check=True)
        for case in report["cases"]:
            assert tuple(case["row"]) == rows[case["original_index"]]
            pairs = schedule(case["row"])
            inp, n, native_count = build_input(tuple((k, t) for h, k, t in pairs))
            assert hashlib.sha256(inp.encode()).hexdigest() == case["input_sha256"]
            assert n == case["trie_nodes"] and native_count == case["native_words"]
            assert sum(t for h, k, t in pairs) == case["colors"]
            proc = subprocess.run([str(exe), "78"], input=inp, text=True,
                                  capture_output=True, check=True, timeout=120)
            assert proc.stdout.strip() == case["receipt"]
            print("PASS", case["rank"], case["original_index"], case["input_sha256"])
    print(json.dumps({"status":"PASS", "exact_new_cases":10, "EXY_ge78":ge78,
          "EXY_lt78":8074, "first200_below78":166, "first200_78_witnesses":2,
          "residual_lt78":7900}, sort_keys=True))

if __name__ == "__main__":
    main()
