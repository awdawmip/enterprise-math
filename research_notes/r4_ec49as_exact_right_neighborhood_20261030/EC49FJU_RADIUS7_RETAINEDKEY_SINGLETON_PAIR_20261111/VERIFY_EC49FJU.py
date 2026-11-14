#!/usr/bin/env python3
"""Exact radius-7 retained-key singleton/pair screen for frozen native BRC.
Needs frozen EC49FGW_RADIUS5_SCREEN.py and EC49FGJ_SEVEN_KEY_94_WITNESSES.json
on PYTHONPATH/in the helper's directory. All arithmetic and paths are exact.
"""
import json
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import W,PIN,raw_key,pref,validate_profile,all_words

OUT=Path('EXACT_REPORT_EC49FJU.json')
catalog=list(all_words())
assert len(catalog)==178850 and len({raw_key(w) for _,w in catalog})==94
records=[]
for profile in W['profiles']:
    rows,original=validate_profile(profile)
    keys={raw_key(d['word']) for d in rows}
    assert len(keys)==7
    allowed=defaultdict(list)
    # For a complete key retained by the fixed 17 paths, no other key is legal.
    idx=defaultdict(dict)
    shortest={}
    for lab,w in catalog:
        if raw_key(w) not in keys: continue
        ps=pref(w)
        allowed[lab].append(ps)
        shortest[lab]=min(shortest.get(lab,999),len(ps))
        for p in ps:
            v=len(ps)-len(p)
            if v<idx[p].get(lab,999):idx[p][lab]=v
    assert sum(map(len,allowed.values()))==9838
    prefix_support=defaultdict(int); key_support=defaultdict(int)
    for i,(row,ps) in enumerate(zip(rows,original)):
        key_support[raw_key(row['word'])]|=1<<i
        for p in ps:prefix_support[p]|=1<<i
    assert len(prefix_support)==94
    # Encode all baseline-prefix overlap information by a 24-bit support mask.
    suffix=defaultdict(dict)
    for p,support in prefix_support.items():
        for lab,cost in idx.get(p,{}).items():
            suffix[lab][support]=min(suffix[lab].get(support,999),cost)
    cache={};counts=Counter();by_budget=defaultdict(Counter);samples=[]
    for q in combinations(range(24),7):
        mask=sum(1<<i for i in q)
        if any((support&mask)==support for support in key_support.values()):
            continue
        budget=sum((support&mask)==support for support in prefix_support.values())-1
        counts['retained_seven']+=1
        if budget<0:
            label='fixed_94'
        else:
            labels=[(rows[i]['window'],rows[i]['signature']) for i in q]
            min_single={}
            for lab in labels:
                m=shortest[lab]
                for support,extra in suffix[lab].items():
                    if (support&mask)!=support and extra<m:m=extra
                min_single[lab]=m
            if any(m>budget for m in min_single.values()):
                label='singleton'
            elif budget in (3,5,7):
                F=frozenset(p for p,support in prefix_support.items() if (support&mask)!=support)
                def options(lab):
                    k=(F,lab,budget)
                    if k not in cache:
                        choices=set()
                        for ps in allowed[lab]:
                            if len(ps)>budget and ps[len(ps)-budget-1] not in F:
                                continue
                            start=0
                            while start<len(ps) and ps[start] in F:start+=1
                            if len(ps)-start<=budget:
                                choices.add(frozenset(ps[start:]))
                        cache[k]=tuple(choices)
                    return cache[k]
                choices={lab:options(lab) for lab in labels}
                assert all(choices.values())
                certificate=None
                for a,b in combinations(labels,2):
                    if not any(len(x|y)<=budget for x in choices[a] for y in choices[b]):
                        certificate=(a,b,min(len(x|y) for x in choices[a] for y in choices[b]))
                        break
                label='pair' if certificate else 'unresolved'
                if certificate and len(samples)<16:
                    samples.append({'q':q,'budget':budget,'pair':certificate})
            else:
                label='unresolved'
        counts[label]+=1;by_budget[str(budget)][label]+=1
    result={'profile_id':profile['profile_id'],'total_seven_subsets':346104,
            'counts':dict(counts),'by_budget':{k:dict(v) for k,v in sorted(by_budget.items(),key=lambda x:int(x[0]))},
            'pair_examples':samples,'cached_label_contexts':len(cache)}
    records.append(result)
    print('EC49FJU',profile['profile_id'],dict(counts),flush=True)
report={'schema':'EC49FJU_EXACT_RADIUS7_SCREEN_V1','frozen_scientific_pin':PIN,
        'legal_word_count':len(catalog),'raw_key_count':94,
        'scope':'seven omitted words; fixed 17 retain all original seven complete raw keys',
        'results':records}
OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('EC49FJU_EXACT_PASS',sum(r['counts'].get(k,0) for r in records for k in ('fixed_94','singleton','pair')))
