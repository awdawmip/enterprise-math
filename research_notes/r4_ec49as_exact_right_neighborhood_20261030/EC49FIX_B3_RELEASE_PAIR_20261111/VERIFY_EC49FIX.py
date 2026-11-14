#!/usr/bin/env python3
"""EC49FIX: exact B=3 key-release obstruction for the frozen 24-label BRC problem.
Import the existing sibling EC49FGW_RADIUS5_SCREEN.py; no rewritten BRC observer.
"""
from pathlib import Path
import collections,itertools,json,sys
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'
if not (HERE/'EC49FGW_RADIUS5_SCREEN.py').exists():sys.path.insert(0,str(SRC))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,pref,validate_profile
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
CATALOG=list(all_words())
assert len(CATALOG)==178850
key_services=collections.defaultdict(set)
for lab,w in CATALOG:key_services[raw_key(w)].add(lab)
assert len(key_services)==94

def cover_without(targets,fixed,slots,forbidden):
    missing=[lab for lab in targets if not any(lab in key_services[k] for k in fixed)]
    if not missing:return True
    target=(1<<len(missing))-1
    masks={sum(1<<j for j,lab in enumerate(missing) if lab in v)
           for k,v in key_services.items() if k not in fixed and k!=forbidden}-{0}
    reach={0}
    for _ in range(slots):
        reach|={a|b for a in tuple(reach) for b in masks}
        if target in reach:return True
    return False

report={'schema':'EC49FIX_B3_RELEASE_EXACT_V1','frozen_science':PIN,
        'catalog_words':len(CATALOG),'raw_keys':len(key_services),'profiles':[]}
for pr in W['profiles']:
    pid=pr['profile_id'];rows,ps=validate_profile(pr)
    labels=[(r['window'],r['signature']) for r in rows]
    old_keys={raw_key(r['word']) for r in rows}
    assert len(old_keys)==7
    ks=collections.defaultdict(int);supports=collections.defaultdict(int)
    for i,(row,path) in enumerate(zip(rows,ps)):
        ks[raw_key(row['word'])]|=1<<i
        for edge in path:supports[edge]|=1<<i
    assert len(supports)==94
    by_l=collections.defaultdict(list)
    for lab,w in CATALOG:
        if raw_key(w) in old_keys:by_l[lab].append(set(pref(w)))
    assert sum(map(len,by_l.values()))==9838
    groups={}
    for Q in itertools.combinations(range(24),6):
        mask=sum(1<<i for i in Q)
        released={k for k,s in ks.items() if (s&mask)==s}
        if not released:continue
        removed=frozenset(p for p,s in supports.items() if (s&mask)==s)
        if len(removed)!=4:continue
        group=groups.setdefault(removed,{'representative':Q,'all':0,'forced':0,
                                         'alternative':0})
        group['all']+=1
        fixed=old_keys-released
        forced=all(not cover_without([labels[i] for i in Q],fixed,len(released),k)
                   for k in released)
        group['forced' if forced else 'alternative']+=1
    assert len(groups)==10 and sum(g['all'] for g in groups.values())==8856
    detailed=[]
    for removed,g in groups.items():
        Q=g['representative'];F=set(supports)-removed
        assert len(F)==90
        H8=sorted(set(Q)&{18,19,20,21})
        assert len(H8) in (1,2)
        cand={}
        for i in H8:
            cand[i]={frozenset(P-F) for P in by_l[labels[i]] if len(P-F)<=3}
        if len(H8)==1:
            assert not cand[H8[0]]
            kind='singleton'
        else:
            i,j=H8
            assert len(cand[i])==len(cand[j])==1
            assert len(next(iter(cand[i]))|next(iter(cand[j])))==4
            assert len((ps[i]|ps[j])-F)==4
            kind='pair'
        assert g['all'] in (885,886)
        detailed.append({'Q_representative':list(Q),'class':kind,
                         'count':g['all'],'forced_original_keys':g['forced'],
                         'may_reallocate_keys':g['alternative'],
                         'H8_pair':H8,'minimum_new_prefixes_original_7_keys':4})
    detailed.sort(key=lambda x:(x['class'],x['H8_pair']))
    H8single=[g for g in detailed if g['class']=='singleton']
    H8pair=[g for g in detailed if g['class']=='pair']
    assert len(H8single)==4 and len(H8pair)==6
    (HERE/f'B3_REP_MASKS_{pid}.txt').write_text(''.join(
        str(sum(1<<i for i in g['Q_representative']))+'\n' for g in detailed))
    assert sum(g['count'] for g in H8single)==3540
    assert sum(g['forced_original_keys'] for g in H8pair)==5310
    assert sum(g['may_reallocate_keys'] for g in H8pair)==6
    assert sum(g['forced_original_keys'] for g in H8single)==3540
    assert sum(g['may_reallocate_keys'] for g in H8single)==0
    report['profiles'].append({'id':pid,'B3_released_total':8856,
         'already_singleton':3540,'new_forced_pair_exact94':5310,
         'other_key_possible_previously_resolved':6,'groups':detailed})
    print('EC49FIX_PROFILE_PASS',pid,'B3 released 8856, singleton previous 3540,',
          'new forced-key pair 5310, alternative-key previous 6',flush=True)
assert sum(p['new_forced_pair_exact94'] for p in report['profiles'])==10620
(HERE/'EXACT_REPORT_EC49FIX.json').write_text(json.dumps(report,indent=2)+'\n')
print('EC49FIX_EXACT_PASS new 10620; all within-original-seven-key B3 backgrounds certified',flush=True)
