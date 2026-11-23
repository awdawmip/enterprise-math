#!/usr/bin/env python3
"""Author exact replay of maximal p13 order9 signed (1,8), negative length6.

Reuses the same committed q0 lattice and six-congruence pair_search as the
previous negative length1..4 author checker. No independent review is claimed.
"""
from pathlib import Path
from math import comb
from itertools import groupby
import argparse, hashlib, importlib.util, json

SOURCE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6_p13_prior_signed_exact",SOURCE)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
PATTERNS={"111113":(1,1,1,1,1,3),"111122":(1,1,1,1,2,2)}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pattern",choices=PATTERNS,required=True)
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=-1)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    pat=PATTERNS[args.pattern]
    num=1
    for _,g in groupby(pat):
        k=len(tuple(g));num*=comb(11+k,k)
    end=num if args.end<0 else args.end
    assert 0<=args.start<=end<=num
    stats={x:0 for x in ("roster_count","raw_pairs","common_canceled","overbudget","gs_nodes","ball_leaves","budget_valid")}
    witnesses=[];digest=hashlib.sha256()
    for index,neg in enumerate(mod.all_rosters(pat)):
        if index<args.start:continue
        if index>=end:break
        stats["roster_count"]+=1
        digest.update(json.dumps(neg,separators=(",",":")).encode()+b"\n")
        for r in range(1,13):
            pos=((1,r),)
            stats["raw_pairs"]+=1
            if pos[0] in neg:
                stats["common_canceled"]+=1
                continue
            skipped,nodes,leaves=mod.pair_search(pos,neg)
            stats["overbudget"]+=int(skipped)
            stats["gs_nodes"]+=nodes
            stats["ball_leaves"]+=len(leaves)
            stats["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    obj=dict(schema="EM_T6_P13_Q9_SIGNED_NEG_LEN6_AUTHOR_REPLAY_V1",
        frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
        negative_pattern=pat,range=[args.start,end],metrics=stats,
        roster_sha256=digest.hexdigest(),witnesses=witnesses,
        status="AUTHOR_EXACT_CHECKER_UNREVIEWED_NOT_ADMITTED")
    Path(args.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(**stats,roster_sha256=obj["roster_sha256"]),sort_keys=True))

if __name__=="__main__":main()
