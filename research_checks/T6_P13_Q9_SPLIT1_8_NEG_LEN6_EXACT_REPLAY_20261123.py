#!/usr/bin/env python3
"""Exact author replay for T6 p13 order9 signed split(1,8): negative length6."""
import argparse, hashlib, importlib.util, json
from pathlib import Path
SOURCE = Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
BLOB = "883ed909d37bed4b7c8b54cc0004b3e1822ee98c"
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pattern",required=True,choices=["111113","111122"])
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    assert 0<=a.start<a.end
    data=SOURCE.read_bytes()
    sha=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()
    assert sha==BLOB, f"Changed base checker SHA {sha}"
    spec=importlib.util.spec_from_file_location("_t6_signed_affine_base",SOURCE)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    pattern=tuple(map(int,a.pattern))
    assert len(pattern)==6 and sum(pattern)==8 and tuple(sorted(pattern))==pattern
    row={"pattern":list(pattern),"start":a.start,"end":a.start,
         "negative_rosters":0,"raw_pairs":0,"common_canceled":0,
         "overbudget":0,"gs_nodes":0,"ball_leaves":0,"budget_valid":0}
    witnesses=[]
    for ix,neg in enumerate(base.all_rosters(pattern)):
        if ix<a.start:continue
        if ix>=a.end:break
        row["negative_rosters"]+=1
        for r in range(1,13):
            pos=((1,r),);row["raw_pairs"]+=1
            if pos[0] in neg:
                row["common_canceled"]+=1
                continue
            skip,n,leaves=base.pair_search(pos,neg)
            row["overbudget"]+=int(skip);row["gs_nodes"]+=n
            row["ball_leaves"]+=len(leaves)
            row["budget_valid"]+=sum(int(w["budget_valid"]) for w in leaves)
            witnesses.extend(leaves)
    row["end"]=a.start+row["negative_rosters"]
    assert row["raw_pairs"]==12*row["negative_rosters"]
    result=dict(schema="EM_T6_P13_Q9_SPLIT1_8_NEG_LEN6_AUTHOR_SEGMENT_V1",
        task_id="RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
        frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
        p=13,side_cap=2331,lattice_index="13^21",gs_min_sq=str(base.dmin),
        row=row,witnesses=witnesses,status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(row,sort_keys=True))
if __name__=="__main__":main()
