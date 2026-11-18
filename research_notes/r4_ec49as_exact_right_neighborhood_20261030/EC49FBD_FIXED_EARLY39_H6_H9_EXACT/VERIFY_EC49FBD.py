#!/usr/bin/env python3
"""EC49FBD: self-contained exact native signed-X6 BRC H6--H9 optimization."""
import itertools, json
from collections import Counter
OPS = {'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ORDER='acdefg'
T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],
   [3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],
   [6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]]
S=[0,0,4,1,16,32,8,2,0]
EARLY={2:['de','ec','fe'],3:['feg','gef'],4:['fegg','gefg'],5:['feggg','gefgg']}
WITNESS={6:['ecgcfc','fegccc','fegddd','gefddd'],
         7:['ecgcffg','fegccfg','fegddgf','gefddgf'],
         8:['fegggffc','fegggffd','gefggffc','gefggffd'],
         9:['fegggffgf','gefggffgf']}
KEY=(6,4,1,0,0,0); TARGET=(2,0,0,0,0,0)
def native(w): return tuple(n for a in w for n in OPS[a])
def read(w):
    p=native(w); k=[0]*6; d=[0]*6; state=0
    for n in p:
        a=abs(n)-1;d[a]+=1 if n>0 else -1
        if n>0:k[a]+=1
    for a in w:state=T[state][ORDER.index(a)]
    return tuple(k),tuple(d),S[state]
def edge_set(ws):
    return {native(w)[:i] for w in ws for i in range(1,len(native(w))+1)}
words={}; hist={}
for h in range(6,10):
    mult='e'+'c'*(9-h)+'f'*(h-5)+'g'*(h-5)
    # enumerate all binary c/d choices, all letter orderings, retaining native histories
    found={}
    for cd in itertools.product('cd', repeat=9-h):
        letters='e'+''.join(cd)+'f'*(h-5)+'g'*(h-5)
        for perm in set(itertools.permutations(letters)):
            w=''.join(perm);k,d,s=read(w)
            if k==KEY and d==TARGET and s:found[w]=s
    words[h]=found;hist[h]=dict(sorted(Counter(found.values()).items()))
assert tuple(len(words[h]) for h in range(6,10))==(240,1260,2240,560)
# every allowed H6--H8 signature is individually necessary; H9 needs E and F.
bit={h:{s:1<<((h-6)*4+i) for i,s in enumerate((1,2,4,8))}
     for h in range(6,9)}
bit[9]={16:1<<12,32:1<<13}
N=[{'children':{},'mask':0,'free':False}]
def insert(p,flag=0,free=False):
    u=0
    for n in p:
        children=N[u]['children']
        if n not in children:
            children[n]=len(N);N.append({'children':{},'mask':0,'free':False})
        u=children[n]
        if free:N[u]['free']=True
    N[u]['mask'] |=flag
for ws in EARLY.values():
    for w in ws:insert(native(w),free=True)
assert sum(n['free'] for n in N)==39
for h in range(6,10):
    for w,s in words[h].items():insert(native(w),flag=bit[h][s])
assert len(N)==26705
# Exact unpruned integer min-plus OR recurrence on signed-native prefix trie.
DP=[None]*len(N);joins=0
for u in range(len(N)-1,-1,-1):
    node=N[u];dp={0:0}
    if node['mask']:dp[node['mask']]=0
    for v in node['children'].values():
        nxt={}
        for a,ca in dp.items():
            for b,cb in DP[v].items():
                m=a|b;c=ca+cb;joins+=1
                if c<nxt.get(m,10**9):nxt[m]=c
        dp=nxt
    if u and not node['free']:
        dp={m:c+(m!=0) for m,c in dp.items()}
    DP[u]=dp
minimum=39+DP[0][(1<<14)-1]
assert minimum==127
allws={**EARLY,**WITNESS}
seen=set();cumulative={};keys=set();masks={}
for h in range(2,10):
    m=0
    for w in allws[h]:
        k,d,s=read(w);assert d==TARGET and s
        keys.add(k);m|=s
    seen |=edge_set(allws[h]);cumulative[h]=len(seen);masks[h]=m
    assert (m&18) and (m&20) and (m&33) and (m&40)
assert len(keys)==5 and cumulative=={2:22,3:31,4:35,5:39,6:85,7:97,8:121,9:127}
assert len(seen)==minimum
print(json.dumps({'schema':'EC49FBD_EXACT_OR_MASK_DP','frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'legal_candidate_count':{str(h):len(words[h]) for h in words},
 'signature_histogram':{str(h):hist[h] for h in hist},'signed_prefix_nodes':len(N),
 'unpruned_transitions':joins,'min_added_edges':minimum-39,'min_total_edges':minimum,
 'cumulative_witness_edges':cumulative,'witness_signatures':masks,
 'full_witness':allws,'result':'PASS'},indent=2,ensure_ascii=False))
