#!/usr/bin/env python3
"""Exact bounded author replay: maximal p13 v13=1, order10 split(1,9),
negative q-pattern (1,1,1,1,2,3). Pinned scientific model d84bd940...
Imports the prior verified 12D q0 lattice/GS kernel; this is a replay wrapper,
not an independent review, admission, or native task run.
"""
from pathlib import Path
from itertools import product, combinations_with_replacement, islice
import argparse
import hashlib
import importlib.util
import json

SOURCE = Path(__file__).with_name(
    "T6_P13_Q10_SPLIT1_9_NEG_LEN1TO3_AUTHOR_EXACT_REPLAY_20261123.py")
spec = importlib.util.spec_from_file_location("t6_q10_exact_kernel", SOURCE)
kernel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kernel)

TOTAL = 196560

def run(start, end):
    assert 0 <= start < end <= TOTAL
    metrics = {k:0 for k in (
        "rosters","raw_pairs","common_cancel","vertical_overbudget",
        "gs_searches","gs_nodes","ball_leaves","budget_valid")}
    digest = hashlib.sha256()
    witnesses = []
    order = product(
        combinations_with_replacement(range(1, 13), 4),
        range(1, 13), range(1, 13))
    for index, (r1, r2, r3) in enumerate(islice(order,start,end), start):
        neg = tuple((1,r) for r in r1) + ((2,r2),(3,r3))
        metrics["rosters"] += 1
        for rp in range(1,13):
            pos = ((1,rp),)
            digest.update((repr((pos,neg)) + "\n").encode("ascii"))
            metrics["raw_pairs"] += 1
            if pos[0] in neg:
                metrics["common_cancel"] += 1
                continue
            skipped, nodes, leaves = kernel.pair_search(pos, neg)
            metrics["vertical_overbudget"] += int(skipped)
            metrics["gs_searches"] += int(not skipped)
            metrics["gs_nodes"] += nodes
            metrics["ball_leaves"] += len(leaves)
            metrics["budget_valid"] += sum(int(x["budget_valid"]) for x in leaves)
            for v in leaves:
                witnesses.append({
                    "negative_index": index,
                    "pos": pos, "neg": neg,
                    "u": v["u"], "masses": v["masses"],
                    "budget_valid": v["budget_valid"]
                })
    assert metrics["rosters"] == end-start
    assert metrics["raw_pairs"] == (end-start)*12
    assert (metrics["common_cancel"]+metrics["vertical_overbudget"]+
            metrics["gs_searches"] == metrics["raw_pairs"])
    return {"schema":"T6_P13_Q10_SPLIT1_9_NEG111123_REPLAY_V1",
        "frozen_science":"d84bd940cfb093cdc60e569f15cad58772a51dca",
        "range":[start,end], "negative_pattern":[1,1,1,1,2,3],
        "total_rosters":TOTAL,"metrics":metrics,
        "pair_digest_sha256":digest.hexdigest(),"witnesses":witnesses,
        "status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("start",type=int)
    ap.add_argument("end",type=int)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    result=run(args.start,args.end)
    Path(args.output).write_text(
        json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result["metrics"],sort_keys=True))

if __name__=="__main__":
    main()
