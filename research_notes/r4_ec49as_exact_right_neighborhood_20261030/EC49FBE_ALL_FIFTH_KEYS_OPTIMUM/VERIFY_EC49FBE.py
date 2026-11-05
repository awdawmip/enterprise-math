#!/usr/bin/env python3
"""EC49FBE: all fifth-key exact signed-X6 BRC finite optimization (standard library)."""
import itertools,json
from collections import Counter,defaultdict
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
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
TARGET=(2,0,0,0,0,0)
def native(w):return tuple(n for c in w for n in OPS[c])
def read(w):
    pos=[0]*6;delta=[0]*6;s=0
    for n in native(w):
        i=abs(n)-1;delta[i]+=1 if n>0 else -1
        if n>0:pos[i]+=1
    for c in w:s=T[s][ORDER.index(c)]
    return tuple(pos),tuple(delta),S[s]
def rank9(mask):return all(mask&v for v in (18,20,33,40))
def signature_clause_mask(s):return sum(1<<i for i,v in enumerate((18,20,33,40)) if s&v)
# Independent count-state DFA: a,e,r=c+d,f,g,observer; handles all words
# without enumerating length-nine sequences or discarding the observer.
state={(0,0,0,0,0,0):1}; signatures={}
for h in range(1,10):
    nxt=defaultdict(int)
    for (a,e,r,f,g,s),n in state.items():
        for c in ORDER:
            da,de,dr,df,dg={'a':(1,0,0,0,0),'c':(0,0,1,0,0),
                           'd':(0,0,1,0,0),'e':(0,1,0,0,0),
                           'f':(0,0,0,1,0),'g':(0,0,0,0,1)}[c]
            nxt[(a+da,e+de,r+dr,f+df,g+dg,T[s][ORDER.index(c)])]+=n
    state=nxt
    if h in (6,7,8,9):
        sig=defaultdict(int)
        for (a,e,r,f,g,s),n in state.items():
            if e==a+1 and S[s]:
                key=(r+2*e+f,r+g,e)
                sig[key]|=S[s]
        signatures[h]=dict(sig)
common=set(signatures[6])
for h in (7,8,9):common &= set(signatures[h])
keys=sorted(k for k in common if all(rank9(signatures[h][k]) for h in (6,7,8,9)))
assert keys==[(5,5,1),(6,4,1),(6,5,1),(7,3,1),(7,3,2),(7,4,1),(7,5,1)]
# Exact native-word enumerator, including every possible c/d ordering.
def candidates(K,h):
    x,y,z=K;a=z-1;e=z;r=x+y-h-1;f=h+1-y-2*z;g=h+1-x
    if min(a,e,r,f,g)<0:return {}
    found={}
    for cd in itertools.product('cd',repeat=r):
        letters='a'*a+'e'*e+''.join(cd)+'f'*f+'g'*g
        for perm in sorted(set(itertools.permutations(letters))):
            w=''.join(perm);key,delta,s=read(w)
            assert key[:3]==K and delta==TARGET
            if s:found[w]=s
    return found
def edge_set(words):
    return {native(w)[:i] for w in words for i in range(1,len(native(w))+1)}
def optimum(K):
    N=[{'ch':{},'free':False,'mask':0}]
    def insert(w,free=False,mask=0):
        u=0
        for step in native(w):
            ch=N[u]['ch']
            if step not in ch:
                ch[step]=len(N);N.append({'ch':{},'free':False,'mask':0})
            u=ch[step]
            if free:N[u]['free']=True
        N[u]['mask'] |=mask
    for ws in EARLY.values():
        for w in ws:insert(w,free=True)
    assert sum(v['free'] for v in N)==39
    count=[];hist=[]
    for h in (6,7,8,9):
        words=candidates(K,h);count.append(len(words));hist.append(dict(sorted(Counter(words.values()).items())))
        for w,s in words.items():insert(w,mask=signature_clause_mask(s)<<(4*(h-6)))
    # No subset-pruning, no random sampling; every legal trie path is present.
    dp=[None]*len(N);joins=0
    for u in range(len(N)-1,-1,-1):
        node=N[u];state={0:0}
        if node['mask']:state[node['mask']]=0
        for v in node['ch'].values():
            merged={}
            for a,ca in state.items():
                for b,cb in dp[v].items():
                    m=a|b;cost=ca+cb;joins+=1
                    if cost<merged.get(m,10**9):merged[m]=cost
            state=merged
        if u and not node['free']:
            state={m:c+int(m!=0) for m,c in state.items()}
        dp[u]=state
    return {'key':K,'candidate_counts':count,'signature_histograms':hist,
            'native_trie_nodes':len(N),'min_plus_pairs':joins,
            'total_native_edges':39+dp[0][65535]}
results=[optimum(key) for key in keys]
assert [r['total_native_edges'] for r in results]==[140,127,166,135,154,162,182]
# Explicit attainment for the globally lowest fifth-key family.
selected={**EARLY,**WITNESS};seen=set();cumulative={};allkeys=set()
for h in range(2,10):
    m=0
    for w in selected[h]:
        k,d,s=read(w)
        assert d==TARGET and s
        allkeys.add(k);m |=s
    assert rank9(m)
    seen |=edge_set(selected[h]);cumulative[h]=len(seen)
assert len(allkeys)==5 and cumulative=={2:22,3:31,4:35,5:39,6:85,7:97,8:121,9:127}
print(json.dumps({'schema':'EC49FBE_ALL_FIFTH_KEYS_EXACT','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'rank_possible_key_counts':{str(h):sum(rank9(m) for m in signatures[h].values()) for h in (6,7,8,9)},
 'common_rank_feasible_keys':keys,'exact_key_results':results,
 'best_key':(6,4,1),'global_fixed_early_minimum':127,
 'cumulative_attaining_edges':cumulative,'attaining_witness':selected,'status':'PASS'},indent=2,ensure_ascii=False))
