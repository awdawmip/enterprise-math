#!/usr/bin/env python3
"""C307 exact 125-path modulus schedule audit.

Requires unpacked C306 portable predecessor files in this script's directory:
C305_MODULAR_NEWTON_CONTENT.py, C306 author complete audit JSON,
and EM_C301_EXACT_PORTABLE/ frozen inputs.
This DOES NOT re-evaluate all 44,038 reduced-numerator residues.
"""
from __future__ import annotations
import json,sys,argparse
from pathlib import Path
from math import gcd,comb
from statistics import median
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from C307_HETEROGENEOUS_NEWTON_CONTENT import adaptive_moduli
import C305_MODULAR_NEWTON_CONTENT as base

def run(output):
    src=json.loads((ROOT/"EM_C301_EXACT_PORTABLE/C293_125_REFINED_BRACKETS.json").read_text())
    ref=json.loads((ROOT/"C306_AUTHOR_COMPLETE_SUPPORT_OPTIMAL_NEWTON_AUDIT_20261025.json").read_text())
    assert len(src["records"])==len(ref["rows"])==125
    paths,_=base.c288.build_paths()
    W,_=base.src.floor_fixed_masses()
    rows=[];all_saves=[]
    for i in range(125):
        s,groups,terms,cancels,d=base.prepare(i,paths[i],int(src["records"][i][1]),W)
        M,h,N=adaptive_moduli(s,d)
        previous=ref["rows"][i]
        assert previous["index"]==i and previous["degree"]==d
        assert previous["sample_start"]==base.window_start(groups,d)
        assert previous["new_modulus_bit_length"]==M.bit_length()
        assert previous["supported_factorial_bit_length"]==h.bit_length()
        assert previous["scalar_bit_length"]==s.bit_length()
        assert previous["reference_C305_exact_gcd_match"] is True
        assert N[0]==N[-1]==M
        assert all(N[j]==N[d-j] for j in range(d+1))
        assert all(M%n==0 and n==M//gcd(M,comb(d,j)) for j,n in enumerate(N))
        savings=[M.bit_length()-n.bit_length() for n in N]
        all_saves+=savings
        rows.append({
            "index":i,"degree":d,"sample_count":d+1,
            "uniform_M_bits":M.bit_length(),
            "minimum_Nj_bits":min(n.bit_length() for n in N),
            "maximum_Nj_bits":max(n.bit_length() for n in N),
            "max_saved_bits":max(savings),
            "sum_saved_bits":sum(savings),
            "strict_improvement_nodes":sum(x>0 for x in savings),
            "median_saved_bits":median(savings),
            "C306_exact_oracle_gcd_dec":previous["gcd_decimal"],
            "C306_witness_inherited_not_reexecuted":True
        })
    audit={
      "schema":"C307_125_NODE_SCHEDULE_EXACT_AUDIT_V1",
      "classification":"EXACT_SCHEDULE_FROM_FROZEN_INPUTS_AND_C306_AUTHOR_ORACLE",
      "frozen_C293_records_sha256":src["records_sha256"],
      "path_count":len(rows),"node_count":len(all_saves),
      "nodes_strictly_smaller_than_C306":sum(x>0 for x in all_saves),
      "nodes_equal_to_C306":sum(x==0 for x in all_saves),
      "bit_reduction_min":min(all_saves),"bit_reduction_max":max(all_saves),
      "bit_reduction_median":median(all_saves),
      "bit_reduction_sum":sum(all_saves),
      "verified_scope":"125 exact modulus schedules, 44038 nodes. All C306 witness values were inherited; 44038 new reduced-numerator evaluations were NOT rerun.",
      "rows":rows
    }
    Path(output).write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
    print("C307_SCHEDULE_125_PASS",len(rows),"NODES",len(all_saves),
       "STRICT",audit["nodes_strictly_smaller_than_C306"],
       "SAVED",audit["bit_reduction_sum"],"MAX",audit["bit_reduction_max"])

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",default=str(ROOT/"C307_125_NODE_SCHEDULE_AUDIT.json"))
    run(p.parse_args().output)
