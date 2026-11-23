#!/usr/bin/env python3
"""Author exact replay for p13 q10 signed (3,7), negative (1,1,5).
Use the frozen q0 H0..H6 lattice, six p-adic congruences and 2331 caps.
Author finite evidence only; no independent review or formal Task admission.
"""
import argparse, hashlib, importlib.util, json
from itertools import combinations_with_replacement, product
from pathlib import Path

kernel = Path(__file__).with_name("T6_P13_Q10_SPLIT2_8_NEG11111111_SLICE_REPLAY_20261123_2300.py")
spec = importlib.util.spec_from_file_location("t6_q0_frozen", str(kernel))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
positives = [((3,r),) for r in range(1,13)]
positives += [((1,r),(2,s)) for r,s in product(range(1,13),repeat=2)]
positives += [tuple((1,r) for r in v) for v in combinations_with_replacement(range(1,13),3)]
assert len(positives) == 520

def replay(start,end):
    assert 0 <= start < end <= 936
    stats = dict(negative_rosters=0, positive_rosters=520, raw_signed_pairs=0,
                 common_named_atom_canceled=0, vertical_original_mass_excess=0,
                 gs_searches=0, gs_nodes=0, relaxed_sphere_witnesses=0,
                 both_original_side_mass_valid=0)
    roster_sha=hashlib.sha256();pair_sha=hashlib.sha256();witnesses=[]
    negatives = (((1,a),(1,b),(5,c))
                 for a,b in combinations_with_replacement(range(1,13),2)
                 for c in range(1,13))
    for ni,neg in enumerate(negatives):
        if ni >= end: break
        if ni < start: continue
        stats["negative_rosters"] += 1
        roster_sha.update((repr(neg)+"\n").encode("ascii"))
        for pi,pos in enumerate(positives):
            stats["raw_signed_pairs"] += 1
            pair_sha.update((repr((ni,pi,pos,neg))+"\n").encode("ascii"))
            if any(atom in neg for atom in pos):
                stats["common_named_atom_canceled"] += 1
                continue
            skip,nodes,leaves=m.pair_search(pos,neg)
            if skip:
                stats["vertical_original_mass_excess"] += 1
                continue
            stats["gs_searches"] += 1
            stats["gs_nodes"] += nodes
            stats["relaxed_sphere_witnesses"] += len(leaves)
            stats["both_original_side_mass_valid"] += sum(int(v["budget_valid"]) for v in leaves)
            for v in leaves:
                v["negative_roster_index"] = ni
                v["positive_roster_index"] = pi
                v["modular_residues"] = [
                    (sum(x*pow(r,-k,13**k) for r,x in enumerate(v["u"],1))
                     +sum(pow(13*q+r,-k,13**k) for q,r in pos)
                     -sum(pow(13*q+r,-k,13**k) for q,r in neg))%(13**k)
                    for k in range(1,7)]
                assert v["modular_residues"] == [0]*6
                witnesses.append(v)
    assert stats["negative_rosters"] == end-start
    assert stats["raw_signed_pairs"] == 520*(end-start)
    assert stats["gs_searches"]+stats["common_named_atom_canceled"]+stats["vertical_original_mass_excess"] == stats["raw_signed_pairs"]
    return dict(schema="EM_T6_P13_Q10_SPLIT3_7_NEG115_AUTHOR_EXACT_SLICE_V1",
                frozen_science="awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca",
                signed_split=[3,7],negative_q_pattern=[1,1,5],
                positive_q_patterns=[[3],[1,2],[1,1,1]],interval=[start,end],
                source_order="negative CWR q1(12,2) then q5(12,1); positive q3 single, q1q2 product, q1^3 CWR",
                budget_each_side=m.CAP,lattice_index="13^21",gs_min_sq=str(m.dmin),
                stats=stats,negative_roster_sha256=roster_sha.hexdigest(),
                pair_digest_sha256=pair_sha.hexdigest(),witnesses=witnesses,
                status="AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED")

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--start",type=int,required=True)
    p.add_argument("--end",type=int,required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    result=replay(args.start,args.end)
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in result.items() if k!="witnesses"},sort_keys=True))
