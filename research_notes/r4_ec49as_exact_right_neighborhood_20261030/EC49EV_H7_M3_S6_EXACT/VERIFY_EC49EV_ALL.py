#!/usr/bin/env python3
"""EC49EV exact finite seven-window / three symbolic BRC cache-key optimum.

Full operation and observer semantics are imported from the already published
EC49EU frozen scientific model; no new axes, observer, or scientific pins.
The C++ integer OR-mask trie kernel is the actually executed EC49EU checker.
For the three all-T4 schedules, reuse its previously verified exact report.
The 462 remaining schedules are solved with integer DP here.
"""
import argparse, json, re, subprocess, sys
from collections import Counter
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PREV=ROOT.parent/'EC49EU_H7_M3_S4_EXACT'
if not PREV.is_dir():
    PREV=ROOT  # same-directory local verification after unpacking predecessor
sys.path.insert(0,str(PREV))
from MODEL_EC49EU import BASE,P0,PAID_BASE,T4,T2,words,signature,path,rank_mod


def fibers():
    complete={};universe=set();pop={}
    for h in range(2,8):
        ff={};n=0
        for e in range(1,(h+2)//2+1):
            for x in range(2*h+1):
                for y in range(h+1):
                    p=(x,y,e,0,0,0)
                    ws=words(h,p)
                    if not ws:continue
                    n+=len(ws)
                    signatures={signature(w) for w in ws}
                    ff[p]=signatures;universe.update(signatures)
        complete[h]=ff;pop[h]=n
    assert pop=={2:8,3:51,4:304,5:1770,6:10224,7:58947}
    assert len(universe)==11 and len(universe-T4)==7
    return complete,universe,pop


def schedule_enumeration():
    complete,universe,pop=fibers()
    extras=sorted(universe-T4)
    exact_class={}
    pair_schedule_count={}
    def enumerate_assignments(domains):
        results=[]
        def visit(h,ps):
            if h==8:
                if len(set(ps))==3:results.append(tuple(ps))
                return
            for p in domains[h]:
                if len(set(ps)|{p})<=3:visit(h+1,ps+[p])
        visit(3,[P0]);return results
    for i,j in combinations(range(7),2):
        active=T4|{extras[i],extras[j]}
        domains={};types={}
        for h,ff in complete.items():
            d={};lab={}
            for p,ss in ff.items():
                have=ss&active
                if rank_mod(have)!=9:continue
                t4=T4.issubset(have);t2=T2.issubset(have)
                assert t4 != t2,(h,p,i,j)
                lab[p]='4' if t4 else '2'
                d[p]=have
            domains[h]=d;types[h]=lab
        assert list(domains[2])==[P0]
        candidates=enumerate_assignments(domains)
        special={extras[i],extras[j]}==T2
        assert len(candidates)==(465 if special else 3)
        pair_schedule_count[f'{i},{j}']=len(candidates)
        if special:exact_class={'schedule':candidates,'types':types}
    assert len(exact_class['schedule'])==465
    return exact_class,pop,pair_schedule_count


def build_trie(ps,types):
    node={():0};raw=[()];parent=[-1];paid=[1];masks=[0]
    def insert(w,bit=0):
        pre=()
        for step in path(w):
            nxt=pre+(step,)
            if nxt not in node:
                node[nxt]=len(raw);raw.append(nxt)
                parent.append(node[pre]);paid.append(int(nxt in PAID_BASE));masks.append(0)
            pre=nxt
        masks[node[pre]]|=bit
    for w in BASE:insert(w)
    labels=[]
    for h,p in zip(range(3,8),ps[1:]):
        sigs=sorted(T4 if types[h][p]=='4' else T2)
        for sig in sigs: labels.append((h,sig))
    positions={entry:k for k,entry in enumerate(labels)}
    for h,p in zip(range(3,8),ps[1:]):
        desired=T4 if types[h][p]=='4' else T2
        for w in words(h,p):
            s=signature(w)
            if s in desired:insert(w,1<<positions[(h,s)])
    assert len({p for p in raw if p in PAID_BASE})==28
    assert len(labels)<=20 and all(any(x&(1<<bit) for x in masks) for bit in range(len(labels)))
    data=f'{len(raw)} {len(labels)}\n'+''.join(f'{parent[i]} {paid[i]} {masks[i]}\n' for i in range(len(raw)))
    return data,len(raw),len(labels)


def verify_all(exe,schedules,types,quick=False):
    prev=json.loads((PREV/'EC49EU_EXACT_EXECUTED.json').read_text())
    assert prev['status']=='PASS' and [x['exact_total_edges'] for x in prev['cases']]==[116,116,128]
    exact_predecessor={tuple(tuple(p) for p in case['p_h3_to_h7']):case['exact_total_edges'] for case in prev['cases']}
    result=[]
    for sid,ps in enumerate(schedules):
        labels=''.join(types[h][p] for h,p in zip(range(3,8),ps[1:]))
        if '2' not in labels:
            cost=exact_predecessor[ps[1:]]
            out={'schedule_id':sid,'E':cost,'signature_classes':labels,'origin':'EC49EU predecessor exact DP'}
        else:
            input_data,nodes,k=build_trie(ps,types)
            r=subprocess.run([str(exe)],input=input_data,capture_output=True,text=True,check=True)
            matched=re.fullmatch(r'PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)',r.stdout.strip())
            assert matched,(sid,r.stdout)
            delta,cost,n,k0,largest,conv=map(int,matched.groups())
            assert n==nodes and k0==k and cost==delta+28
            out={'schedule_id':sid,'E':cost,'signature_classes':labels,'nodes':nodes,'terminal_colors':k,'max_live_masks':largest,'integer_convolutions':conv}
        result.append(out)
        if quick and sid==46:break
    if not quick:
        assert len(result)==465
        best=min(x['E'] for x in result)
        winners=[x['schedule_id'] for x in result if x['E']==best]
        assert best==86 and winners==[46]
    else:best=result[-1]['E'];winners=[result[-1]['schedule_id']]
    return result,best,winners


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--quick',action='store_true');ap.add_argument('--output',default='EC49EV_RERUN.json');args=ap.parse_args()
    cls,pop,pairs=schedule_enumeration()
    cpp=PREV/'VERIFY_EC49EU_EXACT_DP.cpp';exe=ROOT/'ec49ev_dp_binary'
    subprocess.run(['g++','-O3','-std=c++17',str(cpp),'-o',str(exe)],check=True)
    r,best,winners=verify_all(exe,cls['schedule'],cls['types'],args.quick)
    report={'status':'PASS','unit':'EC49EV','scope':'H=2..7/M=3/S<=6','operation_counts':pop,'signature_universe':11,'global_signature_pairs':21,'all_key_schedules':465,'exactly_reused_prior_case_count':sum('origin' in x for x in r),'new_exact_dp_case_count':sum('origin' not in x for x in r),'minimum_E':best,'winner_ids':winners,'cases':r}
    (ROOT/args.output).write_text(json.dumps(report,indent=1)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=1))

if __name__=='__main__':main()
