#!/usr/bin/env python3
"""Exact 93-budget key-cover test for EC49FIR's 290 true key alternatives.
Requires EC49FIR_REPRO_REPORT.json, EC49FGW_RADIUS5_SCREEN.py and its witness
JSON in current directory, all frozen to the same EC49FGJ science input.
"""
import collections as C
import json
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, raw_key, pref, validate_profile

assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
frontier = json.loads(Path('EC49FIR_REPRO_REPORT.json').read_text())
assert frontier['frozen_pin'] == PIN
catalog = list(all_words()); assert len(catalog) == 178850
keyset = {raw_key(w) for _,w in catalog}; assert len(keyset)==94
reports=[]
for profile, old in zip(W['profiles'], frontier['profiles']):
    assert profile['profile_id']==old['profile']
    rows, paths=validate_profile(profile)
    labels=[(r['window'],r['signature']) for r in rows]
    key_support=C.defaultdict(int); prefix_support=C.defaultdict(int)
    for i, (row, ps) in enumerate(zip(rows, paths)):
        key_support[raw_key(row['word'])] |= 1 << i
        for p in ps:prefix_support[p] |= 1 << i
    original_prefixes=set(prefix_support)
    min_word={}; min_extension=C.defaultdict(dict)
    for lab, word in catalog:
        k=raw_key(word); lk=(lab,k); wps=pref(word); L=len(wps)
        if L<min_word.get(lk,1000):min_word[lk]=L
        for p in wps:
            if p in original_prefixes:
                c=L-len(p)
                if c<min_extension[lk].get(p,1000):min_extension[lk][p]=c
    min_extension={lk:tuple(d.items()) for lk,d in min_extension.items()}
    counts=C.Counter(); by_B=C.Counter(); survivor=[]; excluded=[]
    for entry in old['reallocation_candidates']:
        Q,b,released,_=entry
        mask=sum(1<<i for i in Q)
        old_released={tuple(k) for k in released}
        fixed=set(key_support)-old_released
        available_slots=7-len(fixed)
        assert available_slots==len(old_released)
        by_key={}
        for k in keyset:
            labmask=0
            for j,i in enumerate(Q):
                lk=(labels[i],k)
                best=min_word.get(lk,1000)
                for p,extra in min_extension.get(lk,()):
                    if prefix_support[p] & mask != prefix_support[p] and extra<best:
                        best=extra
                if best<=b:labmask|=1<<j
            by_key[k]=labmask
        fixedmask=0
        for k in fixed:fixedmask |= by_key[k]
        new_masks={m for k,m in by_key.items() if k not in fixed and m}
        reach={fixedmask}
        for _ in range(available_slots):
            reach |= {oldmask | newmask for oldmask in tuple(reach) for newmask in new_masks}
        if 63 in reach:
            counts['necessary_budget_cover_survives']+=1
            by_B[(b,'survive')]+=1
            survivor.append(entry)
        else:
            counts['exact_94_budget_cover_proved']+=1
            by_B[(b,'excluded')]+=1
            excluded.append(entry)
    assert len(old['reallocation_candidates'])==290
    assert counts==C.Counter(necessary_budget_cover_survives=210,exact_94_budget_cover_proved=80)
    reports.append(dict(profile=profile['profile_id'], counts=dict(counts),
         by_budget=[dict(B=k[0],result=k[1],n=v) for k,v in sorted(by_B.items())],
         unresolved_210=survivor, exact94_80=excluded))
    print('EC49FIS_PROFILE_PASS',profile['profile_id'],dict(counts))
Path('EXACT_REPORT_EC49FIS.json').write_text(json.dumps(dict(
     schema='EC49FIS_BUDGET_COVER_V1',pin=PIN,profiles=reports),sort_keys=True,indent=2)+'\n')
print('EC49FIS_EXACT_PASS')
