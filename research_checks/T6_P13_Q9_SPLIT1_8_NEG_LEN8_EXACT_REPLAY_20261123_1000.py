#!/usr/bin/env python3
"""Exact author replay T6 p13 q-order9 signed (1,8), negative all eight q1 atoms.

Reuse committed 12-dimensional saturated q0 lattice and pair_search from
previous p13 signed checker, preserving exact integer/rational semantics.
"""
import argparse, hashlib, importlib.util, json
from pathlib import Path

PREV=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("p13_exact_prev",PREV)
p13=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p13)
PAT=(1,)*8
FULL=75582

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--start",type=int,default=0)
    parser.add_argument("--end",type=int,default=FULL)
    parser.add_argument("--output",required=True)
    a=parser.parse_args()
    assert 0<=a.start<=a.end<=FULL
    s={key:0 for key in ("roster_count","raw_pairs","common_canceled","overbudget","gs_nodes","ball_leaves","budget_valid")}
    witnesses=[];digest=hashlib.sha256()
    for i,negative in enumerate(p13.all_rosters(PAT)):
        if i<a.start:continue
        if i>=a.end:break
        s["roster_count"]+=1
        digest.update(json.dumps(negative,separators=(",",":")).encode()+b"\n")
        for r in range(1,13):
            positive=((1,r),)
            s["raw_pairs"]+=1
            if positive[0] in negative:
                s["common_canceled"]+=1
                continue
            skip,n,leaves=p13.pair_search(positive,negative)
            s["overbudget"]+=int(skip)
            s["gs_nodes"]+=n
            s["ball_leaves"]+=len(leaves)
            s["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    obj=dict(schema="EM_T6_P13_Q9_SIGNED_NEG_LEN8_EXACT_REPLAY_V1",frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
             pattern=PAT,start=a.start,end=a.end,metrics=s,roster_sha256=digest.hexdigest(),witnesses=witnesses,status="AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED")
    Path(a.output).write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n")
    print(json.dumps(dict(metrics=s,roster_sha256=obj["roster_sha256"]),sort_keys=True))

if __name__=="__main__":main()
