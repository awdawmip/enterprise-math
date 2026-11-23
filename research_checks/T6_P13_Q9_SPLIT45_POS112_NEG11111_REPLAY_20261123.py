#!/usr/bin/env python3
"""Exact replay of T6 p13 q9 signed (4,5), plus q112 versus minus q11111.

This is a fresh repository replay wrapper over the existing exact saturated-q0
lattice and Fraction/Gram-Schmidt implementation. Author-executed evidence is
in the matching FULL_AUTHOR_EXACT_CERT JSON. Post-publication independent
execution/review is not claimed.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

prior_path = Path(__file__).with_name(
    "T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py"
)
spec = importlib.util.spec_from_file_location("t6_p13_q9_exact_kernel", prior_path)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

POS = list(prior.all_rosters((1, 1, 2)))
NEG = list(prior.all_rosters((1, 1, 1, 1, 1)))
assert len(POS) == 936 and len(NEG) == 4368

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    assert 0 <= a.start < a.end <= len(NEG)

    stats = {
        "raw_pairs": 0, "common_cancelled": 0, "vert_overbudget": 0,
        "gs_nodes": 0, "ball_leaves": 0, "budget_valid": 0
    }
    ordered_pairs = hashlib.sha256()
    negative_rosters = hashlib.sha256()
    witnesses = []
    for minus in NEG[a.start:a.end]:
        negative_rosters.update((repr(minus) + "\n").encode("ascii"))
        named_minus = set(minus)
        for plus in POS:
            stats["raw_pairs"] += 1
            ordered_pairs.update((repr((plus, minus)) + "\n").encode("ascii"))
            if not set(plus).isdisjoint(named_minus):
                stats["common_cancelled"] += 1
                continue
            skip, nodes, leaves = prior.pair_search(plus, minus)
            stats["vert_overbudget"] += int(skip)
            stats["gs_nodes"] += nodes
            stats["ball_leaves"] += len(leaves)
            stats["budget_valid"] += sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)

    result = {
        "schema": "EM_T6_P13_Q9_SPLIT45_POS112_NEG11111_REPLAY_V1",
        "task": "RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
        "frozen_science": "d84bd940cfb093cdc60e569f15cad58772a51dca",
        "positive_pattern": [1, 1, 2],
        "negative_pattern": [1, 1, 1, 1, 1],
        "positive_rosters": len(POS),
        "negative_rosters": len(NEG),
        "start": a.start, "end": a.end,
        "statistics": stats,
        "negative_roster_sha256": negative_rosters.hexdigest(),
        "pair_order_sha256": ordered_pairs.hexdigest(),
        "witnesses": witnesses,
        "status": "AUTHOR_REPLAY_CODE_UNREVIEWED_NOT_ADMITTED"
    }
    Path(a.output).write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps({k: v for k, v in result.items() if k != "witnesses"}, sort_keys=True))

if __name__ == "__main__":
    main()
