#!/usr/bin/env python3
"""Exhaustive finite-horizon N=4 observer DFA certificate. Python 3 standard library."""
from itertools import product, combinations
from collections import defaultdict
import json

ALPHABET='012'
HORIZON=4

def words(n):
    return [''.join(w) for w in product(ALPHABET,repeat=n)]

def readout(w):
    return (int('01' in w),int('10' in w),int(len(w)>1 and w[-1]==w[-2]))

words_by_depth={t:words(t) for t in range(HORIZON+1)}
profile={}; cl={}; groups={}; transitions={}
for t in reversed(range(HORIZON+1)):
    suffixes=[z for j in range(HORIZON-t+1) for z in words(j)]
    profile[t]={h:tuple(readout(h+z) for z in suffixes) for h in words_by_depth[t]}
    if t==HORIZON:
        signature={h:readout(h) for h in words_by_depth[t]}
    else:
        signature={h:(readout(h),tuple(cl[t+1][h+a] for a in ALPHABET))
                   for h in words_by_depth[t]}
    signatures=sorted(set(signature.values()))
    cl[t]={h:signatures.index(signature[h]) for h in words_by_depth[t]}
    by_class=defaultdict(list)
    for h,c in cl[t].items():
        by_class[c].append(h)
    groups[t]=dict(sorted(by_class.items()))
    for h,h2 in combinations(words_by_depth[t],2):
        assert (cl[t][h]==cl[t][h2])==(profile[t][h]==profile[t][h2])
    if t<HORIZON:
        transitions[t]={i:{a:cl[t+1][w[0]+a] for a in ALPHABET}
                        for i,w in groups[t].items()}
        for i,ws in groups[t].items():
            for h in ws:
                for a in ALPHABET:
                    assert cl[t+1][h+a]==transitions[t][i][a]

summary=[]; witnesses={}
for t in range(HORIZON+1):
    count_fibers=defaultdict(list)
    for h in words_by_depth[t]:
        k=tuple(h.count(a) for a in ALPHABET)
        count_fibers[k].append(h)
    joint=sum(len(set(profile[t][h] for h in ws)) for ws in count_fibers.values())
    max_labels=max(len(set(profile[t][h] for h in ws)) for ws in count_fibers.values())
    summary.append((t,len(words_by_depth[t]),len(groups[t]),joint,max_labels))
    ws=[]
    for i,j in combinations(sorted(groups[t]),2):
        x,y=groups[t][i][0],groups[t][j][0]
        z=next(z for jn in range(HORIZON-t+1) for z in words(jn)
               if readout(x+z)!=readout(y+z))
        ws.append((i,j,x,y,z,readout(x+z),readout(y+z)))
    assert len(ws)==len(groups[t])*(len(groups[t])-1)//2
    witnesses[t]=ws

assert [x[2] for x in summary]==[1,3,8,14,8]
assert [x[3] for x in summary]==[1,3,9,27,43]
assert [x[4] for x in summary]==[1,1,2,6,6]
assert sum(len(x) for x in witnesses.values())==150
print('PASS: exhaustive suffix profiles, independent backward classes, all transitions, witnesses')
print('depth/words/pure_states/joint_states/max_count_aware_labels:')
for row in summary:
    print(*row)
print('witnesses:',sum(map(len,witnesses.values())))
