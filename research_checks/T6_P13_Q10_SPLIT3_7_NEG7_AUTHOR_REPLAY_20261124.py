#!/usr/bin/env python3
"""Reproduce p13 q10 split(3,7), negative q=(7,) at T6=2332.
Exact author finite research; depends on the pinned q0 lattice kernel.
Run from the research_checks directory:
python T6_P13_Q10_SPLIT3_7_NEG7_AUTHOR_REPLAY_20261124.py --output result.json
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
from sympy import Matrix

kernel=Path(__file__).with_name("T6_P13_Q10_SPLIT2_8_NEG11111111_SLICE_REPLAY_20261123_2300.py")
spec=importlib.util.spec_from_file_location("t6_q0_exact",str(kernel))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
for q in (3,7):
    for r in range(1,13):
        m.c_atom[(q,r)]=[F(x) for x in Matrix(1,m.N,m.particular(q,r))*m.UI]

pos=[((3,r),) for r in range(1,13)]
pos += [((1,r),(2,s)) for r,s in product(range(1,13),repeat=2)]
pos += [tuple((1,r) for r in a) for a in combinations_with_replacement(range(1,13),3)]
neg=[((7,r),) for r in range(1,13)]
assert len(pos)==520 and len(neg)==12
counts=dict(negative_rosters=12,positive_rosters=520,raw_signed_pairs=0,
    shared_named_atoms=0,vertical_original_mass_excess=0,
    gs_searches=0,gs_nodes=0,relaxed_sphere_witnesses=0,
    both_original_side_mass_valid=0)
roster_hash=hashlib.sha256()
pair_hash=hashlib.sha256()
witnesses=[]
for ni,n in enumerate(neg):
    roster_hash.update((repr(n)+"\n").encode("ascii"))
    for pi,p in enumerate(pos):
        counts["raw_signed_pairs"]+=1
        pair_hash.update((repr((ni,pi,p,n))+"\n").encode("ascii"))
        if any(a in n for a in p):
            counts["shared_named_atoms"]+=1
            continue
        skip,nodes,leaves=m.pair_search(p,n)
        if skip:
            counts["vertical_original_mass_excess"]+=1
            continue
        counts["gs_searches"]+=1
        counts["gs_nodes"]+=nodes
        counts["relaxed_sphere_witnesses"]+=len(leaves)
        counts["both_original_side_mass_valid"]+=sum(int(v["budget_valid"]) for v in leaves)
        for v in leaves:
            v["negative_roster_index"]=ni
            v["positive_roster_index"]=pi
            v["modular_residues"]=[
                (sum(x*pow(r,-k,13**k) for r,x in enumerate(v["u"],1))
                +sum(pow(13*q+r,-k,13**k) for q,r in p)
                -sum(pow(13*q+r,-k,13**k) for q,r in n))%(13**k)
                for k in range(1,7)]
            assert v["modular_residues"]==[0]*6
            witnesses.append(v)
assert counts["raw_signed_pairs"]==6240
assert counts["shared_named_atoms"]+counts["vertical_original_mass_excess"]+counts["gs_searches"]==6240
res=dict(schema="EM_T6_P13_Q10_SPLIT3_7_NEG7_AUTHOR_EXACT_CERT_V1",
    frozen_science="awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca",
    p=13,q_vertical_total=10,signed_split=[3,7],
    positive_q_patterns=[[3],[1,2],[1,1,1]],negative_q_pattern=[7],
    original_side_mass_cap=2331,lattice_index="13^21",gs_min_sq=str(m.dmin),
    source_order="neg q7 r=1..12; pos single q3 then q1q2 then q1^3 CWR",
    counts=counts,negative_roster_sha256=roster_hash.hexdigest(),
    pair_digest_sha256=pair_hash.hexdigest(),witnesses=witnesses,
    status="AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED")
parser=argparse.ArgumentParser()
parser.add_argument("--output",required=True)
a=parser.parse_args()
with open(a.output,"w",encoding="utf8") as f:
    json.dump(res,f,indent=2,sort_keys=True)
print(json.dumps({k:v for k,v in res.items() if k!="witnesses"},sort_keys=True))
