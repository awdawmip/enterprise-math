#!/usr/bin/env python3
"""T6 signed p13 q-order9 split(1,8), seven negative vertical atoms: exact replay.

Reuses committed p13 q0 lattice/signed pair_search. Author only, not formal
Native Result, independent review or external checker report.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path

SOURCE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6_p13_exact_prev",SOURCE)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
PAT=(1,1,1,1,1,1,2)
FULL=148512

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=FULL)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    assert 0<=a.start<=a.end<=FULL
    st={key:0 for key in ("roster_count","raw_pairs","common_canceled","overbudget","gs_nodes","ball_leaves","budget_valid")}
    digest=hashlib.sha256();witnesses=[]
    for i,negative in enumerate(mod.all_rosters(PAT)):
        if i<a.start:continue
        if i>=a.end:break
        st["roster_count"]+=1
        digest.update(json.dumps(negative,separators=(",",":")).encode()+b"\n")
        for r in range(1,13):
            positive=((1,r),)
            st["raw_pairs"]+=1
            if positive[0] in negative:
                st["common_canceled"]+=1
                continue
            skip,n,leaves=mod.pair_search(positive,negative)
            st["overbudget"]+=int(skip)
            st["gs_nodes"]+=n
            st["ball_leaves"]+=len(leaves)
            st["budget_valid"]+=sum(int(v["budget_valid"]) for v in leaves)
            witnesses.extend(leaves)
    obj=dict(schema="EM_T6_P13_Q9_SIGNED_LEN7_AUTHOR_REPLAY_V1",
        frozen_task="d84bd940cfb093cdc60e569f15cad58772a51dca",
        negative_pattern=PAT,start=a.start,end=a.end,
        metrics=st,roster_sha256=digest.hexdigest(),
        witnesses=witnesses,status="AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED")
    Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(metrics=st,roster_sha256=obj["roster_sha256"]),sort_keys=True))

if __name__=="__main__":main()
