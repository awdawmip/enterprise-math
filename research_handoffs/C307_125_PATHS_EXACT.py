#!/usr/bin/env python3
"""C307 partial or full end-to-end exact variable-modulus numerator replay.

Requires frozen C306 portable package unpacked beside this script:
C305_MODULAR_NEWTON_CONTENT.py, EM_C301_EXACT_PORTABLE/,
C305_AUTHOR_COMPLETE_MODULAR_NEWTON_AUDIT_20261025.json.
No floating-point decisions; all comparisons are exact integers.
The full 125-path replay is an available command, not an already completed run.
"""
from __future__ import annotations
import argparse,json,sys,time
from pathlib import Path
from statistics import median
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from C307_HETEROGENEOUS_NEWTON_CONTENT import adaptive_moduli,content_gcd_from_sample_residues
import C305_MODULAR_NEWTON_CONTENT as base

def adaptive_reduced_numerator_samples(groups,terms,cancels,d,T,moduli):
    eval_p=base.eval_p
    vals=[]
    for j,t in enumerate(range(T,T+d+1)):
        modulus=moduli[j]
        qv={q:eval_p(q,t) for q in groups}
        assert all(qv.values()),("denominator zero",j)
        shared_den=1
        for q,e in groups.items():
            shared_den*=qv[q]**e
        cancel=eval_p(cancels[0],t)*eval_p(cancels[1],t)
        assert cancel!=0
        lifted_modulus=modulus*abs(cancel)
        numerator=0
        for coeff,nums,powers in terms:
            den=1
            for q,e in powers.items(): den*=qv[q]**e
            assert shared_den%den==0
            term=(coeff*(shared_den//den))%lifted_modulus
            for n in nums: term=(term*eval_p(n,t))%lifted_modulus
            numerator=(numerator+term)%lifted_modulus
        assert numerator%abs(cancel)==0
        residue=(numerator//abs(cancel))%modulus
        if cancel<0:residue=(-residue)%modulus
        vals.append(residue)
    return vals

def run(indices,output):
    frozen=json.loads((ROOT/"EM_C301_EXACT_PORTABLE/C293_125_REFINED_BRACKETS.json").read_text())
    refs=json.loads((ROOT/"C305_AUTHOR_COMPLETE_MODULAR_NEWTON_AUDIT_20261025.json").read_text())["rows"]
    paths,_=base.c288.build_paths()
    W,_=base.src.floor_fixed_masses()
    assert len(frozen["records"])==len(refs)==125
    rows=[]
    for i in indices:
        started=time.monotonic()
        s,groups,terms,cancels,d=base.prepare(
            i,paths[i],int(frozen["records"][i][1]),W)
        M,h,node_moduli=adaptive_moduli(s,d)
        T=base.window_start(groups,d)
        residues=adaptive_reduced_numerator_samples(
            groups,terms,cancels,d,T,node_moduli)
        calculated=content_gcd_from_sample_residues(s,d,residues)
        assert refs[i]["index"]==i and refs[i]["degree"]==d
        assert refs[i]["content_gcd_dec"]==str(calculated),(i,"C305 mismatch")
        savings=[M.bit_length()-n.bit_length() for n in node_moduli]
        row={"index":i,"degree":d,"sample_start":T,
             "sample_count":len(node_moduli),"uniform_modulus_bits":M.bit_length(),
             "nodes_strictly_smaller":sum(q>0 for q in savings),
             "max_node_bit_saving":max(savings),
             "median_node_bit_saving":median(savings),
             "C305_gcd_match":True,
             "gcd_dec":str(calculated),
             "elapsed_seconds_observed":round(time.monotonic()-started,3)}
        rows.append(row)
        print("C307_PATH_PASS",i,"degree",d,
              "strict",row["nodes_strictly_smaller"],
              "max_saved",max(savings),flush=True)
    report={"schema":"C307_HETEROGENEOUS_CIRCUIT_PARTIAL_OR_FULL_AUDIT_V1",
            "status":"AUTHOR_EXACT_NOT_SOURCE_ADMITTED",
            "C293_records_sha256":frozen["records_sha256"],
            "paths_checked":len(rows),
            "sample_count_total":sum(r["sample_count"] for r in rows),
            "rows":rows,
            "assumptions":"C300 numerator cancellation identity; C305 author-level gcd oracle; frozen positive-rational auxiliary, not native X6"}
    Path(output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print("C307_CIRCUIT_PASS",len(rows),report["sample_count_total"])

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--indices",default="0,28,63")
    p.add_argument("--output",default=str(ROOT/"C307_CIRCUIT_AUDIT.json"))
    args=p.parse_args()
    ids=list(range(125)) if args.indices=="all" else [int(x) for x in args.indices.split(",")]
    run(ids,args.output)
