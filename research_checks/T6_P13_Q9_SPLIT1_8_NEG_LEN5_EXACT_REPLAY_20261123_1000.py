#!/usr/bin/env python3
"""Exact reproducibility check: T6 p13 order9 split(1,8), negative roster length5.

Uses the previously published saturated q0 lattice and rational Gram-Schmidt
implementation, whose finite domain is unchanged. Author checker only.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

SOURCE = Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec = importlib.util.spec_from_file_location("t6_p13_prior_exact", SOURCE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

PATTERNS = {
    "11114": (1,1,1,1,4),
    "11123": (1,1,1,2,3),
    "11222": (1,1,2,2,2),
}

def run(pattern, start, end):
    stats = dict(pattern=pattern, start=start, end=end, roster_count=0,
                 raw_pairs=0, common_canceled=0, overbudget=0,
                 gs_nodes=0, ball_leaves=0, budget_valid=0)
    witnesses = []
    sha = hashlib.sha256()
    for idx, negative in enumerate(mod.all_rosters(pattern)):
        if idx < start:
            continue
        if idx >= end:
            break
        stats["roster_count"] += 1
        sha.update(json.dumps(negative,separators=(",",":")).encode()+b"\\n")
        for r in range(1,13):
            positive = ((1,r),)
            stats["raw_pairs"] += 1
            if positive[0] in negative:
                stats["common_canceled"] += 1
                continue
            skipped, nodes, leaves = mod.pair_search(positive,negative)
            stats["overbudget"] += int(skipped)
            stats["gs_nodes"] += nodes
            stats["ball_leaves"] += len(leaves)
            stats["budget_valid"] += sum(int(w["budget_valid"]) for w in leaves)
            witnesses.extend(leaves)
    return dict(metrics=stats, roster_sha256=sha.hexdigest(), witnesses=witnesses)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--pattern",choices=list(PATTERNS),required=True)
    parser.add_argument("--start",type=int,default=0)
    parser.add_argument("--end",type=int,default=-1)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    p=PATTERNS[args.pattern]
    blocks=[len(list(g)) for _,g in itertools.groupby(p)]
    total=1
    from math import comb
    for k in blocks:
        total*=comb(11+k,k)
    end=total if args.end<0 else args.end
    assert 0<=args.start<=end<=total
    result=run(p,args.start,end)
    result.update(schema="EM_T6_P13_Q9_SPLIT1_8_NEG_LEN5_REPLAY_V1",
                  frozen_task_commit="d84bd940cfb093cdc60e569f15cad58772a51dca",
                  status="AUTHOR_EXACT_CHECKER_NOT_INDEPENDENT_REVIEW")
    Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+"\\n",encoding="utf-8")
    print(json.dumps({**result["metrics"],"roster_sha256":result["roster_sha256"]},sort_keys=True))

if __name__=="__main__":
    main()
