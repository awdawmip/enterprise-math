#!/usr/bin/env python3
"""Complete eight-window H8/M4/S<=6 global result certificate assembly.
Exact signed-native prefix-tree integer solver evidence and independent witness.
"""
from SCREEN_H5_EC49EXJ import build_input, HERE, OPS, native, sig, T4,T2
import subprocess, json, re, time, hashlib
from collections import Counter

WITNESS={
 2:['ce','de','ec','ed'],
 3:['feg','gef'],
 4:['fegd','gefd','gefc','fegc'],
 5:['fegfg','geffg'],
 6:['geffgd','geffgc','fegfgd','fegfgc'],
 7:['fegfgfg','geffgfg'],
 8:['fegfgfgg','geffgfgg']}

def poscount(w):
    st=native(w)
    return tuple(st.count(i) for i in range(1,7))
def rank_fraction(mat):
    from fractions import Fraction
    a=[[Fraction(x) for x in row] for row in mat]
    if not a:return 0
    row=0
    for col in range(len(a[0])):
        piv=next((i for i in range(row,len(a)) if a[i][col]),None)
        if piv is None: continue
        a[row],a[piv]=a[piv],a[row]
        v=a[row][col]
        a[row]=[x/v for x in a[row]]
        for i in range(len(a)):
            if i!=row and a[i][col]:
                m=a[i][col];a[i]=[x-m*y for x,y in zip(a[i],a[row])]
        row+=1
        if row==len(a):break
    return row

def sig_row(s):
    return [(s//(5**j))%5 for j in range(9)]

def rank_observer(sigset):
    a=[]
    for j in range(9):
        row=[]
        for s in sorted(sigset):
            idx=sig_row(s)[j]
            row.extend(int(v==idx) for v in range(5))
        a.append(row)
    return rank_fraction(a)

def verify_witness():
    pref=set();keys=set();signatures=set();rows=[]
    for h,ws in sorted(WITNESS.items()):
        kset=set()
        aset=set()
        for w in ws:
            assert len(w)==h
            st=native(w)
            assert tuple(st.count(i)-st.count(-i) for i in range(1,7)) == (2,0,0,0,0,0)
            p=poscount(w);kset.add(p);keys.add(p)
            aset.add(sig(st));signatures.add(sig(st))
            for t in range(1,len(st)+1):pref.add(st[:t])
        assert len(kset)==1
        rr=rank_observer(aset)
        assert rr==9,(h,rr)
        rows.append({'h':h,'words':ws,'key':list(kset.pop()),'observation_rank':rr,
                     'signature_count':len(aset), 'cumulative_prefix_edges':len(pref)})
    assert (len(pref),len(keys),len(signatures))==(90,4,6)
    assert len(T4)==4 and len(T2)==2 and set(signatures)==set(T4)|set(T2)
    return rows

def main():
    j5=json.loads((HERE/'EC49EXJ_H5_EXECUTED.json').read_text())
    j6=json.loads((HERE/'EC49EXJ_H6_EXECUTED.json').read_text())
    j7=json.loads((HERE/'EC49EXJ_H7_EXECUTED.json').read_text())
    ana=json.loads((HERE/'EC49EXJ_ANALYTIC_EXECUTED.json').read_text())
    assert (ana['complete_schedules'],ana['residual_schedules'])==(55493,26933)
    assert (j5['screened_by_H5_bound'],j6['H6_screened_additional'],j7['H7_additional_screened'],j7['H7_residual_schedules'])==(22804,3593,528,8)
    results=[]
    for i,case in enumerate(j7['H7_residual_cases']):
        p=tuple((tuple(k),t) for k,t in case)
        inp,nn,nwords=build_input(p)
        pr=subprocess.run([str(HERE/'exact_dp'),'90'],input=inp,encoding='utf-8',capture_output=True,timeout=60)
        assert pr.returncode==0
        assert 'BOUND_PASS minimum_total_at_least=90' in pr.stdout, (i,pr.stdout)
        results.append({'case':i,'family':case,'trie_nodes':nn,'eligible_words':nwords,
                        'colors':sum(t for k,t in p),'solver_stdout':pr.stdout.strip()})
    rows=verify_witness()
    o={'status':'PASS',
       'theorem':'min{E : H=8, M=4, S<=6}=90 for frozen exact native-X6 symbolic BRC model',
       'model_pins':{'global_knowledge':'773d538180bfb49e24cffeb35c3ee75eb0628e2e','enterprise_math':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'},
       'frozen_source':'EC49EXI/EC49EXH at PR #1730 SHA 8c81ed682aa47a8714ed7ef5b6ad931f9f97e4a1',
       'all_H8_M4_family_assignments':55493,
       'fourth_key_first_at_h8_previous_lower_bound_90':28560,
       'four_keys_by_h7':26933,
       'by_H5_exact_cost_and_last_3_terminal_bounds':22804,
       'by_H6_exact_cost_and_last_2_terminal_bounds':3593,
       'by_H7_exact_bounded_cost_and_last_terminal_bound':528,
       'by_final_H8_bounded_DP':len(results),
       'unresolved_assignments':0,
       'exact_primitive_witness_resource':{'E':90,'M':4,'S':6},
       'native_witness_verification':rows,
       'last_eight_bounded_DP_cases':results,
       'stage_data_sources':['EC49EXJ_H5_EXECUTED.json','EC49EXJ_H6_EXECUTED.json','EC49EXJ_H7_EXECUTED.json'],
       'limitations':'Author-side finite exhaustive proof; not a native TASK result or independent Driver review.'}
    path=HERE/'EC49EXJ_COMPLETE_EXECUTED.json'
    path.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:o[k] for k in ('status','theorem','all_H8_M4_family_assignments','fourth_key_first_at_h8_previous_lower_bound_90','four_keys_by_h7','by_H5_exact_cost_and_last_3_terminal_bounds','by_H6_exact_cost_and_last_2_terminal_bounds','by_H7_exact_bounded_cost_and_last_terminal_bound','by_final_H8_bounded_DP','unresolved_assignments','exact_primitive_witness_resource')},ensure_ascii=False,indent=2))
    print('witness rows',rows)
if __name__=='__main__':main()
