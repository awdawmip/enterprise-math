#!/usr/bin/env python3
"""T6 exact author finite slice: maximal p13, q10 signed (1,9),
negative q=(1,1,1,1,1,1,3), original H0..H6 and both 2331 budgets.
Uses previously published exact q0 affine lattice kernel; no new axiom.
Scientific pin d84bd940cfb093cdc60e569f15cad58772a51dca.
"""
import argparse
import hashlib
import importlib.util
from itertools import product, combinations_with_replacement, islice
import json
from pathlib import Path

SOURCE=Path(__file__).with_name(
  "T6_P13_Q10_SPLIT1_9_NEG_LEN1TO3_AUTHOR_EXACT_REPLAY_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p13_q10_kernel",SOURCE)
kernel=importlib.util.module_from_spec(spec)
spec.loader.exec_module(kernel)
TOTAL=12376*12

def run(start,end):
    assert 0<=start<end<=TOTAL
    stats={k:0 for k in ("rosters","raw_pairs","common_cancel",
                         "vertical_overbudget","gs_searches","gs_nodes",
                         "ball_leaves","budget_valid")}
    witnesses=[]
    digest=hashlib.sha256()
    it=product(combinations_with_replacement(range(1,13),6),range(1,13))
    for idx,(r1,r3) in enumerate(islice(it,start,end),start):
        neg=tuple((1,r) for r in r1)+((3,r3),)
        stats["rosters"]+=1
        for rp in range(1,13):
            pos=((1,rp),)
            digest.update((repr((pos,neg))+"\n").encode("ascii"))
            stats["raw_pairs"]+=1
            if pos[0] in neg:
                stats["common_cancel"]+=1
                continue
            skip,nodes,leaves=kernel.pair_search(pos,neg)
            stats["vertical_overbudget"]+=int(skip)
            stats["gs_searches"]+=int(not skip)
            stats["gs_nodes"]+=nodes
            stats["ball_leaves"]+=len(leaves)
            stats["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
            for x in leaves:
                witnesses.append(dict(negative_index=idx,
                    pos=pos,neg=neg,u=x["u"],masses=x["masses"],
                    modular_residues=[0]*6,
                    radius_sq=x["radius_sq"],budget_valid=x["budget_valid"]))
    assert stats["rosters"]==end-start
    assert stats["raw_pairs"]==12*(end-start)
    assert (stats["gs_searches"]+stats["vertical_overbudget"]+
            stats["common_cancel"]==stats["raw_pairs"])
    return dict(schema="T6_P13_Q10_SPLIT1_9_NEG1111113_AUTHOR_REPLAY_V1",
        source_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
        negative_pattern=[1,1,1,1,1,1,3],negative_range=[start,end],
        total_rosters=TOTAL,metrics=stats,
        pair_sha256=digest.hexdigest(),witnesses=witnesses,
        status="AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("start",type=int)
    ap.add_argument("end",type=int)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    obj=run(a.start,a.end)
    Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    print(json.dumps(obj["metrics"],sort_keys=True))
