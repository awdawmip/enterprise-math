#!/usr/bin/env python3
"""EC49EXW portable exact W1/census/H7 replay. Run inside existing PR #1730 checkout.
Examples: python VERIFY_EC49EXW.py census
          python VERIFY_EC49EXW.py h7 --timeout 60
          python VERIFY_EC49EXW.py h8 --ids 719,730,756 --timeout 60
"""
import argparse, collections, hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"EC49EXT_H8_M5_TRIPLE_173_EXACT_DP"))
from VERIFY_EC49EXT import catalog, build_input
def examine():
    cases=catalog()
    assert len(cases)==946
    assert sum(c["words"]<=700 for c in cases)==367
    tail=collections.Counter(); groups=collections.defaultdict(list); zero=[]
    for c in cases:
        if c["words"]<=700: continue
        s=c["schedule"]
        lens=[2*(sum(k)-1) for k,t in s]
        m8=s[-1][1]; assert m8==2
        g=m8*max(0,lens[-1]-max(max(lens[:-1]),lens[-1]-3))
        tail[g]+=1
        if g:
            key=(s[:-1],80-g)
            groups[key].append(c)
        else:zero.append(c)
    assert tail=={0:284,4:166,6:129},tail
    assert len(groups)==129 and sum(map(len,groups.values()))==295
    return cases,groups,zero,tail
def run():
    p=argparse.ArgumentParser();p.add_argument("mode",choices=("census","h7","h8"))
    p.add_argument("--ids",default="")
    p.add_argument("--timeout",type=float,default=60.0)
    opts=p.parse_args()
    cases,groups,zero,tail=examine()
    print(json.dumps({"mode":"census","remaining_triple":579,"tail_gain":dict(tail),"distinct_h7_inputs":len(groups),"zero_gain":len(zero)},sort_keys=True))
    if opts.mode=="census":return
    src=ROOT/"EC49EXJ_H8_M4_S6_GLOBAL_EXACT"/"EXACT_OR_MASK_DP.cpp"
    exe=Path(__file__).with_name("ec49exw_exact_dp")
    subprocess.run(["g++","-O3","-std=c++17",str(src),"-o",str(exe)],check=True)
    if opts.mode=="h7":
        tasks=[(group[0]["index"],schedule,cutoff,sorted(c["index"] for c in group))
               for (schedule,cutoff),group in groups.items()]
    else:
        ids={int(x) for x in opts.ids.split(",") if x.strip()}
        chosen=[c for c in zero if c["index"] in ids]
        assert len(chosen)==len(ids),"All ids must be zero-tail triple survivors"
        tasks=[(c["index"],c["schedule"],80,[c["index"]]) for c in chosen]
    failed=[]; results=[]
    for idx,schedule,cutoff,ids in tasks:
        input_text,nodes,nwords=build_input(schedule)
        digest=hashlib.sha256(input_text.encode()).hexdigest()
        try:
            r=subprocess.run([str(exe),str(cutoff)],input=input_text,text=True,capture_output=True,timeout=opts.timeout)
            result=r.stdout.strip()
            status=("BOUND_PASS" if r.returncode==0 and result==
                    f"BOUND_PASS minimum_total_at_least={cutoff} nodes={nodes} colors={int(input_text.splitlines()[0].split()[1])}" else "OTHER")
        except subprocess.TimeoutExpired:
            status="TIMEOUT";result=""
        if status!="BOUND_PASS":failed.append(ids)
        results.append({"index":idx,"case_ids":ids,"cutoff":cutoff,"status":status,"stdout":result,
            "nodes":nodes,"input_sha256":digest,"words":nwords})
        print(json.dumps(results[-1],sort_keys=True),flush=True)
    print(json.dumps({"attempts":len(results),"all_bound_pass":not failed,"not_verified":failed},sort_keys=True))
if __name__=="__main__":run()
