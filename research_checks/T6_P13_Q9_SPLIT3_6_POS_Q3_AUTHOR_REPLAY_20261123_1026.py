#!/usr/bin/env python3
"""Exact T6 p13 q9 signed split(3,6), positive q3 one-atom complete replay.
Imports existing signed p13 saturated 12D q0 checker. Author only.
"""
from itertools import groupby
import argparse,hashlib,importlib.util,json
from pathlib import Path
SRC=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("base",SRC)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
def partitions(n,length,low=1):
    if length==0:
        if n==0:yield ()
        return
    for q in range(low,n+1):
        for tail in partitions(n-q,length-1,q):yield (q,)+tail
def rosters():
    for length in range(1,7):
        for pat in partitions(6,length):
            for neg in base.all_rosters(pat):yield length,neg
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=int,default=0)
    ap.add_argument("--end",type=int,default=42614)
    ap.add_argument("--output",required=True)
    a=ap.parse_args();assert 0<=a.start<=a.end<=42614
    rows=[dict(length=i,rosters=0,raw_pairs=0,common_canceled=0,overbudget=0,gs_nodes=0,leaves=0,legal=0) for i in range(1,7)]
    h=hashlib.sha256();witnesses=[]
    for idx,(length,neg) in enumerate(rosters()):
        if idx<a.start:continue
        if idx>=a.end:break
        st=rows[length-1];st["rosters"]+=1
        h.update((str(length)+" "+" ".join(f"{q} {r}" for q,r in neg)+"\n").encode())
        for r in range(1,13):
            pos=((3,r),);st["raw_pairs"]+=1
            if pos[0] in neg:
                st["common_canceled"]+=1;continue
            skip,n,leaves=base.pair_search(pos,neg)
            st["overbudget"]+=int(skip);st["gs_nodes"]+=n;st["leaves"]+=len(leaves)
            st["legal"]+=sum(int(v["budget_valid"]) for v in leaves);witnesses.extend(leaves)
    obj={"schema":"EM_T6_P13_Q9_SPLIT3_6_POS_Q3_REPLAY_V1","range":[a.start,a.end],"rows":rows,"witnesses":witnesses,"roster_line_sha256":h.hexdigest(),"frozen_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca","status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}
    Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"rows":rows,"sha256":obj["roster_line_sha256"]},sort_keys=True))
if __name__=="__main__":main()
