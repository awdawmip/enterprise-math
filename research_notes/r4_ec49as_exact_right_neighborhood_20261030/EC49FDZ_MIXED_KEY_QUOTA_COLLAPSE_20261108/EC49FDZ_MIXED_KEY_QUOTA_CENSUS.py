#!/usr/bin/env python3
"""Exact finite rank/quota census allowing per-window mixing of three full typed BRC keys.
Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from itertools import combinations
from collections import defaultdict, Counter
import json
from pathlib import Path
# The native original six-symbol nine-history automaton; see immutable science pin.
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)
def rank9(mask):return all(mask & c for c in CLAUSES)
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
def word_pool(h,k):
    """Enumerate complete literal operation words independently of aggregate key-count DP."""
    x,y,z=k; a=z-1;r=x+y-h-1; f=h+1-y-2*z;g=h+1-x
    if min(a,r,f,g)<0:return []
    counts={'a':a,'c':0,'d':0,'e':z,'f':f,'g':g}
    out=[]
    def walk(left,w,q):
        if not left:
            if SIG[q]:
                path=[step for symbol in w for step in OPS[symbol]]
                from collections import Counter
                c=Counter(path)
                assert tuple(c[i]-c[-i] for i in range(1,7))==(2,0,0,0,0,0)
                assert tuple(c[i] for i in (1,2,3))==k
                out.append(SIG[q])
            return
        for i,sym in enumerate('acdefg'):
            if counts[sym]:
                counts[sym]-=1;w.append(sym);walk(left-1,w,TRANS[q][i]);w.pop();counts[sym]+=1
    for nc in range(r+1):
        counts['c']=nc;counts['d']=r-nc
        walk(h,[],0)
    return out
Q={4:2,5:4,6:2,7:4,8:4,9:2}
state={(0,0,0,0,0,0,0):1}
profiles={}
for h in range(1,10):
    nxt=defaultdict(int)
    for s,m in state.items():
        for i in range(6):
            t=(*tuple(s[j]+int(j==i) for j in range(6)),TRANS[s[6]][i]);nxt[t]+=m
    state=nxt
    if h not in Q:continue
    rec=defaultdict(lambda: defaultdict(int))
    for (a,c,d,e,f,g,q),n in state.items():
        if e!=a+1 or not SIG[q]:continue
        k=(2*e+c+d+f,c+d+g,e)
        rec[k][SIG[q]]+=n
    profiles[h]={k:dict(s) for k,s in rec.items()}
keys=sorted(set().union(*(p.keys() for p in profiles.values())))
assert len(keys)==155
fullpairs=set()
for t in combinations(keys,2):
    if all(rank9(__import__('functools').reduce(int.__or__,(b for k in t for b in profiles[h].get(k,{})),0)) for h in Q):
        fullpairs.add(t)
assert len(fullpairs)==124

def minimal_quota(h, t):
    joint=Counter()
    for k in t:joint.update(profiles[h].get(k,{}))
    mask=0
    for s,n in joint.items():
        if n:mask|=s
    # The nine-history Boolean observer has four clauses (16|2),(16|4),(32|1),(32|8).
    # Each complete word supplies exactly one signature. Every minimal hitting set has size <= 4.
    # For q=2, only hitting set is {16,32}. For q=4 there are the four alternatives below.
    q=Q[h]
    if sum(joint.values())<q:return (False,0,mask,dict(joint))
    choices=[(16,32),(16,1,8),(32,2,4),(1,2,4,8)]
    hits=[c for c in choices if len(c)<=q and all(joint[x]>0 for x in c)]
    return (bool(hits),min(map(len,hits)) if hits else 0,mask,dict(joint))

valid=[];unfit=Counter();examples={};min_cover=Counter();four_quota_min={h:10**9 for h in (5,7,8)}
for t in combinations(keys,3):
    if any(not rank9(__import__('functools').reduce(int.__or__,(b for k in t for b in profiles[h].get(k,{})),0)) for h in Q):continue
    if any(p in fullpairs for p in combinations(t,2)):continue
    status={h:minimal_quota(h,t) for h in Q}
    for h in four_quota_min:
        count=sum(sum(profiles[h].get(k,{}).values()) for k in t)
        four_quota_min[h]=min(four_quota_min[h],count)
    missed=tuple(h for h in Q if not status[h][0])
    if missed:
        unfit[missed]+=1
        if missed not in examples:examples[missed]={'keys':t,'profiles':{str(h):status[h][3] for h in missed}}
        continue
    valid.append(t)
    min_cover[tuple(status[h][1] for h in Q)]+=1
assert len(valid)+sum(unfit.values())==6734
assert min(four_quota_min.values())>=4
A=((3,2,1),(4,1,1))
B=((3,4,1),(5,2,2),(6,1,1),(6,1,2))
C=((4,6,1),(5,5,1),(6,4,2),(7,3,1),(7,3,2),(8,2,1),(8,2,2),(8,2,3))
three_phase_set={tuple(sorted((a,b,c))) for a in A for b in B for c in C}
assert len(three_phase_set)==64
assert set(valid)==three_phase_set,('mixed quota triples not equal to 64 quota three-phase families', set(valid)^three_phase_set)
# Constructive finite rank-and-quota verification of the three blocks H4 | H5,H6 | H7,H8,H9.
for a in A:
    assert minimal_quota(4,(a,))[0]
for b in B:
    assert all(minimal_quota(h,(b,))[0] for h in (5,6))
for c in C:
    assert all(minimal_quota(h,(c,))[0] for h in (7,8,9))
# Direct exhaustive operator-word cross-check for every (h,key) in the 64 remaining triples and H4 exceptions.
exception_keys=[(2,3,1),(4,1,2),(5,0,1),(5,0,2),(6,4,1)]
all_checked_keys=set(exception_keys).union(*(set(t) for t in valid))
literal_checks=0
for h in (4,6,9):
    for k in all_checked_keys:
        literal=word_pool(h,k)
        counts=Counter(literal)
        assert dict(counts)==profiles[h].get(k,{}),(h,k,counts,profiles[h].get(k,{}))
        literal_checks+=1

print('rank-feasible genuine triples',6734, 'quota feasible with mixing',len(valid), 'rejected',sum(unfit.values()))
print('missed windows histogram',dict(unfit));print('minimal covers',dict(min_cover));print('four word quota window minimum accepted words',four_quota_min); print('literal (h,key) profiles verified',literal_checks)
for missing in sorted(examples,key=lambda x:(len(x),x)):
 print('first failure',missing,'keys',examples[missing]['keys'])
report={'schema':'EC49FDZ_MIXED_KEY_QUOTA_CENSUS_V1','science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','genuine_three_key_rank_feasible':6734,
 'unrestricted_per_window_mixing_quota_feasible':len(valid),'unrestricted_per_window_mixing_quota_infeasible':sum(unfit.values()),
 'four_word_quota_windows_min_accepted_word_count_for_rank_triples':four_quota_min,
 'quota_feasibility_determined_by_H4_H6_H9':True,
 'identical_key_triples_to_64_quota_three_phase_family':True,
 'independent_literal_horizon_key_profile_checks':literal_checks,
 'quota_infeasible_by_failed_window_subset':{str(k):v for k,v in sorted(unfit.items())},
 'local_min_signature_cover_size_histogram':{str(k):v for k,v in sorted(min_cover.items())},
 'exceptional_h4_mixed_rank_key_triples':[[[2,3,1],[5,0,1],[6,4,1]],[[2,3,1],[5,0,2],[6,4,1]],[[4,1,2],[5,0,1],[6,4,1]],[[4,1,2],[5,0,2],[6,4,1]]],
 'first_infeasible_profiles':{str(k):v for k,v in examples.items()},'sample_quota_feasible_triples':valid[:12],
 'scope':'Full three-key rank-only family EC49FDU, arbitrary key mixture at each H4..H9, exact per-window quotas. Every chosen triple is genuinely three-key necessary by fullpair definition. No native-prefix minimization; changed early key budgets remain outside this scope.'}
Path(__file__).with_name('EC49FDZ_MIXED_QUOTA_RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
Path(__file__).with_name('EC49FDZ_MIXED_QUOTA_VALID_KEYS.json').write_text(json.dumps(valid,separators=(',',':'))+'\n')
