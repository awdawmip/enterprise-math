#!/usr/bin/env python3
"""Author exact replay p13 q-order9 signed split(2,7), negative pattern(7)."""
import hashlib,importlib.util,json
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path
from sympy import Matrix
BASE=Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
PIN="883ed909d37bed4b7c8b54cc0004b3e1822ee98c"
def main():
    data=BASE.read_bytes()
    sha=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()
    assert sha==PIN,sha
    spec=importlib.util.spec_from_file_location("_t6_p13_affine",BASE)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    # The pinned base includes q=1..9 particular vectors.
    pos_rosters=[((2,r),) for r in range(1,13)]
    pos_rosters.extend(((1,r),(1,s)) for r,s in combinations_with_replacement(range(1,13),2))
    assert len(pos_rosters)==90
    st=dict(schema="EM_T6_P13_Q9_SPLIT2_7_NEG_PATTERN7_AUTHOR_V1",raw_pairs=0,
            common_canceled=0,overbudget=0,gs_nodes=0,ball_leaves=0,budget_valid=0)
    witnesses=[]
    for r in range(1,13):
        neg=((7,r),)
        cn=sum(13*(13*q+x)-1 for q,x in neg)
        for pos in pos_rosters:
            st["raw_pairs"]+=1
            if any(x in neg for x in pos):
                st["common_canceled"]+=1
                continue
            cp=sum(13*(13*q+x)-1 for q,x in pos)
            if max(cp,cn)>2331:
                st["overbudget"]+=1
                continue
            # Pin base pair_search already validates 6 congruences and both budgets.
            skip,n,leaves=base.pair_search(pos,neg)
            st["overbudget"]+=int(skip)
            st["gs_nodes"]+=n
            st["ball_leaves"]+=len(leaves)
            st["budget_valid"]+=sum(bool(x["budget_valid"]) for x in leaves)
            witnesses.extend(leaves)
    assert st["raw_pairs"]==1080 and st["common_canceled"]==0
    out=dict(task_id="RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
             frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
             gs_min_square=str(base.dmin),result=st,witnesses=witnesses,
             status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__":main()
