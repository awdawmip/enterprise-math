#!/usr/bin/env python3
"""Exact T6 p13 order9 split(1,8) negative lengths seven/eight: segment replay.

This reuses the frozen previously published 12D affine enumeration and only
changes the signed vertical roster range. Author checker; no Native acceptance.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
EXPECTED_BASE_BLOB = "883ed909d37bed4b7c8b54cc0004b3e1822ee98c"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pattern", choices=["1111112","11111111"], required=True)
    p.add_argument("--start", type=int, required=True)
    p.add_argument("--end", type=int, required=True)
    p.add_argument("--out", required=True)
    args=p.parse_args()
    assert 0 <= args.start < args.end
    raw=BASE.read_bytes()
    blob=hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
    if blob != EXPECTED_BASE_BLOB:
        raise RuntimeError(f"Changed base exact checker: {blob}")
    spec=importlib.util.spec_from_file_location("_t6_p13_affine_base",BASE)
    base=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    pattern=tuple(map(int,args.pattern))
    assert sum(pattern)==8 and tuple(sorted(pattern))==pattern and len(pattern) in (7,8)
    row=dict(pattern=pattern, start=args.start, end=args.start, negative_rosters=0,
             raw_pairs=0, common_canceled=0, overbudget=0,
             gs_nodes=0, ball_leaves=0, budget_valid=0)
    witnesses=[]
    for i,neg in enumerate(base.all_rosters(pattern)):
        if i < args.start:
            continue
        if i >= args.end:
            break
        row["negative_rosters"]+=1
        for r in range(1,13):
            pos=((1,r),)
            row["raw_pairs"]+=1
            if pos[0] in neg:
                row["common_canceled"]+=1
                continue
            skip,n,leaves=base.pair_search(pos,neg)
            row["overbudget"]+=int(skip)
            row["gs_nodes"]+=n
            row["ball_leaves"]+=len(leaves)
            row["budget_valid"]+=sum(int(w["budget_valid"]) for w in leaves)
            witnesses.extend(leaves)
    row["end"]=args.start+row["negative_rosters"]
    assert row["raw_pairs"]==12*row["negative_rosters"]
    result=dict(schema="EM_T6_P13_Q9_SPLIT1_8_NEG_LEN7_8_AUTHOR_SEGMENT_V1",
                task_id="RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
                frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
                p=13,side_cap=2331,lattice_index="13^21",gs_min_sq=str(base.dmin),
                row=row,witnesses=witnesses,
                status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(row,sort_keys=True))
if __name__=="__main__":
    main()
