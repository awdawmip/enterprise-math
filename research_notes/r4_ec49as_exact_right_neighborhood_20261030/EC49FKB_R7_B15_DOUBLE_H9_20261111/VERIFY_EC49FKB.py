#!/usr/bin/env python3
"""EC49FKB: finite R7 retained-key B15, double-H9 exact obstruction.
Run next to EC49FJD_RELEASE_B11_COMPLETE_20261111; optional EC49FKB_INPUT_DIR
points to a frozen generator+witness directory. Exact integer/set operations.
"""
import collections,itertools,json,os,sys
from pathlib import Path
D=Path(os.environ.get('EC49FKB_INPUT_DIR',Path(__file__).resolve().parent.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(D))
import EC49FGW_RADIUS5_SCREEN as g
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
S={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
def path(w):
    h=();out=set()
    for c in w:
        for x in S[c]:
            h+=(x,);out.add(h)
    return frozenset(out)
def key(w):
    a=[x for c in w for x in S[c]]
    return tuple(a.count(x) for x in (1,2,3))
cat=list(g.all_words())
assert len(cat)==178850 and len({key(w) for _,w in cat})==94
report=[]
for profile in g.W['profiles']:
    rows=sorted(profile['demands'],key=lambda d:(d['window'],d['signature']))
    assert len(rows)==24
    labels=[(d['window'],d['signature']) for d in rows]
    psets=[path(d['word']) for d in rows]
    keys={key(d['word']) for d in rows}
    assert len(keys)==7 and len(set().union(*psets))==94
    prefix_s=collections.defaultdict(int); key_s=collections.defaultdict(int)
    for i,(d,P) in enumerate(zip(rows,psets)):
        key_s[key(d['word'])]|=1<<i
        for p in P:prefix_s[p]|=1<<i
    groups=collections.defaultdict(list)
    for Q in itertools.combinations(range(24),7):
        m=sum(1<<i for i in Q)
        if any((v&m)==v for v in key_s.values()):continue
        rem=frozenset(p for p,v in prefix_s.items() if (v&m)==v)
        if len(rem)==16:groups[rem].append(Q)
    assert len(groups)==67 and sum(map(len,groups.values()))==4336
    large=[(r,Q) for r,Q in groups.items() if len(Q)==1762]
    assert len(large)==1
    removed,Qs=large[0]
    assert all({(9,16),(9,32)}.issubset({labels[i] for i in Q}) for Q in Qs)
    F=set(prefix_s)-set(removed)
    assert len(F)==78
    eligible={lab:[] for lab in ((9,16),(9,32))}
    raw=collections.Counter()
    for lab,w in cat:
        if lab in eligible and key(w) in keys:
            raw[lab]+=1
            delta=path(w)-F
            if len(delta)<=15:eligible[lab].append((w,delta))
    assert [raw[l] for l in eligible]==[280,280]
    assert [len(eligible[l]) for l in eligible]==[35,35]
    joined=[(len(u|v),w,t) for w,u in eligible[(9,16)] for t,v in eligible[(9,32)]]
    assert len(joined)==1225
    mincost=min(x[0] for x in joined)
    assert mincost==16
    witness=next((a,b) for n,a,b in joined if n==mincost)
    report.append({'profile':profile['profile_id'],'seven_subsets':346104,'retained_key_B15':4336,'backgrounds':67,'target_contexts':1762,'fixed_prefixes':78,'remaining_labels':[[9,16],[9,32]],'allowed_raw_candidates_per_label':280,'allowed_budget_candidates_per_label':35,'tested_pairs':1225,'minimum_joint_new_prefixes':mincost,'exact_total':94,'witness_words':witness,'example_Q':list(Qs[0])})
    print('EC49FKB_PAIR_PASS',profile['profile_id'],1762,mincost,1225,flush=True)
print('EC49FKB_B15_H9_EXACT_3524_PASS',flush=True)
print(json.dumps({'schema':'EC49FKB_B15_H9_EXACT','frozen_pin':g.PIN,'profiles':report},sort_keys=True))
