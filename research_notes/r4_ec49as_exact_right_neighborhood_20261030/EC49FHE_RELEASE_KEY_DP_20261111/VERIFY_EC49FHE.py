#!/usr/bin/env python3
"""EC49FHE: exact released-key radius-five BRC finite study (budgets <=15)."""
import json, itertools, collections, sys, time
from pathlib import Path
HERE=Path(__file__).resolve().parent
P=HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'
sys.path.insert(0,str(P))
from EC49FGW_RADIUS5_SCREEN import W,all_words,pref,raw_key,validate_profile,PIN
BUDGETS=(1,3,5,7,9,10,11,12,13,14,15)

def exact_cover(groups,retained,B):
    states={(frozenset(),frozenset())}
    for group in sorted(groups,key=len):
        next_states=collections.defaultdict(list)
        for U,K in states:
            for D,k in group:
                U1=U|D
                if len(U1)>B:continue
                K1=K if k in retained else K|{k}
                if len(retained)+len(K1)>7:continue
                next_states[K1].append(U1)
        if not next_states:return False
        states=set()
        for K,unions in next_states.items():
            minimal=[]
            for U in sorted(set(unions),key=len):
                if not any(V<=U for V in minimal):minimal.append(U)
            states.update((U,K) for U in minimal)
    return bool(states)

def key_feasible(groups,retained):
    # Exact group-cover necessary condition, without joint prefix costs.
    cand=collections.defaultdict(int);covered=0
    for j,group in enumerate(groups):
        ks={k for D,k in group}
        if ks&retained:covered|=1<<j
        for k in ks-retained:cand[k]|=1<<j
    dp={covered:0}
    for mask in cand.values():
        for old,x in list(dp.items()):
            nm=old|mask
            dp[nm]=min(dp.get(nm,100),x+1)
    return dp.get(31,100)<=7-len(retained)

def check(pr,catalog):
    rows,ps=validate_profile(pr)
    labels=[(r['window'],r['signature']) for r in rows]
    baseline=set().union(*ps)
    sup=collections.defaultdict(int);ksup=collections.defaultdict(int)
    for i,(r,pp) in enumerate(zip(rows,ps)):
        ksup[raw_key(r['word'])]|=1<<i
        for p in pp:sup[p]|=1<<i
    near={b:collections.defaultdict(list) for b in BUDGETS}
    for label,w,k,pp in catalog:
        z=0
        for p in pp:
            if p in baseline:z+=1
            else:break
        d=len(pp)-z
        for b in BUDGETS:
            if d<=b:near[b][label].append((k,pp))
    counts=collections.Counter();cases=[]
    for Q in itertools.combinations(range(24),5):
        mask=sum(1<<i for i in Q)
        released={k for k,s in ksup.items() if s&mask==s}
        if not released:continue
        B=sum(s&mask==s for s in sup.values())-1
        if B not in BUDGETS:continue
        F={p for p,s in sup.items() if s&mask!=s}
        retained=set(ksup)-released
        groups=[]
        for i in Q:
            group=[]
            for k,pp in near[B][labels[i]]:
                D=frozenset(p for p in pp if p not in F)
                if len(D)<=B:group.append((D,k))
            groups.append(group)
        if any(not g for g in groups):state='singleton_excluded'
        elif not key_feasible(groups,retained):state='key_cover_excluded'
        elif not exact_cover(groups,retained,B):state='new_joint_excluded'
        else:state='feasible'
        counts[(B,len(released),state)]+=1
        cases.append({'Q':list(Q),'B':B,'released_keys':len(released),'classification':state})
    return {'profile':pr['profile_id'],
        'counts':[{'B':b,'release':r,'status':s,'count':n} for (b,r,s),n in sorted(counts.items())],
        'cases':cases}

if __name__=='__main__':
    start=time.monotonic()
    catalog=[(lab,w,raw_key(w),tuple(pref(w))) for lab,w in all_words()]
    assert len(catalog)==178850
    profiles=[check(pr,catalog) for pr in W['profiles']]
    for p in profiles:
        n=collections.Counter(c['classification'] for c in p['cases'])
        print(p['profile'],len(p['cases']),dict(n),flush=True)
        assert len(p['cases'])==12544
        assert n=={'singleton_excluded':7456,'key_cover_excluded':416,'new_joint_excluded':4672}
    report={'schema':'EC49FHE_RELEASE_EXACT_BUDGETS_LE_15_V1',
            'frozen_pin':PIN,'legal_native_words':len(catalog),
            'budgets':list(BUDGETS),'profiles':profiles}
    (HERE/'EC49FHE_EXACT_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print('EC49FHE_EXACT_PASS',round(time.monotonic()-start,3))
