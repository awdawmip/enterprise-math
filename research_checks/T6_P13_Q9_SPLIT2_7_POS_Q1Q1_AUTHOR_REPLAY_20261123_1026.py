#!/usr/bin/env python3
"""Exact author replay: p13 valuation1 q-order9 signed (2,7), positive length2 q=(1,1).
Reuses the published 12D saturated q0 lattice and exact rational pair_search.
Scientific output only; not Source Native PROGRESS, Review or Result.
"""
import argparse,hashlib,importlib.util,json
from itertools import combinations_with_replacement
from pathlib import Path
SOURCE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6_p13_exact",SOURCE)
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
def patterns(n,k,low=1):
    if k==0:
        if n==0:yield ()
        return
    for q in range(low,n+1):
        for tail in patterns(n-q,k-1,q):yield (q,)+tail
def all_neg():
    for length in range(1,8):
        for pat in patterns(7,length):
            for neg in base.all_rosters(pat):
                yield length,neg
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=153960)
    p.add_argument("--output",required=True)
    a=p.parse_args();assert 0<=a.start<=a.end<=153960
    rows=[dict(length=i,rosters=0,raw_pairs=0,common_canceled=0,
               vertical_overbudget=0,gs_nodes=0,ball_leaves=0,budget_valid=0) for i in range(1,8)]
    h=hashlib.sha256();witnesses=[]
    for i,(length,neg) in enumerate(all_neg()):
        if i<a.start:continue
        if i>=a.end:break
        st=rows[length-1];st["rosters"]+=1
        h.update((str(length)+" "+" ".join(f"{q} {r}" for q,r in neg)+"\n").encode())
        for r1,r2 in combinations_with_replacement(range(1,13),2):
            pos=((1,r1),(1,r2));st["raw_pairs"]+=1
            if any(v in neg for v in pos):
                st["common_canceled"]+=1;continue
            skip,n,leaves=base.pair_search(pos,neg)
            st["vertical_overbudget"]+=int(skip)
            st["gs_nodes"]+=n
            st["ball_leaves"]+=len(leaves)
            st["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    obj={"schema":"T6_P13_Q9_SPLIT2_7_POS_Q1Q1_AUTHOR_REPLAY_V1",
         "range":[a.start,a.end],"frozen_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca",
         "rows":rows,"roster_line_sha256":h.hexdigest(),"witnesses":witnesses,
         "status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}
    Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"rows":rows,"roster_line_sha256":obj["roster_line_sha256"]},sort_keys=True))
if __name__=="__main__":main()
