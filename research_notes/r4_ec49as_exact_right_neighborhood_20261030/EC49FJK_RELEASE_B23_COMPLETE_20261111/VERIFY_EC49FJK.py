#!/usr/bin/env python3
"""EC49FJK B=23: exact radius-six released-key theorem for frozen EC49FGJ witnesses.

Dependencies (same directory): EC49FGW_RADIUS5_SCREEN.py,
EC49FGJ_SEVEN_KEY_94_WITNESSES.json. Python >=3.9, exact integers.
"""
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
import json
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,pref,validate_profile

CAP = 24 # We test a 93-edge candidate: with |F|=70 this means <=23 new prefixes.
C = list(all_words())
assert len(C)==178850
by_label_key=defaultdict(list)
key_coverage=defaultdict(set)
for lab,w in C:
    k=raw_key(w)
    by_label_key[lab,k].append(w)
    key_coverage[k].add(lab)
assert len(key_coverage)==94

def exact_trie(F,labels,allowed_keys,cap=CAP):
    """Exact minimum new native prefix count clipped at CAP=24.

    A rooted native prefix edge corresponds to a signed ordered X6 microstep.
    Node-state DP tracks the subset of six distinct labels met in a subtree.
    Edge costs are 0 for prefixes in F and 1 for new prefixes.
    """
    ch=[{}]; ends=[0]; edgecost=[0]
    for j,lab in enumerate(labels):
        for k in allowed_keys:
            for w in by_label_key.get((lab,k),()):
                u=0
                for p in pref(w):
                    a=p[-1]
                    v=ch[u].get(a)
                    if v is None:
                        v=len(ch);ch[u][a]=v
                        ch.append({});ends.append(0);edgecost.append(int(p not in F))
                    u=v
                ends[u] |= 1<<j
    dp=[None]*len(ch)
    for u in range(len(ch)-1,-1,-1):
        em=ends[u]
        state={m:0 for m in range(64) if m & ~em ==0}
        for v in ch[u].values():
            nxt=state.copy()
            for s,c0 in state.items():
                for t,c1 in dp[v].items():
                    if s&t:continue
                    tot=c0+c1+edgecost[v]
                    if tot < nxt.get(s|t,cap):nxt[s|t]=tot
            state={s:c for s,c in nxt.items() if c<cap}
        dp[u]=state
    return dp[0].get(63,cap), len(ch)

def support_masks(rows,paths):
    sp=defaultdict(int);sk=defaultdict(int)
    for i,(r,ps) in enumerate(zip(rows,paths)):
        sk[raw_key(r['word'])] |= 1<<i
        for p in ps:sp[p] |= 1<<i
    assert len(sp)==94 and len(sk)==7
    return sp,sk

reports=[]
for profile in W['profiles']:
    rows,paths=validate_profile(profile)
    sp,sk=support_masks(rows,paths)
    oldkeys=set(sk)
    n_cases=0
    for Q in combinations(range(24),6):
        mask=sum(1<<i for i in Q)
        removed=sum((v&mask)==v for v in sp.values())
        if removed !=24:continue
        released={k for k,v in sk.items() if (v&mask)==v}
        if not released:continue
        assert len(released)==1
        F={p for p,v in sp.items() if (v&mask)!=v}
        assert len(F)==70
        fixed=oldkeys-released
        assert len(fixed)==6
        labels=[(rows[i]['window'],rows[i]['signature']) for i in Q]
        uncovered={lab for lab in labels if not any(lab in key_coverage[k] for k in fixed)}
        additional=[k for k in key_coverage if k not in fixed and uncovered.issubset(key_coverage[k])]
        assert released.issubset(additional)
        mincost=CAP
        maxnodes=0
        for k in additional:
            cost,nodes=exact_trie(F,labels,fixed|{k})
            maxnodes=max(maxnodes,nodes)
            if cost<mincost: mincost=cost
            if cost<CAP:raise AssertionError(('FOUND_93_OR_BETTER',profile['profile_id'],Q,k,cost))
        assert mincost==24
        orig=set().union(*(paths[i] for i in range(24)))
        assert len(orig)==94 and len(orig-F)==24
        reports.append({'profile':profile['profile_id'],'Q':list(Q),'F':70,
                        'new_prefix_budget_93':23,'released_key':list(next(iter(released))),
                        'allowed_seventh_key_count':len(additional),
                        'minimum_new_prefixes':24,
                        'trie_node_count_max':maxnodes})
        n_cases+=1
    assert n_cases==9,(profile['profile_id'],n_cases)
assert len(reports)==18
summary={'schema':'EC49FJK_EXACT_FINITE_V1', 'frozen_science_pin':PIN,
         'candidate_words':len(C), 'full_raw_keys':len(key_coverage),
         'cases':18, 'counts':{'A':9,'B':9},
         'forced_old_key_cases':sum(x['allowed_seventh_key_count']==1 for x in reports),
         'flexible_key_cases':sum(x['allowed_seventh_key_count']>1 for x in reports),
         'all_min_cost':94,'results':reports}
Path('EXACT_REPORT_EC49FJK.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'cases':18,'forced':summary['forced_old_key_cases'],'flexible':summary['flexible_key_cases'],
    'keys_histogram':dict(Counter(x['allowed_seventh_key_count'] for x in reports)),'all_min_cost':94},ensure_ascii=False))
print('EC49FJK_ALL_18_PASS')
