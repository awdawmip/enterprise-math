#!/usr/bin/env python3
"""Exact EC49FIT: key-unrestricted four-H8-label lower bound, 91 cases/profile.
Run: python research_notes/r4_ec49as_exact_right_neighborhood_20261030/
               EC49FIT_H8_QUADRUPLE_B7_20261111/VERIFY_EC49FIT_PORTABLE.py
The frozen EC49FGW/EC49FHD sibling evidence supplies original generator and trie.
"""
import collections, hashlib, itertools, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,STEPS,all_words,pref,raw_key,validate_profile
sys.path.insert(0,str(ROOT/'EC49FHD_PREFIX_TRIE_RADIUS5_20261110'))
from VERIFY_EC49FHD import solve_group_tree,native_word,brute_crosscheck
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
BRUTE=brute_crosscheck()
full=list(all_words());assert len(full)==178850
by_label=collections.defaultdict(list)
for lab,w in full:
    if lab[0]==8:
        by_label[lab].append(native_word(w))
labels=((8,1),(8,2),(8,4),(8,8))
options=[by_label[l] for l in labels]
assert [len(x) for x in options]==[28063,34777,28063,34777]
report={'schema':'EC49FIT_H8_UNRESTRICTED_QUADRUPLE_B7_V1','pin':PIN,
        'source':'frozen EC49FGW and EC49FHD verifiers + EC49FGJ A/B witnesses',
        'catalog_words':len(full), 'H8_candidates':[len(x) for x in options],
        'unrestricted_raw_key_count':len({raw_key(w) for _,w in full}),
        'profiles':[]}
assert report['unrestricted_raw_key_count']==94
for pr in W['profiles']:
    rows,ps=validate_profile(pr)
    sup=collections.defaultdict(int)
    for i,p in enumerate(ps):
        for pref0 in p:sup[pref0]|=1<<i
    assert len(sup)==94
    chosen=[];F0=None
    for i,j in itertools.combinations(range(24),2):
        if i in (18,19,20,21) or j in (18,19,20,21):continue
        Q=tuple(sorted((18,19,20,21,i,j)))
        mask=sum(1<<x for x in Q)
        F={p for p,m in sup.items() if m & mask != m}
        if len(F)!=86:continue
        assert F0 is None or F==F0
        F0=F
        original_added=set().union(*(ps[x] for x in Q))-F
        assert len(original_added)==8
        chosen.append(Q)
    assert len(chosen)==91
    m,stat=solve_group_tree(options,F0)
    assert m==8,(pr['profile_id'],m)
    sha=hashlib.sha256(b'\n'.join(sorted(F0))).hexdigest()
    rec={'id':pr['profile_id'],'positions':len(chosen),'Q':[list(q) for q in chosen],
         'fixed_prefix_count':len(F0),'fixed_prefix_sha256':sha,
         'trie_nodes':stat['trie_nodes'],'min_h8_new_signed_prefixes':m,
         'min_full_cost_at_least':len(F0)+m,'original_upper_bound':94,
         '93_prefix_completion_possible':False}
    report['profiles'].append(rec)
    print('EC49FIT_PASS',pr['profile_id'],'cases',len(chosen),'min',m,
          'fixed',len(F0),'trie',stat['trie_nodes'],flush=True)
assert sum(p['positions'] for p in report['profiles'])==182
(HERE/'EXACT_REPORT_EC49FIT_PORTABLE.json').write_text(json.dumps(report,indent=2)+'\n')
print('EC49FIT_EXACT_PASS:182 key-unrestricted H8 quadruple exclusions',flush=True)
