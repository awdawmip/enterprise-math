#!/usr/bin/env python3
"""Exact native signed X6 trie Steiner DP for H4/H5 low-signature demand family.
Scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab;
original BRC_ORIGINAL_MODEL_EC49FFJ.py Git blob 6350340fbe869f17b5a50bd1ba30640db44a3a99.
"""
from collections import Counter
import json
ORDER='acdefg'
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIGNATURE=(0,0,4,1,16,32,8,2,0)
SIG=(1,2,4,8)
HORIZONS=(4,5)
DEMANDS=tuple((h,s) for h in HORIZONS for s in SIG)
M=len(DEMANDS); ALL=(1<<M)-1
INF=10**10

def native(word):
    return tuple(step for op in word for step in OPS[op])
def observed(word):
    state=0
    for c in word: state=T[state][ORDER.index(c)]
    return SIGNATURE[state]
def candidates(h,key):
    x,y,z=key; ct=[z-1,0,0,z,h+1-y-2*z,h+1-x]; cd=x+y-h-1
    assert min(ct)>=0 and cd>=1
    for c in range(cd+1):
        ct[1]=c;ct[2]=cd-c
        def rec(prefix,state):
            if not any(ct):
                yield prefix,SIGNATURE[state]
                return
            for i,num in enumerate(ct):
                if num:
                    ct[i]-=1
                    yield from rec(prefix+ORDER[i],T[state][i])
                    ct[i]+=1
        yield from rec('',0)
def keys(h):
    for z in range(1,(h+1)//2+1):
        for x in range(2*z,h+2):
            for y in range(h+2-2*z):
                if x+y-h-1>=1 and h+1-y-2*z>=0 and h+1-x>=0:
                    yield (x,y,z)

def run():
    children=[{}];terminal=[0];labels=[{}];total=Counter();key_counts={}
    for h in HORIZONS:
        kk=list(keys(h));key_counts[str(h)]=len(kk)
        for key in kk:
            for word,sig in candidates(h,key):
                if sig not in SIG: continue
                assert observed(word)==sig
                axis=native(word)
                assert len(axis)==2*(sum(key)-1)
                count=Counter(axis)
                assert tuple(count[i]-count[-i] for i in range(1,7))==(2,0,0,0,0,0)
                assert tuple(count[i] for i in (1,2,3))==key
                total[h]+=1
                p=0
                for a in axis:
                    nxt=children[p].get(a)
                    if nxt is None:
                        nxt=len(children);children[p][a]=nxt
                        children.append({});terminal.append(0);labels.append({})
                    p=nxt
                bit=1<<DEMANDS.index((h,sig))
                terminal[p]|=bit;labels[p][bit]=(h,sig,key,word)
    dp=[None]*len(children)
    def merge(d,e):
        out=d.copy()
        for a,ca in d.items():
            for b,cb in e.items():
                if not(a&b):
                    v=ca+cb+(1 if b else 0)
                    if v<out.get(a|b,INF):out[a|b]=v
        return out
    for u in range(len(children)-1,-1,-1):
        mask=terminal[u]; d={0:0};sub=mask
        while sub:d[sub]=0;sub=(sub-1)&mask
        for v in children[u].values():d=merge(d,dp[v])
        dp[u]=d
    cost=dp[0][ALL]
    chosen=[]
    def recover(u,want):
        vs=list(children[u].values())
        mask=terminal[u];d={0:0};sub=mask
        while sub:d[sub]=0;sub=(sub-1)&mask
        prefix=[d]
        for v in vs:
            d=merge(d,dp[v]);prefix.append(d)
        assert d[want]==dp[u][want]
        rest=want
        for i in range(len(vs)-1,-1,-1):
            v=vs[i];pick=None
            for b,cb in dp[v].items():
                if b&rest!=b:continue
                a=rest^b
                if a in prefix[i] and prefix[i][a]+cb+(1 if b else 0)==prefix[i+1][rest]:
                    pick=b;break
            assert pick is not None
            if pick:recover(v,pick)
            rest^=pick
        assert rest&~mask==0
        for i in range(M):
            bit=1<<i
            if rest&bit:chosen.append(labels[u][bit])
    recover(0,ALL)
    assert len(chosen)==M
    native_prefixes=set()
    for h,s,key,word in chosen:
        axis=native(word)
        native_prefixes.update(axis[:d] for d in range(1,len(axis)+1))
    assert len(native_prefixes)==cost
    report={'schema':'EC49FFO_EXACT_CROSS_WINDOW_V1',
      'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'status':'EXACT_INTEGER_TRIE_DP_PASS','key_configurations':key_counts,
      'candidate_word_counts':{str(h):total[h] for h in HORIZONS},
      'native_trie_nodes_including_root':len(children),
      'optimal_cost_unrestricted_key_count':cost,
      'witness_distinct_key_count':len(set(k for h,s,k,w in chosen)),
      'witness':[{'h':h,'signature':s,'key':list(k),'word':w} for h,s,k,w in chosen]}
    assert key_counts=={'4':7,'5':13}
    assert total[4]==176 and total[5]==950
    assert len(children)==4903 and cost==40
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
