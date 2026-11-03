#!/usr/bin/env python3
"""EC49EXV exact H7 replay for 18 EC49EXU full-H8 timeouts.
Place this folder beside EC49EXT and EC49EXJ inside the existing PR #1730 tree.
"""
from pathlib import Path
import hashlib, json, re, subprocess, sys
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'EC49EXT_H8_M5_TRIPLE_173_EXACT_DP'))
from VERIFY_EC49EXT import catalog,build_input
EXJ=ROOT/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
TIMEOUT_IDS=(663,676,678,589,601,661,674,583,592,604,606,652,662,675,677,590,660,673)
def main():
    cases={c['index']:c for c in catalog()}
    exe=Path(__file__).with_name('EC49EXV_exact_dp')
    subprocess.run(['g++','-O3','-std=c++17',str(EXJ/'EXACT_OR_MASK_DP.cpp'),'-o',str(exe)],check=True)
    results=[];unique={}
    for idx in TIMEOUT_IDS:
        case=cases[idx];s=case['schedule']
        assert case['words'] in (577,601,675,699)
        assert tuple(t for _,t in s)==(4,4,4,4,4,2,2)
        lengths=[2*(sum(key)-1) for key,t in s]
        assert max(lengths[:-1])<=16 and lengths[-1]==18
        assert s[-1][0] not in [key for key,t in s[:-1]]
        inp,nodes,nwords=build_input(s[:-1])
        assert int(inp.splitlines()[0].split()[1])==22
        digest=hashlib.sha256(inp.encode()).hexdigest()
        if digest not in unique:
            p=subprocess.run([str(exe),'76'],input=inp,text=True,capture_output=True,timeout=90,check=True)
            stdout=p.stdout.strip()
            assert stdout==f'BOUND_PASS minimum_total_at_least=76 nodes={nodes} colors=22',stdout
            unique[digest]=stdout
        results.append(dict(index=idx,original_total_candidate_words=case['words'],nodes=nodes,input_sha256=digest,
                            cutoff_h7=76,solver_stdout=unique[digest],fresh_h8_edges_at_least=4))
    assert len(results)==18 and len(unique)==12
    print(json.dumps(dict(status='PASS',unique_h7_inputs=12,cases=results,remaining_triple=579,remaining_double=44234),indent=2))
if __name__=='__main__':main()
