#!/usr/bin/env python3
"""T6 p13 q-order9 signed split(1,8): exact length-five roster enumerator.

Run from enterprise-math/research_checks. Uses the pinned previously published
exact saturated-lattice arithmetic; this is an author checker, not a Native Result.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
EXPECTED_GIT_BLOB = "883ed909d37bed4b7c8b54cc0004b3e1822ee98c"

def load_pinned():
    data = BASE.read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()
    if actual != EXPECTED_GIT_BLOB:
        raise RuntimeError(f"Base exact checker blob changed: {actual}")
    spec = importlib.util.spec_from_file_location("_t6_p13_pinned_affine", BASE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_segment(model, pat, start, end):
    assert len(pat) == 5 and tuple(sorted(pat)) == pat and sum(pat) == 8
    visited = 0
    row = dict(pattern=pat, range=[start, start], raw_pairs=0,
               common_canceled=0, overbudget=0, gs_nodes=0, ball_leaves=0, budget_valid=0)
    witnesses = []
    for index, neg in enumerate(model.all_rosters(pat)):
        if index < start:
            continue
        if index >= end:
            break
        visited += 1
        for r in range(1,13):
            pos = ((1,r),)
            row["raw_pairs"] += 1
            if pos[0] in neg:
                row["common_canceled"] += 1
                continue
            skip, nodes, leaves = model.pair_search(pos,neg)
            row["overbudget"] += int(skip)
            row["gs_nodes"] += nodes
            row["ball_leaves"] += len(leaves)
            row["budget_valid"] += sum(int(w["budget_valid"]) for w in leaves)
            witnesses.extend(leaves)
    row["range"][1] = start + visited
    row["negative_rosters"] = visited
    assert row["raw_pairs"] == visited * 12
    assert all(not w["budget_valid"] for w in witnesses)
    return dict(schema="EM_T6_P13_Q9_SPLIT1_8_NEG_LEN5_AUTHOR_EXACT_SEGMENT_V1",
                task_id="RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
                scientific_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
                split=[1,8], negative_length=5, p=13, cap=2331,
                q0_lattice_index="13^21",
                exact_gs_min_square=str(model.dmin),
                row=row,witnesses=witnesses,
                status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--pattern",choices=["11114","11123","11222"],required=True)
    parser.add_argument("--start",type=int,required=True)
    parser.add_argument("--end",type=int,required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    if not 0 <= args.start < args.end:
        parser.error("Expected 0 <= start < end")
    model=load_pinned()
    result=run_segment(model,tuple(map(int,args.pattern)),args.start,args.end)
    Path(args.out).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result["row"],sort_keys=True))
if __name__=="__main__":
    main()
