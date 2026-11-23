#!/usr/bin/env python3
"""Exact finite p13 q10 split(3,7), negative q=(1,6).
Author replay, not independent review or native Result.
Dependencies: published frozen q0 lattice kernel; Python sympy.
"""
import argparse,hashlib,importlib.util,json
from fractions import Fraction as F
from itertools import combinations_with_replacement,product
from pathlib import Path
from sympy import Matrix
kernel=Path(__file__).with_name("T6_P13_Q10_SPLIT2_8_NEG11111111_SLICE_REPLAY_20261123_2300.py")
spec=importlib.util.spec_from_file_location("t6_q0_exact",str(kernel))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
for q in (6,):
    for r in range(1,13):
        m.c_atom[(q,r)]=[F(x) for x in Matrix(1,m.N,m.particular(q,r))*m.UI]
pos=[((3,r),) for r in range(1,13)]
pos += [((1,r),(2,s)) for r,s in product(range(1,13),repeat=2)]
pos += [tuple((1,r) for r in x) for x in combinations_with_replacement(range(1,13),3)]
assert len(pos)==520
a=argparse.ArgumentParser()
a.add_argument("--start",type=int,required=True)
a.add_argument("--end",type=int,required=True)
a.add_argument("--output",required=True)
args=a.parse_args()
assert 0<=args.start<args.end<=144
stats=dict(negative_rosters=0,positive_rosters=520,raw_signed_pairs=0,
           common_named_atom_canceled=0,vertical_original_mass_excess=0,
           gs_searches=0,gs_nodes=0,relaxed_sphere_witnesses=0,
           both_original_side_mass_valid=0)
roster_hash=hashlib.sha256();pair_hash=hashlib.sha256();witnesses=[]
for ni,t in enumerate(product(range(1,13),range(1,13))):
    if ni>=args.end:break
    if ni<args.start:continue
    neg=((1,t[0]),(6,t[1]))
    stats["negative_rosters"]+=1
    roster_hash.update((repr(neg)+"\n").encode("ascii"))
    for pi,p in enumerate(pos):
        stats["raw_signed_pairs"]+=1
        pair_hash.update((repr((ni,pi,p,neg))+"\n").encode("ascii"))
        if any(atom in neg for atom in p):
            stats["common_named_atom_canceled"]+=1
            continue
        skip,nodes,leaves=m.pair_search(p,neg)
        if skip:
            stats["vertical_original_mass_excess"]+=1
            continue
        stats["gs_searches"]+=1;stats["gs_nodes"]+=nodes
        stats["relaxed_sphere_witnesses"]+=len(leaves)
        stats["both_original_side_mass_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
        for v in leaves:
            v["negative_roster_index"]=ni
            v["positive_roster_index"]=pi
            v["modular_residues"]=[
                (sum(x*pow(r,-k,13**k) for r,x in enumerate(v["u"],1))
                 +sum(pow(13*q+r,-k,13**k) for q,r in p)
                 -sum(pow(13*q+r,-k,13**k) for q,r in neg))%(13**k)
                for k in range(1,7)]
            assert v["modular_residues"]==[0]*6
            witnesses.append(v)
assert stats["negative_rosters"]==args.end-args.start
assert stats["raw_signed_pairs"]==520*(args.end-args.start)
assert (stats["common_named_atom_canceled"]+stats["vertical_original_mass_excess"]+
        stats["gs_searches"]==stats["raw_signed_pairs"])
res=dict(schema="EM_T6_P13_Q10_SPLIT3_7_NEG16_AUTHOR_EXACT_SLICE_V1",
         frozen_science="awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca",
         signed_split=[3,7],negative_q_pattern=[1,6],
         positive_q_patterns=[[3],[1,2],[1,1,1]],interval=[args.start,args.end],
         budget_each_side=m.CAP,lattice_index="13^21",gs_min_sq=str(m.dmin),
         source_order="neg q1 then q6 single, both 1..12; positives q3,q1q2,q1^3 CWR",
         stats=stats,negative_roster_sha256=roster_hash.hexdigest(),
         pair_digest_sha256=pair_hash.hexdigest(),witnesses=witnesses,
         status="AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED")
with open(args.output,"w") as f:json.dump(res,f,indent=2,sort_keys=True)
print(json.dumps({k:v for k,v in res.items() if k!="witnesses"},sort_keys=True))
