#!/usr/bin/env python3
"""EC49FIU: exact unrestricted-key four-H8 group native-prefix B=9 lower bound."""
import collections, hashlib, itertools, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,validate_profile
sys.path.insert(0,str(ROOT/'EC49FHD_PREFIX_TRIE_RADIUS5_20261110'))
from VERIFY_EC49FHD import solve_group_tree,native_word,brute_crosscheck
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
brute_crosscheck()
full=list(all_words());assert len(full)==178850
H8=[(8,1),(8,2),(8,4),(8,8)];options=collections.defaultdict(list)
for lab,w in full:
    if lab in H8:options[lab].append(native_word(w))
assert [len(options[h]) for h in H8]==[28063,34777,28063,34777]
report={'schema':'EC49FIU_EXACT_UNRESTRICTED_H8_B9_V1','pin':PIN,
        'complete_candidate_count':len(full), 'h8_candidate_counts':[len(options[h]) for h in H8],
        'profiles':[]}
for pr in W['profiles']:
    rows,paths=validate_profile(pr)
    byfixed=collections.defaultdict(list)
    for i,j in itertools.combinations(range(24),2):
        if i in (18,19,20,21) or j in (18,19,20,21):continue
        Q=tuple(sorted((18,19,20,21,i,j)))
        F=frozenset().union(*(paths[t] for t in range(24) if t not in Q))
        if len(F)==84:
            added=set().union(*(paths[t] for t in Q))-F
            assert len(added)==10
            byfixed[F].append(Q)
    assert len(byfixed)==4 and sorted(map(len,byfixed.values()))==[13]*4
    groups=[];excluded=0
    for F,qs in byfixed.items():
        m,stats=solve_group_tree([options[x] for x in H8],set(F))
        assert m in (9,10),(pr['profile_id'],m)
        excluded+=(m>9)*len(qs)
        groups.append({'Q':[list(q) for q in qs], 'count':len(qs),
                       'fixed_prefixes_hex':sorted(p.hex() for p in F),
                       'fixed_prefix_sha256':hashlib.sha256(b'\n'.join(sorted(F))).hexdigest(),
                       'min_new_prefixes_for_four_H8':m,'B93':9,
                       '94_proved':m>9, 'trie_nodes':stats['trie_nodes']})
    assert excluded==26,(pr['profile_id'],excluded)
    report['profiles'].append({'id':pr['profile_id'],'Q_with_all_four_H8_and_F84':52,
                               'distinct_F':4,'excluded_94_optimal':excluded,
                               'unresolved_at_this_bound':52-excluded,'groups':groups})
    print('EC49FIU_PROFILE_PASS',pr['profile_id'],'H8_Q',52,
          'new_94',excluded,'minima',sorted(g['min_new_prefixes_for_four_H8'] for g in groups),flush=True)
report['new_94_profile_cases']=sum(p['excluded_94_optimal'] for p in report['profiles'])
assert report['new_94_profile_cases']==52
(HERE/'EXACT_REPORT_EC49FIU.json').write_text(json.dumps(report,indent=2)+'\n')
print('EC49FIU_EXACT_PASS 52 newly excluded six-label backgrounds',flush=True)
