#!/usr/bin/env python3
"""EC49FRR-B: exact full original-native BRC Bellman joint-surcharge certificate.
Run: python EC49FRR_JOINT_SURCHARGE_PHASE_VERIFY_20261117.py <EC49FRQ-full-release-root> <output-json>
Needs inherited archive source/, code/, evidence/ from EC49FRQ; no surrogate response model.
"""
from pathlib import Path
from functools import cache
import json,sys,hashlib
base=Path(sys.argv[1]).resolve();sys.path.insert(0,str(base/'code'))
from EC49FRQ_INDEPENDENT_ALL228 import PARTS,OBS,ALL,representatives,multiplicities,subset_keys
from EC49FQI_NATIVE_DATA import V,weights,cost_pair,PIN,MASTER,CSV,keys,reps
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((base/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((base/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(OBS)==len(V)==228 and len(weights)==141 and sum(weights)==310
assert representatives==reps and multiplicities==weights
assert all(OBS[i]==V[i] for i in range(144))
assert set(keys)==set(subset_keys) and len(keys)==len(subset_keys)==84
assert all(OBS[144+j]==V[144+keys.index(k)] for j,k in enumerate(subset_keys))
@cache
def solve(s):
    if s.bit_count()==1:return (0,())
    best=10**30;first=[]
    for q,part in enumerate(PARTS):
        children=[s&t for t in part if s&t]
        if len(children)<2:continue
        c=143 if q in (32,34) else 141
        v=c*s.bit_count()+sum(solve(t)[0] for t in children)
        if v<best:best=v;first=[q]
        elif v==best:first.append(q)
    return best,tuple(first)
value,first=solve(ALL)
assert (value,first)==(42018,(32,34,140,142))
base0=json.loads((base/'evidence/x1-1_l0-1.json').read_text())
root_ties=json.loads((base/'evidence/x1-1_l155-1847.json').read_text())
assert base0['optimal_total_uniform']==296 and base0['optimal_first_uniform']==[32,34]
assert {'140','142'}<=set(root_ties['all_optimal_first_trees'])
def replay(tree):
    paths={32:0,34:0}
    for i in range(141):
        n=tree;seen=set()
        while 'leaf' not in n:
            q=n['q'];assert 0<=q<228 and q not in seen
            seen.add(q)
            if q in paths:paths[q]+=1
            n=n['children'][str(V[q][i])]
        assert n['leaf']==i
    costs=cost_pair(tree)
    return {'root':tree['q'],'U_1':costs['U_total'],'M_1':costs['M_total'],
            'charged_uses_on_141_states':sum(paths.values()),'q32_uses':paths[32],
            'q34_uses':paths[34]}
A=replay(base0['all_optimal_first_trees']['32'])
Ap=replay(base0['all_optimal_first_trees']['34'])
B=replay(root_ties['all_optimal_first_trees']['140'])
Bp=replay(root_ties['all_optimal_first_trees']['142'])
assert [v['U_1'] for v in (A,Ap,B,Bp)]==[296,296,298,298]
assert [v['charged_uses_on_141_states'] for v in (A,Ap,B,Bp)]==[141,141,0,0]
assert all(141*v['U_1']+2*v['charged_uses_on_141_states']==value for v in (A,Ap,B,Bp))
cert={'schema':'EC49FRR_JOINT_NAMED_QUERY_SURCHARGE_PHASE_CERTIFICATE_V1','scientific_pin':PIN,
      'master_sha256':MASTER,'profile_sha256':CSV,
      'at_critical_point':{'epsilon':'2/141','integer_bellman_minimum':value,
                           'all_optimal_first_physical_observations':list(first),
                           'recursive_state_subsets':solve.cache_info().currsize},
      'source_root_index_alignment':'Original (root,subset) key bijection; native terminal q indices 0..143 preserved',
      'baseline':{'cost':296,'first':[32,34]},'witnesses':{'A':A,'A_prime':Ap,'B':B,'B_prime':Bp},
      'theorem':'For all real eps>=0, V(eps)/t=min(296+141eps,298)/141; optimal-first actions phase transition at eps=2/141',
      'status':'AUTHOR_PROVED/EXACT_FINITE_BELLMAN_228/NOT_REVIEWED'}
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).with_suffix('.json')
out.write_text(json.dumps(cert,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
print('PASS full original-native 228-observation Bellman 42018; first',first,'subsets',solve.cache_info().currsize)
