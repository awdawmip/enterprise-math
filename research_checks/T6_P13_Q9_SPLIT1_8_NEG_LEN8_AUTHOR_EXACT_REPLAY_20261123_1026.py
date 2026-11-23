#!/usr/bin/env python3
"""Exact rational replay for T6 p13 q9 signed (1,8), negative length eight.
Uses the previously committed saturated q0 lattice and pair_search.
This replay file is author reproduction code, not independent review/Native Result.
"""
import argparse, hashlib, importlib.util, json
from pathlib import Path
SOURCE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6_p13_base",SOURCE)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
PAT=(1,)*8
FULL=75582
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=int,default=0)
    ap.add_argument("--end",type=int,default=FULL)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    assert 0<=args.start<=args.end<=FULL
    st={k:0 for k in ("negative_rosters","raw_pairs","common_canceled","vertical_overbudget","gs_nodes","ball_leaves","both_budget_legal")}
    h=hashlib.sha256();witnesses=[]
    for i,neg in enumerate(mod.all_rosters(PAT)):
        if i<args.start: continue
        if i>=args.end: break
        st["negative_rosters"]+=1
        h.update(json.dumps(neg,separators=(",",":")).encode()+b"\n")
        for r in range(1,13):
            pos=((1,r),)
            st["raw_pairs"]+=1
            if pos[0] in neg:
                st["common_canceled"]+=1
                continue
            skip,n,leaves=mod.pair_search(pos,neg)
            st["vertical_overbudget"]+=int(skip)
            st["gs_nodes"]+=n
            st["ball_leaves"]+=len(leaves)
            st["both_budget_legal"]+=sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    obj={"schema":"EM_T6_P13_Q9_SPLIT1_8_NEG_LEN8_REPLAY_V1",
         "frozen_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca",
         "range":[args.start,args.end],"pattern":PAT,"metrics":st,
         "roster_sha256":h.hexdigest(),"witnesses":witnesses,
         "status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}
    Path(args.output).write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"metrics":st,"roster_sha256":obj["roster_sha256"]},sort_keys=True))
if __name__=="__main__":
    main()
