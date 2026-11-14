#!/usr/bin/env python3
"""EC49FJX: exact retained-key radius-seven B=11 screen on frozen BRC words.

Inputs: unchanged EC49FGW_RADIUS5_SCREEN.py and EC49FGJ_SEVEN_KEY_94_WITNESSES.json,
         pinned scientific source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Theorem: pair obstruction if no at-most-eleven-new-prefix legal pair exists.
All 7 original key identities remain fixed by the 17 unchanged original paths.
"""
from __future__ import annotations
import itertools,json,sys,time,collections,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'EC49FJR'))
import EC49FGW_RADIUS5_SCREEN as g
B=11
full=list(g.all_words());assert len(full)==178850
bykey=collections.defaultdict(lambda:collections.defaultdict(list))
for lab,w in full:
 bykey[g.raw_key(w)][lab].append(tuple(g.pref(w)))
assert len(bykey)==94

def minimal_antichain(x):
    """Every retained suffix set has no strictly smaller suffix set for this demand."""
    ordered=sorted(set(x),key=lambda s:(len(s),tuple(sorted(s))))
    out=[]
    for s in ordered:
        if not any(p<=s for p in out):out.append(s)
    return out

def choices_by_label(F, keys):
    res=collections.defaultdict(set)
    for k in keys:
        for lab,paths in bykey[k].items():
            for ps in paths:
                t=0
                while t<len(ps) and ps[t] in F:t+=1
                if len(ps)-t<=B:
                    res[lab].add(frozenset(ps[t:]))
    return {lab:minimal_antichain(ss) for lab,ss in res.items()}

def minimum_pair_by_antic(lab1,lab2,options):
    aa,bb=options.get(lab1,[]),options.get(lab2,[])
    if not aa or not bb:return B+1
    m=1000
    for x in aa:
        for y in bb:
            z=len(x|y)
            if z<m:
                m=z
                if m<=B:return m
    return m

def analyze_profile(profile):
    rows,ps=g.validate_profile(profile)
    labels=tuple((x['window'],x['signature']) for x in rows)
    keys=tuple(g.raw_key(x['word']) for x in rows);K=set(keys)
    assert len(K)==7
    key_sup=collections.defaultdict(int);sup=collections.defaultdict(int)
    for i,(pp,k) in enumerate(zip(ps,keys)):
        for p in pp:sup[p]|=1<<i
        key_sup[k]|=1<<i
    assert len(sup)==94
    bgroups=collections.defaultdict(list)
    released=0
    for Q in itertools.combinations(range(24),7):
        mask=sum(1<<i for i in Q)
        if any((s&mask)==s for s in key_sup.values()):
            released+=1
            continue
        deleted=tuple(sorted(p for p,s in sup.items() if (s&mask)==s))
        if len(deleted)==B+1:bgroups[deleted].append(Q)
    assert released==192696 and sum(len(q) for q in bgroups.values())==15736 and len(bgroups)==36
    group_reports=[];covered=0;uncovered=[];pair_counts=collections.Counter()
    for gid,(deleted,Qs) in enumerate(sorted(bgroups.items()),1):
        F=set(sup).difference(deleted)
        opts=choices_by_label(F,K)
        pair_cache={};witnesses=[]
        for Q in Qs:
            found=None
            for i,j in itertools.combinations(Q,2):
                pair=tuple(sorted((labels[i],labels[j])))
                if pair not in pair_cache:
                    pair_cache[pair]=minimum_pair_by_antic(*pair,opts)
                if pair_cache[pair]>B:
                    found=(i,j,pair_cache[pair]);break
            if found is None:
                uncovered.append([list(Q),gid]);continue
            pair_counts[str((labels[found[0]],labels[found[1]]))]+=1
            witnesses.append({'positions':list(Q),'pair_positions':list(found[:2]),'minimum_among_budget_filtered_options':found[2]})
        covered+=len(witnesses)
        group_reports.append({'group':gid,'deleted_prefixes':len(deleted), 'examples_deleted_native_prefixes':[p.hex() for p in deleted[:2]],'contexts':len(Qs),'pair_excluded':len(witnesses),'survived_pair':len(Qs)-len(witnesses),'pair_queries':len(pair_cache),'min_option_counts_by_label':{f'{lab[0]}:{lab[1]}':len(a) for lab,a in opts.items()},'examples':witnesses[:4]})
        print(profile['profile_id'],'group',gid,'contexts',len(Qs),'excluded',len(witnesses),'survive',len(Qs)-len(witnesses),'opt_total',sum(map(len,opts.values())),flush=True)
    return {'profile':profile['profile_id'],'all_seven_subsets':346104,'all_retained_key_seven_subsets':153408,'B11_backgrounds':len(bgroups),'B11_cases':sum(map(len,bgroups.values())),'B11_pair_excluded':covered,'B11_pair_survived':len(uncovered),'pair_labels_frequencies':pair_counts,'groups':group_reports,'unexcluded':uncovered}

if __name__=='__main__':
    st=time.time()
    results=[analyze_profile(p) for p in g.W['profiles']]
    out={'schema':'EC49FJX_BRC_R7_B11_PAIR_EXACT_V1','source_pin':g.PIN,'method':'all legal BRC words on original seven complete raw cache keys; exact prefix-set antichain pair union','catalog_words':len(full),'all_raw_keys':len(bykey),'profiles':results,'elapsed_seconds':round(time.time()-st,3)}
    dest=Path(__file__).with_name('EC49FJX_B11_PAIR_REPORT.json')
    dest.write_text(json.dumps(out,indent=2,ensure_ascii=False,default=lambda x:dict(x) if isinstance(x,collections.Counter) else x)+'\n')
    print('FINAL',[(r['profile'],r['B11_pair_excluded'],r['B11_pair_survived']) for r in results], 'report sha256',hashlib.sha256(dest.read_bytes()).hexdigest())
