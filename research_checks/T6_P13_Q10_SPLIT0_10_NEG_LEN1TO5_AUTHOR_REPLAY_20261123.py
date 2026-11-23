#!/usr/bin/env python3
"""Exact author replay for p13 qorder10 split(0,10), negative lengths 1..5.

Scientific pin: enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca.
Original named denominator 13(13q+r), signed multiplicities, both
mass caps 2331 and six exact inverse-power congruences remain mandatory.
This is a callable replay, not a native Result or independent review.
"""
import argparse
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F
from sympy import Matrix

SOURCE = Path(__file__).with_name(
    "T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py"
)
spec = importlib.util.spec_from_file_location("p13_exact_base", SOURCE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

# The earlier published q9 kernel caches q=1..9. Add q=10 to retain
# the genuine q10 named atomic denominator instead of relabeling q9 data.
for r in range(1, 13):
    base.c_atom[(10, r)] = [
        F(z) for z in Matrix(1, base.N, base.particular(10, r)) * base.UI
    ]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, required=True, choices=range(1, 6))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = []
    witnesses = []
    for pattern in base.patterns(10, args.length):
        state = {
            "pattern": pattern, "rosters": 0, "vertical_overbudget": 0,
            "gs_nodes": 0, "sphere_leaves": 0, "budget_valid": 0
        }
        for neg in base.all_rosters(pattern):
            state["rosters"] += 1
            skip, nodes, leaves = base.pair_search((), neg)
            state["vertical_overbudget"] += int(skip)
            state["gs_nodes"] += nodes
            state["sphere_leaves"] += len(leaves)
            state["budget_valid"] += sum(int(w["budget_valid"]) for w in leaves)
            witnesses.extend(leaves)
        rows.append(state)
        print("COMPLETE", state, flush=True)

    result = {
        "schema": "EM_T6_P13_Q10_SPLIT0_10_LENGTH_REPLAY_V1",
        "frozen_science": "d84bd940cfb093cdc60e569f15cad58772a51dca",
        "length": args.length, "side_cap": 2331,
        "named_denominator": "13(13q+r)", "rows": rows,
        "totals": {
            "rosters": sum(x["rosters"] for x in rows),
            "gs_nodes": sum(x["gs_nodes"] for x in rows),
            "sphere_leaves": sum(x["sphere_leaves"] for x in rows),
            "budget_valid": sum(x["budget_valid"] for x in rows)
        },
        "witnesses": witnesses,
        "status": "AUTHOR_REPLAY_OUTPUT_UNREVIEWED_NOT_ADMITTED"
    }
    Path(args.output).write_text(
        json.dumps(result, sort_keys=True, indent=2), encoding="utf-8"
    )

if __name__ == "__main__":
    main()
