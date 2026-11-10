#!/usr/bin/env python3
"""EC49FIP exact B=10,12 fixed-seven-key classifier.
Dependencies: frozen EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py,
its EC49FGJ_SEVEN_KEY_94_WITNESSES.json, and EC49FIO's generated TRIE_A/B.txt
plus compiled VERIFY_EC49FIO.cpp pair/triple solver named 'verify_pair_triple'.
Put dependencies beside this file, as described in README. Execute:
python VERIFY_EC49FIP.py A
python VERIFY_EC49FIP.py B
"""
import collections,hashlib,itertools,json,pathlib,subprocess,sys
R=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(R/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,raw_key,validate_profile
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
profile_filter=sys.argv[1] if len(sys.argv)>1 else None
if profile_filter is not None: assert profile_filter in ('A','B')
result={'schema':'EC49FIP_B10_B12_FIXED_SEVEN_KEY_EXACT_V1','frozen_scientific_pin':PIN,'profiles':{}}
for prof in W['profiles']:
    if profile_filter is not None and prof['profile_id']!=profile_filter:continue
    name=prof['profile_id'];rows,paths=validate_profile(prof)
    ps=collections.defaultdict(int);ks=collections.defaultdict(int)
    for i,(row,path) in enumerate(zip(rows,paths)):
        for p in path:ps[p]|=1<<i
        ks[raw_key(row['word'])]|=1<<i
    assert len(ps)==94 and len(ks)==7
    result['profiles'][name]={}
    for B in (10,12):
        Q=[]
        for q in itertools.combinations(range(24),6):
            m=sum(1<<i for i in q)
            if sum((s&m)==s for s in ps.values())!=B+1:continue
            if any((s&m)==s for s in ks.values()):continue
            Q.append(q)
        path=R/f'QS_{name}_{B}.txt'
        path.write_text(''.join(' '.join(map(str,q))+'\n' for q in Q))
        raw=subprocess.check_output([str(R/'verify_pair_triple'),str(R/f'TRIE_{name}.txt'),str(path),str(B)],text=True)
        lines=raw.splitlines(); report=json.loads(lines[0])
        assert report['checked']==len(Q) and report['survivors']==0
        assert len(lines)==1
        assert report['pair_excluded']+report['triple_excluded']==len(Q)
        result['profiles'][name][str(B)]={'positions':len(Q),'pair_excluded':report['pair_excluded'],
            'triple_excluded':report['triple_excluded'],'candidate_93':0,
            'new_prefix_lower_bound':B+1,'original_completion_new_prefixes':B+1,
            'exact_total_optimum':94,'q_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
assert all(v['10']['positions']==2572 and v['12']['positions']==2970 for v in result['profiles'].values())
result['total_positions']=sum(d[str(j)]['positions'] for d in result['profiles'].values() for j in (10,12))
(R/('EXACT_REPORT_EC49FIP_'+(profile_filter or 'AB')+'.json')).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True,indent=2))
print('EC49FIP_EXACT_B10_B12_PASS')
