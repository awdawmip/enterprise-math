#!/usr/bin/env python3
"""Exact q=9 positive six-branch BRC: 3-adic Smith transformation of return H and full terminal B.

Usage: python3 R762FC_Q9_IMAGE_LATTICE_SMITH_VERIFY.py 125 > evidence125.json
       python3 R762FC_Q9_IMAGE_LATTICE_SMITH_VERIFY.py 160 > evidence160.json

The named six-branch positive BRC transitions are implemented literally.
No floating point, continuous geometry, signed-force cancellation or native claim.
"""
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

sibling=Path(__file__).with_name("R762FB_Q9_RETURN_MOMENT_SMITH_VERIFY.py")
spec=importlib.util.spec_from_file_location("r762fb_brc", sibling)
brc=importlib.util.module_from_spec(spec)
spec.loader.exec_module(brc)

def compute(precision):
    q=9
    r=127
    modulus=3**precision
    points=[(i//(q*q),(i//q)%q,i%q) for i in range(q**3)]
    predecessors=[
        [((((x-dx)%q)*q+(y-dy)%q)*q+(z-dz)%q)
         for x,y,z in points] for dx,dy,dz in brc.BRANCHES
    ]
    state=[0]*(q**3)
    state[0]=1
    B=[[0]*r for _ in range(q**3)]
    moments=[]
    for n in range(2*r-1):
        moments.append(state[0])
        if n<r:
            for g,x in enumerate(state):
                B[g][n]=x
        state=[sum(state[src[g]] for src in predecessors)%modulus
               for g in range(q**3)]
    H=[[moments[i+j] for j in range(r)] for i in range(r)]
    exponents=[]
    for j in range(r):
        val,ip,kp=min(
            (brc.v3(H[i][k],precision),i,k)
            for i in range(j,r) for k in range(j,r)
        )
        if val>=precision:
            raise ArithmeticError("insufficient 3-adic precision at "+str(j))
        H[j],H[ip]=H[ip],H[j]
        if kp!=j:
            for row in H:
                row[j],row[kp]=row[kp],row[j]
            for row in B:
                row[j],row[kp]=row[kp],row[j]
        power=3**val
        remaining_modulus=modulus//power
        inverse=pow(H[j][j]//power,-1,remaining_modulus)
        # Left elimination U: zero all entries below H[j,j].
        for i in range(j+1,r):
            if H[i][j]:
                factor=((H[i][j]//power)*inverse)%remaining_modulus
                H[i][j]=0
                for k in range(j+1,r):
                    H[i][k]=(H[i][k]-factor*H[j][k])%modulus
        # Right elimination V: zero H[j,k], simultaneously apply to B.
        for k in range(j+1,r):
            if H[j][k]:
                factor=((H[j][k]//power)*inverse)%remaining_modulus
                H[j][k]=0
                for row in B:
                    row[k]=(row[k]-factor*row[j])%modulus
        exponents.append(val)
    assert exponents==sorted(exponents)
    image_column_valuations=[
        min(brc.v3(row[j],precision) for row in B)
        for j in range(r)
    ]
    penalties=[e-v for e,v in zip(exponents,image_column_valuations)]
    assert max(exponents)<precision and max(image_column_valuations)<precision
    assert sum(exponents)==6157 and max(exponents)==113
    assert max(penalties)==58
    witness=max(range(r), key=lambda j:penalties[j])
    assert witness==126 and exponents[witness]==113 and image_column_valuations[witness]==55
    return {
        "schema":"R762FC_Q9_TERMINAL_IMAGE_LATTICE_V1",
        "status":"AUTHOR_SIDE_EXACT_BRC_ARITHMETIC",
        "precision_trits":precision,
        "q":q,
        "terminal_positions":q**3,
        "power_basis_size":r,
        "moments_n_range":[0,2*r-2],
        "BRC_branch_steps":[list(step) for step in brc.BRANCHES],
        "H_3adic_smith_exponents":exponents,
        "BV_column_minimum_3adic_valuations":image_column_valuations,
        "precision_penalty_exponents":penalties,
        "determinant_3adic_valuation":sum(exponents),
        "coefficient_recovery_loss":max(exponents),
        "terminal_recovery_loss":max(penalties),
        "sharp_witness_pivot_index_0based":witness,
        "sharp_witness_e":exponents[witness],
        "sharp_witness_b":image_column_valuations[witness],
        "reduction":"UHV=diag(3^e*units), BV tracked using the exact same 3-adic unimodular column operations",
        "scope":"positive BRC full 729-terminal observer, not native signed X6 event",
        "review":"NOT_REVIEWED"
    }

if __name__=="__main__":
    precision=int(sys.argv[1]) if len(sys.argv)>1 else 125
    if precision not in (125,160):
        raise ValueError("Use validated precision 125 or 160")
    print(json.dumps(compute(precision),sort_keys=True,indent=2))
