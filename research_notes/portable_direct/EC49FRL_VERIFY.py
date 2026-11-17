#!/usr/bin/env python3
"""EC49FRL native BRC exact certificate verifier, 2026-11-17.

Place next to code/EC49FQI_NATIVE_DATA.py in the inherited EC49FRK release
(which must also include source/frozen_original_master.txt and
source/EC49FPG_PROFILE.csv), then execute with Python >=3.10.
The full 228 depth-two witness cells and A/B trees are in the
EC49FRL_ADAPTIVE_OPTIMALITY_CERTIFICATE.json deliverable.
"""
import hashlib
import itertools
import math
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from EC49FQI_NATIVE_DATA import V, weights, reps, PIN, MASTER, CSV

ROOT=Path(__file__).resolve().parent.parent
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert hashlib.sha256((ROOT/"source/frozen_original_master.txt").read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((ROOT/"source/EC49FPG_PROFILE.csv").read_bytes()).hexdigest()==CSV
assert len(V)==228 and len(weights)==len(reps)==141 and sum(weights)==310
P=(8,139)
Q=(46,140)
assert all(weights[i]==1 for i in P+Q)
T=range(144)
R=range(144,228)
FULLSTATE=tuple(range(141))

@lru_cache(None)
def parts(q,S):
    d=defaultdict(list)
    for i in S:
        d[V[q][i]].append(i)
    return tuple(tuple(g) for g in d.values())

signatures=defaultdict(list)
for i in FULLSTATE:
    signatures[tuple(V[q][i] for q in T)].append(i)
assert len(signatures)==139
assert sorted(tuple(g) for g in signatures.values() if len(g)>1)==[P,Q]

pairs=list(itertools.combinations(FULLSTATE,2))
assert len(pairs)==9870
bits=[]
for q in range(228):
    b=0
    for k,(i,j) in enumerate(pairs):
        if V[q][i]!=V[q][j]:
            b|=1<<k
    bits.append(b)
allpairs=(1<<9870)-1
tested=0
maxcovered=0
for a in range(226):
    for b in range(a+1,227):
        pre=bits[a]|bits[b]
        for c in range(b+1,228):
            v=(pre|bits[c]).bit_count()
            maxcovered=max(maxcovered,v)
            tested+=1
            assert v<9870
assert tested==1949476 and maxcovered==9866
for ids in [(34,36,66,148),(117,132,153,161)]:
    union=0
    for q in ids:union|=bits[q]
    assert union==allpairs

checked3r=0
for a,b,c in itertools.combinations(R,3):
    pre=bits[a]|bits[b]|bits[c]
    for t in T:
        assert (pre|bits[t])!=allpairs
        checked3r+=1
assert checked3r==13720896
checked4r=0
for a,b,c,d in itertools.combinations(R,4):
    assert (bits[a]|bits[b]|bits[c]|bits[d])!=allpairs
    checked4r+=1
assert checked4r==1929501

bad={}
for q in range(228):
    for s in parts(q,FULLSTATE):
        if len(s)>1 and not any(len(parts(r,s))==len(s) for r in range(228)):
            bad[q]=s
            break
assert len(bad)==228

# A sharp root floor of 4 permits asking a root query only while one or
# both *complete* unresolved terminal-indistinguishable pairs remain.
special={frozenset(P),frozenset(Q),frozenset(P+Q)}
root_splitters=[
    q for q in R
    if V[q][P[0]]!=V[q][P[1]]
    and V[q][Q[0]]!=V[q][Q[1]]
]
assert root_splitters==list(range(148,164))

def optimal(weights_vector):
    @lru_cache(None)
    def dp(S,depth):
        if len(S)==1:return (0,None)
        if depth==0:return None
        queries=tuple(T)+(tuple(root_splitters)
                           if frozenset(S) in special else ())
        best=None
        for q in queries:
            sub=parts(q,S)
            if len(sub)<2:continue
            value=sum(weights_vector[i] for i in S) if q<144 else 0
            for s in sub:
                v=dp(s,depth-1)
                if v is None:break
                value+=v[0]
            else:
                if best is None or value<best[0]:
                    best=(value,q)
        return best
    solution=dp(FULLSTATE,3)
    assert solution is not None
    def build(S,d):
        if len(S)==1:return {"leaf":S[0]}
        q=dp(S,d)[1]
        return {"q":q,"children":{
            str(V[q][g[0]]):build(g,d-1) for g in parts(q,S)
        }}
    tree=build(FULLSTATE,3)
    score=[0,0,0,0]
    for i in FULLSTATE:
        node=tree
        depth=0
        while "leaf" not in node:
            q=node["q"]
            depth+=1
            assert depth<=3
            if q<144:
                score[0]+=1
                score[1]+=weights[i]
            else:
                score[2]+=1
                score[3]+=weights[i]
            node=node["children"][str(V[q][i])]
        assert node["leaf"]==i
    assert score[2:]==[4,4]
    return solution[0],tree,tuple(score)

uval,utree,ustats=optimal([1]*141)
mval,mtree,mstats=optimal(weights)
assert uval==296 and mval==688
assert ustats[0]==296 and mstats[1]==688

# Select a lambda=0 minimizer with multiplicity tie break.
aval,atree,astats=optimal([1000000+mi for mi in weights])
# Select a lambda=1 minimizer with named-count tie break.
bval,btree,bstats=optimal([1000000*mi+1 for mi in weights])
assert astats==(296,707,4,4)
assert bstats==(298,688,4,4)

# Exact mixed-prior endpoint at beta=620/3299; no floating-point inputs.
a=310*(3299-620)
b=141*620
beta_value,_,_=optimal([a+b*mi for mi in weights])
assert beta_value==a*296+b*707==a*298+b*688==307630980
assert 2*(3299-620)*310==19*620*141

print("PASS all 1,949,476 mixed triples and both exact four-query witnesses")
print("PASS all 13,720,896 three-root/four-query and 1,929,501 four-root palettes")
print("PASS depth-two obstruction for all 228 first physical queries")
print("PASS native adaptive depth 3, exact minimal root mass 4")
print("PASS U_T=296, M_T=688 endpoint minima")
print("PASS full mixture interval: 620/3299, A=(296,707), B=(298,688)")
print("PASS original frozen input SHA256 and all 141-state A/B tree replays")
