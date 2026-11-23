#!/usr/bin/env python3
"""Author exact rational replay: maximal p13 q10 split(1,9), negative
(1,1,1,2,2,2), original H0..H6 and two 2331 mass budgets.
Scientific pin d84bd940cfb093cdc60e569f15cad58772a51dca.
Not a Native Result or independent review.
"""
from itertools import product, combinations_with_replacement, islice
from pathlib import Path
import argparse, hashlib, importlib.util, json

SOURCE=Path(__file__).with_name(
    "T6_P13_Q10_SPLIT1_9_NEG_LEN1TO3_AUTHOR_EXACT_REPLAY_20261123.py")
spec=importlib.util.spec_from_file_location("t6_q10_kernel",SOURCE)
kernel=importlib.util.module_from_spec(spec)
spec.loader.exec_module(kernel)
TOTAL=364*364

def run(start,end):
    assert 0<=start<end<=TOTAL
    stats={k:0 for k in (
        "rosters","raw_pairs","common_cancel","vertical_overbudget",
        "gs_searches","gs_nodes","ball_leaves","budget_valid")}
    digest=hashlib.sha256()
    witnesses=[]
    order=product(
        combinations_with_replacement(range(1,13),3),
        combinations_with_replacement(range(1,13),3))
    for index,(r1,r2) in enumerate(islice(order,start,end),start):
        neg=tuple((1,r) for r in r1)+tuple((2,r) for r in r2)
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
            stats["budget_valid"]+=sum(int(v["budget_valid"]) for v in leaves)
            for v in leaves:
                witnesses.append(dict(negative_index=index,
                    pos=pos,neg=neg,u=v["u"],masses=v["masses"],
                    budget_valid=v["budget_valid"]))
    assert stats["rosters"]==end-start
    assert stats["raw_pairs"]==12*(end-start)
    assert (stats["common_cancel"]+stats["vertical_overbudget"]+
            stats["gs_searches"]==stats["raw_pairs"])
    return dict(
       schema="T6_P13_Q10_SPLIT1_9_NEG111222_REPLAY_V1",
       frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
       negative_pattern=[1,1,1,2,2,2],range=[start,end],
       total_rosters=TOTAL,statistics=stats,
       pair_digest_sha256=digest.hexdigest(),witnesses=witnesses,
       author_status="UNREVIEWED_NOT_ADMITTED")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("start",type=int)
    ap.add_argument("end",type=int)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    result=run(a.start,a.end)
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result["statistics"],sort_keys=True))

if __name__=="__main__":main()
