#!/usr/bin/env python3
"""Reproduce author-level p13 qorder10 split(0,10), negative q-pattern
(1,1,1,1,1,2,3), contiguous canonical source-order interval.
Uses the published exact saturated q0 lattice and mixed 13-adic
kernel. This published wrapper is a reproducibility artifact,
not an independent review or automatically executed verification.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

KERNEL = Path(__file__).with_name(
    "T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
s = importlib.util.spec_from_file_location("t6_p13_kernel", KERNEL)
assert s is not None and s.loader is not None
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

def run(start, end):
    residue5 = list(itertools.combinations_with_replacement(range(1, 13), 5))
    assert len(residue5) == 4368
    total = len(residue5) * 144
    assert total == 628992 and 0 <= start < end <= total
    stats = dict(visited=0, vertical_overbudget=0,
                 gs_searches=0, gs_nodes=0, ball_leaves=0, budget_valid=0)
    witnesses = []
    h = hashlib.sha256()
    for idx in range(start, end):
        first, rest = divmod(idx, 144)
        r2, r3 = divmod(rest, 12)
        negative = tuple((1, r) for r in residue5[first]) + (
            (2, r2 + 1), (3, r3 + 1))
        h.update((repr(negative) + "\n").encode("ascii"))
        stats["visited"] += 1
        skip, nodes, leaves = m.search_one(negative)
        if skip:
            stats["vertical_overbudget"] += 1
            continue
        stats["gs_searches"] += 1
        stats["gs_nodes"] += nodes
        stats["ball_leaves"] += len(leaves)
        for w in leaves:
            valid = max(w["masses"]) <= 2331
            stats["budget_valid"] += int(valid)
            witnesses.append(dict(source_index=idx,
                negative_named_qr=negative, q0_signed_u=w["u"],
                mass_plus_minus=w["masses"], radius_sq=w["radius_sq"],
                budget_valid=valid))
    assert stats["visited"] == end-start
    assert stats["vertical_overbudget"]+stats["gs_searches"] == stats["visited"]
    return dict(schema="EM_T6_P13_Q10_NEG1111123_REPLAY_SLICE_V1",
        scientific_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
        q_pattern=[1,1,1,1,1,2,3],
        negative_roster_range=[start,end], total=total,
        original_mass_cap_per_side=2331, stats=stats,
        roster_sha256=h.hexdigest(),
        witnesses=witnesses,
        mathematical_acceptance="NOT_ADMITTED")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("start", type=int)
    p.add_argument("end", type=int)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    out = run(args.start, args.end)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",
        encoding="utf-8")
    print(json.dumps(out["stats"],sort_keys=True))
