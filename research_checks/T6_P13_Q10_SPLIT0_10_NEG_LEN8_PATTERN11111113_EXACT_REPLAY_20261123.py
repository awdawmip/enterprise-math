#!/usr/bin/env python3
"""Exact author replay for T6 maximal-p13 qorder10 split(0,10),
negative named q-pattern (1,1,1,1,1,1,1,3). Supports full or bounded
canonical contiguous intervals. Execution of this published wrapper
has not been independently verified.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

KERNEL=Path(__file__).with_name(
 "T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
s=importlib.util.spec_from_file_location("t6_p13_kernel",KERNEL)
assert s is not None and s.loader is not None
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)

def run(start,end):
    q1=list(itertools.combinations_with_replacement(range(1,13),7))
    q3=list(range(1,13))
    assert len(q1)==31824 and len(q3)==12
    total=len(q1)*len(q3)
    assert total==381888 and 0<=start<end<=total
    stats=dict(visited=0,vertical_overbudget=0,gs_searches=0,
         gs_nodes=0,ball_leaves=0,budget_valid=0)
    leaves=[];hash_roster=hashlib.sha256()
    for idx in range(start,end):
        first,second=divmod(idx,len(q3))
        negative=tuple((1,r) for r in q1[first])+((3,q3[second]),)
        hash_roster.update((repr(negative)+"\n").encode("ascii"))
        stats["visited"]+=1
        skip,nodes,found=m.search_one(negative)
        if skip:
            stats["vertical_overbudget"]+=1
            continue
        stats["gs_searches"]+=1;stats["gs_nodes"]+=nodes
        stats["ball_leaves"]+=len(found)
        for w in found:
            valid=max(w["masses"])<=2331
            stats["budget_valid"]+=int(valid)
            leaves.append(dict(index=idx,negative_named_qr=negative,
                q0_signed_u=w["u"],masses=w["masses"],
                radius_sq=w["radius_sq"],budget_valid=valid))
    assert stats["visited"]==end-start
    assert stats["vertical_overbudget"]+stats["gs_searches"]==stats["visited"]
    return dict(schema="EM_T6_P13_Q10_NEG11111113_EXACT_REPLAY_V1",
        scientific_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
        pattern=[1,1,1,1,1,1,1,3],interval=[start,end],universe=total,
        cap_each_side=2331,stats=stats,roster_sha256=hash_roster.hexdigest(),
        relaxed_witnesses=leaves,strength="AUTHOR_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("start",type=int)
    p.add_argument("end",type=int)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    d=run(a.start,a.end)
    Path(a.output).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(d["stats"],sort_keys=True))
