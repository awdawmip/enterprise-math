#!/usr/bin/env python3
"""Exact author replay for maximal p13, v13=1, signed order10 split(2,8).
Requires sibling T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py
for the unchanged exact saturated q0 lattice, particular solutions and GS search.
This is a reproducibility aid; not an independently reviewed Native Result.
"""
import argparse
import hashlib
import json
from itertools import combinations_with_replacement, groupby, product
from math import comb
import T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900 as base

PATTERNS = {
    "1115": (1,1,1,5),
    "1124": (1,1,2,4),
    "1133": (1,1,3,3),
    "1223": (1,2,2,3),
    "2222": (2,2,2,2),
    "11114": (1,1,1,1,4),
    "11123": (1,1,1,2,3),
    "11222": (1,1,2,2,2),
}
POSITIVES = (
    [((2,r),) for r in range(1,13)] +
    [((1,r1),(1,r2)) for r1,r2 in
        combinations_with_replacement(range(1,13),2)]
)
assert len(POSITIVES)==90
assert base.P==13 and base.CAP==2331 and base.N==12
assert base.dmin>2*base.CAP**2

def roster_count(pat):
    # Product counting, one combinations-with-replacement block per equal-q group.
    result=1
    for _, g in groupby(pat):
        size=len(tuple(g))
        result *= comb(11+size,size)
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--pattern",choices=PATTERNS,required=True)
    parser.add_argument("--start",type=int,default=0)
    parser.add_argument("--end",type=int)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    pat=PATTERNS[args.pattern]
    total=roster_count(pat)
    end=total if args.end is None else args.end
    assert 0<=args.start<end<=total
    stats=dict(negative_roster_start=args.start,negative_roster_end=end,
        negative_rosters_visited=0,raw_signed_pairs=0,
        common_named_atom_canceled=0,vertical_original_mass_excess=0,
        gs_searches=0,gs_nodes=0,relaxed_sphere_witnesses=0,
        both_original_side_mass_valid=0)
    digest=hashlib.sha256()
    witnesses=[]
    for index, neg in enumerate(base.all_rosters(pat)):
        if index>=end:break
        if index<args.start:continue
        stats["negative_rosters_visited"]+=1
        for pidx,pos in enumerate(POSITIVES):
            stats["raw_signed_pairs"]+=1
            digest.update((repr((index,pos,neg))+"\n").encode("ascii"))
            if any(atom in neg for atom in pos):
                stats["common_named_atom_canceled"]+=1
                continue
            skip,nodes,leaves=base.pair_search(pos,neg)
            if skip:
                stats["vertical_original_mass_excess"]+=1
                continue
            stats["gs_searches"]+=1
            stats["gs_nodes"]+=nodes
            stats["relaxed_sphere_witnesses"]+=len(leaves)
            for w in leaves:
                w=dict(w,negative_roster_index=index,positive_roster_index=pidx)
                witnesses.append(w)
                stats["both_original_side_mass_valid"]+=int(w["budget_valid"])
    assert stats["negative_rosters_visited"]==end-args.start
    assert stats["raw_signed_pairs"]==90*(end-args.start)
    assert (stats["common_named_atom_canceled"]+
        stats["vertical_original_mass_excess"]+
        stats["gs_searches"]==stats["raw_signed_pairs"])
    stats["pair_digest_sha256"]=digest.hexdigest()
    result=dict(schema="EM_T6_P13_Q10_SPLIT2_8_AUTHOR_EXACT_REPLAY_V1",
        task_id="RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
        frozen_scientific_source="d84bd940cfb093cdc60e569f15cad58772a51dca",
        negative_q_pattern=pat,positive_q_patterns=[(2,),(1,1)],
        negative_roster_total=total,positive_roster_total=90,
        six_moduli=[13**j for j in range(1,7)],
        saturated_q0_lattice_index="13^21",
        gs_min_diagonal_sq=str(base.dmin),
        both_original_mass_budget=2331,stats=stats,
        full_signed_witnesses=witnesses,
        strength="AUTHOR_REPLAY / UNREVIEWED / NOT_ADMITTED")
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,sort_keys=True)
    print(json.dumps({"pattern":args.pattern,"stats":stats},sort_keys=True))

if __name__=="__main__":
    main()
