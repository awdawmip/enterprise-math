#!/usr/bin/env python3
"""Exact T6 p13 signed q-order9 (3,6), positive q=(1,1,1), full author replay.
Imports published p13 q0 saturated 12D lattice; no external admissions.
"""
import argparse,hashlib,importlib.util,json
from itertools import combinations_with_replacement
from pathlib import Path
SRC=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec=importlib.util.spec_from_file_location("t6_p13",SRC)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
def patterns(n,k,low=1):
    if k==0:
        if n==0: yield ()
        return
    for q in range(low,n+1):
        for t in patterns(n-q,k-1,q):yield (q,)+t
def all_negative():
    for k in range(1,7):
        for pat in patterns(6,k):
            for neg in base.all_rosters(pat):yield k,neg
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=42614)
    p.add_argument("--output",required=True)
    a=p.parse_args();assert 0<=a.start<=a.end<=42614
    stats=[dict(length=k,rosters=0,raw_pairs=0,shared=0,overbudget=0,gs_nodes=0,leaves=0,budget_valid=0) for k in range(1,7)]
    digest=hashlib.sha256();witnesses=[]
    for idx,(length,neg) in enumerate(all_negative()):
        if idx<a.start:continue
        if idx>=a.end:break
        s=stats[length-1];s["rosters"]+=1
        digest.update((str(length)+" "+" ".join(f"{q} {r}" for q,r in neg)+"\n").encode())
        for rs in combinations_with_replacement(range(1,13),3):
            pos=tuple((1,r) for r in rs)
            s["raw_pairs"]+=1
            if any(x in neg for x in pos):
                s["shared"]+=1;continue
            skip,n,leaves=base.pair_search(pos,neg)
            s["overbudget"]+=int(skip);s["gs_nodes"]+=n;s["leaves"]+=len(leaves)
            s["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    obj={"schema":"EM_T6_P13_Q9_SPLIT3_6_POS_Q1Q1Q1_REPLAY_V1",
         "range":[a.start,a.end],"rows":stats,"witnesses":witnesses,
         "frozen_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca",
         "negative_roster_sha256":digest.hexdigest(),"status":"AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED"}
    Path(a.output).write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"rows":stats,"negative_roster_sha256":obj["negative_roster_sha256"]},sort_keys=True))
if __name__=="__main__":main()
