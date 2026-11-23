#!/usr/bin/env python3
"""Exact author replay: T6 p13 q9 signed split(3,6), positive (q1,q2), negative order 6.
The initial full author run used GMP exact rational arithmetic, independently verified
by complete segment counts and witness checks. This Python replay itself is unreviewed.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path
SRC=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6base",SRC)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
def patterns(n,k,low=1):
    if k==0:
        if n==0: yield ()
        return
    for q in range(low,n+1):
        for tail in patterns(n-q,k-1,q): yield (q,)+tail
def negative_rosters():
    for k in range(1,7):
        for pat in patterns(6,k):
            for neg in base.all_rosters(pat): yield k,neg
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=42614)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    assert 0<=a.start<=a.end<=42614
    rows=[dict(length=k,rosters=0,raw_pairs=0,common_canceled=0,overbudget=0,gs_nodes=0,leaves=0,budget_valid=0) for k in range(1,7)]
    h=hashlib.sha256();witnesses=[]
    for i,(length,neg) in enumerate(negative_rosters()):
        if i<a.start:continue
        if i>=a.end:break
        st=rows[length-1];st["rosters"]+=1
        h.update((str(length)+" "+" ".join(f"{q} {r}" for q,r in neg)+"\n").encode())
        for r1 in range(1,13):
            for r2 in range(1,13):
                pos=((1,r1),(2,r2))
                st["raw_pairs"]+=1
                if any(v in neg for v in pos):
                    st["common_canceled"]+=1;continue
                skip,n,leaves=base.pair_search(pos,neg)
                st["overbudget"]+=int(skip);st["gs_nodes"]+=n
                st["leaves"]+=len(leaves)
                st["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
                witnesses.extend(leaves)
    obj={"schema":"EM_T6_P13_Q9_SPLIT3_6_POS_Q1Q2_REPLAY_V1",
         "range":[a.start,a.end],"frozen_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca",
         "rows":rows,"witnesses":witnesses,"negative_roster_line_sha256":h.hexdigest(),
         "status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}
    Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"rows":rows,"negative_roster_line_sha256":obj["negative_roster_line_sha256"]},sort_keys=True))
if __name__=="__main__": main()
