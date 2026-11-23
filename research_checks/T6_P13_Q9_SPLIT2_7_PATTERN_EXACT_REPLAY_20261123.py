#!/usr/bin/env python3
"""Exact T6 p13 order9 split(2,7): replay a named negative q-partition interval."""
import argparse,hashlib,importlib.util,json
from itertools import combinations_with_replacement
from pathlib import Path
BASE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
EXPECTED_BASE_BLOB="883ed909d37bed4b7c8b54cc0004b3e1822ee98c"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pattern",required=True)
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=10**9)
    p.add_argument("--out",required=True)
    a=p.parse_args()
    pat=tuple(map(int,a.pattern))
    assert pat==tuple(sorted(pat)) and sum(pat)==7
    assert 0<=a.start<a.end
    raw=BASE.read_bytes()
    sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\x00"+raw).hexdigest()
    assert sha==EXPECTED_BASE_BLOB,sha
    spec=importlib.util.spec_from_file_location("_t6_p13_exact",BASE)
    b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
    pos=[((2,r),) for r in range(1,13)]
    pos.extend(((1,r),(1,s)) for r,s in combinations_with_replacement(range(1,13),2))
    assert len(pos)==90
    st=dict(schema="EM_T6_P13_Q9_SPLIT2_7_PATTERN_SEGMENT_AUTHOR_V1",
            task_id="RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
            science_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
            pattern=pat,range=[a.start,a.start],neg_rosters=0,raw_pairs=0,
            common=0,overbudget=0,nodes=0,leaves=0,valid=0)
    witnesses=[]
    for ix,neg in enumerate(b.all_rosters(pat)):
        if ix<a.start:continue
        if ix>=a.end:break
        st["neg_rosters"]+=1
        cn=sum(13*(13*q+r)-1 for q,r in neg)
        for posrow in pos:
            st["raw_pairs"]+=1
            if any(x in neg for x in posrow):
                st["common"]+=1
                continue
            cp=sum(13*(13*q+r)-1 for q,r in posrow)
            if max(cp,cn)>2331:
                st["overbudget"]+=1
                continue
            skip,n,leaves=b.pair_search(posrow,neg)
            st["overbudget"]+=int(skip)
            st["nodes"]+=n
            st["leaves"]+=len(leaves)
            st["valid"]+=sum(int(w["budget_valid"]) for w in leaves)
            witnesses.extend(leaves)
    st["range"][1]=a.start+st["neg_rosters"]
    assert st["raw_pairs"]==90*st["neg_rosters"]
    result=dict(summary=st,witnesses=witnesses,gs_min_sq=str(b.dmin),
                status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(st,sort_keys=True))
if __name__=="__main__":
    main()
