#!/usr/bin/env python3
"""Exact H6 S4 M4/M5 proof by exhaustive H5 screened native prefix OR-mask DP."""
import json,time,os
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from VERIFY_EC49ER import *
from VERIFY_EC49ES import worker,init_worker
start=time.time();fs=fibers();out={}
for m,bound in ((4,80),(5,60)):
 data=json.load(open(f'EC49ES_M{m}_SCREENED.json'))
 cs=[tuple(tuple(p) for p in ps) for ps in data['screened']]
 print('STRATUM',m,'remaining',len(cs),'total',data['total'],'bound',bound,flush=True)
 chunks=[cs[i:i+4] for i in range(0,len(cs),4)]
 parts=[];t=time.time()
 with ProcessPoolExecutor(max_workers=5,initializer=init_worker) as pool:
  for k,r in enumerate(pool.map(worker,chunks,[bound]*len(chunks),chunksize=1)):
   parts.append(r)
   if (k+1)%10==0: print('PROGRESS',m,sum(x['cases'] for x in parts),'/',len(cs),'elapsed',round(time.time()-t,1),flush=True)
 exact=min(p['minE'] for p in parts)
 assert exact<=bound,(m,exact)
 best=next(p['best'] for p in parts if p['minE']==exact)
 ver=exact_trie_opt(fs,dict(zip(range(3,7),best)),True)
 assert ver['E']==exact and ver['M']==m and ver['S']==4
 out[str(m)]={'all_cases':data['total'],'H5_prefix_screened':data['total']-len(cs),'exact_tested_cases':len(cs),'H5_lower_bound':'E(H5)+4 <= supplied H6 feasible bound, because each of four terminal T4 signatures at h6 has a distinct last primitive native edge not a prefix of a shorter operation word (prefix-free native token encoding)', 'screened_counts':data['eligible_distribution'], 'case_bound':bound,'min_E':exact,'case_within_bound':sum(p['within'] for p in parts),'best_p_h3_to_h6':[list(p) for p in best], 'witness':ver['chosen_words_by_h'], 'witness_E':ver['E'],'witness_M':ver['M'],'witness_S':ver['S'],'witness_nodes':ver['trie_nodes'], 'trie_nodes_traversed':sum(x['nodes'] for x in parts),'max_DP_states':max(x['maxstates'] for x in parts),'elapsed_sec':round(time.time()-t,2)}
 print('FINISHED',m,'minimum',exact,'witness',ver['chosen_words_by_h'],'elapsed',out[str(m)]['elapsed_sec'],flush=True)
 with open('EC49ES_INTERIM.json','w') as f:json.dump(out,f,indent=2)
points=[(90,2,6),(68,3,6),(84,3,4),(54,4,6),(out['4']['min_E'],4,4),(out['5']['min_E'],5,4)]
frontier=sorted(p for p in points if not any(q!=p and all(a<=b for a,b in zip(q,p)) for q in points))
report={'unit':'EC49ES','status':'PASS','problem':'H6 full Pareto (E distinct native signed prefix edges, M symbolic positive-BRC vector keys, S terminal observer transition signatures)','frozen_sources':{'global':'773d538180bfb49e24cffeb35c3ee75eb0628e2e','em':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'},'inherited_exact_points':'EC49ER(90,2,6),(68,3,6),(84,3,4); EC49EM(54,4,6)','results':out,'all_points':points,'pareto':frontier,'validity':'Finite 7-operation alphabet, h=2,...,6, signed native X6 return +2E1, common full positive step p by h, rational rank9 9 historical observer states, two positive BRC symbolic channels, full ordered native prefix trie', 'execution_seconds':round(time.time()-start,2)}
with open('EC49ES_EXECUTED.json','w') as f:json.dump(report,f,indent=2)
print('PARETO',frontier,'total_s',report['execution_seconds'],flush=True)
