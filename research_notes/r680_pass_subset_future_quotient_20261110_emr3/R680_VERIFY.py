#!/usr/bin/env python3
"""R680 exact PASS-only future quotient, V27 sensor minima and S3 witness."""
from itertools import combinations, permutations
from collections import defaultdict
import json
T = tuple(combinations(range(6),3))
MATCH = (((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
PASS = ((0,1),(1,2),(2,0))
BIAS = ((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),(2,4,3,-10),(3,2,4,-10),(4,3,2,-10))
def code(s,m):
    if any((a in s)+(b in s)!=1 for a,b in m):return 0
    return 1 if sum(b in s for a,b in m)%2==0 else -1
C = {s:tuple(code(s,m) for m in MATCH) for s in T}
N = {s:tuple(t for t in T if len(set(s)&set(t))==2) for s in T}
assert len(set(C.values()))==20 and all(len(N[s])==9 for s in T)
WORDS = tuple(w for k in range(4) for w in permutations(range(3),k))
SUB = tuple(tuple(j for j in range(3) if mask&(1<<j)) for mask in range(8))
assert len(WORDS)==16
def ledger(u0,w):
    u=list(u0);M=[[0]*4 for _ in range(4)]
    for a in w:
        x,y=PASS[a];M[x][y]+=1;u[x]+=1;u[y]-=1
    return tuple(u),tuple(tuple(r) for r in M)
def winners(u0,w):
    u,M=ledger(u0,w)
    O=[[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
    p={t:sum(u[i]*C[t][i] for i in range(4)) for t in T}
    out=[]
    for s in T:
        z={t:p[t]+sum(C[s][i]*O[i][j]*C[t][j] for i in range(4) for j in range(4)) for t in N[s]}
        mx=max(z.values())
        out.append(tuple(T.index(t) for t in N[s] if z[t]==mx))
    return tuple(out)
OBS={}
for u in BIAS:
    groups=defaultdict(set)
    for w in WORDS:groups[tuple(sorted(w))].add((ledger(u,w),winners(u,w)))
    assert len(groups)==8 and all(len(v)==1 for v in groups.values())
    OBS[u]=tuple(winners(u,s) for s in SUB)
    assert len(set(OBS[u]))==8
def identifies(u,ids):
    return len({tuple(OBS[u][m][j] for j in ids) for m in range(8)})==8
single={}
for u in BIAS:
    counts=[]
    for k in range(4):
        good=[ids for ids in combinations(range(20),k) if identifies(u,ids)]
        counts.append(len(good))
        if k==3:example=good[0]
    assert counts[:3]==[0]*3 and counts[3] in (7,36)
    single[str(u)]={'counts':counts,'example':[''.join(map(str,T[i])) for i in example]}
pairs=tuple(combinations(range(8),2));cover=[]
for i in range(20):
    bits=0
    for j,u in enumerate(BIAS):
        for k,(a,b) in enumerate(pairs):
            if OBS[u][a][i]!=OBS[u][b][i]:bits|=1<<(j*len(pairs)+k)
    cover.append(bits)
full=(1<<(6*len(pairs)))-1
counts={};witness=None
for k in range(8):
    n=0
    for ids in combinations(range(20),k):
        bits=0
        for i in ids:bits|=cover[i]
        if bits==full:
            n+=1
            if witness is None:witness=ids
    counts[str(k)]=n
assert [counts[str(k)] for k in range(7)]==[0]*7 and counts['7']==86
a=(0,2,1);b=(2,1,0);compose=lambda x,y:tuple(x[y[i]] for i in range(3))
assert compose(a,b)==(1,2,0) and compose(b,a)==(2,0,1)
out={'schema':'R680_PASS_SUBSET_V27_SENSORS_EXACT_V1','role':'AUTHOR_SIDE',
'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
'R679_source':'fab76ba01a87745b098ab57a0219d958707bdbb9',
'model':'once-only three PASS labels, all future V27 winner maps and legal remaining PASS labels',
'prefix_words':16,'minimal_future_classes':8,'biases':[list(u) for u in BIAS],
'single_bias_probes':single,'common_counts':counts,
'common_seven_example':[''.join(map(str,T[i])) for i in witness],
'positive_BRC_mass':'factorial(subset size)',
'optional_S3_extension':{'AB':list(compose(a,b)),'BA':list(compose(b,a))},
'validation':'exhaustive integer arithmetic 16 prefixes x 6 baselines and all 20-choose-k sensors up to k=7',
'independent_driver_review':False}
with open('R680_EVIDENCE.json','w',encoding='utf-8') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'single':single,'common_counts':counts,'uniform':out['common_seven_example']},ensure_ascii=False,indent=2))
print('R680_PASS_SUBSET_MINIMAL_SENSOR_CERTIFICATE_PASS')
