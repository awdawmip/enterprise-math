#!/usr/bin/env python3
"""Exact signed T6 p13 order9 split(2,7), positive one q2 atom.
Reuse q0 exact saturated 12D basis and six mixed mod congruences.
Author checker; not independent review or native publication.
"""
import argparse, importlib.util, json, hashlib
from pathlib import Path
from itertools import groupby
SOURCE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6_q0",SOURCE)
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
def patterns(total,length,low=1):
    if length==0:
        if total==0: yield ()
        return
    for q in range(low,total+1):
        for t in patterns(total-q,length-1,q):
            yield (q,)+t
def all_negative():
    for length in range(1,8):
        for pat in patterns(7,length):
            for atoms in base.all_rosters(pat):
                yield length,atoms
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=int,default=0)
    ap.add_argument("--end",type=int,default=153960)
    ap.add_argument("--output",required=True)
    a=ap.parse_args(); assert 0<=a.start<=a.end<=153960
    rows=[{"length":i,"rosters":0,"raw_pairs":0,"common_canceled":0,
           "vertical_overbudget":0,"gs_nodes":0,"ball_leaves":0,"budget_valid":0} for i in range(1,8)]
    h=hashlib.sha256();witnesses=[]
    for i,(length,neg) in enumerate(all_negative()):
        if i<a.start:continue
        if i>=a.end:break
        st=rows[length-1]
        st["rosters"]+=1
        h.update((str(length)+" "+" ".join(f"{q} {r}" for q,r in neg)+"\n").encode())
        for r in range(1,13):
            pos=((2,r),);st["raw_pairs"]+=1
            if pos[0] in neg:
                st["common_canceled"]+=1;continue
            skip,n,leaves=base.pair_search(pos,neg)
            st["vertical_overbudget"]+=int(skip)
            st["gs_nodes"]+=n
            st["ball_leaves"]+=len(leaves)
            st["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    out={"schema":"T6_P13_Q9_SPLIT2_7_POS_Q2_AUTHOR_REPLAY_V1",
         "frozen_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca",
         "range":[a.start,a.end],"rows":rows,
         "roster_text_sha256":h.hexdigest(),"witnesses":witnesses,
         "status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"rows":rows,"roster_text_sha256":out["roster_text_sha256"]},sort_keys=True))
if __name__=="__main__": main()
