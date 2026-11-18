#!/usr/bin/env python3
"""Exact necessary joint key-cover screen after fifth-label singleton feasibility.
For each replacement label only paths fitting its own NEW-prefix budget are used;
all their raw keys are retained. Additional keys are solved by a 32-mask DP.
Complete candidate enumeration, no floating point, no assumption of fixed keys.
"""
import json,itertools,collections,time
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import W,P,all_words,pref,raw_key,validate_profile,REQ,PIN

def get_key_index(catalog,baseline):
    idx=collections.defaultdict(dict);base={}; labelkeys=collections.defaultdict(set)
    for lab,w in catalog:
        k=raw_key(w); LK=(lab,k)
        ps=pref(w);L=len(ps)
        labelkeys[lab].add(k)
        if L<base.get(LK,1000):base[LK]=L
        for p in ps:
            if p not in baseline:continue
            d=idx[p]
            if L<d.get(LK,1000):d[LK]=L
    return idx,base,labelkeys

def min_new_keys_needed(label_key_options,retained):
    m=len(label_key_options); allmask=(1<<m)-1; initial=0
    candidate_new={}
    for i,keys in enumerate(label_key_options):
        if retained & keys:initial|=1<<i
        for k in keys-retained:
            candidate_new[k]=candidate_new.get(k,0)|(1<<i)
    if initial==allmask:return 0
    dp={initial:0}
    for mask in candidate_new.values():
        old=dp.copy()
        for coverage,n in old.items():
            cand=coverage|mask
            if n+1<dp.get(cand,1000):dp[cand]=n+1
    return dp.get(allmask,1000)

def scan(pr,catalog):
    rows,ps=validate_profile(pr);labs=[(r['window'],r['signature']) for r in rows]
    keys=[raw_key(r['word']) for r in rows]
    sup=collections.defaultdict(int); key_sup=collections.defaultdict(int)
    for i,(p,k) in enumerate(zip(ps,keys)):
        for v in p:sup[v]|=1<<i
        key_sup[k]|=1<<i
    E=set(sup)
    idx,base,labkeys=get_key_index(catalog,E)
    stat=collections.Counter();interesting=[];hist=collections.Counter(); t=time.time()
    for Q in itertools.combinations(range(24),5):
        mask=sum(1<<i for i in Q)
        removed={p for p,s in sup.items() if s&mask==s}
        B=len(removed)-1
        if B<0:continue
        retained={k for k,s in key_sup.items() if s&mask!=s}
        free=7-len(retained)
        labels=[labs[i] for i in Q]
        relevant=set(labels)
        mins={LK:L for LK,L in base.items() if LK[0] in relevant}
        F=E-removed
        for p in F:
            Lp=len(p)
            for LK,L in idx[p].items():
                if LK[0] in relevant and L-Lp<mins.get(LK,1000):mins[LK]=L-Lp
        options=[{k for (ll,k),x in mins.items() if ll==l and x<=B} for l in labels]
        if any(not ks for ks in options):
            stat['singleton_rejected']+=1;continue
        stat['singleton_survived']+=1
        need=min_new_keys_needed(options,retained)
        if need>free:
            stat['key_cover_rejected']+=1;hist[(free,need)]+=1
            if len(interesting)<10:interesting.append({'Q':list(Q),'labels':labels,'B':B,'free':free,'minimum_new_keys':need,'retained':sorted(retained)})
        else:
            stat['key_cover_survived']+=1
            stat['survives_with_'+str(free)+'_new_key_slots']+=1
    return {'id':pr['profile_id'],'counts':dict(stat),'key_cover_rejected_by_slots':{str(k):v for k,v in sorted(hist.items())},
            'index_prefixes':len(idx),'keyed_terminal_states':len(base),'examples':interesting,
            'elapsed_seconds':round(time.time()-t,2)}

if __name__=='__main__':
    catalog=list(all_words());assert len(catalog)==178850
    result={'schema':'EC49FGW_RADIUS5_KEY_COVER_NECESSITY_V1','pin':PIN,'catalog_count':len(catalog),'profiles':[]}
    for pr in W['profiles']:
        r=scan(pr,catalog)
        result['profiles'].append(r)
        print(pr['profile_id'],r['counts'],r['key_cover_rejected_by_slots'],'elapsed',r['elapsed_seconds'],flush=True)
    (P/'EXACT_KEY_SCREEN_EC49FGW.json').write_text(json.dumps(result,indent=2)+'\n')
    print('EC49FGW_KEY_SCREEN_PASS')
